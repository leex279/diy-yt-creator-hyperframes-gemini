# Design — Dynamous-Slides Long-form Template

Brand reference for this template. Adapted from the **Dynamous brand
system** (deep navy + Dynamous Blue, Montserrat for display, JetBrains
Mono for data, weight-contrast 300/800) to the long-form HyperFrames
sub-composition architecture.

All values live as CSS custom properties on `:root` in `tokens/dynamous.css`.

---

## Palette

| Token           | Hex / Value             | Role                                                |
| --------------- | ----------------------- | --------------------------------------------------- |
| `--bg`          | `#07090F`               | Near-black with a blue tint — every scene background |
| `--bg-alt`      | `#080A13`               | Slightly warmer alternate                            |
| `--ink`         | `rgba(255,255,255,.98)` | Primary headlines + display type                     |
| `--ink-2`       | `rgba(255,255,255,.78)` | Body copy                                            |
| `--muted`       | `rgba(255,255,255,.58)` | Captions, secondary lines                            |
| `--muted-2`     | `rgba(255,255,255,.36)` | Pillar sublines, low-emphasis                        |
| `--accent`      | `#3B82F6`               | **Dynamous Blue** — hero color, primary focus        |
| `--accent-2`    | `#60A5FA`               | Highlights, eyebrows, accent underlines              |
| `--accent-3`    | `#0EA5E9`               | Dynamous Cyan — CTA glow + secondary halo            |
| `--accent-dim`  | `#1E40AF`               | Deep halo / hover state                              |
| `--accent-pale` | `#DBEAFE`               | Reserved for rare light-mode accents                 |
| `--accent-warn` | `#F97316`               | Used ONLY on the closing subscribe pill (legacy alias)|

**Brand rules** (carried from the Dynamous deck):

- Dynamous Blue is the hero. Restrict to one or two focal elements per scene.
- **NO PURPLE.** For tertiary accents reach for Cyan (`#0EA5E9`) or the deep halo (`#1E40AF`), never purple.
- The persistent `#bg-halo` (blue) + `#bg-halo-2` (cyan) backdrop layers do the brand atmosphere — keep per-scene glows subtle so they don't fight.

## Typography

| Font            | Variable          | Used for                                            |
| --------------- | ----------------- | --------------------------------------------------- |
| Montserrat      | `--font-display` | Every word the viewer reads. Weight 300/700/800/900.|
| JetBrains Mono  | `--font-data`    | Eyebrows, numbers, URLs, code-feeling type.         |

**Weight contrast is the signature.** A 300-weight `<span class="light">`
against an 800-weight headline, in the same headline, is the deck's most
recognizable move (used in `scene-headline-accent` and `scene-tension-pivot`).

Type scale at 1920x1080:

| Class / role        | Size   | Used in                                   |
| ------------------- | ------ | ----------------------------------------- |
| Hook wordmark       | 260px  | `scene-hook-wordmark`                     |
| Big stat number     | 360px  | `scene-big-stat`                          |
| Stat suffix         | 220px  | `scene-big-stat`                          |
| Tension headline    | 152px  | `scene-tension-pivot`                     |
| Section headline    | 138px  | `scene-headline-accent`                   |
| CTA wordmark        | 144px  | `scene-cta`                               |
| Quote body          | 72px   | `scene-quote-card`                        |
| Pillars headline    | 76px   | `scene-pillars-3`                         |
| Pillar title        | 82px   | `scene-pillars-3`                         |
| List headline       | 70px   | `scene-list-reveal`                       |
| Debate question     | 64px   | `scene-cta`                               |
| List row label      | 46px   | `scene-list-reveal`                       |
| Pillar sub          | 30px   | `scene-pillars-3`                         |
| Body / subline      | 38-44px| Most scenes                               |
| List row descriptor | 28-30px| `scene-list-reveal`                       |
| Eyebrow (kicker)    | 22-26px| Every scene (uppercase, JetBrains Mono)   |

Minimum for video readability: 60px+ headlines, 22px+ labels. Long-form
canvas allows tighter type than Shorts (no mobile UI overlay), so 28-30px
list descriptors are safe.

## Decorative layers (composited in this order)

Root index.html persists all of these behind every scene wrapper:

| Layer          | Z   | Purpose                                                                                  |
| -------------- | --- | ---------------------------------------------------------------------------------------- |
| `#ambient`     | 0   | Triple-source radial breath (blue + cyan + deep halo). 30s yoyo across composition.      |
| `#grid-bg`     | 0   | Hairline 96px grid, radial-masked. Anchors the stage visually without competing.         |
| `#shape-backdrop` | 0 | 12 deterministic shape SVGs scattered at 4% opacity. Drift subtly.                       |
| `#bg-halo`     | 0   | Large Dynamous-Blue radial halo top-right. 12s yoyo.                                     |
| `#bg-halo-2`   | 0   | Cyan halo bottom-left. 14s yoyo.                                                         |
| `#vignette`    | 7   | Cinematic edge-darkening on every scene.                                                 |
| `#flash-overlay` | 6 | Blue radial burst overlay — GSAP-driven only on flagged transition boundaries.           |
| Scenes         | 1   | Sub-composition wrappers. Each scene paints on track 1.                                  |
| `#noise-overlay` | 8 | SVG `feTurbulence` film-grain at 6% opacity. Mix-blend overlay.                          |
| `#captions-wrap` | 9 | Captions populated by `npx hyperframes transcribe`.                                      |
| `#top-banner`  | 10  | Dynamous wordmark, persistent.                                                           |
| `#progress-track` | 10 | Slim Dynamous-Blue progress bar.                                                       |

**Important:** never use SVG-filter `data:image/svg+xml` grain — it taints
the WebGL snapshot in Safari and breaks any future shader transition the
operator might wire in.

## Scene catalog

| #  | File                              | Default window | Archetype                                        |
| -- | --------------------------------- | -------------- | ------------------------------------------------ |
| 1  | `scene-hook-wordmark.html`        | 0 - 10s        | Character-stagger wordmark hero + flame mark.    |
| 2  | `scene-headline-accent.html`      | 10 - 25s       | Two-line headline with Dynamous-Blue sweep.      |
| 3  | `scene-big-stat.html`             | 25 - 40s       | Counter ramp with gradient text + receipt.       |
| 4  | `scene-tension-pivot.html`        | 40 - 55s       | 300/800 weight-contrast headline. Flash on entry.|
| 5  | `scene-pillars-3.html`            | 55 - 75s       | Three-pillar grid, step-by-step reveal.          |
| 6  | `scene-list-reveal.html`          | 75 - 95s       | 6-row enumerated list, marker-sweep per row.     |
| 7  | `scene-quote-card.html`           | 95 - 110s      | Line-by-line quote reveal + author chip.         |
| 8  | `scene-cta.html`                  | 110 - 120s     | Logo lockup + debate question + pill row.        |

All durations are operator-tunable per video. The root `index.html`
defines the scene `data-start` values; the sub-composition's internal
timeline owns its length.

## Transition flavors

The root `crossfadeScenes()` function takes an extra `flash` flag:

- `flash: false` — standard 1.1s blur+scale crossfade.
- `flash: true` — same crossfade PLUS a brief Dynamous-Blue radial flash overlay across the midpoint. Use sparingly for the **hero pivot** boundary and the **CTA landing** boundary only.

Default flagged boundaries in this template:
- big-stat → tension-pivot (hero pivot — first emotional turn)
- quote-card → cta (CTA landing — settles instead of punches)

## Voice (carry into copy)

When swapping copy, keep the Dynamous tone in mind:

- **"Honestly"** and **"super"** show up. Use them.
- Direct address — say "you" often.
- Tell viewers what NOT to focus on. Removes overwhelm.
- Numbers, not vague claims. "40,000 lines" beats "a lot of code."
- One conviction per scene, max.

## Audio (operator wires per video)

Audio bed comments in `index.html` show the canonical 3-segment bg-music
pattern (hook / body / cta) keyed by section mood. Volume caps per
[`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md):

- Narration: `data-volume="1"`
- BG music hook: `data-volume="0.12"`
- BG music body: `data-volume="0.07"`
- BG music CTA: `data-volume="0.12"`

SFX cues use track 4+ (track 2 = narration, track 3 = bg-music). Sync
files via `bash scripts/sync-video-sfx.sh videos/<slug>` with the
default cues from `sfx-cues.txt`.

## What NOT to do

- Don't add purple anywhere. Cyan or deep-halo instead.
- Don't strip the flame mark from the hook + CTA — it's the Dynamous brand seal.
- Don't reduce the wordmark below 220px on the hook scene — it loses its scroll-stop power.
- Don't pulse every scene's accent at the same cadence. Vary the rhythm so the eye notices the variations.
- Don't enable a flash transition on every boundary — it loses its punch. Two per video, max.
