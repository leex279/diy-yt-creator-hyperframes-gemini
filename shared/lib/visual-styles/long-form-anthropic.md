# Long-Form Anthropic Dark — Postmortem Stage (1920x1080)

**Mood:** Confident, premium engineering | **Best for:** Anthropic / Claude long-form deep dives — product launches, postmortems, "how it works" explainers, multi-figure article responses, dev-tooling narratives that need 4–10 min to breathe.

The horizontal 1920×1080 sibling of the Anthropic Shorts dark stage. Warm off-white type on near-black canvas. Claude orange leads; purple / blue / green rotate through middle scenes; red reserved for warnings only. Spring-driven motion with a percussive slam beat. Reads like a premium engineering postmortem, not an influencer reaction video. Splits into one paused timeline per scene (sub-composition architecture), supports background music, and ships scene archetypes specifically engineered for long-form storytelling.

## Tokens

[`shared/lib/tokens/long-form-anthropic.css`](../tokens/long-form-anthropic.css)

Defines: `--bg`, `--bg-card`, `--bg-surface`, `--border`, `--border-bright`, `--accent-1` (Claude orange), `--accent-2` (purple), `--accent-3` (blue), `--accent-4` (green), `--accent-warn` (red), `--accent-stat`, `--text`, `--text-secondary`, `--text-muted`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--sans`, `--mono`.

Same variable NAMES as [`long-form-standard.css`](../tokens/long-form-standard.css) so per-video overrides interchange across long-form variants.

## Palette roles

| Role          | Token            | When to use                                                              |
| ------------- | ---------------- | ------------------------------------------------------------------------ |
| Background    | `--bg`           | Canvas + date-chip text color (near-black `#0B0F18`).                    |
| Card surface  | `--bg-card`      | Dense secondary panels.                                                  |
| Pill / chip   | `--bg-surface`   | Default chip fill (`rgba(245,241,235,0.08)`).                            |
| Stroke        | `--border` / `--border-bright` | Card edges, screenshot frames.                          |
| Body          | `--text`         | Headlines, body — warm off-white.                                        |
| Caption       | `--text-secondary` | Secondary lines, metadata (4.7:1 contrast).                            |
| Primary       | `--accent-1`     | Claude orange — hero stats, CTA, lead scene accent.                      |
| Secondary     | `--accent-2`     | Purple — alternate scene accent, second-feature panels.                  |
| Technical     | `--accent-3`     | Blue — docs, API, technical references.                                  |
| Positive      | `--accent-4`     | Green — launches, "shipped", positive reversals.                         |
| Warning       | `--accent-warn`  | Red — regression, deprecation, "removed in this release" only — never decorative. |
| Hero stat     | `--accent-stat`  | Hero stat digits (same orange — Anthropic uses orange, not yellow).      |

**Accent rotation rule:** within one video, no two adjacent scenes share the same accent. Orange leads (hook + CTA); purple / blue / green rotate through middle scenes.

## Typography

| Role             | Family                       | Weight  | Treatment                                                          |
| ---------------- | ---------------------------- | ------- | ------------------------------------------------------------------ |
| Hero / slam      | `--sans` (Inter)             | 900     | `letter-spacing: -4px`, glow + drop-shadow                         |
| Headline         | `--sans` (Inter)             | 800-900 | `letter-spacing: -1px`, line-height 1.05                           |
| Body large       | `--sans` (Inter)             | 600     | line-height 1.3                                                    |
| Body             | `--sans` (Inter)             | 500     | line-height 1.4                                                    |
| Section overline | `--mono` (JetBrains Mono)    | 700     | UPPERCASE, `letter-spacing: 5-7px`, accent color                   |
| Date chip        | `--mono` (JetBrains Mono)    | 700-900 | `letter-spacing: 1-2px`, tabular-nums                              |
| Stat number      | `--sans` (Inter)             | 900     | tabular-nums, `letter-spacing: -4px`                               |
| URL / code       | `--mono` (JetBrains Mono)    | 600-700 | `letter-spacing: 2px`                                              |

**Type scale (long-form-tuned, 1920×1080):** Hero stat 200px · Headline 100–120px (3D-reveal scene uses 72px headline to fit beside the image) · Body large 36–40px · Body 28–32px · Overline 28–32px · Caption 24–28px.

> Smaller than Shorts on the slam (200 vs 240) because the horizontal canvas affords more sub-headline room; larger on the body (28+ vs 36+) because viewers sit further from the screen.

## Motion Signature

| Easing           | Use for                                                   |
| ---------------- | --------------------------------------------------------- |
| `back.out(1.7)`  | Hero / slam-word entrances (the signature spring)         |
| `back.out(1.6)`  | Stat pill pop                                             |
| `back.out(1.5)`  | Card slide-in with overshoot                              |
| `back.out(1.4)`  | 3D-reveal image entrance (rotateY -25→0, scale 0.7→1)     |
| `power3.out`     | Headlines and primary text rises                          |
| `power2.out`     | Body / chip / pill text entrances                         |
| `expo.out`       | High-impact one-element reveals (URL slam)                |
| `power1.in`      | Outgoing scene blur + fade                                |
| `sine.inOut`     | Ambient breath only · finite 3D-image rotateY micro-yoyo  |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Stagger:** 80-140ms on body lists; 40-60ms on chip rows; 200-280ms between timeline cards; 500ms between adjacent stat pills; **1.5s between list-card reveals** (long-form step-by-step pacing).

**Inline shake** on the impact frame of a hook slam word (4 ticks, ±5px, 40ms each). One shake per scene maximum.

## Suggested Lib Picks

| Block / Component / Effect                                                       | Use for                                                              |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [`tokens/long-form-anthropic.css`](../tokens/long-form-anthropic.css)            | Always link first — every other entry depends on these tokens       |
| [`blocks/dynamous-midroll/`](../blocks/dynamous-midroll/)                        | 31.5s Dynamous AI Mastery promotional break (horizontal, brand-locked) |
| [`blocks/dynamous-endcard/`](../blocks/dynamous-endcard/) (Shorts; long-form uses scene-cta) | Reference for the Dynamous wordmark + 10% OFF treatment        |
| [`components/ambient-radial/`](../components/ambient-radial/)                    | Background depth — orange + purple breath                            |
| [`components/progress-bar/`](../components/progress-bar/)                        | Bottom-edge time progress                                            |
| [`components/top-banner-wordmark/`](../components/top-banner-wordmark/)          | Persistent Anthropic wordmark (copy logo from `shared/logos/`)       |
| [`components/subscribe-banner/`](../components/subscribe-banner/)                | Mid-video subscribe pop-in (long-form 1920×1080)                     |
| [`components/support-banner/`](../components/support-banner/)                    | Mid-video support-the-channel banner                                 |
| [`effects/phase-crossfade.js`](../effects/phase-crossfade.js)                    | Scene-to-scene transitions (blur + opacity, 1.1s span)               |
| [`effects/hero-slam-shake.js`](../effects/hero-slam-shake.js)                    | Impact-frame shake on the hook slam word                             |
| [`effects/stat-pill-pop.js`](../effects/stat-pill-pop.js)                        | Stat pill scale-pop entrance                                         |

## Scene archetypes (template-local — not yet promoted to shared/lib/blocks)

Long-form Anthropic ships 12 scene archetypes via `compositions/scene-*.html`. These are not yet extracted to `shared/lib/blocks/` because they're tightly coupled to the long-form sub-composition pattern. The canonical source is `templates/long-form/anthropic/compositions/`:

- `scene-hook.html` — 200px stat slam + inline shake; opens the video
- `scene-image-3d-reveal.html` — **signature scene** — `rotateY -25→0, z -200→0, scale 0.7→1` on a hero image with a finite-repeat `±1.5° sine.inOut` micro-yoyo after settle. Ideal for blog screenshots, product mockups, source-graphics that benefit from depth
- `scene-list-cards.html` — 4-card 2×2 grid with ~1.5s stagger reveals (step-by-step enforced)
- `scene-quote-card.html` — 180px orange opening quote-mark + italic centered quote + marker-sweep underline
- `scene-side-by-side.html` — orange vs purple two-panel compare
- `scene-stat-pill-row.html` — 2–3 huge stat pills with mono labels, 500ms stagger
- `scene-dynamous-midroll.html` — opt-out community plug
- `scene-subscribe-banner.html` — 7s mid-video subscribe pop-in
- `scene-source-cards.html` — 3-card photo + overline + title row
- `scene-video-embed.html` — embedded clip with mono overline + caption
- `scene-architecture-stack.html` — 5-layer stack for system recap
- `scene-cta.html` — closing CTA with debate question (mandatory per [`engagement-cta.md`](../../../.claude/rules/engagement-cta.md))

## Surface detail formulas

- **Cards:** 20-26px radius, `linear-gradient(135deg, <accent>26, <accent>0c)`, `border: 2px solid <accent>66`, `box-shadow: 0 14px 36px <accent>33`.
- **Stat pill:** column flex, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>66`).
- **Date chip:** mono 700-900, solid accent fill, `color: var(--bg)` for AAA contrast.
- **URL pill:** mono 700, green gradient + green border, max-width 920px.
- **3D-reveal frame:** 20px radius, `border: 2px solid #E9745888`, `box-shadow: 0 24px 60px rgba(0,0,0,0.55), 0 0 80px #E9745844`, `transform-style: preserve-3d` on parent.
- **Quote card:** opening quote-mark 180px Inter 900 orange, body 56px Inter 700 italic, attribution 28px mono uppercase.

## Audio / SFX

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Default cue set is **transition-whoosh only** (same as Anthropic Shorts) — one `cinematic-whoosh` per scene boundary, `data-volume="0.11"`, `data-duration="1.5"`. Per-element SFX (impact-slam, scale-slam, screen-shake, spring-pop, pop, glitch-zap, strike-cross) are opt-in for a single deliberate moment.

**Long-form supports background music** (Shorts do not). The template ships the 3-segment bed pattern from `templates/long-form/standard/` (commented out in `index.html`):

| Segment             | When                                       | `data-volume` |
| ------------------- | ------------------------------------------ | ------------- |
| `bg-music-hook.mp3` | First 8–12s, before narration kicks in    | `0.12`        |
| `bg-music-body.mp3` | Body of the video, under narration         | `0.07`        |
| `bg-music-cta.mp3`  | Final 10–15s, energy back up for CTA      | `0.12`        |

Hard cap **0.25** per single per-cue SFX (sonic-logo at 0.45 is the only documented exception). Never lyrical music under narration.

## What NOT to Do

1. No light canvas. This style is dark-stage only.
2. No more than one accent per scene — pick orange OR purple OR blue OR green for that scene's chrome.
3. No serif headlines — Inter only.
4. No flashing strobes / glitches longer than 6 frames.
5. No `<br>` in content text — use `max-width` for natural wrapping.
6. No `position: absolute; top: Npx` on scene-root content — use padding-based positioning.
7. No accent below 40px — orange / purple / blue / green don't carry contrast for body. Reserve them for hero, headline, badges, borders, single accent words.
8. No `tl.from()` at timeline position > 5 without `immediateRender: false` (long-form-specific gotcha — prefer explicit `tl.set` + `tl.to` per [`step-by-step-reveal.md`](../../../.claude/rules/step-by-step-reveal.md)).
9. No `data-duration` on sub-composition wrapper `<div>`s in `index.html` — the sub-comp's internal timeline owns its length.
10. No `class="clip"` on `<audio>` or `<video>` elements.
11. No `repeat: -1` on the 3D-reveal scene's micro-yoyo — calculate finite repeats (`Math.floor(SCENE_DURATION / 12)`).
