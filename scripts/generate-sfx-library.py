"""Generate canonical SFX library for shared/audio/sfx/ via ElevenLabs.

Idempotent: skips files already on disk unless --force. Per-cue prompts and
target durations live in the CUES list below — tune them when a generated cue
has the wrong character.

Usage:
  python scripts/generate-sfx-library.py
  python scripts/generate-sfx-library.py --only impact-slam --force
  python scripts/generate-sfx-library.py --out-dir /tmp/sfx-test

Requires ELEVENLABS_API_KEY in .env (same key used by elevenlabs-tts.py).
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs import ElevenLabs


CUES: list[dict] = [
    {
        "name": "impact-slam",
        "prompt": "Deep cinematic bass impact slam, single hit, no reverb tail, dry punchy",
        "duration_seconds": 0.6,
        "prompt_influence": 0.7,
    },
    {
        "name": "scale-slam",
        "prompt": "Heavy metallic scale slam, weighty single drop, very short tail",
        "duration_seconds": 0.7,
        "prompt_influence": 0.7,
    },
    {
        "name": "screen-shake",
        "prompt": "Subtle low-frequency rumble, half a second, no rise no decay, suitable to layer under another impact",
        "duration_seconds": 0.5,
        "prompt_influence": 0.6,
    },
    {
        "name": "cinematic-whoosh",
        "prompt": "Quick cinematic whoosh, transition sweep, mid-range, no reverb",
        "duration_seconds": 0.8,
        "prompt_influence": 0.6,
    },
    {
        "name": "spring-pop",
        # ElevenLabs sound-effects API rejects duration_seconds < 0.5; the
        # cue itself is shorter — pick the perceptual peak via the prompt.
        "prompt": "Light bouncy spring pop, UI element entrance, snappy attack with quick tail",
        "duration_seconds": 0.5,
        "prompt_influence": 0.7,
    },
    {
        "name": "pop",
        "prompt": "Soft round pop, small UI tap, very short attack and decay",
        "duration_seconds": 0.5,
        "prompt_influence": 0.7,
    },
    {
        "name": "glitch-zap",
        "prompt": "Digital glitch zap, electric sputter, retro tech, half a second",
        "duration_seconds": 0.5,
        "prompt_influence": 0.7,
    },
    {
        "name": "strike-cross",
        "prompt": "Quick brush strikethrough sound, pen scratch crossing out text",
        "duration_seconds": 0.6,
        "prompt_influence": 0.7,
    },
    {
        "name": "sonic-logo",
        "prompt": "Brief warm orchestral brand stinger, ascending two-note motif, ends clean",
        "duration_seconds": 1.5,
        "prompt_influence": 0.5,
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate canonical SFX library via ElevenLabs.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate cues even if the .mp3 already exists.",
    )
    parser.add_argument(
        "--only",
        type=str,
        default=None,
        help="Only generate this single cue (must match a name in CUES).",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: shared/audio/sfx/ relative to repo root).",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=None,
        help="Path to env file (default: <repo-root>/.env). Relative paths "
             "resolve against repo root. Use for per-creator configs like .env.cole.",
    )
    return parser.parse_args()


def generate_cue(client: ElevenLabs, cue: dict, out_path: Path) -> int:
    """Generate one cue. Returns 0 on success, 1 on failure."""
    try:
        audio = client.text_to_sound_effects.convert(
            text=cue["prompt"],
            duration_seconds=cue["duration_seconds"],
            prompt_influence=cue["prompt_influence"],
            output_format="mp3_44100_128",
        )
        with open(out_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)
    except Exception as exc:
        # Don't leave a 0-byte file behind — future runs would skip it as "exists".
        if out_path.exists() and out_path.stat().st_size == 0:
            out_path.unlink()
        print(f"[sfx] FAILED   {cue['name']}.mp3: {exc}", file=sys.stderr)
        return 1
    size = out_path.stat().st_size
    print(f"[sfx] generated {cue['name']}.mp3 ({cue['duration_seconds']}s, {size} bytes)")
    return 0


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    env_path = args.env_file if args.env_file is not None else Path(".env")
    if not env_path.is_absolute():
        env_path = repo_root / env_path
    if not env_path.exists():
        print(f"ERROR: env file not found: {env_path}", file=sys.stderr)
        return 2
    load_dotenv(env_path, override=True)
    print(f"[sfx] env_file={env_path}")

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not set in environment", file=sys.stderr)
        return 2

    out_dir = args.out_dir if args.out_dir is not None else repo_root / "shared" / "audio" / "sfx"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.only is not None:
        selected = [c for c in CUES if c["name"] == args.only]
        if not selected:
            available = ", ".join(c["name"] for c in CUES)
            print(f"ERROR: --only {args.only!r} not in CUES. Available: {available}",
                  file=sys.stderr)
            return 2
    else:
        selected = list(CUES)

    client = ElevenLabs(api_key=api_key)
    failures = 0

    for i, cue in enumerate(selected):
        out_path = out_dir / f"{cue['name']}.mp3"
        if out_path.exists() and not args.force:
            print(f"[sfx] skipped   {cue['name']}.mp3 (exists)")
            continue
        if i > 0:
            time.sleep(1)
        if generate_cue(client, cue, out_path) != 0:
            failures += 1

    if failures:
        print(f"[sfx] DONE with {failures} failure(s) — see stderr above", file=sys.stderr)
        return 1
    print(f"[sfx] DONE — {len(selected)} cue(s) processed, output dir: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
