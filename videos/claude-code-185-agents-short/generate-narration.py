"""Local edge-tts wrapper — workaround for the global script's word-boundary bug.

The repo-level scripts/edge-tts-fallback.py was written against edge-tts <7.x,
which emitted WordBoundary events by default. edge-tts 7.2.8 (the installed
version) requires the `boundary='WordBoundary'` kwarg on Communicate() or zero
word boundaries come back — which breaks transcript.json and all downstream
retiming.

Until scripts/edge-tts-fallback.py is updated upstream (out of scope for this
video — per CLAUDE.md scope discipline), this local script does the right
thing for THIS video only. To regenerate narration:

    python videos/claude-code-185-agents-short/generate-narration.py

Produces:
    audio/narration.wav (PCM 44.1kHz mono)
    audio/narration.mp3
    transcript.json (word-level timestamps)
"""

import asyncio
import json
import re
import subprocess
import sys
from pathlib import Path

import edge_tts

VOICE = "en-US-AndrewMultilingualNeural"
RATE = "+10%"


def strip_punctuation(word: str) -> str:
    return re.sub(r"^[\W_]+|[\W_]+$", "", word)


async def synthesize(text: str, voice: str, rate: str, out_mp3: Path) -> list[dict]:
    communicate = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    words: list[dict] = []
    with open(out_mp3, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                offset_s = chunk["offset"] / 10_000_000.0
                dur_s = chunk["duration"] / 10_000_000.0
                raw = chunk["text"]
                clean = strip_punctuation(raw)
                if not clean:
                    continue
                words.append(
                    {
                        "word": raw,
                        "start": round(offset_s, 3),
                        "end": round(offset_s + dur_s, 3),
                    }
                )
    return words


def mp3_to_wav(src: Path, dst: Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(src),
            "-ar", "44100", "-ac", "1",
            "-c:a", "pcm_s16le",
            str(dst),
        ],
        check=True,
        capture_output=True,
    )


def main() -> int:
    proj = Path(__file__).parent
    script_path = proj / "script.txt"
    text = script_path.read_text(encoding="utf-8").strip()
    print(f"[edge-tts] voice={VOICE} rate={RATE}")
    print(f"[edge-tts] chars={len(text)}")

    audio_dir = proj / "audio"
    audio_dir.mkdir(exist_ok=True)
    mp3_path = audio_dir / "narration.mp3"
    wav_path = audio_dir / "narration.wav"
    transcript_path = proj / "transcript.json"

    words = asyncio.run(synthesize(text, VOICE, RATE, mp3_path))
    print(f"[edge-tts] generated {len(words)} word boundaries")

    mp3_to_wav(mp3_path, wav_path)
    print(f"[edge-tts] wav: {wav_path}")

    transcript_path.write_text(json.dumps(words, indent=2), encoding="utf-8")
    print(f"[edge-tts] transcript: {transcript_path}")

    if words:
        last = words[-1]["end"]
        print(f"[edge-tts] total duration ~ {last:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
