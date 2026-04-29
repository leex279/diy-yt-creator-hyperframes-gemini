# Implementation Report

**Plan**: `.claude/PRPs/plans/generic-long-form-template.plan.md`
**Branch**: `main`
**Date**: 2026-04-28
**Status**: COMPLETE

---

## Summary

Shipped `templates/long-form/standard/` — the first generic horizontal long-form HyperFrames template (1920x1080 / 30fps). The template ships a working ~120-second multi-scene demo composition exercising 8 reusable scene archetypes (hero hook, image-hero with overlay, side-by-side compare, stat-pill row, source-image cards, embedded-video frame, architecture stack, CTA endcard) plus a captions sub-composition. Each scene is an external HTML file with its own paused GSAP timeline registered on `window.__timelines`, and the root composition only orchestrates ambient background + scene crossfades. Defaults match the synthesized "dark navy + 4-accent rotation" palette but ship as project-swappable CSS variables on `:root` so any video can re-skin without forking. Lint, validate, inspect all clean; draft render produced an 8.5MB MP4 of the full 120s demo.

---

## Assessment vs Reality

| Metric     | Predicted | Actual    | Reasoning                                                                                       |
| ---------- | --------- | --------- | ----------------------------------------------------------------------------------------------- |
| Complexity | HIGH      | HIGH      | 25 files created, sub-composition wiring novel for repo, 3 lint/render iterations needed       |
| Confidence | HIGH      | HIGH      | Plan was well-researched; major patterns (`<template>` wrapping, `data-composition-src`, `data-caption-root`) all worked as documented |

**Deviations:**

- **Audio bed left as commented snippets in `index.html`.** The plan wired `<audio>` elements live for narration + 3-segment bg-music, but the lint emits `audio_src_not_found` as an error (not a warning) when files are missing. Following the existing `templates/shorts/anthropic/` pattern, I commented out the audio elements with a clear "uncomment when adding audio" instruction. Operators uncomment after dropping their narration/music files.

- **`<video>` element in `scene-video-embed.html` replaced with placeholder slate.** The plan called for a live `<video src="assets/clips/demo.mp4">` element. The render hard-fails with "video metadata not ready after 45000ms" when the .mp4 is missing — even though the plan said don't ship a video file. Mitigated by replacing the `<video>` with a labeled placeholder div ("DROP YOUR CLIP · assets/clips/demo.mp4") that operators replace with the real `<video>` element per the README snippet. This keeps the bare template render-able.

- **`data-start="0"` added to all 9 sub-composition root divs.** The plan's snippet did not include `data-start` on sub-comp roots; the lint warns on every external sub-comp without it ("runtime needs data-start='0' on the root element to begin playback"). Added to all 9 files.

- **Source-card overline contrast bumped.** The plan's accent-on-translucent-card pattern at 14px failed WCAG AA (4.06:1, need 4.5:1). Bumped font-size to 18px and switched to brighter accent variants (`#93C5FD`, `#67E8F9`, `#C4B5FD`) — now passes AA at the small-text threshold.

- **Architecture-stack `.meta` text recolored from `--text-muted` to `--text-secondary`.** The 3.6:1 contrast on small body text failed AA; `--text-secondary` (`#9AA0A6`) gives 4.7:1.

- **Placeholder PNGs generated via ImageMagick** instead of skipping. The plan said "Use ImageMagick/skip if not available — document the requirement in README.md instead." ImageMagick was available, so I generated minimal 1920x1080 / 16:9 dark-gray slates with "REPLACE WITH HERO IMAGE" / "SOURCE 1/2/3" / "NEXT VIDEO THUMBNAIL" labels. This brings the bare template's `validate` count from 6 missing-asset errors down to 1 (only the operator-supplied `demo.mp4`).

---

## Tasks Completed

| #   | Task                                                                  | Files                                                                                       | Status |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| 1   | Directory structure + meta files                                      | `meta.json`, `hyperframes.json`, `sfx-cues.txt`, `.gitkeep` × 4                             | ✅     |
| 2   | Shape SVGs copied                                                     | `assets/shapes/shape{1,2,3}.svg`                                                            | ✅     |
| 3   | Tokens CSS                                                            | `tokens/long-form.css`                                                                       | ✅     |
| 4   | Hook scene                                                            | `compositions/scene-hook.html`                                                              | ✅     |
| 5   | Image-hero scene + placeholder PNG                                    | `compositions/scene-image-hero.html`, `assets/screenshots/hero-shot.png`                    | ✅     |
| 6   | Side-by-side scene                                                    | `compositions/scene-side-by-side.html`                                                      | ✅     |
| 7   | Stat-pill-row scene (1920x1080 adaptation)                            | `compositions/scene-stat-pill-row.html`                                                     | ✅     |
| 8   | Source-cards scene + placeholder PNGs                                 | `compositions/scene-source-cards.html`, `assets/screenshots/source-{1,2,3}.png`             | ✅     |
| 9   | Video-embed scene (with placeholder slate; operator wires real video) | `compositions/scene-video-embed.html`                                                       | ✅     |
| 10  | Architecture-stack scene                                              | `compositions/scene-architecture-stack.html`                                                | ✅     |
| 11  | CTA scene + placeholder PNG                                           | `compositions/scene-cta.html`, `assets/screenshots/next-video-thumbnail.png`                | ✅     |
| 12  | Captions sub-composition                                              | `compositions/captions.html`                                                                | ✅     |
| 13  | Root index.html composition                                           | `index.html`                                                                                | ✅     |
| 14  | Logo copied                                                           | `assets/anthropic-logo-light.svg`                                                            | ✅     |
| 15  | DESIGN.md                                                             | `DESIGN.md`                                                                                  | ✅     |
| 16  | README.md                                                             | `README.md`                                                                                  | ✅     |
| 17  | Parent README updated                                                 | `templates/long-form/README.md`                                                              | ✅     |
| 18  | Shared lib visual-style + token + MANIFEST                            | `shared/lib/visual-styles/long-form-standard.md`, `shared/lib/tokens/long-form-standard.css`, `shared/lib/MANIFEST.md` | ✅     |

---

## Validation Results

| Check                         | Result | Details                                                                                       |
| ----------------------------- | ------ | --------------------------------------------------------------------------------------------- |
| `hyperframes lint`            | ✅     | 0 errors, 0 warnings on the bare template (10 files)                                          |
| `hyperframes validate` (WCAG) | ✅     | 44 text elements pass AA · 0 contrast warnings · 1 missing-asset error (operator-supplied `demo.mp4`) |
| `hyperframes inspect`         | ✅     | 0 layout issues across 9 timeline samples                                                     |
| Spawn dry-run                 | ✅     | `cp -r template /tmp/test-spawn-lf` + meta.json sed → lint clean (0 errors, 0 warnings)        |
| `hyperframes render --quality draft` | ✅ | 8.5MB MP4 produced · 2:59 run time at draft on this workstation (32 cores, 8 workers auto)    |

All acceptance criteria from the plan are met:
- All 25 files present (created)
- Lint exits 0 with 0 errors ✓
- Validate reports no AAA contrast failures, no AA failures on headlines ✓
- Inspect reports no overflow at 1920x1080 ✓
- Render produces a viewable MP4 ✓
- All 10 expected timeline IDs (`main`, 8 scenes, `captions`) register on `window.__timelines` ✓
- Spawn dry-run lints clean without code changes ✓
- `templates/long-form/README.md` updated to mark `standard/` as canonical baseline ✓
- `shared/lib/visual-styles/long-form-standard.md`, `shared/lib/tokens/long-form-standard.css`, MANIFEST entries ✓
- DESIGN.md and README.md mirror `templates/shorts/anthropic/` structure ✓
- No `class="clip"` on `<audio>` or `<video>` (lint enforces) ✓
- No `data-duration` on any sub-composition wrapper div ✓
- All `tl.from()` at position > 5 use `immediateRender: false` ✓

---

## Files Changed

| File                                                                       | Action | Lines |
| -------------------------------------------------------------------------- | ------ | ----- |
| `templates/long-form/standard/meta.json`                                   | CREATE | +4    |
| `templates/long-form/standard/hyperframes.json`                            | CREATE | +9    |
| `templates/long-form/standard/sfx-cues.txt`                                | CREATE | +5    |
| `templates/long-form/standard/audio/.gitkeep`                              | CREATE | +0    |
| `templates/long-form/standard/assets/.gitkeep`                             | CREATE | +0    |
| `templates/long-form/standard/assets/sfx/.gitkeep`                         | CREATE | +0    |
| `templates/long-form/standard/assets/clips/.gitkeep`                       | CREATE | +0    |
| `templates/long-form/standard/assets/screenshots/README.md`                | CREATE | +28   |
| `templates/long-form/standard/assets/screenshots/hero-shot.png`            | CREATE | (1920x1080 placeholder) |
| `templates/long-form/standard/assets/screenshots/source-{1,2,3}.png`       | CREATE | (1280x720 placeholders × 3) |
| `templates/long-form/standard/assets/screenshots/next-video-thumbnail.png` | CREATE | (1280x720 placeholder) |
| `templates/long-form/standard/assets/shapes/shape{1,2,3}.svg`              | CREATE | (copied from shorts × 3) |
| `templates/long-form/standard/assets/anthropic-logo-light.svg`             | CREATE | (copied from shared/logos) |
| `templates/long-form/standard/tokens/long-form.css`                        | CREATE | +52   |
| `templates/long-form/standard/compositions/scene-hook.html`                | CREATE | +95   |
| `templates/long-form/standard/compositions/scene-image-hero.html`          | CREATE | +119  |
| `templates/long-form/standard/compositions/scene-side-by-side.html`        | CREATE | +152  |
| `templates/long-form/standard/compositions/scene-stat-pill-row.html`       | CREATE | +135  |
| `templates/long-form/standard/compositions/scene-source-cards.html`        | CREATE | +175  |
| `templates/long-form/standard/compositions/scene-video-embed.html`         | CREATE | +110  |
| `templates/long-form/standard/compositions/scene-architecture-stack.html`  | CREATE | +145  |
| `templates/long-form/standard/compositions/scene-cta.html`                 | CREATE | +145  |
| `templates/long-form/standard/compositions/captions.html`                  | CREATE | +56   |
| `templates/long-form/standard/index.html`                                  | CREATE | +330  |
| `templates/long-form/standard/DESIGN.md`                                   | CREATE | +145  |
| `templates/long-form/standard/README.md`                                   | CREATE | +220  |
| `templates/long-form/README.md`                                            | UPDATE | +21/-9 |
| `shared/lib/visual-styles/long-form-standard.md`                           | CREATE | +110  |
| `shared/lib/tokens/long-form-standard.css`                                 | CREATE | +50   |
| `shared/lib/MANIFEST.md`                                                   | UPDATE | +2/0  |

**Total: 26 CREATE + 2 UPDATE = 28 file mutations.**

(The plan estimated 25 CREATE + 2 UPDATE; the +1 CREATE is `templates/long-form/standard/assets/screenshots/README.md` which was added as an asset-replacement guide.)

---

## Issues Encountered

1. **Lint detects media in HTML comments.** The lint scans for `src="..."` attribute patterns and `<video>` literal tags inside HTML comments and reports them as duplicate-media-discovery-risk warnings. Fixed by rewording comments to avoid the literal `<video>` tag and instead saying "video element" / "the video element".

2. **Render hard-blocks on missing `<video>` source files.** Unlike audio (which warns), a `<video>` element pointing at a missing `.mp4` causes the render to fail with `[FrameCapture] video metadata not ready after 45000ms`. Mitigated by replacing the `<video>` with a placeholder div until the operator wires their real clip.

3. **WCAG AA contrast warnings on small accent-colored text.** Source-card overlines (14px accent on translucent gradient bg) and architecture-stack meta lines (18px `--text-muted`) failed AA. Fixed by bumping source-card overline to 18px with brighter accent variants, and switching architecture meta to `--text-secondary`.

4. **Sub-composition root divs need `data-start="0"`.** The plan's `<template>` snippet did not include this; lint warns on every external sub-comp. Added to all 9.

5. **`data-volume="1"` warning style** — the existing `audio-design.md` was independently updated mid-implementation (SFX volumes recalibrated 25% lower). My template's commented audio bed uses the plan's original numbers (0.07 / 0.12 for bg-music, 1.0 for narration). The `audio-design.md` recalibration only affected SFX volumes (impact-slam, scale-slam, etc.), not bg-music or narration — so the template's numbers remain canonical. No action needed.

---

## Tests Written

This plan ships a template (no executable code beyond GSAP timelines), so the testing strategy is the validation suite rather than unit tests:

- `hyperframes lint` — runs the framework's static analyzer against all 10 .html files
- `hyperframes validate` — runs WCAG contrast audit in headless Chrome
- `hyperframes inspect` — checks 9 timeline samples for layout overflow
- Spawn dry-run — copies the template to `/tmp/test-spawn-lf`, replaces meta.json placeholders, lints
- Draft render — full 120s render at 30fps, draft quality, 8 workers

All five passed in this implementation pass.

---

## Next Steps

- [ ] Operator can now `cp -r templates/long-form/standard videos/<slug>` and produce a 4-15min long-form by editing copy + screenshots + narration.
- [ ] Future variants (`templates/long-form/dynamous/`, `templates/long-form/news-explainer/`, `templates/long-form/tutorial/`, `templates/long-form/claude-code-version/`) fork this baseline.
- [ ] If 3+ long-form videos use the same scene archetype, consider extracting it into `shared/lib/blocks/` per the plan's "Future enhancements" notes.
- [ ] Companion plan `.claude/PRPs/plans/claude-code-version-longform-template.plan.md` can be revisited and likely simplified to "fork `standard/` and swap palette + scene archetypes".
