# notification-toast-stack — Recipe

macOS-style notification toasts that stack vertically in the top-right corner
of the canvas. Up to N toasts slide in from off-canvas right with a bouncy
spring ease, persist for a hold period, then slide out together.

## Wiring

This is a **paste-in component** (no `data-composition-src`). Merge three
sections from `component.html` into your host composition:

1. **HTML** — the `.notification-toast-stack` div (with `data-toasts` JSON)
   into the root `<div data-composition-id="...">` at a layer that renders
   in front of background content.
2. **CSS** — the `<style>` block into your host `<style>`.
3. **JS** — the `<script>` block (containing `addNotificationToastStack`)
   into your host `<script>`, then call it from the root timeline.

## Slots

| Attribute | Required | Description |
|---|---|---|
| `data-toasts` | yes | JSON array of `{icon, title, sub}` objects. `icon` is any CSS color string. |

## Function signature

```js
addNotificationToastStack(tl, sel, at, opts)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | gsap.timeline | — | Paused root timeline |
| `sel` | string | — | CSS selector for the `.notification-toast-stack` element |
| `at` | number | — | Time on tl when the first toast slides in (seconds) |
| `opts.holdSec` | number | `4` | Seconds all toasts remain visible after the last one slides in |
| `opts.stagger` | number | `0.6` | Delay between consecutive toast slide-ins (seconds) |

## SFX coupling

| Cue | Offset from `at` | `data-volume` | `data-track-index` | Description |
|---|---|---|---|---|
| `pop` | `+0.0` | `0.10` | `3` | First toast slides in |
| `pop` | `+stagger` | `0.10` | `4` | Second toast slides in |
| `pop` | `+stagger*2` | `0.10` | `5` | Third toast slides in |

### Audio wiring snippet (3 toasts, stagger=0.6, at=2.0)

```html
<audio id="sfx-toast-1" class="clip" src="assets/sfx/pop.mp3"
       data-start="2.00" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-toast-2" class="clip" src="assets/sfx/pop.mp3"
       data-start="2.60" data-duration="0.52" data-track-index="4" data-volume="0.10"></audio>
<audio id="sfx-toast-3" class="clip" src="assets/sfx/pop.mp3"
       data-start="3.20" data-duration="0.52" data-track-index="5" data-volume="0.10"></audio>
```

Update `data-start` values to match your `at` value exactly.

### Sync cues script

```bash
bash scripts/sync-video-sfx.sh videos/<slug> pop
```

## Alignment check

Three sequential `pop` cues fire at `at + 0`, `at + stagger`, `at + stagger*2`.
Each toast slide-in animation starts at the same time as its corresponding
`pop`. Drift between `data-start` and the GSAP insertion time must be ≤ 0.05s
(percussive cue).

## Full example

```html
<div class="notification-toast-stack" id="toast-stack-1"
  data-toasts='[
    {"icon":"#FF6B6B","title":"Build complete","sub":"Render finished in 4m"},
    {"icon":"#4FC3F7","title":"New message","sub":"Cole: check the PR"},
    {"icon":"#A5D6A7","title":"Deploy ready","sub":"Vercel · prod · 12s ago"}
  ]'>
</div>
```

```js
// In root timeline script, after tl is created:
addNotificationToastStack(tl, "#toast-stack-1", P1 + 1.0, { holdSec: 4, stagger: 0.6 });
```

## Gotchas

- `data-toasts` must be valid JSON. Single quotes inside JSON values will
  break parsing — use the HTML attribute with single-quote wrapper and
  double-quotes inside the JSON.
- The toast DOM is built at call time. If the element isn't in the DOM when
  `addNotificationToastStack` is called, it silently returns.
- `holdSec` starts after the *last* toast finishes sliding in, not from `at`.
  Total phase duration = `stagger * (n-1) + 0.55 + holdSec + 0.45`.
- backdrop-filter renders in HyperFrames' Chromium renderer. No polyfill needed.
- Track indices 3, 4, 5 are used for the three pop cues. If other SFX in the
  same phase use those tracks, bump the toast pop tracks up to avoid overlap.
