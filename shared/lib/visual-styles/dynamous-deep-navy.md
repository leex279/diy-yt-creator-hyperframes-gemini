# Dynamous Deep-Navy — Workshop Stage

**Mood:** Confident, premium, "Cole-grade" workshop teach | **Best for:** Dynamous-branded long-form workshops, AI-coding deep-dives, "scaling X" or "strategies for Y" episodes, channel-host long-form where the host is the brand.

A long-form deep-navy stage built around the **classic Dynamous brand
system** (deep navy + Dynamous Blue, NO purple). Weight contrast between
300-weight and 800-weight Montserrat is the signature move. Persistent
blue/cyan halo background, hairline grid, JetBrains Mono eyebrows.
Reads like a workshop deck recorded for YouTube, not a punchy news clip.

> **Distinct from `dynamous-modern.css`** — that token file is for the
> slate+purple+pink+cyan **Dynamous-promotion** artifacts (midroll,
> endcard, discount bubble). This visual style is for the **video
> compositions themselves** when filmed/authored under the Dynamous
> brand — the original "Dynamous Slides" aesthetic.

## Tokens

[`shared/lib/tokens/dynamous-deep-navy.css`](../tokens/dynamous-deep-navy.css)

Defines: `--bg`, `--bg-alt`, `--ink`, `--ink-2`, `--muted`, `--muted-2`,
`--accent` (Dynamous Blue), `--accent-2` (Dynamous Light), `--accent-3`
(Dynamous Cyan), `--accent-dim` (Deep Halo), `--accent-pale`,
`--font-display` (Montserrat), `--font-data` (JetBrains Mono),
`--pad-top`, `--pad-x`, `--pad-bottom`.

## Palette roles

| Role             | Token           | When to use                                                          |
| ---------------- | --------------- | -------------------------------------------------------------------- |
| Background       | `--bg`          | Canvas — near-black with blue tint (`#07090F`).                      |
| Body             | `--ink`         | Headlines, hero wordmarks, primary display type (98% white).         |
| Caption          | `--ink-2`       | Subline body copy (78% white).                                       |
| Secondary        | `--muted`       | Sublines under cards, eyebrow runs (58% white).                      |
| Primary accent   | `--accent`      | Dynamous Blue — hero focal element, gradient stat fill, pillar rule. |
| Light accent     | `--accent-2`    | Eyebrow kicker, eyebrow rule, marker sweep on light moments.         |
| CTA halo         | `--accent-3`    | Dynamous Cyan — bottom-corner halo, secondary glow.                  |
| Deep halo        | `--accent-dim`  | Background depth wash. Rarely used as type color.                    |
| Warn / subscribe | `--accent-warn` | Legacy alias — kept for cross-template compat. Used only on the closing subscribe pill border.|

**Brand rules** (carried from the original Dynamous deck):

- Dynamous Blue is the hero. Restrict to one or two focal elements per scene.
- **NO PURPLE.** For tertiary accents reach for Cyan (`#0EA5E9`) or the deep halo (`#1E40AF`), never purple.
- If everything glows, nothing does. Per-scene glows must be subtle so the persistent `#bg-halo` blue/cyan backdrop carries the brand atmosphere.

## Typography

| Role             | Family                                | Weight | Treatment                                             |
| ---------------- | ------------------------------------- | ------ | ----------------------------------------------------- |
| Hero wordmark    | Montserrat                            | 900    | `letter-spacing: -0.05em`, character stagger entrance |
| Hero stat number | Montserrat                            | 800    | Gradient text (accent-2 → accent), tabular-nums       |
| Tension / pivot  | Montserrat                            | 300 + 800 | Same line — light → bold weight contrast            |
| Section headline | Montserrat                            | 700-800 | `letter-spacing: -0.025em`, line-height 1.0-1.2     |
| Pillar title     | Montserrat                            | 700    | 72-82px, `letter-spacing: -0.02em`                    |
| Body / subline   | Montserrat                            | 300-400 | line-height 1.3-1.35                                 |
| Eyebrow (kicker) | JetBrains Mono                        | 500    | UPPERCASE, `letter-spacing: 0.32em`, with `::before` 56px bar |
| Stat suffix      | Montserrat                            | 800    | `--accent-2` solid (not gradient — pairs with the gradient number)|
| URL / data line  | JetBrains Mono                        | 500    | `letter-spacing: 0.04-0.05em`, accent-2 color         |

**Type scale at 1920x1080:** Hero wordmark 260px · Big stat 360px · Tension 152px · Section headline 118-138px · Pillar title 72px · CTA wordmark 144px · Quote body 72px · List label 38-46px · Body 38-44px · Eyebrow 22-26px.

## Motion Signature

| Easing            | Use for                                                   |
| ----------------- | --------------------------------------------------------- |
| `power3.out`      | Hero wordmark character stagger (each char rises 120px in 0.55s) |
| `back.out(1.6)`   | Flame mark scale-in, comment/subscribe pills              |
| `back.out(1.4)`   | List row slides, CTA pill row                             |
| `back.out(1.3)`   | Pillar card entrance                                      |
| `expo.out`        | Stat counter ramp, CTA debate question rise               |
| `power2.out`      | Eyebrows, sublines, marker sweeps                         |
| `sine.inOut`      | All mid-hold beats — flame yoyo, halo breath, scale pulses|
| `power1.in/out`   | Crossfade in/out (blur+scale)                             |

**Stagger:** 70ms between wordmark characters, 0.13s between pillars (paced 4s apart for narration sync), 0.55s+2.8s+5.6s for list reveals (~3s apart, narration-paced).

**Subtle scale pulse** (scale: 1 → 1.02-1.04, sine.inOut yoyo) is used on every scene's mid-hold to keep the visual surface alive per the visual-pacing-5s rule.

## Suggested Lib Picks

| Block / Component / Effect                                                | Use for                                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [`tokens/dynamous-deep-navy.css`](../tokens/dynamous-deep-navy.css)       | Always link first — palette + type scale source of truth          |
| Templates: [`templates/long-form/dynamous-slides/compositions/*`](../../../templates/long-form/dynamous-slides/compositions/) | Reuse scene archetypes directly when forking      |
| Registry: `vfx-text-cursor`                                                | Premium hero text reveal (operator opt-in for hero scene)         |
| Registry: `vfx-portal`                                                     | Hero transition between two key scenes (replaces a flash boundary)|
| Registry: `vfx-liquid-glass`                                               | Quote-card variant with refractive glass surface                  |
| Registry: shader transitions (`cinematic-zoom`, `cross-warp-morph`, `light-leak`) | Hero pivot boundaries — for projects that fold all scenes into one HTML |
| Local: `#bg-halo` + `#bg-halo-2`                                          | The signature persistent dual-halo backdrop                       |

## Surface detail formulas

- **Pillar cards:** 18px radius, `rgba(255,255,255,0.03)` fill, `1px solid rgba(255,255,255,0.10)` border. Bottom rule = 4px Dynamous Blue with 16px blue shadow, animates `scaleX: 0 → 1` AFTER the card slides in.
- **List rows:** 16px radius, same fill+border as pillars. Marker sweep on bottom edge: 3px accent-2 with 12px glow, animates `width: 0% → 100%` after row entrance.
- **Big stat:** Gradient text `linear-gradient(180deg, accent-2 0%, accent 100%)` via `-webkit-background-clip: text`, with `text-shadow: 0 0 80px rgba(59,130,246,0.35)` for depth.
- **Eyebrow kicker:** Mono uppercase, `::before` 56px×2px accent-2 bar, 0.32em letter-spacing.
- **CTA flame:** SVG path with `linearGradient(accent-2 → accent)`, `drop-shadow(0 0 50px rgba(59,130,246,0.7))`, yoyo translateY drift in mid-hold.

## Audio / SFX

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

This style is **long-form only** — BG music is supported here (NOT on
Shorts). Use the 3-segment bed: hook (≈ first 12s, `data-volume="0.12"`),
body (`data-volume="0.07"`), CTA (final 15s, `data-volume="0.12"`).

| Cue                | Use on                                       | Default `data-volume` |
| ------------------ | -------------------------------------------- | --------------------- |
| `cinematic-whoosh` | Every scene boundary (default)               | 0.11                  |
| `impact-slam`      | The hero pivot (big-stat → tension boundary) | 0.15                  |
| `scale-slam`       | Big stat reveal                              | 0.15                  |
| `spring-pop`       | First pillar entrance, first list row        | 0.11                  |
| `pop`              | Subsequent list rows                         | 0.10                  |

Sync files with `bash scripts/sync-video-sfx.sh videos/<slug>` using the
default cues from the template's `sfx-cues.txt`.

## What NOT to Do

1. **No purple anywhere.** Cyan or deep-halo instead — this is the single hardest brand rule.
2. **No light canvas.** Deep-navy `#07090F` only.
3. **No serif headlines** — Montserrat only.
4. **No more than ~2 flash transitions per video.** Default flagged boundaries are the hero pivot (big-stat → tension) and the CTA landing (quote-card → cta). More than two and they stop reading as special.
5. **No removing the flame mark** from the hook + CTA scenes — it's the Dynamous brand seal.
6. **No reducing the hook wordmark below 220px** — loses its scroll-stop power.
7. **No pulse-on-everything.** Vary mid-hold cadences so the eye notices the variations.
8. **No purple gradients** sneaking in via card backgrounds, halos, or hover states.
9. **No background music on Shorts** — this style is long-form only. Shorts use `templates/shorts/*` styles.
