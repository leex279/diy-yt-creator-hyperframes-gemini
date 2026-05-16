---
description: "Phase 0 (screencap-dubbed) — Ingest a screen recording, extract audio, transcribe with word-level timestamps"
argument-hint: <slug> <path-to-recording>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

<objective>
Ingest the operator's screen recording into a screencap-dubbed video project and produce the timing scaffold (word-level transcript) the rest of the pipeline depends on.

**Goal**: Copy the recording into `videos/<slug>/`, extract Whisper-ready audio, run `hyperframes transcribe` to get word-level timestamps, and write a human-readable transcript so the operator can sanity-check before Phase 2.

**Input**: A path to a screen recording (`.mp4`, `.mov`, `.mkv`, `.webm`) + a slug.
**Output**:
- `videos/<slug>/source/recording.mp4` — original recording (preserved as the timing scaffold)
- `videos/<slug>/assets/clips/recording.mp4` — copy wired into the composition
- `videos/<slug>/source/recording.wav` — mono 16kHz PCM extracted for Whisper
- `videos/<slug>/source/transcript.json` — word-level timestamps from the recording
- `videos/<slug>/source/transcript.md` — human-readable transcript with sentence-line markers
</objective>

<process>

## Step 1 — Sanity-check inputs

1. Confirm `videos/<slug>/` exists (operator has already copied the template per the playbook step 2). If not — STOP and tell the operator: "Run step 2 of `new-long-form-screencap-dubbed.md` first: `cp -r templates/long-form/screencap-dubbed videos/<slug>`."
2. Confirm the recording file at `<path-to-recording>` exists and is readable.
3. Probe the recording with `ffprobe`:
   ```bash
   ffprobe -v error -show_format -show_streams "<path>" 2>&1
   ```
   Capture: duration (seconds), video stream dimensions (WxH), fps, audio stream (yes/no), audio sample rate, audio channels.
4. If duration > 15 minutes — WARN: "Recording is over 15 min. This template targets 1-15min. Confirm or trim before ingesting?" Wait for confirmation.
5. If no audio stream present — note SILENT branch: skip transcription, only probe duration + dimensions. Phase 2 will need the operator's separately-written script.

## Step 2 — Stage the source recording

Create `videos/<slug>/source/` if it doesn't exist:

```bash
mkdir -p videos/<slug>/source
```

Copy the recording into two locations:

```bash
# 1. Preserved scaffold (the "ground truth" recording used to derive timings)
cp "<path-to-recording>" videos/<slug>/source/recording.mp4

# 2. Composition-wired copy (the file the <video> element will reference)
cp "<path-to-recording>" videos/<slug>/assets/clips/recording.mp4
```

If the source isn't `.mp4` (e.g. `.mov`, `.mkv`), re-encode the composition copy to `.mp4` h264 baseline for maximum renderer compatibility, but keep the original at `source/recording.<ext>` for archival:

```bash
# Example: .mov -> .mp4 h264
cp "<path-to-recording>" "videos/<slug>/source/recording.<ext>"
ffmpeg -y -i "<path-to-recording>" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  "videos/<slug>/assets/clips/recording.mp4"
```

## Step 3 — Extract Whisper-ready audio

```bash
ffmpeg -y -i "videos/<slug>/source/recording.mp4" \
  -vn -acodec pcm_s16le -ar 16000 -ac 1 \
  "videos/<slug>/source/recording.wav"
```

Flags explained:
- `-vn` — drop video stream
- `-acodec pcm_s16le` — uncompressed PCM (Whisper prefers this; mp3/aac can introduce subtle artifacts that hurt word-boundary detection)
- `-ar 16000` — 16 kHz sample rate (Whisper's native input rate)
- `-ac 1` — mono (Whisper doesn't use stereo info)

If the recording had no audio stream — skip Step 3 and Step 4. Proceed to Step 5 with the silent-branch note.

## Step 4 — Transcribe with word-level timestamps

```bash
npx hyperframes transcribe "videos/<slug>/source/recording.wav" -d "videos/<slug>/source/"
```

For 5+ minute recordings, prefer `-m medium.en` for accuracy on technical vocabulary:

```bash
npx hyperframes transcribe "videos/<slug>/source/recording.wav" -d "videos/<slug>/source/" -m medium.en
```

This writes `videos/<slug>/source/transcript.json` with the schema HyperFrames uses (`{ words: [{ text, start, end, ... }] }`).

## Step 5 — Render a human-readable transcript

Read `videos/<slug>/source/transcript.json`. Group words into sentences by:

1. Words ending in `.`, `?`, `!` end a sentence.
2. Gaps > 0.6s between adjacent word `end` and next word `start` also end a sentence (natural breath).

Write `videos/<slug>/source/transcript.md`:

```markdown
# Source transcript — <slug>

**Recording**: `source/recording.mp4`
**Duration**: `XX min YY s`
**Resolution**: `WxH @ Nfps`
**Audio**: `XXkHz mono` (or `silent`)
**Words**: `N` (`M WPM`)
**Sentences**: `K`

---

## Transcript (with sentence-start timestamps)

[00:00.0]  Okay so today we're going to walk through the signup flow for X.
[00:04.2]  First, head over to the homepage at example.com.
[00:08.5]  You'll see the signup button in the top-right corner — click it.
...

---

## Filler-word density

- `um`: N occurrences
- `uh`: M occurrences
- `like` (as filler): K occurrences
- false-start markers (e.g. "let me try that again"): J

If filler density is > 20 in a 5-minute transcript, consider re-recording with cleaner narration. Phase 2 will strip these, but heavy editing risks restructuring the script and breaking the natural-sync premise.
```

Format the timestamp as `[MM:SS.t]` where `t` is the tenth-of-second.

## Step 6 — Report

Report to the operator in one concise block:

```
Ingested videos/<slug>/source/recording.mp4
  Duration:    XX min YY s
  Resolution:  WxH @ Nfps (aspect: 16:9 / 4:3 / other)
  Audio:       XXkHz mono / silent
  Words:       N (M WPM)
  Sentences:   K
  Fillers:     um=X uh=Y like=Z false-starts=W

Outputs:
  videos/<slug>/source/recording.mp4    (preserved scaffold)
  videos/<slug>/source/recording.wav    (16kHz mono, Whisper-ready)
  videos/<slug>/source/transcript.json  (word-level timestamps)
  videos/<slug>/source/transcript.md    (human-readable, with stats)
  videos/<slug>/assets/clips/recording.mp4  (wired into composition)

Next: /diy-yt-creator:phase2-script-from-transcript <slug>
```

## Step 7 — Handle the silent-recording branch

If the recording had no audio stream:

- Skip Step 3, Step 4, Step 5.
- Still copy the recording per Step 2.
- Report:
  ```
  Ingested videos/<slug>/source/recording.mp4 (SILENT)
    Duration:    XX min YY s
    Resolution:  WxH @ Nfps
    Audio:       NONE

  No transcript generated — recording is silent.

  Next: Provide your narration text to phase2-script-from-transcript, or write it directly to videos/<slug>/script.txt and skip Phase 2.
  ```

## Edge cases

- **Path with spaces**: always quote `"<path-to-recording>"` in bash commands.
- **Path is a URL**: NOT supported. The operator must download the recording locally first. STOP and ask for a local path.
- **Recording is > 2 GB**: WARN before copying. Confirm the operator has disk space.
- **Recording is portrait (e.g. 1080x1920 from a phone)**: WARN — this template targets 1920x1080. Portrait recordings will letterbox heavily. Suggest using a portrait template or cropping the recording.

</process>

<output>
**Files created** under `videos/<slug>/source/` and `videos/<slug>/assets/clips/`.

**STOP HERE.** The operator runs `/diy-yt-creator:phase2-script-from-transcript <slug>` next.

Do NOT proceed to script writing in this command — the transcript is the input, and the user may want to spot-check it before Phase 2 runs.
</output>
