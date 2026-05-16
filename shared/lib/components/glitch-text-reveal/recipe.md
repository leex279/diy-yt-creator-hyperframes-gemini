# glitch-text-reveal

## What it does
Text materializes through a digital glitch: RGB split (cyan +6px / magenta −8px clones), deterministic scrambled-character swaps for ~0.5s (mulberry32 seed `0xCAFE`), scanline CRT overlay jitter, then settles clean over 0.4s.

## Function
`addGlitchTextReveal(tl, sel, at, opts)`

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | GSAP Timeline | — | Host timeline to add tweens to |
| `sel` | string | — | CSS selector for the text element to reveal |
| `at` | number | — | Timeline position (seconds) for the glitch start |
| `opts.duration` | number | `0.9` | Total reveal duration: glitch window (0.5s) + settle (0.4s) |
| `opts.scanlineSel` | string | `'#gtr-scanline'` | CSS selector for the scanline overlay div |

## SFX coupling

| Cue | Offset from `at` | data-volume | Track-index |
|---|---|---|---|
| `glitch-zap` | `+0.0s` | `0.09` | `3` |
| `glitch-zap` | `+0.3s` | `0.09` | `4` |

Wire the audio in the host's `index.html`:
```html
<audio id="sfx-gtr-1"
       class="clip"
       src="assets/sfx/glitch-zap.mp3"
       data-start="<at>"
       data-duration="0.52"
       data-track-index="3"
       data-volume="0.09"></audio>

<audio id="sfx-gtr-2"
       class="clip"
       src="assets/sfx/glitch-zap.mp3"
       data-start="<at + 0.3>"
       data-duration="0.52"
       data-track-index="4"
       data-volume="0.09"></audio>
```
Replace `<at>` with the value passed to `addGlitchTextReveal`. The second glitch-zap at `+0.3s` hits the mid-reveal stutter beat. Per `.claude/rules/audio-design.md`, percussive drift > 0.05s is a bug. These two elements must be on **different** track indices because `glitch-zap` is 0.52s long — the first cue's window `[at, at+0.52)` overlaps with the second at `at+0.3`. Use track 4 for the second cue.

## Slots

| Element | Role |
|---|---|
| `[class="gtr-target"]` | Text element to receive the glitch reveal. Add this class to your existing text div. |
| `#gtr-scanline` | Full-canvas scanline overlay (paste once per composition root). |

## Gotchas
- The function reads `el.textContent` at call time. Ensure the element already has its final text before calling `addGlitchTextReveal`.
- Clone divs are injected into `el.parentNode`. The parent must have `position: relative` or `position: absolute` so the clones can be absolutely positioned against it.
- The scanline overlay uses `z-index: 90`. Ensure your text content sits at `z-index` ≤ 89 or ≥ 91.
- `mulberry32(0xCAFE)` is fully deterministic — the scramble sequence is identical on every seek/scrub. No `Math.random()`.
- The two sequential `glitch-zap` audio elements on track-index 3 are safe because they don't overlap in time (0.52s duration, 0.3s apart means ~0.22s gap between them).
