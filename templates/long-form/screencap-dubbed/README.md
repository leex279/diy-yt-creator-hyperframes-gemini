# Long-Form Screencap-Dubbed Template

Horizontal YouTube long-form (1920x1080, 30fps, 1-15 minutes) where the bulk of the runtime is a **real screen recording** (you on a website, an app, a terminal) dubbed with an **AI voice** generated from your own transcribed narration. Use this when the video needs authentic screen interaction but you don't want your real voice in the output.

Forked from [`../standard`](../standard/). Full design system in [DESIGN.md](./DESIGN.md). Workflow playbook: [`.claude/skills/diy-yt-creator/new-long-form-screencap-dubbed.md`](../../../.claude/skills/diy-yt-creator/new-long-form-screencap-dubbed.md).

## When to use this template

Pick this template when **all** of the following are true:

1. The video centers on a real screen interaction (signup flow, app demo, tool walkthrough, settings tour) that's hard to fake with a synthetic composition.
2. You don't want your own voice in the published output (privacy, accent preference, polish).
3. You can record the screen with your voice once — explaining what you're doing in your natural pace.

If you can fake the screen content with synthetic visuals, use [`../standard`](../standard/) instead — it's more flexible. If you want screen footage + your real voice, use `../standard` with `scene-video-embed.html`. This template specifically serves the "real recording + dubbed voice" case.

## The dub workflow at a glance

```
1. You record your screen + voice once (silent screen capture works too if you'd rather write the script).
2. /diy-yt-creator:phase0-ingest-recording <slug> <path-to-recording>
     -> copies recording into videos/<slug>/source/, extracts audio,
        transcribes to source/transcript.json + source/transcript.md
3. /diy-yt-creator:phase2-script-from-transcript <slug>
     -> applies minimal-edit rules (strip fillers, fix flubs, heteronym audit)
     -> writes videos/<slug>/script.txt with preserved pacing
4. You review script.txt and lightly tweak wording (NEVER restructure).
5. npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav ...
     OR scripts/elevenlabs-tts.py per your .env config
6. /diy-yt-creator:phase-sync-check <slug>
     -> aligns source transcript vs new TTS transcript at sentence boundaries
     -> prints per-sentence drift; flags any > +/-0.8s
7. Operator builds the composition (this template) and wires the <video>.
8. Lint -> preview -> render.
```

The full playbook codifies steps 1-8 end-to-end. Use it via `/diy-yt-creator new screencap-dubbed video <slug>` or invoke the playbook directly.

## What this template ships

A self-contained ~115-second demo composition (`index.html`) with **3 scenes**:

| File | Pattern | Use for |
|---|---|---|
| `compositions/scene-title.html` | overline + 96px headline + mono subline | 4-5s opener — kicker tag, video title, one-line preview |
| `compositions/scene-screencap.html` | full-bleed `<video>` slot + optional step-callout pills | The screen recording — operator wires their MP4 here |
| `compositions/scene-cta.html` | debate question + comment pill + subscribe pulse + next-video card | Closing CTA (10s) with the mandatory engagement question |

The root composition (`index.html`) orchestrates: ambient + 10 drifting shapes + corner watermark + bottom progress bar + 2 crossfades between the 3 scenes. Narration `<audio>` and per-cue SFX are commented-out blocks the operator uncomments and tunes.

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="my-website-signup-walkthrough"

# 2. Copy the template
cp -r templates/long-form/screencap-dubbed videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-website-signup-walkthrough",
#      "name": "How to Sign Up for X — Walkthrough"
#    }

# 4. Drop your screen recording at:
#      videos/$SLUG/assets/clips/recording.mp4
#    Native 1920x1080 is best; other aspects letterbox via object-fit:contain.

# 5. Generate your narration audio (after running phase0 -> phase2 of the playbook):
#      videos/$SLUG/audio/narration.wav

# 6. Edit videos/$SLUG/index.html:
#    - Bump #root data-duration and the const TOTAL_DURATION to your recording's
#      length + 5s (title bookend) + 10s (cta bookend)
#    - Update the screencap data-start, the cta data-start, and the scene labels
#      in tl.addLabel(...) accordingly
#    - Uncomment the <audio id="narration"> block and set data-duration to your
#      narration's actual length

# 7. Edit compositions/scene-screencap.html — REPLACE the placeholder div with
#    the <video> snippet below ("Wiring your screen recording")

# 8. Edit compositions/scene-title.html and compositions/scene-cta.html
#    with your real video title + debate question

# 9. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG
npx hyperframes inspect videos/$SLUG

# 10. Preview
npx hyperframes preview videos/$SLUG

# 11. Render (operator triggers manually)
npx hyperframes render videos/$SLUG --quality high --workers 4 -o videos/$SLUG/out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/long-form/screencap-dubbed videos/$SLUG`.

## Wiring your screen recording

When you drop your recording at `assets/clips/recording.mp4`, open `compositions/scene-screencap.html` and **replace the entire `<div id="screencap-placeholder">...</div>` block** with this snippet:

```html
<video src="assets/clips/recording.mp4"
       muted
       playsinline
       preload="auto"
       style="width:100%; height:100%; object-fit:contain; background:#000;"></video>
```

Hard rules — both non-negotiable:

1. **`muted` is mandatory.** The original audio (your voice as you recorded) MUST NOT play. The TTS dub on the root composition's `<audio>` element replaces it. Without `muted`, both tracks overlap AND the browser blocks autoplay.
2. **NO `class="clip"`, NO `data-*` attributes on the `<video>` itself.** The scene wrapper in `index.html` owns timing. The `<video>` is a plain media tag — the framework starts it when the scene becomes visible.

If your recording has audio you DO want (a system sound, an alert tone, a notification chime), extract it to a different filename and add it as a separate `<audio>` element — same pattern as `../standard`'s embedded-video block. But for the typical "I narrated while screencasting" case, the original audio is exactly what you're replacing — leave it muted.

## Wiring the narration audio

After you generate `audio/narration.wav` (typically at `data-start = 4.5` so it begins when the title bookend ends), uncomment this block in `index.html`:

```html
<audio id="narration"
       src="audio/narration.wav"
       data-start="4.5"
       data-duration="100"
       data-track-index="2"
       data-volume="1"></audio>
```

Tune `data-duration` to your actual narration length. NEVER put `class="clip"` on `<audio>`.

## Recording tips that make the dub workflow easier

1. **Record at 1920x1080 native.** Other aspects letterbox via `object-fit: contain` — fine, but you lose canvas to bars. 1080p screen recording is the sweet spot.
2. **Move your cursor deliberately.** The AI voice is steady; jerky cursor motion reads as unprofessional. Hover before clicking. Pause briefly after each action.
3. **Speak in complete sentences.** The script-from-transcript phase strips fillers but won't restructure broken sentences. "Okay so um, like, what we're going to do, basically..." becomes garbage. "Okay. First, we'll click the signup button." is gold.
4. **Pause between major steps.** A 1-2s silent gap between actions gives the transcript natural sentence boundaries — and gives the dub a place to breathe.
5. **Don't read on-screen text aloud.** The viewer can read. Saying "and I'm clicking the green Submit button" while clicking it is redundant — explain WHY instead: "this submits the form and triggers the verification email."
6. **Verify before recording the real take.** Do a 60-second test recording, run it through phase0 + phase2 + tts + phase-sync-check, and watch the result. Catching pacing problems on a 60s test is free; catching them on a 10-minute master is painful.

## Recording's audio is your timing scaffold

The whole sync premise: TTS spoken at the same WPM as you recorded ~= same sentence durations ~= no manual time-warping needed. The `phase-sync-check` command verifies this. If drift exceeds +/-0.8s per sentence, the most common cause is **over-editing the script** — adding/removing too many words. The minimal-edit rules in `phase2-script-from-transcript` exist specifically to prevent this. Follow them.

## Logos — use real ones

The template ships with `assets/anthropic-logo-light.svg` as the corner watermark. Swap per video:

```bash
cp shared/logos/<brand>-logo-light.svg videos/<slug>/assets/
# Then in videos/<slug>/index.html, point #corner-watermark img src at the new file:
#   <img src="assets/<brand>-logo-light.svg" alt="<Brand>" />
```

Use `*-light.svg` or `*-light.png` only — `*-dark` variants are invisible during the title and CTA bookends (the screencap scene covers the chrome anyway, so the watermark is the only persistent brand cue).

## Expected lint warnings on the bare template

Before you wire your recording, the bare template lints **0 errors, 0 warnings**. After spawning a video, you may see:

- `audio_src_not_found` — until you uncomment + drop `audio/narration.wav`.
- `404 loading assets/clips/recording.mp4` — until you drop the recording. Note: this is a **warning**, not an error, because the placeholder slate has no live `<video>` element pointing at the missing file. Once you wire the real `<video>` snippet, the warning disappears as soon as the file exists.

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The screencap-specific big ones:

- **Don't restructure the script after transcription.** Minimal edits only. Re-record if the script needs surgery.
- **Don't leave the `<video>` un-`muted`.** Both audio tracks overlap.
- **Don't render before replacing the placeholder slate.** The bare template has no live `<video>` — the placeholder must be swapped for a real one.
- **Don't add a bg-music bed without thinking.** UI clicks in the recording will muddy it. If you really want music, mute the original recording's audio at the ffmpeg level first.
- **Don't skip phase-sync-check.** A 0.8s drift you ignored at preview becomes obvious on a 5-minute render.
