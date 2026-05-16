# Generic News Template — Cinematic Tech-News Shorts

Brand-neutral cinematic shorts template for tech-news drops, product launches, and "what just shipped" recaps. **1080×1920 vertical · ~79s default (15 phases) · designed to stretch to 2-3 min by extending phase durations.**

Forked from the [`OpenAI News`] design canvas (`spectrum-drift` direction). Two pre-built accent variants:

- **Default (`index.html`)** — Spectrum Drift: cyan / purple / blue / amber rotation.
- **Alt (`_alt/frontier-green.html`)** — Frontier Green: ChatGPT-mint mono-accent.

Swap by either editing `--orange / --purple / --blue / --green` on `#root` inside `index.html`, or copying `_alt/frontier-green.html` over `index.html`.

## What this template ships

- **15 phase archetypes** (cinematic stage chrome runs through all of them):
  - **P1 — Hook** (brand lockup → topic slam → hero word with RGB glitch + impact ring)
  - **P2 — Terminal** (mac-style window with staggered CLI output lines + cursor blink)
  - **P3 — Benchmark chart** (4-row horizontal bar chart with count-up percentages + leader marker)
  - **P4 — Code diff** (before/after stacked panels with line wipes)
  - **P5 — Timeline** (vertical event rail with date pings + playhead)
  - **P6-P14 — Free-form content slots** (replace per video)
  - **P15 — Quote + CTA** (avatar + handle + ticking engagement stats + URL bar with caret)
- **Cinematic chrome** that persists across all phases:
  - Letterbox top/bottom
  - Viewfinder corners
  - `REC ●` indicator with pulsing dot
  - Live timecode (`MM:SS:FF`)
  - Phase label (`01 / 15`) + 15 tick dots (right side)
  - Top banner wordmark
  - Progress fill bar
- **Atmospheric layers** (all behind content):
  - Ambient radial gradient (drifts via Ken Burns)
  - Gradient mesh orbs (4 drifting color blobs)
  - Particle constellation (30 deterministic dots + nearest-neighbor connecting lines)
  - Token-stream edges (faint vertical mono character columns left/right)
  - Grain + scanlines (subtle film texture)
  - Vignette
- **Effect bursts** triggered at phase transitions:
  - Light leak (warm streak diagonal sweep)
  - Anamorphic flare (blue-white horizontal whip)
  - Phase crossfade (blur + scale dissolve, 0.5s)

## Quick spawn (manual)

```bash
# Copy template to a new video slug
cp -r templates/shorts/generic-news-template videos/my-news-short
# (PowerShell: Copy-Item -Recurse templates/shorts/generic-news-template videos/my-news-short)

# Update meta.json
# {"id": "my-news-short", "name": "My News Short"}

# Replace the placeholder content in videos/my-news-short/index.html:
#   - #p1-topic-slam        → your headline (max ~2 words per line, 2 lines)
#   - #p1-hero              → your hero one-word reveal (e.g. "ZERO.", "LAUNCHED.")
#   - #p1-ga-receipt        → date / format / runtime line
#   - #p2-l1 ... #p2-l7     → your terminal CLI lines
#   - #p3-row-1..4 .pct     → your benchmark percentages (data-pct on .bench-fill)
#   - #p4 diff panels       → before/after code lines (file name in #p4-filename)
#   - #p15 quote + URL      → your CTA URL + spoken-debate question

# Drop narration audio + sync SFX
cp my-narration.wav videos/my-news-short/audio/narration.wav
scripts/sync-video-sfx.sh videos/my-news-short

# Lint, preview, render
npx hyperframes lint    videos/my-news-short
npx hyperframes preview videos/my-news-short
npx hyperframes render  videos/my-news-short -o out/my-news-short.mp4
```

## Spawn via diy-yt-creator (recommended)

See [`.claude/skills/diy-yt-creator/new-generic-news-short.md`](../../../.claude/skills/diy-yt-creator/new-generic-news-short.md) for the topic-prompt-to-rendered-MP4 workflow.

```
/diy-yt-creator new-generic-news-short topic="vercel-labs/zero — programming language for agents"
```

## Brand-overlay slots

The template ships brand-neutral. To rebrand per video:

- **Top wordmark** — edit `#top-banner-wordmark` (text + sub) and `#p1-brand-wordmark`. To use a brand SVG logo, drop the SVG in `assets/<brand>-logo.svg` and replace the wordmark `<span>` block with an `<img>`.
- **Accent rotation** — edit the four `--orange / --purple / --blue / --green` variables on `#root`.
- **Phase ticks color** — `#phase-label .num` and `.phase-tick.active` use `var(--orange)`. Stays auto-correct when you re-tint.
- **CTA URL** — `#p15-url-text` is empty by default and gets typed in via the timeline. Edit the JS line that builds the typed string.

## Duration

The template runs **~79 seconds at the default phase boundaries** (T1=5.6s ... T14=71.6s, P15 runs to ~79s).

For longer videos (2-3 min target), extend phase windows by editing the `T1..T14` and `P2..P15` anchors near the bottom of the `<script>` block. The phase content (terminal stagger, bar fills, code-diff line wipes, quote tick-up) all use relative offsets from the phase start anchor, so widening the phase window automatically lengthens the breathing room.

For shorter videos (30-60s), drop unused phases by hiding their `<div id="phaseN" class="phase">` block and removing the matching `T(N-1)` / `P(N)` anchors.

## Don'ts

- **Do NOT** put `font-family: var(--sans)` or `var(--mono)` anywhere in the file — the render compiler can't resolve CSS variable indirection. Use the literal `'Inter', system-ui, sans-serif` / `'JetBrains Mono', ui-monospace, monospace` as the source ships. See [`.claude/rules/hyperframes-pitfalls.md §8`](../../../.claude/rules/hyperframes-pitfalls.md).
- **Do NOT** reference assets via `../../shared/logos/` paths. HyperFrames' bundler rejects paths outside the video directory. Copy brand logos into `videos/<slug>/assets/` first.
- **Do NOT** add background music. Shorts are narration + SFX only.

## Assets

- `assets/shapes/shape1.svg`, `shape2.svg`, `shape3.svg` — drifting backdrop shapes (referenced via `spawnShapes()` in the script — currently unused, atmosphere is gradient-mesh only by default).
- `assets/sfx/.gitkeep` — populated by `scripts/sync-video-sfx.sh` based on `sfx-cues.txt`.
- `audio/.gitkeep` — operator drops `narration.wav` here.

## Design system

See [`DESIGN.md`](./DESIGN.md) for the full color / type / motion spec.
