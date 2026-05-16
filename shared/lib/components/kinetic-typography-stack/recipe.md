# kinetic-typography-stack

## What it does
3–4 words slam in vertically stacked — each with `back.out(1.7)` spring scale (0.72→1.0) + 4-tick ±6px inline shake on land — rhythmically staggered at `+0.4s` each. Words alternate accent colors (orange/purple/blue/green). Last word holds 1s then all fade up and out.

## Function
`addKineticTypographyStack(tl, sel, at, opts)`

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | GSAP Timeline | — | Host timeline to add tweens to |
| `sel` | string | — | CSS selector for the `.kts-stack` container div |
| `at` | number | — | Timeline position (seconds) for word 0 entrance |
| `opts.stagger` | number | `0.4` | Seconds between each word's entrance |
| `opts.holdSec` | number | `1.0` | Seconds all words hold before fade-out |

## SFX coupling

For 3 words with default `stagger: 0.4`:

| Cue | Offset from `at` | data-volume | Track-index |
|---|---|---|---|
| `impact-slam` | `+0.0s` (word 0) | `0.15` | `3` |
| `impact-slam` | `+0.4s` (word 1) | `0.15` | `4` |
| `impact-slam` | `+0.8s` (word 2) | `0.15` | `5` |

Wire the audio in the host's `index.html`:
```html
<audio id="sfx-kts-0"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="<at>"
       data-duration="0.63"
       data-track-index="3"
       data-volume="0.15"></audio>

<audio id="sfx-kts-1"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="<at + 0.4>"
       data-duration="0.63"
       data-track-index="4"
       data-volume="0.15"></audio>

<audio id="sfx-kts-2"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="<at + 0.8>"
       data-duration="0.63"
       data-track-index="5"
       data-volume="0.15"></audio>
```
Replace `<at>` with the value passed to `addKineticTypographyStack`. For 4 words, add a 4th `<audio>` on track-index `6` at `at + 1.2`. Each word needs its own track index because `impact-slam` is 0.63s and the stagger is 0.4s — they overlap in time. Per `.claude/rules/audio-design.md`, percussive drift > 0.05s is a bug.

## Slots

| Attribute | Where | Purpose |
|---|---|---|
| `data-stack-words` | `.kts-stack` container | JSON array of word strings, e.g. `'["FAST.","BOLD.","DONE."]'` |

## CSS variables

| Variable | Default | Purpose |
|---|---|---|
| `--kts-size` | `160px` | Font size for all words |
| `--kts-accent2` | `var(--purple, #A78BFA)` | Color for word 2 |
| `--kts-accent3` | `var(--blue, #60A5FA)` | Color for word 3 |
| `--kts-accent4` | `var(--green, #4ADE80)` | Color for word 4 |
| `--accent` | `#E97458` | Color for word 1 |

## Gotchas
- The function calls `container.innerHTML = ''` at runtime to build word divs fresh. Any pre-existing content inside `.kts-stack` is replaced. Put your `data-stack-words` attribute on the container; the text content is ignored.
- Each `impact-slam` SFX needs its own `data-track-index` because `impact-slam` (0.63s) overlaps with the next slam at 0.4s stagger. Using the same track index causes a lint error (`overlapping_clips`).
- The 4-tick shake runs at `wordAt + 0.05, 0.09, 0.13, 0.17` — these use basic GSAP append to the same element. If you use `overwrite: "auto"` elsewhere on the same element, drop the `overwrite` from those tweens or they'll cancel each other.
- For Shorts (1080×1920), 3 words at 160px fit comfortably. 4 words may be tight — reduce `--kts-size` to 130px or shorten the word strings.
- Font minimums rule: each word at 160px is well above the 140px hero-slam minimum for Shorts. Don't reduce below 140px.
