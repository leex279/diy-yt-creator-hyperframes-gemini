# Long-Form Claude Code Version Update Template

Horizontal Claude Code release-update video (1920x1080, 30fps, ~3-5 minutes) in the **GitHub-dark + Claude Code accent triad** aesthetic. Forked from [`templates/long-form/standard/`](../standard/), with palette overrides, three replaced scene archetypes, and a persistent VersionBranding overlay.

The full design system (palette, variant-specific surfaces, type/motion inherited from standard) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained ~120-second demo composition (`index.html`) with **8 reusable scene archetypes** + a captions sub-composition + persistent VersionBranding overlay. Scene mix tuned for release-update content shape.

| File | Pattern | Use for |
|---|---|---|
| `compositions/scene-hook.html` | overline + 100px headline + 130px stat slam + sub-line | Scroll-stop opener |
| `compositions/scene-stats-opener.html` | version badge + 3 huge stat pills (cyan/purple/green) | "5 features / 30 fixes / 7 improved" receipts moment |
| `compositions/scene-side-by-side.html` | two LiquidGlassCard panels (blue vs purple), entering from opposite sides | Before vs after; A vs B compare |
| `compositions/scene-stat-pill-row.html` | 2 huge color-rotated stats with mono labels | Per-release hero stats |
| `compositions/scene-feature-cards.html` | configurable 4-6 card grid (2x2 / 3x2 / stack) with number badges | Highlights scene; per-category listings |
| `compositions/scene-video-embed.html` | animated wrapper around `<video>` with mono overline + caption | Embedded clips, demo footage |
| `compositions/scene-terminal.html` | macOS chrome + JetBrains Mono code block | Command demos (e.g. `/plan`, `/vim`); release CTA |
| `compositions/scene-cta.html` | debate question + comment pill + subscribe pulse + inline `$ claude update` terminal | Closing CTA with finite-pulse glow |
| `compositions/captions.html` | empty captions sub-composition with `data-caption-root="true"` | Word-level captions populated by `npx hyperframes transcribe` |

The root composition (`index.html`) only orchestrates: ambient background (radial wash + 14 drifting shapes + noise overlay), narration `<audio>`, optional 3-segment bg-music, the persistent VersionBranding overlay, and 8 `data-composition-src` wrappers that pull in each scene file. Variant-specific surfaces are documented in [DESIGN.md](./DESIGN.md) under "Variant-specific Surfaces".

## Per-release content extraction

The variant is driven end-to-end by the `/claude-code-version` slash command. It takes a Claude Code release URL or version tag and produces a wired `videos/claude-code-v<NN>/` directory ready for preview + render.

```text
/claude-code-version v2.1.118
```

Steps the command performs:

1. WebFetch the release notes from `marckrenn/claude-code-changelog` (Highlights section) and `anthropics/claude-code/blob/main/CHANGELOG.md` (full inventory).
2. Derive scene categories (features / fixes / improvements / breaking changes) from the changelog.
3. AskUserQuestion to confirm WatchNext + highlights selection.
4. Write narration script to `videos/<slug>/script.txt` (TTS-optimized).
5. `npx hyperframes tts videos/<slug>/script.txt -o videos/<slug>/audio/narration.wav -v am_michael -s 1.0`
6. `npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>` → `transcript.json`
7. `cp -r templates/long-form/claude-code-version videos/<slug>` and apply per-release edits (placeholder text → real text in `compositions/scene-*.html`; `#vb-version-string` to the actual `vX.Y.Z`; scene wrapper `data-start` values to transcript word offsets).
8. `npx hyperframes lint`, `inspect`, `validate` — must pass before render.
9. Output a YouTube description at `videos/<slug>/youtube-description.md` (chapters + SEO).
10. Render: `npx hyperframes render videos/<slug> --quality high --workers 4 -o videos/<slug>/out/long-form.mp4`.

The full step-by-step lives in `.claude/commands/diy-yt-creator/claude-code-version.md`. Per-video manual edits are limited to text replacements + scene timing — no compositional rewrites.

## Spawn a new video manually (without the slash command)

From the repo root:

```bash
# 1. Pick a slug (kebab-case, e.g. claude-code-v2118)
SLUG="claude-code-v2118"

# 2. Copy the template
cp -r templates/long-form/claude-code-version videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "claude-code-v2118",
#      "name": "Claude Code v2.1.118 — What's New"
#    }

# 4. Drop narration audio at:
#      videos/$SLUG/audio/narration.wav
#    Then UNCOMMENT the <audio id="narration"> block in index.html
#    (and tune data-duration to your narration's actual length).

# 5. Edit index.html:
#    - Set #vb-version-string text to the real "github.com/anthropics/claude-code/releases  |  vX.Y.Z"
#    - Tune data-start values on each scene wrapper to match your script's
#      scene boundaries (the 0/12/32/55/70/90/105/115 defaults are demo timing)
#    - Bump #root data-duration to your real total length
#    - Update tl.set({}, {}, TOTAL_DURATION) at the bottom of <script>

# 6. Edit each compositions/scene-*.html with your real copy
#    (the templates ship placeholder text — "vX.Y.Z", "5 features / 30 fixes / 7 improved", etc.)

# 7. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG     # WCAG contrast audit
npx hyperframes inspect videos/$SLUG      # layout overflow check

# 8. Preview
npx hyperframes preview videos/$SLUG

# 9. Render
npx hyperframes render videos/$SLUG --quality high --workers 4 -o videos/$SLUG/out/long-form.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/long-form/claude-code-version videos/$SLUG`.

## Brand surfaces

The variant ships with **VersionBranding** (`#version-branding`) as the single brand surface — Anthropic + Claude Code logos top-right at 0.7 opacity, with the version string + repo URL bottom-right. The standard's centered top-banner is disabled by default (`#top-banner { display: none }`) to avoid the duplicate-media-discovery-risk lint warning.

The two required logos already live at `assets/anthropic-logo-light.svg` and `assets/claude-code-logo-light.svg` (copied from `shared/logos/` when the template was forked).

To re-enable the centered top-banner per video, drop a different wordmark (e.g. `claude-logo-light.svg`) into `assets/` and uncomment the `#top-banner` block in `index.html`. **Do NOT reuse `anthropic-logo-light.svg` for the top-banner** — it's already in VersionBranding, and lint rejects two `<img>` elements with identical source/start/duration.

## When NOT to use this variant

Use [`templates/long-form/standard/`](../standard/) (or another variant) for any non-Claude-Code video. Cues that signal the wrong fit:

- The video isn't about a Claude Code release.
- The brand surface should be the channel's own wordmark, not Anthropic + Claude Code.
- The content shape isn't release-update (no version, no feature/fix counts, no terminal command).

VersionBranding can be hidden per video, but the rest of the variant (scene mix tuned for release-update content + Claude Code palette) is over-fit for non-release videos.

## Customizing per video

Most styling is driven by CSS variables on `:root` (in `tokens/long-form.css`). Override per video by re-declaring any var in a tighter scope:

```css
/* In videos/<slug>/tokens/long-form.css OR inline in index.html */
:root {
  --accent-1:    #58A6FF;   /* Claude Code cyan-blue (default) */
  --accent-3:    #A371F7;   /* Claude Code purple (default) */
  --accent-4:    #3FB950;   /* Claude Code green (default) */
  --accent-warn: #F78166;   /* Claude Code orange (default) */
}
```

Per-scene accent rotation: change which `--accent-*` a scene uses by editing the scene's CSS — most scenes pin one lead color (`scene-stats-opener` rotates cyan/purple/green; `scene-terminal` uses cyan-blue + green; `scene-feature-cards` rotates through all four).

## Adding more scenes

The 8 archetypes are starting points — any video can add, remove, or reorder scenes. Mirror standard's "Adding more scenes" workflow (in [`../standard/README.md`](../standard/README.md)). The variant-specific addition: when adding a scene that uses release-version data, read `videos/<slug>/transcript.json` for word offsets and pass the version string from `meta.json` (or the `vb-version-string` element's content) so all surfaces stay in sync.

## Adding narration

Same as standard. See [`../standard/README.md`](../standard/README.md) "Adding narration".

## Adding background music

Same as standard. See [`../standard/README.md`](../standard/README.md) "Adding background music".

## Adding SFX

Same as standard. See [`../standard/README.md`](../standard/README.md) "Adding SFX". Variant ships `sfx-cues.txt` with `impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop` (inherited from standard — all five files exist in `shared/audio/sfx/`).

**Volume caps are post-2026-04-28** — see [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md) for the calibrated table. Never lyrical music under narration.

## Embedded video

Same as standard. See [`../standard/README.md`](../standard/README.md) "Embedded video — bringing the audio in".

## Expected lint warnings on the bare template

Before you wire your media, the bare template lints **0 errors, 0 warnings**. After you spawn a video and start dropping screenshots, you may see:

- `audio_src_not_found` — until you uncomment + drop narration/bg-music files.
- `404 loading assets/clips/demo.mp4` — until you drop a clip (or remove `compositions/scene-video-embed.html` from the wiring if you don't need it).
- `duplicate_media_discovery_risk` — if you re-enable the centered top-banner with the same source as VersionBranding (see "Brand surfaces" above).

## Don'ts

Inherit standard's full "What NOT to Do" list. Variant-specific additions are in [DESIGN.md](./DESIGN.md). The big variant-specific ones:

- No same-source img twice in `index.html` with same start/duration (lint warning).
- No auto-generated `#vb-version-string` at render time — set once per release.
- No `class="clip"` on `#version-branding` or its children.
