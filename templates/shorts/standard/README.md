# Standard Shorts Template — Warm Paper

Vertical YouTube Short (1080x1920, 30fps, 24-180s) in a **brand-neutral, warm-paper editorial** aesthetic. The **canonical baseline for Shorts** in this repo — fork it for any topic that benefits from a warm, premium-publication feel rather than a dark stage.

The full design system (colors, type scale, motion, surface detail, SFX cues, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## Why use this template

Pick this template when:

- The topic is **not anchored to a specific brand aesthetic** (general explainers, how-to walkthroughs, news, opinion, comparisons, tips).
- You want a **warm, editorial, "premium publication" feel** instead of a dark stage.
- You want **scene variety** — nine sub-composition archetypes you can mix, reorder, or drop per video.
- You want a **serif-led typographic system** (Playfair Display headlines + Inter sans utility + JetBrains Mono technical voice).

Pick a different template when:

- The topic is an **Anthropic / Claude product launch or postmortem** → use [`templates/shorts/anthropic/`](../anthropic/) (Claude-orange dark stage, dated timeline cards).
- The topic is an **Archon workflow showcase** → use [`templates/shorts/archon/`](../archon/) (cyan-magenta gradient).

## What this template ships

A self-contained **68-second** demo composition (`index.html`) that orchestrates **nine sub-composition scene archetypes**:

| # | Scene | File | Pattern | Use for |
|---|---|---|---|---|
| 1 | Title | `compositions/scene-title.html` | mono kicker → big serif headline (per-word stagger) → ink rule → italic byline | editorial intro / chapter card |
| 2 | Stat | `compositions/scene-stat.html` | mono label → white card with one huge counter + serif italic suffix → italic caption | one-number reveal |
| 3 | Counter grid | `compositions/scene-counter-grid.html` | header → 3 stacked rows, each with its own counter + label, three accents in parallel | dashboard feel: many metrics at once |
| 4 | Quote | `compositions/scene-quote.html` | huge serif glyph → italic body with one accented word → ink rule → mono attribution | pull-quote callout |
| 5 | Bullets | `compositions/scene-bullets.html` | header → 3 raised cards, each with a circular icon badge (rotating accent) + bold title + italic sub | "three things worth knowing" |
| 6 | Compare | `compositions/scene-compare.html` | header → before card (line-through) → italic "vs." → after card (terracotta border) | before/after, old way vs new way |
| 7 | Marker | `compositions/scene-marker.html` | mono pretitle → big serif headline with one word highlighted by a left-to-right marker sweep → italic subline | emphasis on a single key claim |
| 8 | Badges | `compositions/scene-badges.html` | header → 2x3 grid of pill chips, each on a different accent (showcases the full palette) | feature cluster, tag set |
| 9 | CTA | `compositions/scene-cta.html` | mono kicker → italic lede → terracotta URL pill → indigo subscribe pill | closing call-to-action |

Each scene is a self-contained `<template>` with its own paused timeline registered on `window.__timelines["scene-<name>"]`. The root composition only handles ambient + chrome + scene-wrapper crossfades.

The bare template uses a styled wordmark pill (`Your Topic` with a terracotta dot) in the top banner — operators replace this with a real logo per video (see "Adding a logo" below).

## Add Dynamous promotion? (opt-in, ask each new video)

Before you wire content, decide:

> **"Add Dynamous promotion to this Short? (y/N — default no)"**

- **No** (default) — skip this section. Proceed to "Spawn a new video" below.
- **Yes** — open [`videos/_template-wiring-snippet.md`](../../../videos/_template-wiring-snippet.md) and follow Step 0 onward. Wires the persistent badge (artifact 1) + endcard (artifact 2). Optionally also the module interstitial (artifact 3) when the topic matches a curriculum module, and the discount bubble (artifact 4) when the platform is visibly on screen.

Existing videos are NOT retroactively touched. Record the choice in `videos/<slug>/meta.json` as `"dynamousPromotion": true|false` for later audit.

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
#      "name": "My New Short",
#      "dynamousPromotion": false
#    }

# 4. Edit videos/$SLUG/index.html
#    - Replace #top-banner-text content (or swap the div for an img tag pointing at your logo)
#    - Adjust scene order / drop scenes / change data-start values per your script
#    - Update TOTAL_DURATION + the addLabel() calls if you change scene timing

# 5. Edit videos/$SLUG/compositions/scene-*.html for the per-scene content
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

# 9. Render — output filename MUST match the slug
npx hyperframes render videos/$SLUG -o videos/$SLUG/out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/standard videos/$SLUG`.

## Tokens — the swap point

Most styling is driven by CSS variables in [`tokens/standard-short.css`](./tokens/standard-short.css). To re-skin the template per video, override the accent vars inside `#root`:

```css
#root {
  --accent-warm: #C9A96E;   /* swap terracotta → muted gold for a finance video */
  --accent-deep: #2D3142;   /* darker indigo */
  --accent-sage: #87BBA2;   /* keep sage close */
  --accent-gold: #D9A05B;   /* warmer gold */
  --accent-rose: #E5989B;   /* keep rose close */
}
```

The aliases `--primary`, `--secondary`, `--tertiary`, `--highlight`, `--pivot` re-bind automatically when you change `--accent-*`, so any lib entry that uses the alias names stays consistent.

For a darker overall feel: change `--bg` to a deeper warm tone like `#2B2A28` and `--text` to `#FBF7EF`. The accent system still works, but verify WCAG contrast with `npx hyperframes validate`.

## Reordering / dropping / adding scenes

Each scene wrapper in `index.html` has a `data-start` (root timeline position) and points at a sub-composition file. To reorder:

1. Move the `<div class="scene-wrapper">` blocks in `index.html` into the order you want.
2. Update the `data-start` value on each wrapper.
3. Update the `tl.addLabel(...)` calls and the `crossfadeScenes(...)` chain in the `<script>` tag at the bottom.
4. Update `TOTAL_DURATION` and the `data-duration` on `#root` if your total length changes.

To drop a scene: delete its `<div class="scene-wrapper">`, its `addLabel()`, and its two `crossfadeScenes()` lines (the one fading INTO it and the one fading OUT of it — replace with a single direct crossfade between its neighbors).

To add a new scene archetype: copy any existing `compositions/scene-*.html`, rename the `data-composition-id` and the `window.__timelines["scene-<name>"]` key, edit the content + timeline, then wire a new wrapper in the root.

## Adding a logo

The repo ships a shared logo library at `shared/logos/` (84 brand wordmarks and icons). The bare template uses a styled text wordmark pill (so it lints / renders cleanly without committing to a brand). When spawning a video for a specific brand, swap the wordmark pill for a real logo `<img>`:

1. Find the logo: `ls shared/logos | grep -i <brand>`
2. **Copy** it into the project's `assets/` (do NOT reference `shared/logos/` directly — the studio's preview server only serves files inside the project directory):

   ```bash
   cp shared/logos/anthropic-logo-light.svg videos/$SLUG/assets/
   ```

3. Replace the `<div id="top-banner-text">…</div>` block in `index.html` with an `<img>`:

   ```html
   <img id="top-banner-logo" src="assets/anthropic-logo-light.svg" alt="Anthropic"
        style="width: 880px; height: auto; display: block; margin: 0 auto;
               filter: drop-shadow(0 4px 12px rgba(43, 42, 40, 0.25));" />
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

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Volume is capped per [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md) — never exceed `0.25` on a single per-cue SFX (sonic-logo at `0.45` is the only exception).

```html
<audio id="sfx-whoosh-1"
       class="clip"
       src="assets/sfx/cinematic-whoosh.mp3"
       data-start="11.82"
       data-duration="0.8"
       data-track-index="3"
       data-volume="0.11"></audio>
```

Place under the `<audio id="narration">` block. Use distinct `data-track-index` values for simultaneous cues.

To copy SFX files into your video's `assets/sfx/`, run:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

(With no extra args, this picks up cues from `videos/<slug>/sfx-cues.txt`, which the template ships with `impact-slam scale-slam cinematic-whoosh spring-pop pop`.)

## Lib provenance

This template's CSS originates in [`shared/lib/tokens/standard-short.css`](../../../shared/lib/tokens/standard-short.css). The named-style fragment is at [`shared/lib/visual-styles/standard-short.md`](../../../shared/lib/visual-styles/standard-short.md). New shorts variants should fork this template and swap the palette / scene mix.

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No dark canvas — this is warm-paper only. Use anthropic/archon for dark stage.
- No more than two accents per scene.
- No serif fonts beyond Playfair Display (`var(--serif)`).
- No `<br>` in content text — use `max-width` for natural wrapping.
- No background music on Shorts — narration + SFX only.
- No `position: absolute; top: Npx` on scene content containers — use padding.
- No real logos in the bare template — operators copy per video.
- No `Math.random()` / `Date.now()` / network fetches at render time.
