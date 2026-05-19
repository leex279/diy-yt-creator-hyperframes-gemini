# Editorial Shorts Template — Warm Paper + Source Serif

Vertical YouTube Short (1080x1920, 30fps, 24-180s) in an **editorial-light, single-accent** aesthetic. Warm cream paper, **Source Serif 4** italic for emphasis, and a **single terracotta accent system** — the same design language as our long-form editorial videos, sized down for a vertical Short.

The full design system (colors, type scale, motion, surface detail, SFX cues, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## Why use this template

Pick this template when:

- The topic is a **deep-explainer or essay** — overviews of a spec, standard, framework, or open protocol; cross-tool comparisons; "what is X and why does it matter".
- You want the **mood of a long-form publication** in a Short — measured, italic accent, single terracotta highlight, no rainbow.
- You want a **serif-led typographic system** (Source Serif 4 headlines + italic accent + Inter sans utility + JetBrains Mono technical voice).
- You're building a **companion / teaser** for a long-form video on the same topic — visual language stays consistent.

Pick a different template when:

- The topic needs **palette variety / 5-accent rotation** → use [`templates/shorts/standard/`](../standard/) (terracotta + indigo + sage + gold + rose with Playfair).
- The topic is an **Anthropic / Claude product launch** → use [`templates/shorts/anthropic/`](../anthropic/) (Claude-orange dark stage).
- The topic is an **Archon workflow showcase** → use [`templates/shorts/archon/`](../archon/) (cyan-magenta gradient).

## What's different from `standard`?

| Dimension | `editorial` (this template) | `standard` |
|---|---|---|
| Palette | **single terracotta** (`#C75A3F`) led, with deep-red `#B14938` + sage `#586F4F` as supporting | 5-accent rotation (terracotta + indigo + sage + gold + rose) |
| Serif | **Source Serif 4** (8-60 optical sizing, italic-first) | Playfair Display (display-only) |
| Top chrome | slim mono wordmark + thin rule (chapter heading feel) | rounded card pill with terracotta dot indicator |
| Background | cream `#F4F1EA` + 3% ghosted shapes, 2% grain | cream `#FBF7EF` + 5% shapes, 4.5% grain |
| Source URL chip | persistent bottom-right pointer for an article/full-video URL | not present by default |
| Body text | italic accent on key words is the default emphasis | bold + accent color is the default emphasis |

## What this template ships

A **210-second** demo composition (`index.html`) that orchestrates **15 sub-composition scene archetypes** — operators drop / reorder / retime per video:

| # | Scene | File | Pattern | Use for |
|---|---|---|---|---|
| 1 | Title | `compositions/scene-title.html` | mono kicker → big serif headline → italic byline | editorial intro / chapter card |
| 2 | Stat | `compositions/scene-stat.html` | mono label → huge counter + serif italic suffix | one-number reveal |
| 3 | Chart | `compositions/scene-chart.html` | header → animated bar chart with staggered reveal | data viz |
| 4 | Counter grid | `compositions/scene-counter-grid.html` | header → 3 stacked counter rows | dashboard feel |
| 5 | Typewriter | `compositions/scene-typewriter.html` | overline → serif line typed on with italic accent + chart visual | terminal/punchline reveal |
| 6 | Code block | `compositions/scene-code-block.html` | macOS-style code window with syntax-highlighted lines | technical artifact |
| 7 | Quote | `compositions/scene-quote.html` | huge serif glyph → italic body with one accented word → mono attribution | pull-quote callout |
| 8 | Bullets | `compositions/scene-bullets.html` | header → 3 raised cards with circular icon + bold title + italic sub | "three things worth knowing" |
| 9 | Process flow | `compositions/scene-process-flow.html` | 4-node connected diagram | system architecture |
| 10 | Compare | `compositions/scene-compare.html` | before card (line-through) → italic "vs." → after card (terracotta border) | before/after |
| 11 | Timeline | `compositions/scene-timeline.html` | horizontal milestones | dated events |
| 12 | Marker | `compositions/scene-marker.html` | big serif headline with one word highlighted by a left-to-right marker sweep | emphasis on one key claim |
| 13 | Image card | `compositions/scene-image-card.html` | framed visual asset with caption | screenshot / hero image |
| 14 | Badges | `compositions/scene-badges.html` | 2x3 grid of pill chips | feature cluster / tag set |
| 15 | CTA | `compositions/scene-cta.html` | mono kicker → italic lede → terracotta URL pill → indigo subscribe pill | closing call-to-action |

Each scene is a self-contained `<template>` with its own paused timeline registered on `window.__timelines["scene-<name>"]`. The root composition only handles ambient + chrome + scene-wrapper crossfades.

The bare template uses a centered mono wordmark (`YOUR TOPIC`) with a thin terracotta rule — operators replace this text or swap in a real logo per video (see "Adding a logo" below).

A persistent bottom-right `#source-url` chip points at an external URL (article, full video, GitHub repo). Operators update the label / text per video, or remove the block if no external pointer applies.

## Add Dynamous promotion? (opt-in, ask each new video)

Before you wire content, decide:

> **"Add Dynamous promotion to this Short? (y/N — default no)"**

- **No** (default) — skip this section. Proceed to "Spawn a new video" below.
- **Yes** — open [`videos/_template-wiring-snippet.md`](../../../videos/_template-wiring-snippet.md) and follow Step 0 onward.

Existing videos are NOT retroactively touched. Record the choice in `videos/<slug>/meta.json` as `"dynamousPromotion": true|false` for later audit.

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="my-new-short"

# 2. Copy the template
cp -r templates/shorts/editorial videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-new-short",
#      "name": "My New Short",
#      "dynamousPromotion": false
#    }

# 4. Edit videos/$SLUG/index.html
#    - Replace #top-banner-wordmark text (or swap for an img tag)
#    - Replace #source-url label + text (or remove the block)
#    - Adjust scene order / drop scenes / change data-start values per script
#    - Update TOTAL_DURATION + the addLabel() calls if you change scene timing

# 5. Edit videos/$SLUG/compositions/scene-*.html for per-scene content
#    - Replace placeholder text in each scene's content block
#    - Each scene's timeline is in its own <script> tag at the bottom of the file

# 6. Sync the default SFX cues (impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop)
bash scripts/sync-video-sfx.sh videos/$SLUG

# 7. Validate
npx hyperframes lint     videos/$SLUG     # 0 errors required
npx hyperframes validate videos/$SLUG     # WCAG contrast audit
npx hyperframes inspect  videos/$SLUG     # 0 layout overflow required

# 8. Preview
npx hyperframes preview videos/$SLUG

# 9. Render — output goes to repo-root out/, filename matches the slug
npx hyperframes render videos/$SLUG -o out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/editorial videos/$SLUG`.

## Tokens — the swap point

All styling flows from CSS variables in [`tokens/editorial-short.css`](./tokens/editorial-short.css). To re-skin the template per video, override the accent vars inside `#root` (or `:root` for a quick swap):

```css
#root {
  --accent-1: #2D6A4F;     /* swap terracotta → forest green for a sustainability video */
  --accent-2: #1B4332;     /* darker green for the secondary accent */
  --accent-3: #74C69D;     /* keep a calm tertiary */
}
```

The aliases `--primary`, `--secondary`, `--tertiary`, `--highlight`, `--pivot` re-bind automatically when you change `--accent-N`, so any lib entry that uses alias names stays consistent.

For a darker overall feel: change `--bg` to a deeper warm tone like `#1A1815` and `--text` to `#F4F1EA`. Verify WCAG contrast with `npx hyperframes validate`.

## Reordering / dropping / adding scenes

Each scene wrapper in `index.html` has a `data-start` (root timeline position) and points at a sub-composition file. To reorder:

1. Move the `<div class="scene-wrapper">` blocks in `index.html` into the order you want.
2. Update the `data-start` value on each wrapper.
3. Update the `tl.addLabel(...)` calls, the `repositionShapesPerScene(...)` start-time array, and the `crossfadeScenes(...)` chain in the `<script>` tag.
4. Update `TOTAL_DURATION` and `data-duration` on `#root` if your total length changes.

To drop a scene: delete its `<div class="scene-wrapper">`, its `addLabel()`, its time from the reposition array, and its two `crossfadeScenes()` lines (the one fading INTO it and the one fading OUT of it — replace with a single direct crossfade between its neighbors).

To add a new scene archetype: copy any existing `compositions/scene-*.html`, rename the `data-composition-id` and the `window.__timelines["scene-<name>"]` key, edit the content + timeline, then wire a new wrapper in the root.

## Adding a logo

The repo ships a shared logo library at `shared/logos/`. The bare template uses a centered mono wordmark text (so it lints / renders cleanly without committing to a brand). When spawning a video for a specific brand, swap the wordmark for a real logo `<img>`:

1. Find the logo: `ls shared/logos | grep -i <brand>`
2. **Copy** it into the project's `assets/` (do NOT reference `shared/logos/` directly — the studio's preview server only serves files inside the project directory):

   ```bash
   cp shared/logos/anthropic-logo-dark.svg videos/$SLUG/assets/
   ```

3. Replace the `<div id="top-banner">…</div>` block in `index.html`'s `<body>` with an `<img>`:

   ```html
   <div id="top-banner">
     <img src="assets/anthropic-logo-dark.svg" alt="Anthropic"
          style="width: 360px; height: auto; display: block; margin: 0 auto;
                 filter: drop-shadow(0 2px 8px rgba(28, 26, 24, 0.15));" />
   </div>
   ```

The warm cream canvas is light, so use **dark variants** of brand logos (`*-dark.svg` or default `*-logo.svg` if there's only one) — light logos will be near-invisible.

## Adding narration

1. Generate or drop your TTS audio at `audio/narration.wav` (or `.mp3`).
2. Add the `<audio id="narration">` block at the bottom of `index.html`, just before the closing `</div>` of `#root`:

   ```html
   <audio id="narration"
          class="clip"
          src="audio/narration.wav"
          data-start="0"
          data-duration="<your_audio_duration>"
          data-track-index="2"
          data-volume="1"></audio>
   ```

3. Tune the per-scene `data-start` values to align scene transitions with spoken-word landmarks. Use `npx hyperframes transcribe` to get word-level timestamps, then sync.

## Adding SFX

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Volume is capped per [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md) — never exceed `0.25` on a single per-cue SFX.

```html
<audio id="sfx-whoosh-1"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="13.5"
       data-duration="1.5"
       data-track-index="3"
       data-volume="0.11"></audio>
```

Place under the `<audio id="narration">` block. Use distinct `data-track-index` values for simultaneous cues.

To copy SFX files into your video's `assets/sfx/`, run:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

(With no args, picks up cues from `videos/<slug>/sfx-cues.txt`, which the template ships with `impact-slam scale-slam cinematic-whoosh spring-pop pop`.)

## Lib provenance

This template's CSS originates in [`shared/lib/tokens/editorial-short.css`](../../../shared/lib/tokens/editorial-short.css). The named-style fragment is at [`shared/lib/visual-styles/editorial-short.md`](../../../shared/lib/visual-styles/editorial-short.md). New shorts variants should fork this template and swap the palette / scene mix.

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No dark canvas — this is warm-paper only. Use anthropic/archon for dark stage.
- No more than one lead accent — the whole point of editorial is restraint. Use the supporting `--accent-2` for one moment per scene, not throughout.
- No serif fonts beyond Source Serif 4 (`var(--serif)`).
- No `<br>` in content text — use `max-width` for natural wrapping.
- No background music on Shorts — narration + SFX only.
- No `position: absolute; top: Npx` on scene content containers — use padding.
- No real logos in the bare template — operators copy per video.
- No `Math.random()` / `Date.now()` / network fetches at render time.
