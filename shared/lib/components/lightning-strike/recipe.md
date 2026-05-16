# lightning-strike — Recipe

Jagged SVG lightning bolt drawn top-to-bottom via `stroke-dashoffset` from
path-length → 0 over 0.15s. Three visual layers: cyan glow halo, blue-white core
stroke, brief full-canvas white flash (opacity 0.4 for 50ms) at moment-of-strike.
Path is a fixed deterministic zigzag; override via `[data-strike-path]` attribute.

## SFX Coupling

| Cue           | Offset from `at` | `data-volume` | `data-track-index` | Notes                        |
|---------------|------------------|---------------|--------------------|------------------------------|
| `glitch-zap`  | `+0.00s`         | `0.09`        | `3`                | Zap onset — at bolt draw     |
| `impact-slam` | `+0.20s`         | `0.15`        | `4`                | Impact ground — at end of draw |

### `<audio>` wiring snippet (paste into host `index.html`)

```html
<!-- lightning-strike SFX — zap at draw, slam at ground strike -->
<audio id="sfx-ls-zap"
       class="clip"
       src="assets/sfx/glitch-zap.mp3"
       data-start="8.0"
       data-duration="0.52"
       data-track-index="3"
       data-volume="0.09"></audio>
<audio id="sfx-ls-slam"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="8.2"
       data-duration="0.63"
       data-track-index="4"
       data-volume="0.15"></audio>
```

Replace `data-start="8.0"` with the exact `at` passed to `addLightningStrike`.
The slam fires at `at + 0.20` (the end of the 0.15s draw phase + 0.05s settle).
Per `.claude/rules/audio-design.md`, percussive cues must be within ≤ 0.05s of
their visual trigger.

## HTML

```html
<div class="lightning-strike">
  <svg class="ls-svg" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <filter id="ls-glow" x="-50%" y="-10%" width="200%" height="120%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <path class="ls-halo" fill="none"
          stroke="var(--lightning-glow, #44DDFF)"
          stroke-width="18" stroke-linecap="round" stroke-linejoin="round"
          filter="url(#ls-glow)"
          d="M 560 0 L 480 260 L 620 310 L 440 620 L 600 680 L 380 1000 L 560 1060 L 320 1380 L 500 1430 L 280 1920"/>
    <path class="ls-core" fill="none"
          stroke="var(--lightning-core, #DDEEFF)"
          stroke-width="5" stroke-linecap="round" stroke-linejoin="round"
          d="M 560 0 L 480 260 L 620 310 L 440 620 L 600 680 L 380 1000 L 560 1060 L 320 1380 L 500 1430 L 280 1920"/>
  </svg>
  <div class="ls-flash"></div>
</div>
```

### Custom path override

```html
<div class="lightning-strike" data-strike-path="M 540 0 L 460 300 L 600 350 L 420 700 L 560 1920">
  ...
</div>
```

## JS function signature

```js
addLightningStrike(tl, containerSel, at, opts)
```

| Param           | Default | Description                                     |
|-----------------|---------|-------------------------------------------------|
| `tl`            | —       | Host GSAP timeline (paused)                     |
| `containerSel`  | —       | CSS selector for the `.lightning-strike` div    |
| `at`            | —       | Timeline position in seconds                    |
| `opts.duration` | `0.4`   | Total animation duration (draw + flash + fade)  |

## CSS variables

| Variable              | Default    | Description             |
|-----------------------|------------|-------------------------|
| `--lightning-glow`    | `#44DDFF`  | Halo / glow stroke color|
| `--lightning-core`    | `#DDEEFF`  | Core bolt stroke color  |

## Dependencies

- GSAP 3 (loaded by HyperFrames host page)
- `getTotalLength()` on SVG `<path>` — available in all modern browsers + headless Chrome renderer

## Gotchas

- The `<filter id="ls-glow">` ID must be unique per page. If you use two
  lightning strikes on the same canvas, rename the filter ID in each instance.
- The `stroke-dasharray` / `stroke-dashoffset` are set both in CSS (as fallback)
  and overwritten by JS from `getTotalLength()`. The CSS value (3000) may not
  match the actual path length — the JS override is authoritative.
- `overflow: hidden` on the container clips the bolt at canvas edges. Set
  `overflow: visible` if you want the bolt to bleed past the canvas boundary.
