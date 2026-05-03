# Google Cinematic — Brand-Stage Vertical

**Mood:** cinematic dark with four-color brand glow | **Best for:** Google AI / Gemini / Workspace / Cloud / Android / Chrome shorts, dev-tool launches that fit the Google brand, anything that wants the canonical four-color rotation on a vertical canvas.

A cinematic dark stage tuned for Google content on a vertical canvas. Off-white type sits on a `#06080F` deep-navy that's washed by four soft-corner brand glows (blue at top-left, red at top-right, green at bottom-center, yellow at bottom-right). The Google wordmark anchors the top of every phase; a small mono `@handle` floats top-right with the active accent color tinting the `@`. A 5-dot progress rail (one Google color each, rotating blue → red → yellow → green → blue) marches across the bottom — one dot lights up per phase, glow tinted to its color. The accent triad is the four canonical Google brand hues; the chosen primary `--accent` colors the eyebrow, the progress-bar fill, the `@` symbol, and the CTA pill stroke. Particles drift; the top-left has a 4px green→yellow ramp; an inner safe-area frame keeps content off the canvas edges. Phase 4 optionally inverts to a soft white "shift" surface for the closing thought.

## Tokens

[`shared/lib/tokens/google-cinematic.css`](../tokens/google-cinematic.css)

Defines: `--g-blue`, `--g-red`, `--g-yellow`, `--g-green` (canonical Google brand triad), `--bg-deep`, `--bg-mid`, `--bg-soft`, `--bg`, `--card`, `--card-bright`, `--border`, `--border-bright`, `--bg-light`, `--bg-light-mid`, `--ink-on-light`, `--text`, `--ink-100/80/60/40/20`, `--text-secondary`, `--text-muted`, `--accent`, `--accent-glow`, `--orange`, `--purple`, `--blue`, `--green`, `--red`, `--yellow`, `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--sans` (Plus Jakarta Sans), `--mono` (JetBrains Mono).

The legacy `--orange / --purple / --blue / --green / --red / --yellow` aliases map onto the closest Google hue so blocks/components pulled from the lib (which reference the legacy names) render correctly without rewrite. `--orange` is the only legacy alias that doesn't have a Google equivalent — it falls back to a warm `#FF8F1F` for terminal string-literal coloring only.

## Palette roles

| Role | Token | When to use |
|---|---|---|
| Background | `--bg-deep` / `--bg` | Canvas `#06080F`. The cinematic theme washes it with four soft corner glows. |
| Card surface | `--card` | Chip / quote / panel bodies (translucent dark over canvas). |
| Body | `--text` / `--ink-100` | Headlines, body — pure white. |
| Caption | `--text-secondary` / `--ink-60` | Subhead, label, secondary copy `#A7B0C5`. |
| Muted | `--ink-40` | Inactive rail labels, prompt symbols, handle base. |
| Primary | `--g-blue` | Default `--accent`; rail dot 1 (SETUP), rail dot 5 (PUBLISH), CTA pill stroke when accent=blue. |
| Alert | `--g-red` | Rail dot 2 (CREATE), chip 4 (AGENT), terminal warning, before-side label in compare row. |
| Warn / hero | `--g-yellow` | Rail dot 3 (EVAL), chip 2 (REFERENCES), terminal flag color, top-line ramp end. |
| Success | `--g-green` | Rail dot 4 (DEPLOY), chip 3 (TARGETS), terminal `cmd` color, top-line ramp start, after-side label in compare row. |
| Light surface | `--bg-light` | Phase 4 "shift" theme (`theme-light` class on `#phase4`). |

**Accent rotation rule:** the chip grid and progress rail rotate through all four Google colors in `blue → red → yellow → green → blue` order, deterministic. Don't introduce a fifth color — the brand reads cleanly only when the four-color rotation is consistent. Within one video, the chosen `--accent` colors persistent chrome (eyebrow, CTA pill border, progress-bar fill, `@` symbol); the four chip / rail colors rotate independently of the chosen `--accent`.

## Typography

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero headline (xl) | `--sans` (Plus Jakarta Sans) | 800 | `letter-spacing: -2px`, line-height 0.98, `text-wrap: balance` |
| Headline (m / s) | `--sans` (Plus Jakarta Sans) | 800 | `letter-spacing: -2px`, line-height 0.98 |
| Body / subhead | `--sans` (Plus Jakarta Sans) | 600 | line-height 1.25, secondary ink |
| Section eyebrow | `--mono` (JetBrains Mono) | 600 | UPPERCASE, `letter-spacing: 6.5px`, accent color |
| Big-stat number | `--sans` (Plus Jakarta Sans) | 800 | 360px, gradient blue→green→yellow with drop-shadow, `tabular-nums` |
| Chip value | `--sans` (Plus Jakarta Sans) | 700 | 50px, primary ink |
| Chip label | `--mono` (JetBrains Mono) | 600 | 26px UPPERCASE, `letter-spacing: 3px`, chip-color |
| Terminal | `--mono` (JetBrains Mono) | 400-500 | 38px, four-color syntax (cmd green / arg ink / flag yellow / kw blue / str peach / prompt ink-40) |
| Quote | `--sans` (Plus Jakarta Sans) | 700 | 64px, line-height 1.15, 4px accent left border |
| CTA pill | `--mono` (JetBrains Mono) | 600 | 36-40px UPPERCASE, `letter-spacing: 5px`, accent-glow box-shadow |
| Rail-dot label | `--mono` (JetBrains Mono) | 600 | 24px UPPERCASE, `letter-spacing: 4px`, ink-40 inactive / dot-color active |
| Footer handle | `--mono` (JetBrains Mono) | 600 | 28px UPPERCASE, `letter-spacing: 4px`, ink-40 with accent-tinted `@` |

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
| Top-line entrance | `power3.out` (`scaleX: 0` from origin 0) | 0.7s |

Stagger 200-300ms between adjacent chips, 600ms between adjacent terminal blocks, 100-300ms between eyebrow → headline → body within a phase. **Never `repeat: -1`.**

## Suggested lib picks

- **Tokens:** [`tokens/google-cinematic.css`](../tokens/google-cinematic.css) (this file's pair)
- **Effects:** [`effects/phase-crossfade.js`](../effects/phase-crossfade.js) (blur+opacity transition between phases) and [`effects/hero-slam-shake.js`](../effects/hero-slam-shake.js) (4-tick inline shake for hero impact frames)
- **Components:** [`components/ambient-radial/`](../components/ambient-radial/) for an extra ambient breath layer if the cinematic corner glows aren't enough — but the stock four-corner gradient in `tokens/google-cinematic.css` already covers most cases
- **Blocks:** [`blocks/dynamous-module-interstitial/`](../blocks/dynamous-module-interstitial/) and [`blocks/dynamous-endcard/`](../blocks/dynamous-endcard/) when running with Dynamous promotion (the `templates/shorts/google/` template ships with both wired by default via `video.config.js`)

## Anti-patterns

- **Don't add a 5th accent color.** The four Google hues are the brand. Adding cyan / pink / orange breaks the visual identity.
- **Don't use orange as a primary accent.** It's not a Google brand color. Map "warn" needs onto red (`--g-red`) and "hero stat" needs onto yellow (`--g-yellow`).
- **Don't overlap the Google logo with the `@handle` or rail labels.** The logo is centered at `top: 80px`, the handle is at `top: 56px; right: 64px`, the rail dots are at `bottom: 110px`. Phase content lives between `--pad-top: 240px` and `--pad-bottom: 240px`.
- **Don't break the four-color rail rotation.** Order is fixed `blue → red → yellow → green → blue`. Reordering or recoloring confuses the brand.
- **Don't disable the inner `#slide-frame` and the top-left `#top-line` together.** Each adds visual structure; removing both leaves the canvas feeling unframed and the cinematic glows look diffuse.
- **Don't skip the deterministic seed prefix when re-spawning particles per video.** The `xmur3` hash uses `'google-short'` as the seed by default — change it per video so particles don't collide if multiple Google shorts render side-by-side in a contact sheet.
