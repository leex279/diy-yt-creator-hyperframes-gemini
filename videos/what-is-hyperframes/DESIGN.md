# DESIGN — Standard Shorts (Brand-Neutral Dark Navy)

Visual system for **YouTube Shorts** (1080x1920, 30fps, 24-180s) in a **brand-neutral, topic-agnostic** aesthetic. Dark navy stage with a 4-accent rotation (blue / cyan / purple / green) plus warn (orange) and stat (yellow). Mirrors the channel's `templates/long-form/standard/` palette so vertical and horizontal videos feel coherent.

This is the **canonical baseline for Shorts**. Use it for any topic that isn't anchored to a specific brand aesthetic. Brand-specific variants (`anthropic`, `archon`) extend the same phase-mutex architecture with their own palette.

## Style Prompt

A confident, brand-neutral dark navy stage built for vertical video. Warm-neutral white type sits on a near-black canvas with a hint of blue. A 4-tier rotating palette of bright accents (blue lead, cyan secondary, purple tertiary, green for success) drives chrome — borders, badges, glows, single accent words. Layout is phase-based: only one phase is visible at any frame, each phase has a 240px top safe-zone reserved for the persistent topic banner, and content is centered with generous breathing room. Motion is spring-driven and percussive — slam-in hero words with a tight inline shake, stat pills that pop, numbered step cards that scale-in with a colored gradient wash. Reads like a clean explainer, not an influencer reaction video — works for any topic from product launches to how-to walkthroughs to news explainers.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **24-180s** (YT Shorts hard max 180s)
- Background: solid `var(--bg)` `#0B0F1A`. No full-screen linear gradients (banding under H.264) — use radial highlights or solid + localized glow only.

## Colors

All colors flow from `tokens/standard-short.css` via CSS variables. Override per video by re-declaring any `--accent-N` inside `#root` (or a per-phase scope). The aliases `--primary`, `--secondary`, `--tertiary`, `--success` mirror anthropic-dark naming so lib entries authored against either system stay portable.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#0B0F1A` | Page canvas — near-black with a hint of blue |
| Card surface | `--bg-card` | `rgba(255,255,255,0.05)` | Default card panel |
| Surface bright | `--bg-surface` | `rgba(255,255,255,0.08)` | Slightly brighter card panel |
| Border | `--border` | `rgba(255,255,255,0.10)` | Default card stroke |
| Border bright | `--border-bright` | `rgba(255,255,255,0.18)` | Brighter card stroke |
| Primary text | `--text` | `#F1F3F4` | Headlines, body — warm-neutral white |
| Secondary text | `--text-dim` | `#9AA0A6` | Captions, meta, fineprint |
| Muted text | `--text-muted` | `#64748B` | Heavy de-emphasis only |
| Accent 1 / primary | `--accent-1` | `#3B82F6` | Blue — phase 1 lead, hero slam, primary CTA |
| Accent 2 / secondary | `--accent-2` | `#06B6D4` | Cyan — phase 2 overline, secondary stat |
| Accent 3 / tertiary | `--accent-3` | `#8B5CF6` | Purple — second feature, alternate phase accent |
| Accent 4 / success | `--accent-4` | `#22C55E` | Green — CTA, "go", positive close |
| Accent — warn | `--accent-warn` | `#F97316` | Orange — caution / non-default warning only |
| Accent — stat | `--accent-stat` | `#FBBC04` | Yellow — hero stat highlights only |
| Pill background | `--pill-bg` | `rgba(241,243,244,0.07)` | Default chip / pill fill |
| Pill border | `--pill-border` | `rgba(241,243,244,0.18)` | Default chip / pill stroke |

**Contrast verified (WCAG):**
- Primary text on background: ~16:1 (AAA)
- Secondary text on background: ~5.5:1 (AA normal)
- Accent 1 (blue) on background: ~5.4:1 (AA normal) — safe for 40px+ headings
- Accent 2 (cyan) on background: ~9:1 (AAA) — safe for body
- Accent 3 (purple) on background: ~4.6:1 (AA large only — use for chips/headings, not body)
- Accent 4 (green) on background: ~7.5:1 (AAA) — safe for body

**Accent rotation rule:** Within one video, no two adjacent phases share the same accent. Default rotation is **blue → cyan → purple → green** (phase 1 → 2 → 3 → 4). Swap to a different rotation per video by re-declaring `--accent-1..4` on `#root`.

## Typography

Pairing rationale: **Inter** is the workhorse — the entire dark-stage aesthetic relies on Inter's tight tracking and its 800/900 weights for the slam-in hero words. **JetBrains Mono** is the technical voice for overlines, dates, code references, URL pills. Two families, no exceptions.

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero stat / slam word | `var(--sans)` (Inter) | 900 | `letter-spacing: -4px`, `text-shadow: 0 0 80px <accent>88, 0 8px 24px rgba(0,0,0,0.6)` |
| Headline | `var(--sans)` (Inter) | 800-900 | `letter-spacing: -1px`, line-height 1.05 |
| Body large | `var(--sans)` (Inter) | 600 | line-height 1.3 |
| Body | `var(--sans)` (Inter) | 500 | line-height 1.4 |
| Section overline | `var(--mono)` (JetBrains Mono) | 700 | UPPERCASE, `letter-spacing: 5-7px`, accent color |
| Step number | `var(--mono)` (JetBrains Mono) | 900 | tabular-nums, near-black on accent fill |
| Caption / chip | `var(--mono)` (JetBrains Mono) | 600-700 | `letter-spacing: 1-2px`, `font-variant-numeric: tabular-nums` |
| URL / code | `var(--mono)` (JetBrains Mono) | 700 | `letter-spacing: 2px` |

**Type scale (Shorts-tuned):**

| Role | Size |
|---|---|
| Hero stat / slam word | 200px (drop to 180px if it overflows) |
| Hero pre-line ("Most people miss…") | 72px |
| Headline | 64px |
| Stat number | 180px |
| Step title | 40px |
| Step sub | 28px |
| Body | 36px |
| Section overline (mono) | 36px |
| Caption (mono) | 30-32px |

**Tabular numerals on stat numbers:** add `font-variant-numeric: tabular-nums lining-nums` so digits don't jitter across springs.

## Layout

**Safe zones — non-negotiable.** A persistent topic banner (or video-title banner) sits at `top: 60px` and is a rounded pill. Every phase container MUST reserve top space for it. A slim progress bar may sit at the bottom.

```
PHASE_PAD_TOP    = 240px   (clears the top banner + mobile UI overlay)
PHASE_PAD_X      = 60px    (default side padding)
PHASE_PAD_BOTTOM = 240px   (clears the progress bar + reading room)
```

`.phase-content` MUST use `width: 100%; height: 100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display: flex; flex-direction: column; box-sizing: border-box`. Padding positions content inward — NEVER `position: absolute; top: Npx`. Absolute-positioned content containers overflow on rendered text.

**Phase mutex:** Only one phase is visible at any frame. Use opacity + visibility crossfades on whole phases, not on individual elements. Each phase typically runs 4-12s.

## Motion Language

- **Easing:**
  - `back.out(1.7)` for slam-in hero words and stat pills (the signature spring)
  - `power3.out` for headlines and primary text rises
  - `power2.out` for body / chip / pill entrances
  - `expo.out` for high-impact one-element reveals (URL slam)
  - `sine.inOut` for ambient breathing only
  - `power1.in` / `power1.out` for outgoing/incoming phase blur
  - **Avoid** `elastic` and `bounce` — they read toy-like.
- **Duration:**
  - Hero / slam word: 0.6-0.9s
  - Headline: 0.5-0.7s
  - Body / chip: 0.35-0.5s
  - Phase crossfade: 0.4s opacity + 0.5s blur
- **Direction:** Vertical y-rises dominate (`y: +30 → 0`). Hero slams use `scale: 0.78 → 1.0`. Horizontal slides only for step cards (`x: -40 → 0`). No rotation. No scale-pop above 1.06.
- **Stagger:** 80-140ms on body lists; 40-60ms on chip rows; 200-280ms between step cards; 500ms between adjacent stat pills.
- **Inline shake** on the impact frame of a slam word (4 ticks, ±5px, 40ms each). One shake per phase max — overusing it cheapens it.

## Surface Detail

- **Cards:** 20-24px radius, `background: linear-gradient(135deg, <accent>26, <accent>0c)` with `border: 2px solid <accent>66`, `box-shadow: 0 10-14px 30-36px <accent>33`. Inner padding 22-32px.
- **Stat pill (huge number + label):** column flex, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>66`). Width 460px, min-height 300px.
- **Step number badge:** mono 900 weight, solid accent fill, near-black `color: var(--bg)` for contrast, 18px radius, 100x100px square.
- **URL / chip pill:** mono 700, accent gradient bg + accent border, max-width 920px, 22px vertical padding.
- **Subscribe pill:** rounded (`border-radius: 999px`), `--pill-bg`, `--pill-border`, accent-1 (blue) arrow.
- **Top banner:** rounded pill in `--pill-bg` / `--pill-border`, mono uppercase wordmark, accent-1 dot indicator. Operator can swap for a real logo `<img>` (see README).
- **Ambient:** dual radial drift in accent-1 + accent-3 at low alpha on the root, slow sine yoyo.
- **Shape backdrop:** 14 generic geometric shapes (circle, rounded square, triangle) scattered with seeded PRNG at 4% opacity — ambient depth without competing with phase content.

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Default cue set ships in [`sfx-cues.txt`](./sfx-cues.txt): `impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop`. Run `bash scripts/sync-video-sfx.sh videos/<slug>` after spawning to copy them into the video's `assets/sfx/`.

Narration is one stem per video (or one continuous stem with `data-media-start` offsets). SFX are layered as separate `<audio>` elements at low volume, keyed to spoken-word seconds.

| Cue | Use on | Default `data-volume` |
|---|---|---|
| `impact-slam` | Hero word reveal (phase 1 slam) | 0.15 |
| `scale-slam` | Stat-pill entrance (phase 2) | 0.15 |
| `cinematic-whoosh` | Phase / scene change | 0.11 |
| `spring-pop` | Step card entrance (phase 3) | 0.11 |
| `pop` | Small chip / list item | 0.10 |
| `glitch-zap` | Pivot / regression callout | 0.09 |
| `sonic-logo` | Composition start (optional) | 0.45 |

Hard cap: **never** exceed `0.25` on a single per-cue SFX (sonic-logo at `0.45` is the only documented exception). Stack 2-3 quiet ones rather than one loud one. **No background music on Shorts.**

## What NOT to Do

1. **No light canvas.** This is dark-stage. Don't tint the background toward gray paper.
2. **No more than one accent per phase.** Pick blue OR cyan OR purple OR green for that phase's chrome — don't paint a rainbow.
3. **No serif headlines.** Inter only.
4. **No flashing strobes / glitches longer than 6 frames.** This is publication-grade calm with percussive accents, not influencer chaos.
5. **No `<br>` in content text.** Use `max-width` so text wraps naturally — `<br>` causes overlap when fonts render slightly wider than estimated.
6. **No background music on Shorts.** Narration + SFX only.
7. **No `position: absolute; top: Npx` on `.phase-content`.** Content containers must use `padding` to position; absolute positioning overflows on dynamic text.
8. **No accent below 40px.** Blue/cyan/purple/green don't carry enough contrast for body — keep them on hero, headline, badges, borders, and single accent words only.
9. **No real logos in the bare template.** Operators copy a logo into `assets/` per video; the bare template ships with a styled wordmark pill so it lints render-clean without committing to any brand.
10. **No date-style chips.** This template uses **numbered** step cards (01/02/03) for topic-agnostic ordering. If you need dated cards (e.g. for a postmortem), use `templates/shorts/anthropic/` instead — that's exactly what its phase 3 is for.
