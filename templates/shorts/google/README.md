# Google — Shorts Template

Vertical YouTube Short (1080x1920, 30fps, 24-180s) tuned for **Google-branded content** (Google AI, Gemini, Workspace, Cloud, Android, Chrome — anything that wants the four-color brand on a cinematic dark stage). Translated from the supplied "Google Short Design" reference (React + tweaks panel) into a HyperFrames mutex-phase composition.

The full design system (palette, typography, motion, phase archetypes, Dynamous integration, tweak knobs) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained 24-second demo composition (`index.html`) showcasing **four reusable phase archetypes** wired for Google-branded content:

| Phase | Pattern | Use for |
|---|---|---|
| 1 — Hero | Google logo + accent eyebrow + xl headline + subhead | scroll-stop hook |
| 2 — Terminal | eyebrow + m headline + 2 colored-syntax terminal blocks | CLI command, code reveal, "one line" moments |
| 3 — Info grid | eyebrow + m headline + 2x2 chip grid (4 Google colors) | feature signals, what-you-get list |
| 4 — Shift / CTA | eyebrow + m headline + accent-bordered quote + CTA pill | the closing thought + drop / subscribe prompt |

Each phase is mutex-visible (only one at a time) with a blur+crossfade transition. Entrance animations only — the transition handles the exit (per HyperFrames rule).

Persistent surfaces across all phases:

- **Google logo** centered at top
- **`@handle`** in top-right corner (mono caps, accent-tinted `@`)
- **5-dot progress rail** at the bottom (SETUP → CREATE → EVAL → DEPLOY → PUBLISH; one dot active per phase, glow in the matching Google color)
- **Top-left accent ramp** (4px green→yellow line)
- **Particle field** (60 deterministic dots in 4 Google colors)
- **Slim progress bar** at the very bottom edge
- **Inner safe-area frame** (rounded hairline border)

## Tweaks panel — the original design's knobs, applied via simple file edits

The supplied React reference shipped a runtime "Tweaks" panel. HyperFrames is HTML-only, so the same knobs become file-level edits or `video.config.js` flags:

| Tweak from reference design | How to apply in this template |
|---|---|
| **Theme** (cinematic / spotlight / editorial) | Change `class="theme-cinematic"` on `#root` to `theme-spotlight` or `theme-editorial` |
| **Accent** (blue / red / yellow / green) | Add inline style on `#root` — `style="--accent: var(--g-red); --accent-glow: rgba(234,67,53,0.35);"` (or any other Google hue) |
| **Show progress rail** | Default ON. To hide: delete the `#progress-rail` block, or set `display: none` |
| **Light "shift" slide** | Add class `theme-light` on `#phase4` for the bright SHIFT variant (matches the reference's `lightShift` toggle) |
| **Hero copy** (eyebrow / headline / subhead) | Edit text inside `#p1-eyebrow`, `#p1-headline`, `#p1-subhead` |
| **Handle** (no @) | Edit text inside `#footer-handle` (after the `<span class="at">@</span>` span) |
| **Big-stat alternate** (Phase 3) | Replace the `.chip-grid` block with `<div class="bigstat"><div class="num">3<span class="num-suffix">x</span></div><div class="label">…</div></div>` to use the reference's "360px gradient stat" pattern instead |
| **Compare row alternate** | Same swap pattern — see `DESIGN.md` for the `.compare` markup template |

### Dynamous overlays — controlled via `video.config.js`

Per the parallel claude-code-version templates, this template ships with three Dynamous AI promotion overlays enabled by default:

| Overlay | Default | Where it sits |
|---|---|---|
| `badge` | ON | Top-left brand pill (avoids the bottom progress rail) |
| `moduleInterstitial` | **OFF** | 3s slide-in card at the first scene transition (~5.6s). Opt-in per video — set `true` and update `moduleId/Name/AccentColor` only when promoting a specific Dynamous module |
| `discountBubble` | ON | 10% OFF pill in the bottom-left during the Phase 4 (CTA) window |

Disable any of them per video by editing `video.config.js`:

```js
window.VIDEO_CONFIG = {
  dynamous: {
    badge: false,             // hide the persistent pill
    moduleInterstitial: false, // skip the 3s module card
    discountBubble: false,    // skip the bottom-left CTA pill
    moduleId: 12,             // override module number
    moduleName: 'Voice + ASR', // override module title
    moduleAccentColor: '#22d3ee', // override the dot color
    discountBubbleStart: 17.0,    // optional override; default = Phase 4 start (18.4s)
    discountBubbleDuration: 6,    // seconds the bubble shows
  },
};
```

The guard script at the bottom of `index.html` removes any disabled element synchronously before HyperFrames scans the DOM, so disabled overlays never appear in the clip list.

## Spawn a new video from this template

The fastest path is the slash-command playbook at [`.claude/skills/diy-yt-creator/new-google-short.md`](../../../.claude/skills/diy-yt-creator/new-google-short.md). It takes a topic prompt, drafts a tight 70-90s shorts script, runs ElevenLabs TTS, computes phase boundaries from the transcript, fills the composition, lints, and opens preview — never auto-renders.

Manual spawn from the repo root:

```bash
# 1. Pick a slug (kebab-case, suffix -short to disambiguate)
SLUG="gemini-cli-launch-short"

# 2. Copy the template
cp -r templates/shorts/google videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "gemini-cli-launch-short",
#      "name": "Gemini CLI Launch — Short"
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

# 5. Optional: edit videos/$SLUG/video.config.js to disable Dynamous overlays
#    or change the module info per release.

# 6. Drop narration at videos/$SLUG/audio/narration.wav and uncomment
#    the <audio id="narration"> block at the bottom of index.html.

# 7. Validate
npx hyperframes lint     videos/$SLUG
npx hyperframes validate videos/$SLUG
npx hyperframes inspect  videos/$SLUG

# 8. Preview
npx hyperframes preview  videos/$SLUG

# 9. Render
npx hyperframes render   videos/$SLUG -o out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/shorts/google videos/$SLUG`.

## Extending a phase to multi-sub-slide (opt-in patterns)

For longer / content-rich shorts (90s+) any phase can be **extended into multiple sub-slides** that crossfade in sequence. The template's `<style>` block already ships the reusable CSS — operators just add markup + GSAP wiring.

**Available CSS classes** (already loaded; no changes needed):

| Class | Purpose |
|---|---|
| `.pX-stage` (`p2-stage`/`p3-stage`/`p4-stage`) | Wrap `.phase-content` to enable absolute-positioned sub-slides |
| `.pX-slide` | Sub-slide container; hidden by default. Add `.is-default-visible` to the first one |
| `.pX-slide[data-color="blue|red|yellow|green"]` | Brand-color theming for slot accents + bullet borders |
| `.hero-figure` + `.src-handle` | Phase 1 image card (tweet/screenshot/UI) — replaces `.subhead` |
| `.settings-figure` + `.inline-mono` | Phase 2B UI screenshot card with mono-tagged caption |
| `.p3-slot-num` + `.p3-eyebrow` + `.p3-headline` | Numbered feature slide ("01 / FEATURE") |
| `.p3-bullets` / `.p2-c-bullets` | Bullet list with mono `.bullet-tag` + sans `.bullet-detail` |
| `.p4-pills` | Phase 4 feature-pill list (perf/security wins) |
| `.p4-perf-eyebrow` + `.p4-perf-headline` | Phase 4 perf-pill stage typography |

**Markup pattern (any phase, any number of sub-slides):**

```html
<div id="phase3" class="phase">
  <div class="phase-content p3-stage">
    <div id="p3-intro" class="p3-slide is-default-visible">
      <!-- intro card -->
    </div>
    <div id="p3-slide-a" class="p3-slide" data-color="blue">
      <div class="p3-slot-num">01</div>
      <div class="eyebrow p3-eyebrow">FEATURE NAME</div>
      <h2 class="p3-headline">One-line headline.</h2>
      <ul class="p3-bullets">
        <li><span class="bullet-tag">TAG</span><span class="bullet-detail">Detail prose</span></li>
      </ul>
    </div>
  </div>
</div>
```

**GSAP pattern (FLICKER-FREE — `tl.set` + `tl.to`, never `tl.from(... immediateRender:false)`):**

```js
// Hide all sub-slide content at t=0 (prevents one-frame flash before reveal)
tl.set("#p3-slide-a .p3-slot-num", { scale: 0.7, opacity: 0 }, 0);
tl.set("#p3-slide-a .p3-eyebrow",  { y: 16, opacity: 0 }, 0);
tl.set("#p3-slide-a .p3-headline", { y: 28, opacity: 0 }, 0);
tl.set("#p3a-b1", { x: -28, opacity: 0 }, 0);

// Crossfade intro → slide A at the narration anchor
const SLIDE_A_AT = 50.21;  // narration timestamp
tl.to("#p3-intro",   { opacity: 0, scale: 0.96, filter: "blur(12px)", duration: 0.4 }, SLIDE_A_AT - 0.30);
tl.set("#p3-intro",  { visibility: "hidden" }, SLIDE_A_AT + 0.10);
tl.set("#p3-slide-a", { visibility: "visible", opacity: 0, scale: 0.97, filter: "blur(12px)" }, SLIDE_A_AT - 0.10);
tl.to("#p3-slide-a", { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.4 }, SLIDE_A_AT - 0.10);

// Animate sub-slide content in
tl.to("#p3-slide-a .p3-slot-num", { scale: 1, opacity: 1, duration: 0.55, ease: "back.out(1.7)" }, SLIDE_A_AT);
tl.to("#p3-slide-a .p3-eyebrow",  { y: 0, opacity: 1, duration: 0.5 }, SLIDE_A_AT + 0.20);
tl.to("#p3-slide-a .p3-headline", { y: 0, opacity: 1, duration: 0.55 }, SLIDE_A_AT + 0.40);

// Reveal each bullet at its own narration anchor
tl.to("#p3a-b1", { x: 0, opacity: 1, duration: 0.45 }, NARRATION_ANCHOR_FOR_BULLET_1);
```

**Why `tl.set` + `tl.to` instead of `tl.from`?** `tl.from(...)` with `immediateRender: false` leaves the element at its CSS-default visible state until the tween fires, then snaps to the from-state and animates — a one-frame flash on playback. The `set` + `to` pattern keeps the element hidden the entire time.

For working examples of the multi-sub-slide architecture see `videos/_archived/gemini-cli-v040-short/index.html` — it uses 3 sub-slides in Phase 2 (terminals → settings UI → explainer), 5 sub-slides in Phase 3 (intro + 4 features + 1 add-on), and 2 sub-slides in Phase 4 (perf-pills → CTA close).

## Brand surfaces

The Google logo (`assets/google-logo.png`) sits at the top-center for the full duration. The `@handle` is in the top-right. Both are persistent (no `class="clip"`). The Dynamous logo (`assets/dynamous-logo.png`) is local — never reference `../../shared/logos/...` paths because HyperFrames' bundler rejects them.

## When NOT to use this variant

Use this variant for any Google-branded or Google-developer content. Cues that signal the wrong fit:

- The brand is Anthropic / Claude → use [`templates/shorts/anthropic/`](../anthropic/) or [`templates/shorts/claude-code-version/`](../claude-code-version/)
- The content has no brand at all → use [`templates/shorts/standard/`](../standard/) (when it lands)
- The aesthetic should be light / minimal rather than cinematic dark stage with corner glows → fork this template and switch to `theme-editorial` as the default

## Customizing per video

Most styling is driven by CSS variables on `:root` in `tokens/google-cinematic.css`. Override per video by re-declaring any var in a tighter scope:

```css
/* In videos/<slug>/tokens/google-cinematic.css OR inline in index.html */
:root {
  --accent:        var(--g-red);                 /* swap primary accent */
  --accent-glow:   rgba(234, 67, 53, 0.35);
  --pad-top:       260px;                        /* nudge top safe-zone */
}
```

**Per-phase accent rotation:** by default, every phase uses the same `--accent` (blue). If you want each phase to lead with a different Google color, set inline `style="--accent: var(--g-red);"` on the phase wrapper (`#phase2`, `#phase3`, etc.) — the eyebrow, CTA pill border, and progress-bar fill will all pick it up.

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
- No `class="clip"` on `#glogo`, `#footer-handle`, `#progress-rail`, `#dynamous-badge`, or `#dynamous-module-interstitial-wrap` — those are persistent visual chrome.
- No `<br>` in content text — use `text-wrap: balance` on the headline / subhead for natural wrapping.
- No orange / pink / cyan accents on the chip grid or rail dots — use the four Google brand colors only (blue / red / yellow / green) so the brand reads cleanly.
- The Dynamous module-interstitial sub-comp uses class-only CSS selectors (no `#dynamous-module-interstitial .dmi-card` chains). Keep it that way — ID-prefixed selectors don't survive HyperFrames' sub-comp scoping reliably.
