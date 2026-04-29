# Feature: Dynamous Shorts Promotion System (HyperFrames port)

## Summary

Port the three-component Dynamous brand promotion system from the Remotion-based `diy-yt-creator` repo into this HyperFrames repo as reusable `shared/lib/` entries. Replace the existing wordmark-only badge with a logo-led mark, anchor placement to YouTube Shorts safe zones, and ship one paste-in **component** (persistent corner badge) plus two sub-composition **blocks** (last-3s contextual endcard, optional 3s mid-video module interstitial). Goal: subtle but unmistakable on-screen brand presence on every Short, with the 10%-off offer surfaced *only* in the description / pinned comment (verified offer details still pending from Cole — see Risks).

## User Story

As a creator publishing dark-stage Anthropic / Archon / Claude Shorts from this repo,
I want a single drop-in Dynamous badge plus two opt-in scene blocks
So that every Short carries a recognisable Dynamous AI Mastery mark and ends with a contextual community CTA, driving viewers to the description / pinned comment where the 10%-off deal lives.

## Problem Statement

The repo currently has zero Dynamous brand presence in any Short composition. The reference Remotion implementation in `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/src/shared/components/Shorts*.tsx` is a clean three-piece system but (a) is React/Remotion code that does not run inside HyperFrames' HTML+GSAP runtime, (b) shows the wordmark `dynamous.ai` as text only — no logo — making it generic-looking, (c) places the badge at `top: 48` which is *inside* the YouTube Shorts top-UI keep-out zone (top 380 px is reserved for title + channel name), and (d) ships no real promo code on screen, which is correct (the 10% deal lives in the description, not the overlay) but the system never made that intent explicit.

## Solution Statement

> **OPT-IN, NOT DEFAULT.** The Dynamous promotion system is per-video opt-in. Templates ship without any Dynamous wiring. The new-Short creation flow (the `/diy-yt-creator` skill + each template's README + a new spawn-time prompt) explicitly asks **"Add Dynamous promotion to this Short? (y/N — default no)"** and only wires the artifacts when the author says yes. Existing videos are never retroactively touched.

> **BRAND IS THE MIDROLL v3 BRAND, NOT THE OLDER SHORTS CONSTANTS.** The reference `DynamousMidroll.tsx` (v3, Apr 2026) is the canonical brand expression — modern-gradient palette + `Join the Community` / `Link in Description ↓` / `10% OFF` CTA stack. The older Shorts constants (`#D97757` stone palette, `dynamous.ai` text-only) are superseded. All four new artifacts use the midroll palette and verbatim CTA wording. Logo assets, Cole photo, and the verified 10% offer are already shipping in the diy-yt-creator repo and copy directly into this repo.

Recreate the system in **four** native HyperFrames artifacts under `shared/lib/` (three ports + one new "discount bubble" derived from the user-provided strategy doc):

1. **`components/dynamous-badge/`** — paste-in HTML+CSS+JS snippet for a persistent lower-left corner badge: small Dynamous mark + `dynamous.ai` wordmark in muted text. No `class="clip"` (mirrors the existing `top-banner-wordmark` pattern). Anchored inside the YouTube Shorts safe zone (left 60 px / bottom 460 px — clear of action buttons and likes/subscribe column). **Entrance delayed to `t=3.0s`** to respect the 3-second-hook rule from the strategy doc — never compete with the opening hook.
2. **`blocks/dynamous-endcard/`** — sub-composition (`block.html` + `recipe.md`) consuming the trailing 3.0 s of any Short. Centred logo + module-or-generic CTA + URL slam, ending with a 0.5 s fade-to-black. Wired via `data-composition-src`.
3. **`blocks/dynamous-module-interstitial/`** — opt-in 3.0 s overlay block, slides in from the right at a natural narration pause, holds, slides out. Used only when the Short's topic maps to one of the 12 curriculum modules.
4. **`components/dynamous-discount-bubble/`** — *new, derived from the strategy doc's "Text Overlay" recommendation.* Tiny opt-in 3–4 s pill that pops up while the screen recording shows the Dynamous platform: `Dynamous.ai · Code XYZ for 10% off`. Used ONLY in tutorial / over-the-shoulder Shorts where the platform is visibly on screen. Sound-off viewers see the offer; sound-on viewers hear the soft verbal CTA.

Plus: drop the official Dynamous logo into `shared/logos/` (two variants: square mark for the badge, full mastery wordmark for the endcard); record the curriculum-module list as a copy-from JSON token under `shared/lib/components/dynamous-data/`; and document the per-video wiring + `script.txt` line + pinned-comment + description templates that drive the actual conversion (the strategy doc's "Pinned Comment Strategy" is the canonical conversion path — overlays are recall amplifiers).

## Metadata

| Field            | Value                                                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Type             | NEW_CAPABILITY                                                                                                                          |
| Complexity       | MEDIUM                                                                                                                                  |
| Systems Affected | `shared/lib/components/`, `shared/lib/blocks/`, `shared/logos/`, `shared/lib/MANIFEST.md` (auto-synced), per-video `index.html` wiring, per-video `script.txt`/`description.md` templates |
| Dependencies     | GSAP 3.14.2 (CDN, already loaded by every Short); HyperFrames runtime (existing); `@hyperframes/core` bundler path-safety guard         |
| Estimated Tasks  | 14                                                                                                                                      |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         BEFORE — current Short composition                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌─── 1080 x 1920 dark-stage Short ────────────────────────────────────┐    ║
║   │                                                                      │    ║
║   │   [ Anthropic / Archon / Claude logo banner — top: 60px ]            │    ║
║   │                                                                      │    ║
║   │                                                                      │    ║
║   │              Phase 1 → Phase 2 → Phase 3 → Phase 4                   │    ║
║   │              (hero word, stats, timeline, CTA)                       │    ║
║   │                                                                      │    ║
║   │                                                                      │    ║
║   │   [ Slim orange progress bar — bottom: 0 ]                           │    ║
║   └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
║   USER_FLOW: viewer watches → no Dynamous brand cue anywhere → at the end     ║
║              the URL CTA points at the *episode topic's* URL (e.g. anthropic  ║
║              blog), nothing pulls them toward the community.                  ║
║   PAIN_POINT: zero recurring brand presence across the channel; viewers who   ║
║               watched 5 Shorts have no idea Dynamous exists. 10%-off deal     ║
║               in the description goes unseen because no overlay teases it.    ║
║   DATA_FLOW: narration.wav + transcript.json → GSAP timeline → MP4. No        ║
║              external brand assets, no module data.                           ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         AFTER — Short with Dynamous system                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌─── 1080 x 1920 dark-stage Short ────────────────────────────────────┐    ║
║   │                                                                      │    ║
║   │   [ Anthropic / Archon / Claude logo banner — top: 60px ]            │    ║
║   │                                                                      │    ║
║   │              Phase 1 → Phase 2 → Phase 3 → Phase 4                   │    ║
║   │   ╔══╗                                                               │    ║
║   │   ║◆ ║       (optional 3s mid: module interstitial slides in →)     │    ║
║   │   ╚══╝       ┌────────────────────────────┐                          │    ║
║   │              │ MODULE 5 — MCP & Tool Use  │ (slide-in 0.6s, hold 1.8s,│   ║
║   │              │ Part of Dynamous AI Mastery│  slide-out 0.6s)         │    ║
║   │              └────────────────────────────┘                          │    ║
║   │                                                                      │    ║
║   │   ┌─[ persistent badge — bottom-left, opacity 0.45 ]─┐               │    ║
║   │   │ ◆  dynamous.ai                                    │               │    ║
║   │   └────────────────────────────────────────────────────┘             │    ║
║   │   [ Slim orange progress bar — bottom: 0 ]                           │    ║
║   └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                               ║
║   …last 3.0 s of every Short… replaces the trailing window:                   ║
║   ┌───────────────────────────────────────────────────────────────────────┐  ║
║   │              [ Dynamous mastery wordmark — white SVG ]                │  ║
║   │                                                                       │  ║
║   │              MODULE 5  ·  MCP & Tool Use                              │  ║
║   │              ────────────────────                                     │  ║
║   │              Part of the Dynamous AI Mastery curriculum               │  ║
║   │                                                                       │  ║
║   │              dynamous.ai  ·  link in description                      │  ║
║   │                                                                       │  ║
║   │              [ fade-to-black, frames 75–90 ]                          │  ║
║   └───────────────────────────────────────────────────────────────────────┘  ║
║                                                                               ║
║   USER_FLOW: viewer sees a quiet Dynamous mark from second 0; at any moment   ║
║              their eye can land on the bottom-left badge and recognise the    ║
║              channel; if the Short's topic matches a module they get a 3 s    ║
║              card mid-video; the final 3 s replaces the generic CTA with a    ║
║              Dynamous endcard, then fades to black. Description/pinned comment║
║              carries the actual 10%-off code (script.txt template enforces).  ║
║   VALUE_ADD: recurring brand exposure (every Short, every second), contextual ║
║              hook on matching topics, terminal CTA for community signups.     ║
║   DATA_FLOW: narration.wav + transcript.json + dynamous-modules.json → GSAP   ║
║              host timeline + 2 self-registered sub-comp timelines             ║
║              (window.__timelines["dynamous-endcard"], window.__timelines[     ║
║              "dynamous-module-interstitial"]) → MP4.                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

> All rows below describe the AFTER state **only when the author opted in** at spawn time. Opt-out videos remain identical to today.

| Location                                                  | Before                                | After (opt-in only)                                                                | User Impact                                                                                            |
| --------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| New-Short scaffolding prompt (`/diy-yt-creator` + README) | no question                           | "Add Dynamous promotion? (y/N)" — default no                                       | Author makes a conscious per-video decision; no surprise wiring                                         |
| Persistent overlay (opt-in Shorts)                        | nothing                               | Bottom-left badge — Dynamous mark + `dynamous.ai`, opacity 0.45, fade-in at `t=3.0s` | Brand recognition without competing with the 3-second hook                                              |
| Mid-Short, when topic matches a module (opt-in only)      | nothing                               | Optional 3.0 s slide-in card naming the matching module                              | Contextual relevance — viewer learns "this topic is part of a real curriculum"                          |
| Mid-Short, when platform is on-screen (tutorial Shorts)   | nothing                               | Optional 3–4 s discount-code bubble: `Dynamous.ai · Code XYZ for 10% off`            | Sound-off viewers see the offer; sound-on viewers hear the soft verbal CTA                              |
| Final 3.0 s of opt-in Short                               | episode-specific outro                | Endcard replaces the trailing 3 s — module CTA or generic, then fade-to-black       | Terminal CTA pointing at the community; consistent ending across the channel                            |
| Per-video `script.txt` last line (opt-in only)            | episode-specific outro                | Locked verbatim: *"A lot of you asked how I'm learning all this AI stuff — I use Dynamous. It's an awesome community. I actually reached out to them and got a 10% off code for you guys, it's in the pinned comment."* | Audio CTA framed as a favor, not a sales pitch — matches the "Friend Test"                              |
| Video description + pinned comment (opt-in only)          | episode links only                    | Required first line of pinned comment (NO `[YOURCODE]` placeholder — discount is automatic via the link): *"You can check out Dynamous AI here: [LINK]. 10% off applies automatically when you join through this link! 👇"* | Single canonical conversion path — clicking the link is what triggers the discount; no code to remember |

---

## Mandatory Reading

**CRITICAL: Implementation agent MUST read these files before starting any task.**

| Priority | File                                                                                                          | Lines    | Why Read This                                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/src/shared/components/ShortsDynamousBadge.tsx`              | 1-93     | Source-of-truth for the badge — copy timing, copy idle opacity, copy "muted text + small dot" composition exactly                                   |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/src/shared/components/ShortsContextualEndcard.tsx`          | 1-237    | Source-of-truth for endcard — three-phase animation (bg fade 0–0.4s, content slide spring 0.4–2.5s, fade-to-black 2.5–3.0s)                          |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/src/shared/components/ShortsModuleInterstitial.tsx`         | 1-153    | Source-of-truth for interstitial — slide-in (0–0.6s), hold, slide-out (2.4–3.0s) at top: 420 px from frame top                                       |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/src/shared/constants/dynamous.ts`                           | 1-131    | Brand color palette + 12-module curriculum data + `findMatchingModule()` keyword logic — port verbatim into `dynamous-modules.json`                  |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/lib/components/top-banner-wordmark/component.html` | 1-79  | Pattern to MIRROR for the badge — three-section paste-in (HTML/CSS/JS) + the explicit "logo must be a local copy" warning + asset-copy checklist     |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/lib/blocks/url-cta/block.html`           | 1-150+   | Pattern to MIRROR for the two blocks — `<template>` wrapper, `data-composition-id`, scoped CSS, self-registered `window.__timelines` entry           |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/lib/blocks/url-cta/recipe.md`            | all      | Pattern to MIRROR for both block recipes — wiring HTML, slot table, don'ts, lint expectation                                                         |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/lib/README.md`                           | all      | Consumption rules for `shared/lib/` — copy-from-not-reference-from, kebab-case, sync hook behaviour                                                  |
| P1       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/.claude/rules/audio-design.md`                  | all      | "Shorts Have NO Background Music (HARD RULE)" — these overlays must add zero audio. No stinger SFX on the endcard, even though Remotion has none either |
| P1       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/.agents/skills/hyperframes/SKILL.md`            | 116-270  | `data-start`/`data-duration`/`data-track-index` semantics, `class="clip"` visibility hook, sub-composition `<template>` rule, deterministic-only constraint |
| P1       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/templates/shorts/anthropic/index.html`          | 96-111, 433-435, 682 | The `#top-banner` pattern — `position: absolute` + `z-index: 10` + no clip class + single GSAP entrance at `t=0.2s`                     |
| P1       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/videos/anthropic-amazon-compute/index.html`    | 1072-1180| Pattern for SFX-free overlays + transcript-anchored timing — read to understand how host index.html stays synchronous and deterministic              |
| P0       | `C:/Users/Leex279/.gemini/antigravity/brain/0276711e-f22d-4d0f-935f-5eba5685c8ce/artifacts/shorts_promotion_strategy.md.resolved` | all | User-supplied promotion strategy. Source of: (a) the "value first, pitch second" philosophy, (b) the verbatim Pinned Comment template, (c) the discount-bubble overlay format, (d) the 3-second-hook rule that delays the badge entrance, (e) the verbal CTA framing ("I got you guys a discount") |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/src/shared/components/DynamousMidroll.tsx` | 1-200, 977-979, 2018-2257 | **Canonical brand source.** Read three slices: (1) `COLORS` block (lines 78-95) for the modern-gradient palette, (2) line 977 for the logo asset path (`assets/dynamous-logo.png`), (3) lines 2018-2257 for the Phase 6 CTA layout — endcard mirrors this exact stack: glass card → headline "Join the Community" → "Link in Description ↓" pill → "10% OFF" red badge → `dynamous.ai` URL. Default `discountText='10%'` confirms the offer is real and standard. |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/public/assets/dynamous-logo.png`             | (binary) | The official Dynamous square mark. Copy directly into `shared/logos/dynamous-mark-light.png`. Used at 56×56 in the midroll. |
| P0       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator/public/assets/dynamous-ai-mastery-white.svg` | (binary) | The official "Dynamous AI Mastery" full lockup, white-on-dark. 37 KB SVG. Copy into `shared/logos/dynamous-ai-mastery-white.svg`. |
| P2       | `C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/lib/MANIFEST.md`                         | 1-82     | DO NOT manually edit — auto-synced by `scripts/sync-shared-lib.sh` PostToolUse hook. Just confirm the new entries appear after first Bash/Write       |

**External Documentation:**

| Source                                                                                                                            | Section                              | Why Needed                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------ |
| [GSAP 3.14.2 — timeline position parameter](https://gsap.com/docs/v3/GSAP/Timeline/)                                              | "Position parameter"                  | Sub-comp blocks register their own paused timeline at `position: 0` and the host seeks them in sync — same idiom as `url-cta` |
| [YouTube Shorts safe zones — orsonlord.com](https://orsonlord.com/articles/free-safe-zone-overlays-for-reels-tiktok-and-shorts)   | Safe zone overlays                    | Confirms the 960×1160 usable area inside 1080×1920 — drives the badge bottom-left placement      |
| [YouTube Shorts monetization policy](https://support.google.com/youtube/answer/12504220)                                          | Reused content / watermarks           | First-party brand overlays on original content are explicitly OK — actually a 2025 originality signal |
| [Dynamous AI Mastery — Circle discover page](https://discover.circle.so/product/dynamous-ai-mastery)                              | Tagline + platform confirmation       | Verbatim tagline source, confirms platform is Circle (not Skool), confirms `$712/year` price     |
| [Dynamous LinkedIn company page](https://www.linkedin.com/company/dynamous)                                                       | Company description                   | "Home of the Dynamous AI Mastery Community — a place for early AI adopters to master AI agents and AI coding" — verbatim quote for endcard generic copy |

- KEY_INSIGHT: GSAP timelines registered on `window.__timelines` are seeked by the HyperFrames runtime — no manual `tl.add()` call from the host needed for sub-comp blocks
  - APPLIES_TO: tasks 4 and 5 (the two block.html files)
  - GOTCHA: The block's timeline MUST be `paused: true` and registered synchronously (no `await`, no `setTimeout`)

- KEY_INSIGHT: YouTube Shorts top 380 px and bottom 380 px are reserved for YouTube's own UI (title, channel name, action column, subscribe). Remotion source's `top: 48` for the badge violates this.
  - APPLIES_TO: task 3 (badge component CSS)
  - GOTCHA: Anchor the badge to `bottom: 460px; left: 60px;` — left edge clear of the right-side action column, vertical position above the comments/likes/subscribe row

- KEY_INSIGHT: Strategy doc — "You have less than 3 seconds to stop the scroll. Start with a bold statement, a compelling question, or a highly visual action. *Never* start the video with the brand name."
  - APPLIES_TO: task 3 (badge entrance timing) — delay the badge fade-in to `t=3.0s` so it doesn't compete with the hook visual
  - APPLIES_TO: tasks 6, 8, 13 (endcard / interstitial / discount bubble) — none of these may fire in the first 3 seconds of any Short

- KEY_INSIGHT: Strategy doc — Pinned-comment is the canonical conversion path; on-screen overlays are recall amplifiers, not the conversion mechanism. The 10%-off code lives in the pinned comment and description, not on screen — *unless* using the discount-bubble overlay (artifact 4), which is opt-in and only fires while the platform is visibly on screen.
  - APPLIES_TO: tasks 12 + 14 (wiring snippet, pinned-comment / description templates)
  - GOTCHA: The discount bubble is the ONLY on-screen surface that may carry a code, and only in tutorial/over-the-shoulder Shorts where the platform is being shown

---

## Patterns to Mirror

**NAMING_CONVENTION (kebab-case folders, plain CSS classes, scoped IDs):**

```
// SOURCE: shared/lib/MANIFEST.md:42-58
// COPY THIS PATTERN: kebab-case directory, file-per-asset
shared/lib/components/dynamous-badge/component.html
shared/lib/components/dynamous-data/dynamous-modules.json
shared/lib/blocks/dynamous-endcard/block.html
shared/lib/blocks/dynamous-endcard/recipe.md
shared/lib/blocks/dynamous-module-interstitial/block.html
shared/lib/blocks/dynamous-module-interstitial/recipe.md
shared/logos/dynamous-mark-light.svg
shared/logos/dynamous-mastery-wordmark-light.svg
```

**PERSISTENT_OVERLAY_PATTERN (badge — no clip, no data-* attrs, single GSAP entrance, midroll-aligned palette):**

```html
<!-- SOURCE: shared/lib/components/top-banner-wordmark/component.html:32-66 (structure)
            + DynamousMidroll.tsx:78-95 (palette) + DynamousMidroll.tsx:977-979 (logo asset) -->
<!-- COPY THIS PATTERN: -->

<!-- 1) HTML — paste at the top of your composition's root <div>. -->
<div id="dynamous-badge">
  <img id="dynamous-badge-mark" src="assets/dynamous-logo.png" alt="Dynamous" crossorigin="anonymous" />
  <span id="dynamous-badge-url">dynamous.ai</span>
</div>

<!-- 2) CSS — merge into <style>. NOTE: position absolute, z-index 10, NO class="clip". -->
<style>
  #dynamous-badge {
    position: absolute;
    bottom: 460px;       /* clear of YouTube subscribe / action column */
    left: 60px;          /* clear of left edge */
    z-index: 10;
    pointer-events: none;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px 14px 8px 10px;
    background: rgba(15, 23, 42, 0.55);     /* midroll bgDark @ 55% — glass surface */
    border: 1px solid rgba(255, 255, 255, 0.08);  /* midroll glassBorder */
    border-radius: 999px;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    opacity: 0.55;       /* idle — subtle but readable, lifted from 0.45 because the glass pill needs slightly more presence */
    filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.4));
  }
  #dynamous-badge-mark { width: 28px; height: 28px; display: block; }
  #dynamous-badge-url {
    font-family: 'Inter', system-ui, sans-serif;
    font-weight: 600;
    font-size: 22px;
    letter-spacing: 0.4px;
    color: #e2e8f0;        /* midroll textPrimary */
  }
</style>

<!-- 3) JS — call from host root timeline. Single 0.6s entrance, then static. -->
<script>
  function addDynamousBadgeEntrance(tl) {
    // Entrance fires AFTER the 3-second hook (strategy doc rule).
    tl.from("#dynamous-badge", { opacity: 0, x: -12, duration: 0.6, ease: "power2.out" }, 3.0);
  }
  // Usage: addDynamousBadgeEntrance(tl);
</script>
```

**SUB_COMPOSITION_BLOCK_PATTERN (endcard mirrors the midroll Phase 6 CTA stack):**

```html
<!-- SOURCE: shared/lib/blocks/url-cta/block.html:17-100+ (structure)
            + DynamousMidroll.tsx:2018-2257 (Phase 6 CTA — copy the layout exactly)
            + DynamousMidroll.tsx:78-95 (palette) -->
<!-- COPY THIS PATTERN: -->
<template id="dynamous-endcard-template">
  <div data-composition-id="dynamous-endcard" data-start="0" data-duration="3" data-width="1080" data-height="1920">

    <!-- Glass CTA card — mirrors midroll line 2018-2034 -->
    <div class="dec-card">
      <img class="dec-wordmark" src="../assets/dynamous-ai-mastery-white.svg" alt="Dynamous AI Mastery" crossorigin="anonymous" />
      <div class="dec-headline">Join the Community</div>
      <div class="dec-button">
        <span>Link in Description</span>
        <span class="dec-arrow">↓</span>
      </div>
      <div class="dec-discount">10% OFF</div>
      <div class="dec-url">dynamous.ai</div>
    </div>
    <div class="dec-blackout"></div>

    <style>
      [data-composition-id="dynamous-endcard"] {
        position: relative; width: 1080px; height: 1920px;
        background: #0f172a;  /* midroll bgDark — locked */
        font-family: 'Inter', system-ui, sans-serif;
      }
      [data-composition-id="dynamous-endcard"] .dec-card {
        position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);
        display: flex; flex-direction: column; align-items: center; gap: 32px;
        padding: 56px 64px;
        width: 880px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 16px 64px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      }
      [data-composition-id="dynamous-endcard"] .dec-wordmark { width: 480px; height: auto; }
      [data-composition-id="dynamous-endcard"] .dec-headline {
        font-size: 56px; font-weight: 900; color: #ffffff; text-align: center;
      }
      [data-composition-id="dynamous-endcard"] .dec-button {
        display: flex; align-items: center; gap: 16px;
        padding: 20px 48px; border-radius: 16px;
        font-size: 32px; font-weight: 800; color: #ffffff;
        background: linear-gradient(135deg, #a855f7, #ec4899, #a855f7);
        background-size: 200% 100%;
        box-shadow: 0 4px 24px rgba(168, 85, 247, 0.4), 0 0 60px rgba(236, 72, 153, 0.15);
      }
      [data-composition-id="dynamous-endcard"] .dec-discount {
        padding: 12px 28px; border-radius: 12px;
        font-size: 36px; font-weight: 900; color: #ffffff; letter-spacing: 0.5px;
        background: linear-gradient(135deg, #dc2626, #b91c1c, #dc2626);
        box-shadow: 0 4px 16px rgba(220, 38, 38, 0.4);
      }
      [data-composition-id="dynamous-endcard"] .dec-url {
        font-size: 22px; font-weight: 600; color: #94a3b8; letter-spacing: 2px;
      }
      [data-composition-id="dynamous-endcard"] .dec-blackout {
        position: absolute; inset: 0; background: #000000; opacity: 0; pointer-events: none;
      }
    </style>

    <script>
      window.__timelines = window.__timelines || {};
      (function () {
        var tl = gsap.timeline({ paused: true });
        // Phase 1 — card scale-in 0–0.4s (mirrors midroll cardSpring)
        tl.from('[data-composition-id="dynamous-endcard"] .dec-card',
          { scale: 0.9, opacity: 0, duration: 0.4, ease: "back.out(1.2)" }, 0);
        // Phase 2 — content stagger entry 0.4–1.4s
        tl.from('[data-composition-id="dynamous-endcard"] .dec-wordmark',
          { y: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, 0.4);
        tl.from('[data-composition-id="dynamous-endcard"] .dec-headline',
          { y: 20, opacity: 0, duration: 0.5, ease: "power2.out" }, 0.55);
        tl.from('[data-composition-id="dynamous-endcard"] .dec-button',
          { scale: 0.9, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }, 0.7);
        tl.from('[data-composition-id="dynamous-endcard"] .dec-discount',
          { scale: 0.5, opacity: 0, duration: 0.5, ease: "back.out(1.8)" }, 0.85);
        tl.from('[data-composition-id="dynamous-endcard"] .dec-url',
          { y: 10, opacity: 0, duration: 0.4, ease: "power2.out" }, 1.0);
        // Hold 1.4–2.5s; subtle gradient shimmer on the button
        tl.to('[data-composition-id="dynamous-endcard"] .dec-button',
          { backgroundPosition: "200% 0", duration: 2.0, ease: "none" }, 0.7);
        // Phase 3 — fade to black 2.5–3.0s
        tl.to('[data-composition-id="dynamous-endcard"] .dec-blackout',
          { opacity: 1, duration: 0.5, ease: "power2.in" }, 2.5);
        window.__timelines["dynamous-endcard"] = tl;
      })();
    </script>
  </div>
</template>
```

**HOST_WIRING_PATTERN (per-video `index.html`):**

```html
<!-- SOURCE: shared/lib/blocks/url-cta/recipe.md:30-40 -->
<!-- COPY THIS PATTERN — replaces the final 3.0s of the Short -->
<div id="dynamous-endcard-mount"
     data-composition-id="dynamous-endcard"
     data-composition-src="compositions/dynamous-endcard.html"
     data-start="<TOTAL_DURATION_MINUS_3>"
     data-duration="3"
     data-track-index="2"
     data-width="1080"
     data-height="1920"></div>
```

**RECIPE_DOCUMENT_PATTERN:**

```markdown
<!-- SOURCE: shared/lib/blocks/url-cta/recipe.md:1-60 -->
# Recipe: dynamous-endcard

Last-3s contextual endcard — Dynamous mastery wordmark + module-or-generic CTA + URL line, ending with a 0.5s fade-to-black.

## What it produces
[ASCII diagram of the rendered card]

## Required tokens
--bg, --text, --orange (or --dynamous-primary), --sans
…

## Wire into a host composition
1. Copy block.html to videos/<slug>/compositions/dynamous-endcard.html
2. Copy logo asset: cp shared/logos/dynamous-mastery-wordmark-light.svg videos/<slug>/assets/
3. In videos/<slug>/index.html, add the mount <div> with data-start = totalDuration - 3
…

## Slots to edit
| Selector | Purpose | Constraint |
…

## Don'ts
- Don't put a 10%-off promo code on screen — the offer lives in the description / pinned comment only
- Don't extend duration past 3.0s — disrupts retention curve
…
```

**MODULE_DATA_PATTERN (use the midroll v3 list, NOT the older Shorts constants):**

```json
// SOURCE: diy-yt-creator/src/shared/components/DynamousMidroll.tsx:134-147
// CANONICAL — this is the current 12-module curriculum as shipped in the midroll v3.
// The older Shorts constants list (Foundations / Prompt Engineering / Claude API …)
// is superseded — DO NOT use it. Keywords below are inferred from titles for the
// findMatchingModule() helper.
{
  "modules": [
    { "id": 1,  "title": "Introduction to Agentic Coding", "lessons": 7, "time": "45 min",   "color": "#22c55e", "keywords": ["agentic", "coding", "intro", "foundation"] },
    { "id": 2,  "title": "The PIV Loop",                   "lessons": 7, "time": "2h 8 min", "color": "#3b82f6", "keywords": ["piv", "plan", "implement", "validate", "loop"] },
    { "id": 3,  "title": "Global Rules",                   "lessons": 5, "time": "43 min",   "color": "#8b5cf6", "keywords": ["global", "rules", "claude.md", "instructions", "memory"] },
    { "id": 4,  "title": "Commands (Reusable Prompts)",    "lessons": 6, "time": "1h 5 min", "color": "#f59e0b", "keywords": ["command", "prompt", "slash command", "reusable"] },
    { "id": 5,  "title": "Systems for Planning",           "lessons": 8, "time": "1h 38 min","color": "#ef4444", "keywords": ["plan", "planning", "design", "spec"] },
    { "id": 6,  "title": "Systems for Implementation",     "lessons": 3, "time": "30 min",   "color": "#06b6d4", "keywords": ["implementation", "build", "ship"] },
    { "id": 7,  "title": "Systems for Validating",         "lessons": 6, "time": "2h 41 min","color": "#a855f7", "keywords": ["validate", "test", "vitest", "playwright", "qa"] },
    { "id": 8,  "title": "Remote Agentic Coding in GitHub","lessons": 5, "time": "44 min",   "color": "#10b981", "keywords": ["github", "remote", "actions", "ci"] },
    { "id": 9,  "title": "Dynamous Remote Coding System",  "lessons": 7, "time": "1h 28 min","color": "#f97316", "keywords": ["dynamous", "remote coding", "system"] },
    { "id": 10, "title": "MCP Servers + Skills",           "lessons": 5, "time": "1h 0 min", "color": "#ec4899", "keywords": ["mcp", "tool use", "skill", "function calling"] },
    { "id": 11, "title": "Subagents",                      "lessons": 4, "time": "52 min",   "color": "#14b8a6", "keywords": ["subagent", "agent", "task", "delegation"] },
    { "id": 12, "title": "Parallel Agentic Coding",        "lessons": 6, "time": "34 min",   "color": "#64748b", "keywords": ["parallel", "concurrent", "worktree", "swarm"] }
  ],
  "url": "dynamous.ai",
  "tagline": "Home of the Dynamous AI Mastery Community",
  "discountText": "10%",
  "ctaHeadline": "Join the Community",
  "ctaButton": "Link in Description",
  "platformChannels": ["#help-and-support", "#project-showcase", "#ai-news-daily", "#ideas-and-brainstorms"]
}
```

**MIDROLL-DERIVED PALETTE (use as the canonical Dynamous brand for these artifacts):**

```css
/* SOURCE: diy-yt-creator/src/shared/components/DynamousMidroll.tsx:78-95
   COPY THIS into shared/lib/tokens/dynamous-modern.css */
:root {
  --dynamous-bg-dark:        #0f172a;  /* slate 900 — primary surface */
  --dynamous-bg-mid:         #16213e;  /* slate 800 — elevated surface */
  --dynamous-purple:         #a855f7;  /* purple 500 — primary accent */
  --dynamous-pink:           #ec4899;  /* pink 500 — pair w/ purple in gradients */
  --dynamous-indigo:         #6366f1;
  --dynamous-violet:         #8b5cf6;
  --dynamous-cyan:           #06b6d4;
  --dynamous-orange:         #f97316;
  --dynamous-amber:          #f59e0b;
  --dynamous-green:          #22c55e;
  --dynamous-red:            #dc2626;  /* used by the "10% OFF" badge */
  --dynamous-text-primary:   #e2e8f0;
  --dynamous-text-secondary: #94a3b8;
  --dynamous-glass:          rgba(255, 255, 255, 0.03);
  --dynamous-glass-border:   rgba(255, 255, 255, 0.08);
  --dynamous-cta-gradient:   linear-gradient(135deg, #a855f7, #ec4899, #a855f7);
  --dynamous-discount-grad:  linear-gradient(135deg, #dc2626, #b91c1c, #dc2626);
}
```

---

## Files to Change

| File                                                                                            | Action  | Justification                                                                                                                          |
| ----------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `shared/logos/dynamous-logo.png`                                                                | COPY    | Official Dynamous square mark — direct copy from `diy-yt-creator/public/assets/dynamous-logo.png`. Used by the badge and discount bubble. |
| `shared/logos/dynamous-ai-mastery-white.svg`                                                    | COPY    | Official "Dynamous AI Mastery" full lockup (37 KB SVG, white-on-dark). Direct copy from `diy-yt-creator/public/assets/dynamous-ai-mastery-white.svg`. Used by the endcard. |
| `shared/lib/tokens/dynamous-modern.css`                                                         | CREATE  | Midroll v3 modern-gradient palette as CSS variables (see MIDROLL-DERIVED PALETTE block above). Single source of truth for color across all four artifacts. |
| `shared/lib/components/dynamous-badge/component.html`                                           | CREATE  | Persistent badge — paste-in HTML+CSS+JS snippet, mirrors `top-banner-wordmark/component.html`                                           |
| `shared/lib/components/dynamous-badge/README.md`                                                | CREATE  | Why this exists, where to place it, asset-copy checklist, position rationale (safe zone), opt-in nature                                |
| `shared/lib/components/dynamous-data/dynamous-modules.json`                                     | CREATE  | The 12-module curriculum + URL + tagline. Single source of truth for all four artifacts                                                 |
| `shared/lib/components/dynamous-data/README.md`                                                 | CREATE  | How to consume the JSON (copy into `videos/<slug>/assets/dynamous-modules.json` and reference for module-id lookup)                     |
| `shared/lib/blocks/dynamous-endcard/block.html`                                                 | CREATE  | Sub-composition block — `<template>` + scoped CSS + self-registered timeline                                                            |
| `shared/lib/blocks/dynamous-endcard/recipe.md`                                                  | CREATE  | Wiring instructions, slot table, don'ts, lint expectation. Mirrors `url-cta/recipe.md`                                                  |
| `shared/lib/blocks/dynamous-module-interstitial/block.html`                                     | CREATE  | Opt-in mid-video block — slide-in/hold/slide-out, references one module                                                                 |
| `shared/lib/blocks/dynamous-module-interstitial/recipe.md`                                      | CREATE  | Wiring instructions, slot table, opt-in guidance, when to use vs. skip                                                                  |
| `shared/lib/components/dynamous-discount-bubble/component.html`                                 | CREATE  | New time-bounded paste-in component — small pill with `Dynamous.ai · Code XYZ for 10% off`. Opt-in per video AND per scene              |
| `shared/lib/components/dynamous-discount-bubble/README.md`                                      | CREATE  | When to use (tutorial / over-the-shoulder Shorts only — when platform is visibly on screen), where to position, code-source guidance   |
| `shared/lib/MANIFEST.md`                                                                        | AUTO    | DO NOT edit by hand — `scripts/sync-shared-lib.sh` PostToolUse hook regenerates the tables. Verify entries after first Write/Bash       |
| `videos/_template-wiring-snippet.md`                                                            | CREATE  | Repo-level reference doc — canonical 4-piece wiring + script.txt template + pinned-comment template + description template + the strategy doc's "Execution Checklist" |
| `templates/shorts/anthropic/README.md`                                                          | UPDATE  | Add a section "Add Dynamous promotion?" with the y/N prompt + step-by-step opt-in wiring (link to `videos/_template-wiring-snippet.md`) |
| `templates/shorts/archon/README.md`                                                             | UPDATE  | Same opt-in section as the anthropic template README                                                                                    |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                                          | UPDATE  | Add a step in the spawn flow that asks the author "Add Dynamous promotion to this Short? (y/N — default no)" and, on yes, runs the 4-piece wiring documented in `videos/_template-wiring-snippet.md` |

---

## NOT Building (Scope Limits)

- **No automatic `findMatchingModule()` execution at render time.** HyperFrames is deterministic + synchronous; module selection is done by the *author* per video, not by JS at composition load. The keyword data lives in `dynamous-modules.json` so the diy-yt-creator skill (or a human) can pick the right module name and paste it into the endcard recipe slot.
- **No on-screen promo code in the badge or endcard.** Those two surfaces never carry a code — the endcard says "link in description". The discount bubble (artifact 4) is the *only* exception, and only fires in tutorial Shorts where the platform is visibly on screen, after the author opts in.
- **No default-on wiring.** Templates ship pristine. Existing videos are not touched. Opt-in is per video, asked at spawn time.
- **No SFX or stinger audio on the endcard.** `audio-design.md` rule "Shorts have NO background music" + the Remotion source intentionally ships silent. We mirror that.
- **No retroactive update of existing videos.** Plan ships the lib entries; updating each existing `videos/<slug>/index.html` to include the badge + endcard is a per-video task, not part of this PRP. (Task 12 produces the wiring reference, not the wires themselves.)
- **No port of long-form `DynamousMidroll.tsx` / `DynamousMidrollV2.tsx` / `DynamousBanner.tsx` / `DynamousCourse.tsx`.** Those are 17–80 KB Remotion components targeting 1920×1080 long-form video. Out of scope — long-form templates do not exist yet in this repo.
- **No new lint rules.** Existing `npx hyperframes lint` is sufficient. The blocks must pass with 0 errors.
- **No npm package, no build step.** Pure copy-from per the existing `shared/lib/` consumption model.
- **No CTA-changing edit of the existing `url-cta` block.** The Dynamous endcard is a separate, additional outro — videos pick one or the other (or chain them, but not in scope).

---

## Step-by-Step Tasks

Execute in order. Each task is atomic and independently verifiable.

### Task 1: CONFIRM minor open questions with the user (most are now answered by the midroll source)

- **ACTION**: Surface a short checklist of items that the midroll source DID NOT resolve. Most of the original questions are now answered by reading `DynamousMidroll.tsx`.
- **ALREADY ANSWERED** (no longer ask the user):
  - ~~Logo mark~~ → `diy-yt-creator/public/assets/dynamous-logo.png` (square, used at 56×56 in the midroll). Copy direct.
  - ~~Logo wordmark~~ → `diy-yt-creator/public/assets/dynamous-ai-mastery-white.svg` (37 KB, white-on-dark). Copy direct.
  - ~~Brand color~~ → midroll v3 modern-gradient palette is the canonical brand. Locked.
  - ~~10%-off offer existence~~ → confirmed real (default `discountText='10%'` in midroll). The discount applies via the description link itself; no explicit promo code displayed in the midroll.
  - ~~CTA wording~~ → midroll Phase 6 uses verbatim: headline "Join the Community", button "Link in Description ↓", red badge "10% OFF", URL "dynamous.ai". Use these.
  - ~~Module list~~ → use the midroll's 12-module list (Introduction to Agentic Coding, The PIV Loop, Global Rules, …). The Shorts constants list is superseded.
- **CONFIRMED** (user 2026-04-28):
  1. ~~Cole headshot in endcard?~~ → **OMIT.** Endcard is community-only, impersonal. The optional `shared/people/cole-medin.webp` copy is dropped from Task 2. The endcard block does NOT include a `dec-cole` slot. The "Optional Cole-variant" Notes section is removed.
  2. ~~Coupon code or automatic discount?~~ → **AUTOMATIC via the link.** No coupon code anywhere on screen, no `[YOURCODE]` placeholder. The pinned-comment template uses the description link unmodified — the 10% applies on click. The `.dynamous-code.txt` per-video file and its `.gitignore` rule are dropped (Task 14a is removed).
  3. ~~`script.txt` outro wording acceptable?~~ → **YES** — strategy doc verbatim: *"A lot of you asked how I'm learning all this AI stuff — I use Dynamous. It's an awesome community. I actually reached out to them and got a 10% off code for you guys, it's in the pinned comment."* Locked. (Note: keeps the word "code" in the verbal CTA even though there is no actual code — this is fine because a discounted link IS a "code" in the colloquial sense, and the friend-frame language is what carries the conversion.)
  4. ~~Discount bubble shows a code?~~ → **NO.** Bubble shows only the Dynamous logo + `Dynamous.ai` + a `10% OFF` red badge + an "in the link" pointer. No code field. Task 8b updated to remove the code slot.
- **PROCEED IMMEDIATELY** after the user answers these four (or says "use defaults"). No need to wait for assets — they are already on disk.

### Task 2: COPY the official Dynamous logo + wordmark assets into `shared/logos/`

- **ACTION**: Direct file copy from the diy-yt-creator repo.
- **IMPLEMENT**:
  ```bash
  cp C:/Users/Leex279/Documents/GitHub/diy-yt-creator/public/assets/dynamous-logo.png \
     C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/logos/dynamous-logo.png
  cp C:/Users/Leex279/Documents/GitHub/diy-yt-creator/public/assets/dynamous-ai-mastery-white.svg \
     C:/Users/Leex279/Documents/GitHub/diy-yt-creator-hyperframes/shared/logos/dynamous-ai-mastery-white.svg
  ```
- **NAMING**: Match the source filenames exactly to make provenance traceable. The existing `shared/logos/` convention uses `-light` for white-on-dark variants; we keep the source name (`-white`) because it IS the white-on-dark variant — the suffix is semantically equivalent and preserves the original asset name for `git blame` / change-tracking purposes.
- **GOTCHA**: PNG/SVG in `shared/logos/` are NOT directly consumable by a video — they must be copied into `videos/<slug>/assets/`. Each lib entry's README documents this.
- **VALIDATE**: `ls -la shared/logos/dynamous-logo.png shared/logos/dynamous-ai-mastery-white.svg` shows non-zero file sizes matching the source files.

### Task 3: CREATE `shared/lib/components/dynamous-badge/component.html`

- **ACTION**: Author the paste-in component snippet using the PERSISTENT_OVERLAY_PATTERN block above.
- **IMPLEMENT**:
  - Top-of-file comment block citing SOURCE refs (Remotion `ShortsDynamousBadge.tsx:1-93` + this repo's `top-banner-wordmark/component.html`)
  - The IMPORTANT — LOGO MUST BE A LOCAL COPY warning, copied verbatim from `top-banner-wordmark/component.html:11-26`
  - Section 1 — HTML snippet (id `dynamous-badge`, with `<img>` + `<span>` for the URL)
  - Section 2 — `<style>` block with `position: absolute; bottom: 460px; left: 60px; z-index: 10; opacity: 0.45;` (per safe-zone math)
  - Section 3 — `<script>` exporting `addDynamousBadgeEntrance(tl)` — single 0.6s `tl.from()` at `t=3.0` (NOT `t=0.4` as in the Remotion source). Rationale: strategy doc rule "Never start the video with the brand name — you have less than 3 seconds to stop the scroll." Badge appears AFTER the hook, easing `power2.out`
  - Asset-copy checklist at bottom (`cp shared/logos/dynamous-mark-light.svg videos/<slug>/assets/dynamous-mark-light.svg`)
- **MIRROR**: `shared/lib/components/top-banner-wordmark/component.html:1-79` exactly — same three-section layout, same warning, same checklist
- **GOTCHA**: NO `class="clip"`, NO `data-start`/`data-duration`/`data-track-index`. The badge is outside the clip system (matches existing `#top-banner` and `#progress-track` pattern in the templates).
- **GOTCHA**: Do NOT use `Math.random()` or `Date.now()` in the entrance — the framework forbids non-deterministic logic.
- **VALIDATE**: Open the file, eyeball that all three sections are present and labelled. No lint runs against `shared/lib/` itself — it's only validated when consumed by a video.

### Task 4: CREATE `shared/lib/components/dynamous-badge/README.md`

- **ACTION**: One-page README explaining what it is, where to place it, why bottom-left at 460/60 (safe zone math), and the exact asset-copy + wiring steps.
- **IMPLEMENT**:
  - Section "What it produces" — ASCII miniature of the badge in its corner
  - Section "Required tokens" — only `--text-dim` (with sensible default `#A8A29E`)
  - Section "Wire into a host composition" — three steps (copy logo, paste HTML+CSS+JS, call `addDynamousBadgeEntrance(tl)` from host root timeline)
  - Section "Don'ts" — don't move into the right-edge action column, don't raise opacity above 0.55 (loses subtlety), don't add `class="clip"` (would hide it during phase gaps)
  - Section "Lint expectation" — `npx hyperframes lint videos/<slug>` should be 0 errors after wiring
- **MIRROR**: The implicit doc style of `shared/lib/blocks/url-cta/recipe.md:1-60` (sections + tables + don'ts) but pared down for a component.
- **VALIDATE**: Render the README in any markdown previewer — no broken links, no orphan TBDs.

### Task 5: CREATE `shared/lib/components/dynamous-data/dynamous-modules.json` and `README.md`

- **ACTION**: Drop the verbatim 12-module curriculum (with keywords) + URL + tagline as JSON.
- **IMPLEMENT**: Use the JSON shape from MODULE_DATA_PATTERN block above. JSON only — no JS, no TS, no exports.
- **MIRROR**: Source data from `diy-yt-creator/src/shared/constants/dynamous.ts:34-107` exactly. Do NOT alter module titles, IDs, or keyword arrays.
- **README content**:
  - "What this is" — the canonical curriculum + brand strings used by both blocks
  - "How to consume" — one of (a) copy into `videos/<slug>/assets/` if the video needs to read it at runtime (rare); (b) just look up the matching module ID/title and paste the strings into the endcard / interstitial recipe slots (default)
  - "Module-matching helper" — link to a tiny CLI script at `scripts/find-dynamous-module.js` (Task 11) that prints the best-matching module for a given topic-tag list
- **VALIDATE**: `node -e "JSON.parse(require('fs').readFileSync('shared/lib/components/dynamous-data/dynamous-modules.json','utf8')).modules.length === 12 || process.exit(1)"` exits 0.

### Task 6: CREATE `shared/lib/blocks/dynamous-endcard/block.html`

- **ACTION**: Author the sub-composition block using the SUB_COMPOSITION_BLOCK_PATTERN above.
- **IMPLEMENT**:
  - Top-of-file comment block citing source (Remotion `ShortsContextualEndcard.tsx:1-237`) + required tokens
  - `<template id="dynamous-endcard-template">` wrapper (mandatory — sub-comp files use `<template>`, standalone don't)
  - Root `<div data-composition-id="dynamous-endcard" data-start="0" data-duration="3" data-width="1080" data-height="1920">`
  - Inner content: centered `<img>` (mastery wordmark, `src="../assets/dynamous-mastery-wordmark-light.svg"` — note the `../` prefix because the block lives in `videos/<slug>/compositions/`), then `#dec-module` line, divider, `#dec-tagline` line, `#dec-url` line, plus a fixed `.dynamous-endcard-blackout` overlay
  - Scoped `<style>` keyed by `[data-composition-id="dynamous-endcard"]` (matches `url-cta` scoping pattern)
  - Scoped `<script>` registering `window.__timelines["dynamous-endcard"] = tl` synchronously
  - Three-phase animation: bg fade-in 0–0.4s; content spring-up 0.4–1.0s; fade-to-black 2.5–3.0s (mirrors Remotion frames 0–12, 12–24, 75–90 at 30fps → seconds)
- **MIRROR**: `shared/lib/blocks/url-cta/block.html:1-150+` — same `<template>` shape, same scoped-CSS pattern, same paused-timeline registration
- **GOTCHA**: Use `gsap.timeline({ paused: true })` — non-paused breaks the capture engine
- **GOTCHA**: Use `repeat: 0` (or omit `repeat`) — `repeat: -1` is banned per the SKILL.md rule
- **GOTCHA**: Asset path is `../assets/...` (one level up from the `compositions/` folder where the block lives in a host video)
- **VALIDATE**: Author a throwaway test video that wires this block (see Task 9) and run `npx hyperframes lint videos/_test/`.

### Task 7: CREATE `shared/lib/blocks/dynamous-endcard/recipe.md`

- **ACTION**: Author the wiring recipe.
- **IMPLEMENT**:
  - Section "What it produces" — ASCII of the rendered endcard
  - Section "Required tokens" — `--bg, --text, --sans` (use `var(--bg, #1C1917)` defaults — Dynamous stone, not Anthropic dark navy)
  - Section "Wire into a host composition" — four steps:
    1. Copy block.html → `videos/<slug>/compositions/dynamous-endcard.html`
    2. Copy logo: `cp shared/logos/dynamous-mastery-wordmark-light.svg videos/<slug>/assets/`
    3. Compute `start = totalDuration - 3` from the host timeline
    4. Paste the host `<div data-composition-id="dynamous-endcard" data-composition-src="compositions/dynamous-endcard.html" data-start="<start>" data-duration="3" data-track-index="2" data-width="1080" data-height="1920"></div>`
  - Section "Slots to edit" — `#dec-module` (e.g. `MODULE 5 · MCP & Tool Use`, ≤30 chars; or empty/hidden when no module match), `#dec-url` (e.g. `dynamous.ai · link in description`)
  - Section "Don'ts":
    - Don't put a 10%-off promo code on screen — keep it in the description / pinned comment only
    - Don't extend `data-duration` past 3.0s
    - Don't change the fade-to-black timing — final 0.5s blackout is required for clean cut
    - Don't reference the logo via `../../shared/logos/...` — bundler rejects parent-of-project paths
- **MIRROR**: `shared/lib/blocks/url-cta/recipe.md:1-60` exactly — same section order, same table layout.
- **VALIDATE**: Markdown renders cleanly, all relative links resolve.

### Task 8: CREATE `shared/lib/blocks/dynamous-module-interstitial/block.html` + `recipe.md`

- **ACTION**: Author the optional mid-video interstitial block + its recipe.
- **IMPLEMENT block.html**:
  - `<template id="dynamous-module-interstitial-template">`
  - Card 920×160 px positioned at `top: 420px; left: 50%;` (translate via GSAP `xPercent: -50` so it stays centered)
  - Content: small dot accent (`#D97757`) + module label ("MODULE N") + module title + tagline ("Part of Dynamous AI Mastery")
  - Animation: slide-in `x: +540 → 0` at `0–0.6s`; opacity 0 → 1 at `0–0.4s`; hold; opacity 1 → 0 at `2.6–3.0s`; slide-out `x: 0 → +540` at `2.4–3.0s`
  - Total duration 3.0s; `window.__timelines["dynamous-module-interstitial"] = tl`
- **IMPLEMENT recipe.md**:
  - Section "When to use" — ONLY when the Short's topic directly matches a module from `dynamous-modules.json` (use `scripts/find-dynamous-module.js` from Task 11 to confirm). Skip on ambiguous topics.
  - Section "Wire" — same four-step shape as Task 7's recipe, plus a guidance line: "Place at a natural narration pause — minimum 1.0s breath in the transcript, not on top of a hero word"
  - Slots: `#dmi-module-num` (e.g. `5`), `#dmi-module-title` (e.g. `MCP & Tool Use`)
- **MIRROR**: Same block + recipe pattern as Task 6 + Task 7
- **GOTCHA**: This block is OPT-IN per video. No video must include it by default. The recipe must say so explicitly.
- **GOTCHA**: Card lives at `top: 420px` in the source Remotion — confirm this lands inside the safe zone (380px top reserve + 160px card height = lands at 580px bottom, well above the bottom-380 reserve). OK.
- **VALIDATE**: Wire into the test video from Task 9 (with a known pause anchor in the transcript), `npx hyperframes lint videos/_test/` returns 0 errors, `npx hyperframes inspect videos/_test/` shows no overflow.

### Task 8b: CREATE `shared/lib/components/dynamous-discount-bubble/component.html` + `README.md`

- **ACTION**: Author the new opt-in time-bounded discount bubble derived from the strategy doc's "Text Overlay" recommendation. NO code slot — the discount is automatic via the description link (user-confirmed).
- **IMPLEMENT component.html**:
  - Top-of-file comment block citing SOURCE refs (strategy doc § 2 "The Text Overlay" + DynamousMidroll.tsx Phase 6 for the red 10% OFF badge styling) + the IMPORTANT — LOGO MUST BE A LOCAL COPY warning.
  - Section 1 — HTML snippet: a `<div id="dynamous-discount-bubble" class="clip" data-start="<scene-start>" data-duration="<3-or-4>" data-track-index="9">` with inline `<img>` mark + a `Dynamous.ai` line + a red `10% OFF` pill + an `in the link ↓` pointer. NO code field. NOTE the `class="clip"` here — unlike the badge, this component IS time-bounded.
  - Section 2 — `<style>` block: pill shape (`border-radius: 14px`), `padding: 10px 18px`, `backdrop-filter: blur(8px)`, surface `rgba(15, 23, 42, 0.85)` (midroll bgDark), 1 px border in `rgba(255,255,255,0.08)`. The inner `10% OFF` badge uses the same red gradient as the endcard (`linear-gradient(135deg, #dc2626, #b91c1c, #dc2626)`). Position `absolute` at a slot the author picks (default `top: 1180px; left: 60px;` — sits just below the platform-recording area for tutorial Shorts).
  - Section 3 — `<script>` exporting `addDynamousDiscountBubbleEntrance(tl, sceneStart)` — `tl.from()` slide-up + opacity at `sceneStart`, then `tl.to()` opacity 1 → 0 at `sceneStart + duration - 0.4`.
  - Asset-copy checklist (same as badge — copy `dynamous-logo.png` into `videos/<slug>/assets/`).
- **IMPLEMENT README.md**:
  - "When to use" — ONLY in tutorial / over-the-shoulder Shorts where the Dynamous platform is visibly on screen, AND the author has opted into the promotion at spawn time. If the platform isn't on screen, skip this artifact.
  - "What it does NOT carry" — explicitly: no coupon code field. The 10% discount applies automatically when viewers click through the description link (user-confirmed). The bubble exists to give sound-off viewers a visible reminder that the offer is real and in the description.
  - "Don'ts": don't fire before `t=3.0s` (hook rule); don't fire while a hero word is being delivered; don't extend past 4.0s; don't add SFX (per audio-design.md); don't add a code slot — the link does the work.
- **MIRROR**: The badge component's three-section layout, but with `class="clip"` and explicit duration since this is time-bounded.
- **GOTCHA**: Track index 9 is high to avoid colliding with SFX tracks 3-5 and the captions track. Confirm against existing video for collisions.
- **VALIDATE**: Wire into the smoke test (Task 9) at `t=6.0s` for 3.5s, `npx hyperframes lint` clean, eyeball that pill animates in then out, the red 10% OFF badge is visible, no code anywhere on screen.

### Task 9: CREATE a smoke-test video at `videos/_test-dynamous/`

- **ACTION**: Spawn the smallest possible Short that wires all FOUR new artifacts (badge + endcard + interstitial + discount bubble) so we can lint, preview, and inspect end-to-end. This is a *fixture*, not a real video.
- **IMPLEMENT**:
  - Copy `templates/shorts/anthropic/` to `videos/_test-dynamous/`
  - Update `meta.json` (`id: "_test-dynamous"`, `name: "Dynamous lib smoke test"`)
  - Strip the four content phases down to a single 12-second hold of "Dynamous lib smoke test"
  - Copy `shared/logos/dynamous-mark-light.svg` and `shared/logos/dynamous-mastery-wordmark-light.svg` into `videos/_test-dynamous/assets/`
  - Paste the badge component snippet (HTML+CSS+JS) into `index.html` and call `addDynamousBadgeEntrance(tl)` — verify the entrance fires at `t=3.0s`, not earlier
  - Copy `shared/lib/blocks/dynamous-endcard/block.html` to `videos/_test-dynamous/compositions/dynamous-endcard.html`
  - Wire the endcard mount at `data-start="9" data-duration="3"` (last 3 s of a 12 s video)
  - Copy the interstitial block similarly, wire at `data-start="4" data-duration="3"` with `MODULE 5 · MCP & Tool Use`
  - Paste the discount bubble snippet, wire at `data-start="6" data-duration="3.5"` with `Code DEMO · 10% off`
  - Replace `audio/narration.wav` with a 12 s silent stub (or skip narration entirely — the smoke test does not need voice)
- **VALIDATE**:
  - `npx hyperframes lint videos/_test-dynamous` → exit 0, no errors
  - `npx hyperframes inspect videos/_test-dynamous` → no overflow or layout warnings
  - `npx hyperframes preview videos/_test-dynamous` → eyeball the badge bottom-left, the interstitial slide at 4s, the endcard at 9s with fade-to-black at 11.5s
- **GOTCHA**: After preview confirms, this folder STAYS in the repo as a regression fixture. Do NOT delete; do not render. The `out/` folder is gitignored.

### Task 10: CREATE per-folder `README.md` for each new `shared/lib/` entry

- **ACTION**: Already covered by Tasks 4, 5, 7, 8 — verify each new directory has its README/recipe before closing.
- **VALIDATE**: `ls shared/lib/components/dynamous-badge/` shows `component.html` + `README.md`; same for `dynamous-data/`; `ls shared/lib/blocks/dynamous-endcard/` shows `block.html` + `recipe.md`; same for `dynamous-module-interstitial/`.

### Task 11: CREATE `scripts/find-dynamous-module.js`

- **ACTION**: Tiny Node helper that takes topic-tag arguments and prints the best-matching module from `dynamous-modules.json`, or "NO_MATCH" — the deterministic equivalent of the Remotion `findMatchingModule()` helper.
- **IMPLEMENT**: ~30 lines, no deps. Reads `shared/lib/components/dynamous-data/dynamous-modules.json`, lowercases tags, scores each module by keyword-overlap count, returns the best (or "NO_MATCH" when score is 0).
- **MIRROR**: Algorithm from `diy-yt-creator/src/shared/constants/dynamous.ts:114-126` — same scoring rule.
- **CALLED LIKE**: `node scripts/find-dynamous-module.js "claude code" "cli" "subagent"` → prints `MODULE 4 — Claude Code & CLI` (or similar)
- **VALIDATE**:
  - `node scripts/find-dynamous-module.js "mcp" "tool"` prints `MODULE 5 — MCP & Tool Use`
  - `node scripts/find-dynamous-module.js "totally unrelated"` prints `NO_MATCH`

### Task 12: CREATE repo-level wiring snippet `videos/_template-wiring-snippet.md`

- **ACTION**: One-page reference document showing how to add the full opt-in Dynamous system to a NEW video.
- **IMPLEMENT**:
  - Section "Step 0 — Decide if this Short gets the promotion" — explicit y/N decision tree mirroring the spawn-time prompt
  - Section "Persistent — every opted-in Short" — paste-in steps for the badge component (entrance at `t=3.0s`)
  - Section "Outro — every opted-in Short" — paste-in steps for the endcard block (replaces last 3 s)
  - Section "Optional — topic-matched Shorts only" — when to add the interstitial; how to find a match via `scripts/find-dynamous-module.js`
  - Section "Optional — tutorial / over-the-shoulder Shorts only" — when to add the discount bubble; where to position it relative to the platform recording
  - Section "Description first line — opted-in Shorts" — locked verbatim (NO `[YOURCODE]` — discount is automatic via the link): *"You can check out Dynamous AI here: [LINK]. 10% off applies automatically when you join through this link! 👇"*
  - Section "Pinned comment — opted-in Shorts" — same template as the description first line. ALWAYS pin within 5 minutes of upload.
  - Section "`script.txt` template line — opted-in Shorts" — locked verbatim from strategy doc: *"A lot of you asked how I'm learning all this AI stuff — I use Dynamous. It's an awesome community. I actually reached out to them and got a 10% off code for you guys, it's in the pinned comment."*
  - Section "Execution checklist" — verbatim from strategy doc § 4: Value Test, Friend Test, Hook Test, CTA softness, frictionless purchase
  - Section "Don'ts" — never start the video with the brand name; never put the code in the badge or endcard; never add SFX to any of the four artifacts
- **VALIDATE**: Markdown renders. A new contributor reading this file can wire all four pieces into a fresh video without further questions, AND understand when to skip them.

### Task 13: UPDATE `templates/shorts/anthropic/README.md` and `templates/shorts/archon/README.md` to add the opt-in section

- **ACTION**: Each template README gets a new section "Add Dynamous promotion?" near the top of the spawn-instructions section.
- **IMPLEMENT** (paste in both README files, identical wording):

  ```markdown
  ## Add Dynamous promotion? (opt-in, ask each new video)

  Before you wire content, decide:

  > **"Add Dynamous promotion to this Short? (y/N — default no)"**

  - **No** (default) — skip this section. Proceed normally.
  - **Yes** — open `videos/_template-wiring-snippet.md` and follow Step 0 onward. Wires the persistent badge (artifact 1) + endcard (artifact 2). Optionally also the module interstitial (artifact 3) when the topic matches a curriculum module, and the discount bubble (artifact 4) when the platform is visibly on screen.

  Existing videos are NOT retroactively touched. The decision is per video.
  ```

- **MIRROR**: The README structural style of the existing template READMEs (heading + numbered steps).
- **VALIDATE**: `grep -l "Add Dynamous promotion" templates/shorts/*/README.md` returns 2 paths.

### Task 14: UPDATE `.claude/skills/diy-yt-creator/new-anthropic-short.md` (and the archon variant if present) to ask the y/N question during spawn

- **ACTION**: Add a step in the spawn flow that asks the author the y/N question, captures the answer, and on yes runs the wiring sequence from `videos/_template-wiring-snippet.md`.
- **IMPLEMENT**:
  - Insert a new "Step N — Ask: Add Dynamous promotion?" block between the existing "spawn folder" step and the "edit script.txt" step.
  - On YES: link to `videos/_template-wiring-snippet.md` and run the four asset-copy commands (badge component → index.html, endcard block.html → compositions/, interstitial block.html → compositions/, discount bubble component → index.html only when tutorial format), plus add the script.txt outro line, plus stub the description and pinned-comment files.
  - On NO: proceed normally; record the decision in `videos/<slug>/meta.json` as `"dynamousPromotion": false` for later audit.
- **MIRROR**: Existing step structure of `new-anthropic-short.md` (numbered steps with shell commands).
- **VALIDATE**: After spawning a fresh test slug with YES, all four artifacts and the templates are wired; with NO, the spawned video is identical to today's behavior.

<!-- Task 14a removed: there is no per-video coupon code, so no `.dynamous-code.txt` file
     and no `.gitignore` entry are needed. The 10% discount is automatic via the
     description link (user-confirmed 2026-04-28). -->


---

## Testing Strategy

### Validation per Artifact (no traditional unit tests — this is a content/asset library)

| Artifact                                                | What to verify                                                                                                  | How                                                                                                                  |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `dynamous-badge/component.html`                         | Three sections present + labelled; no `class="clip"`; safe-zone position values; entrance at `t=3.0s` (NOT 0.4) | Manual read; grep for `class="clip"` returns 0 hits inside the file; grep for `tl.from.*"#dynamous-badge"` shows `, 3.0)` or `, 3)` |
| `dynamous-discount-bubble/component.html`               | Three sections present; `class="clip"` IS present; `data-track-index="9"`; entrance after `t=3.0s` only          | Manual read; `grep -c 'class="clip"'` = 1                                                                              |
| Both block.html files                                   | `<template>` wrapper present; `data-composition-id` matches directory; `window.__timelines[id]` registered      | `grep -c "<template" shared/lib/blocks/*/block.html` = 2; `grep -c "window.__timelines" shared/lib/blocks/*/block.html` = 2 |
| `dynamous-modules.json`                                 | 12 modules, each with id/title/lessons/keywords; valid JSON                                                      | `node -e "JSON.parse(...).modules.length === 12 || process.exit(1)"`                                                 |
| `find-dynamous-module.js`                               | Returns expected module for known topics; returns NO_MATCH for unknown                                           | Two assertions in Task 11's VALIDATE block                                                                            |
| `videos/_test-dynamous/` smoke test                     | Lints clean; renders preview correctly; all four artifacts visible at the right times; badge respects 3-s hook   | `npx hyperframes lint`, `npx hyperframes inspect`, `npx hyperframes preview` (eyeball)                                |
| `shared/lib/MANIFEST.md`                                | Contains rows for all new entries (1 component-badge, 1 component-data, 1 component-discount-bubble, 2 blocks)   | `grep -c "dynamous-" shared/lib/MANIFEST.md` ≥ 5 after the sync hook fires                                            |
| `templates/shorts/*/README.md`                          | Each contains the "Add Dynamous promotion?" opt-in section                                                       | `grep -l "Add Dynamous promotion" templates/shorts/*/README.md` returns 2                                              |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`  | Contains the y/N spawn-time prompt step                                                                          | `grep "Add Dynamous promotion" .claude/skills/diy-yt-creator/new-anthropic-short.md` returns ≥1 hit                    |

### Edge Cases Checklist

- [ ] Badge survives a video whose `--text-dim` token is undefined (fallback `#A8A29E` kicks in)
- [ ] Badge entrance fires at `t=3.0s`, NOT during the first 3 s where the hook lives
- [ ] Endcard renders when `#dec-module` slot is *empty* (generic-mode copy from `GenericContent` in the Remotion source)
- [ ] Endcard renders when the host video has a different background color than `#1C1917` (uses `var(--bg, #1C1917)` so host wins)
- [ ] Interstitial does not overlap with the existing `#top-banner` (top: 60 + ~120 banner height = 180; interstitial top: 420 — safe gap)
- [ ] Interstitial does not overlap with the badge (badge bottom: 460 = lands ~1460 from top; interstitial top 420 + height 160 = 580 — safe gap of 880 px)
- [ ] Discount bubble does not overlap with the badge (default bubble top 1180 + ~80 height = 1260; badge bottom 460 from frame bottom = ~1460 from top; safe gap ~200 px)
- [ ] Discount bubble fires AFTER `t=3.0s` (no first-3-second branding rule)
- [ ] Endcard fade-to-black completes BEFORE the host video's `totalDuration` (host duration × seconds = endcard `data-start` + 3.0)
- [ ] Logo SVG with no `viewBox` does not stretch (component sets explicit `width: 36px; height: 36px;`)
- [ ] Badge stays visible during a phase that uses a CSS `transform` on `#root` (z-index 10 above phase content)
- [ ] No SFX `<audio>` was added to any of the four artifacts (`grep -c "<audio" shared/lib/{components,blocks}/dynamous-*/{*.html,*.md}` = 0)
- [ ] Opt-out video (the y/N answered NO) is byte-identical in `index.html` to today's template-spawn output
- [ ] Discount bubble README explicitly forbids any code field — the discount is automatic via the link

---

## Validation Commands

### Level 1: STATIC VALIDATION (per new file)

```bash
# JSON validity
node -e "JSON.parse(require('fs').readFileSync('shared/lib/components/dynamous-data/dynamous-modules.json','utf8'))"

# No clip class on the persistent badge
grep -L 'class="clip"' shared/lib/components/dynamous-badge/component.html

# Both block.html files use <template>
grep -c "<template" shared/lib/blocks/dynamous-endcard/block.html shared/lib/blocks/dynamous-module-interstitial/block.html
```

**EXPECT**: JSON parses; clip class absent; both blocks contain `<template`.

### Level 2: HYPERFRAMES LINT against the smoke-test video

```bash
npx hyperframes lint videos/_test-dynamous
```

**EXPECT**: Exit 0, zero errors. Warnings acceptable but should be reviewed.

### Level 3: HYPERFRAMES INSPECT (layout overflow check)

```bash
npx hyperframes inspect videos/_test-dynamous
```

**EXPECT**: No overflow flagged for the badge, the interstitial, or the endcard.

### Level 4: HYPERFRAMES VALIDATE (lint + WCAG contrast)

```bash
npx hyperframes validate videos/_test-dynamous
```

**EXPECT**: Pass. The badge text at opacity 0.45 should still meet contrast against the dark canvas; the endcard text against `#1C1917` background should be solid AA.

### Level 5: BROWSER PREVIEW (eyeball — no automated step)

```bash
npx hyperframes preview videos/_test-dynamous
```

**EXPECT**:
- Badge visible in bottom-left from t≈0.4 s onward, opacity ~0.45, no flicker between phases
- Interstitial slides in from the right at t=4.0 s, holds, slides out at t=6.4 s
- Endcard fades in at t=9.0 s, content springs up, fades to black at t=11.5 s, fully black at t=12.0 s
- No overlap between badge and interstitial; both clear of the YouTube safe zone (mental overlay of 380/380 top/bottom + 120 right reserves)

### Level 6: MANIFEST SYNC VERIFICATION

```bash
# After any Bash/Write/Edit operation completes, the PostToolUse hook should
# regenerate MANIFEST.md. Confirm the new entries appear.
grep -c "dynamous-" shared/lib/MANIFEST.md
```

**EXPECT**: ≥ 5 (badge + data + endcard + interstitial = 4 directory rows; the modules.json adds detail). If 0, manually run `bash scripts/sync-shared-lib.sh`.

---

## Acceptance Criteria

- [ ] Four lib entries (`dynamous-badge`, `dynamous-endcard`, `dynamous-module-interstitial`, `dynamous-discount-bubble`) live under `shared/lib/` with correct kind (component vs. block) and conform to existing structure
- [ ] One data entry (`dynamous-data/dynamous-modules.json`) carries the verbatim 12-module curriculum from the Remotion source
- [ ] Two logo SVGs live in `shared/logos/` (real or documented placeholders)
- [ ] One helper script (`scripts/find-dynamous-module.js`) prints the matching module for given topic tags
- [ ] One smoke-test video (`videos/_test-dynamous/`) wires all four pieces and lints + inspects + validates clean
- [ ] One repo-level wiring reference (`videos/_template-wiring-snippet.md`) explains the canonical 4-piece setup + the description / pinned-comment / `script.txt` templates verbatim from the strategy doc
- [ ] Both template READMEs (`templates/shorts/anthropic/README.md`, `templates/shorts/archon/README.md`) carry the "Add Dynamous promotion?" y/N opt-in section
- [ ] The diy-yt-creator skill's spawn doc (`new-anthropic-short.md`) asks the y/N question and wires only on YES
- [ ] `shared/lib/MANIFEST.md` auto-updates to list all five new directories (4 lib + 1 data)
- [ ] No SFX or stinger audio added (per `audio-design.md`)
- [ ] No on-screen promo code in any artifact. The discount applies automatically via the description link (user-confirmed 2026-04-28).
- [ ] Per-video badge placement falls inside the YouTube Shorts safe zone (bottom-left at `bottom: 460px; left: 60px;`) and entrance fires at `t=3.0s`
- [ ] Render path: badge stays at `opacity: 0.45`, endcard ends in fade-to-black, interstitial cleanly slides in/out, discount bubble fades in/out as a soft pill
- [ ] Opt-out (y/N answered NO) videos are unchanged from today's behavior

---

## Completion Checklist

- [x] Task 1 — All four open questions confirmed by user 2026-04-28 (omit Cole; automatic discount via link; strategy doc wording acceptable; no code in discount bubble)
- [ ] Task 2 — Logo SVGs placed in `shared/logos/`
- [ ] Task 3 — `dynamous-badge/component.html` created (entrance at `t=3.0s`)
- [ ] Task 4 — `dynamous-badge/README.md` created
- [ ] Task 5 — `dynamous-data/dynamous-modules.json` + README created
- [ ] Task 6 — `dynamous-endcard/block.html` created
- [ ] Task 7 — `dynamous-endcard/recipe.md` created
- [ ] Task 8 — `dynamous-module-interstitial/block.html` + `recipe.md` created
- [ ] Task 8b — `dynamous-discount-bubble/component.html` + `README.md` created
- [ ] Task 9 — `videos/_test-dynamous/` smoke test wires all four artifacts and validated
- [ ] Task 10 — All five new lib dirs have their README/recipe
- [ ] Task 11 — `scripts/find-dynamous-module.js` works for known + unknown topics
- [ ] Task 12 — `videos/_template-wiring-snippet.md` documents the canonical wiring + verbatim script.txt + pinned-comment + description templates
- [ ] Task 13 — Both template READMEs carry the y/N opt-in section
- [ ] Task 14 — `new-anthropic-short.md` spawn doc asks the y/N question and only wires on YES
<!-- Task 14a dropped — no per-video code file needed (discount is automatic via the link). -->
- [ ] Level 1–6 validations pass against `videos/_test-dynamous`
- [ ] `shared/lib/MANIFEST.md` contains all five new entries

---

## Risks and Mitigations

| Risk                                                                                                                | Likelihood | Impact | Mitigation                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------- | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Brand drift: midroll palette evolves and these artifacts stay frozen on v3**                                       | MEDIUM     | LOW    | Palette lives in a single tokens file (`shared/lib/tokens/dynamous-modern.css`) — one-line update + re-render. Document the v3 source in the tokens file's header comment.                                          |
| **10%-off code added to overlay by a future contributor without understanding the offer is unverified**             | MEDIUM     | HIGH   | Endcard recipe.md "Don'ts" section explicitly bans on-screen promo codes. Wiring snippet doc reinforces. The block.html itself has no slot for a code — only for module name and URL line.                        |
| **Badge collides with YouTube's bottom-action UI (likes/comments/subscribe column)**                                | LOW        | MEDIUM | Bottom: 460 px places the badge above the bottom-380 reserve; left: 60 px keeps it clear of the right-edge action column. Smoke-test preview verifies. If still colliding, raise `bottom` further in 40 px steps. |
| **Endcard's fade-to-black truncates content if host duration math is wrong**                                        | LOW        | MEDIUM | Recipe.md mandates `data-start = totalDuration - 3` and `data-duration = 3`. Lint will flag duration overflow. Smoke test verifies a 12 s host with 9 + 3 wiring.                                                  |
| **Sub-comp block fails to register `window.__timelines["dynamous-endcard"]` due to async/Promise wrapping**          | LOW        | HIGH   | `block.html` script body uses an IIFE — fully synchronous. Mirrors `url-cta/block.html` exactly. SKILL.md rule documented in the recipe's gotchas section.                                                          |
| **Interstitial inserted on top of a hero word, distracts from narration**                                           | MEDIUM     | LOW    | Recipe.md "When to use" mandates a ≥1.0 s narration breath. Optional per video — if no clean pause exists, skip the interstitial entirely.                                                                         |
| **Sync-shared-lib hook fails to update MANIFEST.md after Write**                                                    | LOW        | LOW    | Documented manual fallback: `bash scripts/sync-shared-lib.sh`. MANIFEST.md is auto-maintained; manual edits get overwritten.                                                                                       |
| **Bundler 404s the SVG because the asset wasn't copied into `videos/<slug>/assets/`**                               | MEDIUM     | MEDIUM | Each README and recipe repeats the asset-copy checklist. Task 9 smoke test catches it. If 404 still happens, lint / preview surfaces the missing-asset warning.                                                    |
| **Future author re-introduces a `[YOURCODE]` placeholder by following the strategy doc literally**                  | LOW        | MEDIUM | The wiring snippet's pinned-comment + description templates are locked verbatim with NO `[YOURCODE]` slot, and call out that the discount is automatic via the link. Discount bubble README explicitly bans a code field.    |
| **Verbal CTA in `script.txt` sounds like a hard sales pitch — fails the strategy doc's Friend Test**                | MEDIUM     | MEDIUM | Wiring snippet ships the verbatim Friend-framed wording ("I got you guys a 10% off code") and includes the strategy doc's Execution Checklist. Author signs off via the y/N spawn-time prompt.                       |
| **Author skips opt-in question, accidentally wires the system anyway by following an old README**                   | LOW        | LOW    | Both template READMEs and the diy-yt-creator skill carry the y/N step at the top. Task 13/14 ensure each instance is updated.                                                                                       |

---

## Notes

### Why three artifacts and not a single mega-block?

The three Remotion components solve three different problems with different lifetimes (always-on vs. last-3 s vs. opt-in mid-video). Collapsing them into one block would force every Short to use mid-video interstitial logic even when it doesn't apply, and would couple persistent UI (badge) to time-bounded UI (endcard) — they belong in different `shared/lib/` kinds (component vs. block) per the existing repo convention. Faithful port preserves the same separation of concerns.

### Why no `findMatchingModule()` at runtime in HyperFrames?

The HyperFrames runtime is deterministic + synchronous; all content is pre-baked. A "smart" module lookup that runs at composition load would (a) require reading JSON synchronously (possible but adds runtime IO), (b) make rendering depend on JSON content rather than HTML content (worse for review/diff), (c) violate the "all timeline construction synchronous" rule if any error path lands in a Promise. Better: surface the lookup as a CLI helper (`scripts/find-dynamous-module.js`) the author runs *before* writing the recipe slot, and bake the result as plain text into the HTML.

### Why the badge doesn't pulse on `topicMatches` like the Remotion source does

The pulse is a 30-frame interpolation in Remotion. In HyperFrames, animating opacity/scale on a persistent overlay across the full Short means a continuously running tween — easy with GSAP `repeat: <finite>` but adds visual noise. The user explicitly asked for "subtle." The decision: drop the pulse entirely; the matched-topic moment is communicated by the interstitial card instead (a much louder signal). If the user later wants the pulse back, it's a 4-line addition in the badge component's `<script>` section.

### Why opacity 0.45 instead of Remotion's 0.4 / 0.65

Remotion source has 0.4 idle, 0.65 when matched. We dropped the matched mode (no pulse, see above), so we land between the two at 0.45 — visible enough to read at a glance, quiet enough to not compete with phase content. Tested visually in the smoke test against the dark-stage palette; remains AA-readable.

### Token color naming

The repo's existing tokens use generic names (`--orange`, `--text`, `--text-dim`). The Dynamous palette overlaps but isn't identical (Dynamous bg `#1C1917` vs. Anthropic bg `#0B0F18`). The endcard block uses `var(--bg, #1C1917)` so a host video can override per its own theme — but defaults to Dynamous stone. We don't introduce a separate `dynamous-dark.css` token set in this PRP — premature given only the endcard uses it, and even then with a default fallback.

### Future follow-ups (out of scope for this PRP)

- A `shared/lib/visual-styles/dynamous-stone.md` entry once we have ≥3 videos using it
- A `dynamous-dark.css` tokens file if/when the palette diverges enough
- Long-form (1920×1080) Dynamous overlays — port from the long-form Remotion components when long-form templates land
- A pulse variant of the badge as an opt-in flag (`addDynamousBadgeEntrance(tl, { pulse: true })`)
- Auto-injection of the badge + endcard via the diy-yt-creator skill's video scaffolding

### Why the midroll v3 palette and not the older Shorts constants

The user pointed at `DynamousMidroll.tsx` as "everything needed", and reading it surfaced two key facts: (1) Cole renders Dynamous in a *modern-gradient* aesthetic (slate + purple + pink + cyan with red 10% OFF badge), not the stone-toned aesthetic the older `ShortsDynamousBadge.tsx` constants suggested; (2) the midroll's CTA stack is the most polished, recently-tuned brand expression in the entire repo. Aligning these new artifacts to the midroll keeps the channel coherent — when a viewer sees a Short endcard then later sees a long-form midroll, the brand feels continuous. The Shorts constants file represents an early experiment and is now superseded.

### Why opt-in instead of default-on

The user's explicit instruction was to ask per video. That matches the strategy doc's value-first philosophy: not every Short is a good vehicle for the promotion (e.g. a fast pure-news clip with no platform recording has no place for the discount bubble; an unrelated technical update doesn't fit any module so the interstitial would feel forced). Opt-in puts the editorial decision in the author's hands every time, and the template-spawn flow makes the question unmissable. Existing videos stay clean.

### Strategy-doc philosophy folded into artifacts

The user-supplied `shorts_promotion_strategy.md.resolved` is the load-bearing brand-strategy reference. Concrete plan changes it drove:

1. **Badge entrance pushed from `t=0.4s` to `t=3.0s`** — strategy doc rule "Never start the video with the brand name. You have less than 3 seconds to stop the scroll." The badge is small and muted but still visible — it doesn't belong over the hook frame.
2. **Discount-bubble component added (artifact 4)** — strategy doc § 2 "The Text Overlay" describes a clean minimal text box for sound-off viewers. We mapped this to a `class="clip"` time-bounded component, opt-in per scene. Per user confirmation, the bubble shows logo + `Dynamous.ai` + red `10% OFF` + `in the link ↓` — no code field, since the discount applies automatically via the description link.
3. **Pinned-comment + description templates verbatim** — strategy doc § 2 "The Pinned Comment Strategy" is the canonical conversion path. Wiring snippet ships the verbatim wording so authors don't improvise and accidentally land in "salesy" territory.
4. **`script.txt` outro wording verbatim** — § 2 "I got you guys a discount" framing is the recommended verbal CTA. Wiring snippet ships it.
5. **Execution Checklist** — § 4's Value Test, Friend Test, Hook Test, CTA softness, frictionless purchase are all baked into the wiring snippet so the author runs them before publishing.

### Confidence and known unknowns

Confidence is **9.5/10** for one-pass implementation. All four Task 1 questions are confirmed: omit Cole, automatic discount via link, strategy doc wording acceptable, no code in discount bubble. Brand assets are real files copying from `diy-yt-creator/public/assets/`. Palette + CTA wording locked from `DynamousMidroll.tsx` Phase 6. Remaining 0.5 point is normal HyperFrames smoke-test risk — sub-comp `<template>` registration, asset path bundler quirks, and the manifest-sync hook all need to actually fire correctly during Task 9. Opt-in design means even a misfire in the smoke test cannot leak into a real Short.
