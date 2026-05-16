# Recipe: bar-fill-pulse

Horizontal bar fills from 0 to a target percent over `duration` seconds. A bright energy-pulse highlight travels along the leading edge of the fill. On completion, the bar flashes briefly.

## What it produces

```
  ████████████████████░░░░░░░░  ← fill expanding left→right with glow
             ↑ bright pulse rides leading edge
```

At completion, a glow flash signals the lock.

## Function signature

```js
addBarFillPulse(tl, sel, at, opts)
```

| Param | Type | Description |
|---|---|---|
| `tl` | GSAP Timeline | Host timeline (paused) |
| `sel` | string | CSS selector for the `.bar-fill-pulse` wrapper |
| `at` | number | Timeline start time in seconds |
| `opts.percent` | number | Target fill percent 0–100 (reads `data-percent` attr if omitted) |
| `opts.duration` | number | Fill duration in seconds (default `1.4`) |

## Required tokens

```
--accent
```

Fallback baked in (`#E97458`). Override `--bfp-width` (default `900px`) and `--bfp-height` (default `24px`) to resize.

## HTML element

```html
<div class="bar-fill-pulse" data-percent="87">
  <div class="bfp-track">
    <div class="bfp-fill"></div>
    <div class="bfp-pulse"></div>
  </div>
</div>
```

## SFX coupling (REQUIRED — add to host index.html)

| Cue | Count | Offset from `at` | `data-track-index` | Volume |
|---|---|---|---|---|
| `cinematic-whoosh` | 1 | `+0.0` (fill starts) | 3 | 0.11 |
| `scale-slam` | 1 | `+duration` (bar locks) | 4 | 0.15 |

Total: **2 `<audio>` elements** per bar-fill-pulse instance.

### Exact `<audio>` snippet (for `at=0`, `duration=1.4`):

```html
<!-- bar-fill-pulse SFX -->
<audio id="sfx-bfp-whoosh" class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="0.0" data-duration="0.84" data-track-index="3" data-volume="0.11"></audio>
<audio id="sfx-bfp-slam"   class="clip" src="assets/sfx/scale-slam.mp3"
       data-start="1.4" data-duration="0.73" data-track-index="4" data-volume="0.15"></audio>
```

## Customizing

- Change bar width/height: set `--bfp-width` / `--bfp-height` on `.bar-fill-pulse` or a parent.
- Change accent color: override `--accent`.
- For a different `at`, recalculate `data-start` for both SFX as `at + offset`.
- The pulse width is fixed at 80px. For a thinner bar (`--bfp-height: 12px`), you may want to reduce the pulse width via a CSS override on `.bfp-pulse { width: 48px; }`.

## Gotchas

- `overflow: visible` on `.bfp-track` is intentional — the pulse extends 4px above/below the track. Don't add `overflow: hidden` or the pulse will clip.
- The fill uses `color-mix(in srgb, ...)` for the right-edge brightening. This requires a modern browser (Chrome 111+, Firefox 113+). HyperFrames' renderer is Chromium-based, so this is safe for render. For preview in older Safari, add a fallback.
- `width: 0%` is set at t=0 (not the element's CSS default). Don't set `width` in CSS — the function controls it.

## Sync cues

```bash
bash scripts/sync-video-sfx.sh videos/<slug> cinematic-whoosh scale-slam
```
