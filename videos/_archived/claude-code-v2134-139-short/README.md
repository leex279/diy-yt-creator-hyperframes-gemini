# Claude Code Version Update — Shorts Template

Vertical YouTube Short (1080x1920, 30fps, 60-180s) tuned for **Claude Code release-update videos**. Forked from [`templates/shorts/anthropic/`](../anthropic/) with the GitHub-dark + Claude Code accent palette from the long-form variant ([`templates/long-form/claude-code-version/`](../../long-form/claude-code-version/)) and a `$ claude update` terminal CTA in place of the URL pill.

The full design system (palette, variant-specific surfaces, type/motion deltas vs anthropic-dark) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained 24-second demo composition (`index.html`) showcasing **three reusable phase archetypes** wired for Claude Code release content. The composition opens cold on Phase 1 — there is no spoken version slam intro. The version is shown as a static visual reference (130px, frame-0 visible) so viewers can read it; narration starts on the first stat number.

| Phase | Pattern | Use for |
|---|---|---|
| 1 — Stats opener (with version header) | overline ("Claude Code Update") + 130px static version (e.g. `v2.1.133`, cyan-blue, no animation slam) + headline + 3 huge stat pills (cyan / purple / green) | cold-open: features / fixes / improved counts; the version sits above as a visual anchor, never narrated |
| 2 — Highlight cards | overline + 3 numbered cards (`01/02/03`, cyan → purple → green) | top 3 highlights of the release (no dates — number badges instead) |
| 3 — CTA | overline + `$ claude update` terminal block (macOS chrome) + Subscribe pill (Claude Code orange glow pulse) | the canonical Claude Code release-video close |

Each phase is mutex-visible (only one at a time), separated by a blur + crossfade transition. Entrance animations only — the transition handles the exit (per HyperFrames rule).

A persistent **VersionBranding** overlay (Anthropic + Claude Code logos top-right + version string + repo URL bottom-center) sits above the phases at `opacity: 0.7` for the full duration. Mirrors the long-form variant's brand-zone pattern.

## Variant deltas vs `templates/shorts/anthropic/`

| Dimension | Anthropic Shorts | Claude Code Version Shorts |
|---|---|---|
| Canvas surface | `#0B0F18` near-black with a touch of blue | `#0D1117` GitHub-dark |
| Accent triad | Claude orange + soft purple / blue / green | Claude Code cyan-blue + purple + green + orange (warn / hero stat) |
| Top brand zone | Centered `#top-banner` Anthropic wordmark | `#top-banner { display: none }` — VersionBranding owns the zone |
| VersionBranding overlay | None | Anthropic + Claude Code logos top-right + version string bottom-center, 0.7 opacity |
| Phase mix | 4 phases: hook → stats → cards → CTA | **3** phases: stats (with version header) → cards → CTA. The spoken version slam from anthropic shorts is dropped — the version sits as a static 130px visual above the stat pills, never narrated |
| Phase 1 hero target | Slam word ("DUMBER?") | 3 stat pills (features / fixes / improved) with a static `vX.Y.Z` reference above |
| Phase 2 cards | Dated timeline cards (Mar 4 / Mar 26 / Apr 16) | Numbered highlight cards (`01` / `02` / `03`) — no dates, top-N highlights |
| Phase 3 CTA | URL pill + Subscribe pill | macOS terminal block showing `$ claude update` + Subscribe pill (Claude Code orange pulse) |

Everything else — the xmur3 shape backdrop, the ambient breath, the noise overlay, the phase-mutex crossfade, the SFX cue catalog, the linter rules — inherits from anthropic shorts verbatim.

## Spawn a new video from this template

The fastest path is the slash-command playbook at [`.claude/skills/diy-yt-creator/new-claude-code-version-short.md`](../../../.claude/skills/diy-yt-creator/new-claude-code-version-short.md). It takes a Claude Code release tag (e.g. `v2.1.118`), reuses the long-form video's content brief if one already exists for the same version, fetches the changelog otherwise, drafts a tight 70-90s shorts script, runs ElevenLabs TTS, computes phase boundaries from the transcript, fills the composition, lints, and opens preview — never auto-renders.

Manual spawn from the repo root:

```bash
# 1. Pick a slug (kebab-case, suffix -short to disambiguate from long-form)
SLUG="claude-code-v2118-short"

# 2. Copy the template
cp -r templates/shorts/claude-code-version videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "claude-code-v2118-short",
#      "name": "Claude Code v2.1.118 — Short"
#    }

# 4. Edit videos/$SLUG/index.html
#    - Replace #vb-version-string text with real "github.com/anthropics/claude-code/releases  |  vX.Y.Z"
#    - Phase 1: replace #p1-version "vX.Y.Z" with the real version (static, no narration)
#             + replace each .stat-num with real counts (features / fixes / improved)
#             + replace #p1-headline with a one-line release-character headline
#    - Phase 2: replace each .hl-title and .hl-sub with the top 3 highlights
#    - Phase 3: terminal already shows "$ claude update" — leave it
#    - Adjust data-duration on #root and the phase transition timestamps
#      (T1/P2/T2/P3) to match the narration length

# 5. Drop narration at videos/$SLUG/audio/narration.wav and uncomment the <audio> block

# 6. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG
npx hyperframes inspect videos/$SLUG

# 7. Preview
npx hyperframes preview videos/$SLUG

# 8. Render
npx hyperframes render videos/$SLUG -o out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/claude-code-version videos/$SLUG`.

## Reusing a long-form claude-code-version video

If a long-form video already exists for the same version at `videos/claude-code-v<NN>/`, the shorts playbook reuses its content artifacts instead of re-fetching the changelog. The playbook reads:

- `videos/claude-code-v<NN>/research/content-brief.md` — version, stats (features / fixes / improved counts), hook angle, highlights list
- `videos/claude-code-v<NN>/research/changelog-marckrenn.md` — for any highlight that needs sharper phrasing
- `videos/claude-code-v<NN>/script.txt` — for narration tone / pacing reference (NOT to copy verbatim — the shorts version is much tighter)

This avoids burning two WebFetches and keeps the stats / highlights consistent across the long-form and short cuts of the same release.

## Brand surfaces

The variant ships with `#top-banner { display: none }` so VersionBranding is the single brand surface. Lint cleanly rejects two `<img>` elements with the same source/start/duration, so when you re-enable the centered top-banner per video, source it from a different file (e.g. `assets/claude-logo-light.svg`) — never from `anthropic-logo-light.svg` (already in VersionBranding).

The two required logos already live at `assets/anthropic-logo-light.svg` and `assets/claude-code-logo-light.svg` (copied from `shared/logos/` when the template was forked).

## When NOT to use this variant

Use [`templates/shorts/anthropic/`](../anthropic/) for any Anthropic / Claude content that ISN'T a Claude Code release (postmortems, model launches, news commentary). Use [`templates/shorts/standard/`](../standard/) for any non-Anthropic topic. Cues that signal the wrong fit:

- The video isn't about a Claude Code release.
- The brand surfaces should be the channel's own wordmark, not Anthropic + Claude Code.
- The content shape isn't release-update (no version, no feature/fix counts, no terminal command).

VersionBranding can be hidden per video, but the rest of the variant (3-pill stats, numbered highlight cards, terminal CTA) is over-fit for non-release videos.

## Customizing per video

Most styling is driven by CSS variables on `:root` (in `tokens/claude-code-dark.css`). Override per video by re-declaring any var in a tighter scope:

```css
/* In videos/<slug>/tokens/claude-code-dark.css OR inline in index.html */
:root {
  --accent-1:    #58A6FF;   /* Claude Code cyan-blue (default) */
  --accent-3:    #A371F7;   /* Claude Code purple (default) */
  --accent-4:    #3FB950;   /* Claude Code green (default) */
  --accent-warn: #F78166;   /* Claude Code orange (default) */
}
```

Per-phase accent rotation: keep cyan as the primary lead for the version slam (Phase 1), and rotate cyan → purple → green through the 3 stat pills (Phase 2) and the 3 highlight cards (Phase 3). Orange is reserved for `--accent-warn` callouts and the Subscribe pill — don't use it on highlight cards or stat pills.

## Adding narration

1. Generate or drop your TTS audio at `audio/narration.wav` (or `.mp3`).
2. Uncomment the `<audio id="narration">` block at the bottom of `index.html`.
3. Tune `data-start` (when narration begins relative to composition 0) and `data-duration` (clip length).
4. Sync phase timestamps (`T1`, `P2`, `T2`, `P3`, `T3`, `P4`) to spoken-word landmarks. Use `npx hyperframes transcribe` (or the ElevenLabs alignment API) to get word-level timestamps.

## Adding SFX

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Volume is capped per [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md) — never exceed `0.25` on a single per-cue SFX.

```html
<audio id="sfx-slam"
       class="clip"
       src="assets/sfx/scale-slam.mp3"
       data-start="1.55"
       data-duration="0.9"
       data-track-index="3"
       data-volume="0.15"></audio>
```

Place under the `<audio id="narration">` block. Use distinct `data-track-index` values so simultaneous cues don't clash.

### Sourcing the actual SFX files

Cues live in [`shared/audio/sfx/`](../../../shared/audio/). Sync into your video's `assets/sfx/` (required because HyperFrames rejects paths outside the project dir at runtime):

```bash
bash scripts/sync-video-sfx.sh videos/<slug> impact-slam scale-slam spring-pop
```

Or list cues in `videos/<slug>/sfx-cues.txt` (one per line) and run without args. The default `sfx-cues.txt` ships with `impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop` — same as the long-form variant.

## Don'ts

See [DESIGN.md](./DESIGN.md) "What NOT to Do" for the full list. The big variant-specific ones:

- No same-source img twice in `index.html` with same start/duration (lint warning) — `anthropic-logo-light.svg` is already in VersionBranding.
- No auto-generated `#vb-version-string` at render time — set once per release.
- No `class="clip"` on `#version-branding` or its children.
- No background music on Shorts — narration + SFX only.
- No `repeat: -1` on the Subscribe pulse — the existing `yoyo: true, repeat: 4` is the deterministic finite pattern.
- No `<br>` in content text — use `max-width` for natural wrapping.
