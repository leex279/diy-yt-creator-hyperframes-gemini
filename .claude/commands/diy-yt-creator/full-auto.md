---
description: "Full pipeline orchestrator (go all-in): research → plan → script → critique → TTS-script → fact-check → TTS → transcribe → retention → composition build → lint → preview"
argument-hint: <topic | URL | brief.md> [--resume <slug>]
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebSearch, WebFetch
---

<objective>
Orchestrate the HyperFrames pipeline end-to-end with NO handoff pauses: phases 0 → 1 → 2 → 2.5 → 2a → 2b → `npx hyperframes tts` → `npx hyperframes transcribe` → phase 3.5 → composition build (via the template playbook, e.g. `new-anthropic-short`) → lint → inspect → Phase YT (YouTube description) → Phase R (video-review quality gate) → preview.

**Goal**: Go from "I have an idea" to "previewable video composition" in one invocation. The user reviews the output in `hyperframes preview`; they do NOT shepherd the pipeline between phases.

**Output**: Every artifact under `videos/<slug>/`, ending with a previewable composition. No auto-render — `npx hyperframes render` remains the user's call.

**Pause policy (per user feedback `feedback_full_auto_no_pauses`)**: NEVER pause for handoff. Only stop early if there's something concrete to TELL the user — a blocking gate failure (Phase 2.5 critique blocked on un-overridable gates, Phase 2b major fabrication, lint errors after the composition build, missing source, decision that genuinely needs a human). If there is nothing to tell, keep going.

**This pipeline does NOT include**:
- Phase 5 (render) — handled by `npx hyperframes render`, always user-triggered
- YouTube **upload** — out of scope here
- YouTube **description** — auto-generated as Phase YT after the composition build (see Phase YT below). NEVER skipped.
</objective>

<initial-setup>

## Step 1 — Detect mode

Parse `$ARGUMENTS`:

| Argument pattern                  | Mode      | Action                                                                  |
| --------------------------------- | --------- | ----------------------------------------------------------------------- |
| `--resume <slug>`                 | RESUME    | Skip phases 0-2b, jump to Phase 3.5 (assumes TTS + transcribe finished) |
| `<topic-text>`                    | FREE-FORM | New pipeline. Derive slug from topic.                                   |
| `<*.md>` containing `**Topic**:`  | BRIEF     | Parse the brief (per `brief-template.md`); use its `Slug` if present    |
| YouTube URL (`youtube.com/watch`, `youtu.be/`, `youtube.com/playlist`, `youtube.com/@handle`) | YOUTUBE | New pipeline. Slug from video/channel title. Phase 0 fetches the transcript via the `youtube-transcript` skill (see `phase0-research.md` Step 0C.5) and feeds it to all four research agents. |
| `<URL>` (non-YouTube)             | URL       | New pipeline. Derive slug from URL/page title.                          |

If running in RESUME mode, read `videos/<slug>/phase-status.md` and continue from the first row whose status is `pending` (or re-run any `blocked` row after the user fixes the issue). Skip Steps 1.5-5; the template + slug are already locked from the prior run.

If new pipeline, run Steps 1.5 - 5.

## Step 1.5 — Template Discovery & Suggestion (interactive)

**Skip this step if**:
- RESUME mode (template is already in `videos/<slug>/` from the prior run), OR
- BRIEF mode AND the brief contains a `**Template:**` field with a non-empty value (use it verbatim, no prompt — the user already decided)

Otherwise, **always** run this step before locking PARAMS. The orchestrator never silent-defaults the template — the user gets a recommendation + alternatives + a chance to pick.

### Step 1.5a — Discover available templates

Scan the `templates/` directory:

```bash
# Implemented templates have BOTH index.html AND README.md (placeholders have only README.md)
find templates -mindepth 2 -maxdepth 3 -name index.html -exec dirname {} \;
```

For each implemented template directory:
- Read its `README.md` first heading + first non-blank line as the one-line summary
- Read its `hyperframes.json` (if present) for resolution + duration hints

Build a list:

| Template ID                    | Status        | Resolution  | Typical duration | One-line summary                                                  |
| ------------------------------ | ------------- | ----------- | ---------------- | ----------------------------------------------------------------- |
| `shorts/anthropic`             | implemented   | 1080×1920   | 60-180s          | Vertical YouTube Short in the Anthropic dark-stage aesthetic      |
| `long-form/*`                  | NOT YET BUILT | 1920×1080   | 4-15min          | placeholder only — `templates/long-form/README.md` describes spec |

Today (2026-04-27), only `shorts/anthropic` is implemented. Future templates will appear here automatically as they're built.

### Step 1.5b — Auto-recommend based on signals

Apply this decision tree to the topic / brief / arguments:

| Signal                                                                          | Recommendation              |
| ------------------------------------------------------------------------------- | --------------------------- |
| Brief specifies `Duration:` < 60s                                               | `shorts/anthropic`          |
| Brief specifies `Duration:` ≥ 3min                                              | a `long-form/*` template *(blocked: none implemented)* |
| Topic text contains: "short", "quick", "tiktok", "reels", "vertical"            | `shorts/anthropic`          |
| Topic text contains: "deep dive", "tutorial", "explainer", "comparison", "vs"   | a `long-form/*` template *(blocked: none implemented)* |
| Topic is an announcement / launch / "just shipped X" without duration hint      | `shorts/anthropic`          |
| Topic mentions "for YouTube" without duration hint                              | `shorts/anthropic` (default Shorts-first for the channel) |
| None of the above                                                               | `shorts/anthropic` (only implemented option today)        |

When recommending a long-form template that doesn't exist yet, surface that explicitly: "I'd recommend long-form for this topic, but no long-form template is implemented yet. Falling back to `shorts/anthropic`. Want to build a long-form template first? See `templates/long-form/README.md`."

### Step 1.5c — Present and ask

Show the user the discovery + recommendation in this format:

```
═══════════════════════════════════════════════════════════════
TEMPLATE SELECTION
═══════════════════════════════════════════════════════════════

Topic: <PARAMS.topic>
Inferred signals: <duration if known> · <topic-type hint>

Available templates:
  1. shorts/anthropic   (implemented)   1080×1920, 60-180s
       Vertical YouTube Short in the Anthropic dark-stage aesthetic.
  [— long-form/* not yet implemented; see templates/long-form/README.md]

→ Suggested: shorts/anthropic
   Reasoning: <one sentence based on the signal that triggered the pick>

Confirm? Reply with one of:
  - "yes" / Enter   → use shorts/anthropic
  - "<template-id>" → use a different listed template
  - "skip"          → abort the pipeline
═══════════════════════════════════════════════════════════════
```

Wait for the user's reply before proceeding. Treat any of these as confirmation:
- `yes`, `y`, `ok`, `proceed`, `continue`, empty/Enter, or the recommended template ID itself

Treat any **listed template ID** as a different choice. Treat anything **unlisted** as an error and re-prompt.

If the user picks a template that's `NOT YET BUILT`, STOP with a clear message — there's no folder to copy and no playbook to drive the composition build later.

Record the chosen template as `PARAMS.template`. Append a one-liner to the orchestration log:

```
Template selected: <id> (suggested: <id>; user confirmed / overrode)
```

## Step 2 — Set parameters (use defaults for missing values)

Collect remaining parameters ONCE. The template is already locked from Step 1.5. Do NOT ask additional questions later.

```yaml
PARAMS:
  topic: "<from $ARGUMENTS>"
  slug: "<from brief Slug field, or kebab-case derivation from topic>"
  template: "<from Step 1.5 (user-confirmed) OR brief Template field>"
  duration: "<from brief or default based on template — shorts/anthropic: 90s, shorts/archon: 90s, long-form/standard: 8min>"
  tone: "<from brief or default: tech-influencer-edgy>"
  links: "<URLs from brief or empty>"
  must_mention: "<from brief Must-Mention Points or empty>"
  technical_terms: "<from brief Technical Terms or empty>"
  voice_style_notes: "<from brief Voice/Style Notes or empty>"
  target_audience: "<from brief or 'developers and technical audience'>"
  key_angle: "<from brief or determine in Phase 0>"
```

### Duration → structure quick reference

| Duration | Scenes  | Words   | Structure                                                                         |
| -------- | ------- | ------- | --------------------------------------------------------------------------------- |
| 15-30s   | 3-5     | 37-75   | Hook → Solution → CTA (Anthropic Shorts: Hero → Stat → Timeline → CTA)            |
| 45-60s   | 5-7     | 112-150 | Hook → Solution → 2-4 Features → CTA                                              |
| 90s      | 7-8     | 225     | Hook → Solution → 4-5 Features → Trust → CTA                                      |
| 3min     | 9-10    | 450     | Preview → Hook → Solution → 5-7 Features → Ecosystem → Trust → CTA                |

For the `shorts/anthropic` template, the 4 base archetypes are forced by the template (see Phase 1 for adding more phases per `templates/shorts/anthropic/README.md`).

## Step 3 — Derive slug

Convert topic to kebab-case (NOT PascalCase — kebab-case is the convention here, matching `templates/shorts/anthropic/README.md`):

- "Docker sandboxes" → `docker-sandboxes`
- "Claude Code v2.1.20" → `claude-code-v2-1-20`
- "Remote agentic coding" → `remote-agentic-coding`
- A URL → use the page title or product name, then kebab-case it

If a brief specified `Slug:`, use it verbatim (assumed already kebab-case).

Store as `SLUG`.

## Step 4 — Initialize phase status file

If `videos/<SLUG>/` doesn't exist, create it (`mkdir -p videos/<SLUG>/research videos/<SLUG>/scripts`).

Create or update `videos/<SLUG>/phase-status.md`:

```markdown
# Phase Status: <SLUG>

| Phase                  | Status  | Completed |
| ---------------------- | ------- | --------- |
| 0 - Research           | pending |           |
| 1 - Plan               | pending |           |
| 2 - Script             | pending |           |
| 2.5 - Critique         | pending |           |
| 2a - TTS Script        | pending |           |
| 2b - Fact Check        | pending |           |
| 3.5 - Retention        | pending |           |
| YT - YouTube description | pending |           |

**Status vocabulary**: `pending` | `in-progress` | `done` | `done <details>` | `blocked (<reason>)`
```

Each phase command updates its own row when it completes. In crash recovery, read this file to determine where to resume.

## Step 5 — Initialize orchestration log

Create `videos/<SLUG>/orchestration-log.md` with:

```markdown
# Orchestration Log: <SLUG>

Pipeline started: <YYYY-MM-DD HH:MM>
Topic: <topic>
Template: <template>
Duration: <duration>

## Phase Summaries (<200 words each)
```

Each phase appends a <200-word summary here. Do NOT re-read full artifacts in the orchestrator.

</initial-setup>

<orchestration>

### Context isolation mandate (CRITICAL)

**All phases run as isolated sub-agents via the Task tool.** Never invoke phase commands as slash commands from this orchestrator — slash commands load their full `.md` contents plus runtime artifacts (web searches, briefs, scripts, transcripts) into the main context and cause massive context bloat by Phase 2b.

**Sub-agent dispatch**: Use `subagent_type: "general-purpose"` for every phase, with self-contained prompts that point the agent at the relevant phase command file and arguments.

After each Task returns, append ONLY a <200-word summary to `videos/<SLUG>/orchestration-log.md`. Do NOT re-read research briefs, plans, scripts, transcripts, or strategy files in this orchestrator.

### Phase status tracking + crash recovery

Each runner agent updates `videos/<SLUG>/phase-status.md` when it completes (mark row as `done <date>` or `blocked (<reason>)`). The orchestrator just checks the latest row and moves on.

**Crash recovery**: if interrupted, re-invoke `/diy-yt-creator:full-auto` (free-form mode with same topic, OR `--resume <slug>` if past Phase 2b). Read `phase-status.md`; resume from the first `pending` row.

---

## Phase 0 — Research

**Skip if** RESUME mode AND row `0 - Research` is `done`.

**Dispatch** via Task tool:

```
subagent_type: "general-purpose"
description: "Phase 0 research for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase0-research for slug `<SLUG>`.

  Read the slash command file from disk for full instructions:
    .claude/commands/diy-yt-creator/phase0-research.md

  Context (from full-auto orchestrator):
  - Topic: <PARAMS.topic>
  - Slug: <SLUG>
  - Duration: <PARAMS.duration>
  - Links to fetch: <PARAMS.links>
  - Key angle hint: <PARAMS.key_angle>
  - Target audience: <PARAMS.target_audience>

  Run in autonomous mode (do NOT ask interactive questions).

  Expected output on disk:
    videos/<SLUG>/research/content-brief.md

  When done, update videos/<SLUG>/phase-status.md row "0 - Research" to "done <date>".
  Return ONLY a <200-word summary covering: research depth used, agents A-D headline
  findings (one bullet each), vidiq enrichment status (used/skipped), quality gate
  results (counts of pass/fail/warn), and any gaps flagged for user input.
```

Wait for return. Append the <200-word summary to `orchestration-log.md`. Confirm phase-status row updated. Proceed.

---

## Phase 1 — Plan

**Skip if** RESUME mode AND row `1 - Plan` is `done`.

```
subagent_type: "general-purpose"
description: "Phase 1 plan for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase1-plan for slug `<SLUG>`.

  Read the slash command file from disk:
    .claude/commands/diy-yt-creator/phase1-plan.md

  Context:
  - Slug: <SLUG>
  - Duration: <PARAMS.duration>
  - Tone: <PARAMS.tone>
  - Template: <PARAMS.template>

  Autonomous mode. Pick the highest-scoring hook variant automatically.

  Expected output: videos/<SLUG>/plan.md

  When done, update phase-status row "1 - Plan" to "done <date>".
  Return <200-word summary: scene count, recommended hook variant + score, hook pattern,
  total data_duration, retention component pick count, fact-check audit summary.
```

Wait, log, proceed.

---

## Phase 2 — Script (raw)

**Skip if** RESUME mode AND row `2 - Script` is `done`.

```
subagent_type: "general-purpose"
description: "Phase 2 script for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase2-script for slug `<SLUG>`.

  Read: .claude/commands/diy-yt-creator/phase2-script.md

  Context:
  - Slug: <SLUG>
  - Tone: <PARAMS.tone>
  - Technical terms: <PARAMS.technical_terms>
  - Must-mention: <PARAMS.must_mention>
  - Voice style notes: <PARAMS.voice_style_notes>

  Autonomous mode (do NOT stop for user review — orchestrator handles flow).

  Expected output: videos/<SLUG>/scripts/full-script.md

  When done, update phase-status row "2 - Script" to "done <date>".
  Return <200-word summary: total word count, scene count, hook variant locked into
  Scene 01 (quote the first sentence), scar inserts present (yes/no with quote), banned
  phrase self-check status.
```

Wait, log, proceed.

---

## Phase 2.5 — Critique (BLOCKING)

```
subagent_type: "general-purpose"
description: "Phase 2.5 critique for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase2-5-critique for slug `<SLUG>`.

  Read: .claude/commands/diy-yt-creator/phase2-5-critique.md

  Run all five passes. Update phase-status row "2.5 - Critique":
    - On PASS: "done (X.X/10 hook, X.X/10 arc) <date>"
    - On FAIL: "blocked (<failed gate names>) <date>"

  Return <200-word summary: gate-by-gate verdict (QG-1 through QG-4) with scores,
  count of banned phrases found, count of loop openers found vs required, overall
  PASS/FAIL.
```

Wait. Read `phase-status.md` row `2.5 - Critique`.
- If `done`: log summary, proceed.
- If `blocked`: STOP orchestration. Surface the agent's summary verbatim to the user. Tell them to fix the issues in `videos/<SLUG>/scripts/full-script.md` and re-run `/diy-yt-creator:full-auto --resume <SLUG>`.

---

## Phase 2a — TTS Script

```
subagent_type: "general-purpose"
description: "Phase 2a TTS script for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase2a-tts-script for slug `<SLUG>`.

  Read: .claude/commands/diy-yt-creator/phase2a-tts-script.md

  Context:
  - Slug: <SLUG>
  - Technical terms: <PARAMS.technical_terms>

  CRITICAL: write BOTH the per-scene .txt files AND the flat videos/<SLUG>/script.txt
  (matching the format of videos/claude-connectors-everyday-life/script.txt). The
  flat file is required by `npx hyperframes tts`. Do not skip it.

  When done, update phase-status row "2a - TTS Script" to "done <date>".
  Return <200-word summary: scene count, scenes with character count > 800 (if any),
  TTS skill used (text-to-speech / fallback), confirmation flat script.txt was written.
```

Wait, log, proceed.

---

## Phase 2b — Fact-Check (BLOCKING)

```
subagent_type: "general-purpose"
description: "Phase 2b fact-check for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase2b-factcheck for slug `<SLUG>`.

  Read: .claude/commands/diy-yt-creator/phase2b-factcheck.md

  Autonomous mode: apply minor auto-corrections inline (rounding, date refresh, URL
  swap) AND re-flatten videos/<SLUG>/script.txt after each correction. STOP on major
  corrections (wrong stat, misattributed quote, false claim).

  Update phase-status row "2b - Fact Check":
    - On PASS: "done (N/N claims verified) <date>"
    - On FAIL: "blocked (N failed claims) <date>"

  Return <200-word summary: claims by tier (T1/T2/T3), verdict counts (verified /
  corrected / stale / unverified / failed), URL audit results, list of every
  auto-applied correction (with scene + original → corrected text + source URL).
```

Wait. Read `phase-status.md` row `2b - Fact Check`.
- If `done`: log summary, proceed immediately to TTS + transcribe (no pause).
- If `blocked`: STOP orchestration. Surface failures + corrections needed verbatim. Tell user to fix and re-run `/diy-yt-creator:full-auto --resume <SLUG>`.

---

## Step A — Run TTS + transcribe (inline, no pause)

After Phase 2b passes, execute the CLI commands directly. Do NOT pause for a handoff. Per `feedback_full_auto_no_pauses`, the user wants one-shot execution; the ElevenLabs credit spend is accepted as part of normal video production.

```bash
npx hyperframes tts videos/<SLUG>
npx hyperframes transcribe videos/<SLUG>
```

Run them sequentially via the Bash tool. After each completes:
- Verify the expected output exists (`videos/<SLUG>/audio/narration.wav` after tts; `videos/<SLUG>/transcript.json` after transcribe).
- Append a one-line entry to `videos/<SLUG>/orchestration-log.md` (`TTS: done — narration.wav <duration>s`, `Transcribe: done — N words`).

If either command FAILS:
- For tts errors (missing API key, rate limit, quota): STOP, surface the exact error verbatim, point user at `.env` / `setup-api-key` skill. Don't auto-retry blindly.
- For transcribe errors (whisper missing, ffmpeg missing): STOP, surface error verbatim, recommend `npx hyperframes doctor`.

If both succeed, proceed to Phase 3.5 (no pause, no message).

---

## Phase 3.5 — Retention Strategy

Runs immediately after transcribe succeeds. Also runs in RESUME mode if the orchestrator was interrupted between Phase 2b and Phase 3.5.

Verify `videos/<SLUG>/transcript.json` exists. If missing (e.g., user invoked `--resume` without TTS), STOP and remind the user to run `npx hyperframes tts videos/<SLUG> && npx hyperframes transcribe videos/<SLUG>`.

```
subagent_type: "general-purpose"
description: "Phase 3.5 retention strategy for <SLUG>"
prompt: |
  Run /diy-yt-creator:phase3-5-retention for slug `<SLUG>`.

  Read: .claude/commands/diy-yt-creator/phase3-5-retention.md

  The phase command spawns its OWN sub-agent for the analysis. You are the
  intermediate runner — invoke the phase command's pattern (read transcript.json,
  filter, dispatch internal sub-agent with the long self-contained prompt from
  phase3-5-retention.md, write retention-strategy.md).

  When done, update phase-status row "3.5 - Retention" to "done <date>".
  Return <200-word summary: scene count, total picks count by category (markers /
  captions / audio-reactive / transitions / gsap effects), constraint violations
  resolved, anchors with no good pick.
```

Wait, log, proceed immediately to composition build (no pause).

---

## Phase 4 — Composition Build (inline, no pause)

After Phase 3.5 completes, immediately dispatch the template-specific build playbook. Per `feedback_full_auto_no_pauses`, do NOT pause for handoff. The build skill reads `plan.md` + `scripts/full-script.md` + `retention-strategy.md` as authoritative inputs and edits `videos/<SLUG>/index.html`.

Pick the playbook from `PARAMS.template`:
- `shorts/anthropic` → `.claude/skills/diy-yt-creator/new-anthropic-short.md`
- `shorts/archon` → `.claude/skills/diy-yt-creator/new-archon-short.md`
- `shorts/standard` → `.claude/skills/diy-yt-creator/new-standard-short.md`
- `shorts/google` → `.claude/skills/diy-yt-creator/new-google-short.md`
- `shorts/openai` → `.claude/skills/diy-yt-creator/new-openai-short.md`
- `shorts/game-map` → `.claude/skills/diy-yt-creator/new-game-map-short.md`
- `shorts/claude-code-version` → `.claude/skills/diy-yt-creator/new-claude-code-version-short.md`
- `long-form/standard` → `.claude/skills/diy-yt-creator/new-long-form-standard.md`
- `long-form/claude-code-version` → `.claude/skills/diy-yt-creator/new-claude-code-version-longform.md`

Dispatch via Task tool (`subagent_type: "general-purpose"`):

```
description: "Composition build for <SLUG>"
prompt: |
  Run the composition-build playbook at <playbook-path> for slug `<SLUG>`.

  Read the playbook file from disk for full instructions.

  Inputs already on disk (Branch A — pipeline-driven build):
    - videos/<SLUG>/research/content-brief.md
    - videos/<SLUG>/plan.md
    - videos/<SLUG>/scripts/full-script.md
    - videos/<SLUG>/script.txt
    - videos/<SLUG>/audio/narration.wav
    - videos/<SLUG>/transcript.json
    - videos/<SLUG>/retention-strategy.md

  Follow the playbook's Branch A path (pipeline output present):
    - DO NOT invent a script — use full-script.md verbatim
    - Map scenes to the template's phase archetypes per plan.md
    - Apply retention components from retention-strategy.md
    - Wire SFX cues automatically (sync-video-sfx.sh)
    - Edit videos/<SLUG>/index.html
    - Run `npx hyperframes lint videos/<SLUG>` — must end with 0 errors
    - Run `npx hyperframes inspect videos/<SLUG>` — must end with 0 overflow
    - **MANDATORY render-blocker check** (per `.claude/rules/hyperframes-pitfalls.md` §8):
      After lint + inspect pass, grep for `font-family:\s*var\(--(sans|mono)` across
      the video's index.html + compositions/*.html. If ANY matches found, apply the
      sed fix from pitfalls §8 to replace each `var(--sans|--mono)` with its literal
      font name BEFORE returning. This pattern is inherited from most templates and
      blocks render even though lint passes.

  When done, return <300-word summary: scene count built, phase data_start/data_duration
  values, retention components installed (block + component names), SFX cues wired,
  lint result (errors / warnings counts), inspect result, **font-var grep result
  (must be empty after fix)**, any issues encountered.
  Do NOT run `npx hyperframes preview` — the orchestrator handles that.
```

Wait for return. Append summary to `videos/<SLUG>/orchestration-log.md`. If the build returned lint errors, surface them verbatim and STOP — do not paper over real validation failures.

---

## Phase YT — YouTube description (MANDATORY — never skip)

After Phase 4 (composition build) lints clean, generate the paste-ready YouTube metadata file. Every video MUST end the pipeline with `videos/<SLUG>/youtube-description.md` on disk — shipping without it is a defect.

Dispatch as an isolated sub-agent so the orchestrator context stays small:

```
Task(
  description: "Phase YT description for <SLUG>",
  subagent_type: "general-purpose",
  prompt: """
  Generate videos/<SLUG>/youtube-description.md per .claude/rules/youtube-metadata.md.

  Required sequence:
  1. vidIQ keyword research — call mcp__claude_ai_vidiq__vidiq_keyword_research, vidiq_outliers, and vidiq_trending_videos for 3-5 topic seeds drawn from the script + plan. Save the snapshot to videos/<SLUG>/research/vidiq-keywords.md.
  2. Read videos/<SLUG>/index.html and extract each phase wrapper's data-start. Long-form ONLY: compute chapter timestamps (M:SS). If a speed_factor applies (see .claude/rules/video-speedup.md), divide by it. Shorts: SKIP chapters entirely (the rule forbids them on vertical Shorts).
  3. Write videos/<SLUG>/youtube-description.md in this exact LEAN order — do NOT add Key Changes / Key Concepts / Key Stats / Key Facts / About This Video / "What's in this short" bullets (these are explicitly cut from the template):
     - SEO hook paragraph (keyword-front-loaded — top 2-3 keywords in first 200 chars; if the video has a feature inventory, pack the top 3-5 into this paragraph as a comma-separated list)
     - Dynamous CTA block in `----` separators (MANDATORY on every video — independent of the `dynamousPromotion` flag in `meta.json`; that flag gates ON-SCREEN Dynamous promotion only):
       ```
       ----
       🚀 Want to learn agentic coding with live daily events and workshops?
       Check out Dynamous AI: https://dynamous.ai/?code=646a60
       Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
       ----
       ```
     - Chapters — LONG-FORM ONLY (omit entirely on Shorts)
     - Resources: (every URL validated via WebFetch, keyword-rich anchor text)
     - Hostinger affiliate block in `----` separators (MANDATORY on every video — Shorts AND long-form):
       ```
       ----
       ⚡ Host your portfolio, side projects, n8n flows, or AI agents on Hostinger (10% OFF):
       Get 10% off here 👉 https://hostinger.com/DIYSMARTCODE
       ----
       ```
     - Engagement debate question (must match script's final spoken CTA line)
     - 15-25 hashtags (mix specific + broad)
  4. Validate every URL with WebFetch. Replace 404s; drop unfixable links.
  5. The description should be SHORT and lean — if it runs longer than ~1500 chars for Shorts or ~3000 chars for long-form, you've over-padded. Trim.

  When done, update videos/<SLUG>/phase-status.md row "YT - YouTube description" to "done <date>".
  """
)
```

Wait for return. Append the <200-word summary to `orchestration-log.md`. Confirm phase-status row updated. Proceed to Phase R.

---

## Phase R — Review (MANDATORY — gate before preview)

After Phase YT finishes, run the comprehensive video-production review. This is the final quality gate: 5 specialized agents in parallel covering timing/pacing, render blockers, layout/typography, script/content, and YouTube metadata. Catches every defect the linter doesn't catch — visual-pacing gaps > 5s, SFX-to-visual drift, font-family render blocker, sub-comp ID mismatches, Shorts typography violations, first/last frame not thumbnail-grade, heteronym risks, engagement CTA cross-surface mismatch, chapter timestamps not adjusted for speedup, and 30+ more.

Dispatch the `video-review` skill in `pre-publish` mode with `--fix safe` (apply mechanical fixes automatically, surface anything risky to the user):

```
Skill(skill: "video-review", args: "<SLUG> --mode pre-publish --fix safe")
```

The skill orchestrator:
1. Validates the composition exists at `videos/<SLUG>/index.html`.
2. Dispatches 5 review agents in parallel:
   - `video-timing-pacer` — timing, pacing, SFX drift, composition duration vs narration
   - `video-render-validator` — lint/validate/inspect + font-var blocker + sub-comp wiring
   - `video-layout-typography` — Shorts typography + first/last frame thumbnail-grade
   - `video-script-content` — heteronyms + engagement CTA in 3 places + source-grounded fact check
   - `video-metadata-publish` — youtube-description.md structure + chapter timestamps post-speedup + URL validation
3. Aggregates findings by severity (BLOCKER / HIGH / MEDIUM / LOW), applies safe auto-fixes, and saves the report to `videos/<SLUG>/qa/review-report.json` + prints a Markdown summary.

**Gate condition (BLOCKING):**
- Verdict `FAIL_BLOCKER` → STOP orchestration. Surface every BLOCKER finding verbatim and recommend specific fixes. The pipeline is NOT done — the user must address blockers and re-run `/video-review <SLUG>` (or fix + re-run full-auto with `--resume`).
- Verdict `FAIL_HIGH` → proceed to Step Z (preview) but surface every HIGH finding in the final completion box. The composition is render-able but not publish-ready.
- Verdict `WARN_MEDIUM`, `PASS_LOW`, or `PASS` → proceed normally; surface MEDIUM findings as advisory.

Append the <200-word summary to `orchestration-log.md`. Add a row to `videos/<SLUG>/phase-status.md` titled `R - Review` with status `done <date>` and the verdict (`PASS`, `WARN_MEDIUM`, `FAIL_HIGH`, `FAIL_BLOCKER`).

## Step Z — Preview

If lint + inspect both passed, fire `npx hyperframes preview videos/<SLUG>` in the background and print the studio URL so the user can review the composition.

```bash
npx hyperframes preview videos/<SLUG> &
```

Print a final completion box:

```
═══════════════════════════════════════════════════════════════
PIPELINE COMPLETE — <SLUG>
═══════════════════════════════════════════════════════════════

All phases done. Composition is previewable at the URL printed by
`npx hyperframes preview` (usually http://localhost:5173).

Artifacts under videos/<SLUG>/:
  research/content-brief.md
  research/vidiq-keywords.md       ← vidIQ snapshot (Phase YT)
  plan.md
  scripts/full-script.md
  scripts/critique-report.md
  scripts/scene-NN-*.txt
  scripts/fact-check-report.md
  script.txt
  audio/narration.wav
  transcript.json
  retention-strategy.md
  index.html                       ← composition
  youtube-description.md           ← paste-ready YouTube metadata (Phase YT)
  qa/review-report.json            ← video-review findings + verdict (Phase R)
  phase-status.md
  orchestration-log.md

Next step (user-triggered):
  npx hyperframes render videos/<SLUG> -o videos/<SLUG>/out/<SLUG>.mp4
═══════════════════════════════════════════════════════════════
```

End orchestrator's run.

</orchestration>

<failure-modes>

## What to do when something goes wrong

| Symptom                                   | Action                                                                                       |
| ----------------------------------------- | -------------------------------------------------------------------------------------------- |
| Phase 0 vidiq enrichment errors           | Ignore — vidiq is OPTIONAL. Phase 0 should silently skip and continue.                       |
| Phase 1 reports missing `/hyperframes` skill | Phase 1 falls back to documenting the prerequisite. Continue.                              |
| Phase 2.5 blocks                          | STOP. Print critique-report.md gate failures. User edits full-script.md, then `--resume`.    |
| Phase 2b blocks (major correction)        | STOP. Print fact-check-report.md failures. User fixes, then `--resume`.                      |
| Phase 2b auto-corrects (minor)            | Phase 2b automatically re-flattens script.txt. Log and continue.                             |
| `transcript.json` missing in --resume     | STOP. Print the two CLI commands. Wait for user to retry `--resume`.                         |
| Phase 3.5 reports invented component name | STOP. The agent invented a name not in retention-components-hyperframes.md. User must edit.  |
| Orchestrator itself crashes               | Re-invoke with same args; phase-status.md drives recovery.                                   |

</failure-modes>

<output>

End-of-run report (after PAUSE 1 or PAUSE 2):

```markdown
## Pipeline Run Summary

**Slug**: <SLUG>
**Mode**: <new pipeline | resume>
**Phases completed this run**: <list>

**Phase status snapshot** (from phase-status.md):
<table>

**Orchestration log**: videos/<SLUG>/orchestration-log.md

**Next action**: <copy of the PAUSE box content>
```

Do NOT include full phase artifacts in the report — they're on disk under `videos/<SLUG>/`.
</output>
