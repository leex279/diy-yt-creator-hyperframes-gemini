# Anthropic Shorts Template

Vertical YouTube Short (1080x1920, 30fps, 60-180s) in the **Anthropic dark-stage** aesthetic. Lifted from `diy-yt-creator/src/AnthropicPostmortemShort` (Remotion) and translated to HyperFrames (HTML + GSAP).

The full design system (colors, type scale, motion, surface detail, SFX cues, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained 24-second demo composition (`index.html`) showcasing the four reusable phase archetypes:

| Phase | Pattern | Use for |
|---|---|---|
| 1 — Hero slam | overline + secondary line + 240px slam word + caption pill | scroll-stop hook |
| 2 — Stat pill row | overline + headline + 2 huge color-rotated stat pills | "X bugs / Y weeks" receipts |
| 3 — Timeline cards | overline + 3 dated cards (orange / purple / blue) | dated event sequence |
| 4 — CTA URL slam | overline + URL pill + subscribe pill | closing call-to-action |

Each phase is mutex-visible (only one at a time), separated by a blur + crossfade transition. Entrance animations only — the transition handles the exit (per HyperFrames rule).

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="my-new-short"

# 2. Copy the template
cp -r templates/shorts/anthropic videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-new-short",
#      "name": "My New Short"
#    }

# 4. Edit videos/$SLUG/index.html
#    - Replace #top-banner-text content (or swap the div for an img tag pointing at your logo)
#    - Replace each phase's text content
#    - Adjust data-duration on #root and the phase transition timestamps if your script length differs from 24s
#    - Drop your narration at videos/$SLUG/audio/narration.wav and uncomment the <audio> block

# 5. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG     # adds WCAG contrast audit
npx hyperframes inspect videos/$SLUG      # checks for layout overflow

# 6. Preview
npx hyperframes preview videos/$SLUG

# 7. Render
npx hyperframes render videos/$SLUG -o videos/$SLUG/out/short.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/anthropic videos/$SLUG`.

## Customizing per video

Most styling is driven by CSS variables on `#root`:

```css
#root {
  --orange: #E97458;   /* swap for a different brand primary */
  --purple: #A78BFA;
  --blue:   #6B9AEF;
  --green:  #7DD3A6;
  --pad-top: 240px;    /* increase if your top banner is taller */
  /* ... */
}
```

Per-phase accent rotation: change a stat-pill's class from `.orange` to `.purple` or a timeline card from `.blue` to `.green`. The card-color CSS rules cover all four accents already.

## Adding more phases

1. Duplicate one of the four `<div class="phase">` blocks. Give it a new id (`#phase5`), add `z-index: 5; opacity: 0;`.
2. Add per-phase CSS rules (`#phase5 .phase-content { ... }`) — keep `padding: var(--pad-top) var(--pad-x) var(--pad-bottom)` so it sits below the top banner.
3. Bump `#root` `data-duration` to cover the new total.
4. Add the entrance tweens and a transition block following the existing pattern (`P1`, `T1`, `P2`, `T2` … convention).
5. Re-run `npx hyperframes lint` after every change.

## Adding narration

1. Generate or drop your TTS audio at `audio/narration.wav` (or `.mp3`).
2. Uncomment the `<audio id="narration">` block at the bottom of `index.html`.
3. Tune `data-start` (when narration begins relative to composition 0) and `data-duration` (clip length).
4. Sync phase timestamps to spoken-word landmarks. Use `npx hyperframes transcribe` to get word-level timestamps.

## Adding SFX

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Volume is capped per `DESIGN.md` — never exceed `0.25` on a single SFX bed.

```html
<audio id="sfx-slam"
       src="assets/sfx/scale-slam.wav"
       data-start="1.55"
       data-duration="0.9"
       data-track-index="3"
       data-volume="0.20"></audio>
```

Place under the `<audio id="narration">` block. Use distinct `data-track-index` values so simultaneous cues don't clash.

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No light canvas — this is dark-stage only.
- No more than one accent per phase.
- No serif headlines — Inter only.
- No `<br>` in content text — use `max-width` for natural wrapping.
- No background music on Shorts — narration + SFX only.
- No `position: absolute; top: Npx` on `.phase-content` — use padding.
