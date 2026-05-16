# Recipe: cinema-title-slam

Standalone cinematic hero-title block. Canvas: 1080×1920 (Shorts). Duration: 6s.

## What it produces

```
         ╔════════════════════════╗
         ║                        ║
         ║                        ║
         ║        H E R O         ║  ← 180px accent, back.out(1.7) slam + shake
         ║     ~~~~~~~~~~~        ║  ← wobbly hand-drawn SVG underline draws in
         ║                        ║
         ║   Your tagline here    ║  ← 42px, fades up
         ║                        ║
         ╚════════════════════════╝
```

Three-tier reveal timeline:

| Time         | Event                                                                |
|--------------|----------------------------------------------------------------------|
| t=0.5s       | Hero word slams in: `back.out(1.7)` scale 0.78→1.0, 0.65s           |
| t=0.55–0.74s | 4-tick inline shake: ±5px x offsets settle to 0                      |
| t=1.4s       | Wobbly SVG underline draws left-to-right via `stroke-dashoffset`     |
| t=2.0s       | Tagline fades up from y+20, opacity 0→1, 0.6s                       |
| t=2.5–5.0s   | Ambient breath on hero (scale 1.0↔1.015, yoyo×1, 1.5s half-cycle)  |
| t=5.0–6.0s   | Full block fades out (hero, underline, tagline staggered)            |

## Slots to edit

In the copied `compositions/cinema-title-slam.html`:

| Selector / attribute       | Purpose                         | Constraint                                 |
|----------------------------|---------------------------------|--------------------------------------------|
| `[data-slot="hero"]`       | Single hero token (1 word best) | 180px; accent color; ≤ 8 chars for 1080px  |
| `[data-slot="tagline"]`    | Supporting line                 | 42px; ≤ ~30 chars before line-wrap         |
| `#cts-underline-path`      | SVG underline shape             | Wobbly `d=` path; start near x=8, end x≈672; y range 14–38 |
| `var(--accent)`             | Hero word + underline color     | Override on host or root tokens             |
| `var(--bg)`                 | Canvas background               | Default `#0A0E1A`                           |
| `var(--text)`               | Tagline color                   | Default `#F5F1EB`                           |

## Required tokens

```
--bg, --accent, --text, --sans
```

Fallbacks are baked in (`#0A0E1A`, `#E97458`, `#F5F1EB`, `'Inter'`). Link
`shared/lib/tokens/anthropic-dark.css` (or your own equivalent) for a full
design-system context, or override individually.

## Wire into a host composition

1. Copy `block.html` to `videos/<slug>/compositions/cinema-title-slam.html`.
2. In `videos/<slug>/index.html`, add (replace `<start>`, `<duration>`, `<track>`):

```html
<div id="cts"
     data-composition-id="cinema-title-slam"
     data-composition-src="compositions/cinema-title-slam.html"
     data-start="<start>"
     data-duration="6"
     data-track-index="<track>"
     data-width="1080"
     data-height="1920"></div>
```

3. The framework nests the block's internal timeline under the host root timeline
   automatically. No manual JS integration needed.

## CSS-var overrides (per-video)

Override tokens on the host's root or on the wiring div's parent:

```css
/* Swap accent to purple for a different video */
#cts {
  --accent: #A78BFA;
  --bg:     #0B0F18;
}
```

## SVG underline customization

The underline uses a cubic-Bezier wobbly path. To match the width of your hero word:

1. Measure the rendered hero word width (inspector or visual estimate).
2. Scale the `d=` path's x-coordinates proportionally.
3. Keep the y-values in the 14–38 range to maintain the "hand-drawn" wobble feel.

Default path spans 680px (appropriate for a 4–6 char word at 180px). For a
single-character hero, scale down to ~200px wide; for a long word, scale up.

## Gotchas

- `stroke-dasharray: 1; stroke-dashoffset: 1` with GSAP tweening to `0` requires
  `pathLength="1"` on the SVG `<path>`. This is already set in block.html. If you
  replace the `<path>` element, add `pathLength="1"` to the new one.
- The underline SVG has `overflow: visible` so the wobbly path extremes don't clip.
  Don't add `overflow: hidden` to its container.
- The ambient breath uses `yoyo: true, repeat: 1` (one full in-and-out). At t=5s
  when the exit fade fires, the breath tween ends at t=5.5s — the exit opacity
  tween at t=5.0 with `power2.in` wins via `overwrite: "auto"` isn't set, so both
  run concurrently. The opacity fade wins visually because it drives opacity; the
  scale tween drives scale — they don't conflict.
- `data-duration="6"` on the wiring div: don't change this unless you alter the
  timeline structure. The block's internal timeline drives its own total length;
  the outer `data-duration` tells the host framework how long to reserve.
- Don't add `overflow: hidden` to `[data-composition-id="cinema-title-slam"]` — it
  would clip the hero word's text-shadow glow halo.

## Lint expectations

`npx hyperframes lint videos/<slug>` should report 0 errors.

Common errors if wired wrong:

- `missing_track_index` — add `data-track-index` to the wiring `<div>` in host.
- `composition_id_mismatch` — `data-composition-id` on wiring div MUST be `cinema-title-slam`.
- `invalid_data_start` — block root div must have `data-start="0"` (already present).
