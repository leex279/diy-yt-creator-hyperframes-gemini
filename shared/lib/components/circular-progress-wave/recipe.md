# Recipe: circular-progress-wave

Circular SVG progress arc fills 0→target%. An outer track ring sits at 8% opacity. A bright bead/wave rides the arc's leading edge via GSAP rotation. The center number increments in lockstep. On completion, a glow flash signals the lock.

## What it produces

```
     ╭─────╮
   ╱    75    ╲   ← center number ticks 0→75
  │      %     │  ← unit label
   ╲          ╱
     ╰── ●───╯    ← bright bead rides leading edge
```

## Function signature

```js
addCircularProgressWave(tl, sel, at, opts)
```

| Param | Type | Description |
|---|---|---|
| `tl` | GSAP Timeline | Host timeline (paused) |
| `sel` | string | CSS selector for `.circular-progress-wave` wrapper |
| `at` | number | Timeline start time in seconds |
| `opts.target` | number | Target percent 0–100 (reads `data-target` attr if omitted) |
| `opts.duration` | number | Fill duration in seconds (default `1.6`) |

## Required tokens

```
--accent, --sans, --mono, --text
```

Fallbacks baked in. Override sizing via:

```css
.circular-progress-wave {
  --cpw-size: 400px;        /* wrapper + SVG size */
  --cpw-number-size: 100px; /* center number font-size */
  --cpw-unit-size: 44px;    /* "%" label */
}
```

## HTML element

```html
<div class="circular-progress-wave" data-target="75">
  <svg class="cpw-svg" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
    <circle class="cpw-track" cx="120" cy="120" r="100"/>
    <circle class="cpw-arc"   cx="120" cy="120" r="100"/>
    <circle class="cpw-bead"  cx="120" cy="20"  r="8"/>
  </svg>
  <div class="cpw-center">
    <span class="cpw-number">0</span>
    <span class="cpw-unit">%</span>
  </div>
</div>
```

## SFX coupling (REQUIRED — add to host index.html)

| Cue | Count | Offset from `at` | `data-track-index` | Volume |
|---|---|---|---|---|
| `cinematic-whoosh` | 1 | `+0.0` (arc starts) | 3 | 0.11 |
| `pop` | 1 | `+duration` (arc locks) | 4 | 0.10 |

Total: **2 `<audio>` elements** per circular-progress-wave instance.

### Exact `<audio>` snippet (for `at=0`, `duration=1.6`):

```html
<!-- circular-progress-wave SFX -->
<audio id="sfx-cpw-whoosh" class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="0.0" data-duration="0.84" data-track-index="3" data-volume="0.11"></audio>
<audio id="sfx-cpw-pop"    class="clip" src="assets/sfx/pop.mp3"
       data-start="1.6" data-duration="0.52" data-track-index="4" data-volume="0.10"></audio>
```

## How the bead works

The `.cpw-bead` is a `<circle>` at `cx="120" cy="20"` (top of the circle, i.e., 12 o'clock position). The SVG itself is rotated −90° via CSS so 12 o'clock maps to the 12 o'clock position on screen. GSAP animates `rotation` on the bead with `transformOrigin: '120px 120px'` (the circle's center), which sweeps it clockwise around the arc matching the fill progress.

Circumference formula: `2π × r = 2 × 3.14159 × 100 ≈ 628.32`. This value is hardcoded in both CSS (`--cpw-circumference`) and JS (`CIRC`).

## Customizing

- **No center number**: remove `.cpw-center` from the HTML and the `proxy` tween from the `addCircularProgressWave` function (or skip calling it).
- **Different radius**: if you change `r` from 100, also update `--cpw-circumference` CSS var and `CIRC` in JS to `2 × Math.PI × newR`.
- **Multiple arcs on one canvas**: give each a unique wrapper selector and call `addCircularProgressWave` once per arc. Ensure SFX IDs are unique.

## Gotchas

- `stroke-dasharray` and `stroke-dashoffset` use `pathLength` units equal to the actual circumference (628.32). Don't set `pathLength="1"` on the `<circle>` elements — that changes the dashoffset coordinate space.
- The SVG `transform: rotate(-90deg)` is on the `<svg>` element via CSS, not GSAP. GSAP animates the bead's rotation independently inside that already-rotated coordinate space. Net visual result: bead starts at 12 o'clock and sweeps clockwise.
- `filter: drop-shadow(...)` on SVG elements is SVG filter, not CSS box-shadow. GSAP `to()` on `filter` is safe in modern Chromium (HyperFrames renderer).

## Sync cues

```bash
bash scripts/sync-video-sfx.sh videos/<slug> cinematic-whoosh pop
```
