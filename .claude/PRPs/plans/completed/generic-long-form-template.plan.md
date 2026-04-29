# Feature: Generic Long-Form HyperFrames Template (`templates/long-form/standard/`)

## Summary

Author the **first generic long-form HyperFrames template** at `templates/long-form/standard/` — a horizontal 1920x1080 / 30fps starter project that ships a working ~120-second multi-scene demo composition exercising every reusable scene archetype the channel needs (hero hook, image-hero with overlay, side-by-side compare, stat-pill row, source-image cards, embedded-video frame, architecture stack, CTA endcard) plus a captions sub-composition. The template uses sub-composition splitting (`data-composition-src`) instead of one monolithic timeline so 8-15 minute videos remain maintainable. Defaults match the synthesized "dark navy + multi-accent" palette extracted from the three Remotion reference projects (`GoogleCloudNext2026V2`, `ClaudeSkillsVsAll`, `Gemma4Models`) but ship as project-swappable CSS variables on `#root` so any video can re-skin without forking. Scene archetypes mirror existing battle-tested patterns from `templates/shorts/anthropic/` and the long-form-specific patterns from those Remotion projects, translated to HTML + GSAP per HyperFrames hard rules.

## User Story

As the channel operator (info@smartcode.diy)
I want one canonical long-form template with all the reusable scene archetypes pre-wired so I can `cp -r templates/long-form/standard videos/<slug>` and produce a 4-15 minute YouTube long-form by editing copy + screenshots + narration only
So that every long-form video starts from a battle-tested, lint-clean, performance-tuned baseline that handles real media (screenshots, source images, embedded video) and ships to YouTube without me re-architecting the composition each time.

## Problem Statement

The repo has zero long-form templates today. `templates/long-form/README.md:5` reads `"No long-form templates yet"`. Every existing video (`videos/anthropic-100b-deal/`, `videos/archon-v0-3-9-release/`, `videos/claude-connectors-everyday-life/`) is a 1080x1920 vertical Short. There is no working `data-composition-src` example in active use anywhere in the repo (only docs reference it). There is no captions sub-composition pattern documented for HyperFrames. There is no real-media handling pattern (full-bleed photo backdrop, source-image card row, embedded-video frame) shipped as ready-to-copy starter scenes. Without this template, every new long-form video requires re-architecting the multi-scene structure, the GSAP timeline split strategy, the audio bed (narration + multi-segment background music), and the captions wiring from scratch — burning 4-6 hours per video on plumbing instead of content.

A separate long-form plan exists at `.claude/PRPs/plans/claude-code-version-longform-template.plan.md` for a *specific* Claude Code release-update video format. That plan is narrower (single video archetype, Claude Code branding). This plan is the **generic baseline** that the Claude Code template (and future variants like `dynamous`, `news-explainer`, `tutorial`) will build on top of.

## Solution Statement

Ship `templates/long-form/standard/` as a fully working, lint-clean, render-able HyperFrames project with this layered structure:

1. **Root composition** (`index.html`) — only orchestrates: ambient background (radial wash + drifting shapes + noise overlay), narration `<audio>`, optional `bg-music` `<audio>` track, and a sequence of `data-composition-src` wrapper divs each pointing at one scene sub-composition. The root timeline holds *only* ambient breath + shape drift + transition crossfades — no scene-internal animations. This caps the root timeline at ~30 tweens regardless of total video length.
2. **One sub-composition per scene archetype** (`compositions/scene-*.html`) — each is a self-contained HTML file with its own `<template>` wrapper, its own paused GSAP timeline registered on `window.__timelines["scene-<name>"]`, and its own `data-width="1920" data-height="1080"`. Eight ship by default: `scene-hook.html`, `scene-image-hero.html`, `scene-side-by-side.html`, `scene-stat-pill-row.html`, `scene-source-cards.html`, `scene-video-embed.html`, `scene-architecture-stack.html`, `scene-cta.html`. Each is independently copyable and re-orderable per video.
3. **Captions sub-composition** (`compositions/captions.html`) with the framework-required `data-timeline-role="captions"` + `data-caption-root="true"` attributes on its root, ready to be filled by `npx hyperframes transcribe` output.
4. **Token CSS file** (`tokens/long-form.css`) — extracted CSS variable system on `:root` with the synthesized dark-navy palette + 4-accent rotation, per-scene padding, type-scale, and easing tokens. Loaded once in `index.html`; inherits to all sub-compositions.
5. **Persistent overlays** — top wordmark banner, bottom progress bar (6px) on the root timeline; `data-composition-src` for both at track-index 8/9 so they sit above scene content but below captions.
6. **README.md + DESIGN.md** — full spawn workflow (cp template → edit meta.json → drop narration → lint → preview → render) and the design system spec (colors, type, motion, anti-patterns) mirroring `templates/shorts/anthropic/{README,DESIGN}.md`.
7. **Scripts wiring** — confirm `scripts/sync-video-sfx.sh` works for long-form videos (it should, but verify with a `sfx-cues.txt` round-trip).

This split-by-scene architecture is consistent with HyperFrames' official examples (`warm-grain`, `swiss-grid`, `play-mode` all use 3-file nesting per the docs at `examples.md`) and avoids the documented long-timeline gotcha where `tl.from(el, {opacity: 0}, 240)` without `immediateRender: false` flashes the future state at `t=0`.

---

## Metadata

| Field            | Value                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type             | NEW_CAPABILITY                                                                                                                                                                     |
| Complexity       | HIGH (multi-file template, sub-composition wiring, real-media patterns, captions facility, multi-segment audio bed)                                                                |
| Systems Affected | `templates/long-form/standard/`, `shared/lib/visual-styles/`, `shared/lib/tokens/`, `.claude/skills/diy-yt-creator/` (handoff doc), `templates/long-form/README.md` (status update) |
| Dependencies     | HyperFrames CLI (existing), GSAP `3.14.2` from jsdelivr CDN (existing), Inter + JetBrains Mono webfonts (existing pattern), `shared/audio/sfx/*` (existing), `shared/logos/*` (existing) |
| Estimated Tasks  | 18                                                                                                                                                                                 |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  CURRENT — only Shorts (1080x1920) ship; long-form folder is empty.           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌──────────────────┐                                                        ║
║   │ operator picks   │                                                        ║
║   │ next long-form   │                                                        ║
║   │ topic            │                                                        ║
║   └────────┬─────────┘                                                        ║
║            │                                                                  ║
║            ▼                                                                  ║
║   ┌──────────────────┐         ┌──────────────────┐                           ║
║   │ ls templates/    │────X───►│  long-form/      │  empty                    ║
║   │ long-form/       │         │  README only     │                           ║
║   └──────────────────┘         └──────────────────┘                           ║
║            │                                                                  ║
║            ▼                                                                  ║
║   ┌──────────────────┐                                                        ║
║   │ choose between:  │                                                        ║
║   │ (a) hand-build   │   4-6h plumbing per video                              ║
║   │ (b) clone Short  │   wrong dimensions, no chapters                        ║
║   │ (c) old Remotion │   different toolchain, can't ship via HyperFrames CLI  ║
║   └──────────────────┘                                                        ║
║                                                                               ║
║   USER_FLOW: copy Shorts (wrong) OR build from scratch (slow)                 ║
║   PAIN_POINT: every long-form video re-architects the composition shape       ║
║   DATA_FLOW: narration + assets → bespoke index.html → render                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  AFTER — generic long-form template ships ready-to-copy with 8 scene types.  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌──────────────────┐                                                        ║
║   │ operator picks   │                                                        ║
║   │ next long-form   │                                                        ║
║   │ topic            │                                                        ║
║   └────────┬─────────┘                                                        ║
║            │  cp -r templates/long-form/standard videos/<slug>                ║
║            ▼                                                                  ║
║   ┌──────────────────────────────────────────────────────────────────────┐    ║
║   │ videos/<slug>/                                                       │    ║
║   │  ├── index.html      ← orchestrator: 8 scene wrappers + bg + audio  │    ║
║   │  ├── compositions/                                                   │    ║
║   │  │    ├── scene-hook.html        (10-15s)                            │    ║
║   │  │    ├── scene-image-hero.html  (full-bleed photo + overlay)        │    ║
║   │  │    ├── scene-side-by-side.html(A vs B compare)                    │    ║
║   │  │    ├── scene-stat-pill-row.html(huge numbers receipts)            │    ║
║   │  │    ├── scene-source-cards.html(photo + overline + title cards)    │    ║
║   │  │    ├── scene-video-embed.html (animated wrapper around <video>)   │    ║
║   │  │    ├── scene-architecture-stack.html(layer tower)                 │    ║
║   │  │    ├── scene-cta.html         (debate Q + comment + subscribe)    │    ║
║   │  │    └── captions.html          (data-caption-root)                 │    ║
║   │  ├── tokens/long-form.css                                            │    ║
║   │  ├── audio/{narration,bg-music-body}.wav                             │    ║
║   │  └── assets/{shapes,sfx,screenshots}/                                │    ║
║   └──────────────────────────────────────────────────────────────────────┘    ║
║            │                                                                  ║
║            ▼                                                                  ║
║   ┌──────────────────────────────────────────────────────────────────────┐    ║
║   │ edit copy + drop screenshots → lint → preview → render               │    ║
║   │ (~30-45 min/video instead of 4-6h)                                   │    ║
║   └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
║   VALUE_ADD:                                                                  ║
║   • each scene is its own paused GSAP timeline (no 600s monolith)             ║
║   • real media: <img> backdrops, <video> frames, source-photo cards built-in  ║
║   • captions facility wired (data-timeline-role="captions")                   ║
║   • multi-segment bg music slot (hook/body/cta) defined                       ║
║   • subscribe-banner + chapter-card overlays available                        ║
║                                                                               ║
║   DATA_FLOW: narration.wav + transcript.json + screenshots                    ║
║              → fill 8 sub-compositions independently                          ║
║              → root timeline only orchestrates background + transitions       ║
║              → render with --quality high --workers 4                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                            | Before                | After                                   | User Impact                                                                                |
| ----------------------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| `templates/long-form/`              | Only README placeholder | `standard/` template subdir present     | `cp -r templates/long-form/standard videos/<slug>` works                                   |
| `templates/long-form/README.md`     | Status: "TBD"         | Status: "First template shipped"        | Catalog updated; future templates know what shape to mirror                                |
| `npx hyperframes preview videos/<slug>` | n/a (no template)  | Live preview at 1920x1080               | Operator can scrub through the 8 scene archetypes and edit live                            |
| `npx hyperframes lint videos/<slug>`    | n/a               | 0 errors, 0 warnings on a fresh copy    | Operator gets clean baseline; lint surfaces drift only on user edits                       |
| `npx hyperframes render videos/<slug>`  | n/a               | Renders to MP4 at high quality          | One-shot ship to YouTube                                                                   |
| `shared/lib/visual-styles/`         | Only `anthropic-dark.md` | Adds `long-form-standard.md` fragment | Future variant templates (`long-form/dynamous/`) can reuse the visual-style spec           |

---

## Mandatory Reading

**CRITICAL: implementation agent MUST read these files before starting any task. The first 4 are non-negotiable.**

| Priority | File                                                                                                                       | Lines              | Why Read This                                                                                                                     |
| -------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| P0       | `.claude/skills/hyperframes/SKILL.md`                                                                                      | full               | HARD RULES: `class="clip"` semantics, `window.__timelines` registration, deterministic-only, `<template>` wrapping for sub-comps  |
| P0       | `templates/shorts/anthropic/index.html`                                                                                    | full               | Battle-tested root composition pattern: phase mutex, P/T transition convention, ambient breath, noise overlay, audio wiring      |
| P0       | `templates/shorts/anthropic/DESIGN.md`                                                                                     | full               | Design system spec — easing table, accent rotation, surface detail, anti-patterns                                                 |
| P0       | `videos/anthropic-100b-deal/index.html`                                                                                    | 855-1006 (timeline) + 689-751 (audio) | Longest existing video (77s, 6 phases) — full SFX wiring, transcript-driven timestamps, partner-row pattern    |
| P1       | `shared/lib/effects/phase-crossfade.js`                                                                                    | full (29-45)       | The canonical 1.1s crossfade function — paste into root timeline as the transition primitive                                      |
| P1       | `shared/lib/MANIFEST.md`                                                                                                   | full               | Catalog of pre-built blocks/components/effects to copy-from (NOT reference-from)                                                  |
| P1       | `shared/lib/tokens/anthropic-dark.css`                                                                                     | full               | CSS variable system pattern; the new `tokens/long-form.css` mirrors this structure                                                |
| P1       | `templates/shorts/anthropic/compositions/` (any sub-comp file if present)                                                  | full               | Verify no sub-comp pattern exists yet in the repo — confirm we are establishing the pattern                                        |
| P2       | `.claude/rules/audio-design.md`                                                                                            | full               | SFX volume caps (0.20-0.25), track-index conventions, multi-segment bg-music rules for long-form                                  |
| P2       | `templates/shorts/anthropic/README.md`                                                                                     | full               | Spawn workflow template — the new long-form README mirrors this voice and structure                                               |
| P2       | `.claude/PRPs/plans/claude-code-version-longform-template.plan.md`                                                         | first 200 lines    | Sibling plan — confirms scope boundary (this generic template is the layer that one builds on)                                    |
| P2       | `.claude/skills/diy-yt-creator/new-anthropic-short.md`                                                                     | 183-283            | Time-derivation formula (T_n = phase_end - 0.2; P_{n+1} = T_n + 0.4) and lint-error catalog                                       |

**External Documentation:**

| Source                                                                                                                                       | Why Needed                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [HyperFrames HTML Schema](https://hyperframes.heygen.com/reference/html-schema.md)                                                            | Authoritative `data-*` attribute contract; **confirms `class="clip"` does NOT apply to `<audio>`/`<video>`**                            |
| [HyperFrames Compositions](https://hyperframes.heygen.com/concepts/compositions.md)                                                           | Sub-composition wiring rules; `<template>` wrapping for external composition files                                                       |
| [HyperFrames GSAP Animation](https://hyperframes.heygen.com/guides/gsap-animation.md)                                                         | `tl.set({}, {}, videoLengthInSeconds)` to extend timeline duration to match render length                                                 |
| [HyperFrames Performance](https://hyperframes.heygen.com/guides/performance.md)                                                               | 33ms/frame budget; cap source images at 3840x2160; expensive CSS to avoid (stacked backdrop-filter, filter:blur on big elements)           |
| [HyperFrames Rendering](https://hyperframes.heygen.com/guides/rendering.md)                                                                   | `--fps 30 --quality high --crf 16 --workers 4 --format mp4` for long-form; `--workers` matters for 30+ second renders                     |
| [HyperFrames Examples](https://hyperframes.heygen.com/examples.md)                                                                            | Confirms 3-file sub-composition architecture (intro + content + captions) is the standard in built-in templates                           |
| [GSAP Timeline Docs](https://gsap.com/docs/v3/GSAP/Timeline/)                                                                                 | Position parameter (labels for scene anchors), `defaults: {ease, duration}` to reduce repetition, `paused: true` requirement              |
| [GSAP Eases](https://gsap.com/docs/v3/Eases/)                                                                                                 | Cinematic eases (`expo.out`, `power3.out`, `back.out(1.4)`); avoid `elastic`/`bounce` for professional content                            |
| [vidIQ — YouTube Algorithm 2026](https://vidiq.com/blog/post/understanding-youtube-algorithm/)                                                | 10s hook window, pattern-interrupt every 20-30s, CTA at 60-70% mark, end-screen at final 20s                                              |

**Critical gotcha (long-form-specific):** For any `tl.from(el, {opacity: 0}, position)` where `position > 5`, set `immediateRender: false` — otherwise GSAP applies `opacity: 0` at construction time and the element flashes invisible at `t=0` of the preview. Documented at https://gsap.com/docs/v3/GSAP/Tween#immediateRender.

---

## Patterns to Mirror

### NAMING_CONVENTION (sub-composition IDs)

```
# SOURCE: examples.md (warm-grain, swiss-grid, play-mode)
# COPY THIS PATTERN: kebab-case scene IDs, prefixed with scene-

scene-hook
scene-image-hero
scene-side-by-side
scene-stat-pill-row
scene-source-cards
scene-video-embed
scene-architecture-stack
scene-cta
captions
```

### ROOT_COMPOSITION_PATTERN

```html
<!-- SOURCE: templates/shorts/anthropic/index.html:418-423 -->
<!-- COPY THIS PATTERN, change dims and duration -->
<div id="root"
     data-composition-id="main"
     data-start="0"
     data-duration="120"
     data-width="1920"
     data-height="1080">
```

### SUB_COMPOSITION_FILE_PATTERN

```html
<!-- SOURCE: HyperFrames examples.md (every external sub-composition) -->
<!-- COPY THIS PATTERN: external sub-comp files MUST wrap content in <template> -->
<template id="scene-hook-template">
  <div data-composition-id="scene-hook"
       data-width="1920"
       data-height="1080">
    <!-- scene content here -->

    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true, defaults: { ease: "power3.out", duration: 0.6 } });

      // scene tweens go here, all using tl.from / tl.to / tl.set
      // CRITICAL: any tl.from with position > 5 must include immediateRender: false

      window.__timelines["scene-hook"] = tl;
    </script>
  </div>
</template>
```

### SUB_COMPOSITION_WIRING_IN_ROOT

```html
<!-- SOURCE: HyperFrames concepts/compositions.md, examples.md -->
<!-- COPY THIS PATTERN: wrapper div in root index.html points at external file -->
<!-- NOTE: data-duration is NOT used on sub-composition wrapper divs -->
<div data-composition-id="scene-hook"
     data-composition-src="compositions/scene-hook.html"
     data-start="0"
     data-track-index="1"></div>

<div data-composition-id="scene-image-hero"
     data-composition-src="compositions/scene-image-hero.html"
     data-start="12"
     data-track-index="1"></div>
```

### CAPTIONS_SUB_COMPOSITION_ROOT

```html
<!-- SOURCE: hyperframes.heygen.com/reference/html-schema.md (captions section) -->
<!-- COPY THIS PATTERN: data-timeline-role and data-caption-root are REQUIRED -->
<template id="captions-template">
  <div data-composition-id="captions"
       data-timeline-role="captions"
       data-caption-root="true"
       data-width="1920"
       data-height="1080">
    <!-- caption groups appear here, each with data-start / data-duration -->
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["captions"] = gsap.timeline({ paused: true });
    </script>
  </div>
</template>
```

### TIMELINE_DURATION_PADDING

```js
// SOURCE: hyperframes.heygen.com/guides/gsap-animation.md
// COPY THIS PATTERN: extend root timeline to match composition duration
// without this, render is truncated at the last animation's end time
const TOTAL_DURATION = 120;  // matches data-duration on #root
tl.set({}, {}, TOTAL_DURATION);
```

### CSS_VARIABLE_TOKEN_SYSTEM

```css
/* SOURCE: shared/lib/tokens/anthropic-dark.css:17-36 */
/* MIRROR: scope to :root in tokens/long-form.css so all sub-comps inherit */
:root {
  /* Surface */
  --bg:             #0B0F1A;
  --bg-card:        rgba(255,255,255,0.04);
  --bg-surface:     rgba(255,255,255,0.08);
  --border:         rgba(255,255,255,0.10);
  --border-bright:  rgba(255,255,255,0.18);

  /* Accents (4-tier rotation, project-swappable) */
  --accent-1:       #3B82F6;  /* blue   — primary */
  --accent-2:       #06B6D4;  /* cyan   — secondary */
  --accent-3:       #8B5CF6;  /* purple — tertiary */
  --accent-4:       #22C55E;  /* green  — success */
  --accent-warn:    #F97316;  /* orange — caution */
  --accent-stat:    #FBBC04;  /* yellow — hero stats */

  /* Text */
  --text:           #F1F3F4;
  --text-secondary: #9AA0A6;
  --text-muted:     #64748B;

  /* Spacing (1920x1080 safe-zone) */
  --pad-top:        80px;
  --pad-x:          100px;
  --pad-bottom:     80px;

  /* Type */
  --sans:           'Inter', system-ui, sans-serif;
  --mono:           'JetBrains Mono', ui-monospace, monospace;
}
```

### PHASE_MUTEX_VS_SUB_COMPOSITION_DECISION

```html
<!-- SOURCE: templates/shorts/anthropic/index.html:137-148 (phase mutex) -->
<!-- vs HyperFrames examples.md (sub-composition split) -->

<!-- ❌ DO NOT USE phase mutex (#phase1, #phase2 with z-index escalation) for long-form. -->
<!-- It works for 24s Shorts but doesn't scale to 600s — every phase's GSAP runs in one root timeline. -->

<!-- ✅ DO USE sub-composition split for long-form. Each scene is its own file with its own timeline. -->
<!-- Crossfade between scenes happens at the root timeline level by tweening the wrapper div opacity. -->
```

### CROSSFADE_AT_ROOT_LEVEL

```js
// SOURCE: shared/lib/effects/phase-crossfade.js:29-45 (adapted for sub-comp wrappers)
// COPY THIS PATTERN: animate the WRAPPER divs, not internal scene content
function crossfadeScenes(tl, fromSel, toSel, atTime) {
  tl.to(fromSel, { filter: "blur(20px)", scale: 1.04, duration: 0.5, ease: "power1.in" }, atTime);
  tl.to(fromSel, { opacity: 0, duration: 0.4, ease: "power1.in" }, atTime + 0.3);
  tl.set(fromSel, { visibility: "hidden" }, atTime + 0.7);
  tl.set(toSel, { filter: "blur(20px)", scale: 0.97, opacity: 0, visibility: "visible" }, atTime + 0.4);
  tl.to(toSel, { opacity: 1, duration: 0.3, ease: "power1.inOut", overwrite: "auto" }, atTime + 0.4);
  tl.to(toSel, { filter: "blur(0px)", scale: 1, duration: 0.5, ease: "power1.out", overwrite: "auto" }, atTime + 0.6);
}
```

### REAL_MEDIA — IMAGE_HERO_BACKDROP

```html
<!-- SOURCE: synthesized from GoogleCloudNext2026V2 Scene03TPU.tsx, Scene04Virgo.tsx -->
<!-- COPY THIS PATTERN: full-bleed photo as scene backdrop with dark gradient overlay -->
<div class="image-hero-backdrop">
  <img class="clip" id="bg-photo"
       data-start="0" data-duration="20" data-track-index="0"
       src="assets/screenshots/hero-shot.png"
       alt="Hero backdrop"
       style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.18" />
  <div class="overlay-gradient"
       style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,15,26,0.55),rgba(11,15,26,0.78))"></div>
</div>
<!-- foreground text/headlines render above this with their own data-start/data-duration -->
```

### REAL_MEDIA — SOURCE_IMAGE_CARD

```html
<!-- SOURCE: synthesized from Gemma4Models Scene12Outro.tsx (Shorts thumbnails),
     GoogleCloudNext2026V2 Scene02Grid.tsx (12-card grid) -->
<!-- COPY THIS PATTERN: photo + overline + title in a glass card -->
<div class="source-card clip"
     data-start="2" data-duration="8" data-track-index="2"
     style="border-radius:20px;border:1px solid var(--border);
            background:linear-gradient(135deg,rgba(59,130,246,0.13) 0%,rgba(59,130,246,0.04) 100%);
            box-shadow:0 24px 60px rgba(0,0,0,0.55);overflow:hidden">
  <img src="assets/screenshots/source-1.png"
       style="display:block;width:100%;height:62%;object-fit:cover" alt="Source" />
  <div class="card-meta" style="padding:24px 28px">
    <div class="overline" style="font-family:var(--mono);font-size:14px;letter-spacing:0.12em;
                                 text-transform:uppercase;color:var(--accent-1)">Source · Anthropic blog</div>
    <h3 style="font:800 32px var(--sans);color:var(--text);margin:8px 0 0">Title of the source</h3>
  </div>
</div>
```

### REAL_MEDIA — EMBEDDED_VIDEO_FRAME

```html
<!-- SOURCE: hyperframes.heygen.com/reference/html-schema.md (video element rules) -->
<!-- COPY THIS PATTERN: animate the wrapper, never the <video> directly -->
<!-- NOTE: <video> does NOT take class="clip" — wrapper div takes it instead -->
<div id="video-frame-wrapper" class="clip"
     data-start="40" data-duration="20" data-track-index="2"
     style="position:absolute;left:160px;top:160px;width:1600px;height:760px;
            border-radius:24px;border:2px solid var(--border-bright);
            box-shadow:0 32px 80px rgba(0,0,0,0.7);overflow:hidden">
  <video src="assets/clips/demo.mp4"
         muted autoplay playsinline preload="auto"
         style="width:100%;height:100%;object-fit:cover"></video>
</div>
<audio src="assets/clips/demo.mp4"
       data-start="40" data-duration="20" data-track-index="6" data-volume="0.6"></audio>
```

### AUDIO_BED — NARRATION + MULTI_SEGMENT_BG_MUSIC

```html
<!-- SOURCE: .claude/rules/audio-design.md (multi-segment bg-music section) -->
<!-- + videos/anthropic-100b-deal/index.html:689-695 (narration pattern) -->
<!-- COPY THIS PATTERN. Audio gets data-start/duration/track-index but NEVER class="clip". -->
<audio id="narration"
       src="audio/narration.wav"
       data-start="0" data-duration="120" data-track-index="2" data-volume="1"></audio>

<audio id="bg-music-hook"
       src="audio/bg-music-hook.mp3"
       data-start="0" data-duration="12" data-track-index="3" data-volume="0.12"></audio>
<audio id="bg-music-body"
       src="audio/bg-music-body.mp3"
       data-start="12" data-duration="95" data-track-index="3" data-volume="0.07"></audio>
<audio id="bg-music-cta"
       src="audio/bg-music-cta.mp3"
       data-start="107" data-duration="13" data-track-index="3" data-volume="0.12"></audio>
```

### EASING_TABLE

| Easing                | Use for                                            |
| --------------------- | -------------------------------------------------- |
| `expo.out`            | Hero word reveal, URL slam, single-element impact  |
| `back.out(1.4)`       | Card / chip / pill entrances (signature spring)    |
| `power3.out`          | Headlines and primary text rises                   |
| `power2.out`          | Body / secondary text entrances                    |
| `power1.in`           | Outgoing scene blur+fade (before crossfade)        |
| `sine.inOut`          | Ambient background breath ONLY                     |
| **AVOID**             | `elastic`, `bounce` — read as toy-like for this brand |

### TIMELINE_LABELS_FOR_LONG_TIMELINES

```js
// SOURCE: gsap.com/docs/v3/GSAP/Timeline/ (position parameter)
// COPY THIS PATTERN: use labels as scene anchors so duration changes don't cascade
const tl = window.__timelines["main"];
tl.addLabel("hook",         0)
  .addLabel("image-hero",   12)
  .addLabel("side-by-side", 32)
  .addLabel("stat-pills",   55)
  .addLabel("source-cards", 70)
  .addLabel("video-embed",  90)
  .addLabel("arch-stack",   105)
  .addLabel("cta",          115);

// Crossfade calls reference labels, not numeric timestamps:
crossfadeScenes(tl, "[data-composition-id='scene-hook']",
                    "[data-composition-id='scene-image-hero']",
                    "image-hero-=0.4");
```

### IMMEDIATE_RENDER_FALSE_TRAP

```js
// SOURCE: gsap.com/docs/v3/GSAP/Tween#immediateRender
// LONG-FORM-SPECIFIC GOTCHA: any .from() at position > 5 needs this flag
// otherwise GSAP applies the "from" state at t=0 — element flashes invisible
tl.from("#headline", {
  y: 30,
  opacity: 0,
  duration: 0.6,
  immediateRender: false   // ← REQUIRED for long timelines
}, "image-hero+=0.3");
```

---

## Files to Change

| File                                                                                  | Action | Justification                                                                                              |
| ------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| `templates/long-form/standard/`                                                       | CREATE | Root template directory                                                                                     |
| `templates/long-form/standard/meta.json`                                              | CREATE | `{ id, name }` placeholder                                                                                 |
| `templates/long-form/standard/hyperframes.json`                                       | CREATE | Standard registry/paths config (identical to all other videos)                                              |
| `templates/long-form/standard/README.md`                                              | CREATE | Spawn workflow + scene archetype catalog (mirrors `templates/shorts/anthropic/README.md`)                   |
| `templates/long-form/standard/DESIGN.md`                                              | CREATE | Color/type/motion spec, easing table, surface detail, anti-patterns                                         |
| `templates/long-form/standard/index.html`                                             | CREATE | Root composition: 8 sub-comp wrappers + audio + persistent overlays + ambient background                    |
| `templates/long-form/standard/tokens/long-form.css`                                   | CREATE | CSS variable system on `:root` (palette + spacing + type)                                                   |
| `templates/long-form/standard/compositions/scene-hook.html`                           | CREATE | Hero hook archetype (10-15s)                                                                                |
| `templates/long-form/standard/compositions/scene-image-hero.html`                     | CREATE | Full-bleed photo backdrop with overlay (15-25s)                                                             |
| `templates/long-form/standard/compositions/scene-side-by-side.html`                   | CREATE | A vs B comparison (20-30s)                                                                                  |
| `templates/long-form/standard/compositions/scene-stat-pill-row.html`                  | CREATE | 2-3 huge accent-colored stats (15-20s)                                                                      |
| `templates/long-form/standard/compositions/scene-source-cards.html`                   | CREATE | Photo + overline + title card row (25-40s)                                                                  |
| `templates/long-form/standard/compositions/scene-video-embed.html`                    | CREATE | Animated wrapper around `<video>` (20-30s)                                                                  |
| `templates/long-form/standard/compositions/scene-architecture-stack.html`             | CREATE | Vertical layer stack revealing top-to-bottom (20-30s)                                                       |
| `templates/long-form/standard/compositions/scene-cta.html`                            | CREATE | Debate question + comment pill + subscribe pill + next-video card (15-20s)                                  |
| `templates/long-form/standard/compositions/captions.html`                             | CREATE | Captions sub-composition with `data-caption-root="true"`                                                    |
| `templates/long-form/standard/audio/.gitkeep`                                         | CREATE | Placeholder so directory exists in git                                                                      |
| `templates/long-form/standard/assets/.gitkeep`                                        | CREATE | Placeholder                                                                                                  |
| `templates/long-form/standard/assets/shapes/shape1.svg`                               | CREATE | Background scatter shape (copy from shorts template)                                                        |
| `templates/long-form/standard/assets/shapes/shape2.svg`                               | CREATE | Background scatter shape                                                                                     |
| `templates/long-form/standard/assets/shapes/shape3.svg`                               | CREATE | Background scatter shape                                                                                     |
| `templates/long-form/standard/assets/sfx/.gitkeep`                                    | CREATE | Placeholder for synced SFX (`scripts/sync-video-sfx.sh` populates this per video)                            |
| `templates/long-form/standard/sfx-cues.txt`                                           | CREATE | Default cue list: `impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop`                              |
| `templates/long-form/README.md`                                                       | UPDATE | Change status from "TBD" to documenting `standard/` as the canonical baseline                                |
| `shared/lib/visual-styles/long-form-standard.md`                                      | CREATE | Named visual-style fragment so future variants (`long-form/dynamous/`) can reference the same spec           |
| `shared/lib/tokens/long-form-standard.css`                                            | CREATE | Library copy of `tokens/long-form.css` so future templates can pick it up via copy-from                      |
| `shared/lib/MANIFEST.md`                                                              | UPDATE | Add the new visual-style + token entries to the catalog                                                     |

**Total: 25 CREATE, 2 UPDATE.**

---

## NOT Building (Scope Limits)

Explicit exclusions to prevent scope creep:

- **No automated content fill / pipeline integration**. This plan ships a *template*. The companion `/diy-yt-creator` skill / `phase*` commands already drive scripted content fill; that integration is a separate plan if needed.
- **No new shared/lib blocks beyond visual-style + tokens**. The 8 scene archetypes ship as sub-compositions inside the template, NOT as `shared/lib/blocks/<name>/block.html` extractions. Extraction is a follow-up if the same scene archetype gets reused across 3+ long-form templates.
- **No second long-form template (`dynamous`, `news-explainer`, `tutorial`)**. Those are siblings to be built on top of this baseline. This plan establishes the baseline only.
- **No render-pipeline / CI changes**. The existing `npx hyperframes render` is sufficient.
- **No agent/skill changes**. The existing `hyperframes` skill covers authoring; the existing `diy-yt-creator` skill covers production. No new skill required for this template.
- **No bespoke content for the demo composition**. The demo uses placeholder copy ("HEADLINE GOES HERE", "Replace this stat", lorem-ish source descriptions) — not topical content. Operators replace per-video.
- **No royalty-free music shipped**. The template documents the bg-music slot pattern but does NOT include music files. Operators source per video.
- **No HDR / 4K render**. Targets 1920x1080 / 30fps SDR. Operators can flip render flags per video if they want HDR/4K.
- **No multi-language captions**. Single-language captions facility wired only.
- **Replacement of the existing Claude Code long-form plan**. The plan at `.claude/PRPs/plans/claude-code-version-longform-template.plan.md` continues to be the right plan for the *Claude Code update* video archetype specifically. This plan is the layer below it.

---

## Step-by-Step Tasks

Execute in order. Each task is atomic and independently verifiable. Validate after each task before moving on.

### Task 1: CREATE template directory + meta files

- **ACTION**: `mkdir -p templates/long-form/standard/{compositions,tokens,audio,assets/shapes,assets/sfx}`
- **IMPLEMENT**: Create `templates/long-form/standard/meta.json`, `hyperframes.json`, `sfx-cues.txt`, and `.gitkeep` files in `audio/`, `assets/`, `assets/sfx/`.
- **MIRROR**: `templates/shorts/anthropic/meta.json`, `templates/shorts/anthropic/hyperframes.json`
- **CONTENT — `meta.json`**:
  ```json
  {
    "id": "REPLACE_WITH_VIDEO_SLUG",
    "name": "REPLACE_WITH_VIDEO_NAME"
  }
  ```
- **CONTENT — `hyperframes.json`**: byte-identical copy of `templates/shorts/anthropic/hyperframes.json`.
- **CONTENT — `sfx-cues.txt`**: `impact-slam\nscale-slam\ncinematic-whoosh\nspring-pop\npop\n`.
- **VALIDATE**: `ls templates/long-form/standard/` shows all directories and files.

### Task 2: COPY background shape SVGs from shorts template

- **ACTION**: `cp templates/shorts/anthropic/assets/shapes/*.svg templates/long-form/standard/assets/shapes/`
- **IMPLEMENT**: Copy `shape1.svg`, `shape2.svg`, `shape3.svg`. These are reused as drifting background scatter elements.
- **MIRROR**: identical files; no edits needed (the shapes are dimension-agnostic).
- **VALIDATE**: `ls templates/long-form/standard/assets/shapes/` shows 3 SVGs.

### Task 3: CREATE `tokens/long-form.css`

- **ACTION**: Author the CSS variable system on `:root` (NOT `#root` — long-form needs it on `:root` so all sub-comps inherit)
- **IMPLEMENT**: Use the synthesized "dark navy + 4-accent rotation" palette. See **Patterns to Mirror › CSS_VARIABLE_TOKEN_SYSTEM** above for the exact content.
- **MIRROR**: `shared/lib/tokens/anthropic-dark.css:17-36` for structure
- **GOTCHA**: Spacing tokens differ from Shorts: `--pad-top: 80px` (vs `240px` for Shorts mobile-UI clearance), `--pad-x: 100px`, `--pad-bottom: 80px`.
- **VALIDATE**: Open in browser, confirm `:root` selector resolves and variables are accessible.

### Task 4: CREATE `compositions/scene-hook.html`

- **ACTION**: Author the first sub-composition — hero hook archetype.
- **IMPLEMENT**: `<template id="scene-hook-template">` wrapping a `<div data-composition-id="scene-hook" data-width="1920" data-height="1080">`. Inside: overline ("URGENT" or category label), 100px headline ("YOUR HOOK HERE"), 130px stat slam ("X.X×"), optional 32px sub-line. GSAP timeline registered as `window.__timelines["scene-hook"]` with: overline rises from y:24 over 0.5s `power2.out`, headline rises from y:30 over 0.6s `power3.out` at +0.3s, stat slams from scale:0.85 over 0.5s `back.out(1.4)` at +0.7s, optional sub-line fades at +1.2s.
- **MIRROR**: `templates/shorts/anthropic/index.html:686-755` (entrance pattern), wrapped per `Patterns to Mirror › SUB_COMPOSITION_FILE_PATTERN`.
- **GOTCHA**: All `.from()` calls beyond timeline position 0 should use `immediateRender: false` per the GSAP gotcha.
- **VALIDATE**: `npx hyperframes lint templates/long-form/standard` reports no errors for this file (lint may emit warnings about missing index.html until Task 13 — that's expected).

### Task 5: CREATE `compositions/scene-image-hero.html`

- **ACTION**: Author full-bleed photo backdrop scene archetype.
- **IMPLEMENT**: Per **Patterns to Mirror › REAL_MEDIA — IMAGE_HERO_BACKDROP**. Foreground: 28px overline + 64px headline + 26px body block (left-aligned, max-width 900px). Image is `assets/screenshots/hero-shot.png` (operator drops their own; ship a 1920x1080 placeholder PNG that says "REPLACE WITH HERO IMAGE"). Animations: image fades in over 0.8s `power2.out`, then content rises via 0.08s stagger `power3.out`.
- **MIRROR**: `Patterns to Mirror › REAL_MEDIA — IMAGE_HERO_BACKDROP` snippet.
- **PLACEHOLDER ASSET**: Create `assets/screenshots/hero-shot.png` as a 1920x1080 dark-gray PNG with white "REPLACE WITH HERO IMAGE" text. (Use ImageMagick/skip if not available — document the requirement in README.md instead.)
- **GOTCHA**: Image element gets `class="clip"`. Verify `image-rendering: auto` on the photo (not `pixelated`).
- **VALIDATE**: `npx hyperframes lint templates/long-form/standard` reports no errors for this file.

### Task 6: CREATE `compositions/scene-side-by-side.html`

- **ACTION**: Author A vs B comparison archetype.
- **IMPLEMENT**: Two `LiquidGlassCard`-style cards (max-width 720px each), centered with 40px gap. Above: 28px overline + 56px headline ("BEFORE vs AFTER"). Each card: 32px title, 22px body, optional huge stat. Card A has accent-1 (blue) tint; card B has accent-3 (purple) tint. Animations: cards enter from opposite sides — card A `x: -80 → 0`, card B `x: 80 → 0`, both 0.6s `back.out(1.4)`, simultaneous trigger.
- **MIRROR**: Synthesized from `GoogleCloudNext2026V2/scenes/Scene03TPU.tsx` and `Scene08Defense.tsx`.
- **GOTCHA**: Cards must be flex children of a centered row container. Do NOT use `position: absolute` on the cards themselves (they need to be in normal flow for the gap to work).
- **VALIDATE**: Lint passes.

### Task 7: CREATE `compositions/scene-stat-pill-row.html`

- **ACTION**: Author the receipts archetype — 2 huge color-rotated stats with labels.
- **IMPLEMENT**: Adapt the existing `shared/lib/blocks/stat-pill-row/block.html` for 1920x1080 dimensions. Two pills side-by-side: orange/accent-1 pill with 130px stat number + 22px label below; purple/accent-3 pill same structure. Above: 28px overline + 56px headline.
- **MIRROR**: `shared/lib/blocks/stat-pill-row/block.html` (copy, then adjust `data-width`/`data-height`/font sizes per the recipe.md note that says "for long-form override these dims").
- **GOTCHA**: The library block is 1080x1920 by default. You're CREATING a new file in `compositions/`, not editing the library copy.
- **VALIDATE**: Lint passes.

### Task 8: CREATE `compositions/scene-source-cards.html`

- **ACTION**: Author source-image card row archetype (3 cards in a row).
- **IMPLEMENT**: 3 cards using **Patterns to Mirror › REAL_MEDIA — SOURCE_IMAGE_CARD** pattern. Each card has its own `data-start` 0.5s after the previous (stagger). Cards rotate accents: card 1 = blue, card 2 = cyan, card 3 = purple.
- **PLACEHOLDER ASSETS**: Ship `assets/screenshots/source-1.png`, `source-2.png`, `source-3.png` as placeholder 16:9 dark-gray PNGs with "SOURCE 1/2/3" text. Add a `assets/screenshots/README.md` documenting that operators replace these per video.
- **MIRROR**: Patterns to Mirror snippet + `Gemma4Models/scenes/Scene12Outro.tsx` (Shorts thumbnail row pattern adapted to 16:9 cards).
- **GOTCHA**: `<img>` gets `class="clip"` AND `data-start` AND `data-duration`. Card wrapper div ALSO gets `class="clip"` so the framework manages its visibility.
- **VALIDATE**: Lint passes; `npx hyperframes inspect` reports no overflow.

### Task 9: CREATE `compositions/scene-video-embed.html`

- **ACTION**: Author embedded-video frame archetype.
- **IMPLEMENT**: Per **Patterns to Mirror › REAL_MEDIA — EMBEDDED_VIDEO_FRAME**. Wrapper div is the only `class="clip"` element; `<video>` and matching `<audio>` (for video's audio track) sit inside without `class="clip"`. Wrapper enters via scale 0.92 → 1 over 0.6s `power3.out`. Above the frame: 26px overline + 48px caption headline.
- **PLACEHOLDER ASSET**: Document in README that operators drop a `.mp4` at `assets/clips/demo.mp4`. Ship a tiny placeholder `clips/.gitkeep`. Do NOT ship a video file.
- **MIRROR**: HyperFrames `reference/html-schema.md` video rules + `patterns.md` PiP frame pattern.
- **GOTCHA**: `<video>` MUST have `muted autoplay playsinline preload="auto"`. Never animate video element directly — only wrapper. Audio track is a separate `<audio>` referencing the same MP4 (HyperFrames muxes them at render).
- **VALIDATE**: Lint passes (will warn about missing `assets/clips/demo.mp4` until operator drops one — document this in README).

### Task 10: CREATE `compositions/scene-architecture-stack.html`

- **ACTION**: Author vertical layer-stack archetype.
- **IMPLEMENT**: 5 horizontal layer bars stacked vertically (top to bottom: "User", "API", "Logic", "Data", "Infra" or similar generic labels). Each layer is 1200px wide, 90px tall, with accent-rotated left-border strip. Animations: layers enter top-down with 0.15s stagger, each `from y: 30, opacity: 0, duration: 0.5, ease: power3.out`. After all 5 are visible, a synthesizing 56px headline fades in below ("How it all connects").
- **MIRROR**: `GoogleCloudNext2026V2/scenes/Scene12CTA.tsx` (ArchitectureTower) and `Scene07Data.tsx` (LayeredArchitecture).
- **GOTCHA**: Use `tl.from(".layer", { ..., stagger: 0.15 }, "+=0")` — GSAP's stagger handles per-element delay. Don't manually compute 5 separate trigger times.
- **VALIDATE**: Lint passes.

### Task 11: CREATE `compositions/scene-cta.html`

- **ACTION**: Author the closing CTA archetype.
- **IMPLEMENT**: 3-phase content (sequential, not phase-mutex — one timeline, sequential reveals): (1) FitHeadline debate question (40-72px Inter 900) at t=0 — `expo.out` rise; (2) Comment-prompt pill ("Drop your take in the comments — `<icon>`") + subscribe pill at t=2.5 — `back.out(1.4)`, side-by-side; (3) Optional next-video Shorts thumbnail card at t=5 — pulsing border per `ClaudeSkillsVsAll/scenes/Scene11CTA.tsx:109-118`.
- **MIRROR**: Synthesized from `Gemma4Models/scenes/Scene12Outro.tsx` (debate Q + tier chips) and `ClaudeSkillsVsAll/scenes/Scene11CTA.tsx` (subscribe pulse).
- **PLACEHOLDER ASSET**: `assets/screenshots/next-video-thumbnail.png` (16:9 placeholder).
- **GOTCHA**: Subscribe pulse uses `repeat: 4, yoyo: true` (NOT `repeat: -1`) per the deterministic-only rule. Calculate finite repeats: `Math.ceil(scene_duration / pulse_cycle)`.
- **VALIDATE**: Lint passes.

### Task 12: CREATE `compositions/captions.html`

- **ACTION**: Author the captions sub-composition with framework-required attributes.
- **IMPLEMENT**: `<template id="captions-template">` wrapping `<div data-composition-id="captions" data-timeline-role="captions" data-caption-root="true" data-width="1920" data-height="1080">`. Inside: empty container `<div id="caption-area" style="position:absolute;left:50%;bottom:120px;transform:translateX(-50%);max-width:1400px"></div>`. GSAP timeline registered. Document in a comment that caption groups are populated via `npx hyperframes transcribe`.
- **MIRROR**: **Patterns to Mirror › CAPTIONS_SUB_COMPOSITION_ROOT** snippet.
- **GOTCHA**: The `data-timeline-role` and `data-caption-root` attributes are case-sensitive and required.
- **VALIDATE**: Lint passes.

### Task 13: CREATE `index.html` root composition

- **ACTION**: Wire the 8 scenes + captions + audio + persistent overlays into the root.
- **IMPLEMENT**:
  - Root `<div id="root" data-composition-id="main" data-start="0" data-duration="120" data-width="1920" data-height="1080">`.
  - `<link rel="stylesheet" href="tokens/long-form.css">` in `<head>`.
  - 8 sub-composition wrapper divs per **Patterns to Mirror › SUB_COMPOSITION_WIRING_IN_ROOT**, each with its own `data-start` (0, 12, 32, 55, 70, 90, 105, 115) and `data-track-index="1"`. NO `data-duration` on these wrappers (HyperFrames rule).
  - Captions wrapper at `data-track-index="9"` (above scenes).
  - Top wordmark banner (`<img id="top-banner-logo" src="assets/anthropic-logo-light.svg">`) — re-use shorts pattern, 60px height, top: 30px.
  - Bottom 6px progress bar — copy from `shared/lib/components/progress-bar/`.
  - Background layer with radial wash + 3 drifting shapes + noise overlay — copy ambient pattern from `templates/shorts/anthropic/index.html:560-637` (spawnShapes seeded PRNG with `seedPrefix="long-form-standard"`).
  - Audio: narration `<audio>` (track 2), 3-segment bg-music `<audio>` elements (track 3) per **Patterns to Mirror › AUDIO_BED**.
  - Single `<script>` block at the bottom: register root timeline, add scene labels, run `crossfadeScenes()` between adjacent scenes, run `animateShapeDrift()` and ambient breath, and finally `tl.set({}, {}, 120)` to pad timeline.
- **MIRROR**: `templates/shorts/anthropic/index.html` (whole file as structural template) + new patterns above.
- **GOTCHA**: Audio elements get `data-start/duration/track-index` but NEVER `class="clip"`. Sub-composition wrappers get `data-start/track-index` but NEVER `data-duration` (sub-comp's internal timeline defines its own length).
- **VALIDATE**: `npx hyperframes lint templates/long-form/standard` reports 0 errors. Some warnings about missing audio files (`narration.wav`, `bg-music-*.mp3`) are EXPECTED since this is a template, not a real video — document in README that operators drop these.

### Task 14: CREATE persistent-overlay logo

- **ACTION**: Copy a default light-theme logo to `templates/long-form/standard/assets/`.
- **IMPLEMENT**: `cp shared/logos/anthropic-logo-light.svg templates/long-form/standard/assets/anthropic-logo-light.svg` (or whichever brand the operator most often defaults to). Document in README that this is swappable.
- **MIRROR**: `templates/shorts/anthropic/index.html:455-462` (logo wiring); same path convention.
- **GOTCHA**: Logo must be a LOCAL copy in `assets/`, not a `../../shared/logos/` reference (HyperFrames rejects out-of-project paths).
- **VALIDATE**: `ls templates/long-form/standard/assets/anthropic-logo-light.svg` exists.

### Task 15: CREATE `DESIGN.md`

- **ACTION**: Author the per-template design system spec.
- **IMPLEMENT**: Mirror `templates/shorts/anthropic/DESIGN.md` structure. Sections: Color tokens (table from `tokens/long-form.css`), Type scale (overline/headline/stat/body/mono with px sizes + weights + letter-spacing), Motion language (easing table from **Patterns to Mirror**, stagger timing 80-140ms body / 200-280ms cards), Surface detail (border 1px, border-radius 12-20px, box-shadow patterns), Audio bed (volume caps, multi-segment bg-music levels), Anti-patterns ("no elastic/bounce", "no `repeat: -1`", "no `position:absolute; top:Npx` on phase-content — use padding", "never animate `<video>` directly — wrapper only").
- **MIRROR**: `templates/shorts/anthropic/DESIGN.md` (whole file).
- **VALIDATE**: Markdown lint or visual inspection.

### Task 16: CREATE `README.md` (template spawn workflow)

- **ACTION**: Author the spawn instructions for this template.
- **IMPLEMENT**: Mirror `templates/shorts/anthropic/README.md` structure. Sections: What this template ships (table of 8 scene archetypes with use-for column), Spawn-a-new-video workflow (`cp -r templates/long-form/standard videos/<slug>` → edit meta.json → drop narration → `npx hyperframes lint/preview/render`), Lib provenance (note that this is the canonical generic baseline for `templates/long-form/`), Customizing per video (CSS variables on `:root` swap palette; per-scene accent rotation), Logos (point at `shared/logos/` catalog), Adding more scenes (duplicate one of the 8 sub-comp files, add a new wrapper in index.html, add a label, extend `data-duration` on root, re-run lint), Adding narration (drop at `audio/narration.wav`, run `npx hyperframes transcribe` to populate `compositions/captions.html`), Adding bg-music (3-segment hook/body/cta convention with volume caps), Adding SFX (`bash scripts/sync-video-sfx.sh videos/<slug>` with `sfx-cues.txt`).
- **MIRROR**: `templates/shorts/anthropic/README.md` (whole file).
- **VALIDATE**: Markdown is render-able; all referenced commands work when copy-pasted.

### Task 17: UPDATE `templates/long-form/README.md`

- **ACTION**: Replace the "TBD" status block with the catalog entry for `standard/`.
- **IMPLEMENT**: Edit lines 5-7 (the "Status: No long-form templates yet" block) to read:
  ```
  > **Status:** First template shipped — `templates/long-form/standard/` is the generic baseline.
  > Future variants (`dynamous`, `news-explainer`, `tutorial`) build on top of it.
  ```
  Add a "Available templates" table below the existing "How long-form differs from shorts" section listing `standard/` with one-line description.
- **MIRROR**: `templates/shorts/` directory layout pattern (parent README catalogs the variants).
- **VALIDATE**: Read the updated file end-to-end; ensure no broken links.

### Task 18: CREATE `shared/lib/visual-styles/long-form-standard.md` + library token + MANIFEST update

- **ACTION**: Add the named visual-style fragment + library token + catalog entry.
- **IMPLEMENT**:
  - `shared/lib/visual-styles/long-form-standard.md`: Mirror `shared/lib/visual-styles/anthropic-dark.md` structure. Document the dark-navy + 4-accent-rotation palette, type scale, easing table, surface detail, and pacing baseline (10s hook, 20-30s pattern interrupts, CTA at 60-70% mark per vidIQ research).
  - `shared/lib/tokens/long-form-standard.css`: byte-identical copy of `templates/long-form/standard/tokens/long-form.css` (so future templates can pick it up via copy-from per the lib consumption rule).
  - `shared/lib/MANIFEST.md`: append entries under "Visual Styles" and "Tokens" for the new files. Mirror existing entry format.
- **MIRROR**: `shared/lib/visual-styles/anthropic-dark.md`, `shared/lib/tokens/anthropic-dark.css`, `shared/lib/MANIFEST.md`
- **VALIDATE**: `cat shared/lib/MANIFEST.md` shows the new entries; `ls shared/lib/visual-styles/ shared/lib/tokens/` shows the new files.

---

## Testing Strategy

### Validation Per File

| File                                                                                  | Validation                                                                                                        |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `templates/long-form/standard/meta.json`                                              | `node -e "JSON.parse(require('fs').readFileSync('templates/long-form/standard/meta.json'))"` returns no error      |
| `templates/long-form/standard/hyperframes.json`                                       | Same JSON parse check; matches `templates/shorts/anthropic/hyperframes.json` byte-for-byte except trailing newline |
| `templates/long-form/standard/index.html`                                             | `npx hyperframes lint templates/long-form/standard` — 0 errors                                                    |
| `templates/long-form/standard/compositions/*.html`                                    | Each lints clean as part of the project lint run                                                                  |
| `templates/long-form/standard/tokens/long-form.css`                                   | Loaded via `<link>` in index.html; `:root` variables resolve in browser DevTools Computed view                     |
| Render test                                                                           | `npx hyperframes render templates/long-form/standard --quality draft` produces an MP4 (with a black/silent track for missing narration — that's fine for the template demo) |

### Edge Cases Checklist

- [ ] Template renders with NO narration.wav (audio elements reference missing files — should warn, not error)
- [ ] Template renders with NO `assets/clips/demo.mp4` (video-embed scene becomes silent/black for that segment — should warn, not error)
- [ ] Template renders with NO `bg-music-*.mp3` (bg-music segments become silent — should warn, not error)
- [ ] Each sub-composition lints clean in isolation (`npx hyperframes lint` scoped to a single file is not supported, but each file should self-validate when the project lints)
- [ ] All 8 scene timelines register on `window.__timelines` (DevTools console: `Object.keys(window.__timelines)` returns `["main", "scene-hook", "scene-image-hero", "scene-side-by-side", "scene-stat-pill-row", "scene-source-cards", "scene-video-embed", "scene-architecture-stack", "scene-cta", "captions"]`)
- [ ] Crossfades between scenes do not flash the wrong scene at `t=0` (the `immediateRender: false` discipline)
- [ ] WCAG contrast: `npx hyperframes validate templates/long-form/standard` reports no AAA failures on body text, no AA failures on headlines

---

## Validation Commands

### Level 1: STATIC_ANALYSIS (HyperFrames lint)

```bash
npx hyperframes lint templates/long-form/standard
```

**EXPECT**: Exit 0, 0 errors. Warnings allowed for: missing audio files (`narration.wav`, `bg-music-*.mp3`, `clips/demo.mp4`), missing per-video screenshots (operator-supplied). Document expected warnings in README.

### Level 2: WCAG_AND_LAYOUT_AUDIT

```bash
npx hyperframes validate templates/long-form/standard
npx hyperframes inspect templates/long-form/standard
```

**EXPECT**: `validate` passes WCAG audit; `inspect` reports no element overflow at 1920x1080.

### Level 3: PREVIEW_SMOKE_TEST

```bash
npx hyperframes preview templates/long-form/standard
```

**EXPECT**: Studio editor opens at 1920x1080. Scrubbing through the 120s timeline shows: scene-hook (0-12s), crossfade, scene-image-hero (12-32s), crossfade, … through scene-cta (115-120s). Console: `Object.keys(window.__timelines).length === 10` (main + 8 scenes + captions).

### Level 4: DRAFT_RENDER

```bash
npx hyperframes render templates/long-form/standard --quality draft --workers 4 -o /tmp/long-form-template-smoke.mp4
```

**EXPECT**: MP4 file produced; ~10-30s render time at draft quality on a workstation. Open and visually verify all 8 scenes appear in order with crossfades.

### Level 5: SPAWN_VIDEO_DRY_RUN

```bash
cp -r templates/long-form/standard /tmp/test-spawn
sed -i 's/REPLACE_WITH_VIDEO_SLUG/test-spawn/' /tmp/test-spawn/meta.json
sed -i 's/REPLACE_WITH_VIDEO_NAME/Test Spawn/' /tmp/test-spawn/meta.json
npx hyperframes lint /tmp/test-spawn
```

**EXPECT**: Lint clean. Confirms the template is self-contained and copy-friendly. Then `rm -rf /tmp/test-spawn`.

### Level 6: MANUAL_VALIDATION

- [ ] Open `templates/long-form/standard/index.html` in a browser via `npx hyperframes preview`. Scrub to t=0, t=15, t=40, t=60, t=80, t=100, t=118. Each timestamp should show the expected scene content (no flashing, no blank screens during transitions).
- [ ] Verify all 8 scene archetypes are visually distinct (no two scenes look identical).
- [ ] Verify the captions sub-composition is empty but the wrapper is wired (DevTools: `document.querySelector('[data-caption-root]')` returns an element).
- [ ] Verify `tokens/long-form.css` is loaded (DevTools Network tab; `:root` variables present in Computed styles).
- [ ] Verify the noise overlay is visible (subtle film-grain texture on top of background).
- [ ] Verify the top wordmark banner is visible at the top center.
- [ ] Verify the bottom 6px progress bar advances during playback.

---

## Acceptance Criteria

- [ ] `templates/long-form/standard/` exists with all 25 files from the **Files to Change** table.
- [ ] `npx hyperframes lint templates/long-form/standard` exits 0 with 0 errors.
- [ ] `npx hyperframes validate templates/long-form/standard` reports no AAA contrast failures and no AA failures on headlines.
- [ ] `npx hyperframes inspect templates/long-form/standard` reports no overflow at 1920x1080.
- [ ] `npx hyperframes preview templates/long-form/standard` opens the studio and scrubs cleanly through 120 seconds.
- [ ] `npx hyperframes render templates/long-form/standard --quality draft` produces a viewable MP4.
- [ ] All 10 expected timeline IDs (`main`, 8 scenes, `captions`) register on `window.__timelines` when the page loads.
- [ ] Spawning a video from the template (`cp -r templates/long-form/standard videos/<slug>`, edit meta.json) lints clean without code changes.
- [ ] `templates/long-form/README.md` is updated to reflect that `standard/` is the canonical baseline.
- [ ] `shared/lib/visual-styles/long-form-standard.md`, `shared/lib/tokens/long-form-standard.css`, and the MANIFEST.md update all land per Task 18.
- [ ] DESIGN.md and README.md mirror the structure of their `templates/shorts/anthropic/` counterparts.
- [ ] No `class="clip"` on `<audio>` or `<video>` elements anywhere in the template (lint enforces this).
- [ ] No `data-duration` on any sub-composition wrapper div (HyperFrames rule).
- [ ] All `tl.from()` calls at timeline position > 5 use `immediateRender: false`.

---

## Completion Checklist

- [ ] Task 1: directory + meta files created
- [ ] Task 2: shape SVGs copied
- [ ] Task 3: tokens/long-form.css authored
- [ ] Task 4: scene-hook.html
- [ ] Task 5: scene-image-hero.html (+ placeholder hero-shot.png)
- [ ] Task 6: scene-side-by-side.html
- [ ] Task 7: scene-stat-pill-row.html (1920x1080 adaptation)
- [ ] Task 8: scene-source-cards.html (+ placeholder source-1/2/3.png)
- [ ] Task 9: scene-video-embed.html
- [ ] Task 10: scene-architecture-stack.html
- [ ] Task 11: scene-cta.html (+ placeholder next-video-thumbnail.png)
- [ ] Task 12: captions.html
- [ ] Task 13: index.html root composition
- [ ] Task 14: anthropic-logo-light.svg copied to assets/
- [ ] Task 15: DESIGN.md
- [ ] Task 16: README.md
- [ ] Task 17: templates/long-form/README.md updated
- [ ] Task 18: shared/lib visual-style + token + MANIFEST update
- [ ] Level 1 lint passes
- [ ] Level 2 validate + inspect pass
- [ ] Level 3 preview opens cleanly
- [ ] Level 4 draft render produces MP4
- [ ] Level 5 spawn dry-run lints clean
- [ ] Level 6 manual validation complete

---

## Risks and Mitigations

| Risk                                                                                                      | Likelihood | Impact | Mitigation                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------- | ---------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linter rejects sub-composition `data-composition-src` pattern (we have no existing example in the repo)   | LOW        | HIGH   | The pattern is documented in HyperFrames `concepts/compositions.md` and `examples.md` confirms 3-file nesting works in built-in templates. If lint fails, fall back to inline sub-templates inside index.html (`<template id="...">` blocks in the same file) — same pattern, no external file. Both are documented as supported. |
| Render produces black frames during scene crossfades                                                      | MEDIUM     | MEDIUM | The `crossfadeScenes()` function uses `visibility: hidden` + opacity transitions. If frames flash black, switch to opacity-only crossfade (drop the `visibility` step). Test on draft render (Level 4) before declaring complete.                                                                                          |
| `<video>` element fails to render in the offline render context                                           | MEDIUM     | MEDIUM | HyperFrames docs confirm `<video>` works with `muted autoplay playsinline preload="auto"`. The existing `videos/anthropic-100b-deal/` doesn't use `<video>` — this is the first template to test it. If render fails, document the limitation in README and ship the scene-video-embed archetype as "placeholder for future support" with a static screenshot fallback. |
| 600s timeline scrubs sluggishly in preview Studio for actual long-form videos                             | MEDIUM     | LOW    | The sub-composition split is the mitigation — root timeline holds ~30 tweens, each scene timeline holds ~20-40, no single timeline exceeds ~50 tweens. Performance docs cap 33ms/frame on individual frames, not on timeline length. If a real 10-min video is slow, profile and optimize per-scene.                                                                  |
| `immediateRender: false` discipline breaks down when authors copy patterns from Shorts (which don't need it because they're 24s) | HIGH       | LOW    | DESIGN.md explicitly documents this gotcha as anti-pattern #1. Add a lint-rule request to HyperFrames upstream if friction continues. For now, code review catches it.                                                                                                                                                                                                |
| Captions facility (`data-timeline-role="captions"`, `data-caption-root="true"`) doesn't work as documented | LOW        | MEDIUM | Verify against a HyperFrames built-in example (warm-grain / swiss-grid / play-mode) before authoring captions.html. If the docs are wrong, fall back to plain DOM caption groups with `data-start`/`data-duration` like any other clip.                                                                                                                              |
| Adding two more files (visual-style + token to shared/lib) creates drift from the in-template versions    | MEDIUM     | LOW    | Both are byte-identical copies at creation time. Add a comment at the top of each lib file: "Canonical version lives in `templates/long-form/standard/tokens/long-form.css`. Sync with `scripts/sync-shared-tokens.sh` if added." Future enhancement: a sync script.                                                                                                  |

---

## Notes

### Relationship to existing plans

- `.claude/PRPs/plans/claude-code-version-longform-template.plan.md` is the *Claude Code update video* plan. After this generic baseline ships, that plan can be revisited and likely simplified to "fork `templates/long-form/standard/` to `templates/long-form/claude-code-version/`, swap palette to GitHub-dark, replace 8 scene archetypes with the Claude-Code-specific ones (terminal window, version branding, feature card grid, etc.)". Doing the generic baseline first removes work from that plan.
- `.claude/PRPs/plans/dynamous-shorts-promotion.plan.md` is unrelated (Shorts-specific).

### Why "standard" as the variant name

The user wants this to be "the generic long-form template to use for most videos." `standard` reads as the unmarked default; future named variants (`dynamous`, `news-explainer`, `tutorial`, `claude-code-version`) are marked as specialty. Alternative names considered and rejected: `default` (reserved-feeling), `base` (sounds incomplete), `generic` (true but flat). `standard` is the term used in the user's brief ("most videos") and it's how the existing `templates/shorts/anthropic/` is structured (named by aesthetic, not by purpose, but the long-form baseline is the most-used one so naming it `standard` makes the catalog read clearly).

### Future enhancements (out of scope, but record for future plans)

1. **Shared-lib block extraction**: After 3+ long-form templates are built, extract the most-reused scene archetypes (likely `image-hero`, `source-cards`, `cta`) into `shared/lib/blocks/` so future templates pick them up via copy-from.
2. **Render preset config**: Add a `templates/long-form/standard/.hyperframesrc` (if HyperFrames supports it) that pins `--quality high --crf 16 --workers 4 --fps 30` so operators don't have to remember flags.
3. **Captions auto-generation hook**: A `scripts/generate-captions.sh` that takes `audio/narration.wav` + `transcript.json` and populates `compositions/captions.html` with caption groups.
4. **Multi-segment bg-music sourcing**: A `scripts/source-bg-music.sh` that pulls 3 clips from a royalty-free library (Pixabay/Artlist) keyed by mood (hook/body/cta).
5. **Alternate aspect-ratio variants**: 1080p horizontal is the baseline; future `templates/long-form/standard-4k/` and `templates/long-form/standard-9x16-square/` variants if the channel needs them.

### Confidence rationale

The plan is detailed enough to execute one-shot because:
- Every scene archetype maps to specific patterns either already in the repo (Shorts template, shared/lib) or in the three Remotion reference projects (with clear translation rules to GSAP).
- The HyperFrames docs research surfaced 3 critical gotchas (no `class="clip"` on audio/video; no `data-duration` on sub-comp wrappers; `immediateRender: false` for long timelines) — all called out explicitly.
- Tasks are independently lintable; failures are caught early.
- Render is testable at draft quality without needing real narration audio (silent MP4 is acceptable proof of structure).
- Risks all have explicit fallbacks documented.

The single highest-uncertainty item is the captions facility (`data-timeline-role="captions"` is documented but I couldn't verify it against a working built-in example). Risk #6 covers the fallback path.
