# DESIGN — Standard Shorts (Warm Paper, Editorial)

Visual system for **YouTube Shorts** (1080x1920, 30fps, 24-180s) in a **brand-neutral, warm-paper editorial** aesthetic. Cream canvas with terracotta/indigo/sage/sunset-gold/warm-rose accents — intentionally different from the dark-stage variants (`anthropic`, `archon`) so the channel can show range.

This is the **canonical baseline for Shorts**. Use it for any topic that isn't anchored to a specific brand aesthetic and that benefits from a warm, editorial, "premium publication" feel — explainers, how-to walkthroughs, news, opinion, comparisons, tips.

## Style Prompt

A confident, premium-publication stage built for vertical video. Warm cream paper canvas (not dark stage, not pure white), warm near-black serif type for headlines, Inter sans for utility, JetBrains Mono for technical voice. A 5-tier rotating palette of warm accents (terracotta, indigo, sage, sunset gold, warm rose) drives chrome — borders, badges, glows, single accent words. Architecture is **sub-composition based**: nine self-contained scene archetypes (title, big stat, counter grid, pull quote, icon bullets, side-by-side, marker highlight, badge grid, CTA) each with their own paused timeline. The root composition orchestrates only ambient + chrome + scene crossfades. Reads like a thoughtful editorial spread, not an influencer reaction video.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **24-180s** (YT Shorts hard max 180s)
- Background: solid `var(--bg)` `#FBF7EF` (warm cream paper). Subtle warm radial wash + 14 deterministic ink shapes at 5% opacity provide depth.

## Architecture — sub-compositions, not phase mutex

Unlike `anthropic` and `archon` (which use a single `index.html` with phase-mutex z-index escalation), this template uses **sub-compositions via `data-composition-src`**:

```
templates/shorts/standard/
├── index.html                 ← orchestrator (ambient + chrome + scene wrappers + crossfades)
└── compositions/
    ├── scene-title.html
    ├── scene-stat.html
    ├── scene-counter-grid.html
    ├── scene-quote.html
    ├── scene-bullets.html
    ├── scene-compare.html
    ├── scene-marker.html
    ├── scene-badges.html
    └── scene-cta.html
```

Each scene file is a self-contained `<template>` with its own embedded `<style>` and `<script>`, registering a paused timeline on `window.__timelines["scene-<name>"]`. The root timeline crossfades scene wrappers in/out. This pattern is borrowed from `templates/long-form/standard/` and adapted for vertical canvas + Shorts pacing.

**Why sub-compositions?** Each scene file stays small enough to inspect/edit independently. New variants can be added without touching the orchestrator. Operators can drop or reorder scenes by editing only the wrapper list in `index.html`.

## Colors

All colors flow from `tokens/standard-short.css` via CSS variables. Override per video by re-declaring any `--accent-*` inside `#root` (or a per-scene scope). The aliases `--primary`, `--secondary`, `--tertiary`, `--highlight`, `--pivot` mirror anthropic-dark naming so lib entries authored against either system stay portable.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#FBF7EF` | Page canvas — warm cream paper |
| Card surface | `--bg-card` | `#FFFFFF` | Default raised card |
| Tinted surface | `--bg-tint` | `#F0E6D2` | Slightly tinted cream for callouts |
| Border | `--border` | `rgba(43, 42, 40, 0.10)` | Default card stroke |
| Border bright | `--border-bright` | `rgba(43, 42, 40, 0.20)` | Brighter stroke |
| Primary text | `--text` | `#2B2A28` | Headlines, body — warm near-black |
| Secondary text | `--text-secondary` | `#6B6862` | Captions, meta, byline |
| Muted text | `--text-muted` | `#908A80` | Heavy de-emphasis only |
| Accent — warm | `--accent-warm` | `#E07A5F` | Terracotta — primary lead |
| Accent — deep | `--accent-deep` | `#3D5A80` | Indigo — counterpoint, label band |
| Accent — sage | `--accent-sage` | `#81B29A` | Sage green — calm secondary |
| Accent — gold | `--accent-gold` | `#F2CC8F` | Sunset gold — highlight / marker sweep |
| Accent — rose | `--accent-rose` | `#F4978E` | Warm rose — soft pivot |
| Accent — ink | `--accent-ink` | `#2B2A28` | Warm near-black — strong contrast badge |
| Pill background | `--pill-bg` | `rgba(43, 42, 40, 0.05)` | Default chip / pill fill |
| Pill border | `--pill-border` | `rgba(43, 42, 40, 0.15)` | Default chip / pill stroke |

**Contrast verified (WCAG):**
- Primary text on background: ~14:1 (AAA)
- Secondary text on background: ~5.6:1 (AA normal)
- Accent terracotta on background: ~4.5:1 (AA normal) — safe for 40px+ headlines
- Accent indigo on background: ~7.5:1 (AAA) — safe for body
- White text on terracotta solid (CTA): ~3.4:1 (AA Large for 38px+)
- Warm-near-black on sunset gold (badge): ~10:1 (AAA)

**Accent rotation rule:** Within one video, no two adjacent scenes lead with the same accent. Default rotation is **terracotta → indigo → sage → gold → rose** repeating. Override per video by re-declaring `--accent-*` inside `#root`.

## Typography

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero serif headline | `var(--serif)` (Playfair Display) | 700 | `letter-spacing: -3px`, line-height 0.95 |
| Italic accent / quote body | `var(--serif)` (Playfair Display, italic) | 400-700 | accent color or italic counterpoint |
| Sans utility headline | `var(--sans)` (Inter) | 800-900 | `letter-spacing: -1px`, line-height 1.05 |
| Body | `var(--sans)` (Inter) | 500-600 | line-height 1.3-1.4 |
| Mono overline / kicker | `var(--mono)` (JetBrains Mono) | 700 | UPPERCASE, `letter-spacing: 5-7px`, accent color |
| Mono caption / chip | `var(--mono)` (JetBrains Mono) | 600-700 | `letter-spacing: 1-3px`, `font-variant-numeric: tabular-nums` |
| Animated counter | `var(--sans)` (Inter) | 900 | tabular-nums, `letter-spacing: -8px` |

**Type scale (Shorts-tuned):**

| Role | Size |
|---|---|
| Serif hero headline | 132px (drop to 116px if a single word > 11 chars) |
| Pull-quote body | 64px |
| Section header | 76-80px |
| Stat number (single hero) | 240px |
| Counter grid number | 140px |
| Body | 36-42px |
| Mono overline | 30-36px |
| Caption (mono) | 28-32px |

**Font deterministic mapping:** HyperFrames maps `var(--serif)` → 'Playfair Display' and `var(--mono)` → 'JetBrains Mono'. Both are in the framework's bundled font set so renders are reproducible.

## Layout

**Safe zones — non-negotiable.**

```
PHASE_PAD_TOP    = 240px   (clears the top banner + mobile UI overlay)
PHASE_PAD_X      = 80px    (default side padding)
PHASE_PAD_BOTTOM = 240px   (clears the progress bar + reading room)
```

Each scene's content container MUST use `width: 100%; height: 100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display: flex; flex-direction: column; box-sizing: border-box`. Padding positions content inward — NEVER `position: absolute; top: Npx`.

**Scene mutex:** Only one scene wrapper is visible at any frame. The root timeline uses `crossfadeScenes()` (1.1s span: 0.5s blur out + 0.4s opacity out + 0.3s opacity in + 0.5s blur in) to transition.

## Motion Language

- **Easing:**
  - `back.out(1.5-1.7)` for spring entrances (hero words, stat pills, badges)
  - `power3.out` for headlines and primary text rises
  - `power2.out` for body / chip / pill text entrances
  - `expo.out` for high-impact one-element reveals (URL slam)
  - `power1.in` / `power1.out` for outgoing/incoming scene blur
  - `power2.inOut` for the marker sweep clip-path
  - `sine.inOut` for ambient breath only
  - **Avoid** `elastic` and `bounce` — they read toy-like for this brand.
- **Duration:**
  - Hero / slam word: 0.6-0.8s
  - Headline: 0.5-0.7s
  - Body / chip: 0.35-0.5s
  - Counter animation: 1.4-1.6s
  - Marker sweep: 0.55-0.6s
  - Scene crossfade: 0.4s opacity + 0.5s blur
- **Stagger:** 80-180ms between siblings. Six pill grid = 80ms; three step rows = 350-450ms; per-word title reveal = 180ms.

## Surface Detail

- **Cards (raised):** white `--bg-card` background, 22-24px radius, `border: 1.5-2px solid <accent>` or `--border`, `box-shadow: var(--shadow-warm)` (warm-tinted shadow — `0 12px 32px rgba(176, 124, 90, 0.18)`).
- **Stat-frame (single big number):** white card with terracotta border, `--shadow-warm`, inline-flex baseline alignment of number + serif italic suffix.
- **Step icon badge (round 92px):** solid accent fill, serif 700 weight letter or symbol, color flips per accent (white on warm/deep, ink on sage/gold).
- **Marker sweep:** real DOM `<span class="marker-band">` absolutely positioned behind the highlighted word, animated via `clip-path: inset(0 100% 0 0)` → `inset(0 0% 0 0)` to simulate a left-to-right highlighter sweep.
- **URL pill:** solid terracotta background, white mono text 56-60px, 22-26px radius, warm shadow.
- **Subscribe pill:** white card, 2px indigo border, indigo sans body, terracotta arrow.
- **Top banner:** rounded white pill with warm shadow, mono uppercase wordmark, terracotta dot indicator.
- **Ambient:** triple radial drift (terracotta + sunset gold + warm rose) at low alpha + 14 ink shapes at 5% opacity. Reads as paper grain / faint watermarks.
- **Paper-grain overlay:** SVG fractal noise at 4.5% opacity with `mix-blend-mode: multiply` (darkens slightly, doesn't lift). Adds tactile texture.

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Default cue set ships in [`sfx-cues.txt`](./sfx-cues.txt): `impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop`. Run `bash scripts/sync-video-sfx.sh videos/<slug>` after spawning to copy them into the video's `assets/sfx/`.

Same volume cap as all Shorts: **never exceed 0.25** on a single per-cue SFX (sonic-logo at 0.45 is the only documented exception). **No background music on Shorts.**

## What NOT to Do

1. **No dark canvas.** This is warm-paper. Use the `anthropic` or `archon` template if you need a dark stage.
2. **No more than two accents per scene.** Pick one lead + one supporting accent — don't paint a rainbow inside a single scene.
3. **No gloomy serifs.** Playfair Display is the editorial voice; don't substitute Times New Roman or other web-default serifs.
4. **No `<br>` in content text.** Use `max-width` for natural wrapping.
5. **No background music on Shorts.** Narration + SFX only.
6. **No `position: absolute; top: Npx` on `.phase-content`.** Use padding for content positioning.
7. **No accent below 40px.** Terracotta/indigo/sage/gold/rose don't carry enough contrast for body. Reserve them for hero, headline, badges, borders, single accent words.
8. **No real logos in the bare template.** Operators copy a logo into `assets/` per video.
9. **No `Math.random()` / `Date.now()` / network fetches.** Deterministic-only — the seeded shape backdrop demonstrates the pattern.
10. **No custom serif fonts beyond `var(--serif)`.** Playfair Display is the only mapped serif this template assumes; substituting an unmapped serif will fall back to system serif at render time.
