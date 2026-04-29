# Standard Short — Warm Paper Editorial

**Mood:** Premium publication, thoughtful, warm | **Best for:** Any vertical Short that benefits from a warm editorial feel rather than a dark stage — explainers, how-to walkthroughs, news, opinion, comparisons, tips.

A warm cream paper canvas with terracotta/indigo/sage/sunset-gold/warm-rose accents. Playfair Display serif headlines paired with Inter sans utility and JetBrains Mono technical voice. **Sub-composition architecture** — nine self-contained scene archetypes (title / stat / counter-grid / quote / bullets / compare / marker / badges / cta), each with its own paused timeline. The canonical brand-neutral baseline for vertical Shorts in this repo. Intentionally different from `anthropic-dark.md` (dark stage Inter-only) and `archon-cyan-magenta.md` (dark stage with brand gradient) so the channel can show range.

## Tokens

[`shared/lib/tokens/standard-short.css`](../tokens/standard-short.css)

Defines: `--bg`, `--bg-card`, `--bg-surface`, `--bg-tint`, `--border`, `--border-bright`, `--shadow-warm`, `--accent-warm`, `--accent-deep`, `--accent-sage`, `--accent-gold`, `--accent-rose`, `--accent-ink`, `--primary` / `--secondary` / `--tertiary` / `--highlight` / `--pivot` (aliases), `--text`, `--text-secondary`, `--text-muted`, `--text-on-warm`, `--text-on-deep`, `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--sans`, `--serif`, `--mono`.

The alias names mirror anthropic-dark naming so lib entries authored against either system stay portable.

## Palette roles

| Role         | Token            | When to use                                                          |
| ------------ | ---------------- | -------------------------------------------------------------------- |
| Background   | `--bg`           | Canvas — warm cream paper `#FBF7EF`.                                 |
| Card surface | `--bg-card`      | Default raised card, white.                                          |
| Body text    | `--text`         | Headlines, body — warm near-black `#2B2A28`.                         |
| Caption      | `--text-secondary` | Bylines, italic supporting copy.                                   |
| Primary      | `--accent-warm`  | Terracotta — phase 1 lead, hero slam, primary CTA.                   |
| Secondary    | `--accent-deep`  | Indigo — overlines, label bands, subscribe pill border.              |
| Tertiary     | `--accent-sage`  | Sage green — calm secondary, success.                                |
| Highlight    | `--accent-gold`  | Sunset gold — marker sweep, hero stat highlights.                    |
| Pivot        | `--accent-rose`  | Warm rose — soft pivot, secondary callout.                           |
| Strong       | `--accent-ink`   | Warm near-black — high-contrast badge fill.                          |

**Accent rotation rule:** within one video, no two adjacent scenes lead with the same accent. Default rotation is **terracotta → indigo → sage → gold → rose** repeating. Override per video by re-declaring `--accent-*` inside `#root`.

## Typography

| Role             | Family                                | Weight  | Treatment                                             |
| ---------------- | ------------------------------------- | ------- | ----------------------------------------------------- |
| Hero serif       | `--serif` (Playfair Display)          | 700     | `letter-spacing: -3px`, line-height 0.95              |
| Italic accent    | `--serif` (Playfair Display, italic)  | 400-700 | accent-warm color, italic counterpoint               |
| Sans utility     | `--sans` (Inter)                      | 800-900 | `letter-spacing: -1px`, line-height 1.05              |
| Body             | `--sans` (Inter)                      | 500-600 | line-height 1.3-1.4                                   |
| Mono overline    | `--mono` (JetBrains Mono)             | 700     | UPPERCASE, `letter-spacing: 5-7px`, accent color      |
| Counter / stat   | `--sans` (Inter)                      | 900     | tabular-nums, `letter-spacing: -8px`                  |

**Type scale (Shorts-tuned):** Hero serif 132px · Pull-quote body 64px · Section header 76-80px · Stat number 240px · Counter grid 140px · Body 36-42px · Overline 30-36px · Caption 28-32px.

## Motion Signature

| Easing           | Use for                                                   |
| ---------------- | --------------------------------------------------------- |
| `back.out(1.5-1.7)` | Spring entrances (hero words, stat pills, badges)       |
| `power3.out`     | Headlines and primary text rises                          |
| `power2.out`     | Body / chip / pill text entrances                         |
| `expo.out`       | High-impact one-element reveals (URL slam)                |
| `power1.in`      | Outgoing scene blur+fade                                  |
| `power2.inOut`   | Marker sweep clip-path animation                          |
| `sine.inOut`     | Ambient breath only                                       |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Stagger:** 80ms between badge pills; 180ms between title words; 350-450ms between bullet rows; 200-300ms between counter-grid rows.

## Architecture — sub-compositions

Unlike `anthropic-dark` and `archon` which use a single `index.html` with phase-mutex z-index escalation, this style uses **sub-compositions via `data-composition-src`**:

- Root `index.html` orchestrates: ambient + chrome + scene wrappers + crossfades only.
- Each scene is a self-contained `<template>` in `compositions/scene-<name>.html`.
- Each scene registers its own paused timeline on `window.__timelines["scene-<name>"]`.
- Scene wrappers are mutex-visible — only one is opaque at any frame.

This pattern is borrowed from `templates/long-form/standard/` and adapted for vertical canvas + Shorts pacing.

## Suggested Scene Archetypes

This style ships nine archetypes; mix-and-match per video:

| Archetype | File | Use for |
|---|---|---|
| Title | `scene-title.html` | Editorial intro / chapter card |
| Stat | `scene-stat.html` | One-number reveal with serif italic suffix |
| Counter grid | `scene-counter-grid.html` | Three parallel counters in a stack |
| Quote | `scene-quote.html` | Pull-quote callout with attribution |
| Bullets | `scene-bullets.html` | Three icon+text rows with circular badges |
| Compare | `scene-compare.html` | Before/after with line-through "before" + accented "after" |
| Marker | `scene-marker.html` | Headline with left-to-right marker sweep on key word |
| Badges | `scene-badges.html` | 2x3 grid of pill chips, full palette showcase |
| CTA | `scene-cta.html` | URL pill + subscribe button |

## Surface detail formulas

- **Cards:** white `--bg-card`, 22-24px radius, `border: 1.5-2px solid <accent>`, `box-shadow: var(--shadow-warm)` (warm-tinted).
- **Stat-frame:** white card, terracotta border, inline-flex baseline alignment of number + serif italic suffix.
- **Step icon badge (round 92px):** solid accent fill, serif 700 weight letter or symbol, color flips per accent.
- **Marker sweep:** real DOM `<span class="marker-band">` absolutely positioned behind highlighted word, `clip-path: inset(0 100% 0 0)` → `inset(0 0% 0 0)` for left-to-right reveal.
- **URL pill:** solid terracotta background, white mono text 56-60px, 22-26px radius.
- **Subscribe pill:** white card, 2px indigo border, indigo body text, terracotta arrow.
- **Top banner:** white pill, warm shadow, mono uppercase wordmark, terracotta dot indicator.
- **Ambient:** triple radial drift (terracotta + sunset gold + warm rose) + 14 ink shapes at 5% opacity.
- **Paper-grain overlay:** SVG fractal noise at 4.5% opacity with `mix-blend-mode: multiply`.

## Audio / SFX

Same volume cap as all Shorts: never exceed **0.25** on a single per-cue SFX. **No background music on Shorts.**

| Cue                | Use on                          | Default `data-volume` |
| ------------------ | ------------------------------- | --------------------- |
| `impact-slam`      | Hero word reveal                | 0.15                  |
| `scale-slam`       | Stat-pill / card entrance       | 0.15                  |
| `cinematic-whoosh` | Scene change                    | 0.11                  |
| `spring-pop`       | Bullet row / badge entrance     | 0.11                  |
| `pop`              | Small chip / counter pop        | 0.10                  |

## What NOT to Do

1. No dark canvas. This style is warm-paper only.
2. No more than two accents per scene.
3. No serif fonts beyond Playfair Display.
4. No `<br>` in content text — use `max-width`.
5. No background music on Shorts.
6. No `position: absolute; top: Npx` on scene content containers — use padding.
7. No accent below 40px — reserve for hero, headline, badges, single accent words.
8. No real logos in the bare template — operators copy per video.
9. No `Math.random()` / `Date.now()` / network fetches at render time.
10. No phase-mutex `z-index` escalation in a single index.html. This style uses sub-compositions; if you find yourself stacking `#phase1 / #phase2 / #phase3` z-indexes inside `index.html`, you've drifted to the anthropic pattern — switch back to scene wrappers.
