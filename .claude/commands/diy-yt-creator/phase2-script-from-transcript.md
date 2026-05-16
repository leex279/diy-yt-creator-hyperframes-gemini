---
description: "Phase 2 (screencap-dubbed) — Convert source transcript into a minimally-edited script.txt that preserves recording pacing"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

<objective>
Convert the operator's transcribed recording into `videos/<slug>/script.txt` for TTS, applying ONLY minimal-edit rules so the dub preserves the recording's natural pacing.

**Goal**: Strip fillers, fix obvious flubs, apply the heteronym audit + tech-term spellings — but NEVER restructure, reorder, or add new sentences. Word-count delta vs source MUST stay <= 15%.

**Why this is different from `/diy-yt-creator:phase2-script`**: The standard Phase 2 writes a fresh script from research using the Kallaway Formula, hook variants, story locks, etc. This phase takes an EXISTING spoken transcript and lightly cleans it — the script is already "written" (by the operator, with their mouth). Our job is to make it TTS-readable without breaking sync.

**Input**: `videos/<slug>/source/transcript.json` (or `source/transcript.md` for human review) from `phase0-ingest-recording`.
**Output**: `videos/<slug>/script.txt` (flat narration, one paragraph per natural pause in the recording).
</objective>

<process>

## Step 1 — Prerequisites

1. Confirm `videos/<slug>/source/transcript.json` exists. If not — STOP and tell the operator: "Run `/diy-yt-creator:phase0-ingest-recording <slug> <path>` first."
2. Read `videos/<slug>/source/transcript.json`. Extract the words array and total duration.
3. Read [`.claude/rules/tts-pronunciation.md`](../../rules/tts-pronunciation.md) — the canonical heteronym + tech-term reference. The audit below is sourced from this rule and may grow over time; always read the live file.

## Step 2 — Reconstruct sentences from the transcript

Group words from `transcript.json` into sentences:

1. Words ending with `.`, `?`, `!` end a sentence (Whisper inserts punctuation in `medium.en` and `small.en`).
2. Gaps > 0.6s between adjacent word `end` and next word `start` also end a sentence (natural breath).
3. Preserve the original word order and spacing exactly.

Result: a sentence array `[{ text, words[], start, end }, ...]` that mirrors the recording's natural cadence.

## Step 3 — Apply the minimal-edit rules (in order)

**HARD RULE**: do NOT add new sentences. Do NOT reorder. Do NOT rewrite for "flow." The whole sync premise depends on word-count parity with the source.

### 3a. Strip filler words

Remove these standalone words wherever they appear:

- `um`, `umm`, `ummm`
- `uh`, `uhh`, `uhhh`
- `er`, `erm`
- `like` ONLY when it's a discourse-marker filler (e.g. `it's like, you know, kind of`). Do NOT strip when `like` is a verb (`I like this`) or a comparator (`like this one`).
- `you know` (as filler — almost always strip)
- `sort of`, `kind of` when used as hedges (`it's sort of complicated` → `it's complicated`)
- `basically` when used as filler

**Edge cases**:
- Don't strip `right?` as a tag question (it's intentional).
- Don't strip `okay` when starting a sentence (`Okay, so first...`) — it's a scene transition cue. Strip only when redundant.

### 3b. Strip false starts and self-corrections

Patterns:
- `let me try that again` → REMOVE the entire sentence (and the broken one before it)
- `wait actually` → REMOVE everything before it in the current sentence, keep the corrected part
- Repeated word starts (`the the the signup`) → keep one occurrence
- Restarted sentences (`First we'll — actually let me start over. First we'll click...`) → keep only the corrected sentence

### 3c. Fix obvious flubs

If the operator clearly said the wrong word and the intended word is unambiguous from context, fix it. Examples:
- `click the green submit buddle` → `click the green submit button` (typo flub)
- `the readme is in the assitents folder` → `the readme is in the assistants folder`

Do NOT fix:
- Stylistic word choices (operator's voice)
- Anything where the intended word is ambiguous (flag instead in step 6)

### 3d. Heteronym audit (per `.claude/rules/tts-pronunciation.md`)

For each occurrence of these words, decide if the spelling will read correctly in context. If ambiguous, swap to the canonical synonym:

| Word | Adjective sense | Default swap |
|---|---|---|
| `live` | broadcast / available (adj) | `available` / `shipping` / `running` |
| `lead` | leader / primary (n/adj) | `primary` / `head` |
| `read` | present tense | usually context-safe; rephrase only if ambiguous |
| `close` | near (adj) | usually context-safe; replace with `near` if ambiguous |
| `minute` | tiny (adj) | `tiny` / `miniscule` |
| `record` | the recording (n) | `recording` |
| `present` | show (verb) | `show` |

Examples:
- "the feature is live today" → "the feature is available today"
- "the lead developer" → "the primary developer" OR "the team lead developer" (verbose works too)
- "let me present this slide" → "let me show this slide"

### 3e. Tech term spellings (per `.claude/rules/tts-pronunciation.md`)

Replace consistently mispronounced tech terms with TTS-friendly spellings:

| Term | TTS spelling |
|---|---|
| `nginx` | `engine-x` |
| `kubectl` | `cube-C T L` |
| `jq` | `jay-queue` |
| `cgroups` | `see-groups` |
| `npm` | `N P M` |
| `OAuth` | `O auth` |
| `regex` | `reh-jex` (only if engine fails it in test; usually fine) |
| `API` | `A P I` |
| `CLI` | `C L I` |
| `SSH` | `S S H` |
| `IDE` | `I D E` |
| `CI/CD` | `C I C D` |
| `OK` | `okay` |
| `dynamous.ai` | `dynamous dot AI` |

If a term in the script isn't in this table and you're unsure how the TTS engine will pronounce it, add a TODO comment to the operator at the end of the script (in HTML-comment form — TTS strips it).

### 3f. Strip Whisper artifacts

Whisper occasionally inserts:
- Bracketed annotations: `[music]`, `[laughs]`, `[clears throat]` — REMOVE
- Speaker markers: `Speaker 1:`, `Speaker 2:` — REMOVE
- Punctuation flubs (double periods `..`, stray commas) — normalize to single

## Step 4 — Write `script.txt`

One paragraph per natural pause in the source recording. Paragraph breaks correspond to the > 0.6s gaps between sentences identified in Step 2.

Format:

```
[paragraph 1 — first natural utterance, after filler stripping]

[paragraph 2 — second natural utterance]

[paragraph 3 — ...]
```

Plain text — no scene headers, no annotations, no TTS markup, no `## Scene 1:` prefixes (those belong to `phase2-script`, not this one). The TTS pipeline reads `script.txt` flat.

If the operator's recording had no natural paragraph breaks (single 5-minute monologue), insert paragraph breaks at every 4-5 sentences for TTS chunking purposes.

## Step 5 — Compute word-count delta

```
source_words = total word count in source/transcript.json
script_words = total word count in script.txt (after edits)
delta_pct    = (source_words - script_words) / source_words * 100
```

**Hard gates**:
- `delta_pct <= 5%` — CLEAN. The script is ready for TTS.
- `delta_pct 5-15%` — WARN. The script likely has heavier filler. Note in the report.
- `delta_pct > 15%` — STOP. The script has been over-edited and sync will drift. Either:
  - Restore more filler words and re-run
  - Tell the operator to re-record with cleaner narration
  - (Operator override) Force-write with `--force` flag if the operator explicitly accepts the drift risk

## Step 6 — Write the operator's review block

Append an HTML-comment block at the END of `script.txt` listing:

- Filler counts stripped (`um=N`, `uh=N`, `like=N`, `you know=N`, false-starts=N)
- Heteronym swaps applied (the actual `X → Y` substitutions)
- Tech-term substitutions applied
- Flubs fixed
- Word-count delta percentage
- Unresolved ambiguities the operator should manually check (if any)

```
<!-- phase2-script-from-transcript audit
Filler strips: um=8 uh=3 like=4 you-know=2 false-starts=1
Heteronym swaps: "live today" -> "available today" (line 3, 12); "lead agent" -> "primary agent" (line 7)
Tech-term swaps: "nginx" -> "engine-x" (line 4); "jq" -> "jay-queue" (line 9)
Flubs fixed: "buddle" -> "button" (line 2)
Word-count delta: -8.4% (source: 743 words, script: 681 words)
Manual-check ambiguities: NONE
-->
```

TTS strips HTML comments — this block is operator-only.

## Step 7 — Report

Report in one block:

```
Script written: videos/<slug>/script.txt
Source words: N
Script words: M
Delta: -X.X% (clean / warn / over-edited)

Edits applied:
  Fillers stripped: um=A uh=B like=C ...
  Heteronym swaps: D
  Tech-term swaps: E
  Flubs fixed: F
  Unresolved ambiguities: G

Next steps:
  1. (Optional) Review videos/<slug>/script.txt for any wording you'd like to tweak.
     Tweaks should be MINIMAL — adding/removing sentences will break sync.
  2. Generate TTS:
       npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav
  3. Verify sync:
       /diy-yt-creator:phase-sync-check <slug>
```

## Edge cases

- **Silent-recording branch** (no transcript): if the operator passed a silent recording to phase0 AND has provided their own script (either at `videos/<slug>/script.txt` already, or via the chat), apply Steps 3d / 3e (heteronym + tech-term audit) to it but skip the filler-stripping and word-count-delta steps. Just normalize and pass through.
- **Operator wrote a fresh script ignoring the transcript**: ASK whether they want the recording-derived pacing or their own. If they want their own, recommend `phase2-script` instead — the natural-sync premise doesn't apply.
- **Transcript has no sentence punctuation**: Some Whisper models produce unpunctuated output. Insert sentence boundaries at every > 0.6s gap and treat each as a sentence. The pacing scaffold is still valid.

</process>

<output>
**Files created**: `videos/<slug>/script.txt` (with operator-review HTML comment block at the end).

**STOP HERE** for operator review unless `--auto-tts` flag was passed.

Tell the operator:
> "Script written: `videos/<slug>/script.txt`
>
> Word count: NEW / SOURCE = M / N (delta: X%). Status: CLEAN / WARN / OVER-EDITED.
>
> Review the script and optionally tweak wording — but do NOT add or remove sentences. The dub's sync depends on word-count parity with the recording.
>
> When ready, generate TTS and run sync-check:
> ```
> npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav
> /diy-yt-creator:phase-sync-check <slug>
> ```"

Do NOT in this command:
- Generate TTS automatically
- Run sync-check
- Modify the composition

Just write the script and stop.
</output>
