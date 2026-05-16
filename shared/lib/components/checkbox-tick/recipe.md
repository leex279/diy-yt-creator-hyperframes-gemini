# checkbox-tick — Recipe

Animated SVG checkbox check sequence. Empty box → box pulse → checkmark draws
→ green flash → label fades in. 60×60px rounded square, SVG stroke-dashoffset
animation for the tick, GSAP fill animation for the green flash.

## Wiring

Paste-in component. Merge three sections from `component.html`:

1. **HTML** — the `.checkbox-tick` div (with optional `.ct-label` text)
   into your host composition wherever the checkbox should appear.
2. **CSS** — the `<style>` block into your host `<style>`.
3. **JS** — the `<script>` block (`addCheckboxTick`) into your host
   `<script>`, then call it from the root timeline.

## Slots

| Element | Required | Description |
|---|---|---|
| `.ct-label[data-slot]` | optional | Text label appearing next to the checkbox at `at+0.6` |

## Function signature

```js
addCheckboxTick(tl, sel, at, opts)
```

| Param | Type | Default | Description |
|---|---|---|---|
| `tl` | gsap.timeline | — | Paused root timeline |
| `sel` | string | — | CSS selector for the `.checkbox-tick` element |
| `at` | number | — | Time on tl when box settle begins (seconds) |
| `opts.duration` | number | `0.7` | Total animation envelope (informational; timing is internal) |
| `opts.color` | string | `'var(--check, #69F0AE)'` | Checkmark + border + flash color |

## Animation breakdown

| Offset | What happens | Duration |
|---|---|---|
| `at + 0.00` | Box scale: 1.0 → 0.95 | 0.07s |
| `at + 0.07` | Box scale: 0.95 → 1.05 | 0.08s |
| `at + 0.15` | Box scale: 1.05 → 1.0 | 0.07s |
| `at + 0.15` | Checkmark draws (dashoffset → 0) | 0.30s |
| `at + 0.45` | Rect fill flashes to accent | 0.10s |
| `at + 0.55` | Rect fill returns to base | 0.15s |
| `at + 0.60` | Label fades + slides up | 0.30s |

## SFX coupling

| Cue | Offset from `at` | `data-volume` | `data-track-index` | Description |
|---|---|---|---|---|
| `pop` | `+0.0` | `0.10` | `3` | Box settle |
| `spring-pop` | `+0.15` | `0.11` | `4` | Tick punch |

### Audio wiring snippet (at=14.0)

```html
<audio id="sfx-cb-pop" class="clip" src="assets/sfx/pop.mp3"
       data-start="14.00" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-cb-spring" class="clip" src="assets/sfx/spring-pop.mp3"
       data-start="14.15" data-duration="0.52" data-track-index="4" data-volume="0.11"></audio>
```

Adjust `data-start` to match your `at` value. The 0.15s offset between
`pop` and `spring-pop` must be preserved — it matches the visual moment
when the tick starts drawing.

### Sync cues script

```bash
bash scripts/sync-video-sfx.sh videos/<slug> pop spring-pop
```

## Alignment check

- `pop` fires at `at + 0.0` (box settle): percussive, must be within 0.05s.
- `spring-pop` fires at `at + 0.15` (tick start): percussive, must be within 0.05s.

## Full example

```html
<div class="checkbox-tick" id="cb-deploy" style="font-size: 48px; font-weight: 600; color: #fff;">
  <svg class="ct-box" viewBox="0 0 60 60" width="60" height="60" aria-hidden="true">
    <rect class="ct-rect" x="3" y="3" width="54" height="54" rx="12" ry="12"/>
    <path class="ct-check" d="M14 31 L25 42 L46 19"/>
  </svg>
  <span class="ct-label" data-slot>Deployed to production</span>
</div>
```

```js
addCheckboxTick(tl, "#cb-deploy", P4 + 2.0, { color: '#69F0AE' });
```

## Gotchas

- `ct-check` path `getTotalLength()` is called at timeline build time. The
  SVG must be in the DOM with layout computed. Path is always in the DOM
  (inline SVG), so this is safe without any timing guard.
- `.ct-label` CSS sets `opacity: 0` as initial state. JS sets `y: 8` via
  `gsap.set` at call time. Do not override initial `opacity` in CSS without
  also updating the JS `gsap.set` call.
- Color override applies the `color` value directly via `element.style.stroke`.
  CSS variables (`var(--check, ...)`) resolve correctly here.
- For a checklist of multiple items, give each `.checkbox-tick` a unique id
  and call `addCheckboxTick` once per element with staggered `at` values
  (~5s apart, per the step-by-step-reveal rule).
- The box is 60×60 SVG units. Scale the visual size with CSS on the `.ct-box`
  selector or on a parent wrapper, not by changing the SVG `width`/`height`
  attributes (those are set in the HTML and drive layout).
