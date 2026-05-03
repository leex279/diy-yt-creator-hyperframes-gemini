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

## Add Dynamous promotion? (opt-in, ask each new video)

Before you wire content, decide:

> **"Add Dynamous promotion to this Short? (y/N — default no)"**

- **No** (default) — skip this section. Proceed to "Spawn a new video" below.
- **Yes** — open [`videos/_template-wiring-snippet.md`](../../../videos/_template-wiring-snippet.md) and follow Step 0 onward. Wires the persistent badge (artifact 1) + endcard (artifact 2). Optionally also the module interstitial (artifact 3) when the topic matches a curriculum module, and the discount bubble (artifact 4) when the platform is visibly on screen.

Existing videos are NOT retroactively touched. The decision is per video. Record the choice in `videos/<slug>/meta.json` as `"dynamousPromotion": true|false` for later audit.

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
npx hyperframes render videos/$SLUG -o out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/anthropic videos/$SLUG`.

## Lib provenance

This template's CSS and JS originate in [`shared/lib/`](../../../shared/lib/). The provenance comments in `index.html` (e.g. `/* BLOCK: shared/lib/blocks/stat-pill-row/ */`, `// EFFECT: shared/lib/effects/phase-crossfade.js`) point at the canonical source for each piece. New templates should be authored by picking entries from [`shared/lib/MANIFEST.md`](../../../shared/lib/MANIFEST.md) — not by copying this file. The named-style fragment for this aesthetic is at [`shared/lib/visual-styles/anthropic-dark.md`](../../../shared/lib/visual-styles/anthropic-dark.md).

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

## Logos — always use real ones

The repo ships a shared logo library at `shared/logos/` (84 brand wordmarks and icons — see `shared/README.md`). The template's top banner already points at `../../../shared/logos/anthropic-logo-light.svg` (Anthropic wordmark on dark canvas). When you copy this template into a video, the path becomes `../../shared/logos/anthropic-logo-light.svg` (one less `../` because the video lives one level shallower than the template).

For other brands, swap the `src`:

```html
<img id="top-banner-logo" src="../../shared/logos/claude-code-logo-light.svg" alt="Claude Code" />
```

Use `*-light.svg` or `*-light.png` variants on this dark-stage template — `*-dark` variants will be near-invisible. Run `ls shared/logos | grep -i <brand>` to find a logo. **Never** swap the img back to a styled text div when a real logo exists.

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

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Volume is capped per [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md) — never exceed `0.25` on a single per-cue SFX (sonic-logo at `0.60` is the only exception).

```html
<audio id="sfx-slam"
       class="clip"
       src="assets/sfx/scale-slam.mp3"
       data-start="1.55"
       data-duration="0.9"
       data-track-index="3"
       data-volume="0.20"></audio>
```

Place under the `<audio id="narration">` block. Use distinct `data-track-index` values so simultaneous cues don't clash.

### Sourcing the actual SFX files

The cues above are names — the audio files live in [`shared/audio/sfx/`](../../../shared/audio/). To copy them into your video's `assets/sfx/` (required because HyperFrames rejects paths outside the project dir at runtime), run:

```bash
bash scripts/sync-video-sfx.sh videos/<slug> impact-slam scale-slam spring-pop
```

Or list the cues you want in `videos/<slug>/sfx-cues.txt` (one per line) and run without arguments. Volume caps and the full per-cue table are in [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md); the cue catalog with default volumes lives in [`shared/audio/MANIFEST.md`](../../../shared/audio/MANIFEST.md).

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No light canvas — this is dark-stage only.
- No more than one accent per phase.
- No serif headlines — Inter only.
- No `<br>` in content text — use `max-width` for natural wrapping.
- No background music on Shorts — narration + SFX only.
- No `position: absolute; top: Npx` on `.phase-content` — use padding.
