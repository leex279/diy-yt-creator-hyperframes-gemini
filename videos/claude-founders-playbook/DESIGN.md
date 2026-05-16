# DESIGN — Anthropic Shorts (Cinematic V3)

> V2 docs follow below — the new V3 components are documented here first.

## V3 component library

V3 ships **four new phase archetypes** + **two new persistent atmosphere layers**, sitting on top of the V2 chrome and motion language. Operators can reorder, swap, or duplicate any of these for a given video.

### Phase archetypes

| Archetype | Selector | Anatomy | When to use |
|---|---|---|---|
| **Terminal** | `.term` | macOS-style window chrome + traffic lights + `LIVE` status pill + body of mono lines, each with `prompt` / `out` / `dim` / `term-tag` spans | "claude-code running an analysis", a setup/methodology phase, anywhere you'd otherwise narrate a process |
| **Benchmark chart** | `.bench` / `.bench-row` | Title + 3-5 horizontal bars; each row is `[label | track→fill | value]`. Bars fill from 0→target with `expo.out`, numbers count up in sync via `countUp()`. Optional `.bench-marker` vertical dashed line for an industry-leader callout | Anytime you have 3-5 comparable values (model scores, error rates, latency by region). One color per bar from the accent rotation |
| **Code diff** | `.diff` / `.diff-panel` | Two stacked panels: `BEFORE` (red-tinted) above, `AFTER` (green-tinted) below. Each panel has a header strip with filename + line-count tag, and a body of `.diff-line` rows (line number + `±` prefix + syntax-highlighted text). Lines stagger in from the side | The "fix" phase of a postmortem, "before X / after Y" config changes, anywhere a prose explanation would lose to actually showing the change |
| **Quote / social-proof card** | `.quote-card` | Twitter/X-style card: avatar (gradient initials), name + handle + date, verified blue check, body text with `.em` accent, bottom stat row (likes / reposts / views) that **counts up via `countUp()`** | Social proof, user testimonial, "what people said about it" beat before a CTA |

### Persistent atmosphere

| Layer | Selector | Role |
|---|---|---|
| **Particle constellation** | `#particle-field` | 30 deterministic dots scattered across the canvas (seeded — same scatter every render), connected to their two nearest neighbors with thin lines. Sits behind content, in front of phases. Particles drift slowly in a sine yoyo over the full duration. Produces a "knowledge graph" / starfield atmosphere that fills empty space between content blocks |
| **Anamorphic flare** | `#anamorphic` | Wide horizontal blue-white streak (1680px wide, 6px tall, blurred, screen-blend) that whips across the canvas via the `fireAnamorphic(tl, t, dur)` helper. Use sparingly — once per video, on the single biggest hero impact frame. Reads as a 2.39:1 lens flare |
| **Token-stream edges** | `.token-stream` (left + right) | Faint vertical mono character columns on the left and right edges, opacity 0.10. Deterministic content seeded once. Decorative — gives a "data console" frame to the composition |

### V3 helpers (in `<script>`)

| Function | Purpose |
|---|---|
| `seedHash(seed)` | Deterministic hash → 0–1 float. Use for any pseudo-random placement |
| `spawnShapes(prefix, container)` | V2 — Anthropic shape backdrop |
| `spawnParticles(prefix, container, svg)` | V3 — particle constellation + connecting lines |
| `animateParticles(tl, positions, duration)` | V3 — slow drift on every particle, sine yoyo |
| `fillTokenStreams()` | V3 — populate left/right token-stream columns |
| `repositionShapesPerPhase(tl, container, prefix, T[])` | V2 — re-scatter shapes at each transition |
| `fireLightLeak(tl, t, dur)` | V2 — warm diagonal sweep |
| `fireAnamorphic(tl, t, dur)` | V3 — horizontal blue-white whip |
| `countUp(tl, sel, target, start, dur, formatter?)` | V2/V3 — number count-up; pass an optional `formatter(v)` for percentages / locale-formatting / K-suffixes |

### Default V3 composition (34s, 6 phases)

| # | Phase | Window | Component | Color |
|---|---|---|---|---|
| 1 | Hook | 0-6s | topic lockup → hero slam | orange |
| 2 | Terminal | 6-11s | claude-cli session | green |
| 3 | Benchmark | 11-16s | 4-bar chart with leader marker | purple |
| 4 | Code diff | 16-21s | before/after stacked | blue |
| 5 | Timeline | 21-27s | connector + 3 dated cards + playhead | orange/purple/blue |
| 6 | Quote + CTA | 27-34s | tweet card → URL pill → CTA question | green |

Accent rotation across phases follows the V2 rule: no two adjacent phases share the same accent. The CTA pill is the only place green is used as the dominant color (positive reversal).

### Swapping in alternate components

To turn V3 back into a 4-phase 24s composition (V2-style):
1. Delete the `#phase2` (terminal), `#phase3` (benchmark), and `#phase4` (diff) markup
2. Renumber: rename `#phase5` → `#phase2`, `#phase6` → `#phase3`, add the V2 stat-pill block as `#phase4` (or omit)
3. Update `--duration` on `#root` to 24, recompute `T1`, `T2`, `T3` timestamps, and remove the unused phase blocks from the timeline script

To add a phase: duplicate the `<div id="phaseN" class="phase">…</div>` block, increment N, add the matching transition block (CSS exit + visibility flip + `fireLightLeak`), update the `phase-ticks` div, and bump `#root` `data-duration` + adjust per-phase timestamps.

---

# DESIGN — Anthropic Shorts (Cinematic V2)

Visual system for **YouTube Shorts** (1080x1920, 30fps, 60-180s) in the Anthropic / Claude product-launch + postmortem aesthetic. Dark stage so the Claude orange accent and warm-paper screenshot crops pop. Lifted from `diy-yt-creator/src/AnthropicPostmortemShort` (Remotion) and adapted to HyperFrames (HTML + GSAP).

## What's new in V2 (compared to V1)

V1 was a competent four-phase Short with crossfades and entrance tweens. V2 is built to **read as cinema**, not as a slide deck.

| Layer | V1 | V2 |
|---|---|---|
| Persistent chrome | Top wordmark + progress bar | Wordmark, progress bar, **letterbox bars, corner viewfinder brackets, REC indicator with pulsing red dot, live timecode counter, phase label** |
| Phase 1 | Topic slam + hero word | Same + **diagonal scan beam sweep**, **RGB chromatic-split flash on the impact frame**, **expanding impact ring**, **subtle Ken Burns push** |
| Phase 2 | Static "3" and "6" stat pills | Numbers **count up from 0 → target**, **3D-tilt entrance**, **pulse halos** after count completes, **mono LIVE ticker** beneath |
| Phase 3 | Three stacked cards | Cards + **animated SVG connector line** drawing top-to-bottom with a gradient, **playhead dot traverses** the line, **ping ring** on each date chip |
| Phase 4 | Static URL pill | URL **types out character-by-character** with a blinking caret, **pulse halo** repeats twice on the pill, **arrow nudge** on Subscribe, **word-stagger** on CTA question, **final radial warm flash** |
| Transitions | Blur + scale + opacity crossfade | Same + **light-leak warm diagonal sweep** at each phase cut |
| Grain | Inline SVG feTurbulence | **CSS radial-gradient grain** + **soft-light scanlines** (replaces feTurbulence, which taints html2canvas in cross-origin iframes and breaks shader transitions) |

All upgrades preserve the V1 design system: Inter + JetBrains Mono pairing, near-black `#0B0F18` canvas, Claude orange / purple / blue / green accent rotation, deterministic seeded shape backdrop, accent-only-on-hero rule.

## Cinematic Chrome (V2 addition)

A persistent, low-opacity "frame within the frame" sits above every phase and below the grain. Treat it like a camera viewfinder — the audience reads it subconsciously as "this is a shot, not a slide."

| Element | Position | Role |
|---|---|---|
| `#letterbox-top` / `#letterbox-bottom` | 24px solid bars top + bottom | Cinematic 2.39-ish framing — reminds the eye it's watching film |
| `#vf-tl`, `#vf-tr`, `#vf-bl`, `#vf-br` | 38px L-shaped corner brackets | Viewfinder corner marks, 55% opacity |
| `#rec-indicator` | Top-left, below corner | `● REC` with pulsing red dot — implies "this is happening live" |
| `#timecode` | Top-right, below corner | `MM:SS:FF` (frame counter) ticking across the full duration |
| `#phase-label` | Bottom-left | `01 / 04` etc — updates on each transition so the viewer always knows where they are |

These are intentionally **low-contrast** (opacity 0.55-0.85) so they frame the content without competing with it. Don't push their opacity up; they should feel like the frame, not the content.

## Light-leak transitions (V2 addition)

`#light-leak` is a single fixed div with a diagonal warm gradient (orange → cream → orange) at 28° rotation, mix-blend-mode: screen, 20px blur. The helper `fireLightLeak(tl, t, dur)` sweeps it from below the canvas, across, and off the top — fired at every phase cut. Replaces the abrupt opacity flip with something that reads as "warm flare swept across the lens."

## HyperShader (optional, not wired by default in V2)

V2 includes `@hyperframes/shader-transitions` via CDN but uses CSS blur+scale crossfades for the three phase transitions, because the CSS path is more robust against html2canvas tainting in cross-origin preview iframes. To **promote** one or more cuts to a WebGL shader transition (e.g. for the hero reveal between phase 1 and phase 2):

1. Change `style="opacity:0;"` initial on the anchor phase pair
2. Add an explicit `tl.set("#phase2", { opacity: 1 }, T1 + 0.4)` for the second anchor (HyperShader doesn't auto-show non-first anchors after the transition)
3. Wire `HyperShader.init({ scenes: ["phase1", "phase2"], timeline: tl, transitions: [{ time: T1 + 0.25, shader: "cinematic-zoom", duration: 0.5 }] })`
4. Remove the corresponding CSS crossfade tweens for that boundary

Recommended shader picks for the Anthropic-dark aesthetic: `cinematic-zoom` (hero reveal), `light-leak` (warm punctuation), `cross-warp-morph` (calm editorial). Avoid `glitch`, `chromatic-split`, `ridged-burn` — too aggressive for the brand.

---

## Style Prompt

A dark, confident stage built for vertical video. Warm off-white type sits on a near-black canvas. A small rotating palette of bright accents (Claude orange, soft purple, soft blue, soft green, plus a single red used only for warnings) drives chrome — borders, badges, glows, single accent words. **Persistent film-camera chrome** (letterbox, viewfinder brackets, REC dot, timecode) frames every shot so the piece reads as cinema, not slides. Layout is phase-based: only one phase is visible at any frame, each phase has a 240px top safe-zone reserved for a persistent Claude wordmark, and content is centered with generous breathing room. Motion is spring-driven and percussive — slam-in hero words with a tight inline shake and a **chromatic RGB split** on the impact frame, stat pills that **count up from zero** and pop with halo rings, timeline cards that **arrive along a drawn connector line** with a traveling playhead, and a CTA URL that **types out under a blinking caret** before bursting with a final radial warm flash. Reads like a premium engineering postmortem with a documentary-film camera, not a tech-influencer reaction video.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **60-180s** (YT Shorts hard max 180s)
- Background: solid `#0B0F18`. No full-screen linear gradients (banding under H.264) — use radial highlights or solid + localized glow only.

## Colors

| Role | Hex | Usage |
|---|---|---|
| Background | `#0B0F18` | Page canvas — near-black with a touch of blue |
| Background deep | `#060810` | Vignette / outer-frame deep tone |
| Card surface | `#161B26` | Dense card panels, secondary surfaces |
| Primary text | `#F5F1EB` | Headlines, body — warm off-white |
| Secondary text | `#9A958D` | Captions, meta, fineprint (4.5:1 on background) |
| Accent — orange | `#E97458` | Claude primary — hero stat, CTA, primary slam word |
| Accent — purple | `#A78BFA` | Secondary feature, "second bug" colorway |
| Accent — blue | `#6B9AEF` | Technical / docs colorway |
| Accent — green | `#7DD3A6` | Positive reversal, URL CTA |
| Accent — red | `#D14343` | REC dot + warnings ONLY — never decorative |

**Accent rotation rule:** Within one video, no two adjacent phases share the same accent. Orange leads (hero + CTA); purple/blue/green rotate through the middle.

## Typography

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero slam word | `Inter` | 900 | `letter-spacing: -4px`, glow + drop-shadow; **add `.rgb-split` class for 0.25s on impact** |
| Topic slam | `Inter` | 900 | 156px, letter-spacing -5px |
| Headline | `Inter` | 800-900 | letter-spacing -1px, line-height 1.05 |
| Section overline | `JetBrains Mono` | 700 | UPPERCASE, letter-spacing 5-7px, accent color |
| Date chip / caption / URL | `JetBrains Mono` | 700-900 | letter-spacing 1-2px, `font-variant-numeric: tabular-nums` |
| Stat number | `Inter` | 900 | 200px, tabular-nums, **count up via `countUp(tl, sel, target, start, dur)` helper** |
| Cinematic chrome (REC, timecode, phase) | `JetBrains Mono` | 700 | 22px, letter-spacing 2-4px |

## Layout safe zones

The chrome reserves space — content must stay within:
- Top: **240px** (clears wordmark at 156px + top chrome at 88px)
- Sides: **60px**
- Bottom: **240px** (clears progress bar, phase label, letterbox)

`.phase-content` uses `padding: 240px 60px 240px; display: flex; flex-direction: column; box-sizing: border-box`. **Never** `position: absolute; top: Npx` on content containers — text wraps overflow.

## Motion Language

- **Easing palette (vary at least 3 per phase):**
  - `back.out(1.6-1.7)` — slam-in hero words, stat pills (signature Anthropic spring)
  - `power3.out` — headlines and primary text rises
  - `power2.out` — body / chip / pill entrances
  - `expo.out` — high-impact reveals (URL slam, impact ring expansion)
  - `sine.inOut` — ambient breath, post-entry float, arrow nudge
  - `steps(N)` — typewriter, caret blink
  - **Avoid** `elastic` and `bounce` — toy-like for this brand
- **Duration:**
  - Hero / slam word entry: 0.6-0.9s
  - Headline: 0.5-0.7s
  - Body / chip: 0.35-0.5s
  - Phase crossfade: 0.4s opacity + 0.5s blur, ~0.7-0.8s total
  - Light-leak sweep: 0.7s
  - Count-up: 1.0s (expo.out so the final digit lands hard)
  - Typewriter: ~60ms per character
- **Inline shake** on slam frame: 4 ticks ±5-6px translate over 0.16s. One shake per phase max.
- **Mid-scene activity** (every scene > 4s):
  - Logo / hero subtle vertical breath (`y: ±4-6`, sine.inOut yoyo)
  - REC dot pulse (yoyo opacity, slow)
  - Subscribe arrow nudge (`x: 8`, yoyo)
  - Pulse halo on stat pills / URL pill (one-shot scale+fade rings)

## Audio / SFX cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

**DEFAULT: transition whooshes only.** One `cinematic-whoosh` per phase boundary, nothing else. The whoosh `data-start` MUST equal `sceneT - 0.4` (matching the shape-backdrop reposition tween start), not `sceneT`.

V2's cinematic chrome adds *visual* punctuation; do NOT add corresponding SFX (no REC-blip, no timecode-tick, no scan-beam-whoosh). Per-cue SFX read as cluttered against the calm dark-stage aesthetic.

| Cue | Use on | Default `data-volume` | Default state |
|---|---|---|---|
| `cinematic-whoosh` | Phase boundary (paired w/ shape reposition + light-leak) | `0.11` | **ON by default** |
| `impact-slam` | Hero word reveal | 0.15 | OFF — opt-in |
| `scale-slam` | Stat-pill entrance | 0.15 | OFF — opt-in |
| `screen-shake` | Hero word inline shake | 0.11 | OFF — opt-in |
| `spring-pop` | Card or chip entrance | 0.11 | OFF — opt-in |
| `sonic-logo` | Composition start | 0.45 | OFF — never on by default |

Hard cap: never exceed `0.25` on a per-cue SFX (sonic-logo `0.45` is the only exception).

## What NOT to Do

1. **No light canvas.** Dark stage only.
2. **No more than one accent per phase.**
3. **No serif headlines.** Inter only.
4. **No flashing strobes > 6 frames.** Publication-grade calm, not influencer chaos.
5. **No `<br>` in content text.** Use `max-width` for natural wrapping.
6. **No background music on Shorts.** Narration + SFX only.
7. **No `position: absolute; top: Npx` on `.phase-content`.** Use padding.
8. **No accent below 40px** outside chrome — orange/purple/blue/green don't carry contrast for body.
9. **No SVG-filter `data:image/svg+xml` grain.** Taints html2canvas; breaks shader transitions. Use the CSS radial-gradient `#grain` in V2.
10. **No per-element SFX by default.** Only `cinematic-whoosh` on phase transitions.
11. **No high-intensity chrome.** Cinematic chrome opacity should sit 0.55-0.85. Push it higher and it dominates the content.
12. **No chromatic-split outside hero impact frame.** RGB split is a one-shot punctuation, not a hold state. Add the `.rgb-split` class for ≤ 0.25s, then remove.
