# typewriter-line — Recipe

Single line of text revealed character-by-character with a blinking cursor.
After typing, the cursor performs a finite blink cycle then fades on an
"enter" press cue. All animation is GSAP-driven — no CSS `@keyframes`,
no `repeat: -1`.

## Wiring

Paste-in component. Merge three sections from `component.html`:

1. **HTML** — the `.typewriter-line` div (with `data-typing-text`) into
   your host composition wherever the typed line should appear.
2. **CSS** — the `<style>` block into your host `<style>`.
3. **JS** — the `<script>` block (`addTypewriterLine`) into your host
   `<script>`, then call it from the root timeline.

## Slots

| Attribute | Required | Description |
|---|---|---|
| `data-typing-text` | yes | The text string to type. Spaces are typed as-is. |

## Function signature

```js
addTypewriterLine(tl, sel, at, opts)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | gsap.timeline | — | Paused root timeline |
| `sel` | string | — | CSS selector for the `.typewriter-line` element |
| `at` | number | — | Time on tl when typing begins (seconds) |
| `opts.duration` | number | `2.0` | Total typing duration (seconds) |
| `opts.blinkRate` | number | `0.5` | Seconds per blink on/off cycle |

## SFX coupling

Wire `pop` at every ~5 characters typed (0.05 volume — subtle key clicks).
Formula for N pops: `at + (5k / total_chars) * duration` for k=1, 2, …, floor(total_chars/5).

| Cue | Offset formula | `data-volume` | `data-track-index` | Description |
|---|---|---|---|---|
| `pop` | `at + (5/chars)*duration` | `0.05` | `3` | ~5 chars typed |
| `pop` | `at + (10/chars)*duration` | `0.05` | `3` | ~10 chars typed |
| … | repeat every 5 chars | `0.05` | `3` | (sequential, non-overlapping) |

Sequential pops on the same track index are fine as long as they are
≥ 0.52s apart (pop duration). For slow typing (> 0.1s/char) this is
always satisfied.

### Audio wiring snippet ("hello world" = 11 chars, 2.0s duration, at=1.0)

Pop at char 5 → t=1.0+(5/11)*2.0 = 1.91s ≈ 1.90
Pop at char 10 → t=1.0+(10/11)*2.0 = 2.82s ≈ 2.80

```html
<audio id="sfx-tw-1a" class="clip" src="assets/sfx/pop.mp3"
       data-start="1.90" data-duration="0.52" data-track-index="3" data-volume="0.05"></audio>
<audio id="sfx-tw-1b" class="clip" src="assets/sfx/pop.mp3"
       data-start="2.80" data-duration="0.52" data-track-index="3" data-volume="0.05"></audio>
```

### Sync cues script

```bash
bash scripts/sync-video-sfx.sh videos/<slug> pop
```

## Alignment check

Each `pop` must fire within 0.05s of when the ~5th, ~10th … character
appears on screen. Compute exact offsets from `(k*5 / total_chars) * duration`
— do not round to the nearest 0.1s. Drift ≤ 0.05s for percussive cues.

## Full example

```html
<div class="typewriter-line" id="tw-cmd" data-typing-text="$ claude --model sonnet-4-6">
  <span class="tl-text"></span><span class="tl-cursor">|</span>
</div>
```

```js
addTypewriterLine(tl, "#tw-cmd", P2 + 1.5, { duration: 3.0, blinkRate: 0.4 });
```

## Gotchas

- Font size, weight, color, and family are inherited from the parent — set
  them on the `.typewriter-line` element itself or a parent.
- Cursor blink cycles: `Math.floor(duration / blinkRate)`. For a 2s type +
  0.5s blink rate that's 4 cycles. The cursor stops blinking after typing
  completes and fades out at `at + duration + 0.3s`.
- Multi-line text is NOT supported — the component is one logical line.
  For a multi-line terminal block, stack multiple `.typewriter-line` elements
  and chain their `at` values sequentially.
- `data-typing-text` must be set in HTML before the timeline JS runs.
- The counter tween uses `snap: { chars: 1 }` to ensure only whole characters
  appear (no half-visible fractional states at render frame boundaries).
