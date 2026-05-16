# rubber-band-snap — Recipe

Element stretches vertically like a rubber band then snaps back with a spring
overshoot. Three stages: stretch (power2.in) → peak hold → snap (back.out(2.5)).
A motion-blur filter fires during the stretch phase.

## SFX Coupling

| Cue          | Offset from `at` | data-volume | track-index | Notes                                              |
|--------------|-----------------|-------------|-------------|----------------------------------------------------|
| `spring-pop` | `+0.5`          | `0.11`      | `3`         | Fires at snap release moment (Stage 3 start). NOT at `at`. |

**Exact `<audio>` snippet** (wire in host `index.html`; replace `<AT>` with `at` value, add 0.5):

```html
<audio id="sfx-rb-snap-1"
       class="clip"
       src="assets/sfx/spring-pop.mp3"
       data-start="<AT + 0.5>"
       data-duration="0.52"
       data-track-index="3"
       data-volume="0.11"></audio>
```

**Alignment check:** `data-start` must equal `at + 0.5` (the snap release instant).
Drift ≤ 0.05s required.

If using a custom `duration` other than 0.7, snap fires at `at + duration * 0.714`:

```
snap_at = at + opts.duration * 0.714
```

## HTML slot

```html
<div class="rubber-band-snap" data-rb id="rb-badge">
  <!-- your content: badge, pill, icon, etc. -->
</div>
```

## CSS

Merge the `<style>` block from `component.html` into your host `<style>`.

`transform-origin: center bottom` — element stretches downward from a fixed top anchor.
Override if you need center-center:

```css
#rb-badge { transform-origin: center center; }
```

## JS

Paste the `addRubberBandSnap` function from `component.html` into your host `<script>`.

```js
// Default snap on a badge
addRubberBandSnap(tl, "#rb-badge", P3 + 1.2);

// More intense snap, slightly slower
addRubberBandSnap(tl, "#rb-badge", P3 + 1.2, { duration: 0.9, intensity: 0.85 });
```

## Opts reference

| Option      | Default | Range | Description                                         |
|-------------|---------|-------|-----------------------------------------------------|
| `duration`  | `0.7`   | > 0   | Total effect duration in seconds                    |
| `intensity` | `0.6`   | 0–1   | 0 = no stretch; 1.0 = stretch to scaleY 1.6        |

## Constraints

- The element should already be **visible** when this fires. Combine with a
  `statPillPop` entrance first, then call `addRubberBandSnap` a beat later for
  layered tactile impact.
- `transform-origin: center bottom` is set in the component CSS. Verify this
  is not overridden by parent CSS that resets transform-origin.
- Wire `spring-pop` in `sfx-cues.txt` and run `scripts/sync-video-sfx.sh` before preview.
- Do NOT reference `shared/lib/...` at runtime. Copy `component.html` content inline.
