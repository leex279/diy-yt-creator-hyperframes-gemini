---
description: "Spawn a Claude Code release-update long-form video end-to-end from a version tag or release URL"
argument-hint: <version-tag | release-URL>  (e.g. v2.1.118)
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebSearch, WebFetch, AskUserQuestion
---

<objective>
Drive a Claude Code release-update video end-to-end from a single version tag.

Takes a version (e.g. `v2.1.118`) or release URL and produces a fully wired `videos/claude-code-v<NN>/` project ready for `npx hyperframes preview` + `npx hyperframes render`. Uses the [`templates/long-form/claude-code-version/`](../../../templates/long-form/claude-code-version/) variant. Output target render: ~3-5 minute, 1920x1080 30fps MP4 with VersionBranding overlay, terminal scene, stats opener, and `$ claude update` CTA.

**Output**: `videos/claude-code-v<NN>/out/long-form.mp4` + `videos/claude-code-v<NN>/youtube-description.md`.
</objective>

<process>

### Step 0 — Slug + idempotency gate

Derive the slug from `$ARGUMENTS`:
- `v2.1.118` → `claude-code-v2118`
- `v2.1.112-v2.1.118` → `claude-code-v2112-118` (range release)
- A `https://github.com/anthropics/claude-code/releases/tag/v2.1.118` URL → extract the tag and apply rule 1.

If `videos/<slug>/` already exists:
- Read `videos/<slug>/meta.json` and confirm with the user before overwriting.
- If meta confirms the same version, **stop and let the user manually rerun specific steps** rather than blindly overwriting in-progress work.

### Step 1 — Fetch the changelog (parallel WebFetch)

Two sources, fetched in parallel:

1. `https://github.com/marckrenn/claude-code-changelog/releases/tag/<tag>` — the **Highlights** section (curated, narrative-friendly).
2. `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` — full inventory under the version's anchor (`#vX.Y.Z`).

Save raw markdown to `videos/<slug>/research/changelog-marckrenn.md` and `videos/<slug>/research/changelog-official.md` for later reference.

If marckrenn lacks the version (very recent), proceed with the official changelog only and note the gap in the content brief.

### Step 1.5 — AskUserQuestion: WatchNext

Ask the user which previously-published Claude Code video should be the WatchNext recommendation. Schema:

```
Question 1: WatchNext title (string)
Question 2: WatchNext URL (string, e.g. https://youtu.be/...)
Question 3: WatchNext one-line teaser (string, ≤80 chars)
```

If the user types `skip`, omit WatchNext entirely from the composition (no scene insertion, no chapter entry, no description link).

### Step 1.6 — AskUserQuestion: Highlights selection

Show the marckrenn Highlights bullets. Ask the user to confirm or edit the 4-6 highlights for `scene-feature-cards` (3x2 grid). Schema:

```
Question 1: Highlights to keep (markdown checklist of marckrenn bullets, user toggles)
Question 2: Custom highlights to add (free text, optional)
Question 3: Confirm category counts (features / fixes / improved) — auto-derived from official changelog, user can override
```

The 3 numbers feed `scene-stats-opener` directly (cyan / purple / green pills).

### Step 2 — Spawn the video directory

```bash
cp -r templates/long-form/claude-code-version videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/long-form/claude-code-version videos/<slug>`.

Update `videos/<slug>/meta.json`:

```json
{
  "id": "<slug>",
  "name": "Claude Code <vX.Y.Z> — What's New"
}
```

### Step 3 — Author the content brief

Write `videos/<slug>/research/content-brief.md` with sections:

- **Version** — full tag (e.g. `v2.1.118`).
- **Stats** — 3 numbers for the stats-opener (features / fixes / improved).
- **Highlights** — 4-6 user-confirmed bullets for `scene-feature-cards` (3x2 layout).
- **Categories** — per-category change groupings derived from the official changelog (use `scene-feature-cards` with `--2x2` or `--stack` layout for category sub-scenes).
- **Terminal scene pick** — choose one notable command demo (`/plan`, `/vim`, `/compact`, etc.) for `scene-terminal`. Default `$ claude update` if no clear candidate.
- **Hook angle** — the most compelling release-level differentiator for `scene-hook`.
- **WatchNext** — copied from Step 1.5.

### Step 4 — Write the narration script

Output: `videos/<slug>/script.txt` (single flat file for `npx hyperframes tts`).

TTS optimization rules (apply during writing, NOT as a post-pass):

- Spell out version numbers: "version two point one point one one eight" (not "v2.1.118").
- Use natural phonetic forms for command names: "claude update" reads fine; "/plan" → "the plan command".
- Keep sentences ≤ 18 words for natural prosody.
- One blank line between scenes — TTS preserves these as breath breaks.
- Total length target: ~520-650 words for 3-5 min runtime at 1.0× speed.

Sub-section the script per scene boundary so the operator can later place `data-start` markers:

```
[SCENE: hook]
…hook narration…

[SCENE: stats-opener]
…stats narration…
```

### Step 5 — Generate TTS

```bash
npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav -v am_michael -s 1.0
```

Defaults: voice `am_michael`, speed 1.0, output `narration.wav`. If a different voice is registered as the channel default, swap `-v` accordingly.

### Step 5.5 — Transcribe for word-level timestamps

```bash
npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
```

Produces `videos/<slug>/transcript.json` with `[ { word, start, end }, … ]`. Used in Step 8 to align scene `data-start` values to spoken-word landmarks.

### Step 6 — Drop placeholder note

(There is no `timing.ts` step in HyperFrames — `data-start` lives on each scene wrapper directly in `index.html`. This step is intentionally a no-op.)

### Step 7 — Populate per-scene content (compositions/*.html)

EDIT (do not regenerate) each WIRED scene file in `videos/<slug>/compositions/`. The 8-scene canonical structure mirrors the reference Remotion video:

- `scene-stats-opener.html` — `#so-vbadge` → `vX.Y.Z`; `#so-overline`, `#so-headline` → release-level message; 3 `.stat-num` values → category counts. Phase-2 dive (4 `.so-card` blocks) → the "biggest patch" lead category fixes (whichever single category dominates this release: slash commands, settings, vim, etc.).
- `scene-feature-cards.html` — populate 6 cards (3x2 grid) from the user-confirmed highlights.
- `scene-detail-headless.html` — Headless / SDK / CLI category dive. 4 `.dh-card` blocks + closer banner ("Pipe it. Script it. Ship it." or similar release-specific tagline).
- `scene-detail-performance.html` — Performance / safety / memory category dive. 4 `.dp-card` blocks (no closer).
- `scene-detail-plugin-system.html` — Plugin system / MCP category dive. 4 `.dpl-card` blocks + closer banner.
- `scene-detail-terminal-ui.html` — Terminal rendering / scrollback / dialog fixes. 4 `.dt-card` blocks (no closer).
- `scene-detail-network.html` — Networking / proxy / OAuth / Vertex AI fixes. 4 `.dn-card` blocks + closer banner.
- `scene-cta.html` — `#cta-debate` → release-specific debate question; the inline terminal block already shows `$ claude update`.

If a release has fewer than ~12 cards' worth of detail content total, drop the weakest detail scene (e.g. cut `scene-detail-network` if there are no networking changes) and adjust the wiring + crossfade list in `index.html`. Always keep the slot anchor `tl.set({}, {}, slot_seconds)` at the end of every detail scene's GSAP timeline — without it the wrapper hides as soon as the internal timeline runs out and you'll see a >5s gap of bare background.

**Unwired-but-on-disk** scenes (`scene-hook`, `scene-side-by-side`, `scene-stat-pill-row`, `scene-video-embed`, `scene-terminal`) remain in `compositions/` for video-specific overrides — uncomment + add a wrapper in `index.html` if the release calls for them. The release-update format opens cold with `scene-stats-opener` (no hook intro).

Placeholder text in the bare template is deliberately bland — replace ALL of it before render.

### Step 8 — Wire timing in `index.html`

EDIT `videos/<slug>/index.html`:

- `#vb-version-string` text content → `github.com/anthropics/claude-code/releases  |  vX.Y.Z` (real version).
- Each `.scene-wrapper`'s `data-start` → derived from `transcript.json` word offsets at scene boundaries (look up the first word of each `[SCENE: …]` block).
- `#root` `data-duration` → total narration length (last word's `end` value, ceil to nearest second).
- `TOTAL_DURATION` const in `<script>` → match `#root` data-duration.
- `tl.set({}, {}, TOTAL_DURATION)` at script bottom → uses the same value.
- The `tl.addLabel(…)` and `crossfadeScenes(…)` calls → bump the time argument on each label/call to match the new `data-start` set.

If a scene is skipped per release (e.g. `scene-video-embed` with no clip), comment out the wrapper div AND remove the matching crossfade call. Don't leave dead crossfade calls — they'll throw `gsap.utils` errors.

### Step 9 — Validate

```bash
npx hyperframes lint videos/<slug>           # MUST pass with 0 errors
npx hyperframes validate videos/<slug>       # WCAG AA contrast audit
npx hyperframes inspect videos/<slug>        # layout overflow check
npx hyperframes preview videos/<slug>        # studio preview at localhost:5173
```

Fix all errors before render. Warnings about `audio_src_not_found` should disappear once narration is in place; if they persist, check the `<audio>` element is uncommented in `index.html`.

### Step 9.5 — YouTube description

**MUST follow [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md) end-to-end.** That rule is the single source of truth for the description format and SEO requirements. Do NOT improvise structure, hashtags, or CTA placement.

Mandatory in this exact order:

1. **vidIQ keyword research** — call `vidiq_keyword_research`, `vidiq_outliers`, and `vidiq_trending_videos` against 3-5 seed terms (e.g., "Claude Code", "AI coding agent", "claude code update"). Save the snapshot to `videos/<slug>/research/vidiq-keywords.md`.
2. **Compute chapter timestamps** — `chapter_seconds = scene.data_start ÷ speed_factor`. The default `speed_factor = 1.0`. If the MP4 was post-processed via ffmpeg `setpts/atempo` per [`.claude/rules/video-speedup.md`](../../rules/video-speedup.md), divide by that factor (e.g. 1.1). Format `M:SS`, first chapter is `0:00`, minimum 10s gap between chapters.
3. **Draft `videos/<slug>/youtube-description.md`** — LEAN structure per the rule: SEO hook (keyword-front-loaded, primary keywords in first 200 chars; if useful, name the top 3-5 features inline as comma-separated — NOT as bullets) → Dynamous CTA in `----` separators → `Chapters` header line + chapter list (long-form has chapters) → Resources: (validated URLs with keyword-rich anchor text) → Hostinger affiliate block in `----` separators (MANDATORY: `🏠 Self-host your AI agents & projects on Hostinger (10% OFF): 👉 https://hostinger.com/DIYSMARTCODE`) → polarizing debate question (must match script's final line) → 15-25 hashtags drawn from the vidIQ shortlist. **NO Key Changes / Key Concepts / Key Stats bullet sections. NO standalone `$ claude update` CTA block** — fold update command into hook paragraph if needed.
4. **Validate every URL** with `WebFetch` — replace 404 / redirect chains with working URLs. Keep total description under ~3000 chars.

### Step 10 — Render

```bash
npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/long-form.mp4
```

Verify flag set with `npx hyperframes docs rendering` if a future CLI version drops `--workers` or renames `--quality`. Default render: 1920x1080, 30fps, h264.

### SFX volume calibration

Per [`.claude/rules/audio-design.md`](../../rules/audio-design.md) (post-2026-04-28 calibration), all SFX `data-volume` values are 25% lower than legacy Remotion projects:

| Cue | New | Old (do NOT use) |
|---|---|---|
| `impact-slam` | `0.15` | 0.20 |
| `scale-slam` | `0.15` | 0.20 |
| `screen-shake` | `0.11` | 0.15 |
| `cinematic-whoosh` | `0.11` | 0.15 |
| `spring-pop` | `0.11` | 0.15 |
| `pop` | `0.10` | 0.13 |
| `glitch-zap` | `0.09` | 0.12 |
| `sonic-logo` | `0.45` | 0.60 |

Hard cap 0.25 on every per-scene SFX. Lint enforces.

### When to skip the WatchNext scene

If Step 1.5 returned `skip`, the variant's standard scene mix (8 scenes, no WatchNext) carries the video unchanged. Don't insert a placeholder WatchNext — visually distracting and out-of-band.

### Brand-zone note

The variant ships with `#top-banner { display: none }` — VersionBranding owns the brand zone. Don't re-enable the centered top-banner unless the release video calls for a third brand cue (rare). If you do, source the wordmark from a file that isn't already in VersionBranding (`anthropic-logo-light.svg` is taken).

</process>

<output_report>

After Step 10 completes, print to the user:

```
✅ Claude Code <vX.Y.Z> — What's New
   Slug:      <slug>
   Render:    videos/<slug>/out/long-form.mp4
   Length:    <N> minutes <M> seconds
   YouTube:   videos/<slug>/youtube-description.md (paste-ready)
   WatchNext: <title or "skipped">
   Highlights: <count> cards
   Stats:     <features> features / <fixes> fixes / <improved> improved
```

Then:
1. Suggest opening `videos/<slug>/out/long-form.mp4` to verify
2. Suggest uploading to YouTube with the generated description
3. Note that `transcript.json` is preserved — re-runs of Step 8 (timing) don't need to re-transcribe

</output_report>
