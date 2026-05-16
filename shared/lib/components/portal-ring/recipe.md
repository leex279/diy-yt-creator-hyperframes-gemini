# portal-ring — Recipe

Circular dimensional portal: 3 concentric pulsating rings (outer 600px, mid 400px,
inner 200px diameter) open from a point with a warm-up flash, rotate during a hold
phase, then collapse with a closing flash. Colors driven by CSS var `--portal`.

PRNG: none — fully deterministic, angle math only. Finite rotation repeats
calculated from `Math.ceil(holdSec / rotationPeriod)`.

## SFX Coupling

| Cue                | Offset from `at`                 | `data-volume` | `data-track-index` | Notes              |
|--------------------|----------------------------------|---------------|--------------------|--------------------|
| `cinematic-whoosh` | `+0.00s`                         | `0.11`        | `3`                | Portal open        |
| `cinematic-whoosh` | `at + openDuration + holdSec`    | `0.11`        | `4`                | Portal close       |

Note: two separate `<audio>` elements are required since the same cue fires twice
at different times. HyperFrames does not support seeking/re-triggering a single
audio element — use two IDs.

### `<audio>` wiring snippet (paste into host `index.html`)

```html
<!-- portal-ring SFX — open whoosh at at, close whoosh at at+openDuration+holdSec -->
<audio id="sfx-portal-open"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="12.0"
       data-duration="0.84"
       data-track-index="3"
       data-volume="0.11"></audio>
<audio id="sfx-portal-close"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="15.0"
       data-duration="0.84"
       data-track-index="4"
       data-volume="0.11"></audio>
```

With defaults: `at=12.0, openDuration=1.0, holdSec=2.0` → close whoosh at `12 + 1 + 2 = 15.0`.
Adjust both `data-start` values to match your actual `at` and durations.

## HTML

```html
<div class="portal-ring"></div>
```

No child elements needed — the function injects the SVG and flash div at runtime.

## JS function signature

```js
addPortalRing(tl, containerSel, at, opts)
```

| Param                | Default                    | Description                               |
|----------------------|----------------------------|-------------------------------------------|
| `tl`                 | —                          | Host GSAP timeline (paused)               |
| `containerSel`       | —                          | CSS selector for the host `<div>`         |
| `at`                 | —                          | Timeline position in seconds              |
| `opts.openDuration`  | `1.0`                      | Seconds for portal to open                |
| `opts.holdSec`       | `2.0`                      | Seconds portal stays open                 |
| `opts.closeDuration` | `0.8`                      | Seconds for portal to collapse            |
| `opts.color`         | `var(--portal, #B388FF)`   | Ring stroke / inner fill color            |
| `opts.originX`       | `540`                      | Center X in canvas px                     |
| `opts.originY`       | `960`                      | Center Y in canvas px                     |

## CSS variables

| Variable   | Default    | Description                          |
|------------|------------|--------------------------------------|
| `--portal` | `#B388FF`  | Ring stroke + inner gradient color   |

## Dependencies

- GSAP 3 (loaded by HyperFrames host page)
- No external assets — pure SVG/GSAP

## Gotchas

- **Two SFX audio elements are required** for the open + close whoosh. They must
  be on different track indices (3 + 4) since they may overlap in time.
- **Rotation repeat counts are finite** — calculated as `Math.ceil(holdSec / period)`.
  If `holdSec` is very long (> 30s), the repeat count becomes large but stays finite.
  Never use `repeat: -1`.
- The `.pr-open-flash` div is injected once and reused on subsequent calls. If you
  call `addPortalRing` twice with the same selector, the second call re-uses the
  existing flash element (idempotent).
- `transform-origin` for SVG elements must be set explicitly as `"cx py"` strings
  in pixels. GSAP's `transformOrigin: "50% 50%"` resolves to the SVG bounding box,
  not the canvas origin — always pass the explicit pixel values.
