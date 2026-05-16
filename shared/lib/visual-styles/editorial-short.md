# Editorial Short — Warm Paper + Source Serif + Single Accent

**Mood:** Editorial restraint, deep-explainer, measured | **Best for:** Vertical Shorts where the topic deserves the mood of a long-form publication — overviews of a spec / standard / open protocol, essay-style "what is X and why" deep-dives, cross-tool comparisons. Companion videos to long-form on the same topic.

A warm cream paper canvas (slightly deeper than `standard-short`) with a **single terracotta accent system** — terracotta lead, deep warm brown counterpoint, sage green tertiary. Source Serif 4 italic for emphasis, Inter sans utility, JetBrains Mono technical voice. **Sub-composition architecture** with 15 scene archetypes. The editorial variant of `standard-short` — same canvas family, opposite philosophy: restraint instead of 5-accent rotation.

Intentionally different from `standard-short.md` (5-accent + Playfair) and from the dark-stage families (`anthropic-dark`, `claude-code-dark`, `google-cinematic`, `openai-mono`) so the channel can show range across both light and dark editorial registers.

## Tokens

[`shared/lib/tokens/editorial-short.css`](../tokens/editorial-short.css)

Defines: `--bg`, `--bg-card`, `--bg-surface`, `--bg-tint`, `--border`, `--border-bright`, `--shadow-warm`, `--accent-1`, `--accent-2`, `--accent-3`, `--accent-4`, `--accent-warn`, `--accent-stat`, `--accent-warm` / `--accent-deep` / `--accent-sage` / `--accent-gold` / `--accent-rose` / `--accent-ink` (standard-template aliases), `--primary` / `--secondary` / `--tertiary` / `--highlight` / `--pivot` (alias-of-accent-N), `--text`, `--text-secondary`, `--text-muted`, `--text-on-warm`, `--text-on-deep`, `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--sans`, `--serif`, `--mono`.

The standard-template alias surface (`--accent-warm` etc.) is kept so scene HTML authored against `standard-short` renders unmodified — editorial restraint is enforced at the **content / authoring** level (one lead accent per scene), not by removing variable surface.

## Palette roles

| Role         | Token            | When to use                                                          |
| ------------ | ---------------- | -------------------------------------------------------------------- |
| Background   | `--bg`           | Canvas — warm cream paper `#F4F1EA` (slightly deeper than standard). |
| Card surface | `--bg-card`      | Default raised card `#FBF8F1`.                                       |
| Body text    | `--text`         | Headlines, body — warm near-black `#1A1815`.                         |
| Caption      | `--text-secondary` | Bylines, italic supporting copy `#5C544B`.                          |
| Primary      | `--accent-1`     | Terracotta `#C75A3F` — lead accent, italic emphasis words, URL pill. |
| Secondary    | `--accent-2`     | Darker terracotta `#B14938` — top-banner wordmark, secondary chrome. |
| Tertiary     | `--accent-3`     | Deep sage `#586F4F` — supporting accent (rarely lead).               |
| Standard alias — warm | `--accent-warm` | = `--accent-1` for portability with `standard-short` scenes.       |
| Standard alias — deep | `--accent-deep` | Deep warm brown `#7A4A3A` — editorial counterpoint, NOT indigo.     |

**Restraint rule:** Within one video, **only `--accent-1` (terracotta) is the lead accent**. `--accent-2` and `--accent-3` are reserved for one supporting moment per scene — never simultaneously dominant. This is the deliberate opposite of `standard-short`'s 5-accent rotation. If a scene needs more than two accents, the wrong template was chosen.

## Typography

| Role             | Family                                | Weight  | Treatment                                             |
| ---------------- | ------------------------------------- | ------- | ----------------------------------------------------- |
| Hero serif       | `--serif` (Source Serif 4)            | 700-900 | `letter-spacing: -1px to -2px`, line-height 0.95-1.0  |
| Italic accent    | `--serif` (Source Serif 4, italic)    | 400-700 | accent-1 (terracotta), for emphasis words only        |
| Body serif       | `--serif` (Source Serif 4)            | 400-600 | line-height 1.3-1.4                                   |
| Sans utility     | `--sans` (Inter)                      | 700-900 | `letter-spacing: -1px`, line-height 1.05              |
| Mono overline    | `--mono` (JetBrains Mono)             | 700-800 | UPPERCASE, `letter-spacing: 5-8px`, accent-2 color    |
| Counter / stat   | `--sans` (Inter)                      | 900     | tabular-nums, `letter-spacing: -8px`                  |

**Type scale (Shorts-tuned):** Hero serif 96-132px · Pull-quote body 56-64px · Section header 72-80px · Stat number 240px · Counter grid 140px · Body 36-44px · Mono overline 28-32px · Caption (mono) 22-28px.

**Font deterministic mapping:** Source Serif 4 loaded via Google Fonts with optical-size range 8-60 and italic. Fallback chain: `Source Serif 4 → Source Serif Pro → Playfair Display → EB Garamond → Georgia → serif`. All terms in the fallback chain are serif-only — no sans drift.

## Motion Signature

| Easing           | Use for                                                   |
| ---------------- | --------------------------------------------------------- |
| `back.out(1.5-1.7)` | Spring entrances (italic accent words, stat pills, badges) |
| `power3.out`     | Headlines and primary text rises                          |
| `power2.out`     | Body / chip / pill text entrances                         |
| `expo.out`       | High-impact one-element reveals (URL slam)                |
| `power1.in`      | Outgoing scene blur+fade                                  |
| `power2.inOut`   | Shape reposition + marker sweep clip-path                 |
| `sine.inOut`     | Ambient breath only                                       |

**Avoid:** `elastic`, `bounce` — read toy-like; editorial is measured.

**Stagger:** 80ms between badge pills; 150-180ms between title words; 350-450ms between bullet rows; 200-300ms between counter-grid rows.

## Architecture — sub-compositions

Same architecture as `standard-short`: **sub-compositions via `data-composition-src`**.

- Root `index.html` orchestrates: ambient + chrome + scene wrappers + crossfades only.
- Each scene is a self-contained `<template>` in `compositions/scene-<name>.html`.
- Each scene registers its own paused timeline on `window.__timelines["scene-<name>"]`.
- Scene wrappers are mutex-visible — only one is opaque at any frame.
- **Shape backdrop repositions** at every scene boundary (paired with `cinematic-whoosh` SFX).

## Suggested Scene Archetypes

15 archetypes inherited from `standard-short` (same `compositions/scene-*.html` files render under the editorial palette via the standard-template alias layer):

| Archetype | File | Use for |
|---|---|---|
| Title | `scene-title.html` | Editorial intro / chapter card |
| Stat | `scene-stat.html` | One-number reveal with serif italic suffix |
| Chart | `scene-chart.html` | Animated bar chart with staggered reveal |
| Counter grid | `scene-counter-grid.html` | Three parallel counters in a stack |
| Typewriter | `scene-typewriter.html` | Terminal type-on with punchline + chart |
| Code block | `scene-code-block.html` | macOS-style window with syntax-highlighted code |
| Quote | `scene-quote.html` | Pull-quote callout with attribution |
| Bullets | `scene-bullets.html` | Three icon+text rows with circular badges |
| Process flow | `scene-process-flow.html` | 4-node connected diagram |
| Compare | `scene-compare.html` | Before/after with line-through "before" + accented "after" |
| Timeline | `scene-timeline.html` | Horizontal milestones |
| Marker | `scene-marker.html` | Headline with left-to-right marker sweep on key word |
| Image card | `scene-image-card.html` | Framed visual asset with caption |
| Badges | `scene-badges.html` | 2x3 grid of pill chips |
| CTA | `scene-cta.html` | URL pill + subscribe button |

## Surface detail formulas

- **Cards:** `--bg-card` background, 18-24px radius, `border: 1px solid var(--border)` or `--border-bright` for emphasis. `box-shadow: var(--shadow-warm)` is low-intensity (warm-tinted, rgba(122, 74, 58, 0.10)) — the editorial card is nearly flat.
- **Stat-frame:** flat card with terracotta border, inline-flex baseline alignment of number + serif italic suffix.
- **Step icon badge (round 92px):** solid terracotta fill, serif 700 weight letter or symbol, white glyph.
- **Marker sweep:** real DOM `<span class="marker-band">` absolutely positioned behind highlighted word, `clip-path: inset(0 100% 0 0)` → `inset(0 0% 0 0)` for left-to-right reveal.
- **URL pill:** solid terracotta background, white mono text 56-60px, 22-26px radius. No shadow — flat editorial chrome.
- **Subscribe pill:** white card, 2px terracotta border, terracotta mono body.
- **Top chrome:** centered mono wordmark + thin terracotta rule (no card pill — reads as a chapter heading).
- **Source URL chip (bottom-right):** subtle backdrop-blur chip with ink-tone label + ink-tone URL text. Persistent across all scenes.
- **Ambient:** dual radial drift (terracotta + deep terracotta) at low alpha + 14 ink shapes at ~3% opacity.
- **Paper-grain overlay:** SVG fractal noise at 2% opacity with `mix-blend-mode: multiply`.

## Audio / SFX

Same volume cap as all Shorts: never exceed **0.25** on a single per-cue SFX. **No background music on Shorts.**

| Cue                | Use on                          | Default `data-volume` |
| ------------------ | ------------------------------- | --------------------- |
| `impact-slam`      | Hero word reveal                | 0.15                  |
| `scale-slam`       | Stat-pill / card entrance       | 0.15                  |
| `cinematic-whoosh` | Scene change (fires at scene transition with shape reposition) | 0.11 |
| `spring-pop`       | Bullet row / badge entrance     | 0.11                  |
| `pop`              | Small chip / counter pop        | 0.10                  |

## What NOT to Do

1. No dark canvas. This style is warm-paper only.
2. No more than one lead accent per scene. The whole point of editorial restraint is single-color discipline.
3. No Playfair Display, Times New Roman, or other web-default serifs. Source Serif 4 only.
4. No `<br>` in content text — use `max-width`.
5. No background music on Shorts.
6. No `position: absolute; top: Npx` on scene content containers — use padding.
7. No accent below 36px — reserve for hero, headline, badges, single italic emphasis words.
8. No real logos in the bare template — operators copy per video.
9. No `Math.random()` / `Date.now()` / network fetches at render time.
10. No phase-mutex `z-index` escalation in a single index.html. This style uses sub-compositions; if you stack `#phase1 / #phase2 / #phase3` z-indexes inside `index.html`, you've drifted to the anthropic pattern — switch back to scene wrappers.
