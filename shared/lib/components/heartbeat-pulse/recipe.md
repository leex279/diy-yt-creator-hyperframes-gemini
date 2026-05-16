# heartbeat-pulse — Recipe

Element pulses on a heartbeat lub-dub rhythm. One cycle = 1.2s:
- Lub at cycle+0.0s (stronger, scale 1.06 + red glow)
- Dub at cycle+0.4s (weaker, scale 1.04)
- Rest 0.6s

Cycles are FINITE: `Math.floor(totalDuration / 1.2)`.

## SFX Coupling

Per cycle, two `pop` cues fire on separate tracks:

| Beat | Cue   | Offset from cycle start | data-volume | track-index |
|------|-------|------------------------|-------------|-------------|
| Lub  | `pop` | `+0.0`                 | `0.10`      | `3`         |
| Dub  | `pop` | `+0.4`                 | `0.06`      | `4`         |

For **4 cycles** (`totalDuration=4.8s`) → **8 `<audio>` elements total**.

**Exact `<audio>` snippet (4 cycles; replace `<AT>` with `at` value):**

```html
<!-- Lub beats: track 3 -->
<audio id="sfx-hb-lub-0" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 0.0>" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-hb-lub-1" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 1.2>" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-hb-lub-2" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 2.4>" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<audio id="sfx-hb-lub-3" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 3.6>" data-duration="0.52" data-track-index="3" data-volume="0.10"></audio>
<!-- Dub beats: track 4 (quieter: 0.06) -->
<audio id="sfx-hb-dub-0" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 0.4>" data-duration="0.52" data-track-index="4" data-volume="0.06"></audio>
<audio id="sfx-hb-dub-1" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 1.6>" data-duration="0.52" data-track-index="4" data-volume="0.06"></audio>
<audio id="sfx-hb-dub-2" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 2.8>" data-duration="0.52" data-track-index="4" data-volume="0.06"></audio>
<audio id="sfx-hb-dub-3" class="clip" src="assets/sfx/pop.mp3"
       data-start="<AT + 3.2>" data-duration="0.52" data-track-index="4" data-volume="0.06"></audio>
```

**Alignment check:** lub SFX at `at + i*1.2`, dub SFX at `at + i*1.2 + 0.4`.
Drift ≤ 0.05s required (percussive beats).

**Scaling for different `totalDuration`:**
- 6.0s → 5 cycles → 10 `<audio>` elements
- 2.4s → 2 cycles → 4 `<audio>` elements

## HTML slot

```html
<div class="heartbeat-pulse" data-hb id="hb-stat">
  <!-- stat number, icon, badge — anything with visual weight -->
</div>
```

## CSS

Merge the `<style>` block from `component.html` into your host `<style>`.

Override the glow color:

```css
:root { --heart-color: #FF6B35; } /* orange glow */
```

Or pass `color` in opts:

```js
addHeartbeatPulse(tl, "#hb-stat", at, { color: '#FF6B35' });
```

## JS

Paste the `addHeartbeatPulse` function from `component.html` into your host `<script>`.

```js
// Default: 4.8s = 4 cycles, red glow
addHeartbeatPulse(tl, "#hb-stat", P2 + 1.5);

// Longer duration — 5 cycles
addHeartbeatPulse(tl, "#hb-stat", P2 + 1.5, { totalDuration: 6.0 });
```

## Opts reference

| Option          | Default                    | Description                                  |
|-----------------|---------------------------|----------------------------------------------|
| `totalDuration` | `4.8`                     | Total heartbeat duration (rounds to full cycles) |
| `color`         | `var(--heart, #FF4070)`   | Glow color (box-shadow)                      |

## Constraints

- Glow uses `box-shadow`. Parent must allow overflow or the glow is clipped.
- Wire `pop` in `sfx-cues.txt` and run `scripts/sync-video-sfx.sh` before preview.
- Do NOT reference `shared/lib/...` at runtime. Copy `component.html` content inline.
- IDs on the `<audio>` elements must be unique per phase/instance.
