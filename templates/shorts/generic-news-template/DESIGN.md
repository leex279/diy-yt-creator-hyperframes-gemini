# Generic News Template — Design System

Brand-neutral cinematic tech-news Shorts. Forked from the [`OpenAI News`] design canvas. **Default variant: Spectrum Drift** (4-color rotation). Alt: **Frontier Green** (ChatGPT-mint mono-accent).

## Canvas

- **Resolution**: 1080×1920 (9:16)
- **Frame rate**: 30fps
- **Duration default**: ~79 seconds (15 phases @ ~5s each)
- **Duration target**: 24-180s (extend phase windows for longer videos)

## Color

### Spectrum Drift (`index.html`)

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#0B0F18` | Canvas base |
| `--bg-deep` | `#060810` | Deep gradient stop |
| `--card` | `#0E121A` | Card / panel background |
| `--text` | `#F5F1EB` | Primary off-white |
| `--text-dim` | `#9A958D` | Secondary text |
| `--orange` | `#06b6d4` | Accent A (cyan) — phase label, REC, leader markers |
| `--purple` | `#c084fc` | Accent B (purple) |
| `--blue` | `#60a5fa` | Accent C (blue) |
| `--green` | `#fbbf24` | Accent D (amber) |
| `--red` | `#D14343` | REC dot / warnings |

### Frontier Green (`_alt/frontier-green.html`)

| Token | Hex | Role |
|---|---|---|
| `--orange` | `#10a37f` | ChatGPT mint (primary) |
| `--purple` | `#19c37d` | Secondary mint |
| `--blue` | `#74e8c0` | Tertiary mint |
| `--green` | `#5eead4` | Quaternary mint |

All other tokens identical to Spectrum Drift.

## Typography

- **Sans**: Inter (300, 500, 700, 800, 900) — body, headlines, slams
- **Mono**: JetBrains Mono (400, 500, 700, 800) — chrome (REC, timecode, phase label), terminal, code diff
- **Heteronym audit**: required per [`.claude/rules/tts-pronunciation.md`](../../../.claude/rules/tts-pronunciation.md) before TTS.

### Size hierarchy (1080×1920 canvas)

| Role | Px | Notes |
|---|---|---|
| Hero slam (single word) | 140-200px | `#p1-hero`, `#p1-topic-slam` |
| Phase headline | 56-72px | `#p3-headline`, etc |
| List item / primary | 48-64px | Cards, pills |
| Descriptor / role | 30-36px | Subtitles below primary |
| Caption pill / context | 32-40px | Hashtag pills |
| CTA pill | 44-56px | Final-phase CTA |
| Overline / mono moustache | 32-36px | Mono labels above headlines |
| Chrome (REC, timecode, phase label) | 22px | Cinematic chrome — kept small intentionally |
| Stat number | 140-200px | Big colored numerals |
| Stat label (under number) | 28-34px | Mono caption |

Sub-32px on canvas is unreadable on phone — see [`.claude/rules/shorts-typography.md`](../../../.claude/rules/shorts-typography.md).

## Motion signature

1. **Phase crossfade** — blur(20px) + scale(0.97 / 1.04) for 0.5s. Hard but cinematic.
2. **Light leak burst** — 0.7s diagonal warm sweep, fired at every transition.
3. **Anamorphic flare** — 0.45s blue-white horizontal whip, fired at hero impact moments only.
4. **RGB split + shake** — 250ms displacement on `#p1-hero` at slam-in (3.7s).
5. **Impact ring** — radial expand-and-fade behind hero word at slam-in.
6. **Particle drift** — 30 dots yoyo across full duration with sine.inOut.
7. **Ken Burns on phases** — every `.phase` scales 1.0 → 1.015 over full DUR for subtle breathing.
8. **Count-up** — `expo.out` over 1.0s on benchmark numbers + engagement stats.

## Architecture

- **Phase mutex** lives inline in `index.html`. All 15 phases sit at `position: absolute; top: 0; left: 0` and use `opacity: 0 / 1` + `visibility` to mutex.
- **No sub-compositions** by default. (Shorts convention — long-form splits into `compositions/scene-*.html`.)
- **Cinematic chrome** (letterbox / corners / REC / timecode / phase label / phase ticks / top banner / progress bar) renders ABOVE phases (z-index 12-13) and persists across the full duration.
- **Atmosphere** (ambient / mesh orbs / particles / token streams / grain / scanlines) renders BELOW phases (z-index 0-8).

## Sound design

| Cue | Used on | File |
|---|---|---|
| `cinematic-whoosh` | Phase transitions | `assets/sfx/cinematic-whoosh.mp3` |
| `impact-slam` | P1 hero word slam-in | `assets/sfx/impact-slam.mp3` |
| `scale-slam` | P1 brand lockup entry | `assets/sfx/scale-slam.mp3` |
| `spring-pop` | Card / chip entrances | `assets/sfx/spring-pop.mp3` |
| `pop` | Tiny accents (counter ticks) | `assets/sfx/pop.mp3` |
| `light-leak` | Cinematic light leak bursts | `assets/sfx/light-leak.mp3` |
| `typewriter` | Terminal staggered output (P2) | `assets/sfx/typewriter.mp3` |

Sync via `scripts/sync-video-sfx.sh videos/<slug>` after dropping `narration.wav`.

## Tasteful customization

- **Re-tint accents** — edit the four `--orange / --purple / --blue / --green` variables on `#root`. Phase ticks and REC dot auto-update.
- **Swap brand wordmark** — edit `#top-banner-wordmark` and `#p1-brand-wordmark`. To use a brand SVG logo, drop it in `assets/<brand>-logo.svg` and swap the wordmark `<span>` block for an `<img>`.
- **Drop unused phases** — for shorter videos (30-60s), hide the `#phaseN` div and remove the matching `T(N-1)` / `P(N)` anchors. The chrome adapts via the `phase-tick` count.

## What this template is NOT for

- **Long-form (4-15 min)** — use `templates/long-form/standard/` instead.
- **Brand-specific cinematic launches** — `anthropic/`, `google/`, `openai/`, `archon/`, `claude-code-version/` have curated branded chrome that beats a generic news template.
- **Tutorial step-throughs** — the cinematic chrome (REC indicator, anamorphic flares) reads as "news report", which clashes with calm tutorial pacing. Use `editorial/` instead.

## Anti-patterns

- Mounting a sub-composition (this template is single-file phase-mutex by design).
- Adding background music (shorts convention: narration + SFX only).
- Removing the cinematic chrome — the chrome IS the design language. If you don't want it, fork a different template.
- Using `font-family: var(--sans)` / `var(--mono)` — render-time compiler blocker. Use literal font names.
