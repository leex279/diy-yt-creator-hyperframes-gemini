# highlight-marker-sweep — Recipe

Animates a hand-drawn-style yellow/orange marker highlight sweeping left-to-right
under a text phrase. Uses an SVG path with `stroke-dashoffset` animation. The
path is deterministically wavy (sine modulation, 2px amplitude) so it reads as
hand-drawn without relying on `Math.random()`. Color defaults to
`var(--marker, #FFD93D)` with `mix-blend-mode: multiply` so it behaves like
a real highlighter behind the text.

## Wiring

Paste-in component. Merge three sections from `component.html`:

1. **HTML** — the `.highlight-marker` span wrapping your text, wherever
   the highlight should appear in your host composition.
2. **CSS** — the `<style>` block into your host `<style>`.
3. **JS** — the `<script>` block (`addHighlightMarkerSweep`) into your host
   `<script>`, then call it from the root timeline.

## Function signature

```js
addHighlightMarkerSweep(tl, sel, at, opts)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | gsap.timeline | — | Paused root timeline |
| `sel` | string | — | CSS selector for the `.highlight-marker` element |
| `at` | number | — | Time on tl when the sweep begins (seconds) |
| `opts.duration` | number | `0.5` | Sweep draw duration (seconds) |
| `opts.color` | string | `'var(--marker, #FFD93D)'` | Stroke color override |

## SFX coupling

| Cue | Offset from `at` | `data-volume` | `data-track-index` | Description |
|---|---|---|---|---|
| `strike-cross` | `+0.0` | `0.11` | `3` | Marker sweep begins |

### Audio wiring snippet (at=8.5)

```html
<audio id="sfx-hm-1" class="clip" src="assets/sfx/strike-cross.mp3"
       data-start="8.50" data-duration="0.63" data-track-index="3" data-volume="0.11"></audio>
```

### Sync cues script

```bash
bash scripts/sync-video-sfx.sh videos/<slug> strike-cross
```

## Alignment check

The `strike-cross` cue fires at exactly `at + 0.0`. Drift ≤ 0.05s — the
marker sweep and the scratch sound must feel simultaneous. Adjust
`data-start` to match the GSAP insertion time exactly.

## Full example

```html
<p style="font-size: 64px; font-weight: 700; color: #fff;">
  The future is
  <span class="highlight-marker" id="hm-main">
    <span class="hm-text">right now</span>
    <svg class="hm-sweep" aria-hidden="true"></svg>
  </span>
</p>
```

```js
addHighlightMarkerSweep(tl, "#hm-main", P3 + 4.0, { duration: 0.6, color: '#FFD93D' });
```

## Gotchas

- The SVG path is measured via `getBoundingClientRect` on `.hm-text` at call
  time. The element must be in the DOM and have computed layout. If the text
  is inside a parent with `opacity: 0`, measurement returns 0 width. Set the
  parent to `opacity: 0.01` (invisible but laid out) before calling, or call
  after a small offset past the entrance tween.
- `mix-blend-mode: multiply` means on a dark canvas the marker appears very
  faint or invisible (multiply darkens). On dark backgrounds, switch blend mode
  to `screen` or `overlay` via the `.hm-path` CSS override in the host style:
  ```css
  .hm-path { mix-blend-mode: screen; opacity: 0.7; }
  ```
- The SVG auto-sizes to the text width. No manual width needed.
- Path waviness: amplitude 2px, 2 sine periods across the text width. To
  increase the hand-drawn feel, edit `amp` and `periods` in the JS (those
  constants are documented in the source).
- For multiple highlights on one composition, give each a unique id:
  `id="hm-1"`, `id="hm-2"`, etc. Call `addHighlightMarkerSweep` once per element.
