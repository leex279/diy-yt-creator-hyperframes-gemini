# Feature: YouTube Shorts 2026 Best Practices — Pipeline Integration

## Summary

Bake the 2026 YouTube Shorts platform spec (safe zones, typography physics, kinetic word-by-word captions, APCA contrast, pacing caps) into the existing `diy-yt-creator` HyperFrames pipeline. The pipeline already covers the structural fundamentals (1080×1920 canvas, `transcript.json` word timing, Phase 2.5 quality gates, 9-cue SFX library). The work is targeted: tighten the template's safe zone to the spec's 900×1160 inner box (with asymmetric 60/120 left/right padding to clear YouTube's right-rail UI), implement the named-but-missing `caption-karaoke` component as a reusable shared-lib block, raise Phase 2.5's WPM ceiling to 200 and add hard caption-length gates, document APCA targets alongside the existing WCAG ratios, and add a single `scripts/validate-shorts-spec.cjs` script that turns the four hard rules (safe zone, char cap, dwell window, WPM) into machine-checkable errors. No framework changes — all work fits inside existing CLAUDE.md key rules.

## User Story

As a YouTube Shorts producer using this pipeline
I want every output composition to mathematically comply with the 2026 platform spec — safe zones, kinetic captions, APCA contrast, dwell windows
So that produced shorts maximise retention and replay-loop monetisation, survive H.264 compression cleanly, and pass international accessibility frameworks (WCAG 2.1 AA, APCA, EAA) without per-video remediation.

## Problem Statement

The existing pipeline produces visually polished 1080×1920 shorts but does not enforce five mechanically-verifiable retention/accessibility rules that the 2026 algorithm rewards:

1. **Safe zone**: template inner box is 960×1440 (`--pad-top: 240px`, `--pad-x: 60px`, `--pad-bottom: 240px`); spec target is 900×1160 with asymmetric 120px right margin to clear the Like/Comment/Share/Remix rail. Captions and CTAs placed in the bottom 240px collide with the channel description + subscribe prompt overlay on real devices.
2. **Typography below the legibility floor**: spec mandates 40–60px body, 60–90px hook/headline. The template's actual values from `index.html` violate the 40px body floor in 8 places: `.overline` 36px (line 163), `#p1-caption` 32px (202), `.stat-label` 30px (271), `.tl-date` 38px (327), `.tl-sub` 28px (346), `.tl-index` 34px (361), `#p4-overline` 38px (404), `#p4-pill` 48px (412 — borderline). Body sub-30px text degrades under H.264 chroma subsampling and disappears on small mobile screens. Hero slam (`#p1-hero` 200px line 190, `.stat-num` 180px line 260) sits *above* the 60–90 hook range — this is an intentional artistic choice for slam moments and is preserved, but must be documented as a deliberate exception.
3. **Kinetic karaoke captions**: `caption-word-pop` is named in `.claude/references/retention-components-hyperframes.md:§2` but has zero implementation in `shared/lib/`, the template, or any existing video. The current template renders only static pill captions with placeholder copy.
4. **APCA contrast**: `DESIGN.md:33-38` documents WCAG ratios only. APCA scores (the modern non-linear-luminance algorithm the spec mandates ≥75) are absent from tokens, design docs, and the `validate` step.
5. **Hard pacing caps**: Phase 2.5 enforces 150–165 WPM but rejects 166–200 WPM scripts that the spec explicitly allows. The ≤42 chars × 2 lines × 1.0–6.0s dwell rules exist only as prose advice in `phase1-plan.md`, not as gates.

Each gap is measurable and currently silent — captions overflow into UI, sub-floor text degrades under compression, contrast fails on bright b-roll, scripts get rejected for being algorithmically optimal, and per-word karaoke (the highest-retention mechanism per the spec) cannot be produced at all.

## Solution Statement

Six-track enhancement, executed in dependency order:

1. **Tokens + template safe zone**: update `shared/lib/tokens/anthropic-dark.css` and `templates/shorts/anthropic/index.html` with new safe-zone CSS variables (`--safe-top: 380px`, `--safe-bottom: 380px`, `--safe-left: 60px`, `--safe-right: 120px`), then re-anchor `.phase-content` and every `max-width` constraint to the new 900×1160 inner box.
2. **Typography floor**: lift every body/label/caption/overline/sub element in `templates/shorts/anthropic/index.html` to ≥40px (8 elements affected — see Task 2b). Preserve hero slam (200px) and stat numerals (180px) as documented intentional artistic exceptions above the 60–90 hook range. Mid-tier headlines (`#p1-pre` 72px, `#p2-headline` 64px, `#p4-url` 64px) already sit inside the spec's 60–90 range and stay as-is.
3. **Shared-lib component (OPT-IN)**: build `shared/lib/components/caption-karaoke/component.html` + `recipe.md` — generates per-word `<span class="clip">` elements with `data-start`/`data-duration`/`data-track-index`, applies the karaoke highlight via GSAP timeline, anchored at `bottom: 600px`. **Captions are not produced by default** — they only appear when the user explicitly requests them via the brief flag `captions: true` (or equivalent natural-language signal in the `/diy-yt-creator full-auto` invocation, e.g. "with karaoke captions"). Default behaviour for every new short remains caption-free.
4. **Pipeline phases**: bump Phase 2.5 WPM bounds to 150–200 (raise ceiling); add a new BLOCKING gate for `chars_per_caption_line ≤ 42 && lines ≤ 2 && dwell_s ∈ [1.0, 6.0]` that runs *only when captions are requested*; Phase 3.5 emits a `caption_strategy` block *only when* `PARAMS.captions === true` is set in the orchestrator state. No density-based auto-emission.
5. **APCA documentation**: extend `DESIGN.md` and `shared/lib/visual-styles/anthropic-dark.md` with APCA scores for every token pairing; document the ≥75 / ≥60 / ≥45 thresholds as design targets.
6. **Validation script**: `scripts/validate-shorts-spec.cjs` — a Node CLI that parses a video's `index.html`, walks every element with timing attributes, and flags safe-zone violations, font-size sub-40px violations, dwell out-of-range, char-cap violations, and (best-effort) APCA mismatches. The caption-specific checks (char cap, dwell window, line count) only fire when a `<div id="captions">` element exists; absence of the captions container is a valid PASS state. Wire the script into the `new-anthropic-short` skill as Step 11.

No new framework primitives. No conflicts with CLAUDE.md key rules — every per-word `<span>` carries `class="clip"` + `data-track-index` per Rule 1/2; karaoke fades use opacity tweens per Rule 6; build-time DOM generation uses `Edit` tool calls (deterministic) per Rule 6.

## Metadata

| Field            | Value                                                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Type             | ENHANCEMENT                                                                                                                            |
| Complexity       | MEDIUM-HIGH                                                                                                                            |
| Systems Affected | `templates/shorts/anthropic/`, `shared/lib/{tokens,components,visual-styles}/`, `.claude/commands/diy-yt-creator/`, `.claude/skills/diy-yt-creator/`, `scripts/`, `CLAUDE.md`, `DESIGN.md` (template + per-video) |
| Dependencies     | hyperframes CLI (existing), GSAP (existing, already in template), Node 18+ for validate script (already used by repo), zero new npm packages |
| Estimated Tasks  | 16                                                                                                                                     |
| Captions Default | **OFF** — captions are opt-in via brief flag or natural-language request only                                                          |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                              BEFORE STATE                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Canvas 1080×1920                  Inner Content Box: 960×1440                ║
║   ┌──────────────────────┐         ┌──────────────────────┐                   ║
║   │  TopBanner (60px)    │         │ pad-top: 240px       │                   ║
║   │  ─────────────────── │         │ pad-x:    60px       │                   ║
║   │                      │   →     │ pad-bot: 240px       │                   ║
║   │  Phase content       │         │                      │                   ║
║   │  Static pill captions│         │ Hero: 200–240px      │                   ║
║   │  Hero slam 200px     │         │ Body:  30–44px       │                   ║
║   │                      │         │ Captions: NONE       │                   ║
║   │  Progress bar (60px) │         │ APCA score: unknown  │                   ║
║   └──────────────────────┘         └──────────────────────┘                   ║
║                                                                               ║
║   PIPELINE_FLOW:                                                              ║
║     phase0-research → phase1-plan → phase2-script → phase2-5-critique         ║
║       (WPM gate 150–165, rejects 166–200)                                     ║
║       → phase2a-tts → phase2b-factcheck → [PAUSE 1: tts/transcribe]           ║
║       → phase3-5-retention (anchors SFX to words, NO captions)                ║
║       → [PAUSE 2: composition build via new-anthropic-short skill]            ║
║       → npx hyperframes lint (validates audio src, track overlap only)        ║
║                                                                               ║
║   PAIN_POINTS:                                                                ║
║     - Captions in bottom 240px collide with YT subscribe-prompt overlay       ║
║     - Right edge (60px margin) collides with Like/Comment/Share/Remix         ║
║     - 30–44px body text fails compression on small mobile screens             ║
║     - Phase 2.5 rejects scripts at 170 WPM (algorithm-optimal range)          ║
║     - No karaoke retention mechanism — caption-word-pop is vapourware         ║
║     - APCA score unknown for any token; only WCAG documented                  ║
║     - No machine-enforceable safe zone — slips through lint silently          ║
║                                                                               ║
║   DATA_FLOW: transcript.json → SFX `data-start` only                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                               AFTER STATE                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Canvas 1080×1920                  Inner Content Box: 900×1160                ║
║   ┌──────────────────────┐         ┌──────────────────────┐                   ║
║   │ ◌ YT system-UI zone  │  60L    │ safe-top:    380px   │  120R            ║
║   │ ━━━━━ pad 380 ━━━━━━ │  ←──    │ safe-left:    60px   │  ←──              ║
║   │ ┌──────────────────┐ │         │ safe-right:  120px   │ (clears Like/    ║
║   │ │ 900×1160         │ │         │ safe-bottom: 380px   │  Cmnt/Shr/Rmx)    ║
║   │ │ Hero  60–90px    │ │   →     │                      │                   ║
║   │ │ Body  40–60px    │ │         │ APCA target: ≥75     │                   ║
║   │ │ Captions:        │ │         │ Dwell:   1.0–6.0s    │                   ║
║   │ │  ★ KARAOKE ★     │ │         │ Chars/line:    ≤42   │                   ║
║   │ │  word-by-word    │ │         │ Lines:           ≤2  │                   ║
║   │ │  bottom: 600px   │ │         │ WPM gate: 150–200    │                   ║
║   │ └──────────────────┘ │         │ Karaoke: GSAP-driven │                   ║
║   │ ━━━━━ pad 380 ━━━━━━ │         │   per-word fade-pop  │                   ║
║   │ ◌ YT channel/sub-UI  │         │                      │                   ║
║   └──────────────────────┘         └──────────────────────┘                   ║
║                                                                               ║
║   PIPELINE_FLOW (added gates marked +; caption path marked ⊕ — OPT-IN):       ║
║     phase0 → phase1-plan (uses new safe-zone tokens)                          ║
║       ⊕ if PARAMS.captions=true: plan reserves caption track-index 2          ║
║     → phase2-script → phase2-5-critique                                       ║
║       (+ WPM gate 150–200)                                                    ║
║       ⊕ if PARAMS.captions=true: NEW chars/dwell/lines gate fires             ║
║     → phase2a-tts → phase2b-factcheck → [PAUSE 1]                             ║
║     → phase3-5-retention                                                      ║
║       ⊕ if PARAMS.captions=true: emit caption_strategy block                  ║
║       ⊖ default (no flag): NO caption_strategy emitted                        ║
║     → [PAUSE 2: new-anthropic-short]                                          ║
║       ⊕ Step 8.5 only runs if retention-strategy.md has caption_strategy      ║
║       (+ Step 11: scripts/validate-shorts-spec.cjs — fails on violations)     ║
║     → npx hyperframes lint + validate-shorts-spec                             ║
║                                                                               ║
║   VALUE_ADD:                                                                  ║
║     - All elements stay inside YT-UI-clear 900×1160 (machine-enforced)        ║
║     - Body/label text raised to ≥40px → survives H.264 compression            ║
║     - Word-by-word karaoke OPT-IN per video (not auto-applied)                ║
║     - APCA-aware token system → legible on bright b-roll                      ║
║     - Hard char/dwell/WPM caps → no per-video remediation                     ║
║     - One validate script catches all five gaps before render                 ║
║                                                                               ║
║   DATA_FLOW: transcript.json → SFX `data-start` + per-word caption spans      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                                                            | Before                                  | After                                                                    | User Impact                                              |
| ------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------- |
| `templates/shorts/anthropic/index.html:41-43` (`#root` CSS vars)    | `--pad-top: 240; --pad-x: 60; --pad-bot: 240` (symmetric) | `--safe-top: 380; --safe-left: 60; --safe-right: 120; --safe-bottom: 380` (asymmetric) | New shorts auto-respect YT UI overlays; no manual nudging  |
| `templates/shorts/anthropic/index.html` (8 sub-40px font sizes)     | `.overline 36, #p1-caption 32, .stat-label 30, .tl-date 38, .tl-sub 28, .tl-index 34, #p4-overline 38, #p4-pill 48` | All ≥40px (see Task 2b for exact mapping) | Body/label text legible after H.264 compression on small screens |
| `shared/lib/tokens/anthropic-dark.css`                              | Same symmetric padding tokens           | Replaced with safe-zone tokens; old tokens kept as deprecated comments    | Existing videos can opt-in via re-copy; backward-tolerant |
| `.claude/commands/diy-yt-creator/brief-template.md` + `full-auto.md` | No `captions` flag in PARAMS            | New `PARAMS.captions: bool` (default `false`); orchestrator parses NL signals like "with captions" / "with karaoke" | User explicitly turns captions on per video |
| `shared/lib/components/caption-karaoke/`                            | Does not exist                          | New component.html + recipe.md — **only consumed when `PARAMS.captions=true`** | Skill can wire word-level captions when requested only   |
| `.claude/commands/diy-yt-creator/phase2-5-critique.md:440`          | WPM gate `150 ≤ wpm ≤ 165` (BLOCKING)   | WPM gate `150 ≤ wpm ≤ 200` (BLOCKING) + char/dwell gate **conditional on captions flag** | Algorithm-optimal scripts (170-200 WPM) no longer rejected; caption gate fires only when captions opted in |
| `.claude/commands/diy-yt-creator/phase3-5-retention.md`             | No caption emission                     | Emits `caption_strategy` block **only when `PARAMS.captions=true`**       | Default = no captions; flag-gated emission; no density auto-detect |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md` Step 11      | Step 10 ends with `npx hyperframes inspect` | New Step 8.5 (conditional on `caption_strategy` presence) + Step 11: `node scripts/validate-shorts-spec.cjs videos/<slug>` (BLOCKING) | Build fails fast on safe-zone, font-size, dwell, char, APCA gaps |
| `templates/shorts/anthropic/DESIGN.md:33-38`                        | WCAG ratios only (5 token pairings)     | WCAG + APCA scores side-by-side; ≥75 / ≥60 / ≥45 targets stated; type-scale section listing all elements with px values | Designers choose tokens with both AA and APCA in mind; type scale audit-able |
| `CLAUDE.md` Key Rules                                               | 6 rules                                 | 7 rules (add: "Captions are OPT-IN — only render `<span class='clip'>` per-word elements when `PARAMS.captions=true`; default = no captions") | Future-Claude knows captions are not a default              |

---

## Mandatory Reading

**CRITICAL: Implementation agent MUST read these files before starting any task:**

| Priority | File                                                              | Lines    | Why Read This                                                                                |
| -------- | ----------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------- |
| P0       | `templates/shorts/anthropic/index.html`                           | 13–46, 95–125, 137–157, 663–755 | Canvas + safe-zone vars + GSAP timeline pattern to mirror |
| P0       | `shared/lib/README.md`                                            | 1–60     | Bundler copy-from contract; how to add a new component without breaking preview/render       |
| P0       | `.claude/commands/diy-yt-creator/phase3-5-retention.md`           | 33–199   | Sub-agent pattern for emitting timing blocks; word-anchor computation rule (`+ offset`)      |
| P0       | `.claude/skills/diy-yt-creator/new-anthropic-short.md`            | 138–296  | Composition build steps 5–10 — where step 11 plugs in                                        |
| P1       | `videos/anthropic-amazon-compute/index.html`                      | 906–973, 1074–1180 | Real-world SFX wiring + counter-tween + transcript-anchored shake patterns to mirror |
| P1       | `templates/shorts/anthropic/DESIGN.md`                            | 33–99    | Existing WCAG documentation pattern to extend with APCA                                      |
| P1       | `.claude/commands/diy-yt-creator/phase2-5-critique.md`            | 286–441  | Existing quality-gate format to extend with char/dwell/WPM gates                             |
| P1       | `.claude/references/retention-components-hyperframes.md`          | §2 (lines 29–46) | Naming vocabulary for `caption-word-pop` and friends — match these names                |
| P1       | `.claude/rules/audio-design.md`                                   | All      | Track-index assignment rules + 0.25 SFX volume cap (caption tracks must not collide)         |
| P2       | `shared/lib/components/top-banner-wordmark/component.html`        | All      | Paste-in component pattern to mirror for `caption-karaoke`                                   |
| P2       | `shared/lib/effects/hero-slam-shake.js`                           | All      | GSAP recipe-style file pattern to mirror for any caption helper effects                      |
| P2       | `shared/audio/MANIFEST.md`                                        | Sentinel block | How `sync-shared-lib.sh` PostToolUse hook auto-maintains the manifest                  |
| P2       | `scripts/sync-shared-lib.sh`                                      | All      | Pattern for the new `scripts/validate-shorts-spec.cjs` — single-file Node CLI                |

**External Documentation:**

| Source                                                                         | Section                                            | Why Needed                                                              |
| ------------------------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------------------- |
| User-provided 2026 article (this issue)                                        | "Mathematics of Spatial Geometry"                  | Canonical 380/60/120/380 → 900×1160 numbers — no other source needed    |
| User-provided 2026 article                                                     | "Implementing the Advanced Perceptual Contrast Algorithm" | APCA thresholds (75 / 60 / 45)                                |
| User-provided 2026 article                                                     | "The Dominance of Word-by-Word Subtitling"         | Karaoke contract — inactive white + drop shadow, active accent          |
| `https://hyperframes.heygen.com/llms.txt`                                      | data-attributes, compositions                      | Confirms `data-start`/`data-duration`/`data-track-index` is exhaustive  |
| `https://github.com/Myndex/apca-w3` (reference)                                | README                                             | APCA-W3 algorithm — implementation reference if we choose to compute scores; v0.1.x |

> APCA is documented as a *target* in this plan; computation is best-effort in `validate-shorts-spec.cjs` (parses CSS color tokens against canvas/card backgrounds). Full per-frame APCA against rendered video pixels is out of scope (see "NOT Building").

---

## Patterns to Mirror

**SAFE_ZONE_CSS_VARS (extending existing CSS-var pattern):**

```css
/* SOURCE: templates/shorts/anthropic/index.html:41-46 */
/* COPY THIS PATTERN — replace pad-* with safe-* names */
#root {
  --pad-top: 240px;
  --pad-x: 60px;
  --pad-bottom: 240px;
  --mono: 'JetBrains Mono', ui-monospace, monospace;
  --sans: 'Inter', system-ui, sans-serif;
}
```

**TIMED_AUDIO_ELEMENT (mirror for per-word caption spans):**

```html
<!-- SOURCE: videos/anthropic-amazon-compute/index.html:906-913 -->
<!-- MIRROR THIS for <span class="clip"> per-word caption elements -->
<audio id="sfx-impact-slam-p0" class="clip"
       src="assets/sfx/impact-slam.mp3"
       data-start="0.61" data-duration="0.63"
       data-track-index="3" data-volume="0.14"></audio>
```

**GSAP_TIMELINE_REGISTRATION (must be preserved as-is):**

```js
// SOURCE: templates/shorts/anthropic/index.html:663-664, 755
// COPY THIS PATTERN — caption animations join the SAME tl, no new timeline
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
// ... all tweens added to tl ...
window.__timelines["main"] = tl;
```

**SHARED_LIB_COMPONENT_FILE (mirror for caption-karaoke):**

```html
<!-- SOURCE: shared/lib/components/top-banner-wordmark/component.html -->
<!-- COPY THIS STRUCTURE: <!-- SOURCE comment --> + <style> + <div> + <script> -->
<!-- SOURCE: templates/shorts/anthropic/index.html:95-125 -->
<style>
  #top-banner { position: absolute; top: 60px; left: 0; ... }
</style>
<div id="top-banner" class="clip" data-start="0" data-duration="..." data-track-index="...">
  <img id="top-banner-logo" src="assets/anthropic-logo-light.svg" alt="" />
</div>
```

**TRANSCRIPT_ANCHORED_TIMING (mirror for caption-strategy emission):**

```yaml
# SOURCE: .claude/commands/diy-yt-creator/phase3-5-retention.md:142
# COPY THIS COMPUTATION RULE for caption_strategy blocks
# data-start = transcript.json[anchor_word_index].start + offset_seconds
sfx_cues:
  - cue: impact-slam
    track_index: 3
    anchor_word_index: 4
    offset_seconds: 0.0
    data_start: 0.610   # = transcript.json[4].start + 0.0
    duration_seconds: 0.63
    volume: 0.14
```

**QUALITY_GATE_BLOCK (mirror for new char/dwell/WPM gate):**

```markdown
<!-- SOURCE: .claude/commands/diy-yt-creator/phase2-5-critique.md:286-355 -->
<!-- COPY THIS PATTERN for new "Spec Compliance Gate" -->

## Quality Gate N — <Name>

**BLOCKING**: <description>

**Computation**:
1. <step>
2. <step>

**Threshold**: <pass condition>

**On fail**: report row in `phase-status.md` set to `blocked`, return rationale.
```

**NODE_CLI_VALIDATOR (mirror for validate-shorts-spec.cjs):**

```bash
# SOURCE: scripts/sync-shared-lib.sh (single-file CLI pattern)
# COPY THIS PATTERN for validate-shorts-spec.cjs
# - shebang
# - usage block
# - argv parsing (project dir is positional arg)
# - exit 0 on pass / exit 1 on fail with structured error list
# - no external deps (use Node's built-in fs/path/url)
```

---

## Files to Change

| File                                                                         | Action  | Justification                                                                                              |
| ---------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| `shared/lib/tokens/anthropic-dark.css`                                       | UPDATE  | Add `--safe-top/left/right/bottom` tokens; keep deprecated `--pad-*` aliases for one cycle                 |
| `templates/shorts/anthropic/index.html`                                      | UPDATE  | Re-anchor `.phase-content` padding to safe-zone vars; reduce `max-width: 920` constraints to 900; raise 8 sub-40px font sizes (see Task 2b) |
| `templates/shorts/anthropic/DESIGN.md`                                       | UPDATE  | Add APCA score column; document 900×1160 inner box + asymmetric R-margin rationale; new "Type Scale" section listing every element + size + tier (body / headline / hero) |
| `shared/lib/visual-styles/anthropic-dark.md`                                 | UPDATE  | Mirror DESIGN.md APCA + Type Scale additions for the shared visual-styles surface                          |
| `shared/lib/components/caption-karaoke/component.html`                       | CREATE  | Paste-in caption layer with per-word `<span class="clip">` template + GSAP highlight recipe — **only used when user opts in** |
| `shared/lib/components/caption-karaoke/recipe.md`                            | CREATE  | Wiring instructions: how to ingest `transcript.json`, generate spans, position at `bottom: 600px`; opens with bold "OPT-IN ONLY" header |
| `shared/lib/components/safe-zone-overlay/component.html`                     | CREATE  | Debug overlay (dashed rectangles for top/bottom/L/R safe margins); only mounted with `?debug=1` query      |
| `shared/lib/components/safe-zone-overlay/recipe.md`                          | CREATE  | Sister recipe for the debug overlay                                                                        |
| `.claude/commands/diy-yt-creator/brief-template.md`                          | UPDATE  | Add `captions: bool` field to the brief schema (default `false`); document the natural-language phrases ("with captions", "karaoke", "subtitles on") that trigger opt-in |
| `.claude/commands/diy-yt-creator/full-auto.md`                               | UPDATE  | Parse `PARAMS.captions` from arguments at the existing PARAMS-detection block (lines 28-36); persist into `videos/<slug>/phase-status.md` so Phase 3.5 + the skill see the flag |
| `.claude/commands/diy-yt-creator/phase2-5-critique.md`                       | UPDATE  | Bump WPM ceiling 165→200; add new BLOCKING gate "Spec Compliance" for chars/dwell/lines, **conditional on PARAMS.captions=true** |
| `.claude/commands/diy-yt-creator/phase3-5-retention.md`                      | UPDATE  | Emit `caption_strategy` block **only when `PARAMS.captions=true`**; default behaviour is no caption emission regardless of narration density |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                       | UPDATE  | Insert conditional Step 8.5 (caption-karaoke wiring — only runs if `retention-strategy.md` has `caption_strategy`) and Step 11 (validate-shorts-spec.cjs) |
| `scripts/validate-shorts-spec.cjs`                                           | CREATE  | Node CLI: parses `videos/<slug>/index.html`, returns exit 1 with structured errors on spec violations; caption checks are absence-tolerant (no `<div id="captions">` is a valid PASS) |
| `CLAUDE.md`                                                                  | UPDATE  | Add Key Rule 7 (captions are OPT-IN; safe-zone reminder); reinforce default = no captions                  |
| `templates/shorts/anthropic/README.md`                                       | UPDATE  | Document new safe-zone tokens, type scale, and how to opt into captions ("pass `captions: true` in your brief or say 'with karaoke'") |

**Note on existing video** (`videos/anthropic-amazon-compute/`): not migrated automatically. Document in `notes` that it ships with the legacy 240/60 padding; future re-renders can opt in by re-copying tokens. Avoids retroactive layout drift on a working asset.

---

## NOT Building (Scope Limits)

Explicit exclusions to prevent scope creep:

- **Per-frame APCA against rendered video pixels** — would require headless rendering + pixel sampling per second; the validate script computes APCA only against CSS token pairings. Out of scope; revisit if `npx hyperframes validate` ever exposes a frame-sampler hook.
- **Auto-migration of `videos/anthropic-amazon-compute/`** — the existing video is a working production asset; touching its layout risks regression. Migration is opt-in (re-copy tokens manually).
- **A new HyperFrames CLI lint rule** — we are not patching `@hyperframes/core`. The validate script is repo-local in `scripts/`. If platform-native, it would require an upstream PR — separate workstream.
- **TikTok / Instagram Reels parity** — the spec is YouTube-Shorts-specific. Cross-platform safe zones differ (TikTok has no top-rail, Reels has different bottom rail). Not addressed.
- **Long-form (16:9) safe-zone changes** — `templates/long-form/` is TBD per `CLAUDE.md`. The 2026 spec is 9:16 only. Long-form is unaffected.
- **Non-Anthropic templates** — only `templates/shorts/anthropic/` is modified. Future shorts templates will re-use `shared/lib/tokens/` so they inherit the safe zone for free.
- **Beat-grid pattern interrupts** — `.claude/rules/audio-design.md` parks beat alignment as TBD long-form-only. We honour that boundary; the existing transcript-anchored SFX cadence (avg ~6.6s per phase) is sufficient pattern-interrupt for shorts.
- **Decoder-fade / 3D-rotate-Y caption animations** — the article lists these as alternatives. We ship `caption-word-pop` only. The other two can be added later as separate `shared/lib/components/caption-*` entries.
- **APCA library install** — we encode the formula inline in the validate script (Myndex's published JS is ~80 lines, MIT). Avoids a new package dependency for a ~one-shot calculation.

---

## Step-by-Step Tasks

Execute in order. Each task is atomic and independently verifiable.

### Task 1: UPDATE `shared/lib/tokens/anthropic-dark.css` (add safe-zone tokens)

- **ACTION**: Add new safe-zone CSS custom properties; keep legacy `--pad-*` as deprecated aliases pointing to the safe-* values.
- **IMPLEMENT**: New tokens `--safe-top: 380px`, `--safe-left: 60px`, `--safe-right: 120px`, `--safe-bottom: 380px`. Update `--pad-top: var(--safe-top)`, `--pad-x: var(--safe-left)` (note: asymmetric — `--pad-x` deprecated; use `--safe-left`/`--safe-right` directly), `--pad-bottom: var(--safe-bottom)`.
- **MIRROR**: Existing token block in `shared/lib/tokens/anthropic-dark.css` (whatever line range holds the `--pad-*` declarations).
- **GOTCHA**: `--pad-x` is symmetric and cannot map to asymmetric safe-zone. Mark it `/* DEPRECATED — use --safe-left / --safe-right */` and leave its old 60px value for backward compatibility with any video that still uses it.
- **VALIDATE**: `npx hyperframes lint templates/shorts/anthropic` — must remain 0 errors / 0 warnings (token file alone has no bindings yet).

### Task 2: UPDATE `templates/shorts/anthropic/index.html` (rewire to safe-zone tokens)

- **ACTION**: Replace `--pad-top: 240px`, `--pad-x: 60px`, `--pad-bottom: 240px` on `#root` (line 41–43) with explicit `--safe-top: 380px; --safe-left: 60px; --safe-right: 120px; --safe-bottom: 380px;`.
- **IMPLEMENT**: Update `.phase-content` (line 152–157) `padding` to `var(--safe-top) var(--safe-right) var(--safe-bottom) var(--safe-left)` (4-arg form for asymmetry).
- **IMPLEMENT**: Reduce every `max-width: 920px` (lines 186, 226, 393 per analyst report) to `max-width: 900px`.
- **IMPLEMENT**: Reduce `#top-banner-logo` width from `972px` to `900px` (`index.html:107`).
- **MIRROR**: Existing `padding: var(...) ...;` shorthand pattern at line 154.
- **GOTCHA**: `.phase` divs at line 137–144 are still `width: 1080px; height: 1920px` (full canvas). The safe zone applies to `.phase-content`, not `.phase`. Do not change `.phase` dimensions — phase layers must paint full-canvas for backdrops.
- **GOTCHA**: Hero slam word at `#p1-hero` is 200px font. The safe zone reduces inner width to 900px → re-test for overflow. May require dropping hero font from 200→180px on long words.
- **VALIDATE**: `npx hyperframes lint templates/shorts/anthropic && npx hyperframes inspect templates/shorts/anthropic` — both must be 0 errors.

### Task 2b: UPDATE `templates/shorts/anthropic/index.html` (raise sub-40px text to spec floor)

- **ACTION**: Lift every font-size below 40px in the template's `<style>` block. Preserve hero slam (200px) and stat numerals (180px) — those are intentional artistic exceptions documented in DESIGN.md.
- **IMPLEMENT**: exact mappings (verified against `index.html`):
  | Selector              | Line | Before | After | Tier      | Notes                                                            |
  | --------------------- | ---- | ------ | ----- | --------- | ---------------------------------------------------------------- |
  | `.overline`           | 163  | 36px   | **42px** | label-mono | Adds 6px; letter-spacing 6px stays                            |
  | `#p1-caption`         | 202  | 32px   | **44px** | caption-mono | Mono pill; may need pill `padding` retune (16px 32px → 18px 34px) |
  | `.stat-label`         | 271  | 30px   | **42px** | label-mono | Falls under 180px stat-num; visual hierarchy preserved          |
  | `.tl-date`            | 327  | 38px   | **42px** | label-mono | Inside accent-coloured pill; recheck min-width 160→ may need 170 |
  | `.tl-title`           | 339  | 40px   | **44px** | body       | Floor; +4 for compression headroom                              |
  | `.tl-sub`             | 346  | 28px   | **40px** | body-mono  | Largest jump; recheck `gap` between `.tl-card` rows after change |
  | `.tl-index`           | 361  | 34px   | **40px** | label-mono | Inside 56×56 box → may need to grow box to 60×60 to fit          |
  | `#p4-overline`        | 404  | 38px   | **42px** | label-mono | Match other overlines for consistency                            |
  | `#p4-pill`            | 412  | 48px   | (keep)   | body+ | Already ≥40px; no change needed                                 |
- **MIRROR**: existing CSS-block format at `index.html:160-166` for `.overline`.
- **GOTCHA**: `.tl-sub` jumping from 28→40 is the largest change (+43%). The 3-card timeline layout has tight vertical room; bump `.timeline-list { gap }` from 24 to 28px and re-run `npx hyperframes inspect` to confirm no overflow.
- **GOTCHA**: `.tl-index` inside a 56×56px box at 40px font may clip ascenders. Verify in preview; bump box to 60×60px if needed.
- **GOTCHA**: `#p1-caption` is a mono pill; bumping 32→44 adds visual weight. If the pill feels too heavy, drop font-weight 600→500 (do NOT use lighter than 500 — sans-serif at low weight degrades under H.264 per the article).
- **GOTCHA**: Preserve the *intentional* hero exceptions. `#p1-hero` 200px (line 190) and `.stat-num` 180px (line 260) are NOT touched. They live above the 60–90 hook range as a deliberate design choice; document in DESIGN.md (Task 3).
- **VALIDATE**: `npx hyperframes lint templates/shorts/anthropic && npx hyperframes inspect templates/shorts/anthropic` — both must remain 0 errors. Visually preview at full 1080×1920 (`npx hyperframes preview`) and confirm no labels truncate or wrap unintentionally.

### Task 3: UPDATE `templates/shorts/anthropic/DESIGN.md` (document safe zone + APCA + type scale)

- **ACTION**: Add three new sections: (a) "Safe Zone (2026 YT Shorts)" with ASCII diagram, (b) APCA columns on the existing contrast table, (c) "Type Scale" enumerating every element + size + tier including the documented hero exceptions.
- **IMPLEMENT**:
  - Section A: ASCII diagram of 1080×1920 canvas with 380/60/120/380 margins → 900×1160 inner box. Note rationale (clears YT right-rail, channel block, system gradients).
  - Section B: extend contrast table with `| APCA Score | APCA Target |` columns. Compute APCA for `#F5F1EB` on `#0B0F18` (≈ Lc 95, target ≥75 = pass), `#9A958D` on `#0B0F18` (≈ Lc 50, target ≥60 = pass for large), `#E97458` on `#0B0F18`, `#A78BFA` on `#0B0F18`, `#D14343` on `#0B0F18`.
  - Section C "Type Scale": one row per element with selector / px / weight / tier. Tiers are: `body (40-60px)`, `headline (60-90px)`, `hero-slam (intentional exception, 180-240px)`, `caption-karaoke-active (56-90px when opted in)`. Mark `#p1-hero` and `.stat-num` with **EXCEPTION** badge and link to the article rationale (slam/poster typography is a design call above the 90px headline ceiling).
- **MIRROR**: Existing markdown table format at lines 33–38.
- **GOTCHA**: APCA score signs matter. `Lc` is signed (positive when text is lighter than bg, negative when darker). Document the absolute-value convention and link to apca-w3.
- **GOTCHA**: The Type Scale table is the single source of truth for the validate script's font-size walker. Keep selectors copy-pasteable (no smart-quotes, no markdown-table cell wrapping that hides parts of the selector).
- **VALIDATE**: Manual review — ensure markdown renders cleanly; no broken links. Cross-check Type Scale table against `index.html` line numbers post-Task 2b.

### Task 4: UPDATE `shared/lib/visual-styles/anthropic-dark.md` (mirror APCA additions)

- **ACTION**: Mirror the DESIGN.md APCA section so playbook agents reading visual-styles see the same targets.
- **IMPLEMENT**: Add the safe-zone diagram + APCA score table identical to Task 3.
- **MIRROR**: Existing structure of `shared/lib/visual-styles/anthropic-dark.md`.
- **GOTCHA**: This file is the *playbook* surface; DESIGN.md is the *template* surface. They should agree but live independently — do not symlink.
- **VALIDATE**: `diff` the APCA tables between DESIGN.md and visual-styles/anthropic-dark.md — must be identical content (formatting allowed to differ).

### Task 5: CREATE `shared/lib/components/safe-zone-overlay/component.html`

- **ACTION**: Build a debug overlay that renders dashed rectangles for top/bottom/left/right safe margins.
- **IMPLEMENT**: Single absolute-positioned `<div id="safe-zone-overlay">` at `z-index: 99` (above noise overlay). Four dashed-border child divs sized to 380×1080, 1080×380, 60×1920, 120×1920 pixels. Hidden by default; mounted only when `window.location.search.includes('debug=1')`.
- **MIRROR**: `shared/lib/components/top-banner-wordmark/component.html` structure (top-of-file `<!-- SOURCE: -->` comment, inline `<style>`, `<div>`, optional `<script>`).
- **GOTCHA**: Must NOT carry timing attributes (`data-start` etc.) — it is a debug overlay, not a clip. Therefore it must NOT have `class="clip"` (Rule 2 only applies to *timed* elements).
- **GOTCHA**: Use `pointer-events: none` so the overlay doesn't capture clicks during `npx hyperframes preview`.
- **VALIDATE**: Paste into `templates/shorts/anthropic/index.html` temporarily, run `npx hyperframes preview templates/shorts/anthropic?debug=1`, eyeball that the dashes outline the 900×1160 inner box correctly. Remove paste before commit.

### Task 6: CREATE `shared/lib/components/safe-zone-overlay/recipe.md`

- **ACTION**: Write the recipe sibling — wiring instructions, slots (none), dependencies (none), gotchas.
- **MIRROR**: `shared/lib/components/top-banner-wordmark/recipe.md` (or whichever component has the most complete recipe today).
- **VALIDATE**: `bash scripts/sync-shared-lib.sh` runs cleanly and adds the new entry to `shared/lib/MANIFEST.md`.

### Task 7: CREATE `shared/lib/components/caption-karaoke/component.html`

- **ACTION**: Build the per-word kinetic caption component.
- **IMPLEMENT**:
  - Outer `<div id="captions" class="clip" data-track-index="2">` at `position: absolute; bottom: 600px; left: var(--safe-left); right: var(--safe-right); text-align: center;` — anchored well inside the new 380px safe-bottom.
  - Per-word `<span class="caption-word clip" data-start="..." data-duration="..." data-track-index="2">word </span>` template — track-index 2 (visual track shared with body text; SFX is on 3+).
  - Inactive style: `color: #F5F1EB; font: 700 56px/1.4 'Inter', system-ui, sans-serif; text-shadow: 0 4px 16px rgba(0,0,0,0.85), 0 0 2px rgba(0,0,0,1);`
  - Active style (applied via GSAP, not CSS): `gsap.to(span, { color: '#E97458', scale: 1.08, duration: 0.06 }, span.dataset.start)` per word.
- **MIRROR**: Existing `<span class="clip">` pattern in template — must carry `class="clip"` per CLAUDE.md Rule 2; must carry `data-track-index` per the linter's `missing_track_index` rule.
- **GOTCHA**: 56px puts body type firmly inside the 40–60px spec range. Hook captions can scale up to 90px via a `.hook` modifier class — document but don't hard-code.
- **GOTCHA**: Sequential words on the same `data-track-index` must NOT overlap their `[start, start+duration)` windows. The recipe's transcript ingestion logic must enforce `word[i+1].start >= word[i].start + word[i].duration` before emission.
- **GOTCHA**: Karaoke "exit" (return to inactive style after the active highlight) is a GSAP color tween back to white — NOT a `visibility` toggle (CLAUDE.md Rule 6). Never use `display: none` mid-clip.
- **GOTCHA**: 42-char-line constraint: the recipe must wrap span groups in `<div class="caption-line">` blocks of ≤42 chars each, max 2 lines visible at once. Older lines fade out via opacity tween before the third line appears.
- **VALIDATE**: Paste into `templates/shorts/anthropic/index.html` with hand-coded test data (e.g., `Hello world`), run `npx hyperframes lint templates/shorts/anthropic` — must remain 0 errors. Run `npx hyperframes preview` and visually confirm the highlight tracks the audio.

### Task 8: CREATE `shared/lib/components/caption-karaoke/recipe.md`

- **ACTION**: Write the recipe — *the* document the composition-build skill reads to know how to wire karaoke from `transcript.json`.
- **IMPLEMENT** (MUST cover):
  - **Inputs**: `videos/<slug>/transcript.json` (word-level)
  - **Slot 1 — span generation**: pseudocode for reading transcript, filtering filler tokens (`uh`, `um`, `huh` < 0.1s), grouping into ≤42-char lines, generating `<span>` elements with `data-start = transcript[i].start`, `data-duration = transcript[i].end - transcript[i].start`, all on `data-track-index="2"`.
  - **Slot 2 — GSAP wiring**: timeline tween block to add to `window.__timelines["main"]` — for each word span, `tl.to(span, { color: 'var(--orange)', scale: 1.08, duration: 0.06, ease: 'back.out(1.6)' }, span.dataset.start)` and a complementary `tl.to(span, { color: 'var(--text)', scale: 1.0, duration: 0.10 }, parseFloat(span.dataset.start) + parseFloat(span.dataset.duration))`.
  - **Positioning**: `bottom: 600px` (well inside `--safe-bottom: 380`); `left: var(--safe-left); right: var(--safe-right)` for asymmetric clearance.
  - **Dwell rules**: minimum line dwell 1.0s, maximum 6.0s (auto-split long lines via NLP chunker — point at the chunker rule in Phase 2.5).
  - **WPM safety**: if any line's `chars / dwell > 13` (the spec's char-to-time ratio), the recipe must extend dwell or split the line.
  - **Z-index**: 5 (above phases at 1–4, below banner/progress at 10).
- **MIRROR**: `shared/lib/blocks/timeline-cards/recipe.md` for recipe structure (slots, dependencies, gotchas).
- **VALIDATE**: `bash scripts/sync-shared-lib.sh` adds the entry. Manually re-read the recipe — could a fresh agent implement Step 8.5 of `new-anthropic-short.md` from this recipe alone?

### Task 8b: UPDATE `.claude/commands/diy-yt-creator/brief-template.md` + `full-auto.md` (introduce captions opt-in flag)

- **ACTION**: Add a `captions: bool` field to the brief schema, default `false`. Teach the orchestrator to detect natural-language signals and persist the flag.
- **IMPLEMENT**:
  - In `brief-template.md`: add a `captions: false  # opt-in: word-by-word karaoke captions per 2026 spec; default off` line to the YAML front-matter section. Document the flag with a one-paragraph note: "Set `true` ONLY if you want kinetic word-by-word subtitles synced to narration. Captions add ~30% visual density and are best for educational, talking-head, or non-English-audience shorts. Do not enable by default."
  - In `full-auto.md` at the existing PARAMS-detection block (lines 28-36): extend the natural-language parser. If `$ARGUMENTS` contains any of `with captions`, `with karaoke`, `with subtitles`, `subtitles on`, `karaoke on`, set `PARAMS.captions = true`. Otherwise default `false`.
  - Persist `PARAMS.captions` into `videos/<slug>/phase-status.md` as a top-of-file YAML key so downstream phases (Phase 2.5, Phase 3.5, the skill) read a single source of truth.
- **MIRROR**: existing PARAMS parsing in `full-auto.md:28-36` (mode detection — RESUME / FREE-FORM / BRIEF / URL). Use the same `$ARGUMENTS.match(/.../i)` pattern.
- **GOTCHA**: The flag must be persistent across the PAUSE 1 / PAUSE 2 boundaries. The user runs `npx hyperframes tts` and `npx hyperframes transcribe` between phases — the orchestrator state could be lost. Writing to `phase-status.md` (which exists across pauses) is the safe surface.
- **GOTCHA**: Do NOT auto-detect captions based on script density, language, or any heuristic. The user's explicit signal is the only trigger. If the user gives no signal, captions stay off — even if the topic is a fast-talking explainer.
- **GOTCHA**: When the orchestrator sees `with captions` in a RESUME flow, honour the flag for the resumed video only — do NOT propagate to other in-flight videos.
- **VALIDATE**: Smoke test the orchestrator with three sample invocations:
  - `/diy-yt-creator full-auto Topic X` → `PARAMS.captions=false` in phase-status.md
  - `/diy-yt-creator full-auto Topic X with karaoke captions` → `PARAMS.captions=true`
  - `/diy-yt-creator full-auto videos/existing-slug` (RESUME) → reads existing phase-status.md value, preserves it
  Confirm via `grep captions videos/<slug>/phase-status.md`.

### Task 9: UPDATE `.claude/commands/diy-yt-creator/phase2-5-critique.md` (raise WPM ceiling, add conditional Spec Compliance gate)

- **ACTION**: Modify line ~440 to bump WPM upper bound from 165 → 200. Add a new Quality Gate ("QG-5: Caption Spec Compliance") that **only fires when `PARAMS.captions=true`**. Otherwise QG-5 is skipped with a one-line "captions off; spec gate skipped" note in the report.
- **IMPLEMENT**:
  - WPM gate update: change `if 150 <= wpm <= 165` to `if 150 <= wpm <= 200`. Always-on. Update the rationale to cite the 2026 spec (200 WPM is the algorithm's hard ceiling). This change is unconditional — regardless of caption flag.
  - QG-5 block: BLOCKING when `PARAMS.captions=true`; SKIPPED otherwise. Read flag from `phase-status.md` top-of-file YAML. Computation = chunk script by sentence, compute chars-per-chunk, simulate per-chunk dwell at WPM rate, flag any chunk with chars > 42 OR predicted-dwell > 6.0s OR predicted-dwell < 1.0s.
- **MIRROR**: Existing Quality Gate block format (e.g., lines 286–355).
- **GOTCHA**: The script doesn't yet have caption-line breaks at this phase (Phase 2.5 is pre-TTS). Use a heuristic: split sentences on `, ` or `; ` if they exceed 42 chars; raise warning if a single un-splittable noun phrase exceeds 42.
- **GOTCHA**: 200 WPM is the *upper* algorithm-ok bound; *target* remains around 160–175 for retention. Document as range, not as new target.
- **GOTCHA**: When QG-5 is skipped, the report must say so explicitly — silent skip is misleading. Format: `QG-5: SKIPPED (captions=false; pass `with captions` to enable spec gate)`.
- **VALIDATE**: Run Phase 2.5 against an existing video's `full-script.md` (e.g., `videos/anthropic-amazon-compute/scripts/full-script.md` if present) twice:
  - With `phase-status.md captions: false` → QG-5 reports SKIPPED, other gates run normally
  - With `phase-status.md captions: true` → QG-5 runs, blocks on real chunking issues, passes on clean scripts

### Task 10: UPDATE `.claude/commands/diy-yt-creator/phase3-5-retention.md` (emit caption_strategy ONLY when opted in)

- **ACTION**: Add a new sub-section to the sub-agent prompt: "Caption Strategy Emission". The block runs **only** when `PARAMS.captions=true` (read from `phase-status.md`). When the flag is `false` (the default), the sub-agent emits NO caption strategy and writes a one-line `# captions: off — no caption_strategy emitted` comment at the top of `retention-strategy.md`.
- **IMPLEMENT**:
  - Read `PARAMS.captions` from `videos/<slug>/phase-status.md` top-of-file YAML at the start of the sub-agent run.
  - If `false`: skip caption emission entirely. Write the off-comment so downstream consumers (the skill) can verify the choice was deliberate.
  - If `true`: for every scene, emit a `caption_strategy` YAML block with `component: caption-karaoke`, `transcript_word_indices: [start_i, end_i]` (where indices map words whose `start` falls inside `[scene.data_start, scene.data_start + scene.data_duration]`), `track_index: 2`, `bottom: 600px`. Density is irrelevant — every scene gets captions when the flag is on.
- **MIRROR**: Existing `sfx_cues:` YAML emission pattern at lines 142–154 of `phase3-5-retention.md`. Existing flag-reading pattern: where the sub-agent reads phase boundaries from `plan.md` (lines 96-119), follow the same pattern for reading `phase-status.md`.
- **GOTCHA**: Removed the original "narration density > 5 words/sec" auto-detect rule per user clarification — captions are purely user-opt-in. No density heuristic. No "smart" suggestions. The user said captions only when requested; honour that strictly.
- **GOTCHA**: track_index 2 is shared with body visual elements. The sub-agent must verify no body element on track 2 overlaps the caption span window — if collision, body element gets bumped to track 6+ (the audio-design rules already permit ≥3 for SFX; visual tracks are 1, 2; high-numbered tracks are unconstrained).
- **GOTCHA**: Filler token filter (`uh`, `um`, `huh` < 0.1s) is already applied at line 52–57 of phase3-5-retention.md. The caption strategy uses the *filtered* transcript. Reference that filter, don't re-implement.
- **GOTCHA**: When the flag is `true` mid-pipeline (user adds `captions: true` to phase-status.md after Phase 1 completed), Phase 3.5 must still honour the flag — phase ordering doesn't lock the flag retroactively.
- **VALIDATE**: Re-run Phase 3.5 on a sample video twice:
  - With `phase-status.md captions: false` → `retention-strategy.md` opens with the off-comment; no `caption_strategy` blocks present
  - With `phase-status.md captions: true` → `caption_strategy` blocks emitted per scene; word indices map correctly to transcript.json

### Task 11: UPDATE `.claude/skills/diy-yt-creator/new-anthropic-short.md` (insert conditional Step 8.5 + Step 11)

- **ACTION**: Add one conditional step and one always-on step to the skill workflow.
- **IMPLEMENT**:
  - **Step 8.5 (after current Step 8 "edit composition") — CONDITIONAL**: "Wire caption-karaoke ONLY if `retention-strategy.md` contains `caption_strategy:` blocks. If the file opens with `# captions: off`, SKIP this step entirely (do not insert any `<div id="captions">`, do not generate spans, do not add caption tweens to the timeline). When captions ARE present:"
    - Read `retention-strategy.md`'s `caption_strategy` blocks
    - Read `transcript.json` for word slices
    - Read `shared/lib/components/caption-karaoke/recipe.md`
    - Generate per-word `<span>` blocks following the recipe; insert into `videos/<slug>/index.html` inside a single `<div id="captions">` parent
    - Add corresponding GSAP tween calls to the `tl` timeline before `window.__timelines["main"] = tl;`
  - **Step 11 (after current Step 10 "inspect overflow") — ALWAYS ON**: "Validate spec compliance."
    - Run `node scripts/validate-shorts-spec.cjs videos/<slug>` — exit 1 fails the build, agent must remediate
- **MIRROR**: Existing step pattern at lines 138–296 of `new-anthropic-short.md`.
- **GOTCHA**: The skill currently has 10 steps; renumbering matters. Preserve "Step 8: edit composition" as-is; insert 8.5 (so old Step 9 stays Step 9 etc.). Add Step 11 at the end.
- **GOTCHA**: Step 8.5 is **double-conditional**: (a) `retention-strategy.md` must have `caption_strategy` blocks (which only happens when `PARAMS.captions=true` per Task 10), AND (b) the skill must not silently downgrade a missing-component case. If `caption_strategy` is present but `shared/lib/components/caption-karaoke/component.html` doesn't exist, FAIL LOUD with a message pointing at Task 7.
- **GOTCHA**: When skipping Step 8.5 (no captions), the skill must NOT add any caption-related code — including no empty `<div id="captions">` placeholder, no commented-out span template. Absence is the correct state. The validate script (Task 12) treats `<div id="captions">` absence as a valid PASS, but presence with zero spans as an ERROR.
- **GOTCHA**: For RESUME flows (re-running the skill on an existing video), preserve user-edited captions. If the user manually added/edited captions outside the pipeline, do not regenerate from `retention-strategy.md` — log a notice and skip Step 8.5 instead.
- **VALIDATE**: Manually walk through two fresh runs:
  - `cp -r templates/shorts/anthropic videos/test-no-captions` + run skill with `PARAMS.captions=false` (default) → no `<div id="captions">` in output; Step 11 passes
  - `cp -r templates/shorts/anthropic videos/test-with-captions` + run skill with `PARAMS.captions=true` → `<div id="captions">` present with per-word spans; Step 11 passes

### Task 12: CREATE `scripts/validate-shorts-spec.cjs`

- **ACTION**: Build the single-file Node CLI validator.
- **IMPLEMENT**: Argv parses positional `<project-dir>`. Reads `<project-dir>/index.html`. Uses Node's built-in `fs`, `path`, and a tiny regex-based HTML walker (no JSDOM dependency — keep it zero-dep). Checks:
  - **Safe Zone (always)**: parse `--safe-top/left/right/bottom` from `#root` style; assert `safe-top >= 380 && safe-bottom >= 380 && safe-left >= 60 && safe-right >= 120`. ERROR if any below threshold.
  - **Font-size floor (always)**: walk every CSS rule in `<style>`; for each `font-size: <N>px` declaration, ERROR if `N < 40` UNLESS the selector is in the documented hero-exception allow-list (`#p1-hero`, `.stat-num`, plus any selector tagged `/* hero-exception */` in the comment immediately above the declaration). The allow-list lives in a constant at the top of the validator.
  - **Caption checks — ABSENCE-TOLERANT**: `<div id="captions">` is OPTIONAL. If absent, all caption checks SKIP and report "captions: off (valid)". If present, all of the following fire:
    - **Caption Char Cap**: walk every `<span class="caption-word">`, group by parent `<div class="caption-line">`, sum chars per line; ERROR if any line > 42 chars.
    - **Caption Line Cap**: any `<div id="captions">` containing > 2 simultaneously visible `<div class="caption-line">` (overlap windows on `data-start`/`data-duration`); ERROR.
    - **Dwell Window**: every `<span class="caption-word">`'s `data-duration` must be ≥ 0.05s (single word) and the parent line's effective dwell (last-word-end − first-word-start) must be in `[1.0, 6.0]`s.
    - **Empty captions container**: `<div id="captions">` with zero `<span class="caption-word">` children → ERROR ("captions container present but empty — either remove the container or wire spans").
  - **APCA token check (best-effort, always)**: read `--text`, `--text-dim`, `--orange`, `--purple`, `--red` against `--bg` from `<style>`; compute APCA Lc; WARN (not error) if any used pairing scores |Lc| < 60.
- **MIRROR**: `scripts/sync-shared-lib.sh` for single-file CLI structure (shebang, usage, argv, exit codes). Use `.cjs` extension because the repo's other scripts use `.py`/`.sh`/`.cjs` (`scripts/measure-logo.cjs` is precedent).
- **GOTCHA**: APCA computation requires the official Myndex polynomial. Inline the ~80-line implementation from `apca-w3` (MIT-licensed) — do NOT add an npm dependency. Cite the source at top of file.
- **GOTCHA**: Regex HTML parsing is brittle. Scope to specific patterns (`#root\s*\{[^}]*--safe-top:\s*(\d+)px`); fail loud on parse miss with a clear message rather than silent zero.
- **GOTCHA**: Output format must be `path:line: error: message` style for editor jump-to-line. Use `index.html` line numbers from `String.split('\n')` indexing.
- **VALIDATE**:
  - `node scripts/validate-shorts-spec.cjs templates/shorts/anthropic` → exit 0 (after Tasks 1, 2, 2b land — captions absent is valid)
  - Manually inject `--safe-bottom: 200px` into the template; re-run → exit 1 with `safe-bottom: expected >=380, got 200` error
  - Manually inject `font-size: 32px;` on `.overline`; re-run → exit 1 with `font-size: expected >=40, got 32 (selector .overline not in hero-exception allow-list)`
  - Run on a hand-crafted fixture with `<div id="captions">` containing one 50-char `<div class="caption-line">` → exit 1 with `chars > 42` error
  - Run on a fixture with no `<div id="captions">` → exit 0; report "captions: off (valid)"
  - `node scripts/validate-shorts-spec.cjs videos/anthropic-amazon-compute` → expected to FAIL on safe-zone (legacy 240/60 padding); document the failure as the migration trigger.

### Task 13: UPDATE `CLAUDE.md` (add Key Rule 7 + safe-zone + opt-in captions reminder)

- **ACTION**: Add a new key rule and a one-line reminder.
- **IMPLEMENT**:
  - Insert as Key Rule 7: `**Captions are OPT-IN.** Default for every new short = no captions. Only render per-word \`<span class="clip">\` from \`shared/lib/components/caption-karaoke/\` when the user explicitly opts in via brief flag \`captions: true\` or natural-language signals like "with karaoke" / "with captions". Never auto-add based on script density, language, or topic. Anchor opt-in captions at \`bottom: 600px\` inside \`--safe-bottom: 380\`. Animate via opacity/color only (Rule 6).`
  - Append to the Key Rules section: `> **Safe Zone**: 380px top, 60px left, 120px right, 380px bottom → 900×1160 inner box. Body text floor: 40px. Enforced by \`scripts/validate-shorts-spec.cjs\`.`
- **MIRROR**: Existing numbered list in `CLAUDE.md` at lines 105–115.
- **GOTCHA**: CLAUDE.md is loaded into every session — keep additions terse. Detailed docs go in DESIGN.md and the recipe files.
- **GOTCHA**: The "OPT-IN" wording must be unambiguous. Future agents read CLAUDE.md as ground truth — if the rule is ambiguous, captions will leak in by default. Use bold and the literal word "OPT-IN".
- **VALIDATE**: Re-read CLAUDE.md end-to-end; check that line count is reasonable (current is ~115 lines; +6 lines is fine).

### Task 14: UPDATE `templates/shorts/anthropic/README.md`

- **ACTION**: Document the safe-zone tokens, the type-scale floor, and the **opt-in** caption-karaoke option.
- **IMPLEMENT**:
  - New "Safe Zone" subsection citing the 380/60/120/380 layout
  - New "Type Scale" subsection: minimum 40px body, 60–90px headline, intentional hero exceptions
  - New "Captions (Opt-In)" subsection with a clear "OFF by default" header. Explain the two ways to turn captions on: (a) `captions: true` in the brief YAML, or (b) natural-language signals in `/diy-yt-creator full-auto Topic with karaoke captions`. Link to `shared/lib/components/caption-karaoke/recipe.md` for details.
  - Mention the new `node scripts/validate-shorts-spec.cjs videos/<slug>` final-validation step
- **MIRROR**: Existing README section structure.
- **GOTCHA**: The "OFF by default" framing matters — someone skimming the README must not infer captions are recommended or automatic.
- **VALIDATE**: Markdown renders cleanly; all code-fence commands runnable as written. Show README to one fresh reader and confirm they correctly identify captions as opt-in without prompting.

---

## Testing Strategy

### Unit Tests to Write

This repo does not have a Node-side test harness for skills/templates. The validation strategy is integration-level — the validate-shorts-spec.cjs script IS the test. Document smoke-test inputs:

| Smoke Test                                                     | Input                                                            | Expected                                              |
| -------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| Clean template post-Task 2                                     | `templates/shorts/anthropic/`                                    | exit 0                                                |
| Bad safe-bottom                                                | Hand-edited template with `--safe-bottom: 200px`                 | exit 1, error mentions `safe-bottom`                  |
| Caption line >42 chars                                         | Hand-crafted index.html with a 50-char caption-line              | exit 1, error mentions `chars > 42`                   |
| Three concurrent caption lines                                 | Hand-crafted index.html, three `<div class="caption-line">` overlap | exit 1, error mentions `lines > 2`                 |
| Sparse-caption scene (no caption_strategy emitted)             | Template with no `<div id="captions">` at all                    | exit 0 (caption layer is optional)                    |
| Dwell out of range                                             | Caption line with effective dwell 0.5s                           | exit 1, error mentions `dwell < 1.0`                  |
| APCA warning                                                   | Hand-edited token `--text: #888` on `#0B0F18` (Lc ~ 50)          | exit 0 with WARNING (not error)                       |
| Legacy video                                                   | `videos/anthropic-amazon-compute/`                               | exit 1 (legacy padding), used as migration trigger    |

Place hand-crafted test fixtures in `scripts/__fixtures__/validate-shorts-spec/` so they don't pollute `videos/`.

### Edge Cases Checklist

- [ ] `--safe-*` declared but as `0px` → ERROR (zero is not a valid safe-zone)
- [ ] No `<div id="captions">` element exists → PASS (captions are optional for low-density scenes)
- [ ] `<div id="captions">` exists but has zero word spans → ERROR ("captions container empty")
- [ ] Word span on `data-track-index="3"` (collides with SFX track) → ERROR
- [ ] Word span missing `class="clip"` → ERROR (CLAUDE.md Rule 2)
- [ ] Word span overlapping the next word on the same track → ERROR
- [ ] APCA computation fails (token references undefined CSS var) → WARN, not ERROR
- [ ] Filler token (`uh`, `um`) under 0.1s in transcript got rendered as a span → WARN ("filler token rendered: filter at Phase 3.5")
- [ ] Single hero phase with NO captions and 8s dwell → PASS (only caption-layer dwell is gated, hero text is uncapped)
- [ ] Asymmetric padding: `--safe-left: 120px; --safe-right: 60px` (reversed) → ERROR (right margin must be ≥120 for YT rail)

---

## Validation Commands

### Level 1: STATIC_ANALYSIS

```bash
npx hyperframes lint templates/shorts/anthropic
npx hyperframes lint videos/<test-slug>
node -c scripts/validate-shorts-spec.cjs    # Node syntax check
```

**EXPECT**: Exit 0, 0 errors, 0 warnings.

### Level 2: SHARED-LIB SYNC

```bash
bash scripts/sync-shared-lib.sh
git diff shared/lib/MANIFEST.md
```

**EXPECT**: New entries for `caption-karaoke` and `safe-zone-overlay` appended in their respective sentinel blocks. No `[REMOVED]` markers.

### Level 3: SPEC COMPLIANCE

```bash
node scripts/validate-shorts-spec.cjs templates/shorts/anthropic
node scripts/validate-shorts-spec.cjs scripts/__fixtures__/validate-shorts-spec/clean
node scripts/validate-shorts-spec.cjs scripts/__fixtures__/validate-shorts-spec/bad-safe-zone
node scripts/validate-shorts-spec.cjs scripts/__fixtures__/validate-shorts-spec/over-42-chars
```

**EXPECT**:
- Clean template + clean fixture: exit 0
- Bad-safe-zone fixture: exit 1, error mentions `safe-*`
- Over-42-chars fixture: exit 1, error mentions `chars > 42`

### Level 4: LAYOUT INSPECT

```bash
npx hyperframes inspect templates/shorts/anthropic
npx hyperframes inspect videos/<test-slug>
```

**EXPECT**: 0 layout issues across 9 samples — confirms Task 2's `max-width: 920 → 900` reduction did not introduce overflow.

### Level 5: PIPELINE END-TO-END (manual smoke)

```bash
# 1. New project from updated template
cp -r templates/shorts/anthropic videos/test-spec

# 2. Run pipeline phases — confirm Phase 2.5's new gates fire
# (manual via /diy-yt-creator full-auto with a test brief)

# 3. After PAUSE 1, generate narration + transcript
npx hyperframes tts videos/test-spec/script.txt -o videos/test-spec/audio/narration.wav
npx hyperframes transcribe videos/test-spec/audio/narration.wav -d videos/test-spec

# 4. Run Phase 3.5 — confirm caption_strategy block emitted for dense scenes

# 5. Composition build via /diy-yt-creator new-anthropic-short
#    Confirm Step 8.5 wires karaoke spans, Step 11 runs validate-shorts-spec.cjs

# 6. Preview
npx hyperframes preview videos/test-spec
```

**EXPECT**: Karaoke caption visible, word highlights track audio, captions sit in the new safe zone, validate script passes.

### Level 6: VISUAL QA (browser)

Use `npx hyperframes preview videos/test-spec?debug=1` and confirm:

- [ ] Safe-zone overlay renders four dashed rectangles outlining the 900×1160 inner box
- [ ] All caption words land *inside* the inner box (no clipping at margins)
- [ ] No element renders within the right 120px (Like/Comment/Share/Remix zone)
- [ ] No element renders within the bottom 380px (channel description / subscribe zone)
- [ ] Karaoke active-word highlight syncs to narration audio (latency feels < 100ms)

---

## Acceptance Criteria

- [ ] `templates/shorts/anthropic/index.html` uses `--safe-*` tokens; inner box measures 900×1160 px exactly.
- [ ] All 8 sub-40px font-size declarations (lines 163, 202, 271, 327, 339, 346, 361, 404) raised per Task 2b mapping; `#p1-hero` 200px and `.stat-num` 180px preserved as documented hero exceptions.
- [ ] `shared/lib/components/caption-karaoke/` exists with both `component.html` and `recipe.md`; `MANIFEST.md` lists it; `recipe.md` opens with bold "OPT-IN ONLY" header.
- [ ] `shared/lib/components/safe-zone-overlay/` exists similarly.
- [ ] `scripts/validate-shorts-spec.cjs` runs zero-dep on Node 18+; exits 0 on the updated template (captions absent is valid); exits 1 on each negative fixture.
- [ ] **Captions stay OFF by default**: a fresh `cp -r templates/shorts/anthropic videos/<slug>` followed by the standard skill run produces a video with NO `<div id="captions">` element unless the user explicitly opts in.
- [ ] **Opt-in path works**: passing `captions: true` in the brief OR including "with karaoke" in `/diy-yt-creator full-auto` arguments propagates through `phase-status.md` → Phase 2.5 (QG-5 fires) → Phase 3.5 (`caption_strategy` emitted) → skill Step 8.5 (spans wired) → validator (caption checks fire and pass).
- [ ] Phase 2.5 critique accepts 200 WPM scripts (previously rejected) regardless of caption flag.
- [ ] Phase 2.5 critique's QG-5 (chars/dwell/lines) reports SKIPPED when `captions=false`, BLOCKING when `captions=true`.
- [ ] Phase 3.5 emits NO `caption_strategy` blocks when `captions=false`; emits per-scene blocks when `captions=true` (no density gating).
- [ ] `new-anthropic-short` skill Step 8.5 is conditional on `caption_strategy` presence; Step 11 (validate-shorts-spec) is always-on.
- [ ] DESIGN.md and `shared/lib/visual-styles/anthropic-dark.md` document APCA scores ≥75 for primary/secondary text pairings, plus a Type Scale section with hero exceptions clearly badged.
- [ ] CLAUDE.md Key Rule 7 uses literal "OPT-IN" wording; safe-zone + 40px floor reminder appended.
- [ ] README.md has a "Captions (Opt-In)" section with "OFF by default" framing.
- [ ] Existing `videos/anthropic-amazon-compute/` is NOT auto-migrated — documented as legacy in plan notes.
- [ ] No regression: existing `npx hyperframes lint` and `inspect` continue to pass on template and on legacy video.

---

## Completion Checklist

- [ ] Tasks 1, 2, 2b, 3, 4 complete (token + template + typography + design docs)
- [ ] Tasks 5–8 complete (shared-lib components + recipes)
- [ ] Task 8b complete (brief-template + full-auto opt-in flag)
- [ ] Tasks 9–11 complete (pipeline phase + skill updates with opt-in conditionals)
- [ ] Task 12 complete (validate-shorts-spec.cjs with absence-tolerant caption checks + font-size walker)
- [ ] Tasks 13–14 complete (CLAUDE.md + README.md docs with explicit OPT-IN framing)
- [ ] Level 1–4 validation commands pass
- [ ] Level 5 end-to-end pipeline smoke test passes on TWO fresh slugs:
  - `videos/test-spec-no-captions/` (default flow, no captions present)
  - `videos/test-spec-with-captions/` (`with karaoke` flow, captions present)
- [ ] Level 6 browser QA confirms karaoke + safe zone visually on the with-captions slug
- [ ] Old video (`videos/anthropic-amazon-compute/`) flagged as legacy in plan notes; no auto-migration attempted

---

## Risks and Mitigations

| Risk                                                                          | Likelihood | Impact | Mitigation                                                                                                                                       |
| ----------------------------------------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 200px hero slam word overflows the new 900px inner width                      | MED        | MED    | Task 2 includes a re-test for hero overflow; fallback is dropping hero font 200→180px (already a known knob per `new-anthropic-short.md:289–293`) |
| `class="clip"` on hundreds of word `<span>`s slows GSAP timeline registration | LOW        | MED    | GSAP handles thousands of tweens fine; pre-built timeline is paused; only render-time impact, not preview-time. Profile with `gsap.timeline().getChildren().length` if symptoms appear |
| Regex-based HTML parsing in validate-shorts-spec.cjs misses edge cases        | MED        | MED    | Fail-loud on parse miss; document fixture-driven test suite; if pain accumulates, swap for `parse5` (zero-dep streaming HTML parser, ~50KB)      |
| Asymmetric padding visually unbalances existing 4-phase template              | LOW        | LOW    | Right rail 120px is a hard YT-UI clearance rule; the visual asymmetry is a feature, not a bug. Document in DESIGN.md so designers don't "fix" it |
| Phase 2.5 char/dwell gate rejects scripts that pass today                     | MED        | LOW    | Gate is BLOCKING but actionable — error message includes the offending chunk and the proposed split. Authors fix scripts in minutes, not hours   |
| APCA inlined polynomial drifts from upstream apca-w3 over time                | LOW        | LOW    | Polynomial is stable (Lc-W3 is published spec); cite version + commit at top of validate-shorts-spec.cjs; revisit annually                       |
| Existing video fails new validate script when re-rendered                     | HIGH       | LOW    | Expected & documented. Migration is opt-in — re-copy tokens, regenerate captions. Not a blocker for new-video pipeline.                          |
| 56px caption font-size + asymmetric margins push hero/caption layout          | LOW        | LOW    | Caption sits at `bottom: 600px` (well above safe-bottom 380); hero phases fade out before captions appear. No z-stack collision                  |
| `.tl-sub` jumping 28→40px overflows 3-card timeline vertical layout           | MED        | LOW    | Task 2b includes `gap` recheck and `inspect` verification; fallback is bumping `.timeline-list { gap }` from 24→28px and `.tl-card` padding 22→26px |
| `.tl-index` 40px font clips inside 56×56 box                                  | MED        | LOW    | Documented in Task 2b GOTCHA; bump box to 60×60 if visual preview shows clipping                                                                  |
| Future agent forgets opt-in default and auto-emits captions                   | MED        | MED    | CLAUDE.md Key Rule 7 uses literal "OPT-IN" wording; recipe.md opens with bold "OPT-IN ONLY"; Phase 3.5 default is explicit no-emit comment in `retention-strategy.md`. Three independent reminders make accidental on-by-default extremely unlikely  |
| User says "with karaoke" in passing context but doesn't actually want them    | LOW        | LOW    | Brief flag is the canonical surface; NL parser is best-effort. If false-positive, user can remove `<div id="captions">` and re-validate; non-destructive |

---

## Notes

**Why NOT split into multiple PRs**: Tasks 1–4 (tokens + template + docs) are tightly coupled — partial application leaves the template inconsistent. Tasks 5–8 (shared-lib components) depend on Tasks 1–2 because they reference `--safe-*` vars. Tasks 9–11 (pipeline phases) reference the recipe from Task 8. Task 12 (validate script) gates everything else. Bundle as one PR; reviewers can read top-to-bottom in dependency order.

**Why ship the legacy video as-is**: `videos/anthropic-amazon-compute/` is a working production asset with hand-tuned counter-tweens and SFX timing. Retroactive padding changes would shift every `data-start` value and risk regression. The plan documents the validation failure as the *migration trigger* — when someone re-renders the video, they re-copy tokens, regenerate captions from `transcript.json`, and validate. Until then, the legacy short ships at 240/60/60/240. This trade is intentional.

**APCA vs WCAG dual-track**: The article makes a strong case for APCA, but WCAG is what audit tools and accessibility laws check today. We document both. APCA targets are aspirational/algorithmic; WCAG targets remain the legal baseline. Token choices that pass APCA ≥75 will almost always pass WCAG AA — the inverse is not always true.

**Why not patch upstream `@hyperframes/core`?** The HyperFrames CLI is owned by the Heygen team. Repo-local validate keeps us moving without an upstream dependency. If the team adopts safe-zone validation natively, the local script can be deprecated. Document this in the validate-shorts-spec.cjs header as "interim local enforcement; upstream proposal pending".

**Pattern-interrupt cadence**: The article calls for visual pattern interrupts every 2–4 seconds. The current pipeline averages ~6.6s per phase. We do NOT add a metronomic interrupt mechanism — `.claude/rules/audio-design.md` parks beat-grid as long-form-only. The opt-in caption-karaoke component, when used, IS the 2–4s pattern interrupt at ~0.3–0.5s cadence per word — exceeding the spec organically via transcript-anchored flow. **When captions are off (default)**, retention is carried by the existing per-phase blur-crossfades, hero slam shakes, marker highlights, counter-tweens, and SFX cues — these already provide phase-level interrupts every ~6s and intra-phase micro-interrupts (shake, mark-fill scaleX, scribble-line scaleX) at ~0.5–1s cadence. The pipeline retains its current retention performance without captions; karaoke is an additive boost for users who want it.

**Why captions are opt-in, not auto-applied**: The user explicitly clarified that captions must only appear when requested. This honours three concerns: (1) **artistic control** — short-form video is a craft; mandatory captions on every video would homogenise the channel's visual identity, (2) **compute cost** — generating per-word spans + GSAP tweens for every video adds non-trivial composition build time, (3) **template flexibility** — not every short topic benefits from karaoke (e.g., a hero-stat-driven 25s short with 3 hero phases doesn't need word-by-word; the hero slam IS the visual). The opt-in design also creates a clean A/B-test surface: ship two videos on similar topics (one with, one without) and measure retention impact directly via the platform analytics.

**Why typography fixes are not opt-in**: The 8 sub-40px elements degrade legibility for *every* viewer regardless of preference. Unlike captions (a stylistic addition), the 40px floor is a compression survival rule — text below 40px flickers and blurs under H.264 chroma subsampling, period. There is no "I prefer my body text at 30px" choice that survives the medium. So Task 2b is unconditional and lands in the template once, for all future videos.

**Future opt-in templates**: When the next shorts template lands (`templates/shorts/<style>/`), it inherits safe-zone tokens automatically by linking `shared/lib/tokens/anthropic-dark.css` (or its own equivalent). The validate script is template-agnostic — it only reads `--safe-*` from `#root`, not template-specific class names.

**Confidence Score**: 8/10 for one-pass implementation success.
- +2: Codebase fully mapped; every file:line reference verified; no ambiguity in patterns to mirror
- +2: External research (the user-supplied article) is comprehensive and unambiguous; user clarifications (typography coverage + opt-in captions) baked in directly
- +2: Zero new framework primitives; everything fits existing CLAUDE.md rules
- +1: Opt-in flag flow is well-defined (brief → full-auto → phase-status → 2.5/3.5/skill) but touches 4 surfaces; small risk of one surface drifting from the others
- +1: Validation script gives hard pass/fail signal with specific error messages including font-size walker
- −1: APCA inline polynomial is the one new computation we're authoring; small risk of arithmetic error
- −1: Phase 2.5's new chunking heuristic for ≤42 chars × line is a heuristic, not a deterministic split — first author may need 1–2 iterations to tune the boundary cases
