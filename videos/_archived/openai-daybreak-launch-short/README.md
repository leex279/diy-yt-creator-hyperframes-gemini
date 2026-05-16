# OpenAI — Shorts Template

Vertical YouTube Short (1080x1920, 30fps, 24-180s) tuned for **OpenAI-branded content** (ChatGPT, GPT-5, Sora, DALL·E, Codex — anything that wants the OpenAI monochrome-editorial feel with a single ChatGPT-mint accent). Forked from [`templates/shorts/google/`](../google/); palette, chrome surfaces, and accent rotation re-worked from cinematic four-color to quiet monochrome+mint.

The full design system (palette, typography, motion, phase archetypes, Dynamous integration, tweak knobs) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained 24-second demo composition (`index.html`) showcasing **four reusable phase archetypes** wired for OpenAI-branded content:

| Phase | Pattern | Use for |
|---|---|---|
| 1 — Hero | Eyebrow + xl headline + subhead | scroll-stop hook |
| 2 — Terminal | Eyebrow + m headline + 2 colored-syntax terminal blocks | CLI command, code reveal, "one line" moments |
| 3 — Info grid | Eyebrow + m headline + 2x2 chip grid (single-accent) | feature signals, what-you-get list |
| 4 — Shift / CTA | Eyebrow + m headline + accent-bordered quote + CTA pill | the closing thought + drop / try / subscribe prompt |

Each phase is mutex-visible (only one at a time) with a blur+crossfade transition. Entrance animations only — the transition handles the exit (per HyperFrames rule).

Persistent surfaces across all phases:

- **ChatGPT spirograph mark** centered at top (`assets/chatgpt-mark.svg`)
- **`@handle`** in top-right corner (mono caps, mint-tinted `@`)
- **5-dot progress rail** at the bottom (INTRO → BUILD → SIGNAL → SHIFT → CTA; one dot active per phase, mint glow)
- **Slim progress bar** at the very bottom edge (mint fill)
- **Sparse monochrome particle field** (40 deterministic dots in 3 off-white tints — far calmer than the Google template's 60-dot 4-color scatter)
- **Inner safe-area frame** (rounded hairline border)

The aesthetic anchor: a quiet editorial surface that reads as "premium product page" rather than "launch fireworks". Mint is the only chromatic accent; lavender (Sora-flavored) and amber (DALL·E-flavored) sit in the token file as auxiliary tints reserved for explicit override.

## Tweaks panel — knobs applied via simple file edits

| Tweak | How to apply in this template |
|---|---|
| **Theme** (quiet / cinematic / editorial) | Change `class="theme-quiet"` on `#root` to `theme-cinematic` (adds a single mint top glow) or `theme-editorial` (faint 60px grid overlay). Default is `theme-quiet` — pure flat off-black. |
| **Accent** (mint / lavender / amber / coral) | Add inline style on `#root` — `style="--accent: var(--oai-lavender); --accent-glow: rgba(167,139,250,0.30);"`. Use lavender for Sora-flavored videos, amber for DALL·E, coral for warning/regression callouts. |
| **Brand mark** (ChatGPT spirograph / OpenAI wordmark) | Default is `assets/chatgpt-mark.svg`. Swap to `assets/openai-wordmark.png` for cross-sub-brand videos (GPT-5 / Sora / DALL·E / Codex) where the spirograph would feel too ChatGPT-specific. The wordmark is shipped alongside the spirograph for one-edit switching. |
| **Show progress rail** | Default ON. To hide: delete the `#progress-rail` block, or set `display: none` |
| **Light "shift" slide** | Add class `theme-light` on `#phase4` for the bright SHIFT variant — flips the Phase 4 surface to a warm off-white (`#F4F4F2`). Headline + quote text auto-switch to `--ink-on-light`. |
| **Hero copy** (eyebrow / headline / subhead) | Edit text inside `#p1-eyebrow`, `#p1-headline`, `#p1-subhead` |
| **Handle** (no @) | Edit text inside `#footer-handle` (after the `<span class="at">@</span>` span) |
| **Big-stat alternate** (Phase 3) | Replace the `.chip-grid` block with `<div class="bigstat"><div class="num">3<span class="num-suffix">x</span></div><div class="label">…</div></div>` to use the 360px gradient-stat pattern |
| **Compare row alternate** | Same swap pattern — see `DESIGN.md` for the `.compare` markup template |

### Dynamous overlays — controlled via `video.config.js`

This template ships with the same Dynamous AI promotion overlays as the Google variant, enabled by default:

| Overlay | Default | Where it sits |
|---|---|---|
| `badge` | ON | Top-left brand pill (avoids the bottom progress rail) |
| `moduleInterstitial` | **OFF** | 3s slide-in card at the first scene transition (~5.6s). Opt-in per video — set `true` and update `moduleId/Name/AccentColor` only when promoting a specific Dynamous module |
| `discountBubble` | ON | 10% OFF pill in the bottom-left during the Phase 4 (CTA) window |
| `endcard` | ON | 5s contextual community CTA card overlay during the final 5s |

Disable any of them per video by editing `video.config.js`:

```js
window.VIDEO_CONFIG = {
  dynamous: {
    badge: false,
    moduleInterstitial: false,
    discountBubble: false,
    moduleId: 12,
    moduleName: 'Voice + ASR',
    moduleAccentColor: '#10A37F',  // pin to OpenAI mint instead of pink
    discountBubbleStart: 17.0,
    discountBubbleDuration: 6,
  },
};
```

The guard script at the bottom of `index.html` removes any disabled element synchronously before HyperFrames scans the DOM, so disabled overlays never appear in the clip list.

## Spawn a new video from this template

The fastest path is the slash-command playbook at [`.claude/skills/diy-yt-creator/new-openai-short.md`](../../../.claude/skills/diy-yt-creator/new-openai-short.md). It takes a topic prompt, drafts a tight 70-90s shorts script, runs ElevenLabs TTS, computes phase boundaries from the transcript, fills the composition, lints, and opens preview — never auto-renders.

Manual spawn from the repo root:

```bash
# 1. Pick a slug (kebab-case, suffix -short to disambiguate)
SLUG="gpt5-launch-short"

# 2. Copy the template
cp -r templates/shorts/openai videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "gpt5-launch-short",
#      "name": "GPT-5 Launch — Short"
#    }

# 4. Edit videos/$SLUG/index.html
#    - Phase 1: replace #p1-eyebrow / #p1-headline / #p1-subhead text
#    - Phase 2: replace terminal commands inside #p2-term-1 / #p2-term-2
#    - Phase 3: replace .chip-label / .chip-value text in each #p3-chip-N
#                 (or swap the grid for .bigstat — see DESIGN.md)
#    - Phase 4: replace #p4-headline / .q-text / .cta-value text
#    - Adjust data-duration on #root and the phase transition timestamps
#      (T1 / P2 / T2 / P3 / T3 / P4) to match the narration length
#    - Update #footer-handle text to your channel handle

# 5. Optional: swap the spirograph for the OpenAI wordmark if the
#    video covers GPT/Sora/DALL·E rather than ChatGPT specifically:
#      <img src="assets/openai-wordmark.png" alt="OpenAI" />

# 6. Optional: edit videos/$SLUG/video.config.js to disable Dynamous
#    overlays or change the module info per release.

# 7. Drop narration at videos/$SLUG/audio/narration.wav and uncomment
#    the <audio id="narration"> block at the bottom of index.html.

# 8. Validate
npx hyperframes lint     videos/$SLUG
npx hyperframes validate videos/$SLUG
npx hyperframes inspect  videos/$SLUG

# 9. Preview
npx hyperframes preview  videos/$SLUG

# 10. Render
npx hyperframes render   videos/$SLUG -o videos/$SLUG/out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/openai videos/$SLUG`.

## Extending a phase to multi-sub-slide (opt-in patterns)

For longer / content-rich shorts (90s+) any phase can be **extended into multiple sub-slides** that crossfade in sequence. The template's `<style>` block already ships the same reusable CSS as the Google variant — operators just add markup + GSAP wiring.

**Available CSS classes** (already loaded; no changes needed):

| Class | Purpose |
|---|---|
| `.pX-stage` (`p2-stage`/`p3-stage`/`p4-stage`) | Wrap `.phase-content` to enable absolute-positioned sub-slides |
| `.pX-slide` | Sub-slide container; hidden by default. Add `.is-default-visible` to the first one |
| `.pX-slide[data-color="mint\|lavender\|amber\|coral"]` | Sub-brand-color theming for slot accents + bullet borders |
| `.hero-figure` + `.src-handle` | Phase 1 image card (tweet/screenshot/UI) — replaces `.subhead` |
| `.settings-figure` + `.inline-mono` | Phase 2B UI screenshot card with mono-tagged caption |
| `.p3-slot-num` + `.p3-eyebrow` + `.p3-headline` | Numbered feature slide ("01 / FEATURE") |
| `.p3-bullets` / `.p2-c-bullets` | Bullet list with mono `.bullet-tag` + sans `.bullet-detail` |
| `.p4-pills` | Phase 4 feature-pill list (perf/security wins) |
| `.p4-perf-eyebrow` + `.p4-perf-headline` | Phase 4 perf-pill stage typography |

The Markup + GSAP pattern is identical to the Google variant (FLICKER-FREE `tl.set` + `tl.to`, never `tl.from(... immediateRender:false)`). See [`../google/README.md`](../google/README.md) "Extending a phase to multi-sub-slide" for the worked example.

## Brand surfaces

The ChatGPT spirograph (`assets/chatgpt-mark.svg`) sits at the top-center for the full duration. The `@handle` is in the top-right. Both are persistent (no `class="clip"`). The OpenAI wordmark (`assets/openai-wordmark.png`) and Dynamous logo (`assets/dynamous-logo.png`) are local — never reference `../../shared/logos/...` paths because HyperFrames' bundler rejects them.

For cross-sub-brand videos (GPT-5 / Sora / DALL·E / Codex — anything that isn't specifically ChatGPT), swap the spirograph for the OpenAI wordmark by editing the single `<img>` inside `#brand-mark`:

```html
<!-- ChatGPT-specific (default) -->
<img src="assets/chatgpt-mark.svg" alt="ChatGPT" />

<!-- Generic OpenAI -->
<img src="assets/openai-wordmark.png" alt="OpenAI" />
```

You may also need to bump `#brand-mark img { height: 110px; }` down to `80-90px` when using the wordmark — it's a wider asset and 110px makes it dominate the top safe zone.

## When NOT to use this variant

Use this variant for any OpenAI-branded content. Cues that signal the wrong fit:

- The brand is Anthropic / Claude → use [`templates/shorts/anthropic/`](../anthropic/) or [`templates/shorts/claude-code-version/`](../claude-code-version/)
- The brand is Google / Gemini / Workspace / Android → use [`templates/shorts/google/`](../google/)
- The content has no brand at all → use [`templates/shorts/standard/`](../standard/)
- The aesthetic should be cinematic with multi-color glows → use the Google template (different brand identity by design)

## Customizing per video

Most styling is driven by CSS variables on `:root` in `tokens/openai-mono.css`. Override per video by re-declaring any var in a tighter scope:

```css
/* In videos/<slug>/tokens/openai-mono.css OR inline in index.html */
:root {
  --accent:        var(--oai-lavender);              /* Sora-flavored swap */
  --accent-glow:   rgba(167, 139, 250, 0.32);
  --pad-top:       260px;                            /* nudge top safe-zone */
}
```

**Per-phase accent rotation:** by default every phase uses the same mint `--accent`. If you want each phase to lead with a different auxiliary hue (e.g. mint hero → lavender terminal → amber stats → coral CTA), set inline `style="--accent: var(--oai-lavender);"` on the phase wrapper (`#phase2`, `#phase3`, etc.) — the eyebrow, CTA pill border, and progress-bar fill will all pick it up.

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

Cues live in [`shared/audio/sfx/`](../../../shared/audio/). Sync into your video's `assets/sfx/`:

```bash
bash scripts/sync-video-sfx.sh videos/<slug> impact-slam scale-slam spring-pop
```

The default `sfx-cues.txt` ships with `impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop`.

## Don'ts

See [DESIGN.md](./DESIGN.md) "What NOT to Do" for the full list. The big variant-specific ones:

- No background music on Shorts — narration + SFX only.
- No `repeat: -1` on the CTA pulse — the existing `yoyo: true, repeat: 4` is the deterministic finite pattern.
- No `class="clip"` on `#brand-mark`, `#footer-handle`, `#progress-rail`, `#dynamous-badge`, or `#dynamous-module-interstitial-wrap` — those are persistent visual chrome.
- No `<br>` in content text — use `text-wrap: balance` on the headline / subhead for natural wrapping.
- No four-color rotation on the chip grid or rail dots. The OpenAI brand is monochrome+mint — adding multi-color decoration breaks the editorial feel. If a phase genuinely needs a contrast moment, use **one** auxiliary hue (lavender for Sora, amber for DALL·E, coral for warning) per phase, never four.
- The Dynamous module-interstitial sub-comp uses class-only CSS selectors (no `#dynamous-module-interstitial .dmi-card` chains). Keep it that way — ID-prefixed selectors don't survive HyperFrames' sub-comp scoping reliably.
