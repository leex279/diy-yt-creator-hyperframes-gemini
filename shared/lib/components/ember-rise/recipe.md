# ember-rise — Recipe

30+ glowing ember particles rising upward like cinders from a fire. Each ember is
an SVG circle with a radial-gradient fill (orange→transparent). Spawned across the
bottom of the canvas, each rises Y from 1920 → –80 with sinusoidal horizontal drift
and opacity fade-in/out. Staggered spawns over `totalDuration/3` so the fire reads
as continuous. Designed as ambient — runs for the full composition duration.

PRNG: mulberry32, seed `0xEMBER = 0x454D4245`. Fully deterministic.

## SFX Coupling

| Cue                | Offset from `at` | `data-volume` | `data-track-index` | Notes                                      |
|--------------------|------------------|---------------|--------------------|--------------------------------------------|
| `cinematic-whoosh` | `+0.00s`         | `0.06`        | `3`                | Quieter than default — sustained ambient   |

Note: volume `0.06` is intentionally below the table default of `0.11` because
this is a persistent ambient effect, not a percussive hit. The whoosh signals
"fire started" rather than commanding attention.

### `<audio>` wiring snippet (paste into host `index.html`)

```html
<!-- ember-rise ambient SFX — single whoosh at onset -->
<audio id="sfx-ember-whoosh"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="0.0"
       data-duration="0.84"
       data-track-index="3"
       data-volume="0.06"></audio>
```

Replace `data-start="0.0"` with the exact `at` passed to `addEmberRise`.

## HTML

```html
<div id="ember-rise" data-no-capture></div>
```

`data-no-capture` prevents shader transitions from sampling it as a texture.
Place above the background layer, below foreground content.

## JS function signature

```js
addEmberRise(tl, containerSel, at, opts)
```

| Param                | Default | Description                                          |
|----------------------|---------|------------------------------------------------------|
| `tl`                 | —       | Host GSAP timeline (paused)                          |
| `containerSel`       | —       | CSS selector for the host `<div>`                    |
| `at`                 | —       | Timeline position where the embers start             |
| `opts.totalDuration` | `24`    | Total seconds the effect runs                        |
| `opts.count`         | `30`    | Number of ember particles                            |
| `opts.riseDuration`  | `4`     | Seconds each ember takes to rise bottom to top       |

## Dependencies

- GSAP 3 (loaded by HyperFrames host page)
- No external assets — pure SVG/GSAP

## Gotchas

- **Finite repeats only.** The rise animation is a single `tl.to()` per particle —
  no `repeat: -1`. For a longer composition, increase `count` and `spawnWindow` so
  more particles are spread across time rather than repeating.
- **`data-no-capture` is required.** Without it, HyperFrames' shader transition
  system may try to snapshot the particle layer and bake it into the transition
  texture, producing a frozen ember frame during scene changes.
- The SVG uses `overflow: hidden` on the container so particles clipping off the
  top of the canvas are hidden naturally without visual glitching at the boundary.
