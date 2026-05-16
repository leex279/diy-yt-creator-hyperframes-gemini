# shockwave-ring — Recipe

Expanding SVG stroke-ring from a configurable origin. Animates `r` 0 → 800px with
stroke-opacity 1→0 over 0.7s. Chromatic edge bleed: red + cyan clone rings offset
±3px on the Y axis, 10ms delayed. Optional secondary ring at 50% scale expands
behind the primary for layered depth.

## SFX Coupling

| Cue            | Offset from `at` | `data-volume` | `data-track-index` | Notes                        |
|----------------|------------------|---------------|--------------------|------------------------------|
| `impact-slam`  | `+0.00s`         | `0.15`        | `3`                | Percussive — drift ≤ 0.05s   |
| `screen-shake` | `+0.00s`         | `0.11`        | `4`                | Layered with slam             |

### `<audio>` wiring snippet (paste into host `index.html`)

```html
<!-- shockwave-ring SFX — fire both at the same data-start as addShockwaveRing at -->
<audio id="sfx-sw-slam"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="4.0"
       data-duration="0.63"
       data-track-index="3"
       data-volume="0.15"></audio>
<audio id="sfx-sw-shake"
       class="clip"
       src="assets/sfx/screen-shake.mp3"
       data-start="4.0"
       data-duration="0.52"
       data-track-index="4"
       data-volume="0.11"></audio>
```

Replace `data-start="4.0"` with the exact visual trigger time from the GSAP timeline.
Per `.claude/rules/audio-design.md`, percussive cues must be within ≤ 0.05s of the
visual event.

## HTML

```html
<div class="shockwave-ring"></div>
```

Position in the z-order above content being "hit", below UI chrome.

## JS function signature

```js
addShockwaveRing(tl, containerSel, at, opts)
```

| Param          | Default                      | Description                                 |
|----------------|------------------------------|---------------------------------------------|
| `tl`           | —                            | Host GSAP timeline (paused)                 |
| `containerSel` | —                            | CSS selector for the host `<div>`           |
| `at`           | —                            | Timeline position in seconds                |
| `opts.originX` | `540`                        | Center X in canvas px                       |
| `opts.originY` | `960`                        | Center Y in canvas px                       |
| `opts.duration`| `0.7`                        | Total animation duration                    |
| `opts.color`   | `var(--shockwave, #FFFFFF)`  | Stroke color CSS value                      |
| `opts.maxRadius`| `800`                       | Outer ring max radius in px                 |
| `opts.inner`   | `true`                       | Show 50%-scale secondary ring behind primary|

## Dependencies

- GSAP 3 (loaded by HyperFrames host page)
- No external assets — pure SVG/GSAP

## Gotchas

- The SVG uses `overflow: visible` so rings that exceed the 1080px canvas edge clip
  only at the browser viewport, not at the SVG boundary. This is intentional — the
  ring should bleed past the canvas edges for full-impact feel.
- The function is idempotent: calling it twice with the same `containerSel` removes
  the previously-injected SVG before adding a new one.
- If the composition uses `transform: scale(...)` on the host div, `originX/originY`
  must be in unscaled canvas coordinates.
