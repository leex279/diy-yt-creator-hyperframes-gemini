# liquid-reveal — Recipe

Content emerges from a vertical liquid wipe. An SVG mask with a deterministic
wavy bottom edge sweeps from off-canvas to off-canvas, revealing the element
beneath. Two wave layers (primary + slow secondary) give depth.

## SFX Coupling

| Cue               | Offset from `at` | data-volume | track-index | Notes                          |
|-------------------|-----------------|-------------|-------------|--------------------------------|
| `cinematic-whoosh`| `+0.0`          | `0.11`      | `3`         | Covers the wipe onset (0.84s). |

**Exact `<audio>` snippet** (wire in host `index.html`; replace `<AT>` with the `at` value):

```html
<audio id="sfx-lr-whoosh-1"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<AT>"
       data-duration="0.84"
       data-track-index="3"
       data-volume="0.11"></audio>
```

**Alignment check:** `data-start` must equal the `at` argument passed to `addLiquidReveal`.
Drift ≤ 0.05s required (percussive wipe onset).

## HTML slot

```html
<div class="liquid-reveal" data-liquid id="my-reveal"
     style="width:800px; height:400px;">
  <div class="lr-content">
    <!-- Your content here -->
  </div>
  <svg class="lr-mask" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path class="lr-ink-primary" id="lr-ink-p"/>
    <path class="lr-ink-secondary" id="lr-ink-s"/>
  </svg>
</div>
```

**Required:** set explicit `width` and `height` on the `.liquid-reveal` wrapper
(inline style or CSS class) — `getBoundingClientRect()` reads these at call time.

## CSS

Merge the `<style>` block from `component.html` into your host `<style>`.

Override ink color per composition:

```css
:root { --liquid: #06080F; } /* deep navy for google-cinematic palette */
```

## JS

Paste the `addLiquidReveal` function from `component.html` into your host `<script>`.

```js
// Reveal content at phase start
addLiquidReveal(tl, "#my-reveal", P1 + 0.5);

// Upward wipe, faster
addLiquidReveal(tl, "#my-reveal", P2 + 1.0, { duration: 1.0, direction: 'up' });
```

## Opts reference

| Option      | Default                    | Description                               |
|-------------|---------------------------|-------------------------------------------|
| `duration`  | `1.4`                     | Seconds for primary wave wipe             |
| `color`     | `var(--liquid, #1A1A2E)`  | SVG fill color (set via CSS --liquid var) |
| `direction` | `'down'`                  | `'down'` or `'up'`                        |

## Constraints

- Call `addLiquidReveal` after the DOM layout phase (inside `DOMContentLoaded` or
  after the GSAP timeline is created synchronously). Paths compute from live `getBoundingClientRect()`.
- Multiple instances on the same page: safe — each call assigns a unique suffix to the path IDs.
- Wire `cinematic-whoosh` in `sfx-cues.txt` and run `scripts/sync-video-sfx.sh` before preview.
- Do NOT reference `shared/lib/...` at runtime. Copy `component.html` content inline.
