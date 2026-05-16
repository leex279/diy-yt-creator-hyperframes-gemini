"""One-off transcript generator for top-3-ai-memory-systems-short.

edge-tts 7.x no longer emits WordBoundary; scripts/edge-tts-fallback.py produces
an empty transcript.json. This script re-synthesizes with SentenceBoundary events
and distributes word timing proportionally by character count within each sentence.
Approximate but good enough for visual-anchor planning.

After this runs, transcript.json contains [{word, start, end}, ...] in seconds.
"""
import asyncio, json, re, sys, subprocess
from pathlib import Path
import edge_tts

PROJ = Path(__file__).parent
SCRIPT = PROJ / "script.txt"
MP3 = PROJ / "audio" / "narration.mp3"
WAV = PROJ / "audio" / "narration.wav"
TRANS = PROJ / "transcript.json"

VOICE = "en-US-AndrewNeural"
RATE = "+10%"


def strip_punct(w: str) -> str:
    return re.sub(r"^[\W_]+|[\W_]+$", "", w)


async def synth() -> list[dict]:
    text = SCRIPT.read_text(encoding="utf-8").strip()
    c = edge_tts.Communicate(text, VOICE, rate=RATE)
    sentences: list[dict] = []  # [{text, offset, duration}]
    with open(MP3, "wb") as f:
        async for chunk in c.stream():
            t = chunk.get("type")
            if t == "audio":
                f.write(chunk["data"])
            elif t == "SentenceBoundary":
                sentences.append({
                    "text": chunk["text"],
                    "offset": chunk["offset"] / 1e7,
                    "duration": chunk["duration"] / 1e7,
                })
    # Distribute per-word inside each sentence proportional to char count.
    words_out: list[dict] = []
    for s in sentences:
        raw_words = s["text"].split()
        if not raw_words:
            continue
        char_lens = [max(1, len(w)) for w in raw_words]
        total = sum(char_lens)
        cum = 0.0
        for raw, cl in zip(raw_words, char_lens):
            frac_start = cum / total
            frac_end = (cum + cl) / total
            cum += cl
            start = s["offset"] + frac_start * s["duration"]
            end = s["offset"] + frac_end * s["duration"]
            clean = strip_punct(raw)
            if not clean:
                continue
            words_out.append({
                "word": clean,
                "start": round(start, 3),
                "end": round(end, 3),
            })
    return words_out


def mp3_to_wav():
    subprocess.run(["ffmpeg", "-y", "-i", str(MP3), "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", str(WAV)], check=True, capture_output=True)


def main():
    words = asyncio.run(synth())
    mp3_to_wav()
    TRANS.write_text(json.dumps(words, indent=2), encoding="utf-8")
    print(f"wrote {len(words)} words; last_end={words[-1]['end']:.2f}s" if words else "no words")


if __name__ == "__main__":
    main()
