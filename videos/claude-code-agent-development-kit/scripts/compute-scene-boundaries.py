"""Compute scene boundaries from transcript.json word-level timestamps.

Each scene's last-word anchor is a unique phrase from the script. We find that
phrase in the transcript word stream and use its `.end` time minus 0.2 (crossfade
lead-in) as the next scene's `data-start`.

Output:
- Prints the 8 scene_starts[] values + TOTAL_DURATION
- Writes a JSON dump of the boundaries to videos/<slug>/scene-boundaries.json
"""

import json
import re
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
TRANSCRIPT = PROJ / "transcript.json"

# Each entry: (scene_name, last_word_anchor_phrase)
# We search for the last occurrence of the final 1-3 words of each scene.
SCENE_ANCHORS = [
    ("scene-1-hook", ["Agent", "Development", "Kit"]),
    ("scene-2-architecture-stack", ["wrong", "thing"]),
    ("scene-3-claude-md", ["across", "conversations"]),
    ("scene-4-skills-vs-hooks", ["working", "together"]),
    ("scene-5-subagents", ["cap", "is", "intentional"]),
    ("scene-6-plugins", ["in", "a", "plugin"]),
    ("scene-7-decision-tree", ["moves", "it", "to", "the", "team"]),
    ("scene-8-lifecycle-cta", ["community"]),
]


def normalize(w):
    return re.sub(r"[^\w]", "", w).lower()


def find_phrase_end(words, phrase):
    """Find the last occurrence of `phrase` in `words` and return the .end of the final token."""
    target = [normalize(p) for p in phrase]
    n = len(target)
    best = None
    for i in range(len(words) - n + 1):
        window = [normalize(words[i + k]["word"]) for k in range(n)]
        if window == target:
            best = words[i + n - 1]["end"]
    return best


def main():
    words = json.loads(TRANSCRIPT.read_text(encoding="utf-8"))
    scene_ends = []
    for name, phrase in SCENE_ANCHORS:
        end = find_phrase_end(words, phrase)
        if end is None:
            print(f"!! could not find anchor for {name}: {phrase}")
            return 1
        scene_ends.append((name, end))
        print(f"{name:35s} ends @ {end:7.2f}s  (anchor: {' '.join(phrase)})")

    scene_starts = [0.0]
    for _, end in scene_ends[:-1]:
        scene_starts.append(round(end - 0.2, 2))

    total_duration = round(scene_ends[-1][1] + 1.5, 2)

    print()
    print("--- scene_starts (paste into index.html) ---")
    for i, (start, (name, _end)) in enumerate(zip(scene_starts, scene_ends)):
        print(f"  scene {i+1} ({name:30s}) data-start='{start}'")

    print()
    print(f"TOTAL_DURATION = {total_duration}")

    out = {
        "scene_starts": scene_starts,
        "scene_ends": [{"name": n, "end": e} for n, e in scene_ends],
        "total_duration": total_duration,
    }
    (PROJ / "scene-boundaries.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nwrote {PROJ / 'scene-boundaries.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
