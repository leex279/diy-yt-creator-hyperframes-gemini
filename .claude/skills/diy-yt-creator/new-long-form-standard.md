# new-long-form-standard — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames horizontal long-form video (1920x1080, 30fps, 4-15 minutes) using the canonical generic baseline at `templates/long-form/standard/`. Zero manual steps; ends at preview, never renders.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 (research → plan → script → critique → fact-check → retention strategy) and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A. Use the pipeline by default; use this skill directly only when you already have a script.

This playbook is the long-form analog of [new-anthropic-short.md](./new-anthropic-short.md). Read that file first if you haven't — most of the pipeline is identical. The deltas for long-form are:

- **Template**: `templates/long-form/standard/` (instead of `templates/shorts/anthropic/`)
- **Canvas**: 1920x1080 horizontal (instead of 1080x1920 vertical)
- **Duration**: 4-15 minutes typical (instead of 24-60s)
- **Architecture**: **sub-composition split** — each scene is an external HTML file in `compositions/scene-*.html` with its own paused timeline registered on `window.__timelines["scene-<name>"]`. The root timeline only orchestrates ambient + scene crossfades. NO phase mutex.
- **Palette**: dark navy + 4-accent rotation (blue / cyan / purple / green; orange + yellow held back for warnings + hero stats). See [`shared/lib/visual-styles/long-form-standard.md`](../../../shared/lib/visual-styles/long-form-standard.md).
- **Audio bed**: narration + **3-segment bg-music** (hook / body / cta on track 3). Shorts forbid bg-music; long-form requires it. See [`.claude/rules/audio-design.md`](../../rules/audio-design.md).
- **Captions**: a `compositions/captions.html` sub-composition is wired by default with `data-caption-root="true"`. Populate via `npx hyperframes transcribe`.
- **Embedded video**: `compositions/scene-video-embed.html` ships a placeholder slate. Operator wires the real `<video>` element when they have a clip (see template README's "Embedded video — bringing the audio in").
- **No Dynamous-promotion opt-in.** Dynamous artifacts (badge, endcard, module interstitial, discount bubble) are Shorts-shaped at 1080x1920. Long-form has its own end-screen pattern via `scene-cta` (debate question + comment pill + subscribe pulse + next-video card) and does NOT use the Dynamous wiring snippet.

## Inputs

User provides ONE of:

- A **topic / prompt** (e.g. _"Why Claude Code Skills change the game for long-form devs"_) — agent drafts the full script
- A **title + key facts** (e.g. _"Claude 4.7 launch — 1M context, 47% on SWE-bench, $5/M tokens, side-by-side vs GPT-5"_) — agent uses the facts verbatim, drafts the framing
- A **pre-written `script.txt`** — agent skips drafting (jump to step 5)

If the topic has no real source data and would require fabricated stats/dates, **stop and ask the user for a source URL** before proceeding. Never invent numbers.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with:

- `script.txt` — narration script (5-12 minutes typical)
- `audio/narration.wav` — Kokoro TTS narration (or operator-recorded)
- `audio/bg-music-{hook,body,cta}.mp3` — optional 3-segment bg-music (operator drops or sources via royalty-free)
- `transcript.json` — word-level timestamps
- `index.html` — root composition with scene timing tuned to spoken-word landmarks
- `compositions/scene-*.html` — 8 scene archetypes filled with real content
- `compositions/captions.html` — populated by `hyperframes transcribe`
- Preview studio open in the browser at the URL printed by `hyperframes preview`

The user runs render themselves: `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4`.

---

## Steps

### 1. Confirm slug + title

Derive a kebab-case slug (3-6 words, no stopwords). Examples:

- "Why Claude Code Skills change long-form" → `claude-skills-long-form-impact`
- "Anthropic vs OpenAI: 2026 Q1 deep dive" → `anthropic-vs-openai-2026-q1`
- "How Archon worktrees end branch hell" → `archon-worktrees-end-branch-hell`

Confirm in one line: _"Spawning `videos/claude-skills-long-form-impact/` — title 'How Claude Code Skills Change Long-Form'. Proceed?"_ Skip if the user already gave you both.

### 2. Copy the template

```bash
cp -r templates/long-form/standard videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/long-form/standard videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `README.md`, `tokens/long-form.css`, `compositions/scene-*.html` (× 8) + `captions.html`, `audio/`, `assets/{shapes,sfx,screenshots,clips}/` should all exist.

### 3. Update meta.json

```json
{
  "id": "<slug>",
  "name": "<Title Case Name>"
}
```

**No Dynamous-promotion question** for long-form. Skip directly to step 4.

### 4. Draft the script (or load from pipeline)

Two branches — try Branch A first.

#### Branch A — pipeline output exists (preferred)

If `videos/<slug>/scripts/full-script.md` exists (Phases 0-2b have run):

1. READ `videos/<slug>/scripts/full-script.md` as the authoritative narration source.
2. READ `videos/<slug>/plan.md` for `## Composition Layout`, `## Retention Component Picks`, `## Data Timing Budget`.
3. READ `videos/<slug>/retention-strategy.md` (if it exists from Phase 3.5) — overrides the plan's picks where they differ.
4. Map the script's `## Scene N: <name>` sections onto the template's 8 scene archetypes. Possible mappings:

   | Script scene type | Template scene file |
   |---|---|
   | Cold-open hook / hero stat | `scene-hook.html` |
   | "Here's the situation" / context | `scene-image-hero.html` |
   | Before/after / A vs B | `scene-side-by-side.html` |
   | Receipts (2 huge numbers) | `scene-stat-pill-row.html` |
   | "Where this came from" / sources | `scene-source-cards.html` |
   | Demo / product footage | `scene-video-embed.html` |
   | "How it fits together" / system view | `scene-architecture-stack.html` |
   | Closing CTA / debate question | `scene-cta.html` |

   You don't need all 8. Drop scenes you don't need by removing the wrapper `<div>` from `index.html` and removing the matching `crossfadeScenes()` call. You can also reorder scenes — just keep the data-start values monotonic and the labels in order.

5. Skip Branch B's inline drafting. Jump to step 4.5+.

If anything in the plan or retention-strategy looks wrong (missing scene mapping, unrecognized retention component), STOP and tell the user — do NOT invent.

#### Branch B — no pipeline output (legacy / quick path)

Fall back to inline drafting. For long-form, recommend running `/diy-yt-creator:full-auto <topic>` first; long-form scripts benefit much more from research than Shorts do.

If you must draft inline, structure narration into 4-8 scenes of 30-90s each. Total target: 4-12 minutes. Map each scene to one of the 8 template archetypes per the table above.

**Style rules for long-form narration:**

- Read [`.claude/references/script-library.md`](../../references/script-library.md) for examples.
- Hook earns the watch in the first 10s (vidIQ research). Pattern-interrupt every 20-30s. CTA at 60-70% mark.
- Short sentences for Kokoro TTS. No semicolons or em-dashes.
- Numbers: write digits ("3 bugs", "47% on SWE-bench").
- Long-form CAN use longer sentences than Shorts (the format breathes), but keep clauses under 15 words.

Save to `videos/<slug>/script.txt`. Use this format (one scene per blank-line block, in scene order):

```
[scene 1 — hook narration]

[scene 2 — image-hero narration]

[scene 3 — side-by-side narration]

...

[scene 8 — cta narration]
```

The blank lines are NOT spoken; they map narration to scenes.

### 4.5. (Optional) Ground the script in real source content

Same as `new-anthropic-short.md` step 4.5 — use `/agent-browser` for JS-rendered sources, `WebFetch` for static pages. Cross-check every stat / date / quote against the source.

### 5. Generate TTS

```bash
npx hyperframes tts videos/<slug>/script.txt \
  -o videos/<slug>/audio/narration.wav \
  -v am_michael \
  -s 1.0
```

Voice picker is identical to the Shorts playbook (`am_michael` default, see Shorts table for alternatives). Speed `1.0` baseline; if rushed at preview, drop to `0.95`. Long-form benefits from a slightly slower default than Shorts — try `0.95` if `1.0` feels frantic.

### 6. Transcribe for word-level sync

```bash
npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
```

Writes `videos/<slug>/transcript.json`. For long-form (5-15min), prefer `-m medium.en` — `small.en` accuracy degrades on longer clips with technical jargon.

### 7. Compute scene boundaries

Read `transcript.json`. The template's 8 scenes are wired with default `data-start` values `[0, 12, 32, 55, 70, 90, 105, 115]` (a 120s demo). Replace these with values derived from your transcript:

```
scene_starts = [0]                         // first scene always starts at 0
for n in [1..N-1]:
    scene_starts[n] = transcript[<last word of scene n-1>].end - 0.2
                                            // 0.2s lead-in for crossfade
total_duration = transcript[<last word>].end + 1.5  // 1.5s tail for CTA breathing
```

Update `index.html`:

- Each scene wrapper's `data-start` → corresponding `scene_starts[n]`
- `<div id="root">` `data-duration` → `total_duration`
- `const TOTAL_DURATION = ...` in `<script>` → `total_duration`
- `tl.set({}, {}, TOTAL_DURATION)` (the timeline pad) — uses the constant; no edit needed
- `tl.fromTo("#progress-fill", { width: 0 }, { width: 1920, duration: TOTAL_DURATION, ease: "none" }, 0)` — uses the constant; no edit needed
- Ambient breath `duration: 30` → consider scaling proportionally (`total_duration / 4` for clean yoyo cycles); not strictly required
- All 7 `crossfadeScenes()` calls — labels reference scene names, so as long as the labels in `tl.addLabel(...)` match the new scene_starts, no change needed. UPDATE the labels' time values to match scene_starts[n].

If the script uses fewer than 8 scenes, remove the matching wrapper `<div>` from `index.html` AND the corresponding `crossfadeScenes()` call AND the `addLabel()` line. The composition still lints.

### 8. Edit each `compositions/scene-*.html`

Always invoke `/hyperframes` before this step. Each scene is its own file — edit them independently.

For each scene the script uses:

1. Replace placeholder text in the inner `<div>` with the script's content for that scene.
2. The scene's GSAP timeline tweens already animate `id="<scene>-overline"`, `id="<scene>-headline"`, etc. Do NOT change ids unless you're also updating the `tl.from(...)` calls in the same file.
3. Drop matching media into `assets/screenshots/`:
   - `hero-shot.png` (1920x1080) for `scene-image-hero.html`
   - `source-{1,2,3}.png` (16:9) for `scene-source-cards.html`
   - `next-video-thumbnail.png` (16:9) for `scene-cta.html`
4. For `scene-video-embed.html`: drop your clip at `assets/clips/demo.mp4`, then replace the `<div id="vembed-placeholder">` block with the snippet from `templates/long-form/standard/README.md` "Embedded video — bringing the audio in". If you also want the clip's audio, extract it via `ffmpeg -i demo.mp4 -vn -acodec libmp3lame demo-audio.mp3` and add the sibling `<audio>` element with track-index 6.
5. Per-scene accent rotation: each scene pins one lead accent in CSS (e.g. `scene-hook` uses `--accent-warn` + `--accent-stat`). Swap to a different `--accent-N` per video if needed. Keep one lead per scene; no rainbows.

### 8a. Edit root `index.html`

1. **`<title>`** in `<head>` → the video title
2. **`<div id="root">`** `data-duration` → `total_duration`
3. **`#top-banner-logo`** `src` → copy a logo from `shared/logos/` into `videos/<slug>/assets/` first (e.g. `cp shared/logos/anthropic-logo-light.svg videos/<slug>/assets/`), then point `src="assets/<file>"`. Same hard rule as Shorts: NEVER reference `../../shared/logos/...` (preview server rejects out-of-project paths).
4. **Scene `data-start` values**: replace with `scene_starts[n]` per step 7
5. **Scene labels** in the `tl.addLabel(...)` chain: replace with `scene_starts[n]`
6. **Audio bed** — uncomment the `<audio>` block (just below `<!-- AUDIO BED ... -->`):
   - `<audio id="narration">` — `data-duration` = `total_duration`
   - `<audio id="bg-music-hook">` — `data-duration` = first scene's duration (≈ 8-12s)
   - `<audio id="bg-music-body">` — `data-start` = bg-music-hook end, `data-duration` = bridge to last scene start
   - `<audio id="bg-music-cta">` — `data-start` = last scene's data-start, `data-duration` = `total_duration - data-start`
   - Volumes: 1.0 / 0.12 / 0.07 / 0.12 — see [`.claude/rules/audio-design.md`](../../rules/audio-design.md). Lower the body volume if the user finds bg-music annoying under voice.

If the user has no bg-music yet, only uncomment narration. The bg-music elements stay commented.

### 8b. Wire SFX from `retention-strategy.md` (skip if no `sfx_cues`)

Same logic as `new-anthropic-short.md` step 8.14. Sync cues into `assets/sfx/`:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

Then add `<audio>` elements at the bottom of `index.html` (after the bg-music block). Track-index 4+ for SFX (track 2 = narration, track 3 = bg-music). Volume cap 0.25.

### 8.5. Lib pick (optional)

Read [`shared/lib/MANIFEST.md`](../../../shared/lib/MANIFEST.md) and [`shared/lib/visual-styles/long-form-standard.md`](../../../shared/lib/visual-styles/long-form-standard.md). Most of the long-form scene archetypes ship as `compositions/scene-*.html` — don't extract them to `shared/lib/blocks/` unless they get reused across 3+ long-form templates (per the plan's "Future enhancements"). For now, the canonical scene archetype source is `templates/long-form/standard/compositions/`.

**Never reference `shared/lib/` paths from `data-composition-src`, `<img src>`, `<audio src>`, `<video src>`, `<link href>`, or `<script src>`** — same hard rule as Shorts. Always copy the file into the project first.

### 9. Lint

```bash
npx hyperframes lint videos/<slug>
```

Must report `0 errors`. Common long-form-specific errors to watch for (in addition to Shorts errors):

| Error | Likely cause | Fix |
|---|---|---|
| `root_composition_missing_data_start` (sub-comp) | Edited a scene file and removed `data-start="0"` from the inner `<div data-composition-id="...">` | Add `data-start="0"` back |
| `media_missing_id` (video) | Wired the real `<video>` element without an id | Add `id="vembed-clip"` (or similar) |
| `audio_src_not_found` (bg-music) | Uncommented bg-music elements but didn't drop the `.mp3` files | Drop the files at `audio/bg-music-{hook,body,cta}.mp3` OR re-comment the elements |
| `duplicate_media_discovery_risk` (video) | `<video>` and `<audio>` point at the same `.mp4` source | Extract audio to a different filename (`demo-audio.mp3`) |
| `[FrameCapture] video metadata not ready` (render only) | `<video>` element points at missing `assets/clips/demo.mp4` | Ship the clip, OR replace the `<video>` element with the placeholder slate from the template |

Other Shorts errors apply identically — see `new-anthropic-short.md` step 9.

### 10. Validate (WCAG) and inspect (overflow)

```bash
npx hyperframes validate videos/<slug>     # WCAG audit + 404 missing-asset check
npx hyperframes inspect videos/<slug>      # layout overflow at 1920x1080
```

Common long-form overflows:

- **Hook headline at 100px wraps onto 4+ lines** — shorten the headline (it's a hook; brevity is the goal anyway).
- **Side-by-side card body overflows the card** — tighten copy or drop body font from 22px to 20px.
- **Architecture-stack layer name truncates** — the layout assumes ≤ 12-char names. Shorten or drop the meta line.
- **Source-card title runs three lines** — keep titles under 5 words / 30 chars.

WCAG warnings (small accent-on-translucent text < 18px, 4.5:1) — bump font size or use brighter accent variants per the template's existing solution (`#93C5FD`, `#67E8F9`, `#C4B5FD`).

### 11. Open preview

```bash
npx hyperframes preview videos/<slug>
```

(Run in background.) Capture the URL (typically `http://localhost:5173`).

### 11.5. (Optional) QA the rendered preview visually

Sub-playbook: `/diy-yt-creator:qa-composition <slug>`. Recommended for long-form because the 1920x1080 canvas + 8-scene flow has more places for visual regressions than a 4-phase Short.

### 12. Report to the user

One concise message containing:

- **Slug + path**: `videos/<slug>/`
- **Total duration**: `XX min YY s` (long-form is minutes, not seconds)
- **Voice + speed**: e.g. `am_michael @ 0.95`
- **Scene count**: e.g. `7 of 8 archetypes used (skipped scene-architecture-stack)`
- **Preview URL**: `http://localhost:5173`
- **Render command** (do NOT run): `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4`
- **Any inspect findings** that needed manual content tradeoffs

Stop. Wait for user iteration or manual render.

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes validate videos/<slug>` → no AAA contrast failures, no AA failures on headlines
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow on hero, source-cards, architecture, side-by-side cards
- [ ] All used scenes have real content (no leftover template placeholders: "YOUR HOOK HEADLINE", "Headline that earns the hook", "Title for option A/B", "label one/two", "Title of the first source", etc.)
- [ ] Scene `data-start` values computed from transcript, NOT left at template defaults (0/12/32/55/70/90/105/115)
- [ ] Scene labels in `tl.addLabel(...)` chain match scene `data-start` values
- [ ] Audio narration `<audio>` uncommented with correct `data-duration`
- [ ] If used: bg-music elements uncommented with correct segment timing
- [ ] If used: `<video>` element wired in `scene-video-embed.html` with id, data-start, data-duration, data-track-index
- [ ] Captions wrapper still present in `index.html` (don't remove it — `hyperframes transcribe` will populate `captions.html` automatically when run after audio is in place)
- [ ] Preview URL is reachable

If any item fails, fix it before reporting.

---

## Real logos — copy into project, don't reference shared

Identical rule to Shorts. The template ships with `assets/anthropic-logo-light.svg`. Swap per video:

```bash
cp shared/logos/<brand>-logo-light.svg videos/<slug>/assets/
# Then in videos/<slug>/index.html:
#   <img id="top-banner-logo" src="assets/<brand>-logo-light.svg" alt="<Brand>" />
```

Use `*-light.svg` / `*-light.png` only — `*-dark` variants are near-invisible on dark navy. The top banner is 60px tall (vs Shorts' 112px-equivalent) — most logos render cleanly at 60px without modification.

## Don'ts

All Shorts don'ts apply. Long-form-specific additions:

- Never use `repeat: -1` anywhere (deterministic-only). The CTA subscribe pulse uses a finite `repeat: 4` — if you extend the CTA scene, scale the repeat count proportionally.
- Never put `tl.from(el, { opacity: 0, ... })` at timeline position > 5 without `immediateRender: false` — the long-form-specific gotcha. The template's scene timelines all have it; preserve the flag when editing.
- Never put `data-duration` on any sub-composition wrapper `<div>` in `index.html` — the sub-comp's internal timeline owns its length. The wrappers only get `data-start` + `data-track-index`.
- Never put `class="clip"` on `<audio>` or `<video>` elements. Wrapper `<div>` takes the clip role for embedded video; audio takes data-start/duration/track-index without class.
- Never run `new-long-form-standard` and `new-anthropic-short` against the same slug — pick one playbook per video.
- Never auto-render — even at draft quality. Long-form renders are 3-15 minutes; the user always triggers them manually.
