# new-google-short — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames Short in the **Google brand cinematic-stage aesthetic** (vertical 1080x1920, 30fps, 24-180s) using [`templates/shorts/google/`](../../../templates/shorts/google/). Zero manual steps; ends at preview, never renders.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A. Use the pipeline by default; use this skill directly only when you already have a script.

This playbook is the Google-template analog of [new-anthropic-short.md](./new-anthropic-short.md). The shape is identical — only the template, palette, persistent chrome, and Dynamous defaults differ. Key deltas:

- **Template**: `templates/shorts/google/` (instead of `templates/shorts/anthropic/`)
- **Palette**: canonical Google brand four-color rotation `blue → red → yellow → green → blue` on a `#06080F` deep-navy with four-corner brand glows. `--accent` colors persistent chrome (eyebrow, CTA stroke, progress-bar fill, `@` symbol); the four chip / rail colors rotate independently.
- **Persistent chrome**: Google logo (top-center), `@handle` (top-right with accent-tinted `@`), 5-dot progress rail (SETUP / CREATE / EVAL / DEPLOY / PUBLISH — one dot active per phase), 4px green→yellow top-left ramp, particle field (60 deterministic dots), inner safe-area frame, slim progress bar at bottom edge.
- **Phase mix**:
  1. **Phase 1 — Hero**: accent eyebrow + xl headline (148px) + subhead — no rail dot active
  2. **Phase 2 — Terminal**: m headline + 2 colored-syntax terminal blocks — rail dot 0 (SETUP, blue) active
  3. **Phase 3 — Info grid**: m headline + 2x2 chip grid in 4 Google colors — rail dot 1 (CREATE, red) active. Alt archetype: `.bigstat` (360px gradient number).
  4. **Phase 4 — Shift / CTA**: m headline + accent-bordered quote + CTA pill with finite pulse — rail dot 4 (PUBLISH, blue) active. Optional `theme-light` for the bright "shift" variant.
- **Theme switch**: `class="theme-cinematic"` on `#root` is default; switch to `theme-spotlight` (single accent beam from top) or `theme-editorial` (60px hairline grid) per video for variety.
- **Dynamous promotion: badge + discount bubble + endcard ON by default; module interstitial OFF by default** (mirrors `templates/shorts/claude-code-version/` and the long-form claude-code-version template). The interstitial popup competes with the hero→setup transition on a 90-180s shorts canvas, so it's opt-in per video — set `dynamous.moduleInterstitial = true` only when the short is specifically promoting a Dynamous module. Operators turn anything else off per video by editing `video.config.js`, NOT by deleting the elements.

## Inputs

User provides ONE of:

- A **topic / prompt** (e.g. _"Gemini 2.0 Flash launch"_, _"Why Workspace + AI is killing Notion"_) — agent drafts the full script
- A **title + key facts** — agent uses the facts verbatim, drafts the framing
- A **pre-written `script.txt`** — agent skips drafting (jump to step 5)

If the topic has no real source data and would require fabricated stats/dates, **stop and ask the user for a source URL** before proceeding. Never invent numbers.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with `script.txt`, `audio/narration.wav`, `transcript.json`, filled `index.html`, optional Dynamous overrides in `video.config.js`, and preview studio open in the browser.

The user runs render themselves: `npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4`.

---

## Steps

### 1. Confirm slug + title

Kebab-case slug (3-6 words). For Google-product launches, suffix with `-short`:

- "Gemini 2.0 Flash launch" → `gemini-2-flash-launch-short`
- "Workspace AI features March update" → `workspace-ai-march-short`
- "Android 16 dev preview" → `android-16-preview-short`

Confirm in one line: _"Spawning `videos/gemini-2-flash-launch-short/` — title 'Gemini 2.0 Flash Launch'. Proceed?"_

### 2. Copy the template

```bash
cp -r templates/shorts/google videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/shorts/google videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `video.config.js`, `sfx-cues.txt`, `tokens/google-cinematic.css`, `compositions/dynamous-module-interstitial.html`, `DESIGN.md`, `README.md`, `audio/`, `assets/google-logo.png`, `assets/dynamous-logo.png`, `assets/shapes/`, `assets/sfx/` should all exist.

### 3. Update meta.json

```json
{
  "id": "<slug>",
  "name": "<Title Case Name>"
}
```

### 3.5. Confirm Dynamous promotion (defaults: badge + bubble + endcard ON, interstitial OFF)

Unlike `new-anthropic-short` and `new-archon-short` (all default OFF), this template ships with the persistent Dynamous overlays enabled and the timed module interstitial OFF. Confirm with the user:

> _"Dynamous defaults: badge ON, 10% OFF bubble ON, endcard ON, module interstitial OFF. Keep these, or change anything?"_

Edit `videos/<slug>/video.config.js` per the user's answer:

| User says | Action |
|---|---|
| "keep defaults" / no answer | Leave `video.config.js` untouched |
| "turn off the badge" | Set `dynamous.badge = false` |
| "turn on the module interstitial" / "promote module N" | Set `dynamous.moduleInterstitial = true`, update `moduleId/Name/AccentColor` |
| "turn off the discount bubble" | Set `dynamous.discountBubble = false` |
| "turn off the endcard" | Set `dynamous.endcard = false` |
| "all off" | Set all four flags to `false` |
| "different module" (only relevant if interstitial is ON) | Update `dynamous.moduleId`, `dynamous.moduleName`, `dynamous.moduleAccentColor` |

If the user wants a different Dynamous module mapped to the topic and the interstitial is enabled, run `node scripts/find-dynamous-module.js <tags>` (if it exists) or read `shared/lib/blocks/dynamous-module-interstitial/recipe.md` for the canonical module list. Pick the closest match.

**Endcard + channel CTA timing**: the endcard fires at `totalDuration - 5` and fades competing chrome 0.5s before that. If the script's channel CTA (subscribe pill) sits in the last 5s of narration, retime the pill earlier so it gets ~3s of solo visibility BEFORE the endcard fade — sync to a narration anchor at least 3s ahead of `totalDuration - 5`. The current `new-google-short` workflow does this automatically (Phase 4 step 8 item 13).

### 4. Theme + accent picks

Decide three per-video knobs (matches the source design's "Tweaks panel"):

| Knob | Default | Pick from | Where to set |
|---|---|---|---|
| **Theme** | `theme-cinematic` | `theme-cinematic` / `theme-spotlight` / `theme-editorial` | `class` on `#root` in `index.html` |
| **Accent** | blue (`--g-blue`) | blue / red / yellow / green | inline `style="--accent: var(--g-red); --accent-glow: rgba(234,67,53,0.35);"` on `#root` |
| **Light shift on Phase 4** | OFF (dark cinematic) | ON / OFF | add `class="phase theme-light"` on `#phase4` |

**Theme picks by content shape:**

- `theme-cinematic` (default) — premium product launch, AI feature reveal, brand moment. Maximum brand presence with all four corner glows.
- `theme-spotlight` — single hero stat / number / payoff. The accent beam from top focuses attention on one thing.
- `theme-editorial` — quiet announcement, post-mortem, methodology explainer. Hairline grid + flat dark surface reads as documentary.

**Accent picks by mood:**

- **Blue** (default): premium, calm, trustworthy. AI features, infra, Google AI Studio.
- **Red**: urgent, alert, pivot. Postmortems, critical updates, deprecations.
- **Yellow**: optimistic, energetic, growth. Workspace launches, creator-tool wins.
- **Green**: success, new, ship. Beta-to-GA promotions, Cloud, Android.

**Light-shift on Phase 4**: turn ON for "the shift" / vision / philosophy / inspirational closes. Turn OFF for technical / changelog / "ship it" closes.

### 5. Draft the script

Two branches — try Branch A first.

#### Branch A — pipeline output exists (preferred)

If `videos/<slug>/scripts/full-script.md` exists, READ it as authoritative. Map its `## Scene N` sections onto the four template phases (Hero / Terminal / Info-grid / Shift-CTA). If the script's content shape doesn't match (e.g. no terminal moment), swap Phase 2's `.terminal` block for a `.bigstat` or a quote — see `templates/shorts/google/DESIGN.md` "Alternate archetype" rows.

#### Branch B — direct draft

Map narration to the four phase archetypes:

| Phase | Duration target | What to write |
|---|---|---|
| **1 — Hero** | 5-7s | Mono eyebrow (2-3 words ALL CAPS): the section label. Hero headline (3-7 words, balanced two-line wrap). Subhead (5-9 words): the receipt. |
| **2 — Terminal** | 6-8s | Mono eyebrow. Headline (3-7 words). Two terminal lines: command + arg + flag, real CLI strings only. Color tokens: `cmd` green (`uvx`, `gemini`), `arg` ink-100 (`google-agents-cli`, `chat`), `flag` yellow (`--stream`, `--model`), `kw` blue (`create`, `deploy`), `str` peach (string literals). |
| **3 — Info grid** | 5-8s | Mono eyebrow. Headline (3-7 words). 2x2 chip grid: each chip = mono UPPERCASE label (1 word) + sans value (1-2 words). Real label/value pairs only. Colors rotate blue / yellow / green / red. |
| **4 — Shift / CTA** | 4-6s | Mono eyebrow ("THE SHIFT" / "WHAT'S NEXT" / "TRY IT"). Headline (3-7 words). Quote (10-16 words, the philosophy line). CTA pill: mono UPPERCASE label (e.g. "DROP", "TRY", "RUN") + value (e.g. "GEMINI", "CLI", "BETA"). |

**Style rules** (apply during writing):

- Short sentences. ≤18 words for natural Kokoro / ElevenLabs prosody.
- Never use semicolons or em-dashes — TTS stumbles. Use periods.
- Numbers: write digits, not words ("3 signals" not "three signals") — matches the visual chips / stats.
- Never use `<br>` in content. Rely on `text-wrap: balance` and font size.
- Total target: **70-130s** (24s template demo is just the layout proof — real videos run ~90s).
- Read [`.claude/references/script-library.md`](../../references/script-library.md) for gold-standard examples.

Save to `videos/<slug>/script.txt` in the standard 4-block format (one phase per blank-line block):

```
[phase 1 narration]

[phase 2 narration]

[phase 3 narration]

[phase 4 narration]
```

### 6. Generate TTS + transcript

```bash
python scripts/elevenlabs-tts.py videos/<slug> --shorts
```

This writes BOTH `videos/<slug>/audio/narration.wav` AND `videos/<slug>/transcript.json` in a single API call (voice ID, model, settings, pronunciation dictionary loaded from `.env`). The `--shorts` flag selects `ELEVENLABS_SPEED_SHORTS`.

If the script changes, re-run — overwrites both files atomically.

### 7. Compute phase boundaries

Read `transcript.json` and identify, in seconds:

- `phase1_end` — `end` time of the last word of the phase 1 narration block
- `phase2_end` — same for phase 2
- `phase3_end` — same for phase 3
- `phase4_end` — `end` time of the last word in the file
- `total_duration` = `phase4_end + 1.5` (1.5s tail for reading the CTA before loop)

Then the GSAP anchors:

```
T1 = phase1_end - 0.2
T2 = phase2_end - 0.2
T3 = phase3_end - 0.2

P2 = T1 + 0.4
P3 = T2 + 0.4
P4 = T3 + 0.4
```

For per-chip (Phase 3) entrances, identify the spoken-anchor for each chip's first word and compute `chip_N_at = transcript[<anchor-word>].start - P3`. For per-terminal (Phase 2) entrances, same pattern (`term_N_at`).

### 7.5. Decide single-slide vs multi-sub-slide per phase

The template ships with the four-phase mutex layout (one slide per phase). For longer / content-rich shorts (90s+) any phase can be **extended into multiple sub-slides** that crossfade in sequence. The template's `<style>` block already includes the reusable CSS (`.pX-stage`, `.pX-slide`, `.is-default-visible`, `.p3-bullets`, `.p2-c-bullets`, `.p4-pills`, `.hero-figure`, `.settings-figure`, `.inline-mono`, etc.) — operators only need to add the markup + GSAP wiring.

**When to extend a phase:**

| Phase | Extend when | Sub-slide pattern |
|---|---|---|
| 1 (Hero) | The topic has a strong source visual (tweet screenshot, website, app screenshot) | Replace `.subhead` with `<figure class="hero-figure">` containing `<img>` + `<figcaption>` |
| 2 (Setup) | The topic has BOTH a CLI install flow AND a UI/settings step | 2A terminals → 2B settings screenshot → optional 2C explainer card |
| 3 (Features) | The release has 4-6 distinct features each worth its own beat | Intro card → numbered sub-slides (`01 / FEATURE` per beat) with bullet list — narrate each as the slide appears |
| 4 (Close) | The topic has a "smaller wins" sweep before the CTA | 4A perf/security pill list → 4B CTA close |

**Markup pattern (any phase, any number of sub-slides):**

```html
<div id="phaseN" class="phase">
  <div class="phase-content pN-stage">

    <div id="pN-slide-a" class="pN-slide is-default-visible">
      <!-- first sub-slide content — eyebrow + headline + bullets/figure -->
    </div>

    <div id="pN-slide-b" class="pN-slide" data-color="blue">
      <!-- second sub-slide -->
    </div>

    <!-- … more sub-slides … -->
  </div>
</div>
```

**GSAP wiring pattern (flicker-free) — see Step 8 item 11.**

### 8. Edit `videos/<slug>/index.html`

Always invoke the `/hyperframes` skill before this step.

Edit in this exact order (one Edit per change):

1. **`<title>`** in `<head>` → the video title
2. **`#root`** `class` → `theme-cinematic` / `theme-spotlight` / `theme-editorial` (per Step 4 pick)
3. **`#root`** inline `style` → if non-default accent: `style="--accent: var(--g-red); --accent-glow: rgba(234,67,53,0.35);"` (per Step 4 pick)
4. **`#root`** `data-duration` → `total_duration` (rounded to 0.1s)
5. **`#footer-handle`** text → real `@handle` (after the `<span class="at">@</span>`)
6. **Phase 1**: `#p1-eyebrow`, `#p1-headline`, `#p1-subhead` text
7. **Phase 2**: `#p2-eyebrow`, `#p2-headline`. Each `.terminal` block — keep the colored `<span>` structure (`prompt`, `cmd`, `arg`, `flag`, `kw`, `str`) and swap the inner text. Real CLI commands only — never invent.
8. **Phase 3**: `#p3-eyebrow`, `#p3-headline`. Each `.chip`'s `.chip-label` + `.chip-value`. Rotate `data-color` `blue → yellow → green → red` (matches default order). If you only have 2-3 real signals, comment out the unused chips AND remove their tweens.
9. **Phase 4**: `#p4-eyebrow`, `#p4-headline`, `.q-text` (quote), `.cta-label` + `.cta-value`. Optionally add `class="phase theme-light"` on `#phase4` for the shift surface.
10. **Phase 4 alternate (light shift):** if Step 4 picked light, change `<div id="phase4" class="phase">` to `<div id="phase4" class="phase theme-light">`.
10.5. **Flicker-free reveals (HARD RULE)**: For any element that should be hidden until a specific timeline anchor (sub-slide content, mid-phase reveals, anything firing >1s after the phase becomes visible), **do not** use `tl.from(el, { ... }, T)` — that pattern leaves the element in its CSS-default visible state until `T`, then snaps it to the from-state and animates. The result is a one-frame flash on playback. Instead use the **`tl.set` + `tl.to` pattern**:

```js
// Correct — element stays hidden from t=0 until the anchor, then animates in
tl.set("#reveal-target", { y: 28, opacity: 0 }, 0);
tl.to("#reveal-target",  { y: 0,  opacity: 1, duration: 0.5, ease: "power2.out" }, NARRATION_ANCHOR);
```

Apply this to every Phase 2 / 3 / 4 reveal that fires past the phase entrance. The Phase 1 hero entrance (firing 0.9-1.7s after t=0) can stay on `tl.from()` because the canvas is just becoming visible there — no flash window. For sub-slide crossfades, the `pXCrossfade(outSel, inSel, at)` helper pattern handles the visibility flip with `tl.set` calls bracketing the opacity/scale tween.

11. **Transition timestamps**: replace `const T1 = 5.6;`, `const T2 = 11.6;`, `const T3 = 17.6;` with computed values.
12. **Phase anchors**: replace `const P2 = 6.4;`, `const P3 = 12.4;`, `const P4 = 18.4;` with computed values.
13. **Per-element anchors** (chips in Phase 3, terminals in Phase 2): replace the literal `P3 + 0.8 / 1.0 / 1.2 / 1.4` and `P2 + 0.9 / 1.5` with `P3 + chip_N_at` / `P2 + term_N_at` from Step 7 (or absolute computed values).
14. **Progress bar tween**: change `duration: TOTAL_DURATION` (the `#progress-fill` `fromTo`) — `TOTAL_DURATION` is already a top-of-script const, just update its value at the top.
15. **Const at top of `<script>`**: change `const TOTAL_DURATION = 24;` to the new `total_duration`.
16. **Particle drift**: change `duration: 12` (yoyo half-period) to `total_duration / 2` rounded to 0.1s.
17. **Audio element**: insert just before `</div>` (the closing tag of `#root`), at the same indent level as `<div id="phase4">`:

```html
  <audio id="narration"
         class="clip"
         src="audio/narration.wav"
         data-start="0"
         data-duration="<phase4_end>"
         data-track-index="2"
         data-volume="1"></audio>
```

18. **Wire SFX from `retention-strategy.md`** if Phase 3.5 ran (skip if not). Same workflow as [new-anthropic-short.md](./new-anthropic-short.md) Step 8 item 14: read `sfx_cues:` blocks → `bash scripts/sync-video-sfx.sh videos/<slug> ${cues[@]}` → insert `<audio>` elements with `data-volume ≤ 0.25`. Reference cue map for this template:
    - Phase 1 hero headline reveal: `impact-slam` at the headline anchor word (volume 0.15)
    - Phase 2 first terminal entrance: `scale-slam` (volume 0.15)
    - Phase 3 chip 1 entrance only (skip 2-4 to stay under density cap): `spring-pop` (volume 0.11)
    - Each phase transition (T1, T2, T3): `cinematic-whoosh` (volume 0.11)
    - Phase 4 CTA entrance: `pop` (volume 0.10)

### 9. Discount-bubble timing (only if `discountBubble: true`)

The guard script auto-wires `#dynamous-discount-bubble`'s `data-start` to the Phase 4 entrance (default 18.4s). After Step 7 recomputed the timeline, override `discountBubbleStart` in `video.config.js` to the new `P4` value:

```js
discountBubbleStart: 76.2,    // P4 in the recomputed timeline
discountBubbleDuration: 6,    // length of Phase 4 + tail
```

If `discountBubble` is `false`, skip this step.

### 10. Lint

```bash
npx hyperframes lint videos/<slug>
```

Must report `0 errors`. Common variant-specific issues:

| Error | Likely cause | Fix |
|---|---|---|
| `audio_src_not_found` (narration) | `narration.wav` missing | Re-run step 6 |
| `audio_src_not_found` (sfx) | Cue `.mp3` missing | `bash scripts/sync-video-sfx.sh videos/<slug> <cue>` |
| `gsap_infinite_repeat` | A `repeat: -1` slipped in | Use a finite count |
| `overlapping_gsap_tweens` (sfx) | Two SFX on same `data-track-index` overlap | Bump second SFX to next track index |

Warnings about `composition_file_too_large` are advisory (the inline-phase-mutex layout intentionally trips this — same as anthropic / claude-code-version shorts).

### 11. Inspect for layout overflow

```bash
npx hyperframes inspect videos/<slug>
```

Common variant-specific overflows:

- **Hero headline at xl (148px) overflows** if it's >2 lines. Drop to `class="headline l"` (128px) or `m` (104px) per `templates/shorts/google/DESIGN.md` size table.
- **Terminal command exceeds 920px width** — shorten the command, or split into two terminal blocks.
- **Chip value overflows the 446px chip width** — shorten the value (single-word values read best). Long brand names ("Cloud Run", "Vertex AI") fit; full sentences don't.
- **Quote overflows 920px width** — shorten to ≤16 words, or drop `.q-text` font-size from 64px to 56px.
- **CTA pill value overflows** — keep `.cta-value` to a single 3-7 char token (`CLI`, `GEMINI`, `BETA`).

Fix overflow at the CSS or content level, then re-run `inspect` until clean.

### 12. Open preview (final step — never render)

Run in background so the studio stays open:

```bash
npx hyperframes preview videos/<slug>
```

Capture the URL.

### 13. Generate YouTube description

**MUST follow [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md) end-to-end.**

Quick checklist:

1. **vidIQ keyword research** against the topic (e.g. `vidiq_keyword_research` for "Gemini Flash", "Google AI", "Workspace AI"). Save to `videos/<slug>/research/vidiq-keywords.md`.
2. **Shorts skip Chapters** — vertical Shorts do not include a `Chapters` section.
3. **Draft `videos/<slug>/youtube-description.md`** — LEAN structure per the rule: SEO hook → Dynamous block in `----` separators (Dynamous ON by default for this template) → Resources: with validated URLs → Hostinger affiliate block in `----` separators (MANDATORY: `🏠 Self-host your AI agents & projects on Hostinger (10% OFF): 👉 https://hostinger.com/DIYSMARTCODE`) → debate question → 15-25 hashtags. **NO Key Changes bullets, NO Key Concepts, NO Chapters — all explicitly cut from the template.**
4. **Validate every URL** with `WebFetch`. Keep total description ~800-1500 chars.

### 14. Report to the user

```
✅ <Title>
   Slug:        <slug>
   Theme:       <cinematic|spotlight|editorial> + <accent>
   Light shift: <on|off>
   Dynamous:    <badge|moduleInterstitial|discountBubble> on / off
   Render:      npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4
   Length:      <N>s
   Voice:       <voice-id> @ <speed>×
   YouTube:     videos/<slug>/youtube-description.md (paste-ready)
   Preview:     http://localhost:5173
```

That's it. Stop. Wait for user to iterate or trigger render manually.

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow on hero, terminals, chips, quote, CTA
- [ ] All four phases have real content (no leftover template placeholders: "AGENTS CLI", "Agents need a path.", "Setup is a single line.", "uvx google-agents-cli", "Four signals. One map.", "SKILLS / installed", "THE SHIFT", "Cloud becomes a command surface.", "DROP / CLI" — unless the video genuinely uses these)
- [ ] Phase transition timestamps computed from transcript, NOT left at template defaults (5.6 / 11.6 / 17.6)
- [ ] Audio element wired with correct `data-duration`
- [ ] If `discountBubble: true`, `discountBubbleStart` in `video.config.js` matches the recomputed Phase 4 anchor
- [ ] No 5th accent color anywhere (only the 4 Google brand hues across chips and rail)
- [ ] No orange anywhere except in terminal `str` color (peach for string literals — that's the only legitimate non-Google-brand color in the composition)
- [ ] Total duration ≤ 180s (YouTube Shorts hard max); preferably 70-130s
- [ ] Preview URL is reachable

---

## Don'ts

- Never auto-render — user explicitly always triggers render manually.
- Never fabricate stats, dates, version numbers, CLI command names, or feature descriptions. Every script line and on-screen string must trace to `tmp/source.md` (the article the user provided) or a screenshot the user attached. If the source is silent on a needed claim, STOP and ask the user for a source URL — never proceed with a guess. See `feedback_no_fabrication_source_only` in project memory for the full rule. Audit the YouTube description against the same source — every bullet, chapter title, and hashtag must trace back.
- Never use `tl.from(... immediateRender: false)` for narration-synced reveals — it causes a one-frame flash. Use the `tl.set` (hide at t=0) + `tl.to` (animate in at anchor) pattern instead. See Step 8 item 10.5.
- Never modify `templates/shorts/google/` — only the copy under `videos/<slug>/`.
- Never introduce a 5th accent color. The four Google hues are the brand.
- Never use orange as a primary accent — it's not a Google brand color.
- Never reference `shared/logos/` paths at runtime — always copy logos into `videos/<slug>/assets/` first.
- Never delete the Dynamous overlay elements from `index.html` to "turn them off" — toggle the flag in `video.config.js` instead. The guard script removes the elements synchronously.
- Never rewrite the module-interstitial sub-comp's CSS to use `#dynamous-module-interstitial`-prefixed selectors. Class-only selectors are intentional — they survive the framework's sub-comp ID rewriting.
- Never add `class="clip"` to `#glogo`, `#footer-handle`, `#progress-rail`, `#dynamous-badge`, `#dynamous-module-interstitial-wrap`, `#slide-frame`, `#particles`, `#top-line`, or `#version-branding` (that one's not in this template but the rule generalizes). Persistent visual chrome stays unclipped.
- Never use `repeat: -1` on the CTA pulse or anywhere else — deterministic timeline rule.
- Never use `Math.random()` / `Date.now()` / network fetches in the composition.
- Never write `<br>` in content text — use `text-wrap: balance`.
- Never run multiple `new-google-short` invocations in parallel against the same slug.
- Never close the user's main `Chrome.exe` if running `agent-browser` for QA / capture.
