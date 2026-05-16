# DESIGN — Anthropic Shorts (Dark Stage)

Visual system for **YouTube Shorts** (1080x1920, 30fps, 60-180s) in the Anthropic / Claude product-launch + postmortem aesthetic. Dark stage so the Claude orange accent and warm-paper screenshot crops pop. Lifted from `diy-yt-creator/src/AnthropicPostmortemShort` (Remotion) and adapted to HyperFrames (HTML + GSAP).

## Style Prompt

A dark, confident stage built for vertical video. Warm off-white type sits on a near-black canvas. A small rotating palette of bright accents (Claude orange, soft purple, soft blue, soft green, plus a single red used only for warnings) drives chrome — borders, badges, glows, single accent words. Layout is phase-based: only one phase is visible at any frame, each phase has a 240px top safe-zone reserved for a persistent Claude wordmark, and content is centered with generous breathing room. Motion is spring-driven and percussive — slam-in hero words with a tight inline shake, stat pills that pop, timeline cards that scale-in with a colored gradient wash. Reads like a premium engineering postmortem, not a tech-influencer reaction video.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **60-180s** (YT Shorts hard max 180s)
- Background: solid `#0B0F18`. No full-screen linear gradients (banding under H.264) — use radial highlights or solid + localized glow only.

## Colors

| Role | Hex | Usage |
|---|---|---|
| Background | `#0B0F18` | Page canvas — near-black with a touch of blue |
| Card surface | `#161B26` | Dense card panels, secondary surfaces |
| Primary text | `#F5F1EB` | Headlines, body — warm off-white (echoes Anthropic paper) |
| Secondary text | `#9A958D` | Captions, meta, fineprint (4.5:1 on background) |
| Accent — orange | `#E97458` | Claude primary — hero stat, CTA, primary slam word |
| Accent — purple | `#A78BFA` | Secondary feature, "second bug" colorway |
| Accent — blue | `#6B9AEF` | Technical / docs colorway |
| Accent — green | `#7DD3A6` | Positive reversal, "fixed", launch confirmation |
| Accent — red | `#D14343` | Warning / regression / "-3% on evals" only — never decorative |
| Pill background | `rgba(245, 241, 235, 0.08)` | Default chip / pill fill |
| Pill border | `rgba(245, 241, 235, 0.18)` | Default chip / pill stroke |
| Screenshot border | `rgba(245, 241, 235, 0.12)` | Subtle frame around image crops |

**Contrast verified (WCAG):**
- Primary text on background: 14.6:1 (AAA)
- Secondary text on background: 4.7:1 (AA normal)
- Orange on background: 6.2:1 (AA normal) — safe for 40px+ headings
- Red `#D14343` on background: 4.6:1 (AA large only — use for chips/badges, never body)

**Accent rotation rule:** Within one video, no two adjacent phases share the same accent. Orange leads (hero + CTA); purple/blue/green rotate through the middle.

## Typography

Pairing rationale: **Inter** is the workhorse — the entire dark-stage aesthetic relies on Inter's tight tracking and its 800/900 weights for the slam-in hero words. **JetBrains Mono** is the technical voice for overlines, dates, code references, URL pills. Two families, no exceptions.

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero stat / slam word | `Inter, system-ui, sans-serif` | 900 | `letter-spacing: -4px`, `text-shadow: 0 0 80px <accent>88, 0 8px 24px rgba(0,0,0,0.6)` |
| Headline | `Inter, system-ui, sans-serif` | 800-900 | `letter-spacing: -1px`, line-height 1.05 |
| Body large | `Inter, system-ui, sans-serif` | 600 | line-height 1.3 |
| Body | `Inter, system-ui, sans-serif` | 500 | line-height 1.4 |
| Section overline | `'JetBrains Mono', ui-monospace, monospace` | 700 | UPPERCASE, `letter-spacing: 5-7px`, accent color |
| Date chip / caption | `'JetBrains Mono', ui-monospace, monospace` | 700-900 | `letter-spacing: 1-2px`, `font-variant-numeric: tabular-nums` |
| URL / code | `'JetBrains Mono', ui-monospace, monospace` | 600 | `letter-spacing: 2px` |

**Type scale (Shorts-tuned):**

| Role | Size |
|---|---|
| Hero stat (e.g. "DUMBER?", "3", "OPUS 4.7") | 240px |
| Hero word secondary (e.g. "Claude Code got…") | 72px |
| Headline | 64px |
| Body large | 40-44px |
| Body | 36px |
| Section overline (mono) | 34-40px |
| Caption (mono) | 30-32px |

**Tabular numerals on stat numbers:** add `font-variant-numeric: tabular-nums lining-nums` so digits don't jitter across springs.

## Layout

**Safe zones — non-negotiable.** A persistent Claude wordmark (or video-title banner) sits at `top: 60px` and is ~560px wide. Every phase container MUST reserve top space for it. A slim progress bar may sit at the bottom.

```
PHASE_PAD_TOP    = 240px   (clears the top wordmark)
PHASE_PAD_X      = 60px    (default side padding)
PHASE_PAD_BOTTOM = 240px   (clears the progress bar + reading room)
```

`.scene-content` MUST use `width: 100%; height: 100%; padding: 240px 60px 240px; display: flex; flex-direction: column; box-sizing: border-box`. Padding positions content inward — NEVER `position: absolute; top: Npx`. Absolute-positioned content containers overflow on rendered text.

**Phase mutex:** Only one phase is visible at any frame. Use opacity + visibility crossfades on whole phases, not on individual elements. Each phase typically runs 4-12s.

## Motion Language

- **Easing:**
  - `back.out(1.7)` for slam-in hero words and stat pills (the signature Anthropic spring)
  - `power3.out` for headlines and primary text rises
  - `power2.out` for body / chip / pill entrances
  - `expo.out` for high-impact one-element reveals (URL slam)
  - `sine.inOut` for ambient breathing only
  - **Avoid** `elastic` and `bounce` — they read toy-like for this brand.
- **Duration:**
  - Hero / slam word: 0.6-0.9s
  - Headline: 0.5-0.7s
  - Body / chip: 0.35-0.5s
  - Phase crossfade: 0.4s opacity + 0.5s blur
- **Direction:** Vertical y-rises dominate (`y: +40 → 0`). Hero slams use `scale: 0.78 → 1.0`. Horizontal slides only for chip rows. No rotation. No scale-pop above 1.06.
- **Stagger:** 80-140ms on body lists; 40-60ms on chip rows; 200-280ms between timeline cards.
- **Inline shake** on the impact frame of a slam word (3-6 frames, ±6px translate). One shake per phase max — overusing it cheapens it.

## Surface Detail

- **Cards:** 20-26px radius, `background: linear-gradient(135deg, <accent>26, <accent>0c)` with `border: 2px solid <accent>66`, `box-shadow: 0 14px 36px <accent>33`. Inner padding 22-32px.
- **Stat pill (huge number + label):** column flex, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>66`).
- **Date chip:** mono, 700-900 weight, solid accent fill, near-black `color: #0B0F18` for contrast, 14px radius.
- **URL / chip pill:** mono, `background: rgba(245,241,235,0.08)`, `border: 1.5px solid rgba(245,241,235,0.18)`, fully rounded (`border-radius: 999px`), 14-18px vertical padding.
- **Screenshot frame:** 20px radius, `border: 2px solid #E9745888`, `box-shadow: 0 24px 60px rgba(0,0,0,0.55), 0 0 80px #E9745844`.
- **Ambient:** one slow radial drift in accent orange (`radial-gradient(circle at 30% 25%, rgba(233,116,88,0.10), transparent 60%)`) on the root, 30s sine yoyo. No noise overlay (HyperFrames lint will flag near-pure-white text on near-pure-black if you push it; the warm off-white avoids that).

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Narration is one stem per scene (or one continuous stem with `data-media-start` offsets). SFX are layered as separate `<audio>` elements at low volume, keyed to spoken-word seconds.

**DEFAULT: transition whooshes only.** The Anthropic-shorts default is *one `cinematic-whoosh` per phase boundary, nothing else* — no per-element impact-slams, spring-pops, scale-slams, glitch-zaps, strike-crosses, screen-shakes, pops, or sonic-logo. Per-element SFX read as cluttered against the calm dark-stage aesthetic and pull attention away from narration. They are opt-in only when a specific moment unambiguously needs them (e.g., a single hero stat that warrants a slam).

**Whoosh + shape-backdrop sync rule (HARD).** Each `cinematic-whoosh` MUST fire at the same instant the shape-backdrop reposition starts. Inside `repositionShapesPerPhase` the reposition tween starts at `sceneT - 0.4`, so the whoosh's `data-start` MUST equal `sceneT - 0.4` (NOT `sceneT`). The 0.4-second offset gives shapes time to settle into their new positions while the whoosh peaks, so the audio impact lands on the visible mid-transition, not after it. Setting `data-start = sceneT` results in a perceptibly late whoosh (drift > 0.15s, which `audio-design.md` flags as a bug).

| Cue | Use on | Default `data-volume` | Default state |
|---|---|---|---|
| `cinematic-whoosh` | Phase / scene change (paired with shape-backdrop reposition) | `0.11` | **ON by default** |
| `impact-slam` | Hero word reveal | 0.15 | OFF — opt-in for a single hero moment |
| `scale-slam` | Stat-pill entrance | 0.15 | OFF — opt-in |
| `screen-shake` | Hero word inline shake | 0.11 | OFF — opt-in |
| `spring-pop` | Card or chip entrance | 0.11 | OFF — opt-in |
| `pop` | Small chip / list item | 0.10 | OFF — opt-in |
| `glitch-zap` | "BUT…" pivot, regression callout | 0.09 | OFF — opt-in |
| `strike-cross` | Strikethrough moment | 0.11 | OFF — opt-in |
| `sonic-logo` | Composition start (optional) | 0.45 | OFF — never on by default |

Hard cap: **never** exceed `0.25` on a single per-cue SFX (sonic-logo at `0.45` is the only documented exception). Stack 2-3 quiet ones rather than one loud one. Per-cue defaults above match `.claude/rules/audio-design.md`'s 2026-04-28 calibration.

## What NOT to Do

1. **No light canvas.** This is dark stage. Don't tint the background toward gray paper.
2. **No more than one accent per phase.** Pick orange OR purple OR blue OR green for that phase's chrome — don't paint a rainbow.
3. **No serif headlines.** Inter only. Reserve serif for the warm-paper light template.
4. **No flashing strobes / glitches longer than 6 frames.** This is publication-grade calm with percussive accents, not influencer chaos.
5. **No `<br>` in content text.** Use `max-width` so text wraps naturally — `<br>` causes overlap when fonts render slightly wider than estimated.
6. **No background music on Shorts.** Narration + SFX only. (BG music is for long-form.)
7. **No `position: absolute; top: Npx` on `.scene-content`.** Content containers must use `padding` to position; absolute positioning overflows on dynamic text.
8. **No accent below 40px.** Orange/purple/blue/green don't carry contrast for body — keep them on hero, headline, badges, borders, and single accent words only.
9. **No horizontal-bar marker overlays on source-screenshot anchors.** When the visual anchor of a phase is a real screenshot of a chart / bar graph (e.g., the source article's own carousel images), do NOT add a `width:0 → width:N` "marker-highlight" `<span>` that animates over the screenshot's existing bars. The screenshot already shows colored bars at the correct lengths — a synthetic overlay that grows on top reads as a duplicate bar and breaks the source aesthetic. Use marker-circles, pill-row entrances, scale-pulses on existing pills, or stat-counter rolls beside the screenshot instead. Underline-markers on synthetic text (headlines, stat-pill words) outside the screenshot frame are still fine.
10. **No per-element SFX by default.** See "Audio / SFX Cues" above — the only default cue is `cinematic-whoosh` on phase transitions, synced to the shape-backdrop reposition. Every other cue is opt-in for a specific deliberate moment.
