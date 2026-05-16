# camera-flash-pop

## What it does
Full-canvas white screen-flash at 2-frame peak (~67ms) then 0.4s exponential decay, with post-peak chromatic aberration (red +4px / cyan −4px clones). Feels like a photo camera capturing the moment.

## Function
`addCameraFlashPop(tl, sel, at, opts)`

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | GSAP Timeline | — | Host timeline to add tweens to |
| `sel` | string | — | CSS selector for the `.cfp-overlay` div |
| `at` | number | — | Timeline position (seconds) for the flash peak |
| `opts.duration` | number | `0.45` | Total flash duration (peak + decay) in seconds |
| `opts.caRedSel` | string | `'#cfp-ca-red'` | CSS selector for the red CA clone div |
| `opts.caCyanSel` | string | `'#cfp-ca-cyan'` | CSS selector for the cyan CA clone div |

## SFX coupling

| Cue | Offset from `at` | data-volume | Track-index |
|---|---|---|---|
| `impact-slam` | `+0.0s` | `0.15` | `3` |
| `glitch-zap` | `+0.0s` | `0.09` | `4` |

Wire the audio in the host's `index.html`:
```html
<audio id="sfx-cfp-impact"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="<at>"
       data-duration="0.63"
       data-track-index="3"
       data-volume="0.15"></audio>

<audio id="sfx-cfp-glitch"
       class="clip"
       src="assets/sfx/glitch-zap.mp3"
       data-start="<at>"
       data-duration="0.52"
       data-track-index="4"
       data-volume="0.09"></audio>
```
Replace `<at>` with the value passed to `addCameraFlashPop`. Per `.claude/rules/audio-design.md`, percussive drift > 0.05s is a bug.

## Slots
None — the flash is a full-canvas overlay. Place content divs underneath (lower z-index) and they will show through via `mix-blend-mode: screen` during the flash.

## Gotchas
- The three overlay divs (`cfp-overlay`, `cfp-ca-red`, `cfp-ca-cyan`) must be placed **inside** the composition root div, not before or after it.
- `mix-blend-mode: screen` requires the parent background to be non-transparent for the blend to be visible. Ensure the composition root has a background color set.
- If you rename the overlay div IDs, pass `opts.caRedSel` and `opts.caCyanSel` explicitly to `addCameraFlashPop`.
- The CA clones use `z-index: 97/98` — ensure your content sits below 97 or above 99. Content at z-index 0–90 is safe by default.
- Do NOT add `class="clip"` to the overlay divs — they are driven solely by GSAP, not the framework timing system.
