"""Chunked ElevenLabs TTS with word-level sync timestamps and delta regen.

Splits the script into sentence-sized chunks, calls ElevenLabs once per chunk,
concatenates the resulting PCM frames bit-perfectly (pure Python via the
``wave`` module — no ffmpeg dependency), and merges the per-chunk word lists
into one continuous timeline.

Why chunking: editing one sentence in script.txt should not cost a full
re-TTS. Each chunk's text is hashed (SHA-256) and stored in
``transcript-history.json``; on the next run, only changed chunks re-hit the
ElevenLabs API. The unchanged chunks' WAV files are reused as-is.

Why a 650ms silence between chunks: ElevenLabs inserts natural sentence-
boundary pauses when processing longer text in a single call. Splitting the
text into multiple calls strips those pauses. 650ms restores them — the value
is calibrated empirically on the source project (79.595s reference single-
call duration vs 79.778s merged across 11 chunks, drift < 200ms).

Used by ``scripts/elevenlabs-tts.py``. The CLI owns ``[SCENE:]`` stripping,
``.env`` parsing, and pronunciation-dictionary plumbing; this module owns
the TTS pipeline and audio/sync stitching.
"""
from __future__ import annotations

import base64
import hashlib
import json
import re
import wave
from pathlib import Path

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs


# ---------------------------------------------------------------------------
# Sentence splitter
# ---------------------------------------------------------------------------

# Abbreviations whose trailing '.' does NOT end a sentence. Surface forms only.
_ABBREVIATIONS = {
    "Dr.", "Mr.", "Mrs.", "Ms.", "Jr.", "Sr.", "St.",
    "e.g.", "i.e.", "etc.", "vs.", "viz.", "cf.",
    "U.S.", "U.K.", "E.U.", "A.I.", "N.B.",
    "a.m.", "p.m.", "A.M.", "P.M.",
    "Inc.", "Ltd.", "Co.", "Corp.",
    "No.", "Vol.", "Ch.", "pp.", "ed.", "approx.",
}

_SENTENCE_BOUNDARY = re.compile(r'(?<=[.!?])(\s+)(?=[A-Z0-9"\'])')
_SECONDARY_BOUNDARY = re.compile(r'(?<=[;:])\s+')


def split_into_chunks(text: str, min_chars: int = 10, max_chars: int = 400) -> list[str]:
    """Split text into sentence-sized chunks for per-chunk TTS generation.

    One-sentence-per-chunk is the default. Sentences shorter than
    ``min_chars`` (very short fragments like "OK.", "Six.") merge forward
    because TTS prosody degrades on tiny fragments. Sentences longer than
    ``max_chars`` split on ``;`` or ``:`` to keep per-chunk regen cheap.
    Abbreviations from ``_ABBREVIATIONS`` are protected from false splits.

    Default ``min_chars=10`` (was 40 pre-2026-05-19): the 40-char threshold
    grouped many natural sentence breaks into single chunks, which made
    ElevenLabs read them back-to-back with no breath between periods.
    Lowering to 10 keeps tiny fragments grouped (they still need prosody
    context) but lets natural sentence boundaries become chunk boundaries
    where the fixed inter-chunk silence applies. Pair with
    ``DEFAULT_INTER_CHUNK_SILENCE_MS=380`` for natural sentence-end breath.
    """
    sentinel = "\x00"
    protected = text
    for abbrev in _ABBREVIATIONS:
        protected = protected.replace(abbrev, abbrev.replace(".", sentinel))

    parts = _SENTENCE_BOUNDARY.split(protected)
    sentences: list[str] = []
    i = 0
    while i < len(parts):
        s = parts[i].replace(sentinel, ".").strip()
        if s:
            sentences.append(s)
        # split() captures the whitespace at odd indices — skip it.
        i += 2

    merged: list[str] = []
    buffer = ""
    for s in sentences:
        if not buffer:
            buffer = s
            continue
        if len(buffer) < min_chars:
            buffer = buffer + " " + s
        else:
            merged.append(buffer)
            buffer = s
    if buffer:
        merged.append(buffer)

    final: list[str] = []
    for s in merged:
        if len(s) <= max_chars:
            final.append(s)
            continue
        sub_parts = _SECONDARY_BOUNDARY.split(s)
        running = ""
        for sub in sub_parts:
            sub = sub.strip()
            if not sub:
                continue
            candidate = (running + " " + sub).strip() if running else sub
            if len(candidate) <= max_chars or not running:
                running = candidate
            else:
                final.append(running)
                running = sub
        if running:
            final.append(running)

    return final


def compute_checksum(text: str) -> str:
    """SHA-256 of whitespace-normalized text. Used as the delta-regen key."""
    normalized = " ".join(text.split())
    return "sha256:" + hashlib.sha256(normalized.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Sync data cleanup
# ---------------------------------------------------------------------------


def clean_sync_data(words_data: list[dict]) -> list[dict]:
    """Strip SSML tag artifacts from word timestamps and tighten boundaries.

    Fixes three problems ElevenLabs alignment can introduce:
    1. Ghost words like "<break" or 'time="0.4s"/>' (SSML fragments).
    2. Combined leakage like "choices:<break" (text merged with SSML).
    3. End times that exceed the next word's start (causes scrub overlap).
    """
    cleaned: list[dict] = []
    for entry in words_data:
        word = entry["word"]
        clean_word = re.sub(r'<break[^>]*>?', '', word)
        clean_word = re.sub(r'time="[^"]*"\s*/?>', '', clean_word)
        clean_word = re.sub(r'/>', '', clean_word)
        clean_word = clean_word.strip().strip('\n')
        if not clean_word:
            continue
        cleaned.append({
            "word": clean_word,
            "start": entry["start"],
            "end": entry["end"],
        })

    for i in range(len(cleaned) - 1):
        if cleaned[i]["end"] > cleaned[i + 1]["start"]:
            cleaned[i]["end"] = cleaned[i + 1]["start"]

    return cleaned


# ---------------------------------------------------------------------------
# Audio I/O
# ---------------------------------------------------------------------------

# Inter-chunk silence in milliseconds. Calibrated against single-call ElevenLabs
# output — see module docstring. Lowered from 650 → 380 (2026-05-19) to match
# the new one-sentence-per-chunk default (split_into_chunks min_chars=10). The
# old 650ms value made paragraph-level breaks land at every sentence boundary
# under the new chunking and sounded draggy; 380ms = natural sentence-end breath.
DEFAULT_INTER_CHUNK_SILENCE_MS = 380

# ElevenLabs output format → PCM sample rate mapping. The Pro-tier-only
# pcm_44100 default stays backwards-compatible; per-creator .env files can opt
# down to pcm_24000 / pcm_22050 / pcm_16000 (Creator tier) by setting
# ELEVENLABS_OUTPUT_FORMAT.
DEFAULT_OUTPUT_FORMAT = "pcm_44100"
SUPPORTED_OUTPUT_FORMATS: dict[str, int] = {
    "pcm_44100": 44100,  # Pro tier
    "pcm_24000": 24000,  # Creator tier
    "pcm_22050": 22050,  # Creator tier
    "pcm_16000": 16000,  # Creator tier
}


def output_format_to_rate(output_format: str) -> int:
    """Resolve a supported ``output_format`` string to its sample rate in Hz."""
    try:
        return SUPPORTED_OUTPUT_FORMATS[output_format]
    except KeyError:
        raise ValueError(
            f"Unsupported ELEVENLABS_OUTPUT_FORMAT={output_format!r}. "
            f"Supported PCM formats: {sorted(SUPPORTED_OUTPUT_FORMATS)}"
        ) from None


def get_wav_duration(wav_path: str) -> float:
    """Read exact WAV duration in seconds via the standard library.

    Reading container duration (rather than ``words[-1]['end']``) avoids drift
    from trailing silence the alignment data does not cover.
    """
    with wave.open(wav_path, "rb") as w:
        frames = w.getnframes()
        rate = w.getframerate()
    return frames / float(rate)


def write_pcm_as_wav(pcm_bytes: bytes, out_path: str, *, sample_rate: int = 44100) -> None:
    """Wrap raw 16-bit signed PCM mono in a WAV container at ``sample_rate``."""
    with wave.open(out_path, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(pcm_bytes)


def _read_pcm_frames(wav_path: str, *, expected_rate: int = 44100) -> bytes:
    """Read raw PCM frames from a WAV file, asserting expected codec params.

    All inputs MUST be 16-bit signed PCM mono at ``expected_rate`` — the
    format ElevenLabs returns for the matching ``output_format`` and what
    ``write_pcm_as_wav`` writes. Mismatched params would silently produce
    garbled audio under raw concat, so we assert loudly instead.
    """
    with wave.open(wav_path, "rb") as w:
        if (w.getnchannels(), w.getsampwidth(), w.getframerate()) != (1, 2, expected_rate):
            raise ValueError(
                f"{wav_path} has unexpected WAV params "
                f"(channels={w.getnchannels()}, sampwidth={w.getsampwidth()}, "
                f"rate={w.getframerate()}). Expected mono 16-bit @ {expected_rate}Hz."
            )
        return w.readframes(w.getnframes())


def concat_wavs(
    chunk_paths: list[str],
    output_path: str,
    inter_chunk_silence_ms: int = 0,
    *,
    sample_rate: int = 44100,
) -> None:
    """Concatenate WAV chunks losslessly via raw PCM frame concatenation.

    All inputs are 16-bit signed PCM mono at ``sample_rate``, so we read each
    file's PCM frames, optionally splice in ``inter_chunk_silence_ms`` of
    zero-bytes between chunks, and write a single new WAV. Bit-perfect by
    construction — no encoding, no ffmpeg dependency. The python ``wave``
    module handles the RIFF header parse/write.
    """
    silence_frames = b""
    if inter_chunk_silence_ms > 0:
        num_frames = int(round(sample_rate * inter_chunk_silence_ms / 1000.0))
        silence_frames = b"\x00\x00" * num_frames

    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    pcm_parts: list[bytes] = []
    for i, p in enumerate(chunk_paths):
        if i > 0 and silence_frames:
            pcm_parts.append(silence_frames)
        pcm_parts.append(_read_pcm_frames(p, expected_rate=sample_rate))

    write_pcm_as_wav(b"".join(pcm_parts), output_path, sample_rate=sample_rate)


def merge_chunk_syncs(
    chunks_data: list[dict],
    inter_chunk_silence_ms: int = 0,
) -> list[dict]:
    """Merge per-chunk word lists into a single continuous timeline.

    Each entry in ``chunks_data`` must supply:
      - ``words``: list of {word, start, end} from the per-chunk TTS call
      - ``duration``: actual WAV duration in seconds (from ``get_wav_duration``)

    ``inter_chunk_silence_ms`` MUST match the value passed to ``concat_wavs``
    for the same generation — otherwise word timestamps drift out of sync.
    """
    silence_seconds = inter_chunk_silence_ms / 1000.0
    merged: list[dict] = []
    cursor = 0.0
    for idx, ch in enumerate(chunks_data):
        if idx > 0:
            cursor += silence_seconds
        for w in ch["words"]:
            merged.append({
                "word": w["word"],
                "start": w["start"] + cursor,
                "end": w["end"] + cursor,
            })
        cursor += ch["duration"]

    for i in range(len(merged) - 1):
        if merged[i]["end"] > merged[i + 1]["start"]:
            merged[i]["end"] = merged[i + 1]["start"]

    return merged


# ---------------------------------------------------------------------------
# ElevenLabs TTS
# ---------------------------------------------------------------------------


def generate_chunk(
    *,
    client: ElevenLabs,
    text: str,
    voice_id: str,
    model_id: str,
    voice_settings: VoiceSettings,
    pronunciation_dictionary_locators: list[dict] | None = None,
    output_format: str = DEFAULT_OUTPUT_FORMAT,
) -> tuple[bytes, list[dict]]:
    """Generate audio for a single chunk and return raw PCM bytes + words.

    Uses ``convert_with_timestamps`` (not streaming) — sentences are 40-400
    chars, so streaming buys nothing. The caller is responsible for writing
    the WAV (via ``write_pcm_as_wav``) and the per-chunk sync JSON. Default
    ``output_format`` is Pro-tier ``pcm_44100``; pass ``pcm_24000`` etc. to
    stay within Creator-tier limits.
    """
    resp = client.text_to_speech.convert_with_timestamps(
        voice_id=voice_id,
        text=text,
        model_id=model_id,
        output_format=output_format,
        voice_settings=voice_settings,
        pronunciation_dictionary_locators=pronunciation_dictionary_locators,
    )
    pcm_bytes = base64.b64decode(resp.audio_base_64)

    align = resp.normalized_alignment or resp.alignment
    words: list[dict] = []
    current: dict | None = None
    for ch, t0, t1 in zip(
        align.characters,
        align.character_start_times_seconds,
        align.character_end_times_seconds,
    ):
        if ch.isspace():
            if current is not None:
                words.append(current)
                current = None
        else:
            if current is None:
                current = {"word": ch, "start": float(t0), "end": float(t1)}
            else:
                current["word"] += ch
                current["end"] = float(t1)
    if current is not None:
        words.append(current)

    return pcm_bytes, clean_sync_data(words)


# ---------------------------------------------------------------------------
# Chunked generation + delta regen
# ---------------------------------------------------------------------------


HISTORY_FILENAME = "transcript-history.json"
CHUNKS_DIRNAME = "narration-chunks"


def chunks_dir_for(narration_wav: Path) -> Path:
    """``audio/narration.wav`` → ``audio/narration-chunks/``."""
    return narration_wav.parent / CHUNKS_DIRNAME


def history_path_for(transcript_json: Path) -> Path:
    """``transcript.json`` → ``transcript-history.json`` (sibling)."""
    return transcript_json.parent / HISTORY_FILENAME


def load_history(history_path: Path) -> dict | None:
    if not history_path.exists():
        return None
    with open(history_path, "r", encoding="utf-8") as f:
        return json.load(f)


def diff_chunks(
    new_chunks: list[str],
    history: dict | None,
) -> tuple[list[int], list[int]]:
    """Return (changed_indices, unchanged_indices) for ``new_chunks``.

    Indices that are ``> len(history.chunks)`` are always changed (new
    chunks). When the history's chunk count exceeds the new count, those
    extra entries silently fall off — they'll be cleaned up at write time.
    """
    if history is None:
        return list(range(len(new_chunks))), []

    old_checksums = [c["checksum"] for c in history.get("chunks", [])]
    changed: list[int] = []
    unchanged: list[int] = []
    for i, text in enumerate(new_chunks):
        if i < len(old_checksums) and compute_checksum(text) == old_checksums[i]:
            unchanged.append(i)
        else:
            changed.append(i)
    return changed, unchanged


def generate_chunked(
    *,
    text: str,
    narration_wav: Path,
    transcript_json: Path,
    client: ElevenLabs,
    voice_id: str,
    model_id: str,
    voice_settings: VoiceSettings,
    pronunciation_dictionary_locators: list[dict] | None = None,
    inter_chunk_silence_ms: int = DEFAULT_INTER_CHUNK_SILENCE_MS,
    force: bool = False,
    log: callable = print,
    output_format: str = DEFAULT_OUTPUT_FORMAT,
    min_chunk_chars: int = 10,
) -> dict:
    """Full chunked-generation pipeline with auto-detect delta regen.

    Returns a summary dict: ``{chunks: int, changed: int, unchanged: int,
    duration_s: float, words: int}``.

    On the first run (no history), generates every chunk. On subsequent runs,
    diffs the new chunks' checksums against ``transcript-history.json`` and
    only re-hits the ElevenLabs API for changed chunks. Unchanged chunks
    reuse their existing WAV file and per-chunk sync JSON.

    With ``force=True``, always regenerates every chunk regardless of
    history.
    """
    sample_rate = output_format_to_rate(output_format)
    chunks_dir = chunks_dir_for(narration_wav)
    chunks_dir.mkdir(parents=True, exist_ok=True)
    history_path = history_path_for(transcript_json)

    new_chunks = split_into_chunks(text, min_chars=min_chunk_chars)
    if not new_chunks:
        raise ValueError("split_into_chunks returned no chunks for input text")

    history = None if force else load_history(history_path)
    # If the previous run used a different output_format, the cached chunk WAVs
    # are at a different sample rate and cannot be safely concatenated. Force
    # full regen rather than tripping the _read_pcm_frames assertion.
    if history is not None and history.get("output_format", DEFAULT_OUTPUT_FORMAT) != output_format:
        log(f"[tts] output_format changed "
            f"({history.get('output_format', DEFAULT_OUTPUT_FORMAT)} → {output_format}) "
            f"— forcing full regen")
        history = None
    changed, unchanged = diff_chunks(new_chunks, history)
    if force:
        changed = list(range(len(new_chunks)))
        unchanged = []

    log(f"[tts] {len(new_chunks)} chunks total — {len(changed)} changed, "
        f"{len(unchanged)} unchanged")

    chunks_data: list[dict] = []
    history_entries: list[dict] = []

    for i, chunk_text in enumerate(new_chunks):
        chunk_wav = chunks_dir / f"chunk-{i:02d}.wav"
        chunk_sync = chunks_dir / f"chunk-{i:02d}-sync.json"

        if i in unchanged and chunk_wav.exists() and chunk_sync.exists():
            with open(chunk_sync, "r", encoding="utf-8") as f:
                words = json.load(f)["words"]
            duration = get_wav_duration(str(chunk_wav))
            log(f"[tts]   chunk {i:02d} — reused ({duration:.2f}s, {len(words)} words)")
        else:
            log(f"[tts]   chunk {i:02d} — generating ({len(chunk_text)} chars)")
            pcm_bytes, words = generate_chunk(
                client=client,
                text=chunk_text,
                voice_id=voice_id,
                model_id=model_id,
                voice_settings=voice_settings,
                pronunciation_dictionary_locators=pronunciation_dictionary_locators,
                output_format=output_format,
            )
            write_pcm_as_wav(pcm_bytes, str(chunk_wav), sample_rate=sample_rate)
            with open(chunk_sync, "w", encoding="utf-8") as f:
                json.dump({"words": words}, f, indent=2)
            duration = get_wav_duration(str(chunk_wav))

        chunks_data.append({"words": words, "duration": duration})
        history_entries.append({
            "index": i,
            "text": chunk_text,
            "checksum": compute_checksum(chunk_text),
            "wav": f"chunk-{i:02d}.wav",
            "duration": duration,
            "word_count": len(words),
        })

    _prune_stale_chunks(chunks_dir, kept=len(new_chunks))

    cursor = 0
    for entry in history_entries:
        entry["words_offset"] = cursor
        cursor += entry["word_count"]

    chunk_paths = [str(chunks_dir / f"chunk-{i:02d}.wav") for i in range(len(new_chunks))]
    concat_wavs(
        chunk_paths,
        str(narration_wav),
        inter_chunk_silence_ms=inter_chunk_silence_ms,
        sample_rate=sample_rate,
    )

    merged_words = merge_chunk_syncs(
        chunks_data,
        inter_chunk_silence_ms=inter_chunk_silence_ms,
    )

    transcript_json.parent.mkdir(parents=True, exist_ok=True)
    with open(transcript_json, "w", encoding="utf-8") as f:
        json.dump(merged_words, f, ensure_ascii=False, indent=2)

    bundle = {
        "voice_id": voice_id,
        "model_id": model_id,
        "voice_settings": {
            "stability": voice_settings.stability,
            "similarity_boost": voice_settings.similarity_boost,
            "style": voice_settings.style,
            "speed": voice_settings.speed,
            "use_speaker_boost": voice_settings.use_speaker_boost,
        },
        "pronunciation_dictionary_locators": pronunciation_dictionary_locators or [],
        "inter_chunk_silence_ms": inter_chunk_silence_ms,
        "output_format": output_format,
        "chunks": history_entries,
    }
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)

    total_duration = get_wav_duration(str(narration_wav))
    return {
        "chunks": len(new_chunks),
        "changed": len(changed),
        "unchanged": len(unchanged),
        "duration_s": total_duration,
        "words": len(merged_words),
    }


def _prune_stale_chunks(chunks_dir: Path, *, kept: int) -> None:
    """Delete chunk-NN.* artifacts where NN >= ``kept``.

    Without this, shrinking a script (e.g. removing a paragraph) leaves
    orphaned ``chunk-11.wav`` files that would silently get included in a
    future glob. The concat list is built from ``range(kept)`` so they
    wouldn't be played, but the cleanup keeps the directory honest.
    """
    if not chunks_dir.exists():
        return
    for entry in chunks_dir.iterdir():
        m = re.match(r"chunk-(\d+)(?:-sync\.json|\.wav)$", entry.name)
        if not m:
            continue
        if int(m.group(1)) >= kept:
            try:
                entry.unlink()
            except OSError:
                pass
