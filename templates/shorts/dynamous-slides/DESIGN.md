# Design — Dynamous-Slides Shorts Template

Vertical (1080×1920) port of `templates/long-form/dynamous-slides/`. Keeps the entire Dynamous brand system (palette, type, weight-contrast, decorative stack, flash-flagged crossfade rhythm) — only the canvas, the safe-zones, and the per-element scale change.

All values live as CSS custom properties on `:root` in `tokens/dynamous-short.css`.

---

## Palette

| Token | Hex / Value | Role |
|---|---|---|
| `--bg` | `#07090F` | Near-black with blue tint — every scene background |
| `--bg-alt` | `#080A13` | Alternate slightly warmer surface |
| `--ink` | `rgba(255,255,255,.98)` | Primary headlines + display type |
| `--ink-2` | `rgba(255,255,255,.78)` | Body copy |
| `--muted` | `rgba(255,255,255,.58)` | Captions, secondary lines |
| `--muted-2` | `rgba(255,255,255,.36)` | Pillar sublines, low-emphasis |
| `--accent` | `#3B82F6` | **Dynamous Blue** — hero color, primary focus |
| `--accent-2` | `#60A5FA` | Dynamous Light — highlights, eyebrows, accent underlines |
| `--accent-3` | `#0EA5E9` | Dynamous Cyan — CTA glow, secondary halo |
| `--accent-dim` | `#1E40AF` | Deep halo / hover state |
| `--accent-pale` | `#DBEAFE` | Reserved for rare light-mode accents |
| `--accent-warn` | `#F97316` | Used ONLY on the closing subscribe pill (legacy alias) |

**Brand rules** (inherited from the deck):

- Dynamous Blue is the hero. Restrict to one or two focal elements per scene.
- **NO PURPLE.** For tertiary accents reach for Cyan (`#0EA5E9`) or the deep halo (`#1E40AF`), never purple.
- The persistent `#bg-halo` + `#bg-halo-2` backdrop layers do the brand atmosphere — per-scene glows stay subtle so they don't fight.

## Typography

| Font | Variable | Used for |
|---|---|---|
| Montserrat | `--font-display` | Every word the viewer reads. Weight 300/700/800/900. |
| JetBrains Mono | `--font-data` | Eyebrows, numbers, URLs, code-feeling type. |

**Weight contrast 300/800** is the signature move — a 300-weight `<span>` against an 800-weight headline (used in `scene-headline-accent` and `scene-tension-pivot`).

Type scale at 1080×1920 (per [`shorts-typography.md`](../../../.claude/rules/shorts-typography.md)):

| Class / role | Size | Used in |
|---|---|---|
| Hook wordmark | 180px | `scene-hook-wordmark` |
| Big stat number | 280px | `scene-big-stat` |
| Big stat suffix | 160px | `scene-big-stat` |
| Tension bold | 138px | `scene-tension-pivot` |
| Tension light | 100px | `scene-tension-pivot` |
| Headline-accent slam | 138px | `scene-headline-accent` |
| Headline-accent light | 90px | `scene-headline-accent` |
| List row headline | 68px | `scene-list-reveal` |
| List row label | 52px | `scene-list-reveal` |
| List row descriptor | 32px | `scene-list-reveal` |
| Quote body | 64px | `scene-quote-card` |
| CTA headline | 64px | `scene-cta` |
| Debate question (`#cta-question`) | 56px | `scene-cta` |
| Offering label | 34px | `scene-cta` |
| Eyebrow (kicker) | 32–34px | Every scene (uppercase, JetBrains Mono) |

All sizes meet or exceed `.claude/rules/shorts-typography.md` minimums.

## Decorative layers (composited in this order)

| Layer | Z | Purpose |
|---|---|---|
| `#ambient` | 0 | Triple-source radial breath (blue + cyan + deep halo). Slow yoyo across composition. |
| `#grid-bg` | 0 | Hairline 96px grid, radial-masked. Anchors stage without competing. |
| `#shape-backdrop` | 0 | 11 Dynamous icon shapes scattered at 5% opacity. Rearrange on every scene transition. |
| `#bg-halo` | 0 | Large Dynamous-Blue radial halo top-right. 18s yoyo. |
| `#bg-halo-2` | 0 | Cyan halo bottom-left. 22s yoyo. |
| `#vignette` | 7 | Cinematic edge-darkening. |
| `#flash-overlay` | 6 | Blue radial burst overlay — GSAP-driven only on flagged transition boundaries. |
| Scenes | 1 | Sub-composition wrappers. Each scene paints on track 1. |
| `#noise-overlay` | 8 | SVG `feTurbulence` film-grain at 6% opacity. Mix-blend overlay. |
| `#top-banner` | 10 | Dynamous wordmark, top-center. Mobile-safe (within 240px top safe zone). |
| `#progress-track` | 10 | Slim Dynamous-Blue progress bar. |

## Scene catalog

| # | File | Default window | Archetype |
|---|---|---|---|
| 1 | `scene-hook-wordmark.html` | 0–9s | Character-stagger wordmark hero + flame mark |
| 2 | `scene-headline-accent.html` | 9–19s | Two-line headline with Dynamous-Blue sweep |
| 3 | `scene-big-stat.html` | 19–27s | Counter ramp with gradient text + receipt |
| 4 | `scene-tension-pivot.html` | 27–35s | 300/800 weight-contrast strike + slam. Flash-on-entry. |
| 5 | `scene-list-reveal.html` | 35–63s | 6-row enumerated list, marker-sweep per row |
| 6 | `scene-quote-card.html` | 63–70s | Line-by-line quote reveal + author chip |
| 7 | `scene-cta.html` | 70–80s | Dynamous endcard — debate question + offerings + URL. Flash-on-entry. |

Total composition: 80s default. Operator retimes per video.

## Transition flavors

The root `crossfadeScenes()` function takes a `flash` flag:

- `flash: false` — standard 1.1s blur+scale crossfade
- `flash: true` — adds a brief Dynamous-Blue radial flash across the midpoint

Default flagged boundaries:
- big-stat → tension-pivot (hero pivot — first emotional turn)
- quote-card → cta (CTA landing — settles instead of punches)

## Voice (carry into copy)

When swapping copy, keep the Dynamous tone in mind:

- **"Honestly"** and **"super"** show up. Use them.
- Direct address — say "you" often.
- Tell viewers what NOT to focus on. Removes overwhelm.
- Numbers, not vague claims. "97 engineers" beats "a lot of devs".
- One conviction per scene, max.

The full voice spec lives in `brand-voices/cole-tone-of-voice.md` when pairing this template with Cole-voice narration.

## Audio (operator wires per video)

- Narration on track 2 at `data-volume="0.9"`
- Cinematic whoosh on every scene boundary, track 3, `data-volume="0.11"`, `data-duration="1.5"`
- **NO background music** — Shorts hard rule per `.claude/rules/audio-design.md`

SFX volume table (volume caps mandatory):

| Cue | `data-volume` | Use for |
|---|---|---|
| `cinematic-whoosh` | 0.11 | Phase / scene change (default cue set) |
| `impact-slam` | 0.15 | Hero word reveal — opt-in for one beat |
| `scale-slam` | 0.15 | Stat entrance — opt-in |
| `spring-pop` | 0.11 | Card/chip entrance — opt-in |

Default ships with whoosh-only on scene transitions. Add per-element SFX only when a beat unambiguously needs the punctuation.

## What NOT to do

- Don't add purple anywhere. Cyan or deep-halo instead.
- Don't strip the flame mark from the CTA — Dynamous brand seal.
- Don't reduce the wordmark below 160px on the hook scene — loses scroll-stop power.
- Don't pulse every scene's accent at the same cadence. Vary the rhythm.
- Don't enable a flash transition on every boundary — two per video, max.
- Don't add `Math.random()`, `Date.now()`, or network fetches.
- Don't ship without replacing every `REPLACE:` token in scene HTML files.
- Don't add background music to the index.html `<audio>` block.
