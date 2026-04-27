---
description: "Full pipeline orchestrator: research → plan → script → critique → TTS-script → fact-check → (TTS handoff) → retention → (composition handoff)"
argument-hint: <topic | URL | brief.md> [--resume <slug>]
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebSearch, WebFetch
---

<objective>
Orchestrate the HyperFrames pipeline: phases 0 → 1 → 2 → 2.5 → 2a → 2b, then PAUSE for the user to run `npx hyperframes tts` + `npx hyperframes transcribe`, then resume with phase 3.5, then PAUSE again at the composition-build handoff.

**Goal**: Go from "I have an idea" to "researched, fact-checked, retention-engineered script + per-scene retention strategy" with two explicit human-handoff pauses (TTS, composition build).

**Output**: Every artifact under `videos/<slug>/`. No auto-render, no auto-TTS, no auto-composition build.

**Critical**: This orchestrator stops twice (after Phase 2b for TTS handoff, after Phase 3.5 for composition handoff). Both stops are deliberate — the side effects (ElevenLabs credit spend, creative composition decisions) need human review.

**This pipeline does NOT include**:
- Phase 3 (audio generation) — handled by `npx hyperframes tts`
- Phase 4 (composition build) — handled by `/diy-yt-creator:new-anthropic-short` (or other template skill)
- Phase 5 (render) — handled by `npx hyperframes render`
- YouTube description / upload — out of scope here
</objective>

<initial-setup>

## Step 1 — Detect mode

Parse `$ARGUMENTS`:

| Argument pattern                  | Mode      | Action                                                                  |
| --------------------------------- | --------- | ----------------------------------------------------------------------- |
| `--resume <slug>`                 | RESUME    | Skip phases 0-2b, jump to Phase 3.5 (assumes TTS + transcribe finished) |
| `<topic-text>`                    | FREE-FORM | New pipeline. Derive slug from topic.                                   |
| `<*.md>` containing `**Topic**:`  | BRIEF     | Parse the brief (per `brief-template.md`); use its `Slug` if present    |
| `<URL>`                           | URL       | New pipeline. Derive slug from URL/page title.                          |

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
  duration: "<from brief or default based on template — shorts/anthropic: 45s>"
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

| Phase           | Status  | Completed |
| --------------- | ------- | --------- |
| 0 - Research    | pending |           |
| 1 - Plan        | pending |           |
| 2 - Script      | pending |           |
| 2.5 - Critique  | pending |           |
| 2a - TTS Script | pending |           |
| 2b - Fact Check | pending |           |
| 3.5 - Retention | pending |           |

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
- If `done`: log summary, proceed to TTS handoff pause.
- If `blocked`: STOP orchestration. Surface failures + corrections needed verbatim. Tell user to fix and re-run `/diy-yt-creator:full-auto --resume <SLUG>`.

---

## PAUSE 1 — TTS Handoff

After Phase 2b passes, STOP orchestration and print to user:

```
═══════════════════════════════════════════════════════════════
PIPELINE PAUSED — TTS HANDOFF (1 of 2)
═══════════════════════════════════════════════════════════════

Phases 0 through 2b are complete. videos/<SLUG>/ now contains:
  - research/content-brief.md
  - plan.md
  - scripts/full-script.md
  - scripts/critique-report.md
  - scripts/scene-NN-*.txt
  - script.txt                  (flat — for hyperframes tts)
  - scripts/fact-check-report.md
  - phase-status.md

Next steps (run these manually — they spend ElevenLabs credit):

  npx hyperframes tts videos/<SLUG>
  npx hyperframes transcribe videos/<SLUG>

After both succeed, resume the pipeline:

  /diy-yt-creator:full-auto --resume <SLUG>

The resume run will execute Phase 3.5 (per-scene retention strategy) using
videos/<SLUG>/transcript.json as input.

Why we pause here: TTS spending and voice/speed/quality are decisions worth
reviewing before committing the rest of the pipeline. The pipeline is also
recoverable from this exact state via --resume, so no work is lost if you
need to step away.
═══════════════════════════════════════════════════════════════
```

End the orchestrator's run. Do NOT proceed.

---

## (RESUME mode) Phase 3.5 — Retention Strategy

**Only runs in RESUME mode**, after the user has executed TTS + transcribe.

Verify `videos/<SLUG>/transcript.json` exists. If missing, STOP and remind the user to run `npx hyperframes tts videos/<SLUG> && npx hyperframes transcribe videos/<SLUG>`.

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

Wait, log, proceed to composition handoff pause.

---

## PAUSE 2 — Composition Build Handoff

After Phase 3.5 completes, STOP orchestration and print to user:

```
═══════════════════════════════════════════════════════════════
PIPELINE PAUSED — COMPOSITION BUILD HANDOFF (2 of 2)
═══════════════════════════════════════════════════════════════

Phase 3.5 is complete. videos/<SLUG>/retention-strategy.md is ready.

The PIPELINE is now COMPLETE. Pipeline artifacts:
  - research/content-brief.md
  - plan.md
  - scripts/full-script.md
  - scripts/critique-report.md
  - scripts/scene-NN-*.txt
  - scripts/fact-check-report.md
  - script.txt
  - audio/narration.wav
  - transcript.json
  - retention-strategy.md
  - phase-status.md

Next: hand off to the composition build skill, which reads plan.md +
retention-strategy.md as authoritative inputs:

  /diy-yt-creator:new-anthropic-short <SLUG>

That skill (per its updated step 4 Branch A) will:
  - Detect that scripts/full-script.md exists → use it instead of inventing a script
  - Map scenes to the template's phase archetypes per plan.md
  - Apply the retention components from retention-strategy.md
  - Edit videos/<SLUG>/index.html
  - Lint, inspect, preview

Why we pause here: composition build is creative work (logo selection, accent
rotation, phase timing) that benefits from human-in-the-loop judgment.
Auto-building would produce a generic output. SFX wiring **is** automated —
new-anthropic-short reads retention-strategy.md sfx_cues, runs
sync-video-sfx.sh, and inserts the <audio> elements per
.claude/rules/audio-design.md.
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
