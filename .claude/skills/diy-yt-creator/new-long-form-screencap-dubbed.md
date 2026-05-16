# new-long-form-screencap-dubbed — Playbook

End-to-end pipeline that turns a **screen recording with the user's own voice** into a previewable HyperFrames horizontal long-form video (1920x1080, 30fps, 1-15 minutes) using the [`templates/long-form/screencap-dubbed/`](../../../templates/long-form/screencap-dubbed/) template. The user's voice is **replaced** by an AI-generated dub of their own transcribed words — preserving natural pacing and per-action sync without keeping their real voice in the published output.

This playbook is the **recording-driven entry path** to the diy-yt-creator pipeline. The other long-form playbooks (`new-long-form-standard`, `new-claude-code-version-longform`, `new-hostinger-sponsored`) start from a **topic prompt** and synthesize visuals. This one starts from an **existing screen recording** and dubs over it. Use this when:

- The video centers on a real screen interaction (signup flow, app demo, settings tour) that's hard to fake with synthetic visuals.
- You don't want your real voice in the published output.
- You can record once with your natural narration as a **timing scaffold** — we transcribe it, lightly clean it, and dub it.

If the video can be done with synthetic visuals, use `new-long-form-standard.md` — it's more flexible. If you want screen footage + your real voice, use `new-long-form-standard.md` with `scene-video-embed.html`.

## The dub workflow at a glance

```
1. You record your screen + voice once (your real voice as natural pacing scaffold)
2. phase0-ingest-recording  -> source/{recording.mp4, recording.wav, transcript.json, transcript.md}
3. phase2-script-from-transcript  -> script.txt with minimal edits (preserves pacing)
4. You review script.txt (optional, light tweaks only)
5. hyperframes tts  -> audio/narration.wav (AI voice, your words, your pacing)
6. hyperframes transcribe  -> transcript.json (word-level timestamps for the NEW audio)
7. phase-sync-check  -> per-sentence drift report; flag >+/-0.8s
8. Composition build: spawn template, wire <video> + <audio>, title, CTA debate question
9. Lint -> preview -> youtube-description -> stop (operator triggers render)
```

The pipeline preserves cadence because the **same person spoke the same words at the same pace**, just twice — once as the recording scaffold, once via TTS. The dub matches the recording within `~5-10%` per sentence in typical cases, well under the +/-0.8s threshold.

## Inputs

User provides ONE of:

- A path to a **screen recording with their voice narrating** (preferred — the recording's own audio drives both the timing scaffold and the script).
- A path to a **silent screen recording** + a separately-written narration draft. Phase 0 still transcribes the (silent) audio to get duration, but Phase 2 takes the script from the user's text instead of the transcript. Sync drift will be larger in this case — operator should still run `phase-sync-check` and use the segment-warp escape hatch if needed.

If the user provides neither — STOP and ask for the recording path. Don't try to synthesize content from a topic; that's `new-long-form-standard.md`'s job.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with:

- `source/recording.mp4` — operator's original screen recording (preserved as-is)
- `source/recording.wav` — extracted mono 16kHz audio for Whisper
- `source/transcript.json` — word-level timestamps from the recording (scaffold)
- `source/transcript.md` — human-readable transcript with sentence-line markers
- `script.txt` — minimally-edited narration for TTS (preserved pacing)
- `audio/narration.wav` — TTS dub of `script.txt`
- `transcript.json` — word-level timestamps for the NEW TTS audio
- `assets/clips/recording.mp4` — copy of source recording wired into the composition
- `index.html` — root composition timed to recording length
- `compositions/scene-{title,screencap,cta}.html` — filled with real content
- `youtube-description.md` — keyword-front-loaded description with chapters + debate CTA
- Preview studio open at the URL printed by `hyperframes preview`

The user runs render themselves: `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4`.

---

## Steps

### 1. Confirm slug + title + recording path

Derive a kebab-case slug (3-6 words, no stopwords) from the recording's topic.

- "Walking through Hostinger signup" → `hostinger-signup-walkthrough`
- "How to add a connector to Claude" → `add-connector-to-claude`
- "Replit deploy in 3 minutes" → `replit-deploy-in-3-minutes`

Confirm in one line: _"Spawning `videos/<slug>/` from the screencap-dubbed template, ingesting `<recording-path>`. Title: '<title>'. Proceed?"_ Skip if the user already gave you both.

### 2. Copy the template

```bash
cp -r templates/long-form/screencap-dubbed videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/long-form/screencap-dubbed videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `README.md`, `tokens/long-form.css`, `compositions/scene-{title,screencap,cta}.html`, `audio/.gitkeep`, `assets/{shapes,clips,screenshots,sfx}` should all exist.

### 3. Update meta.json

```json
{
  "id": "<slug>",
  "name": "<Title Case Name>"
}
```

### 4. Ingest the recording (Phase 0)

```
/diy-yt-creator:phase0-ingest-recording <slug> <path-to-recording>
```

Phase 0 will:

1. Copy the recording into `videos/<slug>/source/recording.mp4` (preserving original)
2. ALSO copy into `videos/<slug>/assets/clips/recording.mp4` (the composition reads from here)
3. Extract audio to `source/recording.wav` (mono, 16kHz, PCM — Whisper-ready)
4. Run `npx hyperframes transcribe source/recording.wav -d source/` -> writes `source/transcript.json`
5. Render a human-readable `source/transcript.md` with sentence-line markers and timestamps
6. Probe duration, FPS, and dimensions; report:
   - Recording duration: `XX min YY s`
   - Resolution / FPS / aspect
   - Words transcribed: `N`
   - Spoken word rate: `M WPM`
   - Sentence count (approx)

If the recording is silent (operator used a separate-script branch), Phase 0 skips transcription and reports only duration + dimensions. The operator's script will be provided in Step 6 instead.

### 5. (Optional) Sanity-check the transcript

Read `videos/<slug>/source/transcript.md` and skim for:

- Tech terms that got mangled by Whisper (e.g. `kubectl` rendered as `kube control`) — these get patched in Phase 2's heteronym/tech-term audit. Just note them.
- Filler-word density: if `um` / `uh` / `like` appear more than ~20 times in a 5-minute transcript, that's heavy editing territory — re-recording with cleaner narration may be faster than editing.
- Obvious flubs (re-started sentences, "let me try that again") — Phase 2 strips these; just verify they exist as expected.

### 6. Generate the script (Phase 2)

```
/diy-yt-creator:phase2-script-from-transcript <slug>
```

Phase 2 reads `source/transcript.json`, applies minimal-edit rules:

- **Strip fillers**: `um`, `uh`, repeated `like`, false starts, "let me try that again"
- **Fix obvious flubs**: misspoken words where context makes the intended word clear
- **Heteronym audit** per [`.claude/rules/tts-pronunciation.md`](../../rules/tts-pronunciation.md): `live` (adj) → `available`, `lead` (n) → `primary`, etc.
- **Tech-term spellings**: `nginx` → `engine-x`, `kubectl` → `cube-C-T-L`, `jq` → `jay-queue`, etc.
- **PRESERVE word count and sentence structure**: do NOT add new sentences, reorder paragraphs, or rewrite for "flow". Edits should land at <= 15% word-count delta vs source. Phase 2 reports the delta and stops if it exceeds 15%.

Output: `videos/<slug>/script.txt` (flat narration, one paragraph per natural pause in the recording).

If the user provided a separately-written script instead (silent-recording branch), Phase 2 just lints their script.txt against the heteronym + tech-term rules and writes it through verbatim.

### 6.5. (Optional) Light user review

Tell the user:
> "Script written to `videos/<slug>/script.txt`. Word count: NEW vs SOURCE (delta: X%). Review and lightly tweak wording — but do NOT restructure or add new sentences. The dub's sync depends on word-count parity with the recording. Run `/diy-yt-creator:phase-sync-check <slug>` after TTS to verify drift stays within +/-0.8s per sentence."

If the user wants major content changes, recommend re-recording instead of rewriting.

### 7. Generate TTS

Use the existing project pipeline — voice + speed already configured in `.env`:

```bash
npx hyperframes tts videos/<slug>/script.txt \
  -o videos/<slug>/audio/narration.wav
```

OR if the project uses ElevenLabs (per `.env`):

```bash
python scripts/elevenlabs-tts.py videos/<slug>/script.txt \
  -o videos/<slug>/audio/narration.wav
```

The TTS-generation step does NOT need a voice picker for this playbook — the user's `.env` is the source of truth (locked per their feedback memory). If the script is long (5+ minutes), the TTS API may chunk it; verify the output `.wav` is a single contiguous file with no gaps before proceeding.

### 8. Transcribe the new TTS

```bash
npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
```

Writes `videos/<slug>/transcript.json` (the NEW transcript, separate from `source/transcript.json`). For 5-15min long-form, prefer `-m medium.en` for accuracy.

### 9. Sync-check (Phase sync-check)

```
/diy-yt-creator:phase-sync-check <slug>
```

The sync-check command aligns `source/transcript.json` vs `transcript.json` at sentence boundaries, computes per-sentence drift, prints a table, and flags any drift > +/-0.8s. It also computes the **net duration delta**:

- If TTS is uniformly shorter/longer (e.g. all sentences are 8% shorter): regenerate TTS at adjusted speed (`-s 0.96` if too fast, `-s 1.04` if too slow).
- If drift varies by sentence (some +0.5s, some -0.4s): drift is within tolerance for the natural-sync approach; ship it.
- If 2+ sentences exceed +/-0.8s and the issue isn't uniform: invoke the **Tier 2 segment-warp escape hatch** (Step 9a below).

### 9a. (Escape hatch — Tier 2) Segment-warp the recording

Use only when Phase sync-check reports > 1 sentence at > +/-0.8s drift after a clean Phase 2 pass. Two paths:

**Path A — speed-adjust the entire narration to match recording total duration:**

```bash
# Net delta is e.g. -3s (TTS is 3s shorter than recording over 100s)
SPEED=$(python -c "print(100 / 103)")   # 0.971
ffmpeg -y -i videos/<slug>/audio/narration.wav \
  -filter:a "atempo=$SPEED" \
  videos/<slug>/audio/narration-adjusted.wav

# Then re-transcribe and re-run sync-check
```

**Path B — per-segment time-warp the video to match TTS:**

For each sentence boundary where drift exceeds tolerance, split the recording at that boundary and `setpts` the segment to fit the TTS duration. This is heavier — only invoke when Path A doesn't resolve the drift. The `phase-sync-check` command emits the per-segment ffmpeg commands when in `--emit-segment-warp` mode; copy them, run them, verify, and update `assets/clips/recording.mp4` with the warped file.

Per [`.claude/rules/video-speedup.md`](../../rules/video-speedup.md), `setpts` + `atempo` are the only acceptable mechanisms — never re-TTS at a different speed mid-video, never re-record.

### 10. Build the composition

Always invoke `/hyperframes` before this step. Edit each file:

#### 10a. `index.html` — root timing

1. Read `transcript.json` for the new TTS audio. The narration's total duration = last word's `end` time.
2. Compute composition timing:
   - Title bookend: `0` → `4.5` (5s default; narration starts at 4.5)
   - Screencap: `4.5` → `4.5 + narration_duration + 0.5` (0.5s tail after last word)
   - CTA: `screencap_end` → `screencap_end + 10` (10s CTA)
   - Total: `cta_end + 0.5` (0.5s tail-hold)
3. Update in `index.html`:
   - `<div id="root">` `data-duration` → computed total
   - `const TOTAL_DURATION = ...` → computed total
   - `#scene-screencap-wrap` `data-start` → 4.5 (unchanged)
   - `#scene-cta-wrap` `data-start` → computed screencap_end
   - `tl.addLabel("screencap", 4.5)` and `tl.addLabel("cta", screencap_end)` → match
4. Uncomment the `<audio id="narration">` block and set `data-duration` to `narration_duration`.

#### 10b. `compositions/scene-screencap.html` — wire the recording

Replace the entire `<div id="screencap-placeholder">...</div>` block with the live `<video>` snippet from the template's README ("Wiring your screen recording"):

```html
<video src="assets/clips/recording.mp4"
       muted
       playsinline
       preload="auto"
       style="width:100%; height:100%; object-fit:contain; background:#000;"></video>
```

Hard rules:
- `muted` is mandatory (the original voice MUST NOT play; TTS replaces it)
- NO `class="clip"` and NO `data-*` attributes on the `<video>` itself — the scene wrapper in `index.html` owns timing

#### 10c. `compositions/scene-title.html` — title card

Replace placeholder text in `#title-overline`, `#title-headline`, `#title-subline` with:
- Overline: a kicker tag (e.g. `WALKTHROUGH`, `STEP-BY-STEP`, `LIVE DEMO`)
- Headline: the actual video title (matches `meta.json` name, fits in 1500px at 96px font)
- Subline: a 1-line preview of what the video covers (~60 chars)

#### 10d. `compositions/scene-cta.html` — debate CTA

Mandatory per [`.claude/rules/engagement-cta.md`](../../rules/engagement-cta.md):
- `#cta-debate` — the polarizing, binary-answerable question that matches the script's final spoken line
- `#cta-comment` — comment-prompt pill (keep "Drop your take in the comments" or similar)
- `#cta-subscribe` — subscribe pill (orange pulse glow already wired, finite repeat:4)
- `#cta-next-card` — wire a real next-video thumbnail at `assets/screenshots/next-video-thumbnail.png` (the template ships a placeholder)

#### 10e. (Optional) Step-callout pills

For long screencaps (5+ minutes), consider adding `step-pill` callouts at major action moments to help the viewer track progress. Clone `#step-pill-example` per step, position appropriately (the default is bottom-left), and add reveal tweens anchored to TTS word timestamps:

```js
// Inside scene-screencap.html's <script> block
const transcript = /* loaded transcript.json */;
tl.from("#step-pill-1", { y: 24, opacity: 0, duration: 0.5,
                          ease: "back.out(1.4)",
                          immediateRender: false },
        transcript.words.find(w => w.text === "first").start);
```

Keep callouts to <= 1 per ~15s of screencap. Every callout fights for attention against the real screen content.

### 11. Lint + validate + inspect

```bash
npx hyperframes lint    videos/<slug>     # 0 errors required
npx hyperframes validate videos/<slug>     # WCAG audit
npx hyperframes inspect videos/<slug>      # layout overflow at 1920x1080
```

Common screencap-dubbed errors:

| Error | Likely cause | Fix |
|---|---|---|
| `media_missing_id` on `<video>` | Wired live `<video>` without `id` attribute | Add `id="screencap-clip"` |
| `audio_src_not_found` | Uncommented `<audio>` but missing file | Drop `audio/narration.wav` OR re-comment |
| `duplicate_media_discovery_risk` | Wrote a literal `src="..."` inside an HTML comment | Use prose ("operator wires the video element") |
| `[FrameCapture] video metadata not ready` (render only) | `<video>` points at missing file | Drop `assets/clips/recording.mp4` OR keep placeholder slate |
| `composition duration shorter than narration` | `tl.set({}, {}, TOTAL_DURATION)` value mismatched the actual narration duration | Recompute per step 10a |

### 12. Preview

```bash
npx hyperframes preview videos/<slug>
```

(Run in background.) Capture the URL. Verify:
- Title scene reads cleanly for ~4.5s
- Screencap scene plays the muted recording with TTS narration in sync
- CTA scene shows the debate question + subscribe pulse + next-video card
- Corner watermark stays visible throughout
- Progress bar fills linearly from 0 to 1920 across the full composition

### 12.5. (Optional) QA the rendered preview visually

`/diy-yt-creator:qa-composition <slug>` — snapshots each phase and reports visual regressions. Recommended for any video over 3 minutes.

### 13. Generate YouTube description (MANDATORY — never skip)

Canonical rule: [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md).

1. **vidIQ keyword research first** — call `mcp__claude_ai_vidiq__vidiq_keyword_research`, `vidiq_outliers`, and `vidiq_trending_videos` for 3-5 topic seeds from the recording's content. Save to `videos/<slug>/research/vidiq-keywords.md`.
2. **Compute chapter timestamps** from the screencap scene's TTS-anchored step-callouts (if used) or sentence boundaries in `transcript.json`. Format `M:SS`. Aim for 4-8 chapters for a 5-15min video, gap >= 30s.
3. **Write `videos/<slug>/youtube-description.md`** — LEAN structure per the rule: keyword-front-loaded SEO hook -> Dynamous block in `----` separators -> `Chapters` header + chapter list (long-form has chapters) -> Resources: (validated URLs) -> Hostinger affiliate block in `----` separators (MANDATORY: `🏠 Self-host your AI agents & projects on Hostinger (10% OFF): 👉 https://hostinger.com/DIYSMARTCODE`) -> debate question matching the script's final spoken line -> 15-25 hashtags. **NO Key Changes / Key Concepts / Key Stats / Key Facts / Key sections bullet blocks — explicitly cut.**
4. **Validate every URL** with `WebFetch`. Keep total description under ~3000 chars.

### 14. Report to the user

One concise message:

- **Slug + path**: `videos/<slug>/`
- **Recording duration**: `XX min YY s`
- **TTS narration duration**: `XX min YY s` (delta vs recording: `+/-X.Xs`)
- **Sync-check verdict**: `clean` / `regenerate at speed X` / `segment-warp recommended`
- **Total composition duration**: `XX min YY s`
- **Preview URL**: `http://localhost:5173`
- **Render command** (do NOT run): `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4`
- **YouTube description**: `videos/<slug>/youtube-description.md` (paste-ready)

Stop. Wait for user iteration or manual render.

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` -> 0 errors
- [ ] `npx hyperframes validate videos/<slug>` -> no AA failures on headlines
- [ ] `npx hyperframes inspect videos/<slug>` -> no overflow on title / CTA
- [ ] `phase-sync-check` reports either `clean` OR drift is documented + accepted
- [ ] `<video>` element is `muted` and has no `class="clip"` / `data-*` attributes
- [ ] `<audio id="narration">` is uncommented with correct `data-duration`
- [ ] Title scene shows real video title (not "REPLACE: video title goes here")
- [ ] CTA scene's `#cta-debate` is a polarizing binary-answerable question that matches the script's final spoken line
- [ ] Corner watermark logo is brand-appropriate (swapped from default Anthropic logo if needed)
- [ ] `youtube-description.md` exists and the closing paragraph contains the same debate question
- [ ] Preview URL is reachable

If any item fails, fix it before reporting.

---

## Don'ts

All standard long-form don'ts apply. Screencap-dubbed-specific additions:

- **Never restructure the script after transcription.** The whole sync premise rests on the AI voice having ~the same pacing as the original recording. Strip filler words, fix flubs, apply heteronym audit — but never add new sentences, reorder paragraphs, or rewrite for "flow." If the script needs surgery, re-record instead.
- **Never leave the `<video>` un-`muted`.** Both audio tracks will play and the dub becomes useless.
- **Never put a live media tag inside an HTML comment.** Lint reports `duplicate_media_discovery_risk`. Use prose in comments.
- **Never auto-trim or auto-stretch the recording blindly.** If drift is uniform, regenerate TTS at adjusted speed first. Segment-warp is a Tier 2 fallback, not the default.
- **Never render with the placeholder slate still in place.** The bare template's `<div id="screencap-placeholder">` must be replaced with the real `<video>` snippet before render.
- **Never add bg-music without verifying the recording is truly silent.** UI clicks captured by the screen recorder will muddy a music bed. If you really want music, ffmpeg-mute the recording's audio first AND don't trust the result without listening to it.
- **Never run `new-long-form-screencap-dubbed` and `new-long-form-standard` against the same slug** — pick one playbook per video.
- **Never auto-render.** Long-form renders take 3-15 minutes; the user always triggers them manually.
