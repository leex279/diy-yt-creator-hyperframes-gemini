# film-strip-reveal

## What it does
A horizontal 35mm-film-strip frame slides in from the left with `power3.out` ease (~1.4s), locks into place with a micro-bounce, holds the frame for ~1.6s (content visible in the aperture window), then slides out right. Sprocket holes rendered via repeating CSS gradient on top and bottom strips.

## Function
`addFilmStripReveal(tl, contentSel, at, opts)`

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | GSAP Timeline | — | Host timeline to add tweens to |
| `contentSel` | string | — | CSS selector for `[data-film-content]` inside the frame |
| `at` | number | — | Timeline position (seconds) for the slide-in start |
| `opts.duration` | number | `1.4` | Slide-in entrance duration in seconds |
| `opts.holdSec` | number | `1.6` | How long the frame holds before exiting |
| `opts.frameSel` | string | `'#fsr-frame'` | CSS selector for the `.fsr-frame` container |

## SFX coupling

| Cue | Offset from `at` | data-volume | Track-index |
|---|---|---|---|
| `cinematic-whoosh` | `+0.0s` | `0.11` | `3` |
| `pop` | `+0.7s` | `0.10` | `4` |

Wire the audio in the host's `index.html`:
```html
<audio id="sfx-fsr-whoosh"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<at>"
       data-duration="0.84"
       data-track-index="3"
       data-volume="0.11"></audio>

<audio id="sfx-fsr-pop"
       class="clip"
       src="assets/sfx/pop.mp3"
       data-start="<at + 0.7>"
       data-duration="0.52"
       data-track-index="4"
       data-volume="0.10"></audio>
```
Replace `<at>` with the value passed to `addFilmStripReveal`. The `pop` at `+0.7s` aligns with the frame locking (micro-bounce at `at + duration` where `duration=1.4` → note: adjust if using a shorter duration). Per `.claude/rules/audio-design.md`, percussive drift > 0.05s is a bug.

## Slots

| Selector | Role |
|---|---|
| `[data-film-content]` | Inner content element — text, image, or any HTML. Place inside `#fsr-content-area`. |
| `#fsr-sprockets-top` | Top sprocket strip (auto-rendered via CSS; swap `--film-bg` var) |
| `#fsr-sprockets-bottom` | Bottom sprocket strip |

## CSS variables

| Variable | Default | Purpose |
|---|---|---|
| `--film-bg` | `#1A1A1A` | Film strip body color |
| `--film-hole` | `#000000` | Sprocket punch-out color |
| `--film-edge` | `#333333` | Border lines separating sprockets from aperture |
| `--film-content-bg` | `#0A0E1A` | Aperture window background |
| `--film-text` | `#F5F1EB` | Default text color inside aperture |

## Gotchas
- The frame starts at `x: -1200` — ensure the parent has `overflow: hidden` if you don't want the frame visible during its offscreen state.
- If the canvas is wider than 1080px, increase the `x: -1200` start and `x: 1300` exit values proportionally.
- The `.fsr-frame` uses `position: absolute; top: 50%; transform: translateX(-1200px) translateY(-50%)`. GSAP will override the `translateX` but preserve the `translateY(-50%)` centering only if you don't set `y` on the frame. Don't add `y` tweens.
- The `pop` SFX at `+0.7s` is calibrated for the default `duration: 1.4`. If you pass a custom duration, adjust `data-start` to `at + duration + 0.07` (the micro-bounce start time).
