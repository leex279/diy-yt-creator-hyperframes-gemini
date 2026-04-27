# Anthropic Dark — Postmortem Stage

**Mood:** Confident, premium engineering | **Best for:** Anthropic / Claude product launches, postmortems, dev-tool reveals, technical deep-dives.

A dark stage built for vertical Shorts. Warm off-white type on near-black canvas. A small rotating palette of bright accents (Claude orange, soft purple, soft blue, soft green; red reserved for warnings only) drives chrome — borders, badges, glows, single accent words. Spring-driven motion with a percussive slam beat. Reads like a premium engineering postmortem, not an influencer reaction video.

## Tokens

[`shared/lib/tokens/anthropic-dark.css`](../tokens/anthropic-dark.css)

Defines: `--bg`, `--card`, `--text`, `--text-dim`, `--orange`, `--purple`, `--blue`, `--green`, `--red`, `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--mono`, `--sans`.

## Palette roles

| Role         | Token        | When to use                                                          |
| ------------ | ------------ | -------------------------------------------------------------------- |
| Background   | `--bg`       | Canvas + date-chip text color (near-black `#0B0F18`).                |
| Card surface | `--card`     | Dense secondary panels.                                              |
| Body         | `--text`     | Headlines, body — warm off-white.                                    |
| Caption      | `--text-dim` | Secondary lines, metadata (4.7:1 contrast).                          |
| Primary      | `--orange`   | Claude primary — hero stats, CTA arrow, lead phase accent.           |
| Secondary    | `--purple`   | Second feature, alternate phase accent.                              |
| Technical    | `--blue`     | Docs, API, technical references.                                     |
| Positive     | `--green`    | Launches, fixes, "go" CTAs.                                          |
| Warning      | `--red`      | Regression, "−3% on evals" only — never decorative.                  |

**Accent rotation rule:** within one video, no two adjacent phases share the same accent. Orange leads; purple/blue/green rotate through the middle.

## Typography

| Role            | Family                                | Weight | Treatment                                             |
| --------------- | ------------------------------------- | ------ | ----------------------------------------------------- |
| Hero / slam     | `--sans` (Inter)                      | 900    | `letter-spacing: -4px`, glow + drop-shadow            |
| Headline        | `--sans` (Inter)                      | 800-900 | `letter-spacing: -1px`, line-height 1.05            |
| Body            | `--sans` (Inter)                      | 500-600 | line-height 1.3-1.4                                  |
| Section overline | `--mono` (JetBrains Mono)            | 700    | UPPERCASE, `letter-spacing: 5-7px`, accent color     |
| Date chip       | `--mono` (JetBrains Mono)             | 700-900 | `letter-spacing: 1-2px`, tabular-nums                |
| Stat number     | `--sans` (Inter)                      | 900    | tabular-nums, `letter-spacing: -4px`                 |
| URL / code      | `--mono` (JetBrains Mono)             | 600-700 | `letter-spacing: 2px`                                |

**Type scale (Shorts-tuned):** Hero stat 240px · Headline 64px · Body 36px · Overline 36px · Caption 30px.

## Motion Signature

| Easing           | Use for                                                   |
| ---------------- | --------------------------------------------------------- |
| `back.out(1.7)`  | Hero / slam-word entrances (the signature spring)         |
| `back.out(1.6)`  | Stat pill pop                                             |
| `back.out(1.5)`  | Timeline cards (slide-in with overshoot)                  |
| `power3.out`     | Headlines and primary text rises                          |
| `power2.out`     | Body / chip / pill text entrances                         |
| `expo.out`       | High-impact one-element reveals (URL slam)                |
| `power1.in`      | Outgoing scene blur+fade                                  |
| `sine.inOut`     | Ambient breath only                                       |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Stagger:** 80-140ms on body lists; 40-60ms on chip rows; 200-280ms between timeline cards; 500ms between adjacent stat pills.

**Inline shake** on the impact frame of a slam word (4 ticks, ±5px, 40ms each). One shake per phase maximum.

## Suggested Lib Picks

| Block / Component / Effect                                                | Use for                                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [`tokens/anthropic-dark.css`](../tokens/anthropic-dark.css)               | Always link first — every other entry depends on these tokens     |
| [`blocks/stat-pill-row`](../blocks/stat-pill-row/)                        | "X bugs / Y weeks" receipts, before/after metrics                 |
| [`blocks/timeline-cards`](../blocks/timeline-cards/)                      | Dated event sequence (3 cards)                                    |
| [`blocks/url-cta`](../blocks/url-cta/)                                    | Closing CTA with real URL + Subscribe pill                        |
| [`components/ambient-radial`](../components/ambient-radial/)              | Background depth — orange + purple breath                         |
| [`components/progress-bar`](../components/progress-bar/)                  | Bottom-edge time progress                                          |
| [`components/top-banner-wordmark`](../components/top-banner-wordmark/)    | Persistent brand wordmark (copy logo from `shared/logos/`)        |
| [`effects/phase-crossfade.js`](../effects/phase-crossfade.js)             | Scene-to-scene transitions (blur + opacity, 1.1s span)            |
| [`effects/hero-slam-shake.js`](../effects/hero-slam-shake.js)             | Impact-frame shake on the phase 1 slam word                       |
| [`effects/stat-pill-pop.js`](../effects/stat-pill-pop.js)                 | Stat pill scale-pop entrance                                      |

## Surface detail formulas

- **Cards:** 20-26px radius, `linear-gradient(135deg, <accent>26, <accent>0c)`, `border: 2px solid <accent>66`, `box-shadow: 0 14px 36px <accent>33`.
- **Stat pill:** column flex, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>66`).
- **Date chip:** mono 700-900, solid accent fill, `color: var(--bg)` for AAA contrast.
- **URL pill:** mono 700, green gradient + green border, max-width 920px.
- **Subscribe pill:** rounded (`border-radius: 999px`), `--pill-bg`, `--pill-border`, orange arrow.

## Audio / SFX

Narration is one stem per scene (or one continuous stem with `data-media-start` offsets). SFX layer as separate `<audio>` elements at low volume. Hard cap **0.25** per single SFX (excluding sonic-logo at 0.50).

| Cue                | Use on                          | Volume      |
| ------------------ | ------------------------------- | ----------- |
| `impact-slam`      | Hero word reveal                | 0.18-0.20   |
| `scale-slam`       | Stat-pill entrance              | 0.18-0.20   |
| `screen-shake`     | Hero word inline shake          | 0.13-0.15   |
| `cinematic-whoosh` | Phase / scene change            | 0.15        |
| `spring-pop`       | Card or chip entrance           | 0.13-0.15   |
| `pop`              | Small chip / list item          | 0.12-0.13   |
| `glitch-zap`       | "BUT…" pivot, regression callout | 0.12       |
| `sonic-logo`       | Frame 0 only                    | 0.50        |

**No background music on Shorts.** Narration + SFX only.

## What NOT to Do

1. No light canvas. This style is dark-stage only.
2. No more than one accent per phase — pick orange OR purple OR blue OR green for that phase's chrome.
3. No serif headlines — Inter only.
4. No flashing strobes / glitches longer than 6 frames.
5. No `<br>` in content text — use `max-width` for natural wrapping.
6. No background music on Shorts — narration + SFX only.
7. No `position: absolute; top: Npx` on `.phase-content` — use padding for content positioning.
8. No accent below 40px — orange/purple/blue/green don't carry contrast for body. Reserve them for hero, headline, badges, borders, single accent words.
