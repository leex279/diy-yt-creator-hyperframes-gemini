# use-cloned-voice — Playbook

Switch any video from a stock ElevenLabs voice to the user's cloned voice,
re-generate narration, rebuild `transcript.json`, re-wire scene timing in
`index.html`, and re-render — without touching the script or compositions.

---

## When to invoke

- "use my voice" / "switch to my voice" / "record with my voice"
- "migrate `<slug>` to my voice"
- "regenerate narration with cloned voice"
- Any time `ELEVENLABS_VOICE_ID` in `.env` needs to point at a different voice

---

## Prerequisites

Confirm the video slug and whether it is long-form (1920×1080) or Shorts (1080×1920).
`.env` is already configured with the correct voice and all settings — do not ask about it, do not read it, do not modify it. The Python script reads it automatically.

---

## Step 1 — Regenerate narration

```powershell
# Long-form (1920×1080)
python scripts/elevenlabs-tts.py videos/<slug> --force

# Shorts (1080×1920)
python scripts/elevenlabs-tts.py videos/<slug> --force --shorts
```

`--force` regenerates every chunk regardless of the old `transcript-history.json`.
Required when changing voice ID; without it, unchanged chunks would be reused
from the previous voice's cache.

This writes:
- `videos/<slug>/audio/narration.wav` — new audio with cloned voice
- `videos/<slug>/transcript.json` — word-level timestamps for the new audio
- `videos/<slug>/audio/narration-chunks/` — per-chunk WAVs (delta regen cache)
- `videos/<slug>/transcript-history.json` — chunk hashes (future reruns skip unchanged chunks)

**Duration shift:** a cloned voice almost always produces slightly different
total narration length than the stock voice — even at the same speed setting.
Expect ± 5-15 seconds. This is normal and handled in Step 3.

---

## Step 3 — Re-wire scene timing in `index.html`

The transcript timestamps changed; every scene's `data-start`, the total
`data-duration` on `#root`, the `TOTAL_DURATION` const, and the crossfade
label times must all be recomputed.

### 3a — Extract scene boundary words from `script.txt`

For each `[SCENE: name]` marker in `script.txt`, note the **first 2-3 words
of the paragraph that follows it**. These are the anchor words you will look
up in `transcript.json`.

Example for `claude-code-v2126`:

| Scene | First words after marker |
|---|---|
| `stats-opener` | "Seven new features" |
| `feature-cards` | "Six changes that" |
| `detail-auth` | "Auth and sessions" |
| *(etc.)* | *(first words of each scene's opening line)* |

The first scene always starts at `data-start="0"` — no lookup needed.

### 3b — Look up timestamps in `transcript.json`

Read `videos/<slug>/transcript.json`. Each entry is:
```json
{ "word": "Seven", "start": 0.12, "end": 0.45 }
```

Find the first anchor word for each scene (matched in order — the N-th
occurrence if the word appears multiple times). Use the **`.start`** value
of the anchor word as the new `data-start`, rounded down to 2 decimal places.

**Total duration** = last entry's `.end` value, ceil'd to the nearest whole
second + 1s buffer.

### 3c — Update `index.html`

Four things to update:

1. **Each scene wrapper `data-start`** — replace old timestamps with the new
   ones from the lookup above.
   ```html
   <!-- old: data-start="38" -->
   <div class="scene-wrapper clip" id="scene-feature-cards"
        data-start="41.2" data-track-index="1">
   ```

2. **`#root` `data-duration`** — set to the new total duration.
   ```html
   <div id="root" class="clip" data-start="0" data-duration="197">
   ```

3. **`TOTAL_DURATION` const** — update the JS const in the `<script>` tag.
   ```js
   const TOTAL_DURATION = 197;
   ```

4. **`tl.addLabel` / `crossfadeScenes` calls** — each crossfade call takes the
   same time value as the corresponding scene's new `data-start`. Update every
   label + crossfade pair to match.
   ```js
   // old: tl.addLabel('feature-cards', 38); crossfadeScenes('stats-opener', 'feature-cards', 38);
   tl.addLabel('feature-cards', 41.2);
   crossfadeScenes('stats-opener', 'feature-cards', 41.2);
   ```

**What NOT to change in `index.html`:**
- Internal GSAP triggers inside each sub-composition (`compositions/scene-*.html`) —
  these are handled in the mandatory Step 3.5 below.

---

## Step 3.5 — Retime internal GSAP triggers in each `scene-*.html` (MANDATORY)

**This step is the most common source of "slides faster/slower than audio" bugs.**
Every scene sub-composition contains GSAP animation triggers timed to word-level
timestamps from the OLD voice. Card entrances, phase transitions, flash effects,
and closing banners all fire at specific `at:` values that are now stale. Slot
anchors (`tl.set({}, {}, N)`) are also stale because scene durations changed.

Skipping this step will cause every visual cue inside a scene to fire at the wrong
moment relative to what the narrator is actually saying.

### 3.5a — Read timing comments in each `scene-*.html`

Every scene composition has a timing comment block at the top of its `<script>`:
```js
// cloned-voice timing. scene_t = root_t - <data_start> (data-start <data_start>). Slot <N>s.
// Narration (internal = global - <data_start>):
//   "First anchor phrase"   scene_t X.XX  (#word_idx word, global G.GG)
//   ...
```

The `scene_t` value is the **internal** time the GSAP trigger must fire —
`internal_t = global_t - scene_data_start`.

### 3.5b — Look up new global timestamps in `transcript.json`

For each narration anchor phrase in the timing comment, find the **first word**
of that phrase in `transcript.json` and read its `.start` value.

**Method:** use `grep` or a small Python snippet:
```python
import json
words = json.load(open('videos/<slug>/transcript.json'))
for i, w in enumerate(words):
    print(f'{i:3d}  {w["start"]:8.3f}  {w["word"]}')
```

Then scan for the anchor word by index or text match.

### 3.5c — Compute new internal trigger times

For each anchor:
```
internal_t = global_t - scene_data_start   (use the data-start from Step 3)
```

Round to 2 decimal places. Triggers that are relative offsets from another
trigger (e.g. `textContent set = phase_pivot + 0.46`) keep their relative
offset but anchor to the new base time.

### 3.5d — Update each `scene-*.html`

For each scene, update:
1. **Timing comment block** — replace old `data-start`, `slot`, and per-anchor
   values with new ones. Update the word indices and global times too.
2. **All `at:` values in card arrays** — replace old times with new internal times.
3. **All standalone `tl.to/fromTo/set` time arguments** — phase transitions,
   flash effects, closing banners, anything driven by a narration cue.
4. **`last_next` references** — `const next = … ? … : OLD_TIME` where `OLD_TIME`
   was the last card's dwell reference. Update to the new closing-banner time.
5. **Slot anchor** — `tl.set({}, {}, N)` must equal
   `next_scene_data_start - this_scene_data_start`. This is the scene's total
   duration from HyperFrames' perspective. Getting it wrong causes scenes to
   cut off early or show a black gap.

**Example** (stats-opener, cloned voice):
```js
// OLD (stock voice, data-start=0, slot=38):
{ sel: "#so-card-1", at: 12.94 },   // "First:" spoken at 12.94 old voice
tl.set({}, {}, 38);

// NEW (cloned voice, data-start=0, slot=45.43):
{ sel: "#so-card-1", at: 14.50 },   // "First:" now at global 14.500
tl.set({}, {}, 45.43);
```

### 3.5e — Phase transitions that lead into card entrances

If a scene has a phase crossfade that fires N seconds *before* the first card:
```js
// Phase 1 → Phase 2 crossfade before "Run…" @ 3.30
tl.to("#fc-phase1", { opacity: 0 }, 2.80);   // 0.50s lead-in
tl.to("#fc-phase2", { opacity: 1 }, 2.80);
```
Keep the same lead-in offset (0.50s here) but anchor it to the new card-1 time:
`phase_transition_t = new_card1_t - 0.50`

---

## Step 4 — Audit SFX alignment

**This step is mandatory.** SFX `data-start` values are pinned to specific
word timestamps in the old transcript. After re-TTS, the same words land at
different times — every SFX element now drifts.

In `index.html` (and any `compositions/scene-*.html` that contains `<audio>`
elements), list every `<audio id="sfx-*">`. For each:

1. Note the word or visual event it's cued to.
2. Find that event's new timestamp in the updated `transcript.json`.
3. Update `data-start` to match (or within 0.05s for percussive cues;
   within 0.15s for ambient/whoosh cues).

Per the [audio-design rules](./../../../.claude/rules/audio-design.md):
- Drift > 0.15s on any SFX = bug.
- Percussive cues (`impact-slam`, `scale-slam`, `screen-shake`) must be
  within 0.05s.

---

## Step 5 — Lint

```powershell
npx hyperframes lint videos/<slug>
```

Must pass with 0 errors before rendering. Fix any `overlapping_gsap_tweens`
errors first — these usually mean a crossfade time was left at an old value
that now overlaps a neighboring scene.

---

## Step 6 — Re-render

```powershell
npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4
```

The rendered MP4 will be slightly different in length than the previous render.
If post-speedup was applied via ffmpeg, re-apply it after the new render (same
factor, same command from [`.claude/rules/video-speedup.md`](../../rules/video-speedup.md)).

Update `videos/<slug>/youtube-description.md` chapter timestamps if the scene
boundaries shifted by more than ~3 seconds.

---

## Common mistakes to avoid

| Mistake | Why it breaks |
|---|---|
| Skipping Step 3.5 (internal GSAP retiming) | "Slides faster/slower than audio" — cards appear before/after the narrator says their cue word, every visual trigger in every scene is wrong |
| Using `--force` on only some chunks | Old-voice cached chunks get mixed into the new narration — audible discontinuities |
| Forgetting to update crossfade label times | GSAP throws `label not found` or scenes fade at wrong time |
| Not re-auditing SFX after re-TTS | SFX fires mid-sentence instead of on the visual trigger |
| Adjusting `ELEVENLABS_SPEED` in `.env` to fix pacing | Use ffmpeg post-process instead — re-TTS at a different speed invalidates every `data-start` again |
| Only updating slot anchors without re-anchoring `at:` triggers | Slots correct, but animations still fire at stale word timestamps |

---

## Verification checklist

- [ ] `audio/narration.wav` regenerated
- [ ] `transcript.json` updated (check timestamps — if identical to before,
  TTS pulled from cache; re-run with `--force`)
- [ ] All scene `data-start` values in `index.html` updated
- [ ] `data-duration` on `#root` updated
- [ ] `TOTAL_DURATION` const updated
- [ ] All `tl.addLabel` / `crossfadeScenes` times updated
- [ ] **All internal GSAP triggers in each `scene-*.html` updated** (Step 3.5) —
  this is the most common source of "slides faster/slower than audio" bugs
  - [ ] Timing comment block updated (data-start ref, slot, per-anchor times + word indices)
  - [ ] All card `at:` values updated to new internal times
  - [ ] All standalone `tl.to/fromTo/set` time arguments updated
  - [ ] `last_next` reference (in `forEach`) updated
  - [ ] Slot anchor `tl.set({}, {}, N)` updated for each scene
- [ ] All `<audio id="sfx-*">` `data-start` values re-audited
- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] Rendered MP4 plays through without visible scene jump or audio gap
- [ ] YouTube description chapter timestamps updated if scene boundaries shifted
