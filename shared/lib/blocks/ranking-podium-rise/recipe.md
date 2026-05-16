# Recipe: ranking-podium-rise

Three podium pillars rise sequentially from off-canvas bottom. Bronze (3rd, shorter) at t=0.6, silver (2nd, medium) at t=1.8, gold (1st, tallest + crown icon + winner label) at t=3.0. Each pillar lands with a layered `screen-shake` + `impact-slam` pair. Number labels fade in 0.3s after landing. Hold from t=4.5–6.5, fade-out t=7–8s.

Canvas: 1080×1920 (Shorts). Duration: 8s.

## What it produces

```
           🏆
         WINNER
        ┌───────┐
        │       │  🥈
        │   1   │ ┌───┐  🥉
        │       │ │ 2 │ ┌───┐
        │       │ │   │ │ 3 │
        └───────┴─┴───┴─┴───┘
```

## Slot

| Selector | Purpose | Constraint |
|---|---|---|
| `[data-slot="winner-name"]` = `#rpr-winner-label` | Label on gold pillar | ≤ 12 chars; 44px; wraps at 300px |

## SFX coupling (already wired inside block.html)

The block ships with its own `<audio>` elements inside the `<template>`. When the block is copied and wired as a sub-composition, the host does NOT need to add separate SFX — they're baked in.

| Cue | ID | `data-start` | `data-track-index` | Volume | Event |
|---|---|---|---|---|---|
| `screen-shake` | `sfx-rpr-shake-3` | 1.0 | 3 | 0.11 | Bronze lands |
| `impact-slam`  | `sfx-rpr-slam-3`  | 1.0 | 4 | 0.15 | Bronze lands |
| `screen-shake` | `sfx-rpr-shake-2` | 2.2 | 3 | 0.11 | Silver lands |
| `impact-slam`  | `sfx-rpr-slam-2`  | 2.2 | 4 | 0.15 | Silver lands |
| `screen-shake` | `sfx-rpr-shake-1` | 3.4 | 5 | 0.11 | Gold lands |
| `impact-slam`  | `sfx-rpr-slam-1`  | 3.4 | 5 | 0.15 | Gold lands |

Total: **6 `<audio>` elements** inside block.html.

**Why t=1.0 / 2.2 / 3.4 for landing (not 0.6 / 1.8 / 3.0)?** The pillar rises with `back.out(1.4)` over 0.55s — the visual impact frame (when the pillar hits the baseline) lands at approximately `start + 0.4s`. The SFX fires at `start + 0.4s`. Percussive drift rule: ≤ 0.05s.

## Wire into a host composition

1. Copy `block.html` to `videos/<slug>/compositions/ranking-podium-rise.html`.
2. In `videos/<slug>/index.html`, add:

```html
<div id="rpr"
     class="clip"
     data-composition-id="ranking-podium-rise"
     data-composition-src="compositions/ranking-podium-rise.html"
     data-start="<start>"
     data-duration="8"
     data-track-index="<track>"
     data-width="1080"
     data-height="1920"></div>
```

3. The framework auto-nests the block timeline under the host root timeline.

## Editing the winner name slot

In the copied `compositions/ranking-podium-rise.html`, find:

```html
<div class="rpr-winner-label" id="rpr-winner-label"
     data-slot="winner-name">WINNER</div>
```

Replace `WINNER` with the actual winner text. Keep ≤ 12 chars for clean layout.

## CSS token overrides

The block reads:

```
--bg, --sans, --mono, --text, --rpr-gold
```

`--rpr-gold` defaults to `#FFD700`. Override per-video:

```css
#rpr { --rpr-gold: #F7C948; }
```

## Sync cues

The block's `<audio>` elements reference `assets/sfx/screen-shake.mp3` and `assets/sfx/impact-slam.mp3` inside the project. Run:

```bash
bash scripts/sync-video-sfx.sh videos/<slug> screen-shake impact-slam
```

## Gotchas

- The `<audio>` elements inside the block use `src="assets/sfx/..."` (relative to the host project, not the block file). When the block is copied as a sub-composition under `videos/<slug>/compositions/`, the SFX paths resolve correctly because the bundler rewrites relative paths relative to the project root.
- `track-index` 5 is used for the gold-pillar pair. If the host has other elements on track 5, increment to 6/7 and update both gold-pillar audio IDs.
- `data-duration="8"` on the wiring div: don't change unless you shorten the internal timeline.
- The `<template>` wrapper in `block.html` is for documentation only — the actual content used is the `<div id="ranking-podium-rise">` inside it. HyperFrames processes the inner div when the file is used as a sub-composition.
