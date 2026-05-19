# DESIGN — Editorial Shorts (Warm Paper, Single Accent, Source Serif)

Visual system for **YouTube Shorts** (1080x1920, 30fps, 24-180s) in an **editorial-light, single-accent** aesthetic. Warm cream canvas, **Source Serif 4** italic for emphasis, single **terracotta** accent system — the same design language as our long-form editorial videos, sized down for vertical.

This template is the **editorial variant** of `templates/shorts/standard/`. Use it when the topic benefits from the mood of a long-form publication (deep explainers, essay-style overviews, what-is-X-and-why deep-dives) and you want restraint instead of palette variety.

## Style Prompt

A measured, editorial publication stage built for vertical video. Warm cream paper canvas (not dark stage, not pure white), warm near-black serif type for headlines, **Source Serif 4 italic** for accent emphasis, Inter sans for utility, JetBrains Mono for technical voice. A **single terracotta accent** drives chrome — italic accent words, borders, marker sweeps, URL pill. Architecture is **sub-composition based**: 15 self-contained scene archetypes each with their own paused timeline. The root composition orchestrates only ambient + chrome + scene crossfades. Reads like a thoughtful editorial spread — slower, more deliberate than the 5-accent `standard` variant.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **24-180s** (YT Shorts hard max 180s)
- Background: solid `var(--bg)` `#F4F1EA` (warm cream paper, slightly deeper than `standard`). Subtle warm radial wash + 14 deterministic ink shapes at 3% opacity provide depth. 2% paper-grain overlay adds tactile texture.

## Architecture — sub-compositions, not phase mutex

Like `standard`, this template uses **sub-compositions via `data-composition-src`**:

```
templates/shorts/editorial/
├── index.html                  ← orchestrator (ambient + chrome + scene wrappers + crossfades)
└── compositions/
    ├── scene-title.html
    ├── scene-stat.html
    ├── scene-chart.html
    ├── scene-counter-grid.html
    ├── scene-typewriter.html
    ├── scene-code-block.html
    ├── scene-quote.html
    ├── scene-bullets.html
    ├── scene-process-flow.html
    ├── scene-compare.html
    ├── scene-timeline.html
    ├── scene-marker.html
    ├── scene-image-card.html
    ├── scene-badges.html
    └── scene-cta.html
```

Each scene file is a self-contained `<template>` with its own embedded `<style>` and `<script>`, registering a paused timeline on `window.__timelines["scene-<name>"]`. The root timeline crossfades scene wrappers in/out.

**Why sub-compositions?** Each scene file stays small enough to inspect/edit independently. New variants can be added without touching the orchestrator. Operators can drop or reorder scenes by editing only the wrapper list in `index.html`.

## Colors

All colors flow from `tokens/editorial-short.css` via CSS variables. Override per video by re-declaring any `--accent-N` inside `#root`. The aliases `--primary`, `--secondary`, `--tertiary`, `--highlight`, `--pivot` re-bind automatically — lib entries authored against either system stay portable.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#F4F1EA` | Page canvas — warm cream paper (slightly deeper than `standard`) |
| Card surface | `--bg-card` | `#FBF8F1` | Default raised card |
| Surface | `--bg-surface` | `#EFEBE0` | Slightly recessed surface |
| Tinted surface | `--bg-tint` | `#E8E1CF` | Strongly tinted cream for callouts |
| Border | `--border` | `rgba(28, 26, 24, 0.10)` | Default card stroke |
| Border bright | `--border-bright` | `rgba(199, 90, 63, 0.50)` | Terracotta-tinted stroke for emphasis |
| Primary text | `--text` | `#1A1815` | Headlines, body — warm near-black |
| Secondary text | `--text-secondary` | `#5C544B` | Captions, meta, byline |
| Muted text | `--text-muted` | `#8A8175` | Heavy de-emphasis only |
| Text on warm | `--text-on-warm` | `#FBF8F1` | Used inside terracotta pills |
| Accent — primary | `--accent-1` | `#C75A3F` | Terracotta — lead accent (italic emphasis, marker sweeps, URL pill) |
| Accent — deep | `--accent-2` | `#B14938` | Darker terracotta — top-banner wordmark, secondary chrome |
| Accent — sage | `--accent-3` | `#586F4F` | Deep sage green — supporting accent (rarely lead) |
| Pill background | `--pill-bg` | `rgba(28, 26, 24, 0.05)` | Default chip / pill fill |
| Pill border | `--pill-border` | `rgba(28, 26, 24, 0.15)` | Default chip / pill stroke |

**Contrast verified (WCAG):**
- Primary text on background: ~15:1 (AAA)
- Secondary text on background: ~6.5:1 (AA normal)
- Accent terracotta `#C75A3F` on background: ~4.4:1 (AA Large for 18pt+)
- Accent deep `#B14938` on background: ~5.8:1 (AA normal)
- Accent sage `#586F4F` on background: ~6.8:1 (AAA normal)
- White on terracotta pill: ~3.6:1 (AA Large for 38px+)

**Restraint rule:** Within one video, the **lead accent** is `--accent-1` (terracotta). `--accent-2` and `--accent-3` are for one moment per scene — never simultaneously dominant. This is the opposite of `standard`'s 5-accent rotation: editorial restraint is the whole point. If a scene needs more than two accents, you're probably reaching for the wrong template.

## Typography

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero serif headline | `var(--serif)` (Source Serif 4) | 700-900 | `letter-spacing: -1px to -2px`, line-height 0.95-1.0 |
| Italic accent | `var(--serif)` (Source Serif 4, italic) | 400-700 | accent color (`--accent-1`) for emphasis words |
| Body serif | `var(--serif)` (Source Serif 4) | 400-600 | line-height 1.3-1.4 |
| Sans utility headline | `var(--sans)` (Inter) | 700-900 | `letter-spacing: -1px`, line-height 1.05 |
| Mono overline / kicker | `var(--mono)` (JetBrains Mono) | 700-800 | UPPERCASE, `letter-spacing: 5-8px`, accent-2 color |
| Mono caption / chip | `var(--mono)` (JetBrains Mono) | 600-700 | `letter-spacing: 1-4px`, `font-variant-numeric: tabular-nums` |
| Animated counter | `var(--sans)` (Inter) | 900 | tabular-nums, `letter-spacing: -8px` |

**Type scale (Shorts-tuned):**

| Role | Size |
|---|---|
| Serif hero headline | 96-132px |
| Pull-quote body | 56-64px |
| Section header | 72-80px |
| Stat number (single hero) | 240px |
| Counter grid number | 140px |
| Body | 36-44px |
| Mono overline | 28-32px |
| Caption (mono) | 22-28px |

**Font deterministic mapping:** Source Serif 4 is loaded via Google Fonts with full optical-size range 8-60 and italic. Both styles are explicitly preconnected in `<head>` to avoid FOUT.

## Layout

**Safe zones — non-negotiable.**

```
PHASE_PAD_TOP    = 240px   (clears the top banner + mobile UI overlay)
PHASE_PAD_X      = 80px    (default side padding)
PHASE_PAD_BOTTOM = 240px   (clears the progress bar + reading room)
```

Each scene's content container MUST use `width: 100%; height: 100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display: flex; flex-direction: column; box-sizing: border-box`. Padding positions content inward — NEVER `position: absolute; top: Npx`.

**Scene mutex:** Only one scene wrapper is visible at any frame. The root timeline uses `crossfadeScenes()` (1.1s span) to transition. **Shapes reposition at every scene boundary** (paired with the cinematic-whoosh SFX on track 3).

## Motion Language

- **Easing:**
  - `back.out(1.5-1.7)` for spring entrances (italic accent words, stat pills, badges)
  - `power3.out` for headlines and primary text rises
  - `power2.out` for body / chip / pill text entrances
  - `expo.out` for high-impact one-element reveals (URL slam)
  - `power1.in` / `power1.out` for outgoing/incoming scene blur
  - `power2.inOut` for shape reposition + marker sweep clip-path
  - `sine.inOut` for ambient breath only
  - **Avoid** `elastic` and `bounce` — they read toy-like; editorial is measured.
- **Duration:**
  - Hero / slam word: 0.6-0.8s
  - Headline: 0.5-0.7s
  - Body / chip: 0.35-0.5s
  - Counter animation: 1.4-1.6s
  - Marker sweep: 0.55-0.6s
  - Scene crossfade: 0.4s opacity + 0.5s blur
  - Shape reposition: 1.0s `power2.inOut` (fires 0.4s before scene swap)
- **Stagger:** 80-180ms between siblings. Six pill grid = 80ms; three step rows = 350-450ms; per-word title reveal = 150-180ms.

## Surface Detail

- **Cards (raised):** `--bg-card` background, 18-24px radius, `border: 1px solid var(--border)` or `--border-bright` for emphasis. `box-shadow: none` (the editorial card is flat — depth comes from the warm cream contrast, not drop shadows).
- **Stat-frame (single big number):** flat card with terracotta border, inline-flex baseline alignment of number + serif italic suffix.
- **Step icon badge (round 92px):** solid terracotta fill, serif 700 weight letter or symbol, white glyph.
- **Marker sweep:** real DOM `<span class="marker-band">` absolutely positioned behind the highlighted word, animated via `clip-path: inset(0 100% 0 0)` → `inset(0 0% 0 0)` for a left-to-right highlighter feel.
- **URL pill:** solid terracotta background, white mono text 56-60px, 22-26px radius (no shadow — flat editorial chrome).
- **Subscribe pill:** white card, 2px terracotta border, terracotta mono body.
- **Top chrome:** centered mono wordmark + thin terracotta rule (no card pill — reads as a chapter heading).
- **Source URL chip (bottom-right):** subtle backdrop-blur chip with terracotta accent label + ink-tone URL text. Persistent across all scenes.
- **Ambient:** dual radial drift (terracotta + deep terracotta) at low alpha.
- **Paper-grain overlay:** SVG fractal noise at 2% opacity with `mix-blend-mode: multiply`. Adds tactile texture.

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Default cue set ships in [`sfx-cues.txt`](./sfx-cues.txt): `impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop`. Run `bash scripts/sync-video-sfx.sh videos/<slug>` after spawning to copy them into the video's `assets/sfx/`.

Same volume cap as all Shorts: **never exceed 0.25** on a single per-cue SFX (sonic-logo at 0.45 is the only documented exception). **No background music on Shorts.**

## What NOT to Do

1. **No dark canvas.** This is warm-paper. Use the `anthropic` or `archon` template if you need a dark stage.
2. **No more than one lead accent per scene.** The editorial variant's point is restraint — one terracotta italic emphasis word per beat is plenty. Reaching for `--accent-3` (sage) is rare and never simultaneous with `--accent-1`.
3. **No Playfair Display, Times New Roman, or other web-default serifs.** Source Serif 4 is the editorial voice. Falling back to Playfair gives a magazine cover feel that fights this template's restraint.
4. **No `<br>` in content text.** Use `max-width` for natural wrapping.
5. **No background music on Shorts.** Narration + SFX only.
6. **No `position: absolute; top: Npx` on scene content containers.** Use padding for content positioning.
7. **No accent below 36px.** Terracotta / deep / sage don't carry enough contrast for body. Reserve them for hero, headline, badges, borders, single accent italic words.
8. **No real logos in the bare template.** Operators copy a logo into `assets/` per video.
9. **No `Math.random()` / `Date.now()` / network fetches.** Deterministic-only.
10. **No font fallback drift.** This template assumes Source Serif 4. If the framework's font cache misses, the fallback chain in `editorial-short.css` falls through to Source Serif Pro → Playfair Display → EB Garamond → Georgia — all serif-only.
