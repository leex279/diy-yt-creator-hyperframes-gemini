# Scene Anchors — openclaw-100-codex-fleet

**Phase 4 REDUX-2 (2026-05-16)** — Authoritative scene timing after TTS heteronym fixes:
1. s06: "CLI" → "C L I" (TTS pronunciation rule)
2. s07: "npm" → "N P M", "CLI" → "C L I" (TTS pronunciation rule)
3. s11: "his reply was four words long" → "his reply was one sentence" (the reply IS the full sentence — old framing literally inaccurate)

4 TTS chunks regenerated. narration.wav grew from 524.99s → 525.27s (+0.28s).
Splice points now derived from END timestamps of s05/s07 last words rather than
START of next scene's first word (per task instructions).

Word anchors pulled from the freshly-regenerated `transcript.json` (audio-time)
and re-mapped to composition-time after inserting two 20s silent midroll windows.

## Audio padding strategy

We **pad the WAV** rather than try to play continuous narration over a longer
composition. The padded audio lives at `audio/narration-padded.wav` and is the
sole audio source referenced from `index.html` (alongside the two layered
Hostinger narration tracks).

```
narration.wav (525.27s, after heteronym fixes)
   ├── part-1: 0.000 → 164.927  (s01..s05; splice at end of "design.")
   ├── part-2: 164.927 → 305.797 (s06..s07; splice at end of "agent.")
   └── part-3: 305.797 → 525.27  (s09..s13)

   + 20s silence inserted between part-1 and part-2 (midroll #1, after s05)
   + 20s silence inserted between part-2 and part-3 (midroll #2, after s07)

narration-padded.wav (565.27s, verified via ffprobe)
```

The Hostinger midroll narration is **separate audio** layered ON TOP of the silence
windows on tracks 22 and 23 (main narration sits on track 2):

```
assets/hostinger-midroll-narration-trimmed.wav (19.5s, 500ms fade-out)
   → wired as <audio> twice in index.html, at data-start=164.927 and data-start=325.797
```

Composition timeline runs **570.01s total**: 565.27s of padded narration + ~4.74s of
terminal thumbnail freeze (silent, narration ended).

## Composition-time boundaries

| # | Scene id | `data-start` | `data-duration` | End | First-spoken-word anchor |
|---|---|---:|---:|---:|---|
| 01 | scene-01-hook              |   0.000 |  29.930 |  29.930 | "One developer." @ 0.035 |
| 02 | scene-02-thesis            |  29.930 |  28.745 |  58.675 | "Here's the question..." @ 30.847 |
| 03 | scene-03-avalanche         |  58.675 |  41.876 | 100.551 | "And to do that..." @ 59.626 |
| 05 | scene-05-clawsweeper       | 100.551 |  64.376 | 164.927 | "Okay, back to the fleet" @ 101.468 |
| 04 | **hostinger-midroll-1**    | **164.927** |  **20.000** | **184.927** | (silent main narration; hostinger audio on track 22) |
| 06 | scene-06-crabbox           | 184.927 |  79.897 | 264.824 | "But sweeping old issues" @ audio 165.112 → comp 185.112 |
| 07 | scene-07-clawpatch         | 264.824 |  60.974 | 325.797 | "So the sandbox runs the demo" @ audio 245.764 → comp 265.764 |
| 08 | **hostinger-midroll-2**    | **325.797** |  **20.000** | **345.797** | (silent main narration; hostinger audio on track 23) |
| 09 | scene-09-fleet-recap       | 345.797 |  40.320 | 386.118 | "Back in, and here's how" @ audio 305.936 → comp 345.936 |
| 10 | scene-10-community-split   | 386.118 | 105.113 | 491.231 | "Which is why the reaction split" @ audio 346.257 → comp 386.257 |
| 11 | scene-11-cost-twist        | 491.231 |  35.618 | 526.849 | "And then Steipete dropped" @ audio 452.160 → comp 492.160 |
| 12 | scene-12-support           | 526.849 |  12.515 | 539.365 | "If this was useful" @ audio 487.789 → comp 527.789 |
| 13 | scene-13-cta               | 539.365 |  30.646 | 570.010 | "So here's the debate" @ audio 500.247 → comp 540.247 |

**Composition total**: 570.010s = **9:30**.
**Narration end**: 565.270s (composition-time).
**Thumbnail freeze tail**: ~4.74s of silent held still on the s13 final frame.

### Midroll positions (M:SS for the description chapters)

- Midroll #1 starts at **2:45** (164.927s) — ~29% of video.
- Midroll #2 starts at **5:26** (325.797s) — ~57% of video.

## Audio-time → composition-time shift constants

- Scenes 01–05: composition-time = audio-time (no shift).
- Scenes 06–07: composition-time = audio-time + 20.0s.
- Scenes 09–13: composition-time = audio-time + 40.0s.

For per-scene internal GSAP timing, each scene's sub-composition timeline starts
at `t=0` (per sub-composition wiring rules). Word-level anchors for internal
animations need to subtract the scene's `data-start` from the composition-time
anchor.

## Hostinger narration audio (NEW in REDUX)

Both midrolls play `assets/hostinger-midroll-narration-trimmed.wav` (19.5s,
500ms fade-out) layered on top of the silent main-narration window. They live
on dedicated track indices (22 and 23) so they don't conflict with each other
or the main narration:

```html
<audio id="hostinger-narration-1"
       class="clip"
       src="assets/hostinger-midroll-narration-trimmed.wav"
       data-start="164.927" data-duration="19.5"
       data-track-index="22" data-volume="1"></audio>

<audio id="hostinger-narration-2"
       class="clip"
       src="assets/hostinger-midroll-narration-trimmed.wav"
       data-start="325.797" data-duration="19.5"
       data-track-index="23" data-volume="1"></audio>
```

The original 21.85s narration was trimmed to 19.5s with `ffmpeg afade=t=out:st=19.0:d=0.5`
to prevent bleed into the scene after the midroll (which would step on s06 / s09).

## ffmpeg re-padding command (used in REDUX-2)

```bash
cd videos/openclaw-100-codex-fleet/audio
ffmpeg -y -i narration.wav -ss 0       -to 164.927 -c pcm_s16le part-1.wav
ffmpeg -y -i narration.wav -ss 164.927 -to 305.797 -c pcm_s16le part-2.wav
ffmpeg -y -i narration.wav -ss 305.797             -c pcm_s16le part-3.wav
ffmpeg -y -f lavfi -i anullsrc=channel_layout=mono:sample_rate=44100 -t 20 -c pcm_s16le silence-20s.wav
# concat-list.txt unchanged:
#   file 'part-1.wav'
#   file 'silence-20s.wav'
#   file 'part-2.wav'
#   file 'silence-20s.wav'
#   file 'part-3.wav'
ffmpeg -y -f concat -safe 0 -i concat-list.txt -c copy narration-padded.wav
# expect: duration=565.266
```

Hostinger narration trim (one-time):

```bash
ffmpeg -y -i assets/hostinger-midroll-narration.wav \
  -t 19.5 -af "afade=t=out:st=19.0:d=0.5" \
  assets/hostinger-midroll-narration-trimmed.wav
```
