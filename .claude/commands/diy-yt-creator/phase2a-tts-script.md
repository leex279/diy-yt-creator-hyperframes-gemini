---
description: "Phase 2a — Apply TTS optimization, split script into per-scene files, and write flat script.txt for hyperframes tts"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Skill
---

<objective>
Execute Phase 2a of the HyperFrames pipeline.
Take the user-approved (and critique-passed) raw script and apply ElevenLabs TTS optimization, then split into per-scene files. **Also** write a flattened `script.txt` so the existing `npx hyperframes tts` pipeline keeps working.

**Goal**: Transform the reviewed raw script into TTS-optimized scene files PLUS a flat `script.txt`, ready for `npx hyperframes tts videos/<slug>` to consume.

**Input**: `videos/<slug>/scripts/full-script.md` (user-reviewed raw script from Phase 2)
**Outputs**:
1. `videos/<slug>/scripts/scene-NN-<name>.txt` (TTS-optimized per-scene files)
2. `videos/<slug>/script.txt` (flat concatenated narration — required by `npx hyperframes tts`)

**WHY DUAL WRITE**: The composition-build skill (`.claude/skills/diy-yt-creator/new-anthropic-short.md` step 5) calls `npx hyperframes tts videos/<slug>` which reads the flat `videos/<slug>/script.txt` to generate narration. Without writing this flat file, the TTS step has nothing to read and the rest of the workflow breaks. The per-scene `.txt` files are kept alongside it for downstream tooling that wants per-scene resolution.

The flat file follows the same format as `videos/claude-connectors-everyday-life/script.txt`: one continuous prose paragraph (or paragraphs separated by blank lines), no scene headers, no `[PAUSE]` markers, no break tags — just the words to be spoken.
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

If invoked as part of the orchestrator:
- Skip the user confirmation in Step 1
- Proceed directly to optimization and file writing
- Report a <200-word summary back to the orchestrator
</autonomous-mode>

<process>

### Phase Gate

Read `videos/<slug>/phase-status.md`.
- **Prerequisites**: Verify `2.5 - Critique` is `done` (not `blocked` or `pending`).
  - If `blocked`: STOP and report "Phase 2.5 is blocked. Fix the script issues and re-run `/diy-yt-creator:phase2-5-critique <slug>` first."
  - If `pending`: STOP and report "Phase 2.5 has not run. Run `/diy-yt-creator:phase2-5-critique <slug>` first."
- **Re-run check**: If `2a - TTS Script` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

## Step 1 — Read the Approved Script

Read the user-reviewed script from `videos/<slug>/scripts/full-script.md`.

In **interactive mode**: confirm with user — "I see the script in `full-script.md`. Has it been reviewed and approved for TTS processing?" If they say no, tell them to edit `full-script.md` first.

In **autonomous mode**: skip the confirmation; the orchestrator implies approval.

## Step 2 — Apply ElevenLabs Optimization

**MANDATORY**: Invoke the `text-to-speech` skill via the Skill tool to inform optimization.

**How to invoke**: `Skill` tool with `skill: "text-to-speech"`. The skill provides voice settings, env var conventions, and pronunciation guidance for ElevenLabs.

**If the Skill tool can't be invoked from inside a slash command** in your environment, fall back to these manual rules and inform the user:

### Pronunciation fixes

- **Acronyms** (letter-by-letter): `API` → `A P I`, `CLI` → `C L I`, `SSH` → `S S H`, `IDE` → `I D E`, `CI/CD` → `C I C D`
- **DO NOT spell out**: `AI` (ElevenLabs pronounces it naturally), `OK` → `okay`
- **Technical terms**: `nginx` → `engine-x`, `kubectl` → `cube-C T L`, `jq` → `jay-queue`, `cgroups` → `see-groups`, `npm` → `N P M`
- **Brands**: keep as-is unless commonly mispronounced
- Apply any per-video pronunciation overrides from the brief's `Technical Terms` field

### Pause control

- Use `<break time="0.5s" />` between major ideas (sparingly — max 2-3 per scene)
- Use ellipses `...` for dramatic pauses
- Use em-dashes `—` for natural mid-sentence pauses
- Period + new sentence for full stops
- `[PAUSE]` markers in the source script become `<break time="0.5s" />` in `.txt` files (NOT in the flat `script.txt`)

### Quality rules

- Keep each scene script under 800 characters
- No curly braces `{}`, angle brackets `<>` (except break tags), or square brackets `[]`
- Write numbers as words: `100` → `one hundred`
- Expand symbols: `$` → `dollars`, `%` → `percent`, `@` → `at`

### Heteronym audit (MANDATORY before writing any `.txt` file)

Read `.claude/rules/tts-pronunciation.md` and grep the script for every word in its **Heteronyms** table (especially `live`, `lead`, `read`, `close`, `record`, `present`).

For each hit, decide whether the spelling will read correctly in context. If ambiguous, apply the default fix from the rule's table. Common swaps for our content:

- *"live today"* → *"available today"* / *"shipping today"* / *"out today"*
- *"live on <platform>"* → *"shipping on <platform>"* / *"running on <platform>"*
- *"a lead agent"* → *"a primary agent"* / *"a coordinator agent"*

This is a 30-second grep that prevents a 7-minute regen + retime + re-render cycle. Add new heteronyms to `.claude/rules/tts-pronunciation.md` whenever a regen is forced by a mispronunciation — the list is meant to grow.

## Step 3 — Write per-scene `.txt` files

For each scene in `full-script.md`, create a TTS-optimized `.txt` file in `videos/<slug>/scripts/`:

```
videos/<slug>/scripts/
├── full-script.md              # kept as-is for reference
├── critique-report.md          # from Phase 2.5
├── scene-00-preview.txt        # if a preview was written (60s+ videos)
├── scene-01-hook.txt           # TTS-optimized
├── scene-02-<name>.txt         # ...
└── scene-NN-<name>.txt         # ...
```

Use kebab-case names matching the scene purpose (hook, solution, features, cta, etc.). Apply the optimizations from Step 2.

## Step 4 — Write the flat `script.txt` (CRITICAL — do not skip)

Concatenate all scenes' narration into a single flat file at `videos/<slug>/script.txt`. This is what `npx hyperframes tts videos/<slug>` reads.

**Format rules** (matching `videos/claude-connectors-everyday-life/script.txt`):
- Continuous prose, no scene headers
- No break tags, no `[PAUSE]` markers, no `<break time="..." />` — just the words spoken
- Paragraph breaks (blank lines between paragraphs) are OK if the narrative naturally has them
- One trailing newline at end of file
- UTF-8

**Example** (3-scene short):
```
Claude just got fifteen new connectors. AllTrails. Spotify. Uber. Living inside the conversation.

Ask for a weekend hike near you. Claude pulls AllTrails data, picks three options, and books your Uber.

The whole thing happens in one chat. No tab switching. No copy-paste. Just talk to Claude.
```

**Why no break tags here**: `npx hyperframes tts` doesn't parse the ElevenLabs SSML break syntax. Break tags belong in the per-scene `.txt` files where they DO get parsed by the optimizer skill's pipeline.

If the source `full-script.md` has scene narration that splits naturally across paragraphs, preserve those paragraph breaks. If it's all one block, write it as one block.

## Step 5 — Final Verification

For each scene `.txt` file, verify:
- Word count within ±10% of target (`scene_duration_s × 2.5`)
- No sentence exceeds 20 words (hard to follow in audio)
- Technical terms are pronunciation-safe
- Break tags used sparingly (max 2-3 per scene)
- Each scene under 800 characters

For `script.txt`, verify:
- File exists and is non-empty
- Contains no scene headers (no `## Scene` lines)
- Contains no break tags or `[PAUSE]` markers
- Total word count matches the sum of per-scene word counts (±5% accounting for whitespace)

</process>

<output>

**Files created**:
1. `videos/<slug>/scripts/scene-NN-<name>.txt` (one per scene)
2. `videos/<slug>/script.txt` (flat — for `npx hyperframes tts`)

**Report to user**:
1. Confirm whether the `text-to-speech` skill was invoked (or note if fallback rules were applied)
2. Table: Scene | Name | Word Count | Target | Estimated Duration | Char Count | Break Tags
3. List of TTS transformations applied (pronunciation fixes, pause insertions)
4. Any concerns flagged (long sentences, missing pause points, char count > 800)
5. Confirm flat `script.txt` was written and matches existing format
6. Next step: Run `npx hyperframes tts videos/<slug>` to generate `audio/narration.wav`, then `npx hyperframes transcribe videos/<slug>` to produce `transcript.json`. After both succeed, run `/diy-yt-creator:phase2b-factcheck <slug>` (or in `full-auto`, the orchestrator dispatches Phase 2b before TTS).

### Update Phase Status

Update `videos/<slug>/phase-status.md` — set the `2a - TTS Script` row to `done <YYYY-MM-DD>`.
</output>
