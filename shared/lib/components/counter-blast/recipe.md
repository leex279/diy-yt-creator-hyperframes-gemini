# Recipe: counter-blast

Number flips rapidly through values (10 tick frames over ~1.0s), then slams and locks on the target with a scale-pop and glow flash.

## What it produces

```
   (tick tick tick...)
        64  ← slams in with scale pop + glow flash
```

The counter element flicks from 0 through intermediate values to the target number. At lock time, a scale-punch (`back.out(2.2)`) and brief glow flash make the landing hit.

## Function signature

```js
addCounterBlast(tl, sel, at, opts)
```

| Param | Type | Description |
|---|---|---|
| `tl` | GSAP Timeline | Host timeline (paused) |
| `sel` | string | CSS selector for the `.counter-blast` span |
| `at` | number | Timeline start time in seconds |
| `opts.target` | number | Final number to lock on (reads `data-target` attr if omitted) |
| `opts.duration` | number | Total animation length (default `1.2`s) |

## Required tokens

```
--sans, --accent
```

Fallbacks baked in (`'Inter'`, `#E97458`). Override `--counter-blast-size` on the element or a parent to change font-size.

## HTML element

```html
<span class="counter-blast" data-target="64">0</span>
```

The initial `0` content is what shows before `at` fires. The function sets opacity to 0 at t=0 so it stays invisible until the reveal.

## SFX coupling (REQUIRED — add to host index.html)

| Cue | Count | Offset from `at` | `data-track-index` | Volume |
|---|---|---|---|---|
| `pop` | 10 | +0.0, +0.1, +0.2, … +0.9 | 3 (sequential — no overlap, each 0.52s, next starts 0.1s later → safe) | 0.10 |
| `impact-slam` | 1 | `at + (duration - 0.2)` = `at + 1.0` for default 1.2s | 4 | 0.15 |

Total: **11 `<audio>` elements** per counter-blast instance.

### Exact `<audio>` snippet (for `at=0`, `duration=1.2`, track base 3):

```html
<!-- counter-blast ticks (10 × pop on track 3, sequential) -->
<audio id="sfx-cb-tick-0"  class="clip" src="assets/sfx/pop.mp3" data-start="0.0" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-1"  class="clip" src="assets/sfx/pop.mp3" data-start="0.1" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-2"  class="clip" src="assets/sfx/pop.mp3" data-start="0.2" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-3"  class="clip" src="assets/sfx/pop.mp3" data-start="0.3" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-4"  class="clip" src="assets/sfx/pop.mp3" data-start="0.4" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-5"  class="clip" src="assets/sfx/pop.mp3" data-start="0.5" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-6"  class="clip" src="assets/sfx/pop.mp3" data-start="0.6" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-7"  class="clip" src="assets/sfx/pop.mp3" data-start="0.7" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-8"  class="clip" src="assets/sfx/pop.mp3" data-start="0.8" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-tick-9"  class="clip" src="assets/sfx/pop.mp3" data-start="0.9" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<!-- counter-blast lock slam (track 4) -->
<audio id="sfx-cb-slam"    class="clip" src="assets/sfx/impact-slam.mp3" data-start="1.0" data-duration="0.63" data-track-index="4" data-volume="0.15"></audio>
```

**Track-overlap note**: `pop` is 0.52s, ticks are 0.1s apart. Each tick on track 3 starts while the previous is still audible. HyperFrames track-overlap rules apply to `data-track-index` clips with overlapping `[start, start+duration)` windows. To avoid lint errors, stagger ticks across tracks 3 and 4 alternating, **or** keep all ticks on track 3 and accept that the linter may flag overlap — test with `npx hyperframes lint` and resolve if needed. Alternatively use the alternating-track pattern shown in the sandbox.

## Customizing

- Change the target: set `data-target="128"` on the span or pass `opts.target`.
- Change font size: set `--counter-blast-size: 200px` on a parent.
- Change accent color: override `--accent` on the element.
- For a different `at` offset, recalculate all SFX `data-start` values as `at + tick_offset`.

## Gotchas

- The `proxy` object in the GSAP tween must be declared outside the function-scope if you need multiple counters — otherwise they share the same proxy. The implementation above is safe for a single counter per host timeline. For multiple, pass unique `opts.proxy` objects or re-implement with a closure per call.
- `tl.from()` is NOT used — the hidden-until-reveal pattern uses explicit `tl.set(sel, { opacity:0 }, 0)` so the element is invisible from frame 0 during scrub.
- The lock time is `at + duration - 0.2` (the slam starts 0.2s before the full duration). The `impact-slam` SFX `data-start` must equal this value.

## Sync cues

```bash
bash scripts/sync-video-sfx.sh videos/<slug> pop impact-slam
```
