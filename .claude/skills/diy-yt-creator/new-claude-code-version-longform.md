# new-claude-code-version-longform — Playbook

End-to-end pipeline that turns a **Claude Code release tag** (e.g. `v2.1.118`) into a previewable HyperFrames horizontal long-form video (1920x1080, 30fps, ~3-5 minutes) using the Claude Code variant at `templates/long-form/claude-code-version/`. Zero manual steps; ends at preview, never renders.

> This playbook is the variant-specific delta of [new-long-form-standard.md](./new-long-form-standard.md) for Claude Code release-update videos. Read that file first — most of the long-form pipeline is identical. The deltas are documented here.

> **For the orchestration command** (changelog WebFetch + AskUserQuestion + script draft + TTS + composition fill in one call): see [/diy-yt-creator:claude-code-version](../../commands/diy-yt-creator/claude-code-version.md). Use the orchestration command by default; this playbook documents the underlying mechanics for direct invocation, debugging, or partial reruns.

## Variant deltas vs new-long-form-standard

- **Template**: `templates/long-form/claude-code-version/` (instead of `templates/long-form/standard/`)
- **Aesthetic**: GitHub-dark (`#0D1117`) + Claude Code accent triad (cyan-blue / purple / green) + orange (warn + stat). Standard's navy + 4-accent rotation is replaced by the Claude Code palette in `tokens/long-form.css`.
- **Persistent overlay**: VersionBranding (`#version-branding`) — Anthropic + Claude Code logos top-right at 0.7 opacity + `vb-version-string` line bottom-right. Renders for full duration.
- **Brand zone**: standard's centered top-banner is **disabled** (`#top-banner { display: none }`). VersionBranding owns the brand zone. To re-enable, see "Brand-zone choice" below.
- **Scene mix**: 8-scene canonical structure mirroring the reference Remotion project at `diy-yt-creator/src/ClaudeCodeV21112-118/`:
  1. `scene-stats-opener` — 3 stats + 4-card lead-detail dive (the "biggest patch" category)
  2. `scene-feature-cards` — 6-card 3x2 highlights overview
  3. `scene-detail-headless` — Headless / SDK / CLI category dive (4 cards 2x2)
  4. `scene-detail-performance` — Performance / safety / memory category dive (4 cards 2x2)
  5. `scene-detail-plugin-system` — Plugin system / MCP category dive (4 cards 2x2)
  6. `scene-detail-terminal-ui` — Terminal rendering / scrollback / dialog fixes (4 cards 2x2)
  7. `scene-detail-network` — Networking / proxy / OAuth / Vertex AI fixes (4 cards 2x2)
  8. `scene-cta` — `$ claude update` close-out with comment + subscribe pills
- **Hard rule on visibility**: every scene anchors its GSAP timeline with `tl.set({}, {}, slot_seconds)` at the end. Without that, HyperFrames hides the wrapper as soon as the internal timeline runs out, leaving a >5s gap of bare background. Operators MUST update the anchor value when retiming a scene's slot.
- **CTA**: standard's next-video thumbnail card is replaced by an inline `$ claude update` terminal block.
- **No screenshot placeholders**: the variant ships with no `assets/screenshots/*.png` — scenes are typography-driven. Operator drops a clip at `assets/clips/demo.mp4` only if `scene-video-embed` is wired (and the scene-video-embed wrapper is uncommented in index.html — it is NOT wired by default).
- **Unwired-but-on-disk scenes**: `scene-hook`, `scene-side-by-side`, `scene-stat-pill-row`, `scene-video-embed`, `scene-terminal` (the standalone command-demo scene) remain on disk in `compositions/` but are NOT wired in `index.html` by default. Operators uncomment + add a wrapper div if they need them. The release-update format opens cold with `scene-stats-opener` (no hook intro).

## Inputs

User provides ONE of:

- A **version tag** (e.g. `v2.1.118`) — orchestration command WebFetches both changelog sources and asks for WatchNext + highlights confirmation
- A **release URL** (e.g. `https://github.com/anthropics/claude-code/releases/tag/v2.1.118`) — same flow
- A **range** (e.g. `v2.1.112-v2.1.118`) — combined release video covering the range
- A **pre-written `script.txt` + content brief** — agent skips the changelog fetch and goes straight to step 5

## Outputs

A previewable HyperFrames project at `videos/claude-code-v<NN>/` with:

- `research/changelog-marckrenn.md` + `research/changelog-official.md` — raw fetched changelogs
- `research/content-brief.md` — version-specific brief (stats, highlights, categories, terminal pick, hook angle)
- `script.txt` — narration script (520-650 words typical)
- `audio/narration.wav` — Kokoro TTS narration
- `transcript.json` — word-level timestamps
- `index.html` — root composition with `#vb-version-string` set to the real `vX.Y.Z` and scene timings tuned to transcript
- `compositions/scene-*.html` — 8 scene archetypes filled with release-specific content
- `youtube-description.md` — paste-ready YouTube metadata (chapters + SEO)
- Preview studio open in the browser at the URL printed by `hyperframes preview`

The user runs render themselves: `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/long-form.mp4`.

---

## Steps

### 1. Confirm slug + version

Derive the slug from the version tag:
- `v2.1.118` → `claude-code-v2118`
- `v2.1.112-v2.1.118` → `claude-code-v2112-118`

Confirm in one line: _"Spawning `videos/claude-code-v2118/` for Claude Code v2.1.118. Proceed?"_

### 2. Copy the template

```bash
cp -r templates/long-form/claude-code-version videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/long-form/claude-code-version videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `README.md`, `tokens/long-form.css`, `compositions/scene-*.html` (× 8) + `captions.html`, `audio/`, `assets/{shapes,sfx,screenshots,clips,anthropic-logo-light.svg,claude-code-logo-light.svg}` should all exist.

### 3. Update meta.json

```json
{
  "id": "<slug>",
  "name": "Claude Code <vX.Y.Z> — What's New"
}
```

### 4. WebFetch changelog (or load from pipeline)

If the orchestration command was used, raw markdown is already at `videos/<slug>/research/changelog-{marckrenn,official}.md` — skip to step 5.

Otherwise, fetch in parallel:
1. `https://github.com/marckrenn/claude-code-changelog/releases/tag/<tag>` — Highlights section
2. `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` — full inventory under the version anchor

Save both to `videos/<slug>/research/`. If marckrenn lacks the version (very recent), proceed with official only and note in the brief.

### 5. AskUserQuestion: WatchNext + Highlights

Two question batches:

**Batch 1 — WatchNext** (3 questions):
- WatchNext title (string)
- WatchNext URL (string)
- WatchNext one-line teaser (≤80 chars)

User can answer `skip` to omit WatchNext entirely.

**Batch 2 — Highlights** (3 questions):
- Highlights to keep (markdown checklist of marckrenn bullets)
- Custom highlights to add (free text, optional)
- Confirm category counts (features / fixes / improved) — auto-derived from official changelog

The 3 numbers feed `scene-stats-opener` directly.

### 6. Author the content brief

Write `videos/<slug>/research/content-brief.md` with sections: Version, Stats (3 numbers), Highlights (4-6 bullets), Categories, Terminal scene pick, Hook angle, WatchNext.

### 7. Draft the script

Output: `videos/<slug>/script.txt` (single flat file for `npx hyperframes tts`).

**TTS rules** (apply during writing, not post-pass):
- **NEVER open with the version number** — do NOT write "Version two point one point one two six shipped today." or any variant. Viewers already know the version from the thumbnail and title. Start `[SCENE: stats-opener]` directly with the stats: "Seven new features. Twenty five bug fixes. Seven improvements." Jump to the content immediately.
- Spell out any other version numbers that appear in the body: "version two point one point one one eight" (not "v2.1.118")
- Phonetic command names: "claude update" reads fine; "/plan" → "the plan command"
- Sentences ≤ 18 words for natural prosody
- One blank line between scenes — TTS preserves these as breath breaks
- Total length: ~520-650 words for 3-5 min runtime at speed 1.0

Sub-section the script per scene boundary:

```
[SCENE: stats-opener]
<N> new features. <N> bug fixes. <N> improvements.

The biggest cluster: <lead category> — <N> fixes landing together.
…
```

Note: the format opens **cold** on the stats scene — no hook intro, no version announcement, no preamble. The first spoken word the viewer hears is a number.

Script style mirrors the standard long-form rules — read [`.claude/references/script-library.md`](../../references/script-library.md) for the gold-standard examples.

### 8. Generate TTS

```bash
npx hyperframes tts videos/<slug>/script.txt \
  -o videos/<slug>/audio/narration.wav \
  -v am_michael \
  -s 1.0
```

### 9. Transcribe

```bash
npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
```

Produces `transcript.json` with word-level timestamps.

### 10. Compute scene boundaries

For each `[SCENE: …]` block in `script.txt`, find the timestamp of the first word in `transcript.json`. That's the scene's `data-start`. The last word's `end` value (rounded up to nearest second) is the total composition duration.

### 11. Edit the composition

Always invoke the `/hyperframes` skill before this step.

Per-video edits — exactly 4 categories of files to touch:

#### a. `tokens/long-form.css`
Per-release palette overrides are **rare** — only if a release has a special theme (e.g. a "10x faster" release that wants a green-led palette). Default: leave the variant palette untouched.

#### b. `index.html`
- `<title>` → "Claude Code <vX.Y.Z> — What's New"
- `#vb-version-string` text content → `github.com/anthropics/claude-code/releases  |  vX.Y.Z`
- Each `.scene-wrapper`'s `data-start` → from transcript word offsets at scene boundaries
- `#root data-duration` → total length (last word's `end`, ceil)
- `TOTAL_DURATION` const in `<script>` → match `#root` data-duration
- `tl.set({}, {}, TOTAL_DURATION)` at script bottom → uses the same value
- `tl.addLabel(…)` time arguments → updated to match new `data-start` set
- `crossfadeScenes(…)` calls → use the same updated label refs (the label ref is a string like `"stats-opener-=0.4"` — update if you re-named labels)

If a scene is skipped per release (e.g. `scene-video-embed` with no clip), comment out the wrapper div AND remove the matching `crossfadeScenes()` call. Don't leave dead crossfade calls — they error.

#### c. `compositions/scene-*.html`
EDIT placeholder text → real text. Per-scene quick reference (8 wired scenes; the 5 unwired-on-disk scenes are noted at the bottom):

**Wired scenes (in playback order):**

- `scene-stats-opener.html` — `#so-vbadge` → `vX.Y.Z`; `#so-overline` + `#so-headline` → release-level message; 3 `.stat-num` values → category counts; phase-2 dive (4 `.so-card` blocks) → the "biggest patch" lead category fixes (slash commands, settings, vim mode, etc.). Update the `tl.set` slot anchor + every card-entrance `at:` value to transcript word offsets.
- `scene-feature-cards.html` — 6 cards from confirmed highlights (3x2 grid). Card entrances retime via the `cardTriggers` array.
- `scene-detail-headless.html` — Headless / SDK / CLI category dive. Header overline + 4 `.dh-card` blocks. Closer banner ("Pipe it. Script it. Ship it."). Retime via `cards` array + closer `at` value.
- `scene-detail-performance.html` — Performance / safety / memory category dive. 4 `.dp-card` blocks (no closer banner).
- `scene-detail-plugin-system.html` — Plugin system / MCP category dive. 4 `.dpl-card` blocks + closer banner ("Small additions, huge for plugin authors.").
- `scene-detail-terminal-ui.html` — Terminal rendering / scrollback / dialog fixes. 4 `.dt-card` blocks (no closer).
- `scene-detail-network.html` — Networking / proxy / OAuth / Vertex AI fixes. 4 `.dn-card` blocks + closer banner ("Quiet wins for enterprise.").
- `scene-cta.html` — `#cta-debate` → release-specific debate question; the inline terminal block already shows `$ claude update`. Retime debate / terminal / pill entrances to transcript.

**Per-detail-scene timing pattern:**

Every detail scene file has the same shape — header (overline + headline) at scene_t 0, four cards entering at narration-anchored `at:` values from a `cards` array, then `tl.set({}, {}, slot_seconds)` at the end. Operators update three things per release per scene: (1) card body text, (2) the `cards[…].at` values from transcript word offsets, (3) the final `tl.set({}, {}, slot_seconds)` call to match the new slot length.

If a release has only 3 (or 5+) bullet points in a category, edit the `.dh-grid` / etc. CSS and the `cards` array together — never leave a card hidden behind opacity 0 (it'll show as a dead grid cell). Best practice: 4 cards per category. Promote bullets to make 4; cut bullets to fit 4.

**Unwired-but-on-disk scenes** (uncomment + add wrapper in index.html if needed):

- `scene-hook.html` — overline + 100px headline + slam stat + sub-line
- `scene-side-by-side.html` — A vs B contrast (e.g. before/after release)
- `scene-stat-pill-row.html` — 2 hero stats (e.g. "10× faster", "70% fewer crashes")
- `scene-video-embed.html` — leave commented unless screencap clip exists at `assets/clips/demo.mp4`
- `scene-terminal.html` — standalone command demo (e.g. `/plan`, `/vim`); the inline `$ claude update` terminal in `scene-cta` covers the CTA need

Placeholder text in the bare template is deliberately bland — replace ALL of it.

#### d. `meta.json`
Already updated in step 3. Re-check.

### 11b. Wire SFX (MANDATORY — every release video)

**Run after `index.html` timing is final** (data-starts and TOTAL_DURATION set).

**Step 1 — sync cue files:**
```bash
bash scripts/sync-video-sfx.sh videos/<slug> cinematic-whoosh spring-pop
```

**Step 2 — add audio elements to `index.html`** immediately after `<audio id="narration">`, before the film-grain SVG. Standard pattern for this 8-scene format:

```html
<!-- SFX: cinematic-whoosh on every scene transition (track 3, sequential) -->
<audio id="sfx-whoosh-1" class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<feature-cards data-start - 0.40>"  data-duration="1.5" data-track-index="3" data-volume="0.11"></audio>
<audio id="sfx-whoosh-2" class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<detail-headless data-start - 0.40>"  data-duration="1.5" data-track-index="3" data-volume="0.11"></audio>
<!-- … repeat for each remaining transition … -->

<!-- SFX: spring-pop on first card entrance in each scene (track 4, sequential) -->
<audio id="sfx-pop-so"  class="clip" src="assets/sfx/spring-pop.mp3"
       data-start="0.06"  data-duration="0.4" data-track-index="4" data-volume="0.11"></audio>
<audio id="sfx-pop-fc"  class="clip" src="assets/sfx/spring-pop.mp3"
       data-start="<feature-cards data-start + card-1 internal time>"  data-duration="0.4" data-track-index="4" data-volume="0.11"></audio>
<!-- … repeat for each scene … -->
```

**Whoosh timing rule**: `data-start = scene_data_start - 0.40` (fires at crossfade start, 400ms before scene fades in).

**Pop timing rule**: `data-start = scene_data_start + card-1_internal_at` (exact word onset of the first card entrance in each scene, looked up from `transcript.json`).

**Track rules**: all whooshes share track 3 (sequential — no overlap). All pops share track 4 (sequential — no overlap). Volume hard cap 0.25; use 0.11 for both cues.

### 12. Lint + inspect + validate

```bash
npx hyperframes lint     videos/<slug>     # MUST pass with 0 errors
npx hyperframes validate videos/<slug>     # WCAG AA contrast audit
npx hyperframes inspect  videos/<slug>     # layout overflow check
```

Common lint issues specific to this variant:

| Error | Cause | Fix |
|---|---|---|
| `duplicate_media_discovery_risk` | Re-enabled `#top-banner` with same source as VersionBranding | Use a different wordmark (e.g. `claude-logo-light.svg`) for the top banner |
| `audio_src_not_found` | `narration.wav` missing | Re-run step 8; check filename |
| `overlapping_gsap_tweens` | Two crossfades targeting the same `.scene-wrapper` at the same time | Adjust scene timing or remove duplicate `crossfadeScenes()` call |

### 13. Open preview (final step — never render)

```bash
npx hyperframes preview videos/<slug>
```

Capture the URL.

### 14. Generate YouTube description

**MUST follow [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md) end-to-end.**
That rule is the single source of truth for the description format, vidIQ
research workflow, SEO requirements, brand link block, chapter timestamp math,
link validation, and engagement-CTA structure. Do not improvise structure.

Quick workflow checklist (the rule has full detail):

1. **vidIQ keyword research** — run `vidiq_keyword_research`, `vidiq_outliers`,
   and `vidiq_trending_videos` per the rule. Save the snapshot to
   `videos/<slug>/research/vidiq-keywords.md`.
2. **Compute chapter timestamps** — `data-start ÷ speed_factor` (default
   speed_factor = 1.0; if the MP4 was ffmpeg-sped per
   [`.claude/rules/video-speedup.md`](../../rules/video-speedup.md), divide by
   that factor). Format `M:SS`. First chapter is always `0:00`. Min 10s gap.
3. **Draft `videos/<slug>/youtube-description.md`** — LEAN structure per the
   rule: SEO hook (keyword-front-loaded; pack the top 3-5 features inline as a
   comma-separated list — NOT as a separate Key Changes bullet block) →
   Dynamous block in `----` separators → `Chapters` header line + chapter list
   (long-form has chapters) → Resources: with validated URLs → Hostinger
   affiliate block in `----` separators (MANDATORY: `🏠 Self-host your AI
   agents & projects on Hostinger (10% OFF): 👉
   https://hostinger.com/DIYSMARTCODE`) → debate question (matches script's
   final line) → 15-25 hashtags. **NO Key Changes / Key Concepts / Key Stats
   bullet sections — explicitly cut.** Fold any `$ claude update` CTA into the
   hook paragraph if needed (no standalone CTA block).
4. **Validate every URL** with `WebFetch` — replace 404/redirect chains with
   working URLs. Long-form descriptions should stay under ~3000 chars total.

### 15. Report to the user

```
✅ Claude Code <vX.Y.Z> — What's New
   Slug:      <slug>
   Render:    npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/long-form.mp4
   Length:    <N>m <M>s
   YouTube:   videos/<slug>/youtube-description.md (paste-ready)
   WatchNext: <title or "skipped">
   Highlights: <count> cards
   Stats:     <features> / <fixes> / <improved>
   Preview:   http://localhost:5173
```

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes validate videos/<slug>` → AA contrast on all text
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow at any sample
- [ ] `#vb-version-string` shows the real version (not `vX.Y.Z`)
- [ ] All 6 feature-cards populated with real highlights (no "Feature title one")
- [ ] All 3 stats-opener pills show real numbers (not `0`)
- [ ] Scene `data-start` values match transcript word offsets (not template demo defaults: 0/12/32/55/70/90/105/115)
- [ ] Audio element uncommented and `data-duration` matches narration length
- [ ] Preview URL reachable (the `hyperframes preview` command is still running)

---

## Brand-zone choice

The variant ships with `#top-banner { display: none }` so VersionBranding (top-right logos + bottom-right URL) is the single brand surface. This is the right default for almost every release video.

To re-enable a centered top-banner per video:

1. Choose a wordmark file that is NOT already used in VersionBranding (`anthropic-logo-light.svg` is taken). Suggested: `claude-logo-light.svg`.
2. Copy it into `assets/`: `cp shared/logos/claude-logo-light.svg videos/<slug>/assets/`.
3. Edit `index.html`: remove the `style="display:none;"` on `#top-banner` and replace the `<span id="top-banner-logo">` with `<img id="top-banner-logo" src="assets/claude-logo-light.svg" alt="Claude" />`.
4. Restore the `tl.from("#top-banner", { y: -16, opacity: 0, duration: 0.6, ease: "power2.out" }, 0.2)` call in the root timeline.
5. Re-lint — must remain 0 errors, 0 warnings (different src than VersionBranding's anthropic logo avoids the duplicate-media-discovery-risk).

---

## Don'ts

- Never auto-render — user explicitly always triggers render manually.
- Never fabricate stats, dates, command names, or version strings. Pull from the changelog or ask the user.
- Never modify `templates/long-form/claude-code-version/` — only the copy under `videos/<slug>/`.
- Never reuse `anthropic-logo-light.svg` for the top-banner (it's in VersionBranding — lint will flag duplicate-media-discovery-risk).
- Never leave the `vX.Y.Z` placeholder in `#vb-version-string`, `scene-stats-opener`'s `#so-vbadge`, or anywhere else — set the real version once per release.
- Never use `repeat: -1`, `Math.random()`, `Date.now()`, or network fetches in the composition.
- Never animate `<audio>` or `<video>` directly. Wrapper div takes the clip role for video; audio uses `data-start/duration/track-index`.
- Never use lyrical music under narration. Long-form bg-music goes on track 3 — see [`.claude/rules/audio-design.md`](../../rules/audio-design.md).
- Never run multiple `claude-code-version` invocations in parallel against the same slug.
