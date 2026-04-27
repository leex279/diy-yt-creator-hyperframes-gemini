# Feature: Shared Visual Library (`shared/lib/`)

## Summary

Stand up a repo-local **copy-from** library at `shared/lib/` that holds reusable HyperFrames building blocks (block compositions, paste-in components, CSS partials, GSAP timelines, palette tokens, named visual styles, SFX bed). Templates and per-video compositions consume the library by **copying snippets in at authoring time**, not by referencing the path at runtime — because HyperFrames' bundler and preview server actively reject filesystem paths that escape the project directory (`isSafePath`/`safePath` in `@hyperframes/core`). The diy-yt-creator playbook gains a "lib pick" step; the upstream `.agents/skills/**` is never modified.

## User Story

As a **video author working in this repo**
I want **one canonical place to keep generic cards, effects, animations, palettes, and styles**
So that **new templates and one-off videos can reuse them without duplicating CSS/JS across `templates/` folders, and without forking the upstream HyperFrames skill**.

## Problem Statement

Today, every reusable visual idea (stat-pill, timeline-card, phase-crossfade, hero-slam shake, accent-rotation system, the four-phase-mutex layout, the `--orange/--purple/--blue/--green` accent token contract) lives **inside `templates/shorts/anthropic/index.html`** as inline CSS + GSAP. There is no path to:

1. Extract a "card" or "effect" without copying the entire template
2. Reuse those building blocks from a future template (e.g. `templates/long-form/<style>/`) without duplication
3. Share named visual-style presets across videos without each video declaring its own palette + motion rules from scratch
4. Distinguish "generic ingredient" (cards, effects, palettes) from "specific recipe" (template aesthetic)

Templates currently do double duty as both *aesthetic* (Anthropic dark-stage) AND *ingredient library*. As we add templates, this guarantees drift.

## Solution Statement

Introduce `shared/lib/` as a **manifested, agent-readable library** of generic HyperFrames building blocks. Each entry is one self-contained directory with an HTML file (block or component), an optional `recipe.md` (how to wire it), and per-entry metadata in a top-level `MANIFEST.md`. The diy-yt-creator playbook reads the manifest, picks entries that fit the script, and **copies them into the spawned `videos/<slug>/`** at authoring time. Templates remain thin "recipes" that pre-import the lib entries appropriate for that aesthetic; the lib is the ingredients.

We do NOT use `data-composition-src="../../shared/lib/..."` at runtime — the HyperFrames bundler will silently drop those paths (see Risks). All sharing is copy-time.

We optionally publish `shared/lib/` to a public GitHub raw URL later (Phase B) so `hyperframes add <name>` resolves against our private registry. Phase A is filesystem-only.

## Metadata

| Field            | Value                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| Type             | NEW_CAPABILITY                                                                                                       |
| Complexity       | MEDIUM                                                                                                               |
| Systems Affected | `shared/`, `templates/shorts/anthropic/`, `.claude/skills/diy-yt-creator/`, `scripts/sync-shared-assets.sh`, `CLAUDE.md`, `README.md` |
| Dependencies     | None new. Uses existing HyperFrames CLI (`lint`, `inspect`, `validate`, `preview`) at versions already in repo.       |
| Estimated Tasks  | 14 (Phase A) + 3 optional (Phase B)                                                                                  |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        BEFORE — everything inline in templates                ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   templates/shorts/anthropic/index.html  (470+ lines: layout + 4 phases +    ║
║   ┌──────────────────────────────────┐   stat-pill CSS + tl-card CSS +       ║
║   │  CSS tokens (--orange, --purple) │   phase-crossfade JS + hero-slam      ║
║   │  .stat-pill.{orange|purple|...}  │   shake + ambient breath + progress)  ║
║   │  .tl-card.{orange|purple|...}    │                                        ║
║   │  .phase + crossfade JS           │                                        ║
║   │  hero-slam shake JS              │                                        ║
║   │  GSAP entrance patterns          │                                        ║
║   └──────────────────────────────────┘                                        ║
║                    │                                                          ║
║                    ▼                                                          ║
║   videos/<slug>/  (full template copy — every video re-ships every CSS rule)  ║
║                                                                               ║
║   PAIN: a new "Velvet Standard" template would have to re-author              ║
║   stat-pill, tl-card, phase-crossfade from scratch (or copy/diverge from     ║
║   anthropic's HTML). No way to extract just "the slam-word effect."           ║
║   shared/ today only has logos/ — no CSS/JS sharing.                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                       AFTER — shared/lib/ is the ingredient pantry            ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   shared/lib/                                                                 ║
║   ├── MANIFEST.md           ← agent-readable catalog of all entries          ║
║   ├── tokens/               ← :root CSS variable sets (palettes)             ║
║   │   └── anthropic-dark.css                                                 ║
║   ├── blocks/               ← standalone <template>-wrapped sub-comps        ║
║   │   ├── stat-pill-row/    ← {block.html, recipe.md, preview.png}           ║
║   │   ├── timeline-cards/                                                    ║
║   │   ├── url-cta/                                                           ║
║   │   └── chapter-card/     ← (new entry, not in any template yet)           ║
║   ├── components/           ← paste-in HTML+CSS+JS snippets                  ║
║   │   ├── ambient-radial/                                                    ║
║   │   ├── progress-bar/                                                      ║
║   │   ├── grain-overlay/                                                     ║
║   │   └── shimmer-sweep/                                                     ║
║   ├── effects/              ← pure GSAP recipes (no markup)                  ║
║   │   ├── hero-slam-shake.js                                                 ║
║   │   ├── phase-crossfade.js                                                 ║
║   │   └── stat-pill-pop.js                                                   ║
║   ├── visual-styles/        ← named style presets (DESIGN.md fragments)     ║
║   │   ├── anthropic-dark.md                                                  ║
║   │   ├── swiss-pulse.md                                                     ║
║   │   └── shadow-cut.md                                                      ║
║   └── README.md                                                              ║
║                                                                               ║
║   FLOW (per video, agent-driven):                                             ║
║                                                                               ║
║       1. /diy-yt-creator:new-anthropic-short  spawns videos/<slug>/          ║
║           │                                                                  ║
║           ▼                                                                  ║
║       2. agent reads shared/lib/MANIFEST.md, picks blocks/components         ║
║           that fit the script (e.g. stat-pill-row + timeline-cards)          ║
║           │                                                                  ║
║           ▼                                                                  ║
║       3. agent COPIES the chosen entry's files into                          ║
║           videos/<slug>/compositions/, components/components/, or            ║
║           inline-merges into index.html (per recipe.md)                      ║
║           │                                                                  ║
║           ▼                                                                  ║
║       4. lint / inspect / preview run on videos/<slug>/ — every file         ║
║           used at runtime is inside the project dir (bundler-safe)           ║
║                                                                               ║
║   VALUE:                                                                      ║
║   - new template = pick from lib instead of copy-from-anthropic               ║
║   - new video = pick a styled block + reuse the effect, swap palette          ║
║   - generic cards/effects/animations live ONCE                                ║
║   - .agents/skills/** stays untouched (upstream-clean)                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                                                | Before                                     | After                                                                                             | User Impact                                  |
| ------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `shared/`                                                | only `logos/` + `ASSETS.md` + `README.md`  | also `lib/` with manifest + blocks + components + effects + tokens + visual-styles                | One pantry for generic visuals               |
| `templates/shorts/anthropic/index.html`                  | self-contained, every CSS/JS rule inline   | references lib via `<!-- SOURCE: shared/lib/blocks/stat-pill-row -->` comments; CSS partials moved to `shared/lib/tokens/` and pasted at template-build time | Template becomes a "recipe", not a kitchen sink |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`   | step 8 = edit content only                  | new step 8.5 = "Lib pick: read `shared/lib/MANIFEST.md`, copy chosen entries into `videos/<slug>/`" | Agent picks ingredients per script           |
| `scripts/sync-shared-assets.sh` (extension of existing)  | tracks `shared/logos/` → `shared/ASSETS.md` | also walks `shared/lib/` and updates `shared/lib/MANIFEST.md` between sentinel comments           | One sync pass updates both inventories        |
| `videos/<slug>/`                                         | gets template copy, edits content          | gets template copy + lib copies merged in; `compositions/` may have lib blocks                    | Still self-contained (bundler-safe)          |

---

## Mandatory Reading

**Implementation agent MUST read these before starting:**

| Priority | File                                                                                       | Lines       | Why Read This                                                                              |
| -------- | ------------------------------------------------------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------ |
| P0       | `templates/shorts/anthropic/index.html`                                                    | 27-46, 103-378 | The canonical CSS+GSAP we're extracting. Tokens at 27-46; component CSS through 378.       |
| P0       | `shared/README.md`                                                                          | 1-45        | Existing `shared/` conventions (path table, naming rules, single-source-of-truth principle). |
| P0       | `shared/ASSETS.md`                                                                          | 1-12        | Sentinel-comment auto-sync pattern that `MANIFEST.md` will mirror.                          |
| P0       | `.claude/skills/diy-yt-creator/new-anthropic-short.md`                                     | 41-49, 156-184 | Spawn step (cp -r) and edit-step structure that the new "lib pick" step plugs into.        |
| P0       | `.agents/skills/hyperframes/SKILL.md`                                                       | 24-39, 138-162, 198-222 | Visual Identity Gate (where named styles plug in), composition structure, non-negotiables.  |
| P1       | `.agents/skills/hyperframes-registry/references/wiring-blocks.md`                          | all         | `data-composition-src` mechanics — blocks copied into `compositions/` follow this contract. |
| P1       | `.agents/skills/hyperframes-registry/references/wiring-components.md`                      | 3-14        | Components are paste-in by design (matches our copy-time approach exactly).                  |
| P1       | `.agents/skills/hyperframes/visual-styles.md`                                               | 1-212       | Reference structure for `shared/lib/visual-styles/<name>.md` entries.                       |
| P2       | `templates/shorts/anthropic/DESIGN.md`                                                      | 1-137       | Section taxonomy (Canvas, Colors, Typography, Layout, Motion, Surface, SFX, Anti-patterns) — DESIGN.md fragments in `shared/lib/visual-styles/` will mirror this. |
| P2       | `skills-lock.json`                                                                          | 1-50        | Confirms `.agents/skills/**` is sync-managed → off-limits.                                  |

**External Documentation:**

| Source                                                                                                            | Section                                       | Why Needed                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [HyperFrames llms.txt](https://hyperframes.heygen.com/llms.txt)                                                   | (machine index — find current pages)         | Discover canonical doc URLs. Do NOT guess.                                                                                            |
| [HyperFrames CLI source `packages/core/src/studio-api/helpers/safePath.ts` on `heygen-com/hyperframes` GitHub]    | `isSafePath` function                         | Proves paths outside project root are 404'd at preview. **Architectural gate — copy-time only, never runtime reference.**             |
| [HyperFrames bundler source `packages/core/src/compiler/htmlBundler.ts`]                                         | `safePath` function                           | Proves bundler also rejects out-of-project paths at render. Same gate as preview.                                                      |
| [HyperFrames CLI `packages/cli/src/commands/add.ts`]                                                              | `runAdd` function                             | If we go to Phase B, this is what consumes `hyperframes.json:registry`. Format published at `docs/schema/registry.json`.              |

---

## Patterns to Mirror

**SHARED_DIRECTORY_README_HEADER:**

```markdown
<!-- SOURCE: shared/README.md:1-12 -->
# shared/

Reusable assets that any video or template in this repo can reference. The
shared library is one source of truth — add a file once, link it from many
videos.

| Consumer                                | Path to a logo                              |
| --------------------------------------- | ------------------------------------------- |
| `videos/<slug>/index.html`              | `../../shared/logos/<file>`                 |
| `templates/shorts/<style>/index.html`   | `../../../shared/logos/<file>`              |
| `templates/long-form/<style>/index.html`| `../../../shared/logos/<file>`              |

HyperFrames lint accepts these cross-project relative paths — verified against
`npx hyperframes lint`.
```

(Mirror this structure for `shared/lib/README.md`, but replace the path table with a copy-time API table — see Task 2.)

**ASSETS_SENTINEL_COMMENT_PATTERN (for `MANIFEST.md`):**

```markdown
<!-- SOURCE: shared/ASSETS.md:1-12 -->
<!-- AUTO-MAINTAINED — do not delete the table boundary HTML comments
  scripts/sync-shared-assets.sh runs on every PostToolUse hook.
  Workflow:
    - Walks shared/ for non-md, non-dotfile assets
    - Appends new files between the markers with blank descriptions
    - Marks files removed from disk with [REMOVED] in the description -->

# Assets

<!-- ASSETS:BEGIN -->
| File | Description |
|------|-------------|
| logos/anthropic-logo-light.svg | Anthropic wordmark, dark-stage |
<!-- ASSETS:END -->
```

(Mirror sentinel-comment pattern for `shared/lib/MANIFEST.md` — but with kind/description/tags columns and per-section tables for blocks / components / effects / styles.)

**BLOCK_COMPOSITION_STRUCTURE (sub-composition):**

```html
<!-- SOURCE: .agents/skills/hyperframes/SKILL.md:144-162 -->
<template id="my-comp-template">
  <div data-composition-id="my-comp" data-width="1920" data-height="1080">
    <!-- content -->
    <style>
      [data-composition-id="my-comp"] {
        /* scoped styles */
      }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      // tweens...
      window.__timelines["my-comp"] = tl;
    </script>
  </div>
</template>
```

(Every `shared/lib/blocks/<name>/block.html` MUST follow this exact wrapper. The block's `data-composition-id` MUST match its directory name.)

**STAT_PILL_CSS (the canonical card pattern to extract first):**

```css
/* SOURCE: templates/shorts/anthropic/index.html:203-241 */
.stat-pill {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 460px;
  min-height: 300px;
  padding: 44px 24px;
  border-radius: 24px;
}
.stat-pill.orange {
  background: linear-gradient(135deg, rgba(233,116,88,0.20), rgba(233,116,88,0.06));
  border: 2px solid rgba(233,116,88,0.40);
  box-shadow: 0 14px 36px rgba(233,116,88,0.20);
}
/* ...(.purple, .blue, .green follow same pattern, swapping rgba)... */
.stat-num {
  font-family: var(--sans);
  font-weight: 900;
  font-size: 180px;
  line-height: 0.9;
  letter-spacing: -4px;
  font-variant-numeric: tabular-nums lining-nums;
}
```

(Block file `shared/lib/blocks/stat-pill-row/block.html` will contain this CSS scoped to `[data-composition-id="stat-pill-row"]` plus a 2-pill row of `<div class="stat-pill orange">` + `<div class="stat-pill purple">` and the entrance tweens from `index.html:535-536`.)

**PHASE_CROSSFADE_GSAP_RECIPE:**

```js
// SOURCE: templates/shorts/anthropic/index.html:520-527
// Reusable phase-crossfade — pure GSAP, no markup.
// Usage: phaseCrossfade(tl, "#phase1", "#phase2", { at: 5.6, blur: 20 });
function phaseCrossfade(tl, fromSel, toSel, { at, blur = 20, duration = 0.4 } = {}) {
  tl.to(fromSel, { filter: `blur(${blur}px)`, scale: 1.04, duration: 0.5, ease: "power1.in" }, at);
  tl.to(fromSel, { opacity: 0, duration, ease: "power1.in" }, at + 0.3);
  tl.set(fromSel, { visibility: "hidden" }, at + 0.7);
  tl.set(toSel, { filter: `blur(${blur}px)`, scale: 0.97, opacity: 0, visibility: "visible" }, at + 0.4);
  tl.to(toSel, { opacity: 1, duration: 0.3, ease: "power1.inOut", overwrite: "auto" }, at + 0.4);
  tl.to(toSel, { filter: "blur(0px)", scale: 1, duration: 0.5, ease: "power1.out", overwrite: "auto" }, at + 0.6);
}
```

(File: `shared/lib/effects/phase-crossfade.js`. Function-style so a video can paste-in and call from its `<script>`. No GSAP-CDN tag — caller already has GSAP loaded.)

**VISUAL_STYLE_FRAGMENT_STRUCTURE:**

```markdown
<!-- SOURCE: .agents/skills/hyperframes/visual-styles.md:25-41 -->
# Anthropic Dark — Postmortem Stage

**Mood:** Confident, premium engineering | **Best for:** Anthropic launches, postmortems, dev-tool reveals

## Tokens
[shared/lib/tokens/anthropic-dark.css]

## Typography
- Hero / slam: Inter 900, letter-spacing -4px, 240px (Shorts) / 180px (Long)
- Headline: Inter 800-900, letter-spacing -1px, 64px
- Overline (mono): JetBrains Mono 700, UPPERCASE, letter-spacing 5-7px, 36px
- ...

## Motion Signature
- `back.out(1.7)` for slam-in hero / stat pills
- `power3.out` for headlines
- `power2.out` for body / chips
- AVOID elastic, bounce — toy-like for this brand

## Suggested Lib Picks
- blocks: stat-pill-row, timeline-cards, url-cta
- components: progress-bar, ambient-radial, top-banner-wordmark
- effects: hero-slam-shake, phase-crossfade, stat-pill-pop

## What NOT to Do
- No light canvas
- No more than one accent per phase
- No serif headlines
- No `<br>` in content text
```

(File: `shared/lib/visual-styles/anthropic-dark.md`. References lib entries by name. Mirror this for every named style.)

**MANIFEST_TABLE_ROW_STRUCTURE:**

```markdown
<!-- SOURCE: shape inferred from .agents/skills/hyperframes-registry/references/discovery.md:39-54 -->
| Name             | Kind       | Description                                          | Dimensions   | Duration | Tags                            | Path                                    |
| ---------------- | ---------- | ---------------------------------------------------- | ------------ | -------- | ------------------------------- | --------------------------------------- |
| stat-pill-row    | block      | Two color-rotated huge-number stat pills             | 1080x1920    | n/a      | stats, numbers, vertical        | blocks/stat-pill-row/                   |
| ambient-radial   | component  | Slow-breathing radial accent wash                    | full-bleed   | —        | background, ambient, decorative | components/ambient-radial/              |
| phase-crossfade  | effect     | Blur+opacity scene transition (0.4s) — function form | —            | 0.4s     | transition, gsap                | effects/phase-crossfade.js              |
| anthropic-dark   | style      | Dark-stage, Claude orange, Inter 900 hero            | —            | —        | dark, premium, tech             | visual-styles/anthropic-dark.md         |
```

---

## Files to Change

| File                                                                               | Action       | Justification                                                                  |
| ---------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------ |
| `shared/lib/`                                                                      | CREATE (dir) | New library root.                                                              |
| `shared/lib/README.md`                                                              | CREATE       | Authoring + consumption guide — mirrors `shared/README.md` shape.              |
| `shared/lib/MANIFEST.md`                                                            | CREATE       | Auto-maintained catalog (sentinel-comment pattern from `shared/ASSETS.md`).    |
| `shared/lib/tokens/anthropic-dark.css`                                              | CREATE       | Extracted `:root` CSS vars from `templates/shorts/anthropic/index.html:27-46`. |
| `shared/lib/blocks/stat-pill-row/block.html`                                        | CREATE       | Extract from `index.html:203-241` + `535-536` (entrance).                       |
| `shared/lib/blocks/stat-pill-row/recipe.md`                                         | CREATE       | How to wire in (data-attrs, accent slot, palette dependency).                  |
| `shared/lib/blocks/timeline-cards/block.html`                                       | CREATE       | Extract from `index.html:260-331` + `552-554`.                                 |
| `shared/lib/blocks/timeline-cards/recipe.md`                                        | CREATE       | Wiring + accent rotation rules.                                                |
| `shared/lib/blocks/url-cta/block.html`                                              | CREATE       | Extract from `index.html:342-378` + entrance tweens.                           |
| `shared/lib/blocks/url-cta/recipe.md`                                               | CREATE       | Wiring.                                                                        |
| `shared/lib/components/ambient-radial/component.html`                               | CREATE       | Extract from `index.html:49-57` + breath tween at 493-497.                     |
| `shared/lib/components/progress-bar/component.html`                                 | CREATE       | Extract from `index.html:82-96` + tween at 499-502.                            |
| `shared/lib/components/top-banner-wordmark/component.html`                          | CREATE       | Extract from `index.html:63-79` + entrance at 504-505.                         |
| `shared/lib/effects/phase-crossfade.js`                                             | CREATE       | Function form of `index.html:520-527` (parameterized).                         |
| `shared/lib/effects/hero-slam-shake.js`                                             | CREATE       | Function form of `index.html:514-517` (4-tick shake from a `slam_t` arg).      |
| `shared/lib/effects/stat-pill-pop.js`                                               | CREATE       | Function form of `index.html:535-536`.                                          |
| `shared/lib/visual-styles/anthropic-dark.md`                                        | CREATE       | Style fragment + lib-pick list. References tokens/anthropic-dark.css.         |
| `scripts/sync-shared-lib.sh`                                                        | CREATE       | Walks `shared/lib/` and rewrites the sentinel-bounded table in `MANIFEST.md`.  |
| `.claude/settings.json`                                                              | UPDATE       | Add the new sync script to the existing PostToolUse + SessionStart hooks (the same hook that runs `sync-shared-assets.sh`). |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                              | UPDATE       | Insert step 8.5 (Lib pick), reference `shared/lib/MANIFEST.md` and `shared/lib/visual-styles/anthropic-dark.md`. Add Don't: "Never reference `shared/lib/` paths via `data-composition-src` at runtime — copy in." |
| `templates/shorts/anthropic/index.html`                                              | UPDATE       | Add `<!-- SOURCE: shared/lib/blocks/stat-pill-row -->` provenance comments above each section that was extracted. Do NOT inline-import — template stays self-contained for bundler safety. |
| `templates/shorts/anthropic/README.md`                                              | UPDATE       | Add "This template's CSS/JS originates in `shared/lib/`. To author a new template, start from a lib pick list rather than copying this file." |
| `CLAUDE.md`                                                                          | UPDATE       | Add `shared/lib/` row to the "Project Structure" tree and a one-line note that lib is copy-from, not reference-from. |
| `README.md`                                                                          | UPDATE       | Mention `shared/lib/` exists and link to its README.                           |

---

## NOT Building (Scope Limits)

- **Phase B (self-hosted registry on GitHub raw URL)** — possible but deferred. Not in this plan. Files for Phase B (a `registry.json` + per-item `registry-item.json` shaped per `docs/schema/registry-item.json` upstream) would be co-located in `shared/lib/` later.
- **Modifying `.agents/skills/**`** — never. That tree is hash-locked in `skills-lock.json` and re-synced from `heygen-com/hyperframes`.
- **Runtime references to `shared/lib/` from videos** — not allowed. HyperFrames `isSafePath` rejects out-of-project paths at preview AND render. All sharing is copy-time.
- **`hyperframes add` integration in Phase A** — Phase A is filesystem-only. Phase B introduces the registry.
- **Refactoring `templates/shorts/anthropic/index.html` to import lib at build-time via a build script** — too invasive for v1. Template adds provenance comments only; lib is the source of truth for *new* templates, not retrofitted into the existing one.
- **Visual-style preset library covering all 8 upstream styles** — Phase A ships only `anthropic-dark.md` (the one we already have evidence for). Add others as future videos demand them.
- **Multi-aesthetic palette tokens beyond `anthropic-dark.css`** — Phase A is one token file. Add `swiss-pulse.css`, `shadow-cut.css` etc. as follow-on PRs.
- **A `npx hyperframes` integration that lints `shared/lib/` itself** — `shared/lib/blocks/<name>/block.html` files are fragments, not full HyperFrames projects. Linting them as projects would fail. We rely on copy-time integration tests (lint the *consuming* video).

---

## Step-by-Step Tasks

Execute top-to-bottom. Each task is independently verifiable.

### Task 1: CREATE `shared/lib/README.md`

- **ACTION**: New file, ~80 lines.
- **IMPLEMENT**:
  - Header: "shared/lib/ — generic visual building blocks"
  - Sections: "What's here" (kinds: blocks/components/effects/tokens/visual-styles), "How to use" (copy-time only — explicit warning that runtime `../../shared/lib/...` paths fail), "How to add an entry", "Naming conventions", "MANIFEST.md is auto-maintained"
- **MIRROR**: `shared/README.md:1-45` — same tone, same path-table style, but replace path table with kind→consume-pattern table.
- **GOTCHA**: Document the `isSafePath` rejection explicitly. Future agents WILL try to use `data-composition-src="../../shared/lib/..."` — the README must say "this is silently dropped at render; copy the file in instead."
- **VALIDATE**: `cat shared/lib/README.md | head -1` returns the header. No HTML/CSS code in this file.

### Task 2: CREATE `shared/lib/MANIFEST.md`

- **ACTION**: New file with sentinel-comment scaffolding. Empty tables initially — Task 14 populates.
- **IMPLEMENT**:
  - Top sentinel comment block matching `shared/ASSETS.md:1-12` (auto-maintained, do not edit by hand).
  - Four sections: `## Blocks`, `## Components`, `## Effects`, `## Visual Styles`. Each has its own `<!-- LIB:BLOCKS:BEGIN --> ... <!-- LIB:BLOCKS:END -->` markers (and analogous for the other three kinds).
  - Each table has columns: Name | Description | Dimensions/Duration | Tags | Path.
- **MIRROR**: `shared/ASSETS.md:1-12` — sentinel comment shape; `shared/ASSETS.md:14+` table shape.
- **GOTCHA**: `MANIFEST.md` must NOT be hand-edited inside the sentinels. Comments above sentinels say so.
- **VALIDATE**: File exists; `grep -c "LIB:.*:BEGIN" shared/lib/MANIFEST.md` returns 4.

### Task 3: CREATE `shared/lib/tokens/anthropic-dark.css`

- **ACTION**: New file. Lift `:root`/`#root` CSS vars from template index.
- **IMPLEMENT**:
  - Copy lines 27-46 of `templates/shorts/anthropic/index.html` verbatim, but scope to `:root` (so paste targets work without `#root` selector). Add a top header comment naming the source: `/* shared/lib/tokens/anthropic-dark.css — extracted from templates/shorts/anthropic/index.html:27-46 */`.
  - Variables: `--bg`, `--card`, `--text`, `--text-dim`, `--orange`, `--purple`, `--blue`, `--green`, `--red`, `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--mono`, `--sans`.
- **MIRROR**: `templates/shorts/anthropic/index.html:27-46`.
- **GOTCHA**: `:root` not `#root` — the template's `#root` is a specific div; tokens should apply at document root so any consumer inherits.
- **VALIDATE**: `npx hyperframes lint videos/<any-existing-slug>` still passes (this file is not yet referenced by any video — should be a no-op).

### Task 4: CREATE `shared/lib/blocks/stat-pill-row/block.html` + `recipe.md`

- **ACTION**: Two new files.
- **IMPLEMENT** (`block.html`):
  - `<template>`-wrapped sub-composition per `.agents/skills/hyperframes/SKILL.md:144-162`.
  - `data-composition-id="stat-pill-row"`, `data-width="1080"`, `data-height="1920"` (Shorts default — recipe explains how to override).
  - Two `<div class="stat-pill <accent>">` children (default accents: `orange`, `purple`).
  - `<style>` block scoped to `[data-composition-id="stat-pill-row"]` containing the rules from `templates/shorts/anthropic/index.html:203-241` (extract verbatim, change selector scoping).
  - `<script>`: GSAP CDN + paused timeline + entrance tweens from index.html:535-536, registered as `window.__timelines["stat-pill-row"]`.
  - Top-of-file comment: `<!-- SOURCE: templates/shorts/anthropic/index.html:203-241, 535-536 -->`.
- **IMPLEMENT** (`recipe.md`):
  - "What it does", "Wiring (host index.html)", "Required tokens (anthropic-dark.css or equivalent)", "Slots (.stat-num, .stat-label per pill)", "Customizing accent class", "Lint rules to keep clean".
- **MIRROR**: SKILL.md:144-162 (template wrapper); index.html:203-241 (CSS); SKILL.md:198-222 (non-negotiables — verify shake/repeat/sync rules respected).
- **GOTCHA**: Do NOT use `repeat: -1` anywhere. Do NOT use `class="clip"` on container — that's the host's wrapper concern (per SKILL.md key rule 2). Block content is NOT a clip itself; it's a sub-composition.
- **VALIDATE**: Spawn a test video, copy `block.html` into its `compositions/`, wire the host `<div data-composition-src=...>`, run `npx hyperframes lint videos/<test>` → 0 errors.

### Task 5: CREATE `shared/lib/blocks/timeline-cards/block.html` + `recipe.md`

- **ACTION**: Two new files.
- **IMPLEMENT** (`block.html`): Mirror Task 4. Source CSS is `index.html:260-331`; entrance tweens from `index.html:552-554` (3 cards, 450ms stagger, `back.out(1.5)`). Three accent classes per default: `orange`, `purple`, `blue`. `data-composition-id="timeline-cards"`.
- **IMPLEMENT** (`recipe.md`): same shape as Task 4 + accent-rotation rule ("no two adjacent cards same accent" — mirror DESIGN.md:38-39).
- **MIRROR**: index.html:260-331, 552-554; DESIGN.md:38-39.
- **GOTCHA**: `tl-date` color is `var(--bg)` (near-black) on solid accent fill — depends on tokens being loaded. Recipe must list tokens dependency.
- **VALIDATE**: Same as Task 4 — copy into a test video, lint clean.

### Task 6: CREATE `shared/lib/blocks/url-cta/block.html` + `recipe.md`

- **ACTION**: Two files. Source: `index.html:342-378`. `data-composition-id="url-cta"`.
- **MIRROR**: index.html:342-378 + 4th-phase entrance pattern.
- **VALIDATE**: Same lint test as Task 4.

### Task 7: CREATE `shared/lib/components/ambient-radial/component.html`

- **ACTION**: New file. Components are paste-in (per wiring-components.md:3-14), so format is HTML + `<style>` + `<script>` snippet WITHOUT a `<template>` wrapper.
- **IMPLEMENT**:
  - Top comment block listing: target placement (host's `<div data-composition-id>` root), CSS to merge into host `<style>`, JS lines to add to host timeline (the breathing tween from `index.html:493-497`).
  - HTML: `<div id="ambient" data-no-capture></div>` (the `data-no-capture` attribute matches `.agents/skills/hyperframes/references/transitions.md:104` rules so shader-transition videos don't try to texture it).
  - CSS: extract from `index.html:49-57`.
  - JS: a function `addAmbientBreath(tl, { duration }) { tl.fromTo("#ambient", ...); }`.
- **MIRROR**: Upstream component pattern in registry (e.g. how `grain-overlay` is structured) — see `.agents/skills/hyperframes-registry/references/wiring-components.md:3-14`.
- **GOTCHA**: `repeat: -1` is BANNED. The breath tween in the source uses `yoyo: true, repeat: 1` with `duration: total_duration / 2`. Document this in the top comment so callers don't simplify it to infinite-repeat.
- **VALIDATE**: Snippet's CSS+JS pasted into a test video; lint clean.

### Task 8: CREATE `shared/lib/components/progress-bar/component.html`

- **ACTION**: New file (paste-in component shape per Task 7).
- **IMPLEMENT**: HTML from `index.html:398`; CSS from `index.html:82-96`; JS function `addProgressBar(tl, { width, totalDuration })` from `index.html:499-502`.
- **MIRROR**: same pattern as Task 7.
- **VALIDATE**: same as Task 7.

### Task 9: CREATE `shared/lib/components/top-banner-wordmark/component.html`

- **ACTION**: New file.
- **IMPLEMENT**: HTML from `index.html:393-395` (with `src` placeholder `__LOGO_SRC__` and a comment noting consumers replace with `../../shared/logos/<file>`); CSS from `index.html:63-79`; entrance JS function from `index.html:504-505`.
- **MIRROR**: same as Task 7. Reference `shared/README.md:6-9` path table for the logo path the consumer fills in.
- **GOTCHA**: This is the one place where the logo path *is* a runtime reference to `../../shared/logos/...` — and it works because logos are static `<img src>` only, served as files (not bundled compositions). The `isSafePath` check in preview also rejects logos outside the project... actually wait — investigate before coding. If logos at `../../shared/logos/...` work today only because the existing video copied them locally to `assets/`, the recipe must instruct: copy the logo into `videos/<slug>/assets/` AND set `src="assets/<file>"`. Check `videos/claude-connectors-everyday-life/index.html:416` to confirm current behavior — it shows `src="assets/anthropic-logo-light.svg"` (local copy). Do the same here.
- **VALIDATE**: Test by following the recipe — copy a logo into a test video, lint clean.

### Task 10: CREATE `shared/lib/effects/phase-crossfade.js`, `hero-slam-shake.js`, `stat-pill-pop.js`

- **ACTION**: Three .js files (effects are pure GSAP recipes, no markup).
- **IMPLEMENT**:
  - `phase-crossfade.js`: function form per "Patterns to Mirror → PHASE_CROSSFADE_GSAP_RECIPE" above. Source: `index.html:520-527`.
  - `hero-slam-shake.js`: function `heroSlamShake(tl, sel, slamT)` that emits the four `tl.to(sel, { x: ... })` ticks at offsets `[slamT, slamT+0.05, slamT+0.10, slamT+0.15]`. Source: `index.html:514-517`.
  - `stat-pill-pop.js`: function `statPillPop(tl, sel, at)` — single `tl.from(sel, { scale: 0.85, opacity: 0, duration: 0.6, ease: "back.out(1.6)" }, at)`. Source: `index.html:535`.
  - Each file has a top JSDoc comment with `// SOURCE:` and a `// USAGE:` example.
- **MIRROR**: existing GSAP patterns in `index.html`.
- **GOTCHA**: No `repeat: -1`. No `Math.random()`. No `Date.now()`. No `await`/`async`/`setTimeout` (per SKILL.md rule on synchronous timeline construction at 207-209).
- **VALIDATE**: Paste each function into a test video's `<script>`, call from the timeline, lint clean.

### Task 11: CREATE `shared/lib/visual-styles/anthropic-dark.md`

- **ACTION**: New file, ~50 lines.
- **IMPLEMENT**: Per "Patterns to Mirror → VISUAL_STYLE_FRAGMENT_STRUCTURE" above. Sections: name+mood, Tokens (link to `tokens/anthropic-dark.css`), Typography, Motion Signature, Suggested Lib Picks (block + component + effect names), What NOT to Do.
- **MIRROR**: `.agents/skills/hyperframes/visual-styles.md:25-41` (Swiss Pulse entry shape) + `templates/shorts/anthropic/DESIGN.md` (section taxonomy).
- **GOTCHA**: Suggested Lib Picks must reference real entries created in Tasks 4-10. Don't list a block that doesn't exist yet.
- **VALIDATE**: Cross-check every name in Suggested Lib Picks resolves to a real entry in `MANIFEST.md` after Task 14 runs.

### Task 12: CREATE `scripts/sync-shared-lib.sh`

- **ACTION**: New shell script (bash, runs on Windows under Git Bash and Linux/macOS).
- **IMPLEMENT**:
  - Walks `shared/lib/` for entries.
  - Detects kind from path: `blocks/<name>/block.html` → block; `components/<name>/component.html` → component; `effects/<name>.js` → effect; `visual-styles/<name>.md` → style.
  - Reads first comment line (or first H1 for `.md`) of each entry as Description.
  - Writes a sorted Markdown table per kind into `shared/lib/MANIFEST.md` between the matching `<!-- LIB:<KIND>:BEGIN -->` / `<!-- LIB:<KIND>:END -->` sentinels.
  - Marks files removed from disk with `[REMOVED]` in the Description column (mirrors `sync-shared-assets.sh`).
- **MIRROR**: `scripts/sync-shared-assets.sh` (read it first to copy structure, awk/sed approach, error handling).
- **GOTCHA**: Do NOT delete or move sentinels. If sentinels are missing, exit 1 with a clear error. Run with `set -euo pipefail`.
- **VALIDATE**: `bash scripts/sync-shared-lib.sh && grep -c "stat-pill-row" shared/lib/MANIFEST.md` returns 1 (after Task 4 ran).

### Task 13: UPDATE `.claude/settings.json`

- **ACTION**: Edit. Add `scripts/sync-shared-lib.sh` to the existing PostToolUse + SessionStart hook chain that already runs `scripts/sync-shared-assets.sh`.
- **IMPLEMENT**: Read current `.claude/settings.json`. Find the hook entry that invokes `sync-shared-assets.sh`. Add a sibling hook that invokes `sync-shared-lib.sh` with the same triggers.
- **MIRROR**: existing hook entry in `.claude/settings.json`.
- **GOTCHA**: Don't break any existing hook. Run `npx hyperframes lint videos/<existing-slug>` after edit to confirm no regression.
- **VALIDATE**: Trigger any tool use; observe both scripts ran (look for table updates in both `shared/ASSETS.md` and `shared/lib/MANIFEST.md`).

### Task 14: RUN `scripts/sync-shared-lib.sh`

- **ACTION**: Execute the script.
- **VALIDATE**: `shared/lib/MANIFEST.md` now lists every entry created in Tasks 3-11 in its kind-appropriate section.

### Task 15: UPDATE `.claude/skills/diy-yt-creator/new-anthropic-short.md`

- **ACTION**: Edit. Insert a new step 8.5 ("Lib pick"). Add to "Don'ts" list.
- **IMPLEMENT**:
  - **New step 8.5 — Lib pick** (insert between current step 8 "Edit `videos/<slug>/index.html`" and step 9 "Lint"). Wording:
    > Read `shared/lib/MANIFEST.md` and `shared/lib/visual-styles/anthropic-dark.md`. Pick blocks, components, and effects that fit your script.
    > For each pick:
    >   - **Block**: copy `shared/lib/blocks/<name>/block.html` to `videos/<slug>/compositions/<name>.html`. Wire it in `index.html` per the recipe.
    >   - **Component**: read `shared/lib/components/<name>/component.html`. Merge HTML/CSS/JS into `index.html` per the top-of-file comment.
    >   - **Effect**: read `shared/lib/effects/<name>.js`. Paste the function into `index.html`'s `<script>`. Call from the timeline.
    > **Never** reference shared/lib paths via `data-composition-src` at runtime. The bundler rejects out-of-project paths.
  - **New Don't**: "Never reference `shared/lib/` paths from `data-composition-src`, `<img src>`, `<audio src>`, `<video src>`, or `<link href>` at runtime — the HyperFrames bundler silently drops out-of-project paths. Always copy the file into `videos/<slug>/`."
- **MIRROR**: existing step structure in `new-anthropic-short.md:156-184`.
- **GOTCHA**: Existing step 8.3 already tells the agent to set `#top-banner-logo` `src` to `../../shared/logos/anthropic-logo-light.svg`. Per the bundler-rejection finding, this also fails at preview/render. **Cross-reference the actual deployed video** at `videos/claude-connectors-everyday-life/index.html:416` — it uses local `src="assets/anthropic-logo-light.svg"`. The playbook's instruction at line 163-164 is wrong in production. Update step 8.3 to "copy the chosen logo from `shared/logos/<file>` into `videos/<slug>/assets/<file>` and set `src="assets/<file>"`." This is an opportunistic fix — it lands on this PR because the lib doc is correcting the same misconception. Keep it scoped: only change step 8.3 wording to match the working pattern.
- **VALIDATE**: Re-run the playbook end-to-end on a tiny test topic; final video lints clean and previews without 404s on the logo.

### Task 16: UPDATE `templates/shorts/anthropic/index.html`

- **ACTION**: Edit. Add provenance comments only — do NOT change any CSS/JS.
- **IMPLEMENT**: Above each extracted block, insert a comment naming the lib entry:
  - Above `:root` (line 27): `/* TOKENS: shared/lib/tokens/anthropic-dark.css */`
  - Above `.stat-pill` (line 203): `/* BLOCK: shared/lib/blocks/stat-pill-row/ */`
  - Above `.tl-card` (line 260): `/* BLOCK: shared/lib/blocks/timeline-cards/ */`
  - Above `#p4-url` (line 342): `/* BLOCK: shared/lib/blocks/url-cta/ */`
  - Above `#ambient` (line 49): `/* COMPONENT: shared/lib/components/ambient-radial/ */`
  - Above `#progress-track` (line 82): `/* COMPONENT: shared/lib/components/progress-bar/ */`
  - Above `#top-banner` (line 63): `/* COMPONENT: shared/lib/components/top-banner-wordmark/ */`
  - Above the phase-crossfade GSAP block (line 520): `// EFFECT: shared/lib/effects/phase-crossfade.js`
  - Above the slam-shake (line 514): `// EFFECT: shared/lib/effects/hero-slam-shake.js`
  - Above the stat-pill pop (line 535): `// EFFECT: shared/lib/effects/stat-pill-pop.js`
- **GOTCHA**: Comments only. Don't touch a single CSS rule or JS line. Template stays bundler-safe and self-contained.
- **VALIDATE**: `git diff templates/shorts/anthropic/index.html` shows ONLY added comment lines. `npx hyperframes lint templates/shorts/anthropic` (or test by spawning a video from it) passes unchanged.

### Task 17: UPDATE `templates/shorts/anthropic/README.md`, `CLAUDE.md`, `README.md`

- **ACTION**: Edit each.
- **IMPLEMENT**:
  - `templates/shorts/anthropic/README.md`: After "Customizing per video" section, add a "Lib provenance" paragraph: "This template's CSS/JS is mirrored in `shared/lib/`. New templates should be authored by picking from the lib instead of copying this file. The provenance comments in `index.html` (e.g. `/* BLOCK: shared/lib/blocks/stat-pill-row/ */`) point at the canonical source."
  - `CLAUDE.md`: Add `└── shared/lib/  ← reusable blocks, components, effects, palettes (copy-from)` to the project structure tree (line 67-71 area). Add a one-line note under "Adding a new video" referencing `shared/lib/MANIFEST.md`.
  - `README.md`: One-line addition: "Reusable visual building blocks live at [`shared/lib/`](shared/lib/README.md)."
- **MIRROR**: existing tone of each file. Brief, declarative.
- **VALIDATE**: `cat CLAUDE.md | grep "shared/lib"` returns ≥ 1 line.

---

## Testing Strategy

### Spawn-and-pick smoke test

After all 17 tasks complete:

```bash
# 1. Spawn a fresh test video from the existing template
cp -r templates/shorts/anthropic videos/test-shared-lib

# 2. Update meta.json with a unique id
# (manual edit: { "id": "test-shared-lib", "name": "Test Shared Lib" })

# 3. Sanity-check no regression
npx hyperframes lint videos/test-shared-lib
npx hyperframes inspect videos/test-shared-lib
# Both should pass clean — proves Tasks 16 (provenance comments) and 13 (hooks) didn't break the pipeline.

# 4. Copy a lib block into the test video and wire it
cp shared/lib/blocks/stat-pill-row/block.html videos/test-shared-lib/compositions/stat-pill-row.html
# Wire in index.html: a <div data-composition-id="stat-pill-row" data-composition-src="compositions/stat-pill-row.html" data-start="..." data-duration="..." data-track-index="..."></div>

# 5. Re-lint
npx hyperframes lint videos/test-shared-lib
# Should still pass clean.

# 6. Preview manually
npx hyperframes preview videos/test-shared-lib
# Confirm the lib block renders in browser, animates correctly, no 404s in DevTools console.

# 7. Clean up
rm -rf videos/test-shared-lib
```

### Negative test (proves the bundler-rejection rule)

```bash
# 1. Spawn another test video
cp -r templates/shorts/anthropic videos/test-bad-ref

# 2. Edit its index.html — replace stat-pill-row sub-comp wiring with:
#    <div data-composition-id="stat-pill-row"
#         data-composition-src="../../shared/lib/blocks/stat-pill-row/block.html"
#         data-start="0" data-duration="6" data-track-index="1"
#         data-width="1080" data-height="1920"></div>

# 3. Lint will pass (no rule checks data-composition-src existence)
npx hyperframes lint videos/test-bad-ref   # passes — but this is misleading

# 4. Preview will show empty div, console warning [Bundler] Composition file not found
npx hyperframes preview videos/test-bad-ref

# 5. Document the negative finding in shared/lib/README.md (already in Task 1)
# 6. Clean up
rm -rf videos/test-bad-ref
```

This negative test only needs to run ONCE during initial implementation — to verify the documented constraint is real. After that, the README captures it; future runs don't need to repeat.

### Edge Cases Checklist

- [ ] Lib block referenced via correct `compositions/<name>.html` path → renders + lints clean
- [ ] Lib block referenced via `../../shared/lib/...` path → bundler drops, empty div (negative test)
- [ ] Effect function pasted twice into the same composition → no GSAP overwrite warnings (verify `overwrite: "auto"` is on the affected tweens)
- [ ] Component pasted into a composition that doesn't import `tokens/anthropic-dark.css` → CSS variables undefined, fall back to UA defaults gracefully (component uses literal hex fallbacks where critical)
- [ ] `MANIFEST.md` regenerated after a lib entry is renamed → old row marked `[REMOVED]`, new row appended
- [ ] Lib block with `data-composition-id` mismatching its directory name → recipe.md says directory and id must match; sync script flags mismatch (Phase B nice-to-have, not blocker for Phase A)

---

## Validation Commands

### Level 1: STATIC_ANALYSIS

```bash
npx hyperframes lint videos/test-shared-lib
npx hyperframes validate videos/test-shared-lib   # adds WCAG contrast
```

**EXPECT**: Exit 0, no errors.

### Level 2: VISUAL_INSPECT

```bash
npx hyperframes inspect videos/test-shared-lib
```

**EXPECT**: No layout overflow on lib-sourced blocks. If overflow appears, it's a recipe bug — recipe.md must specify `max-width` rules.

### Level 3: PREVIEW (manual / browser)

```bash
npx hyperframes preview videos/test-shared-lib
```

**EXPECT**: Studio loads. DevTools console clean (no 404s, no "Composition file not found"). Animation runs as in source template.

### Level 4: NEGATIVE_BUNDLER_TEST (one-time)

See "Negative test" above. Confirms bundler rejection of out-of-project paths.

### Level 5: SYNC_HOOK_INTEGRATION

```bash
# After any tool use that touches shared/lib/, the hook should re-sync MANIFEST.md
# Trigger a tool use (e.g. Edit on shared/lib/effects/phase-crossfade.js)
# Then:
git diff shared/lib/MANIFEST.md
```

**EXPECT**: Auto-sync ran; if any entry changed, MANIFEST table updated between sentinels.

### Level 6: NO_UPSTREAM_DRIFT

```bash
git diff .agents/skills/
git diff skills-lock.json
```

**EXPECT**: Empty diffs. Upstream skills must be untouched.

---

## Acceptance Criteria

- [ ] `shared/lib/` exists with README, MANIFEST, tokens/, blocks/ (3), components/ (3), effects/ (3), visual-styles/ (1)
- [ ] `MANIFEST.md` is auto-regenerated by `scripts/sync-shared-lib.sh` and the hook fires on PostToolUse
- [ ] `templates/shorts/anthropic/index.html` carries provenance comments but is otherwise byte-identical
- [ ] `templates/shorts/anthropic/index.html` still lints + previews clean (no template regression)
- [ ] `.claude/skills/diy-yt-creator/new-anthropic-short.md` step 8.5 documents the lib-pick flow
- [ ] `.claude/skills/diy-yt-creator/new-anthropic-short.md` step 8.3 corrected to copy logo locally (not reference via `../../shared/logos/`)
- [ ] `.claude/skills/diy-yt-creator/new-anthropic-short.md` "Don'ts" lists the runtime-reference prohibition
- [ ] CLAUDE.md, README.md, template README acknowledge `shared/lib/`
- [ ] Spawn-and-pick smoke test passes
- [ ] Negative bundler test confirms `../../shared/lib/...` is silently rejected
- [ ] `git diff .agents/skills/ skills-lock.json` is empty

---

## Completion Checklist

- [ ] Tasks 1-17 completed in order
- [ ] After each task, `npx hyperframes lint` on the existing video (`claude-connectors-everyday-life`) still passes — proves no regression
- [ ] After all tasks, smoke test passes
- [ ] Negative bundler test run once and documented
- [ ] Hook integration verified
- [ ] No `.agents/skills/` or `skills-lock.json` diff
- [ ] PR description links the manifest, names the three blocks / three components / three effects / one style shipped

---

## Risks and Mitigations

| Risk                                                                                                                            | Likelihood | Impact   | Mitigation                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Future agents try to use `data-composition-src="../../shared/lib/..."` and get silent failures (empty div, console warning).    | HIGH       | MEDIUM   | Three docs explicitly forbid it: `shared/lib/README.md`, `new-anthropic-short.md` Don'ts, every `recipe.md`. Negative test in this plan proves the failure mode.                                       |
| `templates/shorts/anthropic/index.html` and `shared/lib/` drift over time (someone edits the template's stat-pill, lib stays).  | MEDIUM     | MEDIUM   | Provenance comments (`/* BLOCK: shared/lib/blocks/stat-pill-row/ */`) make drift detectable in code review. A future task could add a sync-checker script. Out of scope for v1.                          |
| `sync-shared-lib.sh` corrupts `MANIFEST.md` if sentinels are damaged.                                                           | LOW        | LOW      | Script exits non-zero on missing sentinels (Task 12 GOTCHA). Hook surfaces the failure; `git diff` shows the corruption.                                                                                |
| Hook integration in `.claude/settings.json` breaks an unrelated agent flow.                                                     | LOW        | MEDIUM   | Task 13 GOTCHA: post-edit lint check on the existing video catches it.                                                                                                                                  |
| Logo-path correction in step 8.3 is not actually necessary and changing it confuses past videos.                                | LOW        | LOW      | Validate before changing: read `videos/claude-connectors-everyday-life/index.html:416` (already does `src="assets/..."`). The change makes the playbook match production. If unsure, leave step 8.3 untouched and document the divergence in lib README. |
| Phase B (self-hosted registry) requires public GitHub raw URL — ties library updates to a remote.                               | —          | —        | Out of scope for this plan. Phase A is filesystem-only. Phase B is a separate decision later.                                                                                                            |
| `isSafePath` enforcement changes upstream (relaxed in a future HyperFrames release).                                            | LOW        | LOW      | If relaxed, runtime references become possible — could simplify a future v2. Until then, copy-time is the safe contract.                                                                                |

---

## Notes

**Why copy-time not reference-time, restated for the implementer**: HyperFrames `@hyperframes/core` ships `isSafePath` (preview server) and `safePath` (bundler) which both reject any path outside `project.dir`. This is a deliberate security boundary in the framework — not a bug. Cross-project references appear to work in `<img src>` because they happen to 404 silently and most templates don't notice. Empirical proof: `videos/claude-connectors-everyday-life/index.html:416` uses a *local* `src="assets/anthropic-logo-light.svg"`, not the `../../shared/logos/...` path the playbook says to use. The playbook is wrong; the working code is right; this plan corrects the playbook.

**Why blocks AND components AND effects** (three kinds, not one): they map to genuinely different consumption modes documented by the framework — blocks are sub-compositions loaded via `data-composition-src`, components are paste-in fragments (`.agents/skills/hyperframes-registry/references/wiring-components.md:3-14`), effects are pure GSAP recipes with no markup. Treating them as one kind would force every effect to ship a `<template>` wrapper it doesn't need.

**Why a manifest, not just a directory listing**: an agent picking from the library at authoring time needs a single read to see what's available. `shared/lib/MANIFEST.md` is one fetch; a directory walk is many. The sentinel-comment auto-sync pattern is already established in `shared/ASSETS.md` — we mirror it.

**Future Phase B**: publish `shared/lib/` to a static URL (GitHub raw or a CDN) with a `registry.json` per the schema at `https://hyperframes.heygen.com/schema/registry.json`. Set the user's local `hyperframes.json:registry` to point at it. Then `hyperframes add stat-pill-row` resolves against our private registry. Filesystem layout stays identical — only adds two manifest files. Defer until a third video has reused a Phase A lib entry.

**Why we update the playbook's step 8.3 (logo path) opportunistically**: it's a documented production bug surfacing right next to the lib doc work. Fixing it inline keeps the lib README consistent ("never use `../../shared/...` at runtime") with the playbook ("here's how step 8.3 works in practice"). If reviewer pushback says "scope creep," split it into a follow-up PR — the lib work doesn't depend on the fix.
