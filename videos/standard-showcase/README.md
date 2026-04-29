# Standard Shorts Template

Vertical YouTube Short (1080x1920, 30fps, 24-180s) in a **brand-neutral, topic-agnostic** dark-navy aesthetic. The **canonical baseline for Shorts** in this repo — fork it for any topic that doesn't have a dedicated brand variant.

The full design system (colors, type scale, motion, surface detail, SFX cues, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## Why use this template

Pick this template when:

- The topic is **not anchored to a specific brand aesthetic** (general explainers, how-to walkthroughs, news, opinion, comparisons, tips).
- You want a **clean, neutral palette** that works for any content category.
- You want **numbered step cards** (01/02/03) instead of dated timeline cards — better for "three things to know", how-tos, feature breakdowns.

Pick a different template when:

- The topic is an **Anthropic / Claude product launch or postmortem** → use [`templates/shorts/anthropic/`](../anthropic/) (Claude-orange + warm off-white, dated timeline cards).
- The topic is an **Archon workflow showcase** → use [`templates/shorts/archon/`](../archon/) (cyan-magenta gradient).

## What this template ships

A self-contained 24-second demo composition (`index.html`) showcasing the four reusable phase archetypes:

| Phase | Pattern | Use for |
|---|---|---|
| 1 — Hero hook | overline + secondary line + 200px slam word + caption pill | scroll-stop hook for any topic |
| 2 — Stat pill row | overline + headline + 2 huge color-rotated stat pills | receipts, before/after, comparison numbers |
| 3 — Step cards | overline + 3 numbered cards (01/02/03), accent rotation | how-to steps, feature breakdowns, "three things to know" |
| 4 — CTA URL slam | overline + URL pill + subscribe pill | closing call-to-action |

Each phase is mutex-visible (only one at a time), separated by a blur + crossfade transition. Entrance animations only — the transition handles the exit (per HyperFrames rule).

The bare template uses a styled wordmark pill (`Your Topic` with an accent-blue dot) in the top banner — operators replace this with a real logo per video (see "Adding a logo" below).

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
cp -r templates/shorts/standard videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-new-short",
#      "name": "My New Short"
#    }

# 4. Edit videos/$SLUG/index.html
#    - Replace #top-banner-text content (or swap the div for an img tag pointing at your logo)
#    - Replace each phase's text content
#    - Adjust data-duration on #root and the phase transition timestamps if your script length differs from 24s
#    - Drop your narration at videos/$SLUG/audio/narration.wav and uncomment the audio block

# 5. Sync the default SFX cues (impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop)
bash scripts/sync-video-sfx.sh videos/$SLUG

# 6. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG     # adds WCAG contrast audit
npx hyperframes inspect videos/$SLUG      # checks for layout overflow

# 7. Preview
npx hyperframes preview videos/$SLUG

# 8. Render — output filename MUST match the slug
npx hyperframes render videos/$SLUG -o videos/$SLUG/out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/standard videos/$SLUG`.

## Tokens — the swap point

Most styling is driven by CSS variables in [`tokens/standard-short.css`](./tokens/standard-short.css). To re-skin a phase or a card per video, override `--accent-1..4` inside `#root`:

```css
#root {
  --accent-1: #FF6B35;   /* swap blue → warm-orange for a fitness video */
  --accent-2: #FFD23F;   /* swap cyan → yellow */
  --accent-3: #06A77D;   /* swap purple → forest green */
  --accent-4: #D62828;   /* swap green → strong red for "go" */
}
```

The aliases `--primary`, `--secondary`, `--tertiary`, `--success` in `tokens/standard-short.css` re-bind automatically when you change `--accent-1..4`, so any lib entry that uses the alias names stays consistent.

Per-phase accent rotation: change a stat-pill's class from `.accent-1` to `.accent-3` or a step card from `.accent-2` to `.accent-4`. The card-color CSS rules cover all four accents already.

## Adding a logo

The repo ships a shared logo library at `shared/logos/` (84 brand wordmarks and icons — see `shared/README.md`). The bare template uses a styled text wordmark pill (so it lints / renders cleanly without committing to a brand). When spawning a video for a specific brand, swap the wordmark pill for a real logo `<img>`:

1. Find the logo: `ls shared/logos | grep -i <brand>`
2. **Copy** it into the project's `assets/` (do NOT reference `shared/logos/` directly — the studio's preview server only serves files inside the project directory):

   ```bash
   cp shared/logos/anthropic-logo-light.svg videos/$SLUG/assets/
   ```

3. Replace the `<div id="top-banner-text">…</div>` block in `index.html` with an `<img>`:

   ```html
   <img id="top-banner-logo" src="assets/anthropic-logo-light.svg" alt="Anthropic"
        style="width: 972px; height: auto; display: block; margin: 0 auto;" />
   ```

Use `*-light.svg` or `*-light.png` variants on this dark-stage template — `*-dark` variants will be near-invisible. **Never** keep the placeholder text wordmark when a real logo exists.

## Adding more phases

1. Duplicate one of the four `<div class="phase">` blocks. Give it a new id (`#phase5`), add `z-index: 5; opacity: 0;`.
2. Add per-phase CSS rules (`#phase5 .phase-content { … }`) — keep `padding: var(--pad-top) var(--pad-x) var(--pad-bottom)` so it sits below the top banner.
3. Bump `#root` `data-duration` to cover the new total.
4. Add the entrance tweens and a transition block following the existing pattern (`P1`, `T1`, `P2`, `T2` … convention).
5. Re-run `npx hyperframes lint` after every change.

## Adding narration

1. Generate or drop your TTS audio at `audio/narration.wav` (or `.mp3`).
2. Add the `<audio id="narration">` block at the bottom of `index.html`, just before the closing `</div>` of `#root`:

   ```html
   <audio id="narration"
          class="clip"
          src="audio/narration.wav"
          data-start="0"
          data-duration="<phase4_end>"
          data-track-index="2"
          data-volume="1"></audio>
   ```

3. Tune `data-start` (when narration begins relative to composition 0) and `data-duration` (clip length).
4. Sync phase timestamps to spoken-word landmarks. Use `npx hyperframes transcribe` to get word-level timestamps.

## Adding SFX

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Volume is capped per [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md) — never exceed `0.25` on a single per-cue SFX (sonic-logo at `0.45` is the only exception).

```html
<audio id="sfx-slam"
       class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="1.55"
       data-duration="0.6"
       data-track-index="3"
       data-volume="0.15"></audio>
```

Place under the `<audio id="narration">` block. Use distinct `data-track-index` values so simultaneous cues don't clash.

### Sourcing the SFX files

The cues above are names — the audio files live in [`shared/audio/sfx/`](../../../shared/audio/). To copy them into your video's `assets/sfx/` (required because HyperFrames rejects paths outside the project dir at runtime), run:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

(With no extra args, this picks up cues from `videos/<slug>/sfx-cues.txt`, which the template ships with `impact-slam scale-slam cinematic-whoosh spring-pop pop`.) Or pass cue names explicitly:

```bash
bash scripts/sync-video-sfx.sh videos/<slug> impact-slam scale-slam glitch-zap
```

Volume caps and the full per-cue table are in [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md); the cue catalog with default volumes lives in [`shared/audio/MANIFEST.md`](../../../shared/audio/MANIFEST.md).

## Lib provenance

This template's CSS and JS originate in [`shared/lib/`](../../../shared/lib/). The provenance comments in `index.html` (e.g. `/* BLOCK: shared/lib/blocks/stat-pill-row/ */`, `// EFFECT: shared/lib/effects/phase-crossfade.js`) point at the canonical source for each piece. New templates should be authored by picking entries from [`shared/lib/MANIFEST.md`](../../../shared/lib/MANIFEST.md) — not by copying this file. The named-style fragment for this aesthetic is at [`shared/lib/visual-styles/standard-short.md`](../../../shared/lib/visual-styles/standard-short.md).

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No light canvas — this is dark-stage only.
- No more than one accent per phase.
- No serif headlines — Inter only.
- No `<br>` in content text — use `max-width` for natural wrapping.
- No background music on Shorts — narration + SFX only.
- No `position: absolute; top: Npx` on `.phase-content` — use padding.
- No real logos in the bare template — operators copy per video.
- No dated chips — use the `anthropic` template if you need dated timeline cards.
