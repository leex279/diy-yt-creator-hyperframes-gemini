---
name: video-review
description: Comprehensive video-production review for a HyperFrames video. Dispatches 5 specialized agents in parallel to audit timing/pacing, render blockers, layout/typography, script/content, and YouTube metadata. Aggregates findings by severity (BLOCKER / HIGH / MEDIUM / LOW) and applies safe deterministic fixes. Use when the user asks "review my video", "video QA", "check video for issues", "audit video <slug>", "is video ready to publish", "video production review", "what's wrong with the video", "review timing", "review layout", "check thumbnail frames", "check engagement CTA". Also auto-invoked as the final phase of /diy-yt-creator:full-auto. Catches everything that can go wrong in HyperFrames video creation — timing gaps > 5s, missing step-by-step reveals, SFX-to-visual drift, font-family render blocker, sub-comp ID mismatches, Shorts typography under min size, first/last frame not thumbnail-grade, heteronym pronunciation risk, missing engagement CTA, YouTube description structure violations, chapter timestamps not matching speedup factor.
---

# video-review

Holistic video-production review that catches everything that can go wrong in HyperFrames video creation. Reads `.claude/rules/*.md` (the failure-mode catalog), dispatches 5 specialized review agents in parallel, aggregates their findings, and applies safe deterministic fixes.

## When to invoke

Trigger phrases:
- "review my video / video <slug>"
- "video QA / video review / production review"
- "check video for issues / audit video"
- "is the video ready to publish / ready to render"
- "what's wrong with videos/<slug>"
- "review timing on …"
- "review layout / typography on …"
- "check thumbnail frames on …"
- "check engagement CTA"
- `/video-review <slug>` (slash command)

Also invoked automatically by `/diy-yt-creator:full-auto` as **Phase R**, between Phase YT (description) and Step Z (preview).

## What this skill is — and isn't

**Is:** a parallel orchestrator over five specialized agents that cover the entire HyperFrames video-production failure surface (timing, render, layout, content, metadata). Each agent encodes a specific subset of `.claude/rules/*.md` and the user's memory feedback.

**Is NOT:** a replacement for `/diy-yt-creator:phase2-5-critique` (which is script-pre-TTS quality gate) or `/diy-yt-creator:phase2b-factcheck` (script vs. source fact-check). Both of those run earlier in the pipeline. This skill runs AFTER composition build and validates the WHOLE artifact.

## Inputs

```
/video-review <slug> [--mode <mode>] [--fix <policy>] [--visual] [--severity <floor>]
```

- `<slug>` — video folder (e.g. `claude-code-v2-launch`). REQUIRED. All paths are `videos/<slug>/…`.
- `--mode pre-render | pre-publish | perfect` — checklist intensity. Default: `pre-publish`.
  - `pre-render` — only BLOCKER findings count; want to know "will this render at all"
  - `pre-publish` — BLOCKER + HIGH must be clean; HIGH-quality bar
  - `perfect` — every level reported (BLOCKER + HIGH + MEDIUM + LOW)
- `--fix off | safe | aggressive` — auto-fix policy. Default: `safe` (per user signoff).
  - `off` — report only
  - `safe` — auto-apply mechanical fixes (font-var sed, scaffold missing description, render-filename corrections, missing `#cta-question` slot, banned-phrase swap in description); ask before any script edit
  - `aggressive` — also auto-apply heteronym swaps + banned-CTA rewrites + pacing tweaks
- `--visual` — additionally run the screenshot pass (requires `npx hyperframes preview` running). Off by default for speed.
- `--severity blocker|high|medium|low` — minimum severity to report. Default `low` in `perfect` mode; `medium` in `pre-publish`; `blocker` in `pre-render`.

## Process

### Step 1 — Validate inputs

a. Verify `videos/<slug>/` exists. If not: ERROR — list known slugs from `videos/*/`.
b. Verify `videos/<slug>/index.html` exists. If not: ERROR — composition not built yet.
c. Determine video kind:
   ```bash
   # canvas size from hyperframes.json, falling back to first <div> with data-width/data-height
   ```
   `vertical = 1080x1920 or 1080x1080 (treat as shorts-like for typography + thumbnail rules)`
   `horizontal = 1920x1080 (long-form)`
d. If `--visual`, verify preview is reachable:
   ```bash
   curl -fsS -o /dev/null "http://localhost:3002/api/projects/<slug>/preview" || echo "preview not running"
   ```
   If not running, ASK the user whether to (a) start preview, (b) fall back to static mode, or (c) abort.

### Step 2 — Dispatch the 5 agents in parallel

Invoke ALL FIVE agents in a single message with parallel `Agent` tool calls. Use `subagent_type="general-purpose"` and inline the agent file's body as the prompt (the agent files at `.claude/agents/video-*.md` are also registered as first-class subagents for future sessions — if you're in a session that has them loaded, prefer `subagent_type="video-timing-pacer"` etc).

The 5 agents and the order priority for reporting (timing FIRST, per user emphasis):

1. **`video-timing-pacer`** — TIMING IS PRIORITY 1. Visual-pacing-5s, step-by-step reveal, hidden-until-reveal pattern, SFX-to-visual drift, composition duration vs narration, scene continuity, track-index overlap.
2. **`video-render-validator`** — lint/validate/inspect, font-var render blocker, sub-comp ID match, missing media sources, oversized images, backdrop-filter stacks, render filename.
3. **`video-layout-typography`** — Shorts typography minimums, first/last frame thumbnail-grade (5 mandatory elements each), bar-chart marker anti-pattern, shape-backdrop rearrange, WCAG contrast, overflow. `--visual` mode adds screenshot QA.
4. **`video-script-content`** — heteronym + tech-term audit, engagement CTA in 3 places, banned CTA phrases, source-grounded fact check, hook strength, narration speed sanity, Hostinger wording.
5. **`video-metadata-publish`** — youtube-description.md structure, Dynamous + Hostinger blocks, hashtags, chapter timestamps post-speedup, vidIQ research, URL validation, CTA cross-reference, banned sections.

Each agent returns a JSON object on stdout (schema in each `.claude/agents/video-*.md`). The orchestrator parses each.

Pass each agent two arguments (inline at top of the prompt):
```
slug: <slug>
mode: <visual or static>   # only video-layout-typography honors mode
```

### Step 3 — Aggregate findings

Merge all 5 agent JSON outputs into a single report. De-duplicate findings that report the same `rule` and `location` (e.g., timing-pacer §8 and render-validator §8 both flag composition-duration-vs-narration).

Sort findings:
1. By severity descending: BLOCKER > HIGH > MEDIUM > LOW
2. Within severity, by agent priority: timing-pacer > render-validator > layout-typography > script-content > metadata-publish
3. Within agent, by file:line

Compute the overall verdict:
- Any BLOCKER → `FAIL_BLOCKER`
- Any HIGH (no BLOCKER) → `FAIL_HIGH`
- Any MEDIUM (no HIGH or BLOCKER) → `WARN_MEDIUM`
- Only LOW → `PASS_LOW`
- Empty → `PASS`

Apply the `--mode` and `--severity` filters before reporting.

### Step 4 — Apply safe auto-fixes (when `--fix safe` or `--fix aggressive`)

For each finding with `auto_fixable: true` AND severity ∈ (BLOCKER, HIGH):

a. Read the file to be modified.
b. Apply the fix described in the finding's `fix` field.
c. Re-run only the agent that reported the finding to confirm the fix landed.
d. Update the finding to `status: AUTO_FIXED`.

**Safe-fix recipes** (deterministic — no user input needed):

| Rule | Auto-fix recipe |
|------|-----------------|
| `font-family-var-render-blocker` | sed replacement per `.claude/rules/hyperframes-pitfalls.md` §8 |
| `sub-comp-id-mismatch` | rewrite parent mount's `data-composition-id` to match child file's `<div id="root" data-composition-id="...">` |
| `render-filename-uses-short.mp4` | replace `short.mp4` references with `<slug>.mp4` |
| `youtube-description-missing` | scaffold from canonical template; fill topic from `meta.json.name` |
| `description-dynamous-block-missing` | insert canonical Dynamous block (BOTH URLs, `----` wrap) AFTER SEO hook, BEFORE Chapters/Resources — independent of `dynamousPromotion` flag |
| `description-dynamous-block-malformed` | replace existing block with canonical verbatim block |
| `description-banned-phrase` | replace last paragraph with the spoken closer's verbatim question |
| `description-forbidden-arrow` | strip `→` / `->` characters |
| `description-hostinger-sponsored-wording` | replace "Sponsored by Hostinger" with "Try Hostinger" |
| `description-banned-section` | remove `Key Concepts` / `Key Stats` / similar headers and their bodies |
| `chapter-timestamp-speedup-mismatch` | recompute `data-start / speed_factor` for every chapter |
| `cta-question-element-missing` | scaffold `<div id="cta-question" ...>` in the final phase with the spoken closer's question |

**Aggressive-fix-only recipes** (off by default; require `--fix aggressive`):

| Rule | Aggressive auto-fix recipe |
|------|----------------------------|
| `heteronym-risk-live-adjective` | swap `live today` → `available today`, `live on` → `shipping on` |
| `heteronym-risk-lead-noun` | swap `lead agent` → `primary agent` |
| `tech-term-pronunciation` | apply rule-table spelling in TTS script (not raw script) |

**NEVER auto-fix** (always require user signoff):
- Pacing edits to `index.html` GSAP tweens (timing changes affect downstream chapter timestamps + SFX alignment)
- Script wording changes that alter meaning
- Image resizing (touches assets)
- Backdrop-filter rework (visual style choice)
- URL replacement after WebFetch 404 (user picks the correct URL)

### Step 5 — Produce the report

Output a human-readable Markdown report to stdout. Save the full JSON to `videos/<slug>/qa/review-report.json` for diff-against-previous-runs.

Report template:

```markdown
# Video Review — <slug>

**Verdict**: FAIL_BLOCKER · 2 BLOCKER · 5 HIGH · 1 MEDIUM · 0 LOW
**Mode**: pre-publish · **Auto-fix**: safe · **Visual**: off
**Canvas**: 1080×1920 (vertical Short)

## Auto-fixes applied (<N>)

- ✅ R-001 font-family `var(--sans|--mono)` replaced with literal `'Inter'` / `'JetBrains Mono'` in index.html + 4 compositions (BLOCKER → fixed)
- ✅ S-002 banned phrase "What do you think?" replaced with spoken closer in youtube-description.md (HIGH → fixed)

## BLOCKER (must fix before render)

### T-001 · Composition duration shorter than narration · `video-timing-pacer`
**Location:** `videos/<slug>/index.html:432`
**Evidence:** `npx hyperframes compositions` reports duration=24.0s; narration.wav is 30.2s. MP4 will cut off mid-sentence.
**Fix:** Add as last line of root timeline: `tl.set({}, {}, 30.7)`
**Auto-fixable:** yes (orchestrator can apply if `--fix safe`)

## HIGH (must fix before publish)

### T-004 · Visual-pacing 5s violation · `video-timing-pacer`
**Location:** `videos/<slug>/index.html:#phase4` (t=77.5 → t=85.7, gap=8.2s)
**Evidence:** Last entrance is `tl.from('#p4-quote-card', ..., 77.5)`. Phase exits at t=85.7. 8.2s static window exceeds 5s cap.
**Fix:** Insert marker-sweep at t≈82.5: `tl.to('#p4-mark-A', { width: '100%', duration: 0.6, ease: 'power2.out' }, 82.5)` and at t≈87.5 on `#p4-author-name`.

[…remaining findings…]

## MEDIUM (quality improvements)

[…]

## What ran

- `video-timing-pacer` · 18 entrances audited across 6 phases · 1 BLOCKER · 3 HIGH
- `video-render-validator` · lint clean · validate AA pass · inspect 0 overflow · 1 BLOCKER (font-var)
- `video-layout-typography` · 4 typography violations · first-frame PASS · last-frame FAIL
- `video-script-content` · heteronyms 0 · CTA across 3 places: PARTIAL · 0 unsourced claims
- `video-metadata-publish` · description present · chapters NOT speedup-adjusted · hashtags 18

## Next steps

1. Apply or accept the 2 BLOCKER auto-fixes above (rerun `/video-review <slug>` to confirm).
2. Address the 5 HIGH findings before publish.
3. (Optional) Run `/video-review <slug> --visual` for the screenshot pass.

Report saved: `videos/<slug>/qa/review-report.json`
```

### Step 6 — Cleanup

If any agent created temp files (e.g., `/tmp/<slug>-lint.json`), leave them — they're useful for diff-against-previous. They get cleaned up at the next session boundary.

## Failure-mode catalog (what the agents catch — quick scan)

Pulled from `.claude/rules/*.md` and memory:

| # | Rule | Agent | Severity |
|---|------|-------|----------|
| 1 | Composition duration < narration length (`hyperframes-pitfalls` §1) | render-validator + timing-pacer | BLOCKER |
| 2 | font-family: var(--sans\|--mono) compile error (`hyperframes-pitfalls` §8) | render-validator | BLOCKER |
| 3 | Sub-comp `data-composition-id` mismatch (`sub-composition-wiring`) | render-validator | BLOCKER |
| 4 | Missing `<video>` source → 45s FrameCapture timeout (`hyperframes-pitfalls` §6) | render-validator | BLOCKER |
| 5 | Missing `<audio>` source (lint `audio_src_not_found`) | render-validator | BLOCKER |
| 6 | Missing `class="clip"` / `data-start` / `data-duration` / `data-track-index` (CLAUDE.md Key Rules) | timing-pacer | BLOCKER |
| 7 | Missing engagement CTA in 3 places (`engagement-cta`) | script-content | BLOCKER |
| 8 | Banned CTA phrase in closer (`engagement-cta` anti-patterns) | script-content | BLOCKER |
| 9 | Unsourced numeric/dated/quoted claim (memory `no_fabrication_source_only`) | script-content | BLOCKER |
| 10 | Missing `youtube-description.md` (`youtube-metadata`) | metadata-publish | BLOCKER |
| 11 | Visual-pacing > 5s static (`visual-pacing-5s`) | timing-pacer | HIGH |
| 12 | All-bullets-at-once (no step-by-step) on 4+ item list (`step-by-step-reveal`) | timing-pacer | HIGH |
| 13 | `tl.from()` at t>5 without `tl.set` at t=0 or `immediateRender: false` | timing-pacer | HIGH |
| 14 | Scene-to-scene continuity gap > 0.5s (memory `continuous_scenes_no_gaps`) | timing-pacer | HIGH |
| 15 | Card entrance not matched to word anchor (drift > 0.15s) | timing-pacer | MEDIUM |
| 16 | SFX-to-visual drift > 0.05s on percussive cue (`audio-design`) | timing-pacer | HIGH |
| 17 | `cinematic-whoosh` data-duration < 1.5s (`audio-design`) | timing-pacer | HIGH |
| 18 | `cinematic-whoosh` fires pre-roll at sceneT-0.4 instead of sceneT | timing-pacer | HIGH |
| 19 | Track-index overlap on same channel (`audio-design`) | timing-pacer | HIGH |
| 20 | Shorts text below typography minimum (`shorts-typography`) | layout-typography | HIGH |
| 21 | First frame not thumbnail-grade (`shorts-thumbnail-frames`) | layout-typography | HIGH/BLOCKER |
| 22 | Last frame not thumbnail-grade (`shorts-thumbnail-frames`) | layout-typography | HIGH |
| 23 | Bar-chart screenshot marker overlay (`screenshot-anchor-markers`) | layout-typography | HIGH |
| 24 | Shape-backdrop NOT rearranged on phase transition (memory `shape_rearrange_on_whoosh_default`) | layout-typography | MEDIUM |
| 25 | WCAG AA contrast failures | layout-typography + render-validator | HIGH |
| 26 | Layout overflow | layout-typography + render-validator | HIGH |
| 27 | Heteronym pronunciation risk (`tts-pronunciation`) | script-content | HIGH |
| 28 | Tech-term pronunciation risk (`tts-pronunciation`) | script-content | MEDIUM |
| 29 | Hook score < 6 (`engagement-hooks-framework`) | script-content | MEDIUM |
| 30 | Narration speed drift > 20% from script word count | script-content | LOW |
| 31 | Hostinger banner reads as "Sponsored" (memory `hostinger_affiliate_not_sponsored`) | script-content | LOW |
| 32 | YouTube description structure order wrong | metadata-publish | HIGH |
| 33a | Dynamous block MISSING from description (mandatory on every video — independent of `dynamousPromotion` meta flag) | metadata-publish | BLOCKER |
| 33b | Dynamous block format drift (missing URLs, missing emoji, missing `----`, wording change) | metadata-publish | HIGH |
| 34 | Hostinger block missing or wrong format | metadata-publish | HIGH |
| 35 | Hashtags < 15 or > 25 | metadata-publish | HIGH |
| 36 | Chapter timestamps not adjusted for ffmpeg speedup (memory `update_description_on_speedup`) | metadata-publish | HIGH |
| 37 | Chapters section on a Shorts video | metadata-publish | HIGH |
| 38 | First 200 chars NOT keyword-front-loaded | metadata-publish | HIGH |
| 39 | URL returns 404 / dead | metadata-publish | HIGH |
| 40 | Engagement CTA across 3 surfaces don't match | metadata-publish + script-content | HIGH |
| 41 | Banned section in description (Key Concepts, etc.) | metadata-publish | MEDIUM |
| 42 | Oversized images (>2× canvas) hurting preview FPS | render-validator | MEDIUM |
| 43 | Heavy backdrop-filter stack (>3 layers or >64px radius) | render-validator | MEDIUM |
| 44 | Render `-o short.mp4` instead of `<slug>.mp4` (memory `render_filename_uses_slug`) | render-validator | LOW |
| 45 | vidIQ research artifact missing | metadata-publish | MEDIUM |
| 46 | `→` arrows in description | metadata-publish | MEDIUM |
| 47 | Generic chapter title (BAD: "Introduction") | metadata-publish | MEDIUM |

## Self-check before declaring review done

- [ ] All 5 agents ran (or you reported which one failed and why)
- [ ] Findings de-duplicated on (rule, location)
- [ ] Findings sorted by severity then agent priority
- [ ] Verdict computed correctly
- [ ] Auto-fixes (if `--fix safe`) actually re-ran the affected agent to confirm
- [ ] Report saved to `videos/<slug>/qa/review-report.json`
- [ ] Markdown report printed to stdout
- [ ] If `--visual` was requested, screenshot pass actually ran

## Don'ts

- Don't run an agent for the wrong video kind (e.g., long-form chapter check on a Short).
- Don't auto-fix anything outside the "safe-fix recipes" table without confirming with the user.
- Don't claim PASS without actually running all 5 agents — partial coverage is not PASS.
- Don't edit the script narration as part of auto-fix — it cascades into TTS regeneration, transcript invalidation, retiming. Always surface those as user-confirm findings.
- Don't run during a render — the renderer drives its own headless browser; another browser snapshotting at the same time may interfere (relevant only for `--visual`).
