#!/usr/bin/env python3
"""Add per-phase shape reposition to all 6 customization shorts.

Replaces the constant `animateShapeDrift` with `repositionShapesPerPhase` —
re-randomizes shape positions at each phase transition (T1, T2, T3), animated
over a 1.4s crossfade window. Mirrors templates/long-form/claude-code-version
behavior, adapted for the 1080×1920 shorts canvas.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SLUGS = [
    "claude-customization-5-features-short",
    "claudemd-vs-skills-short",
    "claude-skills-autotrigger-short",
    "claude-subagents-explained-short",
    "claude-hooks-explained-short",
    "claude-mcp-vs-skills-short",
]

# New function definition — replaces animateShapeDrift entirely.
NEW_FUNCTION = """  // Re-randomise shape positions at every phase transition. Each phase gets a
  // fresh deterministic placement (overlap-aware, mirrors spawnShapes); the
  // tween animates over the crossfade window so it reads as part of the
  // transition rather than independent drift.
  // Mirrors templates/long-form/claude-code-version/index.html, adapted for
  // the 1080x1920 shorts canvas.
  function repositionShapesPerPhase(tl, container, seedPrefix, phaseStartTimes) {
    const imgs = Array.from(container.querySelectorAll('img'));
    if (!imgs.length || !phaseStartTimes.length) return;
    const w = 1080, h = 1920, minDist = 340, MAX_TRIES = 80;
    const anchors = imgs.map(img => ({
      left: parseFloat(img.style.left),
      top:  parseFloat(img.style.top),
      size: parseFloat(img.style.width),
    }));
    phaseStartTimes.forEach((sceneT, sceneIdx) => {
      const placed = [];
      let attempt = 0;
      const positions = imgs.map((img, i) => {
        const size = anchors[i].size;
        let best = null, bestScore = -1;
        for (let t = 0; t < MAX_TRIES; t++) {
          const seed = seedPrefix + '-phase' + sceneIdx + '-' + i + '-' + (attempt++);
          const cx = seedHash(seed + '-x') * (w - size * 0.4) + size * 0.2;
          const cy = seedHash(seed + '-y') * (h - size * 0.4) + size * 0.2;
          const rot = (seedHash(seed + '-rot') - 0.5) * 90;
          let nearest = Infinity;
          for (const p of placed) {
            const dx = cx - p.cx, dy = cy - p.cy;
            const d2 = dx * dx + dy * dy;
            if (d2 < nearest) nearest = d2;
          }
          if (nearest >= minDist * minDist) { best = { cx, cy, rot }; break; }
          if (nearest > bestScore) { bestScore = nearest; best = { cx, cy, rot }; }
        }
        placed.push({ cx: best.cx, cy: best.cy });
        return {
          x: (best.cx - size / 2) - anchors[i].left,
          y: (best.cy - size / 2) - anchors[i].top,
          rot: best.rot,
        };
      });
      // ONE tween targeting all imgs via function-based values — GSAP treats
      // them as a single animation unit, in lock-step at the same time. Tween
      // starts 0.4s before the phase transition so the reposition reads as
      // part of the crossfade rather than landing after.
      tl.to(imgs, {
        x: (i) => positions[i].x,
        y: (i) => positions[i].y,
        rotation: (i) => positions[i].rot,
        duration: 1.4,
        ease: 'power2.inOut',
      }, sceneT - 0.4);
    });
  }
"""

# Pattern: match the entire animateShapeDrift function definition (multiline).
ANIMATE_DRIFT_PATTERN = re.compile(
    r"  function animateShapeDrift\(tl, container, seedPrefix, totalDuration\) \{\n"
    r".*?\n"
    r"  \}\n",
    re.DOTALL,
)

# Pattern: match the animateShapeDrift call line (slug-specific second arg).
DRIFT_CALL_PATTERN = re.compile(
    r"  animateShapeDrift\(tl, document\.getElementById\('shape-backdrop'\), '[^']+', TOTAL\);\n"
)


def patch_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html

    # 1. Replace function definition
    html, n_func = ANIMATE_DRIFT_PATTERN.subn(NEW_FUNCTION, html, count=1)

    # 2. Remove the old call line
    html, n_call = DRIFT_CALL_PATTERN.subn("", html, count=1)

    # 3. Extract the seedPrefix from the spawnShapes call (same prefix as drift)
    spawn_match = re.search(r"spawnShapes\('([^']+)',", html)
    if not spawn_match:
        print(f"  ERROR: {path}: no spawnShapes call found", file=sys.stderr)
        return False
    seed = spawn_match.group(1)

    # 4. Add the new call right before window.__timelines["main"] = tl;
    new_call = (
        f'\n  // Reposition shapes at each phase transition (paired with cinematic-whoosh SFX).\n'
        f'  repositionShapesPerPhase(\n'
        f'    tl,\n'
        f'    document.getElementById(\'shape-backdrop\'),\n'
        f'    \'{seed}\',\n'
        f'    [T1, T2, T3]\n'
        f'  );\n\n'
    )
    html, n_register = re.subn(
        r'(\n)(  window\.__timelines\["main"\] = tl;)',
        rf'\g<1>{new_call}\g<2>',
        html,
        count=1,
    )

    if html == original:
        print(f"  WARN: {path}: no changes made", file=sys.stderr)
        return False
    if n_func != 1 or n_call != 1 or n_register != 1:
        print(
            f"  WARN: {path}: unexpected match counts "
            f"(func={n_func}, call={n_call}, register={n_register})",
            file=sys.stderr,
        )

    path.write_text(html, encoding="utf-8")
    return True


def main() -> int:
    failed = []
    for slug in SLUGS:
        index_path = REPO_ROOT / "videos" / slug / "index.html"
        if not index_path.exists():
            print(f"  ERROR: {slug}: missing index.html", file=sys.stderr)
            failed.append(slug)
            continue
        ok = patch_file(index_path)
        print(f"  {'OK ' if ok else 'FAIL'} {slug}")
        if not ok:
            failed.append(slug)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
