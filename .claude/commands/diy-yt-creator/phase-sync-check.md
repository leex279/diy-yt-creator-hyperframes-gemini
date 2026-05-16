---
description: "Phase sync-check (screencap-dubbed) — Compare TTS narration timing vs source recording, flag drift, recommend fix"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

<objective>
After TTS generation, verify the AI-voice narration's pacing matches the source recording closely enough that the dub stays in sync with the screen capture. Report per-sentence drift; recommend (a) speed-adjust if uniform, (b) segment-warp if variable.

**Goal**: Catch sync drift before render. A 0.8s drift you ignored at preview will be jarringly obvious in the final MP4 — the cursor clicks before the narrator says "click", or after.

**Input**:
- `videos/<slug>/source/transcript.json` — word-level timestamps from the original recording
- `videos/<slug>/transcript.json` — word-level timestamps from the new TTS audio (produced by `npx hyperframes transcribe` on `audio/narration.wav`)

**Output**: A sync report table printed to chat, plus `videos/<slug>/sync-report.md` for the record.

**Verdict classes**:
- `CLEAN` — every sentence within +/-0.5s drift. Ship it.
- `WARN` — 1-2 sentences between 0.5-0.8s drift. Acceptable but document it.
- `DRIFT_UNIFORM` — all sentences shifted in the same direction by > 0.5s. Recommend speed-adjust regeneration.
- `DRIFT_VARIABLE` — 2+ sentences exceed +/-0.8s in different directions. Recommend segment-warp (Tier 2 escape hatch).
</objective>

<process>

## Step 1 — Prerequisites

1. Confirm both transcripts exist:
   - `videos/<slug>/source/transcript.json` (from `phase0-ingest-recording`)
   - `videos/<slug>/transcript.json` (from `npx hyperframes transcribe audio/narration.wav -d videos/<slug>`)

   If the new transcript is missing, STOP and tell the operator: "Run TTS + transcribe first:
   ```
   npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav
   npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
   ```"

2. Read both transcripts.

## Step 2 — Reconstruct sentences from each transcript

Apply the same sentence grouping as `phase2-script-from-transcript` step 2:

- Words ending with `.`, `?`, `!` end a sentence
- Gaps > 0.6s end a sentence

Produce two aligned arrays:

```
source_sentences = [{ text, start, end, duration }, ...]
tts_sentences    = [{ text, start, end, duration }, ...]
```

## Step 3 — Align sentences across the two transcripts

The TTS sentences should correspond 1:1 with source sentences if `phase2-script-from-transcript` did its job (no added/removed sentences). Match by:

1. **Position-based matching** is the primary strategy: assume `source_sentences[i]` corresponds to `tts_sentences[i]`. This works when sentence counts are equal.
2. **Fuzzy text-based fallback**: if sentence counts differ, fall back to a Levenshtein-ratio match between source[i] and tts[j] within a +/-2 sentence window. Report any matches with similarity < 0.6 as `UNMATCHED — manual review` in the table.
3. If sentence count delta > 20%, STOP and tell the operator the script was over-edited and they need to re-run `phase2-script-from-transcript` (or restore filler).

## Step 4 — Compute per-sentence drift

For each matched pair:

```
source_dur = source_sentences[i].end - source_sentences[i].start
tts_dur    = tts_sentences[i].end    - tts_sentences[i].start
drift      = tts_dur - source_dur     // positive = TTS is longer
cumulative_drift_at_end = sum of drift up to and including sentence i
```

The **per-sentence drift** is the local mismatch. The **cumulative drift** is what shows up at the end of the video — if every sentence is +0.1s drift, by sentence 50 the cumulative is +5s and the final action in the recording happens 5s before the narration finishes.

## Step 5 — Classify the verdict

```
max_abs_drift           = max(|drift| over all sentences)
max_abs_cumulative      = max(|cumulative_drift|)
uniform_direction       = (all drifts have the same sign AND mean |drift| > 0.2s)
variable_drift_count    = count(sentences where |drift| > 0.8)
```

| Verdict | Condition |
|---|---|
| `CLEAN` | `max_abs_drift <= 0.5` AND `max_abs_cumulative <= 1.0` |
| `WARN` | `0.5 < max_abs_drift <= 0.8` AND `variable_drift_count == 0` |
| `DRIFT_UNIFORM` | `uniform_direction == true` AND `mean_drift > 0.3 OR mean_drift < -0.3` |
| `DRIFT_VARIABLE` | `variable_drift_count >= 2` |
| `DRIFT_MIXED` | `variable_drift_count == 1` AND not uniform — still warn-acceptable but flag the outlier |

## Step 6 — Print the report

Print to chat AND write to `videos/<slug>/sync-report.md`. Same content both places:

```markdown
# Sync report — <slug>

**Generated**: <ISO date>
**Source duration** (recording): `Y min Z s`
**TTS duration** (narration): `Y2 min Z2 s`
**Total delta**: `+/-X.Xs` (TTS vs source)
**Verdict**: `CLEAN` / `WARN` / `DRIFT_UNIFORM` / `DRIFT_VARIABLE` / `DRIFT_MIXED`

## Per-sentence drift

| # | Sentence preview                             | Source dur | TTS dur | Drift  | Cumulative | Status |
|---|----------------------------------------------|-----------:|--------:|-------:|-----------:|--------|
| 01| "Okay so first we head to the homepage."     | 3.2s       | 3.4s    | +0.2   | +0.2       | ok     |
| 02| "Click the signup button in the corner."     | 2.8s       | 2.1s    | -0.7   | -0.5       | warn   |
| 03| "Fill in your email and a strong password."  | 4.1s       | 4.3s    | +0.2   | -0.3       | ok     |
| 04| "You'll see a verification email arrive."    | 3.5s       | 4.5s    | +1.0   | +0.7       | DRIFT  |
| ...

## Diagnosis

<one-paragraph plain-English diagnosis of what the drift pattern means>

## Recommended action

<one of the four blocks below, picked by verdict>
```

### Action blocks (pick one and inline in the report)

**For `CLEAN`**:
> Ship it. The dub is within tolerance. Proceed to composition wiring.

**For `WARN`**:
> Acceptable. Note the WARN sentences in the operator's `notes.md` and proceed. If preview reveals visible mismatch on the flagged sentences, return here for segment-warp.

**For `DRIFT_UNIFORM`** (the most common — TTS slightly faster/slower than source overall):
> Regenerate TTS at adjusted speed. Compute the speed factor:
> ```
> source_total = <source duration>
> tts_total    = <tts duration>
> speed_factor = tts_total / source_total
> ```
> If `speed_factor < 1` (TTS is shorter), regenerate at lower speed:
> ```bash
> npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav -s 0.96
> ```
> If `speed_factor > 1` (TTS is longer), regenerate at higher speed:
> ```bash
> npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav -s 1.04
> ```
> Then re-transcribe and re-run sync-check. Alternative (no re-API-call): post-process with ffmpeg `atempo`:
> ```bash
> ffmpeg -y -i videos/<slug>/audio/narration.wav -filter:a "atempo=<speed_factor>" videos/<slug>/audio/narration-adjusted.wav
> mv videos/<slug>/audio/narration-adjusted.wav videos/<slug>/audio/narration.wav
> ```

**For `DRIFT_VARIABLE`** (multiple sentences exceed +/-0.8 in different directions):
> Tier 2 escape hatch needed. The drift isn't uniform — it varies per sentence, so a single speed-adjust won't fix it. Two options:
>
> 1. **Re-record** with cleaner cadence (the recording was likely uneven — some fast sentences, some slow).
> 2. **Per-segment time-warp the recording**: split the recording at sentence boundaries and `setpts` each segment to fit its TTS counterpart. Per [`.claude/rules/video-speedup.md`](../../rules/video-speedup.md), `ffmpeg setpts` is the only acceptable mechanism. For each flagged sentence:
>    ```bash
>    # speed = source_dur / tts_dur (note: this is the inverse of audio speed)
>    SEG_SPEED=$(python -c "print(<source_dur> / <tts_dur>)")
>    ffmpeg -y -ss <source_start> -to <source_end> -i videos/<slug>/source/recording.mp4 \
>      -filter_complex "[0:v]setpts=PTS/$SEG_SPEED[v]" -map "[v]" \
>      -an videos/<slug>/source/segments/seg_<i>.mp4
>    ```
>    Then concat all segments into a new `assets/clips/recording.mp4`. This is heavy — only do it when re-recording isn't an option.

**For `DRIFT_MIXED`** (one outlier sentence):
> Inspect sentence #<n> in the recording. Common causes: operator coughed/paused mid-sentence, recorded a long thinking-pause, OR Phase 2 missed a filler-word strip. Either:
> - Re-edit just that one sentence in `script.txt` and regenerate TTS for the whole thing
> - Per-segment warp just that one sentence
> - Or accept the drift if the visible mismatch is minor

## Step 7 — Reporting

After writing `sync-report.md`, emit a concise chat summary:

```
Sync verdict: <VERDICT>
  Source total: X min Y s
  TTS total:    X2 min Y2 s
  Total delta:  +/-Z.Zs
  Max per-sentence drift:   +/-A.As at sentence #N
  Max cumulative drift:     +/-B.Bs

Full report: videos/<slug>/sync-report.md

Recommended next step: <one-line action from the action block>
```

## Edge cases

- **Sentence count delta > 20%**: STOP. The script was over-edited. Re-run `phase2-script-from-transcript` (or restore filler in `script.txt`) before continuing.
- **TTS transcript has UNMATCHED sentences**: list them in the report with similarity scores. Don't try to auto-fix — operator needs to decide.
- **Sentence start times are negative or zero in the TTS transcript**: indicates Whisper failed on the TTS audio (rare; usually means the audio file is corrupt or empty). Tell the operator to re-run TTS.

</process>

<output>
**Files created**: `videos/<slug>/sync-report.md`.

**STOP HERE** unless the verdict is `CLEAN`.

For CLEAN: report and recommend proceeding to composition wiring.

For WARN / DRIFT_UNIFORM / DRIFT_VARIABLE / DRIFT_MIXED: report and STOP. Don't automatically regenerate TTS or run ffmpeg — the operator decides whether to accept, regenerate, or re-record.
</output>
