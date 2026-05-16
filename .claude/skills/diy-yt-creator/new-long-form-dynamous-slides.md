# new-long-form-dynamous-slides — Playbook

End-to-end pipeline that turns a **topic prompt** or **workshop recording transcript** into a previewable HyperFrames long-form in the classic Dynamous deep-navy + Dynamous Blue workshop-deck aesthetic. Zero manual steps; ends at preview, never renders.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 (research → plan → script → critique → fact-check → retention strategy) and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A. Use the pipeline by default; use this skill directly only when you already have a script.

This playbook is the Dynamous-Slides analog of [new-long-form-standard.md](./new-long-form-standard.md) and [new-long-form-anthropic.md](./new-long-form-anthropic.md). The shape is identical — only the template, palette, scene archetype set, and a few template-specific quirks differ.

If you've used `new-long-form-standard`, the deltas are:

- **Template**: `templates/long-form/dynamous-slides/` (instead of `templates/long-form/standard/`)
- **Palette**: deep-navy `#07090F` + Dynamous Blue `#3B82F6` hero + Cyan `#0EA5E9` halo. **NO PURPLE anywhere.** Tertiary accents reach for cyan or deep-halo `#1E40AF`.
- **Typography**: Montserrat for display (weights 300/700/800/900), JetBrains Mono for data — the **300/800 weight contrast** in the same line is the signature move.
- **Eyebrow chrome**: every scene's kicker is an uppercase JetBrains Mono with a 56px×2px accent-2 `::before` bar — keep this rhythm across the video.
- **Persistent backdrop**: dual blue/cyan halos (`#bg-halo` top-right, `#bg-halo-2` bottom-left) breathing on separate yoyo cadences. Don't fight them with per-scene halos.
- **8 scene archetypes** (different from standard):
  1. `scene-hook-wordmark` — character-stagger hero with flame mark badge (decorative SVG icon top-right)
  2. `scene-headline-accent` — two-line headline with Dynamous-Blue underline sweep (background-size 0% → 100%)
  3. `scene-big-stat` — counter ramp with gradient text (accent-2 → accent) + suffix slide-in + receipt label
  4. `scene-tension-pivot` — `light` 300 + `strong` 800 weight contrast in the same headline, subtle scale push-in
  5. `scene-pillars-3` — three-pillar grid, **step-by-step paced reveal** (~4s apart, per `step-by-step-reveal.md`), bottom rule fills after card
  6. `scene-list-reveal` — 6-row enumerated list, marker sweep on bottom of each row, paced ~2.8s apart
  7. `scene-quote-card` — line-by-line quote reveal with marker sweep on hero phrase + author chip with pulsing dot
  8. `scene-cta` — flame + Dynamous wordmark + URL lockup + debate question + comment/subscribe pill row
- **Two flagged "flash" transitions** by default — the root timeline's `crossfadeScenes(..., flash: true)` triggers a brief Dynamous-Blue radial flash overlay at:
  - big-stat → tension-pivot (hero pivot — the emotional turn)
  - quote-card → cta (CTA landing — settles, doesn't punch)
  - Every other boundary uses the standard 1.1s blur+scale crossfade with no flash. Don't add more flashes — they lose their punch.
- **Brand assets**: `assets/dynamous-logo-light.svg` is already inside the template (white wordmark). The flame mark is inlined as SVG inside `scene-hook-wordmark` and `scene-cta` — no asset to copy.

## Inputs

User provides ONE of:

- A **topic / prompt** (e.g. _"6 strategies for scaling AI coding to complex codebases"_, _"What I learned from 50 brownfield migrations"_) — agent drafts the full script
- A **title + key facts** (e.g. _"Brownfield AI layer: 9 sub-agents, 300-line global rules cap, vertical slice architecture"_) — agent uses facts verbatim, drafts the framing
- A **workshop recording transcript** (e.g. an Obsidian clipping of a Zoom workshop, a YouTube transcript, a podcast transcript) — agent extracts the spine + key claims, drafts a 2-15 min script in the host's voice
- A **pre-written `script.txt`** — agent skips drafting (jump to step 5)

If the topic has no real source data and would require fabricated stats/dates, **stop and ask the user for a source URL** before proceeding. Never invent numbers — every claim in the script must trace to the source.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with:

- `script.txt` — flat narration script (per Phase 2a)
- `scripts/full-script.md` — segmented script with per-scene `[SCENE: ...]` headers
- `audio/narration.wav` — TTS narration (ElevenLabs OR `scripts/edge-tts-fallback.py` for draft voice)
- `transcript.json` — word-level timestamps
- `index.html` — composition filled with real content, scene `data-start` values sync'd to spoken-word frames
- `youtube-description.md` — keyword-front-loaded description with chapters + Dynamous CTA + engagement question
- Preview studio open in browser at the URL printed by `hyperframes preview`

The user runs render themselves:

```bash
npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4
```

---

## Steps

### 1. Confirm slug + title

Derive a kebab-case slug from the topic (3-6 words, no stopwords). Examples:

- "6 strategies for scaling AI coding to complex codebases" → `scaling-ai-coding-complex-codebases`
- "Brownfield AI layer setup with Claude Code" → `brownfield-ai-layer-setup`
- "Why Dynamous workshops beat reading docs" → `dynamous-workshops-vs-docs`

Confirm with the user in one line: _"Spawning `videos/<slug>/` — title '<Title>'. Proceed?"_ Skip confirmation if the user already gave you both.

### 2. Copy the template

```bash
cp -r templates/long-form/dynamous-slides videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/long-form/dynamous-slides videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `README.md`, `tokens/dynamous.css`, `compositions/scene-*.html`, `audio/.gitkeep`, `assets/dynamous-logo-light.svg`, `assets/shapes/`, `assets/screenshots/` should all exist.

### 3. Update meta.json

Replace the placeholders:

```json
{
  "id": "<slug>",
  "name": "<Title Case Name>"
}
```

### 4. Source the script

**Branch A — pipeline output exists**: if `videos/<slug>/scripts/full-script.md` already exists (full-auto wrote it during research → plan → script → critique → TTS-script → fact-check), read it and proceed to step 5 to wire content. Skip drafting.

**Branch B — pre-written script provided**: if the user pasted a `script.txt`, write it to `videos/<slug>/script.txt` verbatim and proceed to step 5.

**Branch C — topic / facts only, no pipeline output**:

1. Read every fact / claim from the user-provided source.
2. Draft a **per-scene segmented script** at `videos/<slug>/scripts/full-script.md` with `[SCENE: hook]`, `[SCENE: headline-accent]`, `[SCENE: big-stat]`, etc. headers matching the 8 scene archetypes used in `index.html`. Target ~150-160 WPM. For a 2-min video that's ~300-320 words; for 7 min, ~1,050-1,120.
3. Per `.claude/rules/tts-pronunciation.md`, audit heteronyms (`live`, `lead`, `read`, `close`, `record`) and tech terms (`nginx`, `kubectl`, `OAuth`, `API`, `CLI`).
4. Per `.claude/rules/engagement-cta.md`, end on a **debate-sparking question** that's binary/short-list answerable, polarizing, references a specific video claim, and answerable in 5 seconds. No banned closers ("What do you think?", "How would you build this differently?").
5. Apply the Phase 2a TTS-optimization pass and write the flat `videos/<slug>/script.txt`.

### 5. Wire copy into each scene

For each scene in `videos/<slug>/index.html` and `compositions/scene-*.html`, replace every `REPLACE:` placeholder with the real copy. Specific notes per archetype:

- **scene-hook-wordmark**: The character-stagger uses `<span class="char">…</span>` per glyph. If your hero word is "BROWNFIELD" — 10 chars — write 10 char spans. The flame mark stays. The wordmark `font-size: 260px` is a hard floor for the scroll-stop power.
- **scene-headline-accent**: Wrap the keyword you want underlined in `<span class="accent-text" id="ha-accent">…</span>`. The 300-weight `<span class="light">` is reserved for the setup clause, 800 for the punchline.
- **scene-big-stat**: Set `const STAT_TARGET = N;` in the script tag to your number. The suffix is a separate span (`+`, `%`, `×`, etc.); keep it short. The receipt label uses `<strong>` for the punchline keyword.
- **scene-tension-pivot**: 300-weight `<span class="light">` on the setup, 800-weight on the punchline. The flash overlay fires on this scene's entry — don't add a competing strong color.
- **scene-pillars-3**: ALWAYS use the step-by-step pattern — narration must name each pillar at its entry beat (~4s apart). If your content has 4+ items, use `scene-list-reveal` instead.
- **scene-list-reveal**: 6 rows is the default. For 4-5 rows, delete rows from the bottom AND the corresponding `tl.to()` lines in the timeline + the corresponding `lr-rN` entries in the `rowTimes` array. Don't leave empty rows.
- **scene-quote-card**: Up to 3 lines of quote body. The hero phrase gets a `<span class="mark" id="qc-mark1">…</span>` wrap for the sweep. Author chip has a `dot` + author name + source.
- **scene-cta**: `#cta-debate` text MUST match the **final spoken line of `script.txt`** AND the **closing paragraph of `youtube-description.md`**. Replace the `REPLACE: dynamous.ai / @ChannelHandle` URL with the real channel handle.

### 6. Adjust scene durations (if needed)

The default 8 scenes total 120s. To extend for longer videos:

1. Bump each scene's `data-start` in `videos/<slug>/index.html` and update the corresponding `tl.addLabel("scene-name", T)` value.
2. Update the `crossfadeScenes()` calls' anchor labels (they reference `"label-=0.4"`).
3. Update the root composition `data-duration` and the `TOTAL_DURATION` constant.
4. Update the `tl.set({}, {}, TOTAL_DURATION)` extender at the bottom of the timeline.

For shorter videos, cut entire scenes — don't compress them below 8s each (the entrance animations + step-by-step reveals need that breathing room).

### 7. Generate narration

**Default — ElevenLabs (production voice)**:

```bash
python scripts/elevenlabs-tts.py videos/<slug>/script.txt videos/<slug>/audio/narration.wav
```

The `.env` is already configured (per `feedback_elevenlabs_env_already_set`); never ask the user about voice ID or settings.

**Draft voice — `edge-tts` fallback** (per `feedback_draft_voice_edge_tts`):

```bash
python scripts/edge-tts-fallback.py videos/<slug>/script.txt videos/<slug>/audio/narration.wav
```

This uses `en-US-AndrewNeural` at +10% rate by default. Use when the user says "draft voice" or when ElevenLabs is unavailable.

### 8. Transcribe + retime

```bash
npx hyperframes transcribe videos/<slug>
```

Writes `videos/<slug>/transcript.json` and populates the captions sub-composition. The transcript drives per-scene retime: anchor each scene's `data-start` to the spoken-word frame where the narrator names the scene's content.

### 9. Wire audio bed

Uncomment the audio bed block in `videos/<slug>/index.html`:

```html
<audio id="narration"
       src="audio/narration.wav"
       data-start="0"
       data-duration="<computed>"
       data-track-index="2"
       data-volume="1"></audio>
```

If background music is generated (Phase 3.2 of full-auto), wire the 3-segment bed per `.claude/rules/audio-design.md`:

- `bg-music-hook.mp3` at `data-start="0"`, hook duration, `data-volume="0.12"`
- `bg-music-body.mp3` for the middle, `data-volume="0.07"`
- `bg-music-cta.mp3` at the final ~15s, `data-volume="0.12"`

NEVER add `class="clip"` on `<audio>` elements.

### 10. Sync SFX (optional)

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

Reads `videos/<slug>/sfx-cues.txt` (defaults to `cinematic-whoosh`, `impact-slam`, `scale-slam`, `spring-pop`, `pop`) and copies the cue files into `assets/sfx/`. Wire them per `.claude/rules/audio-design.md` — typical pattern: a `cinematic-whoosh` (`data-volume="0.11"`, `data-duration="1.5"`) at each scene boundary, an `impact-slam` (`0.15`) at the hero pivot moment, a `scale-slam` (`0.15`) at the big stat reveal.

### 11. Lint + validate + inspect

```bash
npx hyperframes lint    videos/<slug>
npx hyperframes inspect videos/<slug>
npx hyperframes validate videos/<slug>
```

Fix any errors. Warnings can stay if they're informational (e.g. `composition_file_too_large` on a verbose root composition).

### 11.7. YouTube description (MANDATORY)

Per `.claude/rules/youtube-metadata.md` and `feedback_youtube_description_mandatory`:

1. Run vidIQ keyword research on the topic (if the MCP is wired in this session).
2. Write `videos/<slug>/youtube-description.md` with:
   - Keyword-front-loaded first 200 chars
   - SEO chapter titles (compute timestamps as `data-start ÷ speed_factor` if MP4 is sped — default `1.0`)
   - Dynamous CTA block in `----` separators
   - Validated URLs (no fabrications)
   - The closing **debate-sparking question** matching `#cta-debate` and the final spoken line
   - 15-25 hashtags

### 12. Preview + hand off

```bash
npx hyperframes preview videos/<slug>
```

Open the studio URL in the user's browser. Confirm:

- Duration matches `audio/narration.wav` length (within ±0.5s)
- All 8 scenes paint without flash-of-empty-content
- Step-by-step reveals fire on narration word anchors
- Two flash transitions fire (big-stat → tension-pivot AND quote-card → cta) — and only those two
- `#cta-debate` is visible at the final frame

Tell the user how to render:

```bash
npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4
```

---

## Quality bar

Before declaring done, verify:

- [ ] Lint passes 0 errors
- [ ] Inspect passes 0 layout overflow
- [ ] Every `REPLACE:` placeholder is gone from `videos/<slug>/index.html` and every `compositions/scene-*.html`
- [ ] `#cta-debate` text matches the final spoken line of `script.txt`
- [ ] `youtube-description.md` exists and ends with the same debate question
- [ ] Scene durations sum within ±0.5s of `audio/narration.wav` length
- [ ] No purple anywhere in the rendered output (audit `index.html` + every scene file for `purple`, `#8B5CF6`, `#a855f7`, `magenta`)
- [ ] No fabricated stats — every number/date traces to a source the user provided

## Don'ts (template-specific)

- **No purple.** Hardest brand rule. If a card / glow / accent reads as purple in the preview, it's wrong — replace with `--accent` (blue) or `--accent-3` (cyan).
- **No more than 2 flash transitions per video.** Default flagged boundaries are the hero pivot and CTA landing. If you flag a third, it stops reading as special.
- **No removing the flame mark** from the hook + CTA scenes — it's the Dynamous brand seal.
- **No animating below 220px** on the hook wordmark — loses scroll-stop power.
- **No `<br>` in `scene-list-reveal` rows** — the grid layout handles wrapping.
- **No third "weight" past 300/800 in the same headline** — the 300/800 contrast is the signature; introducing 500 or 700 muddies it.
- **No reveal-all-at-once on `scene-pillars-3` or `scene-list-reveal`** — step-by-step is mandatory per `.claude/rules/step-by-step-reveal.md`.
