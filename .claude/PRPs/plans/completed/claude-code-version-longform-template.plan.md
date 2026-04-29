# Feature: Claude Code Version Update — Long-Form Template (Variant)

## Summary

Fork the just-shipped `templates/long-form/standard/` baseline into a new variant `templates/long-form/claude-code-version/` for Claude Code release-update videos (1920x1080, ~3-5 min). The variant swaps the standard navy palette for the Claude Code GitHub-dark palette, replaces 3 of the 8 scene archetypes with Claude Code-specific scenes (stats opener, highlights grid, terminal command), adds a persistent VersionBranding overlay (top-right Anthropic + Claude Code logos + bottom-right GitHub URL), and ships a `/claude-code-version` slash command that automates per-release content extraction (changelog → script → TTS → composition fill).

This plan is now significantly smaller than the original draft because the standard template already provides: sub-composition split + crossfade orchestration, token system (`--accent-1..4` + warn/stat), 3-segment BG music pattern, logo copy-from-shared workflow, captions sub-comp, SFX sync via `sfx-cues.txt`, and lint-clean baseline. We do NOT need to author shared/lib blocks for this variant — most archetypes are already covered by `compositions/scene-*.html`. Forking + swapping is the canonical workflow per `templates/long-form/README.md:54-63`.

## User Story

As the channel operator (info@smartcode.diy)
I want to spawn a new Claude Code version update video with one slash command + minimal manual edits
So that every Claude Code release ships a consistent, branded, SEO-optimized YouTube long-form within ~30 minutes of the changelog dropping.

## Problem Statement

The old Remotion-based `diy-yt-creator/src/ClaudeCodeV21112-118/` produced 50+ Claude Code version update videos using a `/claude-code-version` slash command. The new HyperFrames repo now has the generic `templates/long-form/standard/` baseline (shipped 2026-04-28), but no Claude Code branded variant exists yet, and no slash command drives the per-release workflow. Without these, the next Claude Code release blocks video production until the operator manually forks the standard template and reimplements Claude Code visuals from scratch each time.

## Solution Statement

Three-step variant:

1. **Fork** `templates/long-form/standard/` → `templates/long-form/claude-code-version/` per `templates/long-form/README.md:54-63`. Update `meta.json`, `README.md`, `DESIGN.md` to document the variant.
2. **Swap palette + scene mix**:
   - Override 6 CSS variables in `tokens/long-form.css` to the Claude Code GitHub-dark palette (`--bg #0D1117`, `--accent-1 #58A6FF`, `--accent-2 #06B6D4`, `--accent-3 #A371F7`, `--accent-4 #3FB950`, `--accent-warn #F78166`, `--accent-stat #F78166`).
   - Replace `scene-source-cards.html` with `scene-stats-opener.html` (3 huge stat counters: features / fixes / improved).
   - Replace `scene-architecture-stack.html` with `scene-feature-cards.html` (vertical-stacked or 3x2 highlights grid via configurable mode).
   - Replace `scene-image-hero.html` with `scene-terminal.html` (macOS terminal chrome with code block).
   - Keep `scene-hook.html`, `scene-side-by-side.html`, `scene-stat-pill-row.html`, `scene-video-embed.html`, `captions.html`.
   - Adapt `scene-cta.html` so the CTA shows `$ claude update` in a terminal block instead of a generic next-video card.
   - Add a paste-in **VersionBranding** overlay block in `index.html` (top-right Anthropic + Claude Code logos at opacity 0.7, bottom-right `github.com/anthropics/claude-code/releases | vX.Y.Z` line).
3. **Ship the orchestration command** at `.claude/commands/diy-yt-creator/claude-code-version.md` that drives per-release research, scriptwriting, TTS, composition fill, lint, and render. Port the 10-step workflow from the old project's `claude-code-version.md`, swapping Remotion CLI calls for `npx hyperframes tts/transcribe/lint/preview/render`.

## Metadata

| Field | Value |
| --- | --- |
| Type | NEW_CAPABILITY (variant of existing template) |
| Complexity | MEDIUM (was HIGH before standard template shipped) |
| Systems Affected | `templates/long-form/`, `.claude/commands/diy-yt-creator/`, `.claude/skills/diy-yt-creator/` |
| Dependencies | `templates/long-form/standard/` (existing baseline), HyperFrames CLI (existing), GSAP 3.14.2 (existing CDN), `shared/logos/anthropic-logo-light.svg` + `shared/logos/claude-code-logo-light.svg` (existing — verified in git status), `shared/audio/sfx/*` (existing) |
| Estimated Tasks | 12 |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  CURRENT — generic standard/ template exists, but no Claude Code variant.    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Operator path for the next release:                                          ║
║                                                                               ║
║  ┌──────────────────┐    ┌──────────────────────┐    ┌─────────────────────┐ ║
║  │  v2.1.NN drops   │──► │ Manual fork standard │──► │ Manual rewire scenes│ ║
║  │  changelog       │    │ Manual swap palette  │    │ Manual write script │ ║
║  └──────────────────┘    │ Manual draft script  │    │ Manual TTS gen      │ ║
║                          │ Manual TTS gen       │    │ Manual fill content │ ║
║                          │ ...every. time.      │    │ Manual render       │ ║
║                          └──────────────────────┘    └─────────────────────┘ ║
║                                                                               ║
║  PAIN_POINT_1: Manual fork + palette swap repeated per release.              ║
║  PAIN_POINT_2: No automation for changelog → scene category derivation.      ║
║  PAIN_POINT_3: VersionBranding (top-right logos) absent from standard.       ║
║  PAIN_POINT_4: Standard's source-cards / architecture-stack don't fit the    ║
║                "list of fixes/features" content shape that Claude Code       ║
║                releases produce.                                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  AFTER — one slash command spawns a fully-wired video for the new release.  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌──────────────────┐    ┌────────────────────┐    ┌───────────────────────┐ ║
║  │  v2.1.NN URL     │──► │  /claude-code-     │──► │  videos/claude-code-  │ ║
║  │  (or bare tag)   │    │  version v2.1.NN   │    │  v2NN/                │ ║
║  └──────────────────┘    └────────────────────┘    │   ├── index.html      │ ║
║                                  │                  │   ├── compositions/   │ ║
║                                  │ Steps:           │   │     scene-*.html  │ ║
║                                  │ 1 fetch changelog│   ├── audio/          │ ║
║                                  │   (marckrenn +   │   │     narration.wav │ ║
║                                  │    official)     │   ├── transcript.json │ ║
║                                  │ 2 derive scenes  │   ├── meta.json       │ ║
║                                  │ 3 ask user:      │   ├── tokens/         │ ║
║                                  │   highlights /   │   │     long-form.css │ ║
║                                  │   watchnext      │   ├── DESIGN.md       │ ║
║                                  │ 4 write script   │   └── youtube-        │ ║
║                                  │ 5 npx tts        │       description.md  │ ║
║                                  │ 6 npx transcribe │                       │ ║
║                                  │ 7 fork variant   │                       │ ║
║                                  │ 8 fill content   │                       │ ║
║                                  │ 9 lint+inspect   │                       │ ║
║                                  ▼                  │                       │ ║
║                          ┌────────────────────┐    │                       │ ║
║                          │ npx hyperframes    │    │                       │ ║
║                          │ render             │──► out/long.mp4 (1920x1080)║
║                          └────────────────────┘                              ║
║                                                                               ║
║  USER_FLOW:                                                                  ║
║   1. /claude-code-version v2.1.NN                                            ║
║   2. Confirm derived scene categories + WatchNext + highlights               ║
║   3. Approve generated narration + render                                    ║
║                                                                               ║
║  VALUE_ADD:                                                                  ║
║    + ~30 minutes from changelog drop to YouTube-ready MP4                    ║
║    + Variant inherits ALL standard improvements (lint, captions, BG music,   ║
║      crossfades) — no per-variant maintenance burden                         ║
║    + Future Claude Code branded videos (workshop, deep-dives) reuse the     ║
║      same variant fork pattern                                                ║
║                                                                               ║
║  DATA_FLOW:                                                                  ║
║    changelog URL → marckrenn highlights + official CHANGELOG.md →             ║
║    derived categories → per-scene narration → npx tts → narration.wav →       ║
║    npx transcribe → transcript.json → scene data-start values →               ║
║    composition fill → npx render → MP4                                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location | Before | After | User Impact |
| --- | --- | --- | --- |
| `templates/long-form/` | 1 template (`standard/`) | 2 templates (`standard/` + `claude-code-version/`) | Operator runs `cp -r templates/long-form/claude-code-version videos/<slug>` for the right palette + scene mix from step 1 |
| `templates/long-form/README.md` "Available templates" table | 1 row | 2 rows | Variant is discoverable in the index |
| `.claude/commands/diy-yt-creator/` | 8 phase commands, no version-update orchestrator | Adds `claude-code-version.md` | One-command spawn from changelog URL |
| `.claude/skills/diy-yt-creator/` | 2 skill notes (anthropic-short, archon-short) | Adds `new-claude-code-version-longform.md` | Future agents discover the variant via skill index |

---

## Mandatory Reading

**Implementation agent MUST read these before starting:**

| Priority | File | Why Read This |
| --- | --- | --- |
| P0 | `templates/long-form/standard/README.md` | Canonical fork workflow ("How to add a new long-form template") + the full file inventory + spawn instructions to mirror in the variant |
| P0 | `templates/long-form/standard/DESIGN.md` | Type scale, motion easings, color tokens, layout safe zones, "What NOT to Do" — the variant inherits all of this and only overrides palette |
| P0 | `templates/long-form/standard/index.html` | Root composition shape — sub-composition wrapping, ambient + shape-drift orchestration, crossfade timeline, audio bed comment block. Tasks 5-7 fork-and-edit this file. |
| P0 | `templates/long-form/standard/tokens/long-form.css` | The 6-variable palette to override |
| P0 | `templates/long-form/standard/compositions/scene-cta.html` | Closing CTA to adapt — swap the next-video card for a `$ claude update` terminal block |
| P0 | `templates/long-form/standard/compositions/scene-stat-pill-row.html` | The 2-pill stat pattern. We extend it to 3 pills for the stats opener (features / fixes / improved) |
| P0 | `templates/long-form/README.md` | Long-form vs shorts table + the official "fork the standard, swap the palette" workflow we follow |
| P0 | `.claude/rules/audio-design.md` | Updated 2026-04-28: SFX caps reduced 25% (impact-slam 0.20→0.15, screen-shake 0.15→0.11, etc.). All `data-volume` values in the variant must use the new numbers, not the old plan's numbers. |
| P1 | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\claude-code-version.md` | The 10-step process to port. Steps 0-4 (research, scriptwriting, AskUserQuestion for highlights/WatchNext) carry over verbatim; steps 5-10 (audio gen, timing constants, scene build, render) get adapted to HyperFrames CLI. |
| P1 | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\src\ClaudeCodeV21112-118\components\TerminalWindow.tsx` | Terminal chrome spec (36px title bar, 12px traffic-light circles `#FF5F56`/`#FFBD2E`/`#27C93F`, JetBrains Mono content) — port to `compositions/scene-terminal.html` |
| P1 | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\src\ClaudeCodeV21112-118\components\VersionBranding.tsx` | Spec for the persistent overlay (top-right logo stack at opacity 0.7, bottom-right URL line in JetBrains Mono 20px) — port inline into variant's `index.html` |
| P1 | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\src\ClaudeCodeV21112-118\constants\colors.ts` | Verbatim Claude Code palette to translate to CSS vars |
| P1 | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\src\ClaudeCodeV21112-118\research\content-brief.md` | Per-release brief format that the slash command should produce |
| P2 | `templates/shorts/anthropic/README.md` | Reference for the "Spawn a new video" section structure to mirror in variant README |
| P2 | `.claude/skills/diy-yt-creator/new-anthropic-short.md` | Skill-note shape for the new long-form skill |
| P2 | `.claude/skills/diy-yt-creator/new-archon-short.md` | Second skill-note example (recently added per git status) |
| P2 | `videos/anthropic-amazon-compute/index.html:737-1300` | Reference for `<audio>` track-index assignment + SFX wiring at the new lower volumes |

**External Documentation:**

| Source | Section | Why Needed |
| --- | --- | --- |
| HyperFrames docs index `https://hyperframes.heygen.com/llms.txt` | data-attributes + rendering | CLI render flag verification (`--quality`, `--workers`, `-o`) for the slash command's render step |
| `https://github.com/marckrenn/claude-code-changelog/tags` | per-tag Highlights section | Drives Scene "Highlights" content + AskUserQuestion confirmation |
| `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` | per-version anchor | Full change inventory drives stat counts + remaining category scenes |

---

## Patterns to Mirror

**FORK_THE_STANDARD (Task 1, the canonical first step per `templates/long-form/README.md:54-63`):**

```bash
# Bash
cp -r templates/long-form/standard templates/long-form/claude-code-version

# PowerShell
Copy-Item -Recurse templates/long-form/standard templates/long-form/claude-code-version
```

**PALETTE_OVERRIDE (Task 2, edit the forked `tokens/long-form.css`):**

```css
/* SOURCE: templates/long-form/standard/tokens/long-form.css */
/* OVERRIDE these specific vars to the Claude Code GitHub-dark palette. */
/* SOURCE-PALETTE: diy-yt-creator/src/ClaudeCodeV21112-118/constants/colors.ts */
:root {
  --bg:           #0D1117;   /* was #0B0F1A standard navy */
  --accent-1:     #58A6FF;   /* Claude Code cyan-blue (was #3B82F6) */
  --accent-2:     #06B6D4;   /* keep cyan */
  --accent-3:     #A371F7;   /* Claude Code purple (was #8B5CF6) */
  --accent-4:     #3FB950;   /* Claude Code green (was #22C55E) */
  --accent-warn:  #F78166;   /* Claude Code orange (was #F97316) */
  --accent-stat:  #F78166;   /* match warn — Claude Code uses same orange for hero stats */
  /* All other tokens (text, border, padding, type families) inherit from standard. */
}
```

**VERSION_BRANDING_OVERLAY (Task 3, paste-in inline addition to variant's `index.html`, immediately after `#top-banner`):**

```html
<!-- SOURCE: diy-yt-creator/src/ClaudeCodeV21112-118/components/VersionBranding.tsx -->
<!-- Persistent overlay; opacity 0.7; positioned absolute, NOT padding -->
<!-- Lives inside #root, NOT inside any scene wrapper. Renders for full duration. -->
<div id="version-branding">
  <div class="vb-logos">
    <img src="assets/anthropic-logo-light.svg" alt="Anthropic" />
    <img src="assets/claude-code-logo-light.svg" alt="Claude Code" />
  </div>
  <div class="vb-version" id="vb-version-string">github.com/anthropics/claude-code/releases  |  vX.Y.Z</div>
</div>
<style>
  #version-branding {
    position: absolute; inset: 0; opacity: 0.7;
    pointer-events: none; z-index: 9;
  }
  #version-branding .vb-logos {
    position: absolute; top: 30px; right: 30px;
    display: flex; flex-direction: column; gap: 12px; align-items: flex-end;
  }
  #version-branding .vb-logos img { width: 240px; height: auto; }
  #version-branding .vb-version {
    position: absolute; bottom: 30px; right: 30px;
    font-family: var(--mono); font-size: 20px; color: var(--text-secondary);
    letter-spacing: 1px;
  }
</style>
```

**TERMINAL_WINDOW_SCENE (Task 6, new `compositions/scene-terminal.html` — port from old TerminalWindow.tsx into the standard sub-comp shape):**

```html
<!-- SOURCE: diy-yt-creator/src/ClaudeCodeV21112-118/components/TerminalWindow.tsx -->
<!-- WRAPPER-SHAPE: templates/long-form/standard/compositions/scene-cta.html (the sub-comp shell pattern) -->
<!-- The .terminal-window block becomes scene content. -->
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<link rel="stylesheet" href="../tokens/long-form.css">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
  html, body { width:100%; height:100%; background: transparent; }
  #scene-terminal-content {
    width: 100%; height: 100%;
    padding: var(--pad-top) var(--pad-x) var(--pad-bottom);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    box-sizing: border-box; gap: 40px;
  }
  .term-overline {
    font-family: var(--mono); font-size: 26px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 6px;
    color: var(--accent-2);
  }
  .term-headline {
    font-family: var(--sans); font-size: 56px; font-weight: 800;
    color: var(--text); letter-spacing: -1px;
    text-align: center; max-width: 1400px; line-height: 1.05;
  }
  .terminal-window {
    width: 1400px; border-radius: 16px; overflow: hidden;
    background: rgba(28,33,40,0.95);
    box-shadow: 0 25px 60px rgba(0,0,0,0.55), 0 0 0 1.5px rgba(88,166,255,0.4);
  }
  .term-titlebar {
    height: 40px; display: flex; align-items: center; gap: 8px;
    padding: 0 16px; background: #21262D; position: relative;
  }
  .term-titlebar .dot { width: 12px; height: 12px; border-radius: 50%; }
  .term-titlebar .dot.red { background: #FF5F56; }
  .term-titlebar .dot.yellow { background: #FFBD2E; }
  .term-titlebar .dot.green { background: #27C93F; }
  .term-titlebar .title {
    position: absolute; left: 50%; transform: translateX(-50%);
    font-family: var(--sans); font-size: 18px; color: var(--text-secondary);
  }
  .term-content {
    padding: 32px 40px;
    font-family: var(--mono); font-size: 32px; line-height: 1.5;
    color: var(--text);
  }
  .term-content .prompt { color: var(--accent-4); }
  .term-content .flag   { color: var(--accent-1); }
</style>
</head>
<body>
<template id="scene-terminal" data-composition-id="scene-terminal">
  <div id="scene-terminal-content">
    <div class="term-overline">PLACEHOLDER OVERLINE</div>
    <div class="term-headline">PLACEHOLDER HEADLINE</div>
    <div class="terminal-window">
      <div class="term-titlebar">
        <span class="dot red"></span>
        <span class="dot yellow"></span>
        <span class="dot green"></span>
        <span class="title">~/project</span>
      </div>
      <div class="term-content">
        <span class="prompt">$</span> claude <span class="flag">update</span>
      </div>
    </div>
  </div>
</template>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  // Match the standard template's scene-internal timing convention
  tl.from(".term-overline",     { y: 20, opacity: 0, duration: 0.6, ease: "power3.out" }, 0.0);
  tl.from(".term-headline",     { y: 30, opacity: 0, duration: 0.7, ease: "power3.out" }, 0.2);
  tl.from(".terminal-window",   { scale: 0.92, opacity: 0, duration: 0.7, ease: "back.out(1.4)", immediateRender: false }, 0.4);
  window.__timelines["scene-terminal"] = tl;
</script>
</body>
</html>
```

**STATS_OPENER_SCENE (Task 6, new `compositions/scene-stats-opener.html` — extends standard's stat-pill-row from 2 to 3 pills):**

Mirror `templates/long-form/standard/compositions/scene-stat-pill-row.html` exactly but: render 3 pills instead of 2, accent-rotate `--accent-1` (cyan, "features") → `--accent-3` (purple, "fixes") → `--accent-4` (green, "improved"), add a small `data-vbadge` line above the pills showing the version (e.g. `vX.Y.Z`) in mono accent-1 26px.

**FEATURE_CARDS_SCENE (Task 6, new `compositions/scene-feature-cards.html` replacing standard's source-cards/architecture-stack):**

Mirror `compositions/scene-source-cards.html` shell but render 4-6 cards in either 2x2 grid (for category scenes) or 3x2 grid (for highlights), accent-rotated. Card shape: number badge (mono, 32px, accent color) + icon slot + title (28px Inter 700) + detail (20px secondary) + optional code pill below. Per-scene class `feature-cards--2x2` / `feature-cards--3x2` / `feature-cards--stack` toggles layout via flexbox.

**SLASH_COMMAND_SHAPE (Task 11):**

Port `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\claude-code-version.md` step-by-step. Critical adaptations:

| Old step | New step | Change |
| --- | --- | --- |
| Step 0: check `src/ClaudeCodeV<NN>/` | Same | path becomes `videos/claude-code-v<NN>/` |
| Step 1: WebFetch marckrenn + official | Unchanged | still WebFetch both sources |
| Step 1.5: AskUserQuestion (WatchNext) | Unchanged | same 3-question schema |
| Step 1.6: AskUserQuestion (highlights) | Unchanged | same schema |
| Step 2: copy template | Changed | `cp -r templates/long-form/claude-code-version videos/claude-code-v<NN>` |
| Step 3: research/content-brief.md | Unchanged | output to `videos/.../research/content-brief.md` |
| Step 4: write scripts (TTS optimization) | Unchanged | output to `videos/.../script.txt` (one combined file for `npx hyperframes tts`) |
| Step 5: `python generate-all-audio.py` | Changed | `npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav -v am_michael -s 1.0` |
| Step 5.5 (NEW) | Added | `npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>` produces `transcript.json` |
| Step 6: timing.ts | DROPPED | HyperFrames has no constants file; `data-start` lives on each scene wrapper directly in `index.html`, and is set from transcript.json word indices during composition fill |
| Step 7: scene .tsx files | Replaced | EDIT `compositions/scene-*.html` to populate per-release content (placeholder text → real text) |
| Step 8: Composition.tsx | Replaced | EDIT `index.html`: scene wrapper `data-start` values, narration `<audio>` `data-duration`, `#root data-duration`, `TOTAL_DURATION`, `#vb-version-string` text, ambient shape colors |
| Step 9: pnpm lint/dev | Changed | `npx hyperframes lint videos/<slug>` + `npx hyperframes inspect <slug>` + `npx hyperframes validate <slug>` (must pass before render) + `npx hyperframes preview <slug>` |
| Step 9.5: youtube-description.md | Unchanged | same SEO structure; output to `videos/<slug>/youtube-description.md` |
| Step 9.7: thumbnail manifest | Out of scope | per `NOT Building` — schema reference preserved as comment |
| Step 10: Remotion render | Changed | `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/long-form.mp4` (verify flags via `npx hyperframes docs rendering` before finalizing) |

---

## Files to Change

### CREATE (variant directory — by forking standard, then editing)

| File | Action | Justification |
| --- | --- | --- |
| `templates/long-form/claude-code-version/` (full subtree) | CREATE via `cp -r` from `templates/long-form/standard/` | Canonical fork workflow per `templates/long-form/README.md:57-58` |
| `templates/long-form/claude-code-version/meta.json` | UPDATE post-fork | `{ "id": "claude-code-version-template", "name": "Claude Code Version Update Template" }` |
| `templates/long-form/claude-code-version/README.md` | UPDATE post-fork | Document variant-specific spawn workflow + the `/claude-code-version` slash command. Replace standard's "Lib provenance" with a "Per-release content extraction" section pointing at the slash command. |
| `templates/long-form/claude-code-version/DESIGN.md` | UPDATE post-fork | Override standard DESIGN's color table with Claude Code palette; add a "Variant-specific surfaces" section documenting the VersionBranding overlay + terminal-window scene; otherwise inherits standard's typography, motion, layout, audio, and "What NOT to Do" rules verbatim. |
| `templates/long-form/claude-code-version/tokens/long-form.css` | UPDATE post-fork | Override the 6 palette CSS vars per PALETTE_OVERRIDE pattern; keep all other vars (spacing, type families, padding) at standard values |
| `templates/long-form/claude-code-version/index.html` | UPDATE post-fork | (a) Add VERSION_BRANDING_OVERLAY block per pattern above. (b) Rewire scene list: replace `scene-source-cards` → `scene-stats-opener` + `scene-feature-cards`, replace `scene-architecture-stack` → second `scene-feature-cards` (different layout class) or `scene-terminal`, replace `scene-image-hero` → `scene-terminal`. (c) Adjust `data-start` values to match the demo's 8-scene timing. (d) Update `<title>` and `tl.set(... TOTAL_DURATION)` if length changes. |
| `templates/long-form/claude-code-version/compositions/scene-stats-opener.html` | CREATE | Replaces `scene-source-cards.html`. 3 huge stat counters (features / fixes / improved) + version badge. Mirrors stat-pill-row shell. |
| `templates/long-form/claude-code-version/compositions/scene-feature-cards.html` | CREATE | Replaces `scene-architecture-stack.html`. 4-6 cards in configurable layout (2x2 / 3x2 / stack). Used for category and highlights scenes. |
| `templates/long-form/claude-code-version/compositions/scene-terminal.html` | CREATE | Replaces `scene-image-hero.html`. macOS terminal chrome with code block. |
| `templates/long-form/claude-code-version/compositions/scene-source-cards.html` | DELETE | Replaced by stats-opener |
| `templates/long-form/claude-code-version/compositions/scene-architecture-stack.html` | DELETE | Replaced by feature-cards |
| `templates/long-form/claude-code-version/compositions/scene-image-hero.html` | DELETE | Replaced by terminal |
| `templates/long-form/claude-code-version/compositions/scene-cta.html` | UPDATE post-fork | Swap the next-video card for a `$ claude update` terminal block (reuse terminal CSS from scene-terminal). Keep the subscribe pulse + debate-question card. |
| `templates/long-form/claude-code-version/assets/anthropic-logo-light.svg` | CREATE via copy | `cp shared/logos/anthropic-logo-light.svg templates/long-form/claude-code-version/assets/` (HyperFrames bundler rejects out-of-project paths, per `standard/README.md:118`) |
| `templates/long-form/claude-code-version/assets/claude-code-logo-light.svg` | CREATE via copy | Same — required by VersionBranding |
| `templates/long-form/claude-code-version/sfx-cues.txt` | UPDATE post-fork | Add Claude-Code-relevant cues: keep `impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop`; add `bell-notification` for subscribe pulse. |

### CREATE (commands + skills)

| File | Action | Justification |
| --- | --- | --- |
| `.claude/commands/diy-yt-creator/claude-code-version.md` | CREATE | Per-release orchestration command. Port from old `claude-code-version.md`, adapt per "SLASH_COMMAND_SHAPE" table above. |
| `.claude/skills/diy-yt-creator/new-claude-code-version-longform.md` | CREATE | Skill note for discoverability (mirror `new-anthropic-short.md` shape). |

### UPDATE (registry + index)

| File | Action | Justification |
| --- | --- | --- |
| `templates/long-form/README.md` | UPDATE | Add a row to "Available templates" table for `claude-code-version`. Update Status note: "2 templates available." |
| `.claude/skills/diy-yt-creator/SKILL.md` | UPDATE | Add reference to new long-form skill note (if SKILL.md indexes per-template skills — verify shape first). |

---

## NOT Building (Scope Limits)

- **shared/lib/ block extraction** — In the original draft we planned to author terminal-window, feature-card-grid, big-stat, cta-terminal, version-branding, subscribe-banner, watchnext-midroll as `shared/lib/` entries. The standard template's pattern is "fork + customize per variant," not "extract everything to shared/lib upfront." If a future second variant (e.g. `news-explainer`) needs the same terminal-window block, **then** extract. Premature lib-ification creates parallel maintenance burdens.
- **Multi-segment BG music generator** — long-form already has the 3-segment pattern documented in standard's README + `audio-design.md`'s "Multi-Segment Background Music" section is still TBD for the auto-generator. This plan ships with the existing manual `bg-music-{hook,body,cta}.mp3` slots inherited from standard, leaving them commented out by default. Per-release the operator drops files manually.
- **Beat alignment helper** — same parking lot as BG music auto-gen.
- **Captions auto-population** — standard ships `compositions/captions.html` already. This plan inherits it; the slash command's transcribe step produces `transcript.json` which the captions sub-comp reads. No new work needed.
- **Dynamous overlay finalization** — `shared/lib/blocks/dynamous-endcard/` and `shared/lib/blocks/dynamous-module-interstitial/` are in-progress (per git status). The variant ships with commented-out hook lines for a Dynamous overlay; operator activates per video once those lib entries finalize.
- **Thumbnail generator pipeline** — old project's Python image generator is not ported. Schema reference preserved in slash command + DESIGN.md.
- **WatchNext midroll component** — could be a future shared/lib component. For now, the slash command handles WatchNext via AskUserQuestion + a per-video manual scene insertion. Standard template doesn't ship one and we're not adding to standard.
- **Subscribe banner component** — standard's `scene-cta.html` already has a subscribe pulse pill. We're not adding a separate mid-video subscribe banner; the CTA covers it.
- **Vertical (1080x1920) Claude Code variant** — out of scope. Future work.
- **`/full-auto` integration** — chaining the new command into `.claude/commands/diy-yt-creator/full-auto.md` is a follow-up after the standalone command is validated on a real release.

---

## Step-by-Step Tasks

Execute in order. Tasks 1-9 build the variant; 10-12 ship the orchestration command + skill + index updates.

### Task 1: FORK `templates/long-form/standard/` → `templates/long-form/claude-code-version/`

- **ACTION**: Run the `cp -r` command per FORK_THE_STANDARD pattern. PowerShell equivalent: `Copy-Item -Recurse templates/long-form/standard templates/long-form/claude-code-version`.
- **VALIDATE**: `npx hyperframes lint templates/long-form/claude-code-version` MUST pass with 0 errors immediately after copy (the variant inherits standard's clean lint state). If it fails, the standard template itself is broken — file separate bug.

### Task 2: UPDATE `templates/long-form/claude-code-version/tokens/long-form.css` with Claude Code palette

- **ACTION**: Edit the 6 CSS variables per PALETTE_OVERRIDE pattern. Keep all other tokens (text, border, padding, type families, motion durations) at standard values.
- **MIRROR**: PALETTE_OVERRIDE block above. Source palette is `diy-yt-creator/src/ClaudeCodeV21112-118/constants/colors.ts`.
- **GOTCHA 1**: Do NOT change `--accent-2` (cyan #06B6D4) — Claude Code's own cyan `#58A6FF` is closer to the standard `--accent-1` blue. Map `--accent-1` → `#58A6FF` and leave `--accent-2` as standard cyan to preserve color separation between scenes.
- **GOTCHA 2**: Standard's `--accent-stat` is yellow (`#FBBC04`); Claude Code does not use yellow. Override to `#F78166` (Claude Code orange) so the hero stat in stat-pill-row inherits brand color.
- **VALIDATE**: `npx hyperframes validate templates/long-form/claude-code-version` runs WCAG contrast audit on the new palette. All accent text on `--bg #0D1117` must pass AA at ≥18.5px / 700 weight per `templates/long-form/standard/DESIGN.md:39-40`. If any accent regresses (e.g. accent-warn at small sizes), brighten it (e.g. `#F78166` → `#FB9070`).

### Task 3: UPDATE `templates/long-form/claude-code-version/meta.json`

- **ACTION**: Edit JSON to:
  ```json
  {
    "id": "claude-code-version-template",
    "name": "Claude Code Version Update Template"
  }
  ```
- **VALIDATE**: `node -e "JSON.parse(require('fs').readFileSync('templates/long-form/claude-code-version/meta.json'))"` (valid JSON).

### Task 4: COPY logos into variant `assets/`

- **ACTION**: Run `cp shared/logos/anthropic-logo-light.svg templates/long-form/claude-code-version/assets/` and `cp shared/logos/claude-code-logo-light.svg templates/long-form/claude-code-version/assets/`.
- **GOTCHA**: HyperFrames bundler rejects paths outside the project dir per `standard/README.md:118`. Logos MUST live inside the template subtree. Same rule applies when this template is later forked into `videos/<slug>/` — the slash command will need to ensure assets/ is copied along with everything else (which `cp -r` does naturally).
- **VALIDATE**: Both files exist in `assets/`; sizes > 0.

### Task 5: ADD VersionBranding overlay to variant's `index.html`

- **ACTION**: Insert the VERSION_BRANDING_OVERLAY block (HTML + CSS) immediately after the `#top-banner` block in `templates/long-form/claude-code-version/index.html`. The block sits inside `#root` but outside any `.scene-wrapper` so it renders for the full duration regardless of which scene is active.
- **GOTCHA 1**: Do NOT give the overlay `class="clip"` — per `standard/DESIGN.md:144`, audio elements never get `class="clip"` and the same logic applies to wrapper-only persistent visual overlays. The standard's `#top-banner` precedent is a reliable model: it has no `class="clip"` and renders for full duration via the timeline.
- **GOTCHA 2**: Logo width 240px (smaller than the old project's 360px) because the long-form canvas (1920x1080) is narrower than the old composition's effective real-estate budget after accounting for the standard top-banner wordmark also occupying the top safe zone. Verify visually in preview that the overlay does not collide with the centered top-banner logo.
- **GOTCHA 3**: If the standard's top-banner logo is the channel wordmark (centered top), and we add Anthropic + Claude Code logos top-right, that's two visual brand zones competing. **Resolution**: per video, the operator either (a) hides the standard top-banner-logo (set `display: none` or remove the img element) and lets VersionBranding own the brand zone, or (b) keeps the channel wordmark centered and accepts the right-edge Claude Code logos as a secondary brand cue. Document this choice in DESIGN.md.
- **VALIDATE**: `npx hyperframes lint templates/long-form/claude-code-version` passes; `npx hyperframes preview` shows logos render top-right at opacity 0.7.

### Task 6: REPLACE 3 scenes — CREATE stats-opener, feature-cards, terminal; DELETE source-cards, architecture-stack, image-hero

- **ACTION (a)**: CREATE `compositions/scene-stats-opener.html`. Copy `compositions/scene-stat-pill-row.html` as starting point. Modify to: 3 stat pills instead of 2 (add a third pill div); accent-rotate cyan→purple→green; add a small `data-vbadge` element above the pills (mono 26px, accent-1, content `vX.Y.Z` placeholder). Update GSAP timeline: stagger the 3 pill entrances at 0.5s/1.0s/1.5s with `back.out(1.6)` per `DESIGN.md:96`.
- **ACTION (b)**: CREATE `compositions/scene-feature-cards.html`. Copy `compositions/scene-source-cards.html` as starting point. Replace photo-card layout with: card has number badge top-left (mono 32px accent), icon slot, title (28px Inter 700), detail (20px secondary), optional code-pill below. Layout via `display: flex; flex-wrap: wrap; gap: 24px;` with per-card flex-basis driven by class on the scene-content root (`.feature-cards--2x2` → `flex: 1 1 calc(50% - 12px)`, `.feature-cards--3x2` → `flex: 1 1 calc(33.333% - 16px)`, `.feature-cards--stack` → `flex: 1 1 100%`). Slide-in from `y: 30, opacity: 0` with `back.out(1.4)` staggered 0.18s.
- **ACTION (c)**: CREATE `compositions/scene-terminal.html` per the TERMINAL_WINDOW_SCENE pattern above.
- **ACTION (d)**: DELETE the three replaced files: `scene-source-cards.html`, `scene-architecture-stack.html`, `scene-image-hero.html`. Also DELETE the matching screenshot placeholders in `assets/screenshots/` referenced ONLY by the deleted scenes (e.g. `source-1.png`, `source-2.png`, `source-3.png`). Keep `next-video-thumbnail.png` because the standard CTA still references it (and we'll adapt it in Task 7).
- **GOTCHA 1**: Per `standard/DESIGN.md:142-143`, `tl.from()` at position > 5 must use `immediateRender: false`. Verify each new scene's GSAP timeline respects this — entrance positions are typically < 5s within scene-local time so usually fine, but the terminal-window's scale entrance at position 0.4 is safe.
- **GOTCHA 2**: Per `standard/DESIGN.md:144`, NO `data-duration` on sub-composition wrapper divs. The sub-comp's internal timeline owns its length. The wrapper in `index.html` only takes `data-start`.
- **GOTCHA 3**: Per `standard/DESIGN.md:145`, NO `class="clip"` on `<audio>` or `<video>`. Stats-opener has no media; feature-cards has no media; terminal has no media. Safe.
- **VALIDATE (per scene)**: `npx hyperframes lint templates/long-form/claude-code-version` after each scene file lands. Then `npx hyperframes preview` and verify the scene mounts in isolation by temporarily setting it as the only wrapper in `index.html`.

### Task 7: UPDATE `compositions/scene-cta.html` for Claude Code

- **ACTION**: Edit the CTA scene to swap the next-video card for a `$ claude update` terminal block (reuse the terminal-window CSS from scene-terminal — duplicate inline; do NOT create a shared CSS file just for this). Keep the rest: subscribe pulse pill, debate-question card. Update placeholder text: heading "Update now." + terminal `$ claude update` + subscribe + debate-question card with placeholder text.
- **MIRROR**: TERMINAL_WINDOW_SCENE pattern above for the terminal block; standard `scene-cta.html` for the subscribe + debate-question card structure.
- **GOTCHA**: The subscribe pulse uses `box-shadow: 0 0 0 6px rgba(249,115,22,0.35); repeat ≤ 4` per `standard/DESIGN.md:119`. Repeat is finite per the `repeat: -1` ban (`DESIGN.md:142`). Verify the pulse repeat count matches.
- **VALIDATE**: Lint + preview the CTA scene.

### Task 8: REWIRE scene list in variant's `index.html`

- **ACTION**: Edit the 8 scene wrappers in `templates/long-form/claude-code-version/index.html`. Map (standard → variant):
  - scene-hook → scene-hook (kept; per-video copy edited later by slash command)
  - scene-image-hero → **scene-terminal** (new src `compositions/scene-terminal.html`, new id `scene-terminal-wrap`)
  - scene-side-by-side → scene-side-by-side (kept)
  - scene-stat-pill-row → **scene-stats-opener** (new src, new id; this is the "5 features / 30 fixes / 7 improved" opener scene — but appears AFTER scene-hook for full opener context)
  - scene-source-cards → **scene-feature-cards** with `feature-cards--3x2` layout class (highlights scene)
  - scene-video-embed → scene-video-embed (kept; optional per video; commented hook out by default)
  - scene-architecture-stack → **scene-feature-cards** with `feature-cards--stack` layout class (the "category" scene archetype)
  - scene-cta → scene-cta (kept; updated in Task 7)
- **ACTION (b)**: Update the `tl.addLabel` and `crossfadeScenes` calls at the bottom of the script to match the new ids (`scene-terminal-wrap` instead of `scene-image-hero-wrap`, etc.).
- **ACTION (c)**: Update `<title>` to "Claude Code Version Update — Template".
- **ACTION (d)**: Update the `#vb-version-string` text content default to a placeholder (`vX.Y.Z`) — the slash command swaps this per release.
- **GOTCHA 1**: The standard template's demo timing (0/12/32/55/70/90/105/115) is for 120s. A real Claude Code video is ~4-5 min. The variant's default timing should still match the demo's 120s — operators tune `data-start` values per video using `npx hyperframes transcribe` output. Document this in README.
- **GOTCHA 2**: The CSS rules in `index.html` for each `.scene-wrapper` (`#scene-image-hero-wrap`, etc.) reference scene IDs by name. Update these CSS rule selectors to the new IDs OR (cleaner) add new id-specific rules and delete the old ones. Don't leave dead CSS rules for deleted scenes.
- **VALIDATE**: `npx hyperframes lint templates/long-form/claude-code-version` MUST pass. `npx hyperframes preview` shows all 8 scenes mounting + crossfading.

### Task 9: UPDATE `README.md` and `DESIGN.md` in the variant

- **ACTION (README)**: Replace standard's variant-agnostic intro with Claude-Code-specific intro. Replace "Lib provenance" section with "Per-release content extraction" — point operators at the `/claude-code-version` slash command (Task 11). Update the spawn command from `cp -r templates/long-form/standard videos/<slug>` to `cp -r templates/long-form/claude-code-version videos/<slug>`. Add a note that VersionBranding overlay requires `assets/anthropic-logo-light.svg` and `assets/claude-code-logo-light.svg` — verify they exist (which Task 4 ensures). Add a "When NOT to use this variant" note: for non-Claude-Code branded videos, fork standard or another variant directly.
- **ACTION (DESIGN)**: Override the "Colors" section's table with the Claude Code palette. Add a new section "Variant-specific surfaces" documenting: VersionBranding overlay layout, terminal-window scene specs (titlebar dots, content padding, code typography), stats-opener 3-pill row, feature-cards layout modes (2x2 / 3x2 / stack). Otherwise inherit standard's typography/motion/layout/audio/anti-patterns.
- **VALIDATE**: Markdown lint clean. Spawn instructions are runnable verbatim.

### Task 10: UPDATE `templates/long-form/README.md` and (optionally) `shared/lib/MANIFEST.md`

- **ACTION (a)**: Edit `templates/long-form/README.md` — add a row to the "Available templates" table:
  ```markdown
  | [`claude-code-version/`](./claude-code-version/) | Dark navy + Claude Code GitHub-dark accents (cyan/green/purple/orange) | Per-release Claude Code version update videos. Adds VersionBranding overlay + terminal-scene + 3-pill stats opener. Spawn via `/claude-code-version` slash command. |
  ```
  Update the Status line: "2 templates available — `standard/` is the canonical baseline; `claude-code-version/` is the first variant."
- **ACTION (b)**: `shared/lib/MANIFEST.md` is auto-synced by `scripts/sync-shared-lib.sh` via PostToolUse hook. We're NOT adding any new shared/lib entries (per "NOT Building"), so the manifest should be unchanged. Verify after Tasks 1-9 land that no spurious rows appear.
- **VALIDATE**: Markdown lint. Verify the table renders correctly.

### Task 11: CREATE `.claude/commands/diy-yt-creator/claude-code-version.md`

- **ACTION**: Port the old `claude-code-version.md` step-by-step per the SLASH_COMMAND_SHAPE table above. Preserve sections: objective, frontmatter (description + argument-hint), 10-step process, output report.
- **MIRROR (structure)**: Old `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\claude-code-version.md`
- **MIRROR (HyperFrames idioms)**: `.claude/skills/diy-yt-creator/new-anthropic-short.md` for `npx hyperframes` CLI invocations
- **GOTCHA 1**: Verify `npx hyperframes render` flags (`--quality`, `--workers`, `-o`) are correct by running `npx hyperframes docs rendering` before finalizing. The standard template's README already uses `--quality high --workers 4 -o <path>` so that's the validated default.
- **GOTCHA 2**: The old command's Step 8 created a `Composition.tsx` from scratch. The new Step 8 EDITS the variant's `index.html` (and per-scene `compositions/*.html`) — DO NOT regenerate. The slash command should populate placeholders, not author whole compositions.
- **GOTCHA 3**: Per the new `audio-design.md` (modified 2026-04-28), SFX volumes are 25% lower than the old project: impact-slam 0.15 (was 0.20), spring-pop 0.11 (was 0.15), pop 0.10 (was 0.13), glitch-zap 0.09 (was 0.12), sonic-logo 0.45 (was 0.60). The slash command's audio-wiring step must use the new caps. If any user-supplied or auto-generated wiring exceeds the new caps, lint will catch it.
- **GOTCHA 4**: AskUserQuestion for WatchNext is mandatory per the old command. Preserve verbatim. Do NOT ship the variant template with a baked-in WatchNext scene — the slash command inserts a watchnext sub-comp on demand if the user provides answers; otherwise the gap is omitted.
- **VALIDATE**: Run the command end-to-end on a real recent Claude Code release URL (e.g., the most recent v2.1.NN). The command should produce a working `videos/claude-code-v<NN>/` directory that lints clean and renders.

### Task 12: CREATE `.claude/skills/diy-yt-creator/new-claude-code-version-longform.md`

- **ACTION**: Author skill note. Mirror `.claude/skills/diy-yt-creator/new-anthropic-short.md` structure: title, "When to use", "Spawn pipeline" with the exact `cp -r` command + per-file edit checklist, the audio + transcription workflow, the lint/preview/render workflow.
- **GOTCHA**: List the 4 files that need per-video edits: `tokens/long-form.css` (palette overrides if a release calls for theme variants), `index.html` (`#vb-version-string` text, `#root data-duration`, scene `data-start` values), `compositions/scene-*.html` (placeholder text → real content), `meta.json` (id, name).
- **VALIDATE**: Markdown lint. Discoverable via `npx hyperframes skills` or whatever the discovery command is.

---

## Testing Strategy

| Test | Command | Validates |
| --- | --- | --- |
| Lint (variant template, post-fork) | `npx hyperframes lint templates/long-form/claude-code-version` | All required attributes, audio overlap, sub-comp wiring |
| Validate (WCAG contrast) | `npx hyperframes validate templates/long-form/claude-code-version` | Claude Code palette passes AA |
| Inspect (layout overflow) | `npx hyperframes inspect templates/long-form/claude-code-version` | No element extends past 1920x1080 (esp. VersionBranding logos top-right + 240px wide check) |
| Preview | `npx hyperframes preview templates/long-form/claude-code-version` | All 8 scenes mount, crossfades render, VersionBranding visible |
| Render smoke (template demo) | `npx hyperframes render templates/long-form/claude-code-version --quality high --workers 4 -o templates/long-form/claude-code-version/out/demo.mp4` | 1920x1080 30fps MP4 |
| End-to-end smoke (real release) | `/claude-code-version v2.1.NN` (most recent version) | Full pipeline from changelog URL → MP4 |

### Edge Cases Checklist

- [ ] Small release (≤10 changes): stats opener reads small numbers without overflow; some category scenes can be omitted by removing wrappers from `index.html`.
- [ ] Large release (30+ changes): 220px stat numbers don't overflow at 3-digit values (`tabular-nums` already in standard tokens).
- [ ] Version range string (e.g. `v2.1.112–v2.1.118`): `#vb-version-string` element's max-width allows the dash-range without wrapping.
- [ ] WatchNext omitted: variant inherits standard's structure with no WatchNext scene; slash command's "skip" answer leaves it out cleanly.
- [ ] Highlights skipped (rare/old releases): scene-feature-cards with `--3x2` layout is removed from `index.html` wiring; remaining 7 scenes carry the video.
- [ ] Brand wordmark conflict: variant ships with VersionBranding ON + standard top-banner ON. Per Task 5 GOTCHA 3, operator chooses per video which to keep visually. Default (template ships): both visible (top-banner centered + VersionBranding right-edge); document override.

---

## Validation Commands

### Level 1: STATIC_ANALYSIS (after each task)

```bash
npx hyperframes lint templates/long-form/claude-code-version
```

**EXPECT**: Exit 0 after Task 1 (post-fork), and after each subsequent edit. Warnings reviewed (e.g. `audio_src_not_found` on the bare template is expected per `standard/README.md:209-213` — fixed when the slash command spawns a video and the operator drops narration).

### Level 2: WCAG + LAYOUT

```bash
npx hyperframes inspect templates/long-form/claude-code-version
npx hyperframes validate templates/long-form/claude-code-version
```

**EXPECT**: No overflow findings. WCAG AA passes for all body text on `--bg #0D1117`. Accent text passes AA at ≥18.5px / 700 weight per `standard/DESIGN.md:39-40`.

### Level 3: PREVIEW

```bash
npx hyperframes preview templates/long-form/claude-code-version
```

**EXPECT**: Studio editor at `http://localhost:5173`. All 8 scenes mount. VersionBranding overlay visible top-right + bottom-right. Crossfades work between scenes.

### Level 4: TEMPLATE RENDER (smoke)

```bash
npx hyperframes render templates/long-form/claude-code-version --quality high --workers 4 -o templates/long-form/claude-code-version/out/demo.mp4
```

**EXPECT**: 1920x1080 30fps MP4, ~120 seconds (matches the demo timing inherited from standard).

### Level 5: END-TO-END (per-release validation)

After Task 11 lands, run `/claude-code-version` on a real or test release URL:

```bash
# Pick a version that the old project already shipped, so you can compare.
# Run the slash command in the agent.
/claude-code-version v2.1.118
```

**EXPECT**: After all interactive steps complete, `videos/claude-code-v2118/` exists, lints clean, previews, and renders to `videos/claude-code-v2118/out/long-form.mp4`. Compare side-by-side with the old Remotion render of the same release.

### Level 6: MANUAL_VALIDATION

- [ ] Operator runs end-to-end on a known release
- [ ] Output MP4 uploadable to YouTube
- [ ] `youtube-description.md` paste-ready (chapters timestamps match render)
- [ ] Narration matches script.txt verbatim (TTS round-trip preserved)
- [ ] VersionBranding shows correct version string

---

## Acceptance Criteria

- [ ] `templates/long-form/claude-code-version/` exists, forked from `standard/`
- [ ] Variant `tokens/long-form.css` has the 6 Claude Code palette overrides
- [ ] Variant `assets/` contains `anthropic-logo-light.svg` and `claude-code-logo-light.svg`
- [ ] Variant `index.html` has VersionBranding overlay, rewired scene list, updated `<title>`
- [ ] Variant `compositions/scene-stats-opener.html`, `scene-feature-cards.html`, `scene-terminal.html` exist; the 3 replaced scenes (source-cards, architecture-stack, image-hero) are deleted
- [ ] Variant `compositions/scene-cta.html` shows `$ claude update` terminal block
- [ ] Variant `meta.json` updated with `claude-code-version-template` id
- [ ] Variant `README.md` and `DESIGN.md` updated for variant specifics
- [ ] `templates/long-form/README.md` "Available templates" table has the new row
- [ ] `.claude/commands/diy-yt-creator/claude-code-version.md` exists, runs end-to-end on a real release
- [ ] `.claude/skills/diy-yt-creator/new-claude-code-version-longform.md` exists
- [ ] `npx hyperframes lint`, `inspect`, `validate` all pass on the variant template
- [ ] Variant template renders to MP4 (smoke test)
- [ ] At least one real-release video produced via the slash command renders successfully
- [ ] No regressions: `npx hyperframes lint templates/long-form/standard` and `npx hyperframes lint templates/shorts/anthropic` still pass; existing 4 vertical Shorts in `videos/` still lint

---

## Completion Checklist

- [ ] Tasks 1-4 complete: fork + palette + meta + logos
- [ ] Task 5 complete: VersionBranding overlay
- [ ] Task 6 complete: 3 new scenes + 3 deleted scenes
- [ ] Task 7 complete: CTA adapted for Claude Code
- [ ] Task 8 complete: scene wiring updated in index.html
- [ ] Task 9 complete: README and DESIGN updated
- [ ] Task 10 complete: parent README updated
- [ ] Task 11 complete: slash command shipped + tested end-to-end
- [ ] Task 12 complete: skill note shipped
- [ ] Levels 1-4 validation pass on the template
- [ ] Level 5 validation passes on a real release
- [ ] All acceptance criteria met

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Standard template changes break the fork (variant drifts from baseline) | LOW | MEDIUM | Document the fork relationship in variant README; periodic "rebase" audits when standard ships breaking changes. The two are independent files post-fork — drift is unavoidable but should be intentional, not accidental. |
| VersionBranding logos collide visually with standard's top-banner wordmark | MEDIUM | LOW | Per Task 5 GOTCHA 3, document the choice in DESIGN.md. Default is both visible; operator can hide top-banner per video by removing the img element. |
| `--accent-stat` Claude Code orange duplicates `--accent-warn` (same hex) | LOW | LOW | Acceptable — Claude Code uses one orange for both stats and warnings. The two contexts (hero stat vs warning callout) are visually distinct from layout, not color. Document in DESIGN.md. |
| New `audio-design.md` SFX volumes (post-2026-04-28 calibration) used incorrectly in slash command audio wiring | LOW | MEDIUM | Slash command Task 11 GOTCHA 3 explicitly references the new numbers. Lint enforces 0.25 hard cap; new numbers are well below cap. |
| HyperFrames CLI render flags differ from what the old project's command expected (`--codec h264 --crf 15 --color-space bt709 --x264-preset slow`) | MEDIUM | MEDIUM | Standard template README already uses `--quality high --workers 4 -o <path>`. Verify those map to comparable quality via `npx hyperframes docs rendering` before finalizing slash command. |
| `data-composition-src` paths break when the template is later forked into `videos/<slug>/` | LOW | HIGH | Variant uses paths relative to `index.html` (`compositions/scene-*.html`), which survive `cp -r` intact. Logos are inside the template subtree so they survive too. Validated in Level 1 lint. |
| Slash command's transcribe step produces transcript.json that doesn't align with the captions sub-comp's expected format | LOW | MEDIUM | Standard's `compositions/captions.html` has `data-caption-root="true"`; HyperFrames' `npx hyperframes transcribe` is the canonical producer. The two are designed to interoperate per `standard/README.md:21`. Validate by running transcribe on a stub narration and confirming captions render in preview. |
| Stats opener 3-pill layout overflows at 3-digit values (e.g. "120 fixes") | LOW | LOW | `font-variant-numeric: tabular-nums lining-nums` (inherited from standard typography) prevents reflow. Verify by spawning a stub video with 999 in each pill and inspecting. |

---

## Notes

### Scope reduction since the original draft

The original plan called for 27 tasks including authoring 7 new `shared/lib/` blocks/components from scratch. That was correct **before** `templates/long-form/standard/` shipped. Now that standard exists with 8 reusable scene archetypes + tokens + audio bed pattern + crossfade orchestrator + captions, the variant work is just "fork standard, swap palette, swap 3 scenes, add VersionBranding, ship slash command." Lib extraction is deferred until a second variant needs the same pieces.

### Why this is a variant, not a new shared/lib

`templates/long-form/README.md:54-63` documents the "fork the standard" pattern as the canonical workflow for new long-form variants. The standard exists precisely so variants don't re-author orchestration. Premature lib extraction (the original plan's approach) would have created two parallel maintenance burdens — a lib copy and a template copy — without a second consumer to justify the lib's existence.

### Why we keep `scene-video-embed.html` despite Claude Code releases rarely needing video embeds

Some Claude Code releases ship features that benefit from a screencap demo (e.g., `/plan` command, vim mode). The slash command's content-derivation step can decide whether to wire the scene-video-embed wrapper into `index.html` per release. Default: commented out, operator activates via the slash command's AskUserQuestion or manual edit.

### Why the slash command does not auto-extract logos to assets

`shared/logos/` is a repo-shared asset directory. Forking standard → variant copies any logos already in `templates/long-form/standard/assets/`. The standard ships with no logos in `assets/`; the variant adds Claude Code logos via Task 4 (one-time setup). When the slash command later spawns `videos/<slug>/` from the variant, those logos are carried along by `cp -r`. No per-spawn logo extraction needed.

### Future enhancements (out of scope, logged)

- **Lib-extract the terminal-window scene** if a second variant needs it.
- **Lib-extract the feature-card-grid scene** if a second variant needs it (e.g., `news-explainer` for a "key takeaways" scene).
- **Lib-extract the VersionBranding overlay** as a `shared/lib/components/version-branding/` component if a second Claude-Code-branded video type emerges (workshop replays, retrospectives).
- **Auto-generate per-release thumbnails** via Canva MCP or a dedicated image generator.
- **Multi-segment BG music auto-gen** per `audio-design.md`'s TBD section.
- **`/full-auto` integration** chaining `/claude-code-version` after research/plan/script phases.
- **Vertical Claude Code variant** for shorts, reusing the variant fork pattern on `templates/shorts/anthropic/`.
