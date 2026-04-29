"""Generate ElevenLabs TTS for a HyperFrames video using project .env defaults.

Usage:
  python scripts/elevenlabs-tts.py <project_dir> [--shorts]

Reads <project_dir>/script.txt, writes <project_dir>/audio/narration.wav.
Loads voice_id, model_id, and voice_settings from .env (see voice-settings.md).
If ELEVENLABS_PRONUNCIATION_DICT_ID and ELEVENLABS_PRONUNCIATION_DICT_VERSION_ID
are set, applies the dictionary to the request (both must be present).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs import ElevenLabs, VoiceSettings


# ElevenLabs reads literal `[SCENE: name]` tags as narration ("bracket scene
# colon stats opener"). Strip them before TTS — they exist solely as scene
# boundary markers for the operator and are not meant to be spoken. Kokoro
# silently ignores them; ElevenLabs does not.
_SCENE_TAG_RE = re.compile(r"\[SCENE:[^\]]*\]\s*\n?", re.IGNORECASE)


def strip_scene_tags(text: str) -> str:
    """Remove `[SCENE: name]` markers and collapse the resulting blank-line runs."""
    cleaned = _SCENE_TAG_RE.sub("", text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned


def project_voice_settings(*, is_shorts: bool) -> VoiceSettings:
    speed_var = "ELEVENLABS_SPEED_SHORTS" if is_shorts else "ELEVENLABS_SPEED"
    return VoiceSettings(
        stability=float(os.environ["ELEVENLABS_STABILITY"]),
        similarity_boost=float(os.environ["ELEVENLABS_SIMILARITY_BOOST"]),
        style=float(os.environ["ELEVENLABS_STYLE"]),
        speed=float(os.environ[speed_var]),
        use_speaker_boost=os.environ["ELEVENLABS_USE_SPEAKER_BOOST"].lower() == "true",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--shorts", action="store_true", help="Use ELEVENLABS_SPEED_SHORTS")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    load_dotenv(repo_root / ".env", override=True)
    project = (repo_root / args.project_dir).resolve() if not args.project_dir.is_absolute() else args.project_dir
    script_path = project / "script.txt"
    out_path = project / "audio" / "narration.wav"

    if not script_path.exists():
        print(f"ERROR: {script_path} not found", file=sys.stderr)
        return 2
    out_path.parent.mkdir(parents=True, exist_ok=True)

    raw_text = script_path.read_text(encoding="utf-8").strip()
    if not raw_text:
        print(f"ERROR: {script_path} is empty", file=sys.stderr)
        return 2
    text = strip_scene_tags(raw_text)
    if not text:
        print(f"ERROR: {script_path} is empty after stripping [SCENE:] tags", file=sys.stderr)
        return 2
    if text != raw_text:
        stripped_count = len(_SCENE_TAG_RE.findall(raw_text))
        print(f"[tts] stripped {stripped_count} [SCENE:] marker(s) before TTS")

    voice_id = os.environ["ELEVENLABS_VOICE_ID"]
    model_id = os.environ["ELEVENLABS_MODEL_ID"]
    settings = project_voice_settings(is_shorts=args.shorts)

    dict_id = os.environ.get("ELEVENLABS_PRONUNCIATION_DICT_ID", "").strip()
    dict_ver = os.environ.get("ELEVENLABS_PRONUNCIATION_DICT_VERSION_ID", "").strip()
    locators = None
    if dict_id and dict_ver:
        locators = [{"pronunciation_dictionary_id": dict_id, "version_id": dict_ver}]
    elif dict_id and not dict_ver:
        print("ERROR: ELEVENLABS_PRONUNCIATION_DICT_ID is set but "
              "ELEVENLABS_PRONUNCIATION_DICT_VERSION_ID is missing — "
              "ElevenLabs requires both. Fetch the version with "
              "client.pronunciation_dictionaries.get(pronunciation_dictionary_id=...).",
              file=sys.stderr)
        return 2

    print(f"[tts] voice_id={voice_id} model_id={model_id} shorts={args.shorts}")
    print(f"[tts] settings stability={settings.stability} similarity={settings.similarity_boost} "
          f"style={settings.style} speed={settings.speed} speaker_boost={settings.use_speaker_boost}")
    if locators:
        print(f"[tts] pronunciation_dictionary={dict_id} version={dict_ver}")
    else:
        print("[tts] pronunciation_dictionary=<none>")
    print(f"[tts] text chars={len(text)}")

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not set in environment", file=sys.stderr)
        return 2
    client = ElevenLabs(api_key=api_key)
    resp = client.text_to_speech.convert_with_timestamps(
        voice_id=voice_id,
        text=text,
        model_id=model_id,
        output_format="pcm_44100",
        voice_settings=settings,
        pronunciation_dictionary_locators=locators,
    )

    import base64
    import json
    import wave

    pcm_bytes = base64.b64decode(resp.audio_base_64)
    print(f"[tts] received pcm bytes={len(pcm_bytes)}")

    # Wrap raw PCM (16-bit signed, 44.1kHz, mono) in a WAV header.
    with wave.open(str(out_path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(44100)
        wav.writeframes(pcm_bytes)

    duration_s = len(pcm_bytes) / 2 / 44100
    print(f"[tts] wrote {out_path}  ({duration_s:.2f}s, {out_path.stat().st_size} bytes)")

    # Group character-level alignment into whitespace-delimited word tokens.
    align = resp.normalized_alignment or resp.alignment
    words = []
    current = None
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
                current = {"word": ch, "start": t0, "end": t1}
            else:
                current["word"] += ch
                current["end"] = t1
    if current is not None:
        words.append(current)

    transcript_path = project / "transcript.json"
    transcript_path.write_text(json.dumps(words, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[tts] wrote {transcript_path}  ({len(words)} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
