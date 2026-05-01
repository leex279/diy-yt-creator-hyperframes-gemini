# new-claude-code-version-short — Playbook

End-to-end pipeline that turns a **Claude Code release tag** (e.g. `v2.1.118`) into a previewable HyperFrames vertical Short (1080x1920, 30fps, **≤3 minutes** — target ~70-130s) using the Claude Code shorts variant at [`templates/shorts/claude-code-version/`](../../../templates/shorts/claude-code-version/). Zero manual steps; ends at preview, never renders.

> This playbook is the variant-specific delta of [new-anthropic-short.md](./new-anthropic-short.md) for Claude Code release-update Shorts. Read that file first — most of the shorts pipeline is identical. The deltas are documented here.

> **Reuses existing long-form research when present.** If the user already shipped (or started) a long-form video for the same release at `videos/claude-code-v<NN>/`, this playbook reads its `research/content-brief.md`, `research/changelog-*.md`, and `script.txt` instead of re-fetching the changelog. Saves a WebFetch round-trip and keeps the stats / highlights consistent across both cuts of the release.

## Variant deltas vs new-anthropic-short

- **Template**: `templates/shorts/claude-code-version/` (instead of `templates/shorts/anthropic/`)
- **Aesthetic**: GitHub-dark (`#0D1117`) + Claude Code accent triad (cyan-blue / purple / green) + orange (warn + Subscribe pulse). Anthropic shorts' warm off-white + Claude orange is replaced by the Claude Code palette in `tokens/claude-code-dark.css`.
- **Persistent overlay**: VersionBranding (`#version-branding`) — Anthropic + Claude Code logos top-right at 0.7 opacity + `vb-version-string` line bottom-center. Renders for full duration.
- **Brand zone**: anthropic shorts' centered top-banner is **disabled** (`#top-banner { display: none }`). VersionBranding owns the brand zone.
- **Phase mix**:
  1. **Phase 1 — Version slam**: overline ("Claude Code Update") + "Version" pre-line + 200px slam version (e.g. `v2.1.118`, cyan-blue) + caption pill ("What's new in 90 seconds")
  2. **Phase 2 — Stats opener (3 pills)**: features / fixes / improved counts (cyan / purple / green)
  3. **Phase 3 — Highlight cards (numbered, not dated)**: top 3 highlights with `01/02/03` badges (cyan / purple / green)
  4. **Phase 4 — `$ claude update` CTA**: macOS terminal block + Subscribe pill (Claude Code orange pulse, `yoyo: true, repeat: 4`)
- **Hard rule**: same as anthropic shorts — every timed element needs `class="clip"` + `data-start` + `data-duration` + `data-track-index`. Audio elements never get `class="clip"`.
- **Duration**: target **≤180s** (YouTube Shorts hard max). Sweet spot for a release update is **70-130s** so the highlights breathe but the watch-through stays intact. Don't blow past 130s unless the release has a once-in-a-quarter shape (≥7 highlights worth showing); even then, cap at 150s.
- **No background music**: shorts hard rule. Narration + SFX only.

## Inputs

User provides ONE of:

- A **version tag** (e.g. `v2.1.118`)
- A **release URL** (e.g. `https://github.com/anthropics/claude-code/releases/tag/v2.1.118`)
- A **range** (e.g. `v2.1.119-v2.1.123`) — combined release Short covering the range; pick top 3 highlights across the range
- An existing **long-form slug** (e.g. `claude-code-v2118`) — short cut spawned from the long-form's research
- A **pre-written `script.txt`** + per-phase plan — agent skips drafting (jump to step 6)

If the topic has no real source (no changelog reachable, no user-supplied facts), **stop and ask the user for a source URL** before proceeding. Never invent stats, highlight titles, or version numbers.

## Outputs

A previewable HyperFrames project at `videos/claude-code-v<NN>-short/` (note the `-short` suffix to disambiguate from the long-form's `videos/claude-code-v<NN>/`) with:

- `research/content-brief.md` — version-specific brief (stats + top 3 highlights + hook angle); copied or distilled from the long-form when present
- `research/changelog-marckrenn.md` + `research/changelog-official.md` — only fetched if no long-form exists for this version
- `script.txt` — narration script (~140-260 words for 70-130s at speed 1.05)
- `audio/narration.wav` — ElevenLabs TTS narration (via `python scripts/elevenlabs-tts.py … --shorts`)
- `transcript.json` — word-level timestamps from ElevenLabs alignment
- `index.html` — composition filled with real content (version slam, 3 stats, 3 highlight cards, terminal CTA), transitions sync'd to spoken-word frames
- `youtube-description.md` — paste-ready YouTube metadata (chapters optional for Shorts, but Dynamous CTA + hashtags required)
- Preview studio open at `http://localhost:5173`

The user runs render themselves: `npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4`.

---

## Steps

### 1. Confirm slug + version

Derive the slug from the version tag with the `-short` suffix:

- `v2.1.118` → `claude-code-v2118-short`
- `v2.1.119-v2.1.123` → `claude-code-v2119-123-short`
- A `https://github.com/anthropics/claude-code/releases/tag/v2.1.118` URL → extract the tag, then apply rule 1

Confirm in one line: _"Spawning `videos/claude-code-v2118-short/` for Claude Code v2.1.118 (≤3 min vertical Short). Proceed?"_

### 2. Reuse-detection — does a long-form exist?

Check whether `videos/claude-code-v<NN>/` (no `-short` suffix) already exists. If YES:

1. READ `videos/claude-code-v<NN>/meta.json` to confirm the version matches.
2. READ `videos/claude-code-v<NN>/research/content-brief.md` — pull the **stats** (features / fixes / improved counts) and **highlights** verbatim.
3. READ `videos/claude-code-v<NN>/research/changelog-marckrenn.md` (and `changelog-official.md`) — for any sharper phrasing of a highlight title.
4. READ `videos/claude-code-v<NN>/script.txt` — for narration tone reference (NOT to copy verbatim — the Short must be much tighter).
5. Skip Step 3 (changelog WebFetch) entirely.
6. Note in the new video's brief: _"Reused research from `videos/claude-code-v<NN>/` (long-form spawned YYYY-MM-DD)."_

If a long-form does NOT exist, proceed to Step 3.

### 3. Fetch the changelog (only if no long-form to reuse)

Two sources, fetched in parallel (mirrors [/diy-yt-creator:claude-code-version](../../commands/diy-yt-creator/claude-code-version.md) Step 1):

1. `https://github.com/marckrenn/claude-code-changelog/releases/tag/<tag>` — the **Highlights** section (curated, narrative-friendly).
2. `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` — full inventory under the version's `#vX.Y.Z` anchor.

Save raw markdown to `videos/<slug>/research/changelog-marckrenn.md` and `videos/<slug>/research/changelog-official.md`.

If marckrenn lacks the version, proceed with the official changelog only and note the gap in the brief.

### 4. Copy the template

```bash
cp -r templates/shorts/claude-code-version videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/shorts/claude-code-version videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `sfx-cues.txt`, `tokens/claude-code-dark.css`, `DESIGN.md`, `README.md`, `audio/`, `assets/` (with `anthropic-logo-light.svg`, `claude-code-logo-light.svg`, `shapes/`, `sfx/`) should all exist.

### 5. Update meta.json

```json
{
  "id": "<slug>",
  "name": "Claude Code <vX.Y.Z> — Short"
}
```

For ranges: `"name": "Claude Code v2.1.119-v2.1.123 — Short"`.

### 5.5. Ask: Add Dynamous promotion?

Same opt-in as anthropic shorts (see [new-anthropic-short.md](./new-anthropic-short.md) Step 3.5). Default NO. On YES, follow [`videos/_template-wiring-snippet.md`](../../../videos/_template-wiring-snippet.md) Steps 1-7 — the badge + endcard + module interstitial are template-agnostic and work the same here as on anthropic shorts.

### 6. Author the content brief

Write `videos/<slug>/research/content-brief.md` with sections:

- **Version** — full tag (e.g. `v2.1.118`).
- **Reused-from** — `videos/claude-code-v<NN>/` if Step 2 found a long-form, else "fresh fetch".
- **Stats** — 3 numbers for the stats opener (features / fixes / improved). If reused from long-form: copy the same numbers verbatim. If fresh: derive from official changelog (count `### Features`, `### Fixes`, `### Improvements` sections; ask user to confirm if categories are unclear).
- **Top 3 highlights** — the 3 most impactful changes for Phase 3's numbered cards. If reused from long-form: pick the top 3 from its 4-6 highlights. If fresh: shortlist 3-5 from marckrenn's Highlights section, then ask the user which 3 to keep.
- **Hook angle** — the single most compelling release-level differentiator (one sentence). E.g. "v2.1.118 finally makes /config persist", "v2.1.119 ships plugin system v1", etc.
- **Caption pill text** — Phase 1's caption (e.g. "What's new in 90 seconds", "Top 3 changes", "ships <date>").

### 7. Draft the script

This step has two branches.

#### Branch A — pipeline output exists (preferred for shorts)

Same as anthropic shorts Branch A (see [new-anthropic-short.md](./new-anthropic-short.md) Step 4 Branch A): if `videos/<slug>/scripts/full-script.md` exists from the `/diy-yt-creator:full-auto` pipeline, READ it as authoritative.

#### Branch B — direct draft (typical for shorts)

Map narration to the four phase archetypes the template ships:

| Phase | Duration target | What to write |
|---|---|---|
| **1 — Version slam** | 5-7s | Mono overline (2-3 words, ALL CAPS): "CLAUDE CODE UPDATE". Pre-line (1 word, ALL CAPS): "Version". Slam version (e.g. "v2.1.118") — read aloud as "version two point one point one one eight" in the script (TTS rule). Caption pill (4-8 words, e.g. "What's new in 90 seconds"). |
| **2 — Stats opener** | 6-8s | Mono overline. Headline (3-7 words, e.g. "The receipts."). Three stat numbers + labels: features / fixes / improved. Numbers MUST be real. |
| **3 — Highlight cards** | 12-20s (the heart of the Short) | Mono overline ("TOP CHANGES"). 3 numbered cards (`01/02/03`): each card has a title (3-5 words) + sub (3-6 words). Real highlights only — never invent. |
| **4 — CTA** | 4-6s | Mono overline ("PULL EVERY FIX"). Terminal already shows `$ claude update`. Subscribe pill stays as "Subscribe". Narration calls out the command + asks for a debate / comment line if Phase 3 budget allows. |

**Style rules for narration text** (apply during writing, NOT as a post-pass):

- Spell out version numbers: "version two point one point one one eight" (not "v2.1.118").
- Phonetic command names: "claude update" reads fine; `/config` → "the config command".
- Sentences ≤ 18 words for natural Kokoro prosody.
- Never use semicolons or em-dashes — Kokoro stumbles. Use periods.
- Numbers: write digits, not words ("3 fixes", not "three fixes") — matches the visual stat pills. Exception: version numbers (rule 1).
- Read [`.claude/references/script-library.md`](../../references/script-library.md) for gold-standard examples.
- Total target: **~140-260 words** for **70-130s** runtime at speed 1.05. Don't pad — release Shorts win on tightness.
- If the release is thin (≤2 highlights worth showing), drop to 60-70s with **2** highlight cards instead of 3 — edit Phase 3 down (remove `#p3-card-3` and the `tl.from("#p3-card-3", …)` tween) and adjust phase timing.

Save to `videos/<slug>/script.txt` using the standard 4-block format (one phase per blank-line block):

```
[phase 1 narration]

[phase 2 narration]

[phase 3 narration]

[phase 4 narration]
```

The blank lines are NOT spoken; they help map narration to phases later.

### 7.5. (Optional) Trust-signal screenshot

Skip for release-update Shorts by default — the persistent VersionBranding overlay + the explicit version slam (`v2.1.118`) already serve as the trust signal. Only capture a release-page screenshot if the user explicitly asks for it; if so, follow [new-anthropic-short.md](./new-anthropic-short.md) Step 4.6 (Playwright screenshot of the GitHub release page) and wire it into Phase 1 per Step 8.4 there.

### 8. Generate TTS + transcript (one shot, ElevenLabs)

```bash
python scripts/elevenlabs-tts.py videos/<slug> --shorts
```

This writes BOTH `videos/<slug>/audio/narration.wav` AND `videos/<slug>/transcript.json` in a single API call. Voice ID, model ID, voice settings, and the pronunciation dictionary are loaded from the repo-root `.env`. The `--shorts` flag selects `ELEVENLABS_SPEED_SHORTS` over `ELEVENLABS_SPEED`.

If the script changes, re-run this command — it overwrites both files atomically.

### 9. Transcript verification

Confirm `videos/<slug>/transcript.json` exists and the last word's `end` matches the audio duration printed by the script (within 0.1s).

### 10. Compute phase boundaries

Read `transcript.json` and identify, in seconds:

- `phase1_end` — `end` time of the last word of the phase 1 narration block (the version slam line)
- `phase2_end` — same for phase 2 (stats opener)
- `phase3_end` — same for phase 3 (3 highlight cards)
- `phase4_end` — `end` time of the last word in the file
- `total_duration` = `phase4_end + 1.5` (1.5s tail for reading the CTA before loop)

Then compute the GSAP timeline anchors:

```
T1 = phase1_end - 0.2     // start phase1→phase2 transition 0.2s before last word
T2 = phase2_end - 0.2
T3 = phase3_end - 0.2

P2 = T1 + 0.4             // phase2 entrance anchor
P3 = T2 + 0.4
P4 = T3 + 0.4
```

Identify the timestamp of the **slam version word** in phase 1 (the version number itself, e.g. "two point one point one one eight" — the last word of the spoken version). That's the new value for the inline-shake offsets:

```
slam_t = transcript[<slam-word-index>].start
shake_offsets = [slam_t, slam_t + 0.05, slam_t + 0.10, slam_t + 0.15]
```

For Phase 3's per-card entrances, identify the spoken-anchor for each card's first word:

```
card_1_at = transcript[<card-1-anchor-word>].start - P3   // expressed relative to P3 anchor
card_2_at = transcript[<card-2-anchor-word>].start - P3
card_3_at = transcript[<card-3-anchor-word>].start - P3
```

For Phase 4's terminal entrance, identify the spoken-anchor for "claude update" or the CTA verb:

```
terminal_at = transcript[<terminal-anchor-word>].start - P4
subscribe_at = transcript[<subscribe-anchor-word>].start - P4   // typically "subscribe" itself
```

### 11. Edit `videos/<slug>/index.html`

Always invoke the `/hyperframes` skill before this step.

Edit in this exact order (one Edit per change):

1. **`<title>`** in `<head>` → `Claude Code <vX.Y.Z> — Short`
2. **`<div id="root">`** `data-duration` → `total_duration` (rounded to 0.1s)
3. **`#vb-version-string`** text content → `github.com/anthropics/claude-code/releases  |  vX.Y.Z` (real version)
4. **Phase 1**:
   - `#p1-overline` → e.g. "Claude Code Update" (or release adjective like "Claude Code v2.1.118 ships")
   - `#p1-pre` → "Version" (or release-specific adjective like "Patch", "Major")
   - `#p1-hero` → real `vX.Y.Z` (the slam target — keep tabular-nums for digit alignment)
   - `#p1-caption` → caption pill text from brief (e.g. "What's new in 90 seconds")
5. **Phase 2**:
   - `#p2-overline` → e.g. "What shipped"
   - `#p2-headline` → e.g. "The receipts." (or "Three releases. The receipts." for ranges)
   - Each `.stat-pill` `.stat-num` → real count; `.stat-label` stays as `features` / `fixes` / `improved` unless the brief overrides
6. **Phase 3**: each `.hl-card`'s `.hl-title` + `.hl-sub` → real highlight text (one card per top highlight, in priority order). Number badges (`01/02/03`) and accent rotation (cyan/purple/green) stay as-is. If the release has only 2 highlights worth showing, comment out `#p3-card-3` AND remove the matching tween (`tl.from("#p3-card-3", …)`).
7. **Phase 4**: `#p4-overline` → e.g. "Pull every fix". Terminal stays at `$ claude update`. Subscribe pill stays as "Subscribe".
8. **Transition timestamps**: replace `const T1 = 5.6;`, `const T2 = 11.6;`, `const T3 = 17.6;` with computed values
9. **Phase anchors**: replace `const P2 = 6.4;`, `const P3 = 12.4;`, `const P4 = 18.4;` with computed values
10. **Per-card anchors** (Phase 3): replace `P3 + 0.5` / `P3 + 0.95` / `P3 + 1.4` with `P3 + card_1_at` / `P3 + card_2_at` / `P3 + card_3_at`. (Or use absolute computed values if more readable.)
11. **Terminal + subscribe anchors** (Phase 4): replace `P4 + 0.5` (terminal entrance) and `P4 + 1.5` (subscribe entrance) + `P4 + 1.8` (subscribe pulse) with the computed `terminal_at` / `subscribe_at` values.
12. **Progress bar tween**: change `duration: 24` (in the `#progress-fill` `fromTo`) to the new `total_duration`
13. **Ambient breath**: change `duration: 12` (yoyo half-period) to `total_duration / 2`
14. **Slam shake**: replace the four `tl.to("#p1-hero", { x: ...}, <time>)` offsets with `shake_offsets`
15. **Audio element**: insert just before `</div>` (the closing tag of `#root`), at the same indent level as `<div id="phase4">`:

```html
  <audio id="narration"
         class="clip"
         src="audio/narration.wav"
         data-start="0"
         data-duration="<phase4_end>"
         data-track-index="2"
         data-volume="1"></audio>
```

16. **Wire SFX from `retention-strategy.md`** if Phase 3.5 ran (skip if not). Same workflow as [new-anthropic-short.md](./new-anthropic-short.md) Step 8 item 14: read `sfx_cues:` blocks → run `bash scripts/sync-video-sfx.sh videos/<slug> ${cues[@]}` → insert `<audio>` elements with `data-volume ≤ 0.25`. Density cap: ~2 placements per 10s narration, hard cap 2.5/10s. Volume table is in [`.claude/rules/audio-design.md`](../../rules/audio-design.md). The reference cue map for this variant:
    - Phase 1 version slam reveal: `impact-slam` at `slam_t` (volume 0.15)
    - Phase 1 inline shake: `screen-shake` at `slam_t` (volume 0.11, layered on track 4)
    - Phase 2 stat-pill 1 entrance only (skip pills 2 + 3 to stay under density cap): `scale-slam` (volume 0.15)
    - Each phase transition (T1, T2, T3): `cinematic-whoosh` (volume 0.11)
    - Phase 4 terminal entrance: `spring-pop` at `terminal_at` (volume 0.11)
    - Subscribe pill entrance: `pop` at `subscribe_at` (volume 0.10)

### 12. Lint

```bash
npx hyperframes lint videos/<slug>
```

Must report `0 errors`. Fix any errors before continuing. Common variant-specific issues:

| Error | Likely cause | Fix |
|---|---|---|
| `audio_src_not_found` (narration) | `narration.wav` missing | Re-run step 8 |
| `audio_src_not_found` (sfx) | Cue `.mp3` missing | `bash scripts/sync-video-sfx.sh videos/<slug> <cue>` |
| `duplicate_media_discovery_risk` | Re-enabled `#top-banner` with same source as VersionBranding | Use a different wordmark (e.g. `claude-logo-light.svg`) |
| `gsap_infinite_repeat` | Some accidental `repeat: -1` in a tween (or a lint-trip on a bare comment that contains the literal text `repeat:-1`) | Use a finite count; rephrase any comment that reads `repeat:-1` |
| `overlapping_gsap_tweens` (sfx) | Two SFX on same `data-track-index` overlap | Bump second SFX to next track index |

Warnings about `composition_file_too_large` are advisory — the shorts variant is intentionally inline-phase-mutex (mirrors anthropic shorts which also trips this warning).

### 13. Inspect for layout overflow

```bash
npx hyperframes inspect videos/<slug>
```

Common variant-specific overflows:

- **Version slam too wide** — long version strings (e.g. `v2.1.123-rc1` at 200px) can blow past 960px. Either drop `#p1-hero` font-size to 180px or shorten the displayed version (use `v2.1.123` and put the suffix in the caption pill).
- **3-pill stats clip on three-digit counts** — if any of the 3 stat numbers is ≥ 4 digits (rare for Claude Code but possible for cumulative-range releases), tighten `min-width: 220px` to fit, or wrap by stacking each pill's num + label vertically (then revert to anthropic-style 2-pill layout if needed).
- **Highlight card title overflows** — 38px font + long title overflows the card's 940px width minus the 96px badge + 26px gap. Shorten the title or drop it to 34px.
- **Terminal block too wide** — only an issue if the user customizes the command past `claude update`. Don't put a multi-line command in the terminal — split into multiple phase-4 sub-elements if needed.

Fix overflow at the CSS or content level, then re-run `inspect` until clean.

### 14. Open preview (final step — never render)

Run in background so the studio stays open:

```bash
npx hyperframes preview videos/<slug>
```

Capture the URL it prints (typically `http://localhost:5173`).

### 15. Generate YouTube description

**MUST follow [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md) end-to-end.** Same single source of truth that the long-form variant uses.

Quick checklist (the rule has full detail):

1. **vidIQ keyword research** — run `vidiq_keyword_research`, `vidiq_outliers`, `vidiq_trending_videos` against seeds like "Claude Code", "Claude Code update", "AI coding agent shorts". Save snapshot to `videos/<slug>/research/vidiq-keywords.md`.
2. **Chapter timestamps**: Shorts under 90s typically don't need chapters (YouTube hides them); for 90-180s Shorts where chapters help retention, compute `data-start ÷ speed_factor` (default 1.0; if ffmpeg-sped per [`.claude/rules/video-speedup.md`](../../rules/video-speedup.md), divide by that factor). 4 phase boundaries → 4 chapters max.
3. **Draft `videos/<slug>/youtube-description.md`** in the rule's prescribed order: hook (keyword-front-loaded) → Dynamous block in `----` separators (only if `dynamousPromotion: true` in meta.json — otherwise skip the block entirely) → Key Changes bullets → Resources with validated URLs → primary CTA (`$ claude update`) → debate question (must match script's final line) → 15-25 hashtags.
4. **Validate every URL** with `WebFetch`.

### 16. Report to the user

```
✅ Claude Code <vX.Y.Z> — Short
   Slug:        <slug>
   Reused:      videos/claude-code-v<NN>/  (or "fresh fetch")
   Render:      npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4
   Length:      <N>s
   Voice:       <voice-id> @ <speed>×
   Stats:       <features> features / <fixes> fixes / <improved> improved
   Highlights:  <count> cards
   YouTube:     videos/<slug>/youtube-description.md (paste-ready)
   Preview:     http://localhost:5173
```

That's it. Stop. Wait for user to iterate or trigger render manually.

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow on version slam, stat pills, highlight cards, or terminal block
- [ ] `#vb-version-string` shows the real version (not `vX.Y.Z`)
- [ ] All 3 stat-pill `.stat-num` values are real (not `0`)
- [ ] All 3 highlight cards have real titles + subs (no leftover "Highlight title one")
- [ ] Phase transition timestamps computed from transcript, NOT left at template defaults (5.6 / 11.6 / 17.6)
- [ ] Audio element wired with correct `data-duration`
- [ ] Total duration ≤ 180s (YouTube Shorts hard max); preferably 70-130s
- [ ] If a long-form `videos/claude-code-v<NN>/` exists, brief explicitly says it was reused (no duplicate WebFetch)
- [ ] Preview URL is reachable (the `hyperframes preview` background command is still running)

If any item fails, fix it before reporting. Don't claim success on a half-built composition.

---

## Don'ts

- Never auto-render — user explicitly always triggers render manually.
- Never fabricate stats, highlight titles, command names, or version strings. Pull from the changelog or the long-form's content brief; ask the user if missing.
- Never reuse `anthropic-logo-light.svg` for a re-enabled top-banner — it's already in VersionBranding (lint will flag duplicate-media-discovery-risk).
- Never leave the `vX.Y.Z` placeholder anywhere — set the real version once per release.
- Never modify `templates/shorts/claude-code-version/` — only the copy under `videos/<slug>/`.
- Never run `python scripts/elevenlabs-tts.py` without the `--shorts` flag for this template (selects the shorts-specific speed env var).
- Never add background music to a Short — narration + SFX only ([`.claude/rules/audio-design.md`](../../rules/audio-design.md) hard rule).
- Never run multiple `new-claude-code-version-short` invocations in parallel against the same slug.
- Never blindly re-run Step 3 (changelog WebFetch) when Step 2 found a long-form to reuse — the user-confirmed highlights are already in the long-form's brief, and re-fetching can produce a different category split if marckrenn updates the post mid-release.
- Never put a long version suffix (e.g. `-rc1`, `-beta.3`) inside `#p1-hero`'s 200px slam — the canvas-width budget is tight. Move the suffix to `#p1-caption` instead.
