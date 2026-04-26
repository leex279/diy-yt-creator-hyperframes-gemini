# DESIGN — Anthropic Cinematic Warm

Style for the "Claude Connectors for Everyday Life" 60s Short. Light canvas. Cinematic + warm. Anthropic-aligned.

## Style Prompt

A premium-publication aesthetic in the Anthropic visual language: warm cream paper, near-black serif headlines, a single clay-orange accent for emphasis. Movement is unhurried and confident — long ease-out entrances, generous whitespace, no flash. Cinematic warmth via subtle radial highlights and soft drop shadows on cards. Reads like a Sunday-supplement feature, not a tech demo.

## Colors

| Role | Hex | Usage |
|---|---|---|
| Canvas | `#F5F1EB` | Page background — warm cream, the dominant surface |
| Ink | `#181816` | Headlines and body text — near-black with a touch of warmth |
| Ink subdued | `#5A554F` | Secondary text, captions, labels (4.7:1 on canvas) |
| Clay | `#CC785C` | Single accent — emphasis words, the active connector chip, button strokes |
| Clay deep | `#A85843` | Hover/active state for clay; rare use, only for hero pop moments |
| Paper warm | `#EAE3D8` | Card surfaces, secondary panels — one notch darker than canvas for depth |

Contrast verified:
- Ink on canvas: 14.6:1 (AAA)
- Ink subdued on canvas: 4.7:1 (AA normal text)
- Clay on canvas: 3.9:1 (AA large text only — never use clay for body)

## Typography

Pairing rationale: Fraunces is the expressive voice (serif, Tiempos analog — performs the headlines and stats). Hanken Grotesk is the recessive voice (modern geometric sans — handles body and UI, gets out of the way). Mono used only for literal commands.

**Banned per skill rules:** Inter, Roboto, Open Sans, Lato, Source Sans, Poppins, Outfit, Playfair, Cormorant, EB Garamond.

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero headline | `Fraunces, Georgia, serif` | 600 (semibold) | Tight line-height 0.95, `letter-spacing: -0.03em`, `font-variant-numeric: oldstyle-nums lining-nums` |
| Section heading | `Fraunces, Georgia, serif` | 600 | Same family as hero |
| Body / UI | `'Hanken Grotesk', system-ui, sans-serif` | 400 / 700 | 44px+ for Shorts. Labels uppercase + 0.12em tracking, weight 700 |
| Numbers / stats | `Fraunces, Georgia, serif` | 700 | `font-variant-numeric: tabular-nums`, tight kerning |
| Mono (literal commands only) | `'JetBrains Mono', ui-monospace, monospace` | 400 | Sparing — only for quoted code/paths |

Weight contrast across the composition: 400 Hanken body vs 600 Fraunces heading vs 700 Fraunces numbers. The serif's optical character carries hierarchy; weight stays restrained per cinematic-warm register.

Sizes (Shorts 1080×1920):
- Hero stat: 220–280px
- Hero headline: 130–160px
- Section heading: 80–96px
- Body: 44–52px
- Labels: 36–40px (uppercase, tracked)
- Caption (sub-text): 40px

## Motion Language

- **Easing:** `power3.out` for primary entrances, `expo.out` for slam/punctuation moments, `sine.inOut` for ambient breathing/decoration. Avoid `back` or `elastic` — they feel toy-like for this brand.
- **Duration:** 0.7–1.1s for hero text; 0.4–0.6s for support text; 0.3s for chip/UI elements. Slow and confident, not snappy.
- **Direction:** Vertical y-translates dominate (text rises into place from +40 to 0). Horizontal slides only for chip rows. No rotation. No scale-pop above 1.05.
- **Stagger:** 80–140ms on body lists; 40–60ms on chip rows.
- **Transitions between scenes:** soft 0.5s crossfade with a 60px upward translate on the incoming scene. No wipes, no glitches.

## Surface Detail

- **Cards:** 24px radius, `background: #EAE3D8`, `box-shadow: 0 8px 32px rgba(24,24,22,0.06), 0 1px 2px rgba(24,24,22,0.04)`. Inner padding 56–72px.
- **Connector chips:** pill shape, 28px tall padding, 56px horizontal padding, `background: #FFF8F0` with `border: 1.5px solid rgba(24,24,22,0.08)`. Active chip gets a `border: 2px solid #CC785C` and lifts 4px (`y: -4`).
- **Ambient:** one slow-drifting radial gradient in warm tone (`radial-gradient(circle at 30% 20%, rgba(204,120,92,0.08), transparent 60%)`) on the root, animated by 6° hue rotation over the full duration. No noise overlay.

## What NOT to Do

1. **No dark mode.** This composition is light-canvas only. Don't tint the cream toward pure white.
2. **No multiple accent colors.** Clay is the only chromatic accent; everything else is in the ink/cream/warm-paper grayscale family.
3. **No flash effects, glitches, or screen shakes.** This is publication-grade calm, not tech-influencer chaos.
4. **No sans-serif for headlines.** Hero text is always Fraunces (serif). Sans is for body/UI only.
5. **No fast/snappy entrances.** Anything under 0.4s for primary content reads as panicked.
6. **No gradient text on body copy.** Solid ink only. Gradients are reserved for decorative ambient layer.
