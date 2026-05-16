# new-long-form-anthropic — Playbook

End-to-end pipeline that turns a **topic prompt** (or an Anthropic / Claude blog post) into a previewable HyperFrames horizontal long-form video (1920x1080, 30fps, 4-10 minutes) using the Anthropic dark-stage template at `templates/long-form/anthropic/`. Zero manual steps; ends at preview, never renders.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A. Use the pipeline by default; use this skill directly only when you already have a script.

This playbook is the **Anthropic-branded** long-form analog of [`new-long-form-standard.md`](./new-long-form-standard.md). Read that file first — most of the pipeline is identical. The deltas for the Anthropic variant are:

- **Template**: `templates/long-form/anthropic/` (instead of `templates/long-form/standard/`)
- **Palette**: dark stage `#0B0F18` near-black + warm off-white `#F5F1EB` + Claude orange `#E97458` leading; purple `#A78BFA`, blue `#6B9AEF`, green `#7DD3A6` rotate through middle scenes. Red `#D14343` is for warnings only — never decorative. See [`shared/lib/visual-styles/long-form-anthropic.md`](../../../shared/lib/visual-styles/long-form-anthropic.md).
- **Tokens linked**: `tokens/anthropic-dark.css` (NOT `tokens/long-form.css`). Same variable NAMES as the standard tokens so per-video overrides interchange.
- **Logo default**: ships `assets/anthropic-logo-light.svg` as the top-banner. Swap only for collab / partner videos.
- **Scene roster**: 12 archetypes shipped, including 5 NEW Anthropic-specific scenes:
  - `scene-image-3d-reveal.html` — **signature scene** for blog screenshots / source figures. Hero image enters with `perspective: 2000px`, `rotateY: -25° → 0°, translateZ: -200 → 0, scale: 0.7 → 1`, `back.out(1.4)` over 1.2s. After settle, finite-repeat `±1.5° sine.inOut` micro-yoyo (calculated `Math.floor(SCENE_DURATION / 12)` cycles — never `repeat: -1`).
  - `scene-list-cards.html` — 2x2 step-by-step grid (`tl.set` hide at t=0, `tl.to` reveal at calculated narration anchors, ~1.5s apart).
  - `scene-quote-card.html` — 180px orange opening quote-mark + 56px italic body + marker-sweep underline 2s after settle.
  - `scene-dynamous-midroll.html` — opt-out community plug (~10–14s; remove if the video doesn't run the Dynamous promo).
  - `scene-subscribe-banner.html` — mid-video subscribe pop-in (~6–8s) distinct from the closing CTA scene.
- **Audio bed**: same long-form-supports-bg-music pattern as the standard template (3-segment hook/body/cta bed on track 3). Default cue set is **transition-whoosh only** (inherited from Anthropic Shorts) — one `cinematic-whoosh` per scene boundary at `data-volume="0.11"`. Per-element SFX (impact-slam, scale-slam, spring-pop) are opt-in for a single deliberate moment.
- **CTA**: `scene-cta.html` is re-skinned to orange-leading and must satisfy [`engagement-cta.md`](../../rules/engagement-cta.md) — debate-sparking question in `#cta-question`, persists through the held final frame.

## Inputs

User provides ONE of:

- A **topic / prompt** (e.g. _"Anthropic's blog post on how Claude Code works in large codebases"_) — agent fact-bases against the source then drafts the script
- A **source URL** (blog post / docs page on `anthropic.com` / `claude.com` / `claude.ai/blog`) — agent fetches, downloads images, drafts an article-response script
- A **title + key facts** — agent uses the facts verbatim, drafts the framing
- A **pre-written `script.txt`** — agent skips drafting (jump to step 5)

If the topic has no real source and would require fabricated stats / dates, **stop and ask the user for a source URL** before proceeding. Never invent numbers. **For article responses, never frame as opinion — frame as "Anthropic shows / explains / lays out…"** so the video is grounded in the source's authority.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with:

- `tmp/source.md` — verbatim source article (article-response only) + curated key facts / quotes
- `tmp/image-map.md` — which downloaded source image anchors which scene (article-response only)
- `assets/blog/<images>` — downloaded blog images (article-response only)
- `script.txt` — narration script (4-10 minutes typical)
- `audio/narration.wav` — ElevenLabs TTS narration (or operator-recorded; voice + speed pulled from `.env`)
- `audio/bg-music-{hook,body,cta}.mp3` — optional 3-segment bg-music (operator drops or sources)
- `transcript.json` — word-level timestamps
- `index.html` — root composition with scene timing tuned to spoken-word landmarks
- `compositions/scene-*.html` — scene archetypes filled with real content (image-3d-reveal scenes point at `assets/blog/<file>`)
- `compositions/captions.html` — populated by `hyperframes transcribe`
- `youtube-description.md` — per [`youtube-metadata.md`](../../rules/youtube-metadata.md)
- Preview studio open in the browser at the URL printed by `hyperframes preview`

The user runs render themselves: `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4`.

---

## Steps

### 1. Confirm slug + title

Derive a kebab-case slug (3-6 words, no stopwords). Examples:

- "Anthropic's Claude Code at scale blog post" → `claude-code-at-scale`
- "How Claude Code works in large codebases" → `claude-code-large-codebases`
- "Anthropic constitutional AI 2026 update" → `constitutional-ai-2026-update`

Confirm in one line — _"Spawning `videos/claude-code-large-codebases/` — title 'How Claude Code Actually Works in Large Codebases'. Proceed?"_ Skip if the user already gave you both.

### 2. Copy the template

```bash
cp -r templates/long-form/anthropic videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/long-form/anthropic videos/<slug>`

Verify: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `README.md`, `tokens/anthropic-dark.css`, `compositions/scene-*.html` (×12) + `captions.html`, `audio/`, `assets/{shapes,sfx,screenshots,clips}/`, `assets/anthropic-logo-light.svg` should all exist.

### 3. Update meta.json

```json
{
  "id": "<slug>",
  "name": "<Title Case Name>"
}
```

**No Dynamous-promotion question** (same as standard long-form). The template ships `scene-dynamous-midroll.html` opt-out — remove the wrapper + crossfade call from `index.html` if the video doesn't run the Dynamous promo. Default: KEEP the midroll.

### 3.5. (Article-response branch only) Download source + images

If the user provided a `claude.com/blog/` / `anthropic.com/news/` URL, do this BEFORE drafting:

1. **Fetch the full article verbatim** with `WebFetch` and save to `videos/<slug>/tmp/source.md`. Include full headings + body + quotes + table contents. Append a "Key facts / stats / quotes" section at the bottom with operator-curated highlights for fact-check.
2. **Extract every inline image URL** from the article. For each, download to `videos/<slug>/assets/blog/<descriptive-name>.<ext>` via `curl -sL -o`. Common Anthropic blog images live on `cdn.prod.website-files.com`. Use descriptive names like `fig1-harness.png`, `fig2-rollout-phases.png`, not the CDN's slugified blobs.
3. **Write `videos/<slug>/tmp/image-map.md`** mapping each downloaded image to: which scene archetype anchors it, suggested 3D-reveal callout label, suggested overline ("FROM THE ARTICLE" / "ANTHROPIC'S DIAGRAM"), and a one-line provenance note.

### 4. Draft the script (or load from pipeline)

Two branches — try Branch A first.

#### Branch A — pipeline output exists (preferred)

If `videos/<slug>/scripts/full-script.md` exists (Phases 0-2b have run):

1. READ `videos/<slug>/scripts/full-script.md` as the authoritative narration source.
2. READ `videos/<slug>/plan.md` for `## Composition Layout`, `## Retention Component Picks`, `## Data Timing Budget`.
3. READ `videos/<slug>/retention-strategy.md` (if it exists from Phase 3.5).
4. Map the script's `## Scene N: <name>` sections onto the template's 12 scene archetypes. Anthropic-specific mappings:

   | Script scene type | Template scene file |
   |---|---|
   | Cold-open hook / hero stat | `scene-hook.html` |
   | Showing a blog figure / screenshot with depth | `scene-image-3d-reveal.html` |
   | Enumerated list (N components, N patterns, N steps) | `scene-list-cards.html` |
   | Pulled quote from the source | `scene-quote-card.html` |
   | Before / after / A vs B | `scene-side-by-side.html` |
   | Receipts (2-3 huge numbers) | `scene-stat-pill-row.html` |
   | "Where this came from" | `scene-source-cards.html` |
   | Demo / product footage | `scene-video-embed.html` |
   | "How it fits together" / system view | `scene-architecture-stack.html` |
   | Dynamous community plug (~10–14s, ~60–70% mark) | `scene-dynamous-midroll.html` |
   | Subscribe / support banner (~6–8s, ~50% mark) | `scene-subscribe-banner.html` |
   | Closing CTA + debate question | `scene-cta.html` |

   You don't need all 12. Drop unused scenes by removing the wrapper `<div>` from `index.html` AND the matching `crossfadeScenes()` call AND the `tl.addLabel(...)` line.

5. Skip Branch B's inline drafting. Jump to step 4.5+.

If anything in the plan or retention-strategy looks wrong (missing scene mapping, unrecognized retention component), STOP and tell the user — do NOT invent.

#### Branch B — no pipeline output (legacy / quick path)

Fall back to inline drafting. For long-form Anthropic, **strongly recommend** running `/diy-yt-creator:full-auto <topic>` first — Anthropic-branded videos benefit much more from research than Shorts do, especially for article responses where fact-grounding is mandatory.

If you must draft inline:

- Structure narration into 5–8 scenes of 30–90s each. Total target: 4–10 minutes.
- **Article-response framing rule**: open every claim with source-grounded language — "Anthropic explains…", "The blog post lays out…", "Anthropic's Applied AI team observed…", "The article cites…". Never "I think…" or "in my opinion…". The video is a faithful response to the source, not a hot take.
- Hook earns the watch in the first 10s. Pattern-interrupt every 20–30s. Mid-video subscribe banner around the 50% mark. Dynamous midroll around the 60–70% mark. Debate-CTA close.
- Short sentences for TTS. No semicolons or em-dashes. Numbers as digits.
- Heteronym audit per [`tts-pronunciation.md`](../../rules/tts-pronunciation.md) — `live` (laɪv vs lɪv), `lead` (liːd vs lɛd), etc.

Save to `videos/<slug>/script.txt`. Use one blank-line-separated block per scene, in order.

### 4.5. Fact-check (article-response only — MANDATORY)

For article-response videos, fact-check the draft script **bidirectionally** against `tmp/source.md`:

1. Every claim in the script must appear in `tmp/source.md` (or be a faithful paraphrase). No fabricated stats / dates / names / quotes.
2. Every operator-curated key fact in `tmp/source.md` Key Facts section that you DIDN'T include should be a deliberate omission, not a miss. Spot-check 3–5 random highlights.
3. Cross-reference the names / titles of every figure shown in `scene-image-3d-reveal` scenes against the article's image captions.

Skip WebSearch — for article-response, the source is the single authority. Use `WebFetch` only to re-pull the source if needed.

### 5. Generate TTS

ElevenLabs is the default. The `.env` file in the repo root has `ELEVENLABS_API_KEY`, voice ID, and speed already configured — the scripts read them automatically.

```bash
python scripts/elevenlabs-tts.py --in videos/<slug>/script.txt --out videos/<slug>/audio/narration.wav
```

Or via hyperframes CLI (if ElevenLabs is wired into the project's TTS adapter):

```bash
npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav
```

Don't ask about voice or speed — they're in `.env` per memory.

### 6. Transcribe for word-level sync

```bash
npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
```

Writes `transcript.json`. For long-form (4–10 min), prefer `-m medium.en`.

### 7. Compute scene boundaries

Identical to `new-long-form-standard.md` step 7. Replace template default `data-start` values `[0, 8, 28, 46, 60, 76, 94, 106, 118]` with values computed from `transcript.json`:

```
scene_starts = [0]
for n in [1..N-1]:
    scene_starts[n] = transcript[<last word of scene n-1>].end - 0.2
total_duration = transcript[<last word>].end + 1.5
```

Update in `index.html`:
- Each scene wrapper's `data-start`
- `<div id="root">` `data-duration` → `total_duration`
- `const TOTAL_DURATION = ...` → `total_duration`
- All `tl.addLabel(...)` time values → matching `scene_starts[n]`
- Whoosh `<audio>` `data-start` for each scene boundary (`data-duration="1.5"`, `data-volume="0.11"`)

### 8. Edit each `compositions/scene-*.html`

Always invoke `/hyperframes` before this step. Each scene is its own file.

For each scene the script uses:

1. Replace placeholder text in the inner `<div>` with the script's content for that scene.
2. **Per-scene accent**: each scene pins one lead accent. Default rotation: hook=orange, list-cards=orange→purple→blue→green per card, quote=orange, side-by-side=orange+purple, stat-pills=orange+purple+blue, image-3d-reveal=orange frame, dynamous-midroll=purple+pink+cyan (locked palette), subscribe-banner=red SUBSCRIBE pill, architecture-stack=4-accent stripes, cta=orange dominant.
3. **For `scene-image-3d-reveal.html`**: replace `src="assets/screenshots/blog-img-01.png"` (or similar) with the actual file path under `assets/blog/<file>`. Update the overline ("FROM THE ARTICLE" / "ANTHROPIC'S DIAGRAM"), the headline (the figure's title), and the caption (one-line description). If the image is wider than 16:9, tune `width` / `height` on the `<img>` to fit the 1200×675 frame the scene ships with. **The micro-yoyo's repeat count is computed from `SCENE_DURATION`** — when you change the scene's duration, recompute `Math.floor(SCENE_DURATION / 12)` cycles.
4. **For `scene-list-cards.html`**: when narration names each item, anchor that card's reveal time to the word's `transcript.json[].start`. Don't leave the template's ~1.5s placeholder spacing in place.
5. **For `scene-quote-card.html`**: pick the marker-sweep word range to underline the key phrase from the quote. The default marker entrance is 2s after quote settles — retime to the narration's emphasis word.
6. **For `scene-dynamous-midroll.html`**: keep the locked Dynamous wording (don't paraphrase) — the spoken line is `"If you want to learn more about AI, check out the dynamous.ai community."` per memory. URL pill stays `dynamous.ai`. Optional `10% OFF` chip — keep or remove based on the video's promo posture.
7. **For `scene-subscribe-banner.html`**: don't restate the closing CTA here. This is a mid-video pop-in saying "if this is useful, subscribe" — distinct from the debate-question CTA at the end.

### 8a. Edit root `index.html`

1. **`<title>`** → the video title
2. **`<div id="root">`** `data-duration` → `total_duration`
3. **`#top-banner-logo`** stays at `assets/anthropic-logo-light.svg`. For collab / partner videos add a second logo + divider; for non-Anthropic content, this template is the wrong template — use `standard` instead.
4. **Scene `data-start`** values: replace with `scene_starts[n]` from step 7
5. **Scene labels** in `tl.addLabel(...)`: replace times with `scene_starts[n]`
6. **Audio bed** — uncomment narration `<audio>` (and bg-music elements if used):
   - `<audio id="narration">` — `data-duration` = `total_duration`, `data-volume="1.0"`
   - bg-music segments — operator drops the three `.mp3` files OR leaves the elements commented
   - Volumes: 1.0 / 0.12 / 0.07 / 0.12 — see [`.claude/rules/audio-design.md`](../../rules/audio-design.md)
7. **Whoosh wiring** — add one `<audio>` per scene boundary (already shipped commented):
   ```html
   <audio id="sfx-whoosh-t1" src="assets/sfx/cinematic-whoosh.mp3"
          data-start="<scene_starts[1]>" data-duration="1.5"
          data-track-index="3" data-volume="0.11"></audio>
   ```
   First sync the cue file: `bash scripts/sync-video-sfx.sh videos/<slug>` (reads `sfx-cues.txt`).

### 8b. Wire SFX from `retention-strategy.md` (optional)

Same logic as `new-long-form-standard.md` step 8b. Track-index 4+ for per-element SFX (track 2 = narration, track 3 = bg-music + whoosh). Volume cap 0.25.

### 8.5. Lib pick (optional)

Read [`shared/lib/MANIFEST.md`](../../../shared/lib/MANIFEST.md) and [`shared/lib/visual-styles/long-form-anthropic.md`](../../../shared/lib/visual-styles/long-form-anthropic.md). For long-form Anthropic, suggested registry / lib blocks:

- `blocks/dynamous-midroll/` — if the inline `scene-dynamous-midroll.html` doesn't fit and you want the full 31.5s 6-phase community break
- `blocks/cinema-title-slam/` — alternative hook
- `vfx-shatter` / `vfx-iphone-device` (upstream registry, `npx hyperframes add`) — premium reveals for product showcases
- Shader transitions (`chromatic-radial-split`, `cinematic-zoom`, `light-leak`) — for mid-video chapter beats

**Never reference `shared/lib/` paths from `data-composition-src`, `<img src>`, etc.** Always copy the file in.

### 9. Lint

```bash
npx hyperframes lint videos/<slug>
```

Must report `0 errors`. Common Anthropic long-form errors:

| Error | Likely cause | Fix |
|---|---|---|
| `composition_id_mismatch` | Parent mount's `data-composition-id` ≠ child file's internal `data-composition-id` | Match them; see [`sub-composition-wiring.md`](../../rules/sub-composition-wiring.md) |
| `audio_src_not_found` (whoosh) | Wired the whoosh `<audio>` elements but didn't sync `cinematic-whoosh.mp3` | Run `bash scripts/sync-video-sfx.sh videos/<slug>` |
| `media_missing_id` | `<img>` in scene-image-3d-reveal without an id | Add `id="figure-1"` (or similar) |
| `duplicate_media_discovery_risk` | Wrote a literal `<img src="...">` inside an HTML comment | Replace with prose like "operator wires the figure here" |
| `data-duration on sub-comp wrapper` | Added `data-duration` to a `<div data-composition-src="...">` in `index.html` | Remove it — the sub-comp owns its length |

### 10. Validate (WCAG) and inspect (overflow)

```bash
npx hyperframes validate videos/<slug>     # WCAG audit + 404 check
npx hyperframes inspect videos/<slug>      # layout overflow at 1920x1080
```

Common Anthropic long-form overflows:

- **Hook headline at 120px wraps onto 4+ lines** — shorten the headline; the slam should be 3–5 words max.
- **Image-3d-reveal: caption runs three lines** — keep captions under ~80 chars; the 1200×675 frame has limited space below.
- **Quote-card body at 56px italic overflows the canvas** — keep quotes under 30 words. If the source quote is longer, use `max-width: 1400px` and pull two non-adjacent sentences with `…` between them.
- **List-cards: descriptor (24px) truncates** — keep descriptors under 6 words.

WCAG warnings: secondary text (#9A958D) on dark-stage hits 4.7:1 — safe for AA normal but flagged for AAA. Bump font ≥ 18px to silence the warning, or keep as-is for body copy.

### 11. Open preview

```bash
npx hyperframes preview videos/<slug>
```

(Run in background.) Capture the URL (typically `http://localhost:5173`).

### 11.5. (Optional) QA the rendered preview visually

`/diy-yt-creator:qa-composition <slug>`. Strongly recommended for long-form Anthropic because the `scene-image-3d-reveal` motion + warm-paper crop within the dark frame has more places for visual regressions than the bare-template tests catch.

### 11.7. Generate YouTube description (MANDATORY — never skip)

**Canonical rule: [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md). Long-form NEEDS chapters — viewers expect them.**

1. **vidIQ keyword research first** — `mcp__claude_ai_vidiq__vidiq_keyword_research`, `vidiq_outliers`, `vidiq_trending_videos` for 3–5 topic seeds.
2. **Article-response specific**: keyword-front-load the article's own keywords ("Claude Code at scale", "large codebases", "CLAUDE.md", "hooks", "skills", "plugins", "MCP", "LSP", "subagents") plus the broader topic seed.
3. **Chapter timestamps** from each scene wrapper's `data-start`. If the rendered MP4 was ffmpeg-sped per [`video-speedup.md`](../../rules/video-speedup.md), divide by speed factor. Format `M:SS`. Long-form: 6–10 chapters typical.
4. **Source citation in the description body** — every article-response video MUST link to the source article in the Resources section: `📝 Source: <full article URL>`. The article is the authority; credit it.
5. **Engagement question** must match the script's final spoken line per [`engagement-cta.md`](../../rules/engagement-cta.md).
6. **15–25 hashtags**, mix of broad (`#claude`, `#anthropic`, `#aiagents`) + specific (`#claudecode`, `#claudemd`, `#largeCodebases`).

### 12. Report to the user

One concise message containing:

- **Slug + path**: `videos/<slug>/`
- **Total duration**: `XX min YY s`
- **Voice + speed**: pulled from `.env`
- **Scene count**: e.g. `9 of 12 archetypes used (scene-video-embed, scene-source-cards, scene-architecture-stack skipped)`
- **3D-reveal figures shown**: list each `assets/blog/<file>` referenced and which scene
- **Preview URL**: `http://localhost:5173`
- **Render command** (do NOT run): `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/<slug>.mp4`
- **YouTube description**: `videos/<slug>/youtube-description.md` (paste-ready)
- **Source citation**: confirm article URL is in description's Resources section
- **Any inspect findings** that needed manual content tradeoffs

Stop. Wait for user iteration or manual render.

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes validate videos/<slug>` → no AAA contrast failures, no AA failures on headlines
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow on hook, image-3d-reveal, list-cards, quote-card, side-by-side, architecture-stack
- [ ] All used scenes have real content (no leftover placeholders: "YOUR HOOK HEADLINE", "[Figure caption]", "List item 1", "Quote text here", etc.)
- [ ] Scene `data-start` values computed from transcript, NOT left at template defaults
- [ ] Scene labels in `tl.addLabel(...)` chain match scene `data-start` values
- [ ] Audio narration `<audio>` uncommented with correct `data-duration`
- [ ] Whoosh `<audio>` for every scene boundary
- [ ] If used: bg-music elements uncommented with correct segment timing
- [ ] If used: each `scene-image-3d-reveal.html` points at a real file under `assets/blog/` or `assets/screenshots/`
- [ ] **Article-response only**: every claim in the script appears in `tmp/source.md` (or is a faithful paraphrase)
- [ ] **Article-response only**: source URL cited in `youtube-description.md` Resources section
- [ ] Captions wrapper still present in `index.html` (don't remove it)
- [ ] Closing CTA satisfies [`engagement-cta.md`](../../rules/engagement-cta.md) — debate-sparking question in `#cta-question`, matching the spoken closing line and the YouTube description's closing paragraph
- [ ] Preview URL is reachable

If any item fails, fix it before reporting.

---

## Real logos — copy into project, don't reference shared

The template ships with `assets/anthropic-logo-light.svg`. For collab / partner videos, add a partner logo:

```bash
cp shared/logos/<partner>-logo-light.svg videos/<slug>/assets/
# Then in videos/<slug>/index.html, replace the single-logo block with a brand-lockup row.
```

Use `*-light.svg` / `*-light.png` only — `*-dark` variants are near-invisible on dark stage. NEVER reference `../../shared/logos/...` — preview server rejects out-of-project paths.

## Don'ts

All standard-long-form don'ts apply. Anthropic-specific additions:

- Never frame article-response content as opinion. Lead with "Anthropic explains…", "The article shows…", "Anthropic's Applied AI team observed…". The video is grounded in the source's authority.
- Never use `repeat: -1` on the `scene-image-3d-reveal` micro-yoyo — compute finite repeats from `SCENE_DURATION / 12`.
- Never put more than one accent on a scene's chrome — pick one of orange / purple / blue / green per scene.
- Never use red (`--accent-warn`) decoratively. Reserve for regression / deprecation / "removed in this release" only.
- Never paraphrase the locked Dynamous midroll spoken line. Per memory: "If you want to learn more about AI, check out the dynamous.ai community."
- Never run `new-long-form-anthropic` and `new-long-form-standard` against the same slug — pick one playbook per video.
- Never auto-render — even at draft quality. The user always triggers renders manually.
- Never edit the template itself when building a video. Only edit the copy under `videos/<slug>/`.
