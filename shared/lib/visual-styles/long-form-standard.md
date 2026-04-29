# Long-Form Standard — Dark Navy Documentary Stage

**Mood:** Confident, premium engineering documentary | **Best for:** Generic horizontal long-form (4-15 min) — product deep-dives, news explainers, technical postmortems, release retrospectives, comparative reviews.

A dark navy stage built for horizontal long-form. Off-white type sits on a deep navy canvas. A 4-tier accent rotation (blue → cyan → purple → green, with orange + yellow held back for warnings and hero stats) drives chrome — borders, badges, glows, single accent words, per-scene tinting. Layout is sub-composition-based: each scene is its own paused GSAP timeline; the root only orchestrates ambient background + crossfades. Motion is restrained but percussive — back.out springs on cards/pills, expo.out on hero reveals, sine.inOut on ambient breath. Reads like a premium engineering documentary, not an influencer upload.

## Tokens

[`shared/lib/tokens/long-form-standard.css`](../tokens/long-form-standard.css)

Defines: `--bg`, `--bg-card`, `--bg-surface`, `--border`, `--border-bright`, `--accent-1`, `--accent-2`, `--accent-3`, `--accent-4`, `--accent-warn`, `--accent-stat`, `--text`, `--text-secondary`, `--text-muted`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--mono`, `--sans`.

## Palette roles

| Role | Token | When to use |
|---|---|---|
| Background | `--bg` | Canvas — near-black `#0B0F1A` with deep navy bias. |
| Card surface (default) | `--bg-card` | Default panel fill (4% white). |
| Card surface (raised) | `--bg-surface` | Pills, raised UI chrome (8% white). |
| Border (default) | `--border` | Card and panel strokes (10% white). |
| Border (bright) | `--border-bright` | Active or featured strokes (18% white). |
| Body text | `--text` | Headlines, body — warm off-white (14.5:1 AAA). |
| Secondary text | `--text-secondary` | Captions, sub-lines, metadata (4.7:1 AA). |
| Muted text | `--text-muted` | Large text only — fails AA at body size; reserve for chrome. |
| Primary accent | `--accent-1` (blue) | Lead in image-hero, side-by-side A, source-card 1. |
| Secondary accent | `--accent-2` (cyan) | Secondary in source-card 2, video-embed overline. |
| Tertiary accent | `--accent-3` (purple) | Source-card 3, side-by-side B, architecture overline. |
| Success accent | `--accent-4` (green) | "Fixed", launch confirmation, positive reversal. |
| Warning accent | `--accent-warn` (orange) | Hook overline, stat-pill #1, CTA subscribe pulse. |
| Stat accent | `--accent-stat` (yellow) | Hero stat slam digits ONLY. |

**Accent rotation rule:** within one video, no two adjacent scenes share the same lead accent. Blue, cyan, purple, green rotate; orange leads warnings; yellow is reserved for hero stats only.

## Typography

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero stat / slam | `--sans` (Inter) | 900 | `letter-spacing: -4px`, glow + drop-shadow |
| Headline | `--sans` (Inter) | 800-900 | `letter-spacing: -1px`, line-height 1.05 |
| Body | `--sans` (Inter) | 500-600 | line-height 1.3-1.4 |
| Section overline | `--mono` (JetBrains Mono) | 700 | UPPERCASE, `letter-spacing: 5-7px`, accent color |
| Stat number | `--sans` (Inter) | 900 | tabular-nums, `letter-spacing: -4px` |
| Card title | `--sans` (Inter) | 800 | `letter-spacing: -0.5px` |
| URL / code | `--mono` (JetBrains Mono) | 600-700 | `letter-spacing: 2px` |

**Type scale (long-form 1920x1080):** Hero stat 130px · Hero headline 100px · Section headline 64px · Comparison headline 56px · Stat pill digit 130px · Side-by-side stat 84px · Card title 28-32px · Body large 26px · Body 22px · Overline 26-28px · Caption 38px (transcribe target).

## Motion Signature

| Easing | Use for |
|---|---|
| `expo.out` | Hero word reveal, URL slam, single-element impact |
| `back.out(1.4)` | Card / chip / pill entrances (signature spring) |
| `back.out(1.6)` | Stat pill pop |
| `power3.out` | Headlines and primary text rises |
| `power2.out` | Body / secondary text entrances |
| `power1.in` | Outgoing scene blur+fade (root crossfade) |
| `sine.inOut` | Ambient background breath ONLY |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Stagger:** 80-140ms on body lists; 120ms on multi-card rows; 150ms on architecture-stack layers; 500ms between adjacent stat pills.

**Inline shake** is reserved for Shorts. Long-form is steadier.

## Suggested Lib Picks

| Block / Component / Effect | Use for |
|---|---|
| [`tokens/long-form-standard.css`](../tokens/long-form-standard.css) | Always copy first — every other entry depends on these tokens |
| [`components/ambient-radial`](../components/ambient-radial/) | 3-radial wash (blue + purple + cyan) for background depth |
| [`components/progress-bar`](../components/progress-bar/) | Bottom-edge time progress (6px, accent-1) |
| [`components/top-banner-wordmark`](../components/top-banner-wordmark/) | Persistent brand wordmark (60px tall, 30px from top) |
| [`effects/phase-crossfade.js`](../effects/phase-crossfade.js) | Scene-to-scene transitions (blur + opacity, 1.1s span) — adapted to wrap sub-comp wrappers in long-form |
| [`effects/stat-pill-pop.js`](../effects/stat-pill-pop.js) | Stat pill scale-pop entrance (used by `scene-stat-pill-row`) |

The 8 scene archetypes themselves live in [`templates/long-form/standard/compositions/`](../../../templates/long-form/standard/compositions/) — copy from there into a new variant or a video, not from `shared/lib/blocks/` (those are Shorts-shaped at 1080x1920).

## Surface detail formulas

- **Cards:** 20-28px radius, `linear-gradient(135deg, <accent>26, <accent>0c)`, `border: 1.5px solid <accent>8c`, `box-shadow: 0 24px 60px rgba(0,0,0,0.55)`.
- **Stat pill (hero):** 56px vertical padding, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>80`).
- **Source card (photo + meta):** 20px radius, photo at 62% height (object-fit cover), meta block 24-28px padding, mono overline at 18px in a brighter accent variant for AA at small sizes.
- **Architecture layer:** 14px radius, 8px accent left-strip, 90px tall, 32-56px padding, mono label → sans name → secondary meta.
- **CTA subscribe pill:** rounded (`border-radius: 999px`), orange gradient, finite yoyo-pulse glow (repeat ≤ 4).
- **Embedded video frame:** 24px radius, 2px bright border, 32px×80px black drop-shadow, wrapper-only animation (NEVER animate `<video>` directly).
- **Ambient:** 3-radial wash (blue + purple + cyan), 30s sine yoyo, 14 deterministic shapes drift across full duration.

## Audio Bed (long-form-specific)

Long-form supports a 3-segment bg-music bed under narration (Shorts forbid bg-music). Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

| Segment | data-volume | When |
|---|---|---|
| Narration (track 2) | `1.0` | Full-composition single stem |
| `bg-music-hook` (track 3) | `0.12` | First 8-12s — energy under hook |
| `bg-music-body` (track 3) | `0.07` | Body — ducked under explanation |
| `bg-music-cta` (track 3) | `0.12` | Final 12-15s — energy back up |

All bg-music sequential on track 3, no overlap. SFX on tracks 4+. Hard cap **0.25** per single per-cue SFX (sonic-logo at 0.60 is the only documented exception).

## Pacing baseline (vidIQ-aligned)

- **Hook:** earn the watch in the first 10 seconds (`scene-hook` ships at 0-12s).
- **Pattern interrupt:** every 20-30s (default scene boundaries: 0/12/32/55/70/90/105/115).
- **CTA placement:** 60-70% mark for the strongest pull (template wires the closing CTA at 115s of 120s — adjust upward when expanding).
- **End-screen:** final 15-20s reserved for `scene-cta` (subscribe pulse + next-video card).

## What NOT to Do

1. No light canvas. This style is dark navy stage only.
2. No more than one lead accent per scene — pick one of blue/cyan/purple/green for that scene's chrome.
3. No serif headlines — Inter only.
4. No `repeat: -1` anywhere — all loops must be deterministic (finite repeat).
5. No `tl.from()` at position > 5 without `immediateRender: false` (long-form-specific gotcha — without the flag, GSAP applies the from state at t=0 and the element flashes invisible).
6. No `data-duration` on sub-composition wrapper divs — the sub-comp's internal timeline owns its length.
7. No `class="clip"` on `<audio>` or `<video>`. Wrapper div takes the clip role for video; audio takes data-start/duration/track-index without class.
8. No `position: absolute; top: Npx` on scene content — use padding for content positioning.
9. No phase mutex for long-form — use sub-composition split (each scene in its own external file).
