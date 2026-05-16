# OpenAI Mono — Editorial Stage + Mint

**Mood:** Quiet, premium, restrained | **Best for:** OpenAI / ChatGPT / GPT / Sora / DALL·E / Codex product launches, research releases, system-card-style explainers, anything that wants the OpenAI brand's calm editorial register.

A monochrome editorial stage tuned for OpenAI content on a vertical canvas. Off-white type (`#ECECEC`) sits on an off-black `#0A0A0A` canvas — no corner glows by default, no four-color rotation, no cinematic flourishes. A single mint accent (`#10A37F` — the canonical ChatGPT hue) threads through the eyebrow, the active rail dot, the progress-bar fill, the `@` symbol, and the CTA pill stroke. The ChatGPT spirograph anchors the top (swap to the OpenAI wordmark for cross-sub-brand videos); a small mono `@handle` floats top-right with the mint `@`. A 5-dot progress rail (INTRO → BUILD → SIGNAL → SHIFT → CTA) marches across the bottom — one dot lights mint per phase. A sparse monochrome particle field (40 dots in three off-white tints) drifts behind the content. An inner safe-area frame keeps content off the canvas edges. Phase 4 optionally inverts to a warm off-white "shift" surface for the closing thought.

## Tokens

[`shared/lib/tokens/openai-mono.css`](../tokens/openai-mono.css)

Defines: `--oai-mint`, `--oai-mint-hi`, `--oai-mint-lo`, `--oai-lavender`, `--oai-amber`, `--oai-coral` (OpenAI brand triad), `--bg-deep`, `--bg-mid`, `--bg-soft`, `--bg`, `--card`, `--card-bright`, `--border`, `--border-bright`, `--bg-light`, `--bg-light-mid`, `--ink-on-light`, `--text`, `--ink-100/80/60/40/20`, `--text-secondary`, `--text-muted`, `--accent`, `--accent-glow`, `--orange`, `--purple`, `--blue`, `--green`, `--red`, `--yellow`, `--g-blue/red/yellow/green` (legacy aliases mapped to mint/auxiliary), `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--sans` (Inter), `--mono` (JetBrains Mono).

The legacy `--orange / --purple / --blue / --green / --red / --yellow` and `--g-blue / --g-red / --g-yellow / --g-green` aliases all map onto the closest OpenAI hue (most resolve to mint; the few that warrant a distinct hue resolve to amber/lavender/coral) so blocks/components pulled from the lib render correctly without rewrite. There is **no four-color rotation** in this style — every alias points at mint or an auxiliary tint.

## Palette roles

| Role | Token | When to use |
|---|---|---|
| Background | `--bg-deep` / `--bg` | Canvas `#0A0A0A`. Default theme is flat off-black, no glows. |
| Card surface | `--card` | Chip / quote / panel bodies (translucent dark over canvas). |
| Body | `--text` / `--ink-100` | Headlines, body — off-white `#ECECEC` (never pure white on OLED). |
| Caption | `--text-secondary` / `--ink-60` | Subhead, label, secondary copy `#A0A0A0`. |
| Muted | `--ink-40` | Inactive rail labels, prompt symbols, handle base `#7A7A7A`. |
| Primary | `--oai-mint` / `--accent` | Default — eyebrow, active rail dot, CTA pill stroke, `@` symbol, progress-bar fill, terminal `cmd`. |
| Auxiliary (Sora) | `--oai-lavender` | Whole-video override for Sora-flavored releases. Never per-element rotation. |
| Auxiliary (DALL·E) | `--oai-amber` | Whole-video override for DALL·E / image-gen releases. Also terminal flag color. |
| Auxiliary (warning) | `--oai-coral` | Regression / deprecation callouts. Rare. |
| Light surface | `--bg-light` | Phase 4 "shift" theme (`theme-light` class on `#phase4`) — warm off-white `#F4F4F2`. |

**Single-accent rule:** within one video, the eyebrow, chip grid, progress rail, terminal `cmd`, and CTA pill all share the same `--accent` (mint by default). Don't introduce a fifth color, and don't rotate accents across chips inside one phase — the brand reads cleanly only when the surface stays quiet. Auxiliary tints exist for **whole-video** override (e.g. a Sora launch Short swaps `--accent` to lavender for the whole composition), never for per-element rotation within one video.

## Typography

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero headline (xl) | `--sans` (Inter) | 800 | `letter-spacing: -2px`, line-height 0.98, `text-wrap: balance` |
| Headline (m / s) | `--sans` (Inter) | 800 | `letter-spacing: -2px`, line-height 0.98 |
| Body / subhead | `--sans` (Inter) | 500 | line-height 1.25, secondary ink |
| Section eyebrow | `--mono` (JetBrains Mono) | 600 | UPPERCASE, `letter-spacing: 6.5px`, mint accent |
| Big-stat number | `--sans` (Inter) | 800 | 360px, gradient mint → bright-mint with drop-shadow, `tabular-nums` |
| Chip value | `--sans` (Inter) | 700 | 50px, primary ink |
| Chip label | `--mono` (JetBrains Mono) | 600 | 26px UPPERCASE, `letter-spacing: 3px`, chip-color (default mint) |
| Terminal | `--mono` (JetBrains Mono) | 400-500 | 38px, monochrome syntax (cmd mint / arg ink / flag amber / kw lavender / str ink-80 / prompt ink-40) |
| Quote | `--sans` (Inter) | 700 | 64px, line-height 1.15, 4px mint left border |
| CTA pill | `--mono` (JetBrains Mono) | 600 | 36-40px UPPERCASE, `letter-spacing: 5px`, mint-glow box-shadow |
| Rail-dot label | `--mono` (JetBrains Mono) | 600 | 24px UPPERCASE, `letter-spacing: 4px`, ink-40 inactive / mint active |
| Footer handle | `--mono` (JetBrains Mono) | 600 | 28px UPPERCASE, `letter-spacing: 4px`, ink-40 with mint `@` |

## Motion signature

| Pattern | Easing | Duration |
|---|---|---|
| Headline rise | `power3.out` | 0.6s |
| Body / eyebrow rise | `power2.out` | 0.5s |
| Chip pop | `back.out(1.5)` | 0.5s |
| Terminal pop | `back.out(1.4)` | 0.6s |
| Phase crossfade out | `power1.in` (blur+scale up to 1.04) | 0.4-0.5s |
| Phase crossfade in | `power1.inOut` opacity → `power1.out` deblur+scale-to-1 | 0.3-0.5s |
| Particle drift | `sine.inOut`, yoyo true, repeat 1, dur 12s | full composition |
| CTA pulse | `sine.inOut`, yoyo true, repeat 4 | 0.7s/half |

Stagger 200ms between adjacent chips, 600ms between adjacent terminal blocks, 100-300ms between eyebrow → headline → body within a phase. **Never `repeat: -1`.**

## Suggested lib picks

- **Tokens:** [`tokens/openai-mono.css`](../tokens/openai-mono.css) (this file's pair)
- **Effects:** [`effects/phase-crossfade.js`](../effects/phase-crossfade.js) (blur+opacity transition between phases) and [`effects/hero-slam-shake.js`](../effects/hero-slam-shake.js) (4-tick inline shake for hero impact frames — use sparingly; the editorial register prefers a smooth rise over a shake)
- **Components:** the stock theme-quiet background covers most cases; opt into the `theme-cinematic` mint glow only for hero/launch moments where the quiet surface needs warmth
- **Blocks:** [`blocks/dynamous-module-interstitial/`](../blocks/dynamous-module-interstitial/) and [`blocks/dynamous-endcard/`](../blocks/dynamous-endcard/) when running with Dynamous promotion (the `templates/shorts/openai/` template ships with both wired by default via `video.config.js`)

## Anti-patterns

- **Don't add a 5th accent color.** Mint is the brand. Lavender / amber / coral are reserved for whole-video override. Adding cyan / pink / neon-green breaks the OpenAI editorial register.
- **Don't rotate accents across chips inside one phase.** The chip grid is single-accent by design — every chip mint, or every chip lavender if the whole video is Sora-flavored. Per-chip color rotation is the Google pattern, not OpenAI.
- **Don't overlap the brand mark with the `@handle` or rail labels.** The brand mark is centered at `top: 80px`, the handle is at `top: 56px; right: 64px`, the rail dots are at `bottom: 110px`. Phase content lives between `--pad-top: 240px` and `--pad-bottom: 240px`.
- **Don't use pure `#000000` for the background or pure `#FFFFFF` for body text.** The off-black `#0A0A0A` + off-white `#ECECEC` pairing reads softer and more premium on OLED — pure black/white feels harsh and "stock template".
- **Don't import the Google template's four-color terminal rim.** The `with-rim` class in this template uses a single mint hairline, not a four-color gradient. Anything four-color reads as "Google" not "OpenAI" to a brand-savvy viewer.
- **Don't skip the deterministic seed prefix when re-spawning particles per video.** The `xmur3` hash uses `'openai-short'` as the seed by default — change it per video so particles don't collide if multiple OpenAI shorts render side-by-side in a contact sheet.
