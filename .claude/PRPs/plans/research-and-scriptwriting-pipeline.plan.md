# Feature: Bring Phases 0–3.5 (Research → Script → Critique → TTS → Fact-Check → Retention) into the HyperFrames Project

## Summary

The companion project `diy-yt-creator` (Remotion-based) has a mature multi-phase content pipeline that takes a topic from "I have an idea" to "fact-checked, retention-engineered, TTS-optimized script with a per-scene retention strategy." This project (`diy-yt-creator-hyperframes`) currently has **none** of that — its only video-creation skill (`diy-yt-creator/new-anthropic-short.md`) jumps from a topic prompt straight to filling a 4-phase HTML composition, with no research, no fact-check, no critique gate, no retention design.

We are NOT copying the source phase files verbatim. We are extracting the **content-layer logic** of phases 0, 2, 2.5, 2a, 2b, 3.5 (which are renderer-agnostic), **rewriting** phase 1 (which is heavily Remotion-coupled) into a HyperFrames-native composition planner, and **wiring** the existing Anthropic-Shorts skill to invoke the pipeline end-to-end. We are also **optimizing**: dropping Remotion-specific inputs (`timing.ts`, 30fps frame conversion, `sceneNN-sync.json`), using HyperFrames' own `transcribe` JSON output, and layering in the `vidiq` MCP tools (available globally but currently unwired) to make Phase 0 stronger than the source.

## User Story

As a video creator using this HyperFrames repo
I want to invoke a single pipeline that takes a topic, researches it, drafts a retention-engineered + fact-checked script, and prepares a per-scene retention strategy
So that I can stop hand-writing scripts from scratch and stop trusting my own first draft, while keeping every artifact under `videos/<slug>/` so the existing HyperFrames composition + render workflow picks up cleanly from there.

## Problem Statement

The current pipeline assumes the user arrives with a finished idea and (implicitly) finished facts. There is no slash command, no skill, and no playbook in the repo that does:

- Topic research (web search, vidiq keyword research, competitor angles, proof points, hooks)
- Script drafting beyond a thin 4-bullet template fill
- Hook variant generation + scoring
- Fact-checking against live web sources
- Script-quality scoring (hook, retention curve, banned-phrase detection)
- Per-scene retention strategy design

This means every video either (a) gets a hand-written script of unknown quality, (b) requires the user to manually run a separate `diy-yt-creator` Remotion project for the research and copy the script over, or (c) skips the research/critique steps entirely. The vidiq MCP tools available in the agent session are completely unused. The result is wasted time and weaker videos.

## Solution Statement

Introduce a `.claude/commands/diy-yt-creator/` namespace containing seven first-class slash commands (`/diy-yt-creator:phase0-research` through `/diy-yt-creator:phase3-5-retention`) plus a `/diy-yt-creator:full-auto` orchestrator. Each phase reads/writes artifacts inside the existing `videos/<slug>/` workspace (not a separate `src/` tree), uses the existing `phase-status.md` state-file pattern from the source, and dispatches to `general-purpose` sub-agents for context isolation. Phase 1 is rewritten as a HyperFrames-native composition planner that picks a template, plans sub-compositions, and budgets `data-start`/`data-duration` — replacing the source's Remotion-bits component selection. Phase 0 is augmented with optional vidiq MCP enrichment. Reference docs (`story-locks.md`, `faceless-tech-scriptwriting-playbook.md`, plus a new `retention-components-hyperframes.md`) live in `.claude/references/`. The existing `new-anthropic-short.md` skill playbook is updated to optionally call the full pipeline before the composition-build step.

## Metadata

| Field            | Value                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Type             | NEW_CAPABILITY                                                                                     |
| Complexity       | HIGH                                                                                               |
| Systems Affected | `.claude/commands/`, `.claude/references/`, `.claude/skills/diy-yt-creator/`, `videos/<slug>/`     |
| Dependencies     | hyperframes CLI (existing), elevenlabs `text-to-speech` skill (existing), vidiq MCP (optional)     |
| Estimated Tasks  | 14                                                                                                 |

---

## UX Design

### Before State

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          CURRENT (Today)                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  User says: "make a short about Claude Connectors"                           │
│       │                                                                      │
│       ▼                                                                      │
│  ┌─────────────────────────────────────┐                                     │
│  │  /diy-yt-creator:new-anthropic-     │                                     │
│  │  short  (single skill playbook)     │                                     │
│  └─────────────────────────────────────┘                                     │
│       │                                                                      │
│       ▼                                                                      │
│  Step 4: "Draft the script" — agent writes ~130-word narration               │
│  directly from topic, mapped to 4 fixed phases (Hero/Stat/Timeline/CTA)      │
│                                                                              │
│   ✗ No research      ✗ No hook variants      ✗ No fact-check                 │
│   ✗ No critique gate ✗ No retention design   ✗ vidiq tools unused            │
│                                                                              │
│       ▼                                                                      │
│  TTS → transcribe → fill HTML → lint → preview → DONE                        │
│                                                                              │
│  RESULT: script quality depends entirely on whatever the agent invents       │
│          on the spot. Stats either fabricated, omitted, or hand-fed.         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### After State

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          NEW (Pipeline)                                      │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  User says: "make a short about Claude Connectors"                           │
│       │                                                                      │
│       ▼                                                                      │
│  ┌──────────────────────────────────────┐                                    │
│  │ /diy-yt-creator:full-auto <topic>    │  (or invoke phases individually)   │
│  └──────────────────────────────────────┘                                    │
│       │                                                                      │
│       ▼  (each phase = isolated sub-agent, writes to disk, summary returns)  │
│                                                                              │
│  Phase 0 — Research (vidiq + web + 4 parallel sub-agents)                    │
│       └─→ videos/<slug>/research/content-brief.md                            │
│       ▼                                                                      │
│  Phase 1 — Plan (HyperFrames-native composition planner)                     │
│       └─→ videos/<slug>/plan.md  (scene list, hook variants, sub-comp        │
│                                   layout, GSAP/audio-reactive picks,         │
│                                   data-start/data-duration budget)           │
│       ▼                                                                      │
│  Phase 2 — Script  (full-script.md, plain narration)                         │
│       ▼                                                                      │
│  Phase 2.5 — Critique  (BLOCKING gate: hook ≥7, arc ≥7, 0 banned phrases)    │
│       ▼                                                                      │
│  Phase 2a — TTS Optimization  (per-scene .txt + flattened script.txt)        │
│       ▼                                                                      │
│  Phase 2b — Fact-Check  (BLOCKING gate: 0 Tier-1 unverified claims)          │
│       ▼                                                                      │
│  ── existing pipeline takes over here ──                                     │
│  npx hyperframes tts → transcribe → produces transcript.json                 │
│       ▼                                                                      │
│  Phase 3.5 — Retention Strategy (per-scene HyperFrames effect picks)         │
│       └─→ videos/<slug>/retention-strategy.md                                │
│       ▼                                                                      │
│  new-anthropic-short.md picks up at "edit index.html" step,                  │
│  using plan.md + retention-strategy.md as authoritative inputs               │
│       ▼                                                                      │
│  lint → inspect → preview → DONE                                             │
│                                                                              │
│  RESULT: every script is researched, hook-tested, fact-checked, and          │
│          arrives at the composition step with explicit per-scene             │
│          animation guidance instead of blank-page improvisation.             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Interaction Changes

| Location                                         | Before                                  | After                                                          | User Impact                                                                       |
| ------------------------------------------------ | --------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Slash command surface                            | None under `diy-yt-creator/`            | 7 phase commands + `full-auto` orchestrator                    | Can run any single phase, resume from any point, debug failures in isolation      |
| `videos/<slug>/`                                 | `meta.json` + `script.txt` + HTML       | + `research/`, `plan.md`, `scripts/`, `phase-status.md`, `retention-strategy.md` | Every artifact co-located with the video; PR diff tells the whole production story |
| `new-anthropic-short.md` step 4 ("draft script") | Agent invents script from topic         | Reads `videos/<slug>/scripts/full-script.md` (Phase 2 output)  | Composition build no longer guesses content                                       |
| Reference docs                                   | None                                    | `.claude/references/{story-locks,scriptwriting-playbook,retention-components-hyperframes}.md` | Banned-phrase list, hook taxonomy, retention component picks all version-controlled |
| vidiq MCP tools                                  | Available but unused                    | Optional Phase 0 enrichment                                    | Keyword research, competitor titles, trending angles fold into `content-brief.md` |

---

## Mandatory Reading

**The implementation agent MUST read these files before starting any task. Do not improvise — read and quote.**

| Priority | File                                                                                                                              | Lines | Why Read This                                                                                                                          |
| -------- | --------------------------------------------------------------------------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------- |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase0-research.md`                            | all   | Source of truth for Phase 0. ADAPT, do not copy verbatim — see "Patterns to Mirror" for what changes.                                  |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase1-plan.md`                                | all   | Source for Phase 1. ~50% of this file is Remotion-specific and gets REPLACED — see Task 4 for the substitution rules.                  |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase2-script.md`                              | all   | Source for Phase 2. Renderer-agnostic — port nearly verbatim, only path conventions change.                                            |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase2-5-critique.md`                          | all   | Source for Phase 2.5. Renderer-agnostic — keep all four passes, just update reference paths.                                           |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase2a-script.md`                             | all   | Source for Phase 2a. Note: source `elevenlabs-tts-optimizer` skill becomes the existing `text-to-speech` skill in this repo.           |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase2b-factcheck.md`                          | all   | Source for Phase 2b. Renderer-agnostic — port verbatim minus path changes.                                                             |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\phase3-5-retention.md`                         | all   | Source for Phase 3.5. Inputs change (`transcript.json` instead of `sceneNN-sync.json` + `timing.ts`). Sub-agent type changes.          |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\full-auto-v2.md`                               | all   | Source for the orchestrator. v2 (sub-agent isolation) is the model — NOT v1 (inline). Adapt to HyperFrames phase set (no Phase 3/4/5). |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\diy-yt-creation\brief-template.md`                             | all   | Input format for both Phase 0 and the orchestrator. Port to new home.                                                                  |
| P1       | `.claude/skills/diy-yt-creator/SKILL.md`                                                                                          | all   | Existing skill that the new commands plug into. Update its "Available commands" table.                                                 |
| P1       | `.claude/skills/diy-yt-creator/new-anthropic-short.md`                                                                            | all   | Step 4 ("draft script") needs replacement — script comes from pipeline now, not invented inline.                                       |
| P1       | `templates/shorts/anthropic/README.md`                                                                                            | all   | Phase 1 must understand which template's structure it's planning into. The 4-phase Hero/Stat/Timeline/CTA is the constraint for shorts.|
| P1       | `templates/shorts/anthropic/DESIGN.md`                                                                                            | all   | Source of design tokens, motion rules, anti-patterns — Phase 1 cites these in the plan.                                                |
| P1       | `CLAUDE.md`                                                                                                                       | all   | Repo conventions — multi-video layout, lint-after-changes rule, deterministic-only logic, `data-*` semantics.                          |
| P1       | `videos/claude-connectors-everyday-life/script.txt`                                                                               | all   | Reference example of the existing `script.txt` flat-prose convention. Phase 2a must produce something this format-compatible.          |
| P1       | `videos/claude-connectors-everyday-life/meta.json`                                                                                | all   | Reference shape: `{id, name, createdAt}`. The pipeline must not break this contract.                                                   |
| P2       | `.agents/skills/hyperframes/SKILL.md` and `.agents/skills/hyperframes/references/audio-reactive.md`, `captions.md`, `transitions.md` | all   | Phase 1 + Phase 3.5 cite these for HyperFrames-native effect picks. Read so the new docs reference real capability names.              |
| P2       | `.agents/skills/gsap/SKILL.md`, `.agents/skills/gsap/references/effects.md`                                                       | all   | Same — Phase 1's animation strategy section enumerates real GSAP patterns available.                                                   |
| P2       | `.claude/settings.json`                                                                                                           | all   | Existing PostToolUse hook on Write/Edit/Bash runs `scripts/sync-shared-assets.sh` — the new commands must not regress this.            |

**External Documentation** (use minimally — most of what's needed is in the source phase files above):

| Source                                                                          | Section            | Why Needed                                                                              |
| ------------------------------------------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------- |
| Claude Code slash-command frontmatter docs (https://docs.claude.com/en/docs/claude-code/slash-commands) | YAML frontmatter   | Confirm `description`, `allowed-tools`, `argument-hint` field syntax for `.md` commands |
| Claude Code Task tool / sub-agent docs                                          | `subagent_type`    | Confirm `general-purpose` is the right fallback for project-unregistered agent types    |

---

## Patterns to Mirror

### NAMING_CONVENTION (slash command files)

```markdown
<!-- SOURCE: C:\...\diy-yt-creator\.claude\commands\diy-yt-creation\phase0-research.md:1-30 -->
<!-- COPY THIS FRONTMATTER PATTERN: -->
---
description: <one-line action description used as the slash-command tooltip>
argument-hint: <topic | URL | brief.md>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebSearch, WebFetch
---

# Phase X — <Name>

**Argument**: `$ARGUMENTS` — <what it expects>

**Goal**: <one-paragraph statement of what this phase accomplishes>

## Prerequisites
...

## Output
...

## Steps
...
```

### STATE_FILE (`phase-status.md`)

```markdown
<!-- SOURCE: phase0-research.md:749-768 (write rules) and full-auto-v2.md:99-100 (read rules) -->
<!-- COPY THIS PATTERN — file lives at videos/<slug>/phase-status.md -->

# Phase Status — <slug>

| Phase | Status | Completed |
|---|---|---|
| 0 - Research | done | 2026-04-27 |
| 1 - Plan | done | 2026-04-27 |
| 2 - Script | done | 2026-04-27 |
| 2.5 - Critique | done (8.2/10 hook, 7.5/10 arc) | 2026-04-27 |
| 2a - TTS Script | done | 2026-04-27 |
| 2b - Fact Check | done (12/12 claims verified) | 2026-04-27 |
| 3.5 - Retention | pending | — |

**Status vocabulary:** `pending` | `in-progress` | `done` | `done <details>` | `blocked (<reason>)`
```

### SUB_AGENT_DISPATCH (orchestrator pattern)

```markdown
<!-- SOURCE: full-auto-v2.md:106-117 (context-isolation mandate) and 341-347 (parallel dispatch) -->
<!-- COPY THIS PATTERN — every phase command runs as an isolated sub-agent: -->

Use the Task tool with:
  - subagent_type: "general-purpose"
  - description: "Phase X — <name> for <slug>"
  - prompt: |
      Run Phase X for video slug `<slug>`. Read inputs from disk:
        - <input file 1>
        - <input file 2>
      Produce outputs to disk:
        - <output file 1>
      When done, update videos/<slug>/phase-status.md row "X - <Name>" to "done <date>".
      Return ONLY a <200-word summary. Do not return file contents.

Wait for the sub-agent to complete. Read ONLY videos/<slug>/phase-status.md and the
specific summary section from the produced artifact (e.g., critique-report.md "Verdict"
section, fact-check-report.md "Summary" section). Do NOT re-read full artifacts.
```

### QUALITY_GATE (blocking pattern)

```markdown
<!-- SOURCE: phase2-5-critique.md:12-14 and phase2b-factcheck.md:289-294 -->
<!-- COPY THIS PATTERN for any phase that gates downstream phases: -->

## Gate Decision

If any of the following are true, set phase-status.md row to `blocked (<reason>)` and STOP:
  - <gate condition 1>
  - <gate condition 2>

Hard stop in autonomous mode too — major issues block regardless of mode (per source
phase2b-factcheck.md:267-279). Minor auto-corrections (rounding, date refresh, URL swap)
may be applied inline and logged.
```

### EXISTING_REPO_PATTERNS (must not violate)

```bash
# SOURCE: CLAUDE.md "Linting — ALWAYS RUN AFTER CHANGES"
# COPY THIS DISCIPLINE — every command that edits files under videos/<slug>/ ends with:
npx hyperframes lint videos/<slug>
# Fix all errors before declaring success. Phase commands that don't touch HTML
# (0, 1, 2, 2.5, 2a, 2b, 3.5) skip lint, but phase commands that touch index.html
# (none in this batch — that's still in new-anthropic-short.md) MUST run it.
```

```html
<!-- SOURCE: CLAUDE.md "Key Rules" 1-6 -->
<!-- COPY THIS DISCIPLINE for any HTML written/suggested by Phase 1: -->
<!-- - Every timed element needs data-start, data-duration, data-track-index -->
<!-- - Elements with timing MUST have class="clip" -->
<!-- - Timelines paused and registered on window.__timelines -->
<!-- - Videos use muted with separate <audio> for audio track -->
<!-- - Sub-compositions via data-composition-src="compositions/file.html" -->
<!-- - Only deterministic logic — no Date.now(), no Math.random(), no fetch -->
```

---

## Files to Change

| File                                                                               | Action  | Justification                                                                                                            |
| ---------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| `.claude/commands/diy-yt-creator/phase0-research.md`                               | CREATE  | Phase 0 entry point. Adapted from source. Adds optional vidiq enrichment.                                                |
| `.claude/commands/diy-yt-creator/phase1-plan.md`                                   | CREATE  | Phase 1 entry point. **Major rewrite** — HyperFrames-native composition planner replaces Remotion-bits selection.        |
| `.claude/commands/diy-yt-creator/phase2-script.md`                                 | CREATE  | Phase 2 entry point. Near-verbatim port (paths only).                                                                    |
| `.claude/commands/diy-yt-creator/phase2-5-critique.md`                             | CREATE  | Phase 2.5 entry point. Verbatim port (paths only).                                                                       |
| `.claude/commands/diy-yt-creator/phase2a-tts-script.md`                            | CREATE  | Phase 2a entry point. Skill reference: `text-to-speech` instead of `elevenlabs-tts-optimizer`. Also writes flat `script.txt`. |
| `.claude/commands/diy-yt-creator/phase2b-factcheck.md`                             | CREATE  | Phase 2b entry point. Verbatim port (paths only). Perplexity script optional and skipped if absent.                      |
| `.claude/commands/diy-yt-creator/phase3-5-retention.md`                            | CREATE  | Phase 3.5 entry point. **Inputs rewritten** — uses HyperFrames `transcript.json` instead of Remotion `sceneNN-sync.json`. |
| `.claude/commands/diy-yt-creator/full-auto.md`                                     | CREATE  | Orchestrator. Modeled on source `full-auto-v2.md` but only chains phases 0–2b + 3.5 (Phase 3/4/5 are HyperFrames-native).|
| `.claude/commands/diy-yt-creator/brief-template.md`                                | CREATE  | Structured brief input format. Port verbatim, drop `Resolution` field (HyperFrames is template-driven).                   |
| `.claude/references/story-locks.md`                                                | CREATE  | Loop-opener taxonomy referenced by Phase 2 + Phase 2.5. Port from source `.claude/references/story-locks.md`.             |
| `.claude/references/faceless-tech-scriptwriting-playbook.md`                       | CREATE  | Banned-phrases list + voice rules referenced by Phase 2 + Phase 2.5. Port from source `.claude/research/`.                |
| `.claude/references/retention-components-hyperframes.md`                           | CREATE  | NEW — maps retention concepts to HyperFrames/GSAP capabilities (replaces source's `remotion-bits` taxonomy).             |
| `.claude/skills/diy-yt-creator/SKILL.md`                                           | UPDATE  | Add the new commands to the "Available commands" table. Add a "When to use the full pipeline vs new-anthropic-short" note.|
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                             | UPDATE  | Step 4 ("Draft the script") changes from "invent" to "read `videos/<slug>/scripts/full-script.md` and adapt to phases".  |

**No changes needed** to:
- `templates/shorts/anthropic/*` (template stays content-free; pipeline writes into `videos/<slug>/` after copy)
- `videos/claude-connectors-everyday-life/*` (existing video unaffected; pipeline is opt-in)
- `scripts/sync-shared-assets.sh` and the `.claude/settings.json` hook (untouched; phase commands write only inside `.claude/` and `videos/`, hook still fires correctly)
- `skills-lock.json`, `.env`, `shared/`, root `README.md`/`CLAUDE.md`/`AGENTS.md`

---

## NOT Building (Scope Limits)

These are explicit exclusions. Don't drift into them, even if a follow-up feels natural:

- **Phase 3 (audio generation), Phase 4 (composition build), Phase 5 (render)**. These already exist in this project as `npx hyperframes tts`, `new-anthropic-short.md` step 8 (HTML edit), and `npx hyperframes render`. Do not re-implement them, do not wrap them, do not call them from the new commands. The pipeline ends at Phase 3.5 and hands off to the existing skill.
- **Phase 3.6 (Scene Design Director), Phase 4b (Visual QA), Phase 4c (Plan Fidelity)** from the source. These are Remotion-coupled tooling that has no equivalent here yet. If retention strategy needs a downstream "scene design" step in HyperFrames later, it's a separate plan.
- **Phase 6/7 (YouTube description, upload)** from the source. Out of scope; this repo currently has no upload story.
- **`retention-strategy-agent` and `diy-phase-runner` project-registered agent types** from the source. We use `general-purpose` with self-contained prompts. Registering project-specific agent types is a separate refactor.
- **Long-form template support**. The Anthropic Shorts template is the only one that exists. Phase 1's template-aware planning has a single branch today; the long-form branch is left as a stubbed `TODO` comment, not implemented.
- **Auto-rendering**. Even after Phase 3.5 succeeds, the pipeline does NOT call `npx hyperframes render`. The `new-anthropic-short.md` rule "Never auto-render" is preserved.
- **vidiq as a hard dependency**. vidiq enrichment is OPTIONAL — Phase 0 detects whether `mcp__claude_ai_vidiq__*` tools are available and either uses them or falls back to web search only. Failure to call vidiq is not a phase failure.
- **Backfilling the existing video** (`videos/claude-connectors-everyday-life/`) with research/critique/fact-check artifacts. The pipeline is forward-only; the existing video stays as-is.
- **Migrating away from `script.txt`**. The existing `npx hyperframes tts` reads `script.txt` (per `new-anthropic-short.md` step 5). Phase 2a writes BOTH `scripts/full-script.md` (rich) AND `script.txt` (flat) so the existing TTS pipeline keeps working without changes.

---

## Step-by-Step Tasks

Each task is atomic and can be validated immediately after completion.

### Task 1 — CREATE `.claude/references/story-locks.md`, `faceless-tech-scriptwriting-playbook.md`, `retention-components-hyperframes.md`

- **ACTION**: CREATE three reference docs.
- **IMPLEMENT**:
  - `story-locks.md` — port verbatim from source `C:\...\diy-yt-creator\.claude\references\story-locks.md` (read it; it defines Loop Openers, hook patterns, story-arc components used by Phase 2 + 2.5 scoring).
  - `faceless-tech-scriptwriting-playbook.md` — port verbatim from source `C:\...\diy-yt-creator\.claude\research\faceless-tech-scriptwriting-playbook.md` (banned-phrase list §11 referenced by Phase 2.5 QG-4; voice rules §1–10 referenced by Phase 2).
  - `retention-components-hyperframes.md` — NEW. Mirrors the *concept* of source's `remotion-bits` component taxonomy but enumerates HyperFrames/GSAP equivalents. Sections:
    - "Marker highlights" → references `.agents/skills/hyperframes/references/transitions/sketchout.md`, `circle.md`, `marker-sweep.md`
    - "Audio-reactive" → references `.agents/skills/hyperframes/references/audio-reactive.md`
    - "Caption styles" → references `.agents/skills/hyperframes/references/captions.md`
    - "Transitions" → references `.agents/skills/hyperframes/references/transitions.md`
    - "GSAP patterns" → references `.agents/skills/gsap/references/effects.md`
    - For each, give 2–3 concrete examples with the actual class/data attribute the HyperFrames framework expects.
- **MIRROR**: Frontmatter style of source reference docs (read those first to match).
- **GOTCHA**: The source `.claude/research/` and `.claude/references/` are TWO directories in the source. Consolidate into `.claude/references/` here for simplicity. Update all phase-command references accordingly.
- **VALIDATE**: `ls .claude/references/` shows three files. Skim each to confirm content actually populated, not stub.

### Task 2 — CREATE `.claude/commands/diy-yt-creator/brief-template.md`

- **ACTION**: CREATE structured brief format.
- **IMPLEMENT**: Port verbatim from source `phase-research/brief-template.md` with two changes:
  - REMOVE the `Resolution` field (HyperFrames resolution is template-driven via `hyperframes.json`, not user-selectable per video).
  - ADD a `Template` field with allowed values `shorts/anthropic` (currently only one). Note: `long-form/* — not yet implemented` as a placeholder line.
- **MIRROR**: Source brief-template.md format and section ordering.
- **GOTCHA**: The orchestrator and Phase 0 detect "structured brief" by the `**Topic**:` literal marker (per source). Preserve that marker exactly.
- **VALIDATE**: File exists; markdown lint passes (no broken headers).

### Task 3 — CREATE `.claude/commands/diy-yt-creator/phase0-research.md`

- **ACTION**: CREATE Phase 0 command. Adapt from source.
- **IMPLEMENT**:
  - Frontmatter: `description: Phase 0 — Topic research → content-brief.md`, `argument-hint: <topic | URL | brief.md>`, `allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebSearch, WebFetch`.
  - Output path: `videos/<slug>/research/content-brief.md` (NOT `src/<AnimationName>/research/`).
  - Output state: `videos/<slug>/phase-status.md` row `0 - Research` set to `done <date>`.
  - Slug derivation: kebab-case from topic (NOT PascalCase as in source). Example: "Claude Code Skills launch" → `claude-code-skills-launch`. Match the existing slug convention shown in `templates/shorts/anthropic/README.md`.
  - Sub-agent dispatch: 4 parallel `general-purpose` sub-agents (Agents A/B/C/D — Core, Competitive, Hook Architecture, Video Production), per source `phase0-research.md:88-89`. Update Agent D's prompt to drop the "Remotion (React-based) explainer video" phrase — replace with "HyperFrames (HTML + GSAP) composition".
  - Content brief schema: port the entire `<output>` block from source `phase0-research.md:500-737` verbatim. Renderer-agnostic.
  - Quality gates: port all 7 (QG-0A through QG-0G) per source `phase0-research.md:476-484`. Behavior on FAIL: flag prominently, proceed (autonomous mode rule).
  - Duration mapping: port the LIGHT/STANDARD/DEEP table per source `phase0-research.md:61-68`.
  - **NEW — vidiq enrichment** (this is the optimization, not a port): Add a Step 1.5 between Wave 1 and Wave 2:
    ```markdown
    ### Step 1.5 — Optional vidiq enrichment (NEW for HyperFrames)
    Probe for vidiq MCP tools by checking the available tool list for any starting with
    `mcp__claude_ai_vidiq__`. If present, run in parallel:
      - `mcp__claude_ai_vidiq__vidiq_keyword_research` for the topic
      - `mcp__claude_ai_vidiq__vidiq_trending_videos` in the relevant category
      - `mcp__claude_ai_vidiq__vidiq_score_title` on 2-3 candidate titles from Wave 1's hook research
    Fold results into the content brief under a new optional section "Keyword Research (vidiq)".
    If vidiq tools are unavailable, skip silently — this is an enrichment, not a gate.
    ```
- **MIRROR**: Source `phase0-research.md` overall structure (Steps 0/1/2, Wave 1 / Wave 2, sub-agent prompt templates A/B/C/D).
- **GOTCHA**: Source uses `model: "sonnet"` for sub-agents. Drop the model parameter — let the orchestrator use the parent model. Setting `sonnet` explicitly here would override Opus on this project.
- **VALIDATE**: `npx hyperframes docs` doesn't fail (proves the markdown isn't corrupt). Manual: invoke the command on a trivial topic, confirm `videos/<slug>/research/content-brief.md` is created with all required sections.

### Task 4 — CREATE `.claude/commands/diy-yt-creator/phase1-plan.md` (HyperFrames-native rewrite)

- **ACTION**: CREATE Phase 1 command. **Major rewrite** — DO NOT verbatim-copy.
- **IMPLEMENT**:
  - Frontmatter: `description: Phase 1 — Composition plan (HyperFrames-native)`, `argument-hint: <slug>`, `allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, Skill`.
  - Inputs: `videos/<slug>/research/content-brief.md` (required), `videos/<slug>/phase-status.md` row `0` must be `done`.
  - Output: `videos/<slug>/plan.md` (NOT `.agents/plans/`). All artifacts stay co-located with the video.
  - **KEEP** from source `phase1-plan.md`:
    - Duration → scene count table (`phase1-plan.md:57-62`)
    - Word-count → minimum display duration table B-10 (`phase1-plan.md:63-83`)
    - Kallaway Formula narrative arc
    - Hook variant generation (3 variants A/B/C with scoring) per `phase1-plan.md:543-545`
    - `cinematic_hook_blueprint:` section
    - `screenshots:` inventory section
    - `images:` AI image prompt section
    - `music_profile:` section (feeds Phase 3.2 in source — here it'd feed `npx hyperframes` SFX/music workflow if used)
    - Open-loop architecture YAML block
    - Fact-Check Gate C-08 rule (every claim cited)
  - **REPLACE** in source phase1-plan.md:
    | Source (Remotion)                                                                                          | Target (HyperFrames)                                                                                                                  |
    | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
    | Mandatory `remotion-best-practices` skill call (`phase1-plan.md:944`)                                      | Mandatory `hyperframes` + `gsap` skill calls — invoke both via Skill tool                                                              |
    | `src/shared/transitions/presets.ts` IDs                                                                    | HyperFrames transition list from `.agents/skills/hyperframes/references/transitions.md`                                               |
    | `src/shared/constants/hookSprings.ts` spring presets                                                       | GSAP spring/ease presets from `.agents/skills/gsap/references/effects.md`                                                              |
    | `remotion-bits` component table (`SyncedAnimatedText`, `SyncedCodeBlock`, `TypeWriter`, etc.) lines 826-838 | "Composition strategy" table — root composition + sub-compositions via `data-composition-src`. Reference `retention-components-hyperframes.md` for the picks |
    | Diagram components (`InfographicFlow`, `Timeline`, etc.) lines 361-374                                     | DROPPED — diagram components don't exist in HyperFrames. Phase 1 plans them as raw GSAP-driven HTML via `.claude/references/retention-components-hyperframes.md` |
    | `TransitionSeries` overlay syntax line 293                                                                 | HyperFrames sub-composition pattern: parent `<div data-composition-src="compositions/scene-NN.html" data-start="X" data-duration="Y">`|
    | File structure (`Composition.tsx`, `scenes/`, `constants/`) lines 934-939                                  | HyperFrames structure: `videos/<slug>/index.html` (root) + `videos/<slug>/compositions/scene-NN-<name>.html` (sub-comps) per CLAUDE.md  |
    | Frame-count specs ("300 frames at 30fps")                                                                  | Seconds-based: `data-start` and `data-duration` in seconds (per `.agents/skills/hyperframes-cli/SKILL.md` and CLAUDE.md key rule 1)   |
    | `remotion_bits_components_used: [list]` plan field                                                         | `hyperframes_blocks_used: [list]` plan field referencing `hyperframes-registry` blocks if any                                          |
  - **NEW** sections (HyperFrames-specific):
    - `template_choice:` — must be one of the templates that exists. Today only `shorts/anthropic`. Plan must declare template before scene planning so it can respect the template's structural constraints (e.g., Anthropic Shorts has fixed 4 phase archetypes Hero/Stat/Timeline/CTA — plan can add more phases per `templates/shorts/anthropic/README.md` "Adding more phases" but must follow that convention).
    - `composition_layout:` — root composition + list of sub-compositions to create under `videos/<slug>/compositions/`. For Anthropic Shorts, this is typically inline (no sub-comps); for richer plans, a sub-comp per scene.
    - `data_timing_budget:` — table of `scene → data-start (s) → data-duration (s) → audio_anchor`. The audio anchors come from Phase 2 + transcribe in seconds, not frames.
    - `retention_component_picks:` — for each scene, name the HyperFrames retention component(s) from `retention-components-hyperframes.md`. This is the bridge to Phase 3.5.
  - When the chosen template is `shorts/anthropic`, the plan MUST honor the template's existing 4-phase mutex visibility model (`templates/shorts/anthropic/README.md:18`) and not invent extra phases unless the plan explicitly extends per the template's "Adding more phases" guidance.
- **MIRROR**: Output structure (YAML+Markdown) from source `phase1-plan.md` minus the Remotion-specific fields.
- **GOTCHA**: Phase 1 in the source writes to `.agents/plans/$ARGUMENTS.plan.md`. We're moving it INTO `videos/<slug>/plan.md` so all artifacts live together. Don't accidentally create `.agents/plans/` here.
- **GOTCHA**: The `Skill` tool can be invoked from inside a slash command — verify by reading frontmatter docs. If it cannot, the command must say "before running this command, also invoke /hyperframes and /gsap" instead of trying to call them programmatically.
- **VALIDATE**: Manual — run on a video with a content-brief, confirm `plan.md` is created with all required sections, no Remotion references in output, scene `data-start`/`data-duration` are in seconds.

### Task 5 — CREATE `.claude/commands/diy-yt-creator/phase2-script.md`

- **ACTION**: CREATE Phase 2 command. Near-verbatim port.
- **IMPLEMENT**:
  - Inputs: `videos/<slug>/plan.md`, `videos/<slug>/research/content-brief.md`, `.claude/references/story-locks.md`, `.claude/references/faceless-tech-scriptwriting-playbook.md`. State gate: phase 1 done.
  - Output: `videos/<slug>/scripts/full-script.md` — plain narration, no TTS markup, no metadata, scene headers `## Scene N: [Name]`. Per source `phase2-script.md:14-31`.
  - Hard stop in interactive mode after writing file (per source `phase2-script.md:285-301`); skip stop in autonomous mode (orchestrator passes a flag or env hint).
  - Word-count targets per source `phase2-script.md:65-72` (~2.5 words/sec).
  - Hook variant lock per source `phase2-script.md:56-60` — first sentence of Scene 01 = the variant selected in `plan.md`'s `recommended` field.
  - Built-in 14-check quality checklist per source `phase2-script.md:305-337`.
  - Reference `.claude/references/story-locks.md` and `.claude/references/faceless-tech-scriptwriting-playbook.md` (NOT source paths).
- **MIRROR**: Source `phase2-script.md` structure verbatim, only paths change.
- **GOTCHA**: Source plan-discovery has a 3-step fallback including kebab-case glob (`phase2-script.md:44-49`). Here the plan is always at the deterministic path `videos/<slug>/plan.md`, so the fallback is unnecessary — drop it, simpler to debug.
- **VALIDATE**: Manual — run on a video with a plan, confirm `scripts/full-script.md` is created with `## Scene N:` headers and plain prose.

### Task 6 — CREATE `.claude/commands/diy-yt-creator/phase2-5-critique.md`

- **ACTION**: CREATE Phase 2.5 command. Verbatim port (paths only).
- **IMPLEMENT**:
  - Inputs: `videos/<slug>/scripts/full-script.md`, `videos/<slug>/plan.md`, `.claude/references/story-locks.md`, `.claude/references/faceless-tech-scriptwriting-playbook.md`.
  - Output: `videos/<slug>/scripts/critique-report.md`. State gate: row `2.5 - Critique` set to `done (X.X/10 hook, X.X/10 arc)` on PASS, `blocked (<failed gate names>)` on FAIL.
  - All four passes (Hook scoring, Retention curve, TTS readability, Story arc, AI-phrasing detection) verbatim per source `phase2-5-critique.md` — pure content scoring, no renderer coupling.
  - Gate thresholds verbatim: hook ≥ 7.0, arc ≥ 7.0, loop openers ≥ `max(2, floor(duration_min / 1.5))`, 0 Critical/High banned phrases.
  - On FAIL: BLOCK Phase 2a (per source `phase2-5-critique.md:12-14`).
- **MIRROR**: Source verbatim.
- **GOTCHA**: Source banned-phrase reference path is `.claude/research/faceless-tech-scriptwriting-playbook.md`. Update to `.claude/references/faceless-tech-scriptwriting-playbook.md` (consolidated location per Task 1).
- **VALIDATE**: Manual — run on a script that intentionally contains a banned phrase ("delve into", "in today's fast-paced..."). Confirm phase blocks. Then run on a clean script, confirm phase passes.

### Task 7 — CREATE `.claude/commands/diy-yt-creator/phase2a-tts-script.md`

- **ACTION**: CREATE Phase 2a command. Adapt — skill reference changes.
- **IMPLEMENT**:
  - Inputs: `videos/<slug>/scripts/full-script.md`, state gate: `2.5 - Critique` is `done` (NOT `blocked`).
  - Outputs:
    - `videos/<slug>/scripts/scene-NN-<name>.txt` — one file per scene, kebab-case names per source `phase2a-script.md:68-69`.
    - **NEW for this project**: `videos/<slug>/script.txt` — flattened concatenation of all scenes (just the narration text, no headers). This is what the existing `npx hyperframes tts` reads (per `new-anthropic-short.md` step 5). Without this, the existing TTS pipeline breaks. Verify by reading `videos/claude-connectors-everyday-life/script.txt` for the format reference.
  - Skill reference: replace source's `elevenlabs-tts-optimizer` (Skill tool) with this repo's `text-to-speech` skill (the ElevenLabs skill at `.agents/skills/text-to-speech/SKILL.md`). Verify the actual skill name string in its SKILL.md frontmatter and use that exact name in the Skill tool call.
  - Per-scene verification per source `phase2a-script.md:76-82` (word count ±10%, sentence ≤20 words, ≤2-3 break tags, ≤800 chars).
  - State: `2a - TTS Script` set to `done`.
- **MIRROR**: Source `phase2a-script.md` structure.
- **GOTCHA**: The TWO outputs (per-scene `.txt` AND flat `script.txt`) is the key adaptation. Forgetting the flat file breaks `npx hyperframes tts`. Document this dual write at the top of the command file so a future maintainer doesn't rip out the "redundant" flat file.
- **GOTCHA**: Existing `videos/claude-connectors-everyday-life/script.txt` has zero scene markers and zero blank-line phase separators — just continuous prose. Preserve that format for `script.txt` (concatenated). The per-scene `.txt` files keep their structure for downstream use.
- **VALIDATE**: Manual — confirm BOTH `scripts/scene-NN-*.txt` files AND `script.txt` exist after running. Confirm `script.txt` matches the existing video's flat format. Confirm `npx hyperframes tts videos/<slug>` succeeds against the produced `script.txt`.

### Task 8 — CREATE `.claude/commands/diy-yt-creator/phase2b-factcheck.md`

- **ACTION**: CREATE Phase 2b command. Verbatim port (paths only).
- **IMPLEMENT**:
  - Inputs: `videos/<slug>/scripts/full-script.md`, `videos/<slug>/scripts/scene-NN-*.txt`, `videos/<slug>/research/content-brief.md`. State gate: `2a - TTS Script` is `done`.
  - Tools: WebSearch + WebFetch for every Tier-1 / Tier-2 claim per source `phase2b-factcheck.md:83-93`.
  - Optional: Perplexity API call via Python script. Source uses `python scripts/perplexity-verify.py $ARGUMENTS` — there is **no** `scripts/perplexity-verify.py` in this repo (only `scripts/sync-shared-assets.sh`). Skip the Perplexity branch entirely if `PERPLEXITY_API_KEY` is unset OR if `scripts/perplexity-verify.py` doesn't exist. Don't create the Python script in this batch.
  - Output: `videos/<slug>/scripts/fact-check-report.md`. State: `2b - Fact Check` set to `done (N/N claims verified)` on PASS, `blocked (N failed claims)` on FAIL.
  - Three-tier classification, six-verdict vocabulary, gate condition (zero Tier-1 FAILED + zero Tier-1 UNVERIFIED + zero broken Tier-1 sources) — all verbatim per source `phase2b-factcheck.md:46-118` and `289-294`.
  - Auto-correction (minor) vs hard-stop (major) rule per source `phase2b-factcheck.md:267-279`.
- **MIRROR**: Source verbatim minus Perplexity.
- **GOTCHA**: When auto-correcting in autonomous mode, the corrections are applied to the per-scene `.txt` files. If we regenerate `script.txt` (from Task 7), keep them in sync. Either (a) re-run the flatten-into-script.txt step after Phase 2b corrections, or (b) document that running Phase 2a after Phase 2b is required if Phase 2b auto-corrected anything. Pick (a) — bake a re-flatten step into Phase 2b's auto-correction block.
- **VALIDATE**: Manual — run on a script with a known-false stat ("Claude Code has 100 million users" if false) — confirm phase blocks. Run on a clean script — confirm phase passes with verified count.

### Task 9 — CREATE `.claude/commands/diy-yt-creator/phase3-5-retention.md`

- **ACTION**: CREATE Phase 3.5 command. Inputs rewritten.
- **IMPLEMENT**:
  - Inputs:
    - `videos/<slug>/plan.md` (Phase 1)
    - `videos/<slug>/scripts/full-script.md` (Phase 2)
    - `videos/<slug>/transcript.json` — produced by `npx hyperframes transcribe videos/<slug>` after `npx hyperframes tts` runs. **REPLACES** source's `sceneNN-sync.json` and `timing.ts`. Verify the transcript.json format by reading `.agents/skills/hyperframes/references/transcript-guide.md` if it exists.
  - State gate: `transcript.json` MUST exist (means TTS+transcribe step has run between Phase 2b and 3.5). Phase 2b being `done` is necessary but NOT sufficient — phase 3.5 explicitly checks for the transcript file's presence and tells the user "run `npx hyperframes tts videos/<slug> && npx hyperframes transcribe videos/<slug>` first" if missing.
  - Output: `videos/<slug>/retention-strategy.md` — per-scene retention component picks. References `.claude/references/retention-components-hyperframes.md` for available picks.
  - Sub-agent: `general-purpose` with `subagent_type` (NOT source's `retention-strategy-agent` which doesn't exist here). Self-contained prompt that lists what to read, what to write.
  - Output Summary Table — main orchestrator only reads this section back to user.
  - Note in command body: "the source phase3-5-retention.md uses Remotion frame conversion `frame = word.start * 30 + audio_offset`. HyperFrames uses seconds directly via `data-start`/`data-duration`. The retention agent should output per-scene retention picks in seconds, not frames."
- **MIRROR**: Source `phase3-5-retention.md` overall command structure.
- **GOTCHA**: The retention strategy output names HyperFrames retention components by name (e.g., "marker-sweep", "audio-reactive-glow") so Phase 4 (the existing `new-anthropic-short.md` step 8 HTML edit) can pick them up. The component vocabulary lives in `.claude/references/retention-components-hyperframes.md` (Task 1). Do not invent component names that aren't in that doc — the framework won't recognize them.
- **VALIDATE**: Manual — run on a video with `transcript.json`, confirm `retention-strategy.md` is created with a Summary Table and per-scene picks that all reference real entries in `retention-components-hyperframes.md`.

### Task 10 — CREATE `.claude/commands/diy-yt-creator/full-auto.md`

- **ACTION**: CREATE orchestrator. Modeled on source `full-auto-v2.md`.
- **IMPLEMENT**:
  - Frontmatter: `description: Full pipeline — research → plan → script → critique → TTS-script → fact-check → (existing TTS+transcribe) → retention strategy`, `argument-hint: <topic | URL | brief.md> [--upload not-supported]`, `allowed-tools: Bash, Read, Write, Edit, Glob, Grep, Task, Skill, WebSearch, WebFetch`.
  - Phase chain (sequential, sub-agent dispatched per `full-auto-v2.md:106-117`):
    1. Phase 0 → Phase 1 → Phase 2 → Phase 2.5 (BLOCKING) → Phase 2a → Phase 2b (BLOCKING)
    2. **PAUSE** — print to user: "Pipeline complete through Phase 2b. Now run `npx hyperframes tts videos/<slug> && npx hyperframes transcribe videos/<slug>`, then re-run `/diy-yt-creator:full-auto --resume <slug>` to execute Phase 3.5."
    3. On `--resume <slug>`: skip phases 0–2b, dispatch Phase 3.5, then PAUSE again at composition build with: "Pipeline complete through Phase 3.5. Now invoke `/diy-yt-creator:new-anthropic-short <slug>` to build the composition using `plan.md` and `retention-strategy.md` as inputs."
  - Crash recovery: read `phase-status.md`, resume from first `pending` row (per source `full-auto-v2.md:99-100`).
  - Orchestration log: `videos/<slug>/orchestration-log.md` — only <200-word summaries per phase (per source `full-auto-v2.md:116-117`). The orchestrator never re-reads full artifacts after a phase completes.
  - Brief detection: detect structured-brief vs free-form by `**Topic**:` marker (per source).
  - Slug derivation: kebab-case from topic if not in brief; if brief specifies a slug, use it.
- **MIRROR**: Source `full-auto-v2.md` orchestration shape — context-isolation mandate, sub-agent dispatch, status-file-driven recovery.
- **GOTCHA**: Source's `full-auto-v2.md` chains all the way through render. Ours STOPS after Phase 2b for human handoff (run TTS), then resumes for Phase 3.5, then hands off to `new-anthropic-short.md` for HTML build. Three explicit stop points. This is a deliberate departure from the source's "full automation" model — necessary because TTS audio generation is a side effect the user may want to review (voice/speed/quality) before proceeding.
- **GOTCHA**: Drop the `--upload` flag from source. No upload story in this repo.
- **VALIDATE**: Manual — run with a trivial topic, confirm pipeline pauses correctly at TTS step, resume runs Phase 3.5, ends at composition handoff.

### Task 11 — UPDATE `.claude/skills/diy-yt-creator/SKILL.md`

- **ACTION**: UPDATE existing skill manifest.
- **IMPLEMENT**:
  - Add a new section **after** the existing "Available commands" table:
    ```markdown
    ## Pipeline commands (research + scriptwriting)

    | Command | Use when |
    |---|---|
    | [/diy-yt-creator:full-auto](../../commands/diy-yt-creator/full-auto.md) | End-to-end pipeline from topic to retention-engineered script + per-scene retention strategy. Stops twice for human review (TTS, composition build). |
    | [/diy-yt-creator:phase0-research](../../commands/diy-yt-creator/phase0-research.md) | Topic research only |
    | [/diy-yt-creator:phase1-plan](../../commands/diy-yt-creator/phase1-plan.md) | Composition plan (after Phase 0) |
    | [/diy-yt-creator:phase2-script](../../commands/diy-yt-creator/phase2-script.md) | Draft script (after Phase 1) |
    | [/diy-yt-creator:phase2-5-critique](../../commands/diy-yt-creator/phase2-5-critique.md) | Quality gate on script (after Phase 2) |
    | [/diy-yt-creator:phase2a-tts-script](../../commands/diy-yt-creator/phase2a-tts-script.md) | TTS-optimize script (after Phase 2.5) |
    | [/diy-yt-creator:phase2b-factcheck](../../commands/diy-yt-creator/phase2b-factcheck.md) | Fact-check claims (after Phase 2a) |
    | [/diy-yt-creator:phase3-5-retention](../../commands/diy-yt-creator/phase3-5-retention.md) | Per-scene retention strategy (after `npx hyperframes transcribe` runs) |
    ```
  - Add a "When to use the pipeline vs direct skill invocation" subsection:
    ```markdown
    ## Pipeline vs direct
    - **Use `/diy-yt-creator:full-auto`** when the user gives you a topic and wants a researched, fact-checked, retention-engineered video. This is the default.
    - **Use `/diy-yt-creator:new-anthropic-short` directly** when the user already has a finished `script.txt` (or content brief) and just wants the composition built. Skips all research/critique steps.
    ```
- **MIRROR**: Existing SKILL.md table style + tone.
- **GOTCHA**: Don't break the existing `Available commands` table or the "Hard rules" section. Append, don't restructure.
- **VALIDATE**: Read the updated file, confirm both old and new sections are present and the markdown renders cleanly.

### Task 12 — UPDATE `.claude/skills/diy-yt-creator/new-anthropic-short.md` (Step 4)

- **ACTION**: UPDATE step 4 ("Draft the script").
- **IMPLEMENT**:
  - Replace the current "Draft the script" content with branched logic:
    ```markdown
    ## 4. Draft the script

    **Branch A — pipeline output exists:** If `videos/$SLUG/scripts/full-script.md` exists
    (Phases 0-2b have run), READ it as the source of truth. Skip the inline drafting; jump
    to step 4.5 (map to template phases).

    **Branch B — no pipeline output:** Use the inline drafting rules below to invent a script
    from the user's topic. (This is the legacy path — for any new video, prefer
    `/diy-yt-creator:full-auto <topic>` first to produce `full-script.md`, then come back here.)

    ### 4.5 Map script → template phases (always runs, regardless of branch)

    The Anthropic Shorts template has 4 phase archetypes (Hero/Stat/Timeline/CTA). Map the
    script's `## Scene N:` sections (Branch A) or your inline draft (Branch B) onto these
    archetypes, respecting the template's mutex-visibility model.

    If the plan (`videos/$SLUG/plan.md`) exists, READ its `composition_layout` and
    `retention_component_picks` sections — they tell you exactly which template phase each
    scene maps to AND what retention components to use. Don't override the plan; if you
    think it's wrong, edit the plan first, then re-derive.
    ```
  - Keep the rest of the step 4 content (the existing inline drafting rules) under "Branch B" so legacy use still works.
  - Add a brief note at the very top of the file: "This skill builds the composition. For research + scriptwriting first, see `/diy-yt-creator:full-auto`."
- **MIRROR**: Existing `new-anthropic-short.md` numbering and tone (terse, command-like).
- **GOTCHA**: Don't break steps 5–12 (TTS, transcribe, edit HTML, lint, inspect, preview). They run unchanged.
- **GOTCHA**: The "Hard rules" carried in SKILL.md (never auto-render, never fabricate facts) still apply. The pipeline reduces fabrication risk because Phase 2b runs, but Branch B (inline drafting) keeps the same "if no source, ASK" rule from the existing skill.
- **VALIDATE**: Manual — run `/diy-yt-creator:new-anthropic-short` on a video that has `full-script.md` (Branch A), confirm it reads the script. Run on a video that doesn't (Branch B), confirm it falls back to inline drafting.

### Task 13 — Add `.gitignore` lines for transient pipeline artifacts

- **ACTION**: APPEND to `.gitignore`.
- **IMPLEMENT**:
  - Add lines to ignore intermediate logs that shouldn't be committed:
    ```
    # Pipeline intermediate artifacts (commit final outputs, not logs)
    videos/*/orchestration-log.md
    videos/*/.phase-cache/
    ```
  - Do NOT ignore `phase-status.md`, `research/content-brief.md`, `plan.md`, `scripts/*.md`, `scripts/*.txt`, `retention-strategy.md`. These are the audit trail and SHOULD be committed.
- **MIRROR**: Existing `.gitignore` style — read it first, append at end with a section header.
- **GOTCHA**: The orchestration log is high-volume and low-signal once a video is done; ignoring it keeps git history clean. The phase-status file is small and high-signal — keep it tracked.
- **VALIDATE**: `git check-ignore videos/foo/orchestration-log.md` returns the path (means it's ignored). `git check-ignore videos/foo/phase-status.md` returns nothing (not ignored).

### Task 14 — End-to-end smoke test on a throwaway video

- **ACTION**: Manual end-to-end validation.
- **IMPLEMENT**:
  - Pick a trivial topic: e.g., "Claude Code Skills launch" (slug `test-pipeline-skills`). This is a real, well-documented topic so research won't dead-end.
  - Run `/diy-yt-creator:full-auto Claude Code Skills launch`.
  - Verify each phase produces the expected file:
    - `videos/test-pipeline-skills/research/content-brief.md`
    - `videos/test-pipeline-skills/plan.md`
    - `videos/test-pipeline-skills/scripts/full-script.md`
    - `videos/test-pipeline-skills/scripts/critique-report.md`
    - `videos/test-pipeline-skills/scripts/scene-NN-*.txt`
    - `videos/test-pipeline-skills/script.txt` (flat — required by existing TTS pipeline)
    - `videos/test-pipeline-skills/scripts/fact-check-report.md`
    - `videos/test-pipeline-skills/phase-status.md` rows 0 through 2b all `done`
  - Run `npx hyperframes tts videos/test-pipeline-skills` — must succeed against the produced flat `script.txt`.
  - Run `npx hyperframes transcribe videos/test-pipeline-skills` — produces `transcript.json`.
  - Run `/diy-yt-creator:full-auto --resume test-pipeline-skills` — runs Phase 3.5, produces `videos/test-pipeline-skills/retention-strategy.md`.
  - Run `/diy-yt-creator:new-anthropic-short test-pipeline-skills` — should hit Branch A in step 4 (script exists) and use `plan.md` + `retention-strategy.md` to drive the HTML edit.
  - Run `npx hyperframes lint videos/test-pipeline-skills` — must be 0 errors.
  - Delete the throwaway video after validation: `rm -rf videos/test-pipeline-skills`.
- **GOTCHA**: A real end-to-end run will burn web search quota and ElevenLabs TTS credit. Time-box to one full run. If a phase fails, fix it, then resume from the failed phase using the status file (don't re-run from Phase 0).
- **VALIDATE**: All eight phase artifacts exist with non-trivial content; `lint` is clean; `phase-status.md` shows the right state vocabulary.

---

## Testing Strategy

This is a slash-command and reference-doc feature. There are no unit tests in this repo (no `package.json` with a test runner). Validation is **observable behavior** of the slash commands plus markdown linting.

### Validation per task type

| Task type                  | Validation                                                                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Reference doc (Task 1)     | File exists, frontmatter (if any) parses, examples reference real HyperFrames artifacts (grep against `.agents/skills/hyperframes/`).  |
| Phase command (Tasks 3-9)  | Manual invocation on a throwaway video produces the documented output file with the documented sections; phase-status row updates.     |
| Orchestrator (Task 10)     | Manual invocation chains correctly; pause/resume points work; sub-agent dispatch works; orchestration-log produced.                    |
| Skill update (Tasks 11-12) | Existing tests (manual: `/diy-yt-creator:new-anthropic-short` on existing `claude-connectors-everyday-life`) still pass.               |
| Smoke test (Task 14)       | All phases run end-to-end on a real topic; lint passes on the resulting composition (after the existing skill takes over for HTML).    |

### Edge cases checklist (from source phase analysis, confirmed applicable here)

- [ ] Topic with no good web sources → Phase 0 quality gates flag missing proof points; orchestrator continues with WARN
- [ ] Banned phrase ("delve into", "in today's fast-paced world", "imagine a world where") in script → Phase 2.5 BLOCKS Phase 2a
- [ ] Hook score < 7.0 → Phase 2.5 BLOCKS Phase 2a
- [ ] Tier-1 claim with no source → Phase 2b BLOCKS handoff to TTS
- [ ] Tier-1 claim with broken source URL → Phase 2b BLOCKS handoff to TTS
- [ ] User runs Phase 1 before Phase 0 → Phase 1 detects missing `content-brief.md`, errors with "run /diy-yt-creator:phase0-research first"
- [ ] User runs Phase 3.5 before TTS+transcribe → Phase 3.5 detects missing `transcript.json`, errors with the exact CLI commands to run
- [ ] vidiq MCP tools unavailable → Phase 0 silently skips enrichment, no error
- [ ] Re-running Phase 0 on a slug that already has `content-brief.md` → warn + overwrite (per source `phase0-research.md:34-38`)
- [ ] Pipeline crashes mid-phase → orchestrator's `phase-status.md`-driven recovery resumes from the first `pending` row
- [ ] Phase 2b auto-corrects a stat → `script.txt` re-flatten triggers automatically (per Task 8 gotcha)

---

## Validation Commands

This repo has no `package.json` test runner. Validation is shell-level + manual invocation.

### Level 1 — Static checks

```bash
# Confirm command files exist with frontmatter
for f in .claude/commands/diy-yt-creator/*.md; do
  head -5 "$f" | grep -q "^description:" || echo "MISSING description in $f"
done

# Confirm reference docs exist and aren't stubs
for f in .claude/references/{story-locks,faceless-tech-scriptwriting-playbook,retention-components-hyperframes}.md; do
  test -f "$f" || echo "MISSING $f"
  test $(wc -l < "$f") -gt 50 || echo "STUB $f (under 50 lines)"
done

# Confirm SKILL.md was actually updated
grep -q "Pipeline commands" .claude/skills/diy-yt-creator/SKILL.md || echo "SKILL.md not updated"

# Confirm new-anthropic-short.md branched
grep -q "Branch A" .claude/skills/diy-yt-creator/new-anthropic-short.md || echo "Step 4 not branched"
```

**EXPECT**: All checks output nothing (no MISSING/STUB messages).

### Level 2 — Per-phase smoke tests

```bash
# Run each phase command in isolation against a throwaway video.
# Expected: each command exits cleanly, produces its documented output file,
# and updates phase-status.md correctly.

SLUG="lint-smoke"
mkdir -p videos/$SLUG
echo '{"id":"'$SLUG'","name":"Lint Smoke","createdAt":"2026-04-27T00:00:00Z"}' > videos/$SLUG/meta.json

# Then invoke each phase command via Claude Code; observe artifact creation.
```

**EXPECT**: Each phase produces its artifact; `phase-status.md` rows update correctly; `npx hyperframes lint videos/lint-smoke` passes (lint runs against HTML; should be 0 errors since no HTML edited yet).

### Level 3 — Full pipeline smoke test

(See Task 14.)

**EXPECT**: All eight phase artifacts exist; `phase-status.md` shows correct vocabulary; pipeline pauses at the right handoff points; `lint` clean.

### Level 4 — No regressions in existing pipeline

```bash
# The existing video must not be affected.
npx hyperframes lint videos/claude-connectors-everyday-life
npx hyperframes inspect videos/claude-connectors-everyday-life
```

**EXPECT**: Both commands pass identically to before this feature was added.

### Level 5 — Hook still works

```bash
# Verify the existing PostToolUse + SessionStart hook on .claude/settings.json
# still fires after Write/Edit operations on the new files.
ls -la shared/ASSETS.md  # mtime should update after we Write any file in this PR
```

**EXPECT**: `shared/ASSETS.md` mtime is recent (the sync hook ran).

---

## Acceptance Criteria

- [ ] All 7 phase commands and 1 orchestrator are present under `.claude/commands/diy-yt-creator/` with proper frontmatter.
- [ ] All 3 reference docs are present under `.claude/references/` with non-stub content (>50 lines each).
- [ ] `.claude/skills/diy-yt-creator/SKILL.md` lists the new commands AND the pipeline-vs-direct guidance.
- [ ] `.claude/skills/diy-yt-creator/new-anthropic-short.md` step 4 has Branch A (read pipeline output) + Branch B (legacy inline drafting).
- [ ] Phase 1 (HyperFrames-native plan) contains ZERO references to: `Composition.tsx`, `remotion-bits`, `TransitionSeries`, `hookSprings.ts`, frame counts at 30fps, `src/<AnimationName>/scenes/`. Grep test:
  ```bash
  grep -E "Composition\.tsx|remotion-bits|TransitionSeries|hookSprings|30fps|src/.*\.tsx" .claude/commands/diy-yt-creator/phase1-plan.md && echo "FAIL: Remotion leak"
  ```
- [ ] Phase 2a writes BOTH `scripts/scene-NN-*.txt` AND flat `script.txt`.
- [ ] Phase 2b's auto-correction path re-flattens `script.txt`.
- [ ] Phase 3.5 reads `videos/<slug>/transcript.json`, NOT `sceneNN-sync.json` or `timing.ts`.
- [ ] `full-auto.md` orchestrator pauses at TTS handoff and at composition-build handoff (no auto-render, no auto-TTS).
- [ ] vidiq enrichment in Phase 0 is OPTIONAL and detected at runtime — phase doesn't fail if vidiq tools are absent.
- [ ] Existing `videos/claude-connectors-everyday-life/` lints/inspects identically to before.
- [ ] Throwaway end-to-end smoke test (Task 14) succeeds.

---

## Completion Checklist

- [ ] Tasks 1–13 completed in order (Task 14 is end-to-end validation, runs last)
- [ ] Each phase command's frontmatter parsed (Level 1 grep)
- [ ] Reference docs are non-stub (Level 1 grep)
- [ ] No Remotion leaks in Phase 1 (Level 1 grep)
- [ ] Existing video lints/inspects clean (Level 4)
- [ ] PostToolUse hook still fires (Level 5)
- [ ] End-to-end smoke test passes (Task 14 / Level 3)
- [ ] All acceptance criteria met
- [ ] `.gitignore` updated (Task 13)

---

## Risks and Mitigations

| Risk                                                                                         | Likelihood | Impact | Mitigation                                                                                                                                                       |
| -------------------------------------------------------------------------------------------- | ---------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Phase 1 rewrite drifts from source intent — loses important narrative-arc / hook-scoring nuance | MED        | HIGH   | Mandatory P0 read of source `phase1-plan.md`. Keep all CONTENT-LAYER sections verbatim (Kallaway arc, hook variant scoring, music profile). Only swap RENDERER-LAYER table per Task 4 substitution rules. Manual diff review against source after writing. |
| Skill tool can't be invoked from inside a slash command (frontmatter limitation)             | LOW        | MED    | Verify by reading current Claude Code slash-command docs. If unsupported, Phase 1's "invoke /hyperframes and /gsap" becomes a documented prerequisite the user must run before the command, not a programmatic call. |
| Sub-agent dispatch via Task tool from inside a slash command differs from inside a skill     | LOW        | MED    | Test in Task 14 smoke test. If broken, fall back to inline phase execution (single agent, no isolation) — slower context growth but functional.                 |
| `npx hyperframes transcribe` JSON format differs from what Phase 3.5 expects                 | MED        | MED    | Read `.agents/skills/hyperframes/references/transcript-guide.md` BEFORE writing Phase 3.5 (Task 9). Match the actual JSON schema, not assumptions.              |
| The existing `script.txt` flat-prose format isn't what `npx hyperframes tts` actually expects | LOW        | HIGH   | Read `videos/claude-connectors-everyday-life/script.txt` (existing working example) and replicate exactly. Manual TTS run during Task 14 smoke test catches this immediately. |
| vidiq MCP tools authentication state varies between sessions                                 | MED        | LOW    | Phase 0's vidiq enrichment must wrap calls in a try/skip pattern — never fail the phase on vidiq error. Document as "best effort enrichment" in the command file. |
| Two pipeline pause points (TTS handoff, composition handoff) confuse users                    | MED        | MED    | Both pauses print explicit, copy-pasteable next-step commands. The `--resume <slug>` flag makes resumption frictionless. Document the three-step flow at the top of `full-auto.md`. |
| Phases written but nobody reads `phase-status.md` first → re-run wastes work                  | LOW        | MED    | Every phase command's first action: read `phase-status.md` and warn if its row is already `done`. Match source `phase0-research.md:34-38` pattern.                |
| Story-locks and scriptwriting-playbook reference docs ported from source contain Remotion-specific examples | LOW | LOW | Skim each on port; replace any Remotion-specific examples with renderer-neutral or HyperFrames examples. These are stylistic playbooks, not framework docs, so most content is portable. |
| Auto-correction in Phase 2b modifies `.txt` files and orchestrator's <200-word summary doesn't surface what changed | MED | LOW | Phase 2b's report includes a "Corrections Applied" section listing every change. Orchestrator surfaces this section verbatim to user even in autonomous mode.       |

---

## Notes

### Why this is a rewrite, not a copy

The instinct on "bring phase 0...3-5 into this project" is to `cp -r .claude/commands/diy-yt-creation .claude/commands/`. That fails for three reasons:

1. **Phase 1 is 50% Remotion**. It explicitly invokes the `remotion-best-practices` skill, references `src/shared/transitions/presets.ts` and `src/shared/constants/hookSprings.ts` (paths that don't exist here), prescribes `remotion-bits` components by name (`SyncedAnimatedText`, `TypeWriter`, `SyncedCodeBlock` — none of which exist in HyperFrames), specifies frame counts at 30fps (HyperFrames uses seconds), and outputs a plan structured around `Composition.tsx` + `scenes/*.tsx` (HyperFrames uses `index.html` + `compositions/*.html`). A blind copy produces a plan that the rest of the HyperFrames pipeline can't execute. Task 4 has the substitution table.

2. **Phase 3.5's input format is Remotion-flavored**. The source reads `sceneNN-sync.json` (custom Python pipeline output) and `timing.ts` (Remotion constants file), then converts seconds to frames via `× 30`. HyperFrames already produces `transcript.json` in seconds via `npx hyperframes transcribe`. Re-pointing the inputs is necessary, AND it removes the entire frame-conversion arithmetic. Net simplification.

3. **The existing skill (`new-anthropic-short.md`) currently does its own ad-hoc scriptwriting in step 4**. If we copy phase 2 alongside, we have two scripts being drafted by two different paths. Task 12 fixes this by branching step 4 — read pipeline output if it exists, fall back to ad-hoc drafting if not. Without this update, the skill ignores the pipeline.

### Why the orchestrator pauses twice

The source `full-auto-v2.md` runs end-to-end including render. We could match that. We deliberately don't, for two reasons:

1. **TTS quality matters**. Voice / speed / model choice for ElevenLabs (or Kokoro via `npx hyperframes tts`) is a side effect with both monetary cost and quality variance. The user should review the audio before committing the rest of the pipeline.

2. **Composition build is creative work, not assembly**. Phase 4 in the source is a Remotion code-generation phase with hard-coded patterns. Here, it's `new-anthropic-short.md` step 8 — a 13-step HTML edit playbook that needs human-in-the-loop judgment (logo selection, accent rotation, phase timing, SFX placement). Auto-running it would produce a generic output. The handoff lets the human (or a future, more sophisticated build phase) consume `plan.md` + `retention-strategy.md` deliberately.

### Why all artifacts live under `videos/<slug>/` instead of `.agents/plans/`

The source splits artifacts: brief and script under `src/<AnimationName>/`, plan under `.agents/plans/$ARGUMENTS.plan.md`. That's a Remotion-monorepo convention. Here, this project is structured around `videos/<slug>/` as a self-contained workspace per CLAUDE.md "Project Structure". Splitting the plan into `.agents/plans/` would fight that convention and complicate `git mv` / `cp -r` operations for archiving or sharing videos. Co-locating everything under `videos/<slug>/` is the cleaner local convention. Cost: orchestrator must always pass the slug to phase commands so they know where to read/write. Negligible.

### Why we're not registering project-specific agent types

The source uses `retention-strategy-agent`, `diy-phase-runner`, `phase4-scene-builder`, etc. These are project-registered agent types defined somewhere outside the slash command files (likely in the source's `.claude/agents/`). Registering them here would be its own multi-task plan: define the agent files, declare their tools, write their system prompts. Punted to a future plan — `general-purpose` with a self-contained prompt does the job for now, just less elegantly. If usage proves the orchestration is too verbose with `general-purpose`, factor agent registration as a follow-up.

### What's explicitly stronger than the source

- **vidiq integration**. Source ignores vidiq. Here, Phase 0 conditionally enriches with keyword research and competitor signals.
- **Single workspace**. Source spans `src/`, `.agents/plans/`, `.claude/research/`, `.claude/references/`. Here, all per-video artifacts under `videos/<slug>/`, all reference docs under `.claude/references/`. Fewer places to look.
- **No frame-count translation**. Source converts seconds ↔ frames at multiple boundaries. HyperFrames is seconds-native end-to-end.
- **Forced artifact backwards-compatibility**. Phase 2a writes BOTH per-scene `.txt` (source format) AND flat `script.txt` (existing project format). The existing `npx hyperframes tts` keeps working without changes. Source has no equivalent dual-write requirement.

### Future work (out of scope here, but worth flagging)

- Register project-specific agent types (replace `general-purpose` with `diy-phase-runner` etc.) — improves orchestration ergonomics.
- Long-form template + Phase 1 long-form branch.
- HyperFrames-native composition build phase (replacing manual `new-anthropic-short.md` step 8 with a code-generation phase that consumes `plan.md` + `retention-strategy.md`).
- YouTube description + upload phases (source phases 6/7).
- Perplexity API integration for Phase 2b deep verification (port `scripts/perplexity-verify.py`).
- Visual QA phase that reads the rendered preview and scores against `plan.md`.
