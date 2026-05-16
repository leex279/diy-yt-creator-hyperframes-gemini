"""Convert whisper.cpp --output-json-full output to HyperFrames transcript schema.

Whisper.cpp emits {transcription: [{tokens: [...]}, ...]} with millisecond offsets
and special tokens (`[_BEG_]`, `[_TT_*]`). HyperFrames expects a flat array:
[{word: str, start: float, end: float}, ...] in seconds.

This converter groups sub-word tokens into whole words (whisper.cpp tokenizes mid-word
with leading-space convention: " Claude" + " code" = two words, "Claude" + "M" + ".md"
or " ." gets merged into the preceding word).

Usage:
  python scripts/whisper-cpp-to-hyperframes.py <project_dir>
"""

import json
import re
import sys
from pathlib import Path


SPECIAL_TOKEN_RE = re.compile(r"^\[_[A-Z]+_?\d*\]$")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: whisper-cpp-to-hyperframes.py <project_dir>", file=sys.stderr)
        return 1

    proj = Path(sys.argv[1])
    src = proj / "transcript.json"
    raw = json.loads(src.read_text(encoding="utf-8"))

    words: list[dict] = []
    current_word = ""
    current_start = None
    current_end = None

    for seg in raw["transcription"]:
        for tok in seg["tokens"]:
            text = tok["text"]
            if SPECIAL_TOKEN_RE.match(text):
                continue
            start_ms = tok["offsets"]["from"]
            end_ms = tok["offsets"]["to"]

            if text.startswith(" "):
                if current_word:
                    words.append(
                        {
                            "word": current_word,
                            "start": round(current_start / 1000.0, 3),
                            "end": round(current_end / 1000.0, 3),
                        }
                    )
                current_word = text.lstrip()
                current_start = start_ms
                current_end = end_ms
            else:
                if not current_word:
                    current_word = text
                    current_start = start_ms
                else:
                    current_word += text
                current_end = end_ms

    if current_word:
        words.append(
            {
                "word": current_word,
                "start": round(current_start / 1000.0, 3),
                "end": round(current_end / 1000.0, 3),
            }
        )

    cleaned = [
        {"word": re.sub(r"^[^\w]+|[^\w]+$", "", w["word"]), "start": w["start"], "end": w["end"]}
        for w in words
        if re.sub(r"^[^\w]+|[^\w]+$", "", w["word"])
    ]

    src.write_text(json.dumps(cleaned, indent=2), encoding="utf-8")
    print(f"[convert] wrote {len(cleaned)} words to {src}")
    if cleaned:
        print(f"[convert] last word: {cleaned[-1]['word']} @ {cleaned[-1]['end']:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
