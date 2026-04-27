---
description: "Phase 3.5 — Per-scene retention strategy from transcript.json + plan + script (HyperFrames-native)"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task
---

<objective>
Execute Phase 3.5 of the HyperFrames pipeline.
Analyze the composition's plan, script, and `transcript.json` to produce a concrete per-scene retention strategy.

**Goal**: Map each scene to specific HyperFrames retention components (from `.claude/references/retention-components-hyperframes.md`) with timings in seconds, so the composition build phase has content-aware decisions rather than generic rules.

**Inputs**:
  - `videos/<slug>/plan.md` (from Phase 1)
  - `videos/<slug>/scripts/full-script.md` (from Phase 2)
  - `videos/<slug>/transcript.json` (from `npx hyperframes transcribe` after `npx hyperframes tts`)

**Output**: `videos/<slug>/retention-strategy.md`

HyperFrames is seconds-native — the framework consumes `data-start` / `data-duration` in seconds via `data-*` HTML attributes (CLAUDE.md Key Rule #1). This phase reads `videos/<slug>/transcript.json` directly (no frame conversion). Per-scene component picks must come from `.claude/references/retention-components-hyperframes.md` — those are the names HyperFrames recognizes.
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

The orchestrator pauses Phase 2b and asks the user to run TTS + transcribe. When the user resumes (`/diy-yt-creator:full-auto --resume <slug>`), this phase fires. Run the strategy agent autonomously and return the Summary Table back to the orchestrator.
</autonomous-mode>

<process>

### Phase Gate

Read `videos/<slug>/phase-status.md`.

Hard prerequisites (each must be true):

- [ ] Row `2b - Fact Check` is `done` (not `blocked`).
- [ ] `videos/<slug>/transcript.json` exists. This file is produced by `npx hyperframes transcribe videos/<slug>` after `npx hyperframes tts videos/<slug>` runs. If missing, STOP and report:
  ```
  Phase 3.5 needs videos/<slug>/transcript.json. Run:

    npx hyperframes tts videos/<slug>
    npx hyperframes transcribe videos/<slug>

  Then re-run /diy-yt-creator:phase3-5-retention <slug>.
  ```
- [ ] `videos/<slug>/plan.md` exists (Phase 1).
- [ ] `videos/<slug>/scripts/full-script.md` exists (Phase 2).

**Re-run check**: If `3.5 - Retention` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

### Quality check `transcript.json`

Per `.agents/skills/hyperframes/references/transcript-guide.md`, before consuming `transcript.json`, sanity-check it:

- If more than 20% of word entries are `♪`/`�` tokens, the transcript is bad — STOP and tell the user to re-transcribe with a larger model (`npx hyperframes transcribe ... --model medium.en`).
- Filter out non-word entries (`♪`, `�`, lone "huh"/"uh"/"oh" with `end - start < 0.1`) before passing to the agent.

---

## Execution — Spawn Sub-Agent

**Spawn an isolated `general-purpose` sub-agent** to do the actual analysis. This prevents the transcript JSON from flooding the orchestrator's context.

Use the Task tool:

```
Task tool:
  subagent_type: "general-purpose"
  description: "Phase 3.5 retention strategy for <slug>"
  prompt: |
    You are the retention strategy agent for the HyperFrames video pipeline.

    Slug: <slug>

    Read these files from disk:
      1. videos/<slug>/plan.md                       (the composition plan)
      2. videos/<slug>/scripts/full-script.md        (the narration script with scene headers)
      3. videos/<slug>/transcript.json               (word-level timestamps in seconds)
      4. .claude/references/retention-components-hyperframes.md  (canonical menu of retention picks)
      5. .claude/references/story-locks.md           (loop opener / story lock taxonomy)
      6. .claude/references/faceless-tech-scriptwriting-playbook.md  (retention mechanics §1)
      7. .agents/skills/hyperframes/references/audio-reactive.md
      8. .agents/skills/hyperframes/references/captions.md
      9. .agents/skills/hyperframes/references/transitions.md
      10. .agents/skills/gsap/references/effects.md (for GSAP effect names)

    Filter the transcript: drop entries that are music tokens (♪, �) or single-syllable filler
    (huh/uh/um/ah/oh) shorter than 0.1s. Trust the cleaned word array.

    For EACH scene in plan.md:

    1. Identify the scene's `data_start` and `data_duration` in seconds (from plan.md's
       `## Data Timing Budget` section).

    2. Find the words in transcript.json whose `start` falls inside [data_start, data_start + data_duration].
       These are the words spoken during this scene.

    3. Identify "anchor moments" — moments worth a retention beat:
       - The first word of the scene (entrance moment)
       - Any number, percentage, or stat (potential `gsap-counter-tween` or `marker-highlight`)
       - The pivot word ("but", "however", "yet") if present (potential PIVOT visual moment)
       - Brand names / product names (potential `marker-circle` or `audio-reactive-glow`)
       - The last 1-2 seconds before the scene transition (handoff moment)
       - The hook variant's selected opening line (the slam moment in Scene 01)
       - Any phrase the script marks with [PAUSE] (silence beat, hold the visual)

    4. Pick 1-3 retention components from `.claude/references/retention-components-hyperframes.md`
       for the scene. Cite by canonical name (e.g. `marker-highlight`, `caption-word-pop`,
       `gsap-counter-tween`, `audio-reactive-glow`, `blur-crossfade`). Do NOT invent names —
       the framework only recognizes names from that file.

    5. For each pick, write the EXACT trigger time in SECONDS (not frames):
         - For a marker on a word: trigger_s = word.start
         - For a counter tween anchored to a number: tween_s_range = [number_word.start - 0.5, number_word.end + 0.3]
         - For a transition: trigger_s = scene.data_start + scene.data_duration - transition_duration

    6. Respect constraints from retention-components-hyperframes.md §8:
         - Max 2 markers per scene
         - Only one caption group visible at a time
         - One primary transition (60-70% of scene changes) + 1-2 accents — never different per scene
         - No exit animations on non-final scenes

    Write the strategy to `videos/<slug>/retention-strategy.md` with this structure:

    # Retention Strategy: <slug>

    ## Summary Table
    | Scene | Pattern (from §7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
    |-------|------------------|------------|----------|----------------|----------------|-------------|

    ## Scene-by-Scene Detail

    ### Scene 01: <name> (data_start=0s, data_duration=8s)
    **Words in scene**: 18 (from transcript)
    **Anchor moments**:
      - 0.5s — first word "Claude"
      - 2.1s — "fifteen" (number, candidate for counter tween)
      - 7.2s — "AllTrails" (brand, candidate for marker)
    **Picks**:
      1. `marker-highlight` on "fifteen" — trigger_s: 2.1, sweep_duration: 0.5s
      2. `caption-word-pop` on the whole scene — synced to transcript.json word timings
      3. `blur-crossfade` to Scene 02 — trigger_s: 7.5, duration: 0.5s
    **Why these picks**: <one-paragraph justification grounded in the script content>

    ### Scene 02: ...

    ## Picks Cross-Reference (validate against menu)
    | Pick name | Source file in retention-components-hyperframes.md | Confirmed valid? |
    |-----------|---------------------------------------------------|------------------|

    ## Override Notes
    Phase 4 (composition build) will read this file as authoritative. To override any pick,
    edit this file directly before invoking the build.

    Return ONLY a <200-word summary including:
    - Scenes count
    - Total picks count by category (markers / captions / audio-reactive / transitions / gsap effects)
    - Any constraint violations you almost made (and how you resolved them)
    - Any anchors you couldn't find a good pick for (and why)

    Do NOT return the full strategy file content. Just the summary. The orchestrator reads
    the file from disk via the Summary Table.
```

Wait for the sub-agent to complete. The agent writes `videos/<slug>/retention-strategy.md` autonomously.

---

## After Agent Returns

1. Confirm `videos/<slug>/retention-strategy.md` exists.
2. Read ONLY the `## Summary Table` section from it (not the full per-scene detail — keeps orchestrator context lean).
3. Validate that every pick name in the Summary Table appears as a canonical name in `.claude/references/retention-components-hyperframes.md`. If any unknown names appear, STOP and report which ones — the agent invented them.
4. Report to user:

```
## Retention Strategy Complete: <slug>

<agent's <200-word summary>

### Scene Type Breakdown
<the Summary Table from retention-strategy.md>

### Override Instructions
To change a decision: edit `videos/<slug>/retention-strategy.md` directly.
The file is human-readable. Phase 4 (composition build) reads it as authoritative.

### Action Required Next
The pipeline is COMPLETE through Phase 3.5. The next step is composition build:

  /diy-yt-creator:new-anthropic-short <slug>

That skill will read videos/<slug>/plan.md AND videos/<slug>/retention-strategy.md
to drive the HTML edit (per the updated step 4 Branch A in new-anthropic-short.md).
```

## Update Phase Status

Update `videos/<slug>/phase-status.md` — set `3.5 - Retention` row to `done <YYYY-MM-DD>`.

</process>
