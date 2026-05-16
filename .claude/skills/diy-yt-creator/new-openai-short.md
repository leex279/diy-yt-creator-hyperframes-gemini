# new-openai-short — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames Short in the **OpenAI monochrome-editorial aesthetic** (vertical 1080x1920, 30fps, 24-180s) using [`templates/shorts/openai/`](../../../templates/shorts/openai/). Zero manual steps; ends at preview, never renders.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 and writes the artifacts under `videos/<slug>/` that step 5 below picks up via Branch A. Use the pipeline by default; use this skill directly only when you already have a script.

This playbook is a **tight delta from [new-google-short.md](./new-google-short.md)**. The overall shape (12-step workflow, Dynamous wiring, lint/inspect/preview gates) is identical — only the template, palette, brand chrome, and accent-rotation knobs differ. **Read new-google-short.md first**, then apply the deltas below for any OpenAI video.

## Deltas from new-google-short

| Dimension | Google variant | OpenAI variant (this skill) |
|---|---|---|
| **Template** | `templates/shorts/google/` | `templates/shorts/openai/` |
| **Palette** | 4-color rotation `blue → red → yellow → green` on cinematic `#06080F` deep-navy with four-corner glows | **Single mint accent** (`#10A37F`) on flat `#0A0A0A` off-black — no rotation, no corner glows by default. Auxiliary lavender/amber/coral reserved for **whole-video override** only (Sora / DALL·E / warning). |
| **Brand mark** | Google logo (top-center, 120px) | **ChatGPT spirograph** (`assets/chatgpt-mark.svg`, 110px, top-center). Swap to `assets/openai-wordmark.png` (drop to 80-90px) for cross-sub-brand videos (GPT / Sora / DALL·E / Codex). |
| **Progress rail labels** | SETUP / CREATE / EVAL / DEPLOY / PUBLISH (5 different colors per dot) | **INTRO / BUILD / SIGNAL / SHIFT / CTA** (5 dots, all mint when active) |
| **Default theme class on `#root`** | `theme-cinematic` (four-corner glows) | **`theme-quiet`** (flat, no glows). Opt into `theme-cinematic` (single mint top glow) for hero/launch moments; `theme-editorial` adds a faint 60px hairline grid. |
| **Terminal rim** | Four-color top stroke (`with-rim`) | Single mint hairline top stroke |
| **Background** | 60 particle dots in 4 Google colors | **12-shape SVG backdrop** at 6% opacity (spirograph hexagon · Daybreak sunrise arcs · hex/network nodes). Reorders on every phase + sub-slide transition paired with `cinematic-whoosh` SFX. |
| **Hero figure (Phase 1)** | not built-in | **opt-in** `.hero-figure` slot — drop a tweet/screenshot/UI image into `assets/`, replace `<p class="subhead">` with the `<figure class="hero-figure">` block (recipe in [`templates/shorts/openai/README.md`](../../../templates/shorts/openai/README.md)). Tilt-in animation: `tl.from('#p1-figure', { rotateY: 8, transformPerspective: 1200, y: 40, scale: 0.94, opacity: 0, duration: 0.9, ease: 'power3.out' }, T)`. Use whenever the topic is sourced from a public post — much higher trust than a generic subhead. |
| **Chip data-color values** | `blue / red / yellow / green` (rotate per chip) | `mint / lavender / amber / coral` (default: every chip `mint`). Use auxiliary tints only for whole-video re-skinning, never per-chip rotation. |
| **Phase 4 rail dot** | dot 4 (PUBLISH, blue) | **dot 3 (SHIFT) at headline, then dot 4 (CTA) at the pill** — rail visibly completes by render end |
| **Aesthetic anchor** | premium cinematic launch stage | **quiet editorial surface** — reads like `openai.com/research`, not `openai.com/sora` |

Everything else — Dynamous defaults (badge + bubble + endcard ON, interstitial OFF), the four-phase mutex layout, sub-slide CSS, `tl.set` + `tl.to` flicker-free reveal pattern, TTS pipeline, transcript-driven phase boundaries, SFX wiring, lint/inspect/preview gates, YouTube metadata workflow — is **byte-identical** to new-google-short. Don't re-read those sections; follow new-google-short and substitute the deltas above.

## Inputs

User provides ONE of:

- A **topic / prompt** (e.g. _"GPT-5 launch"_, _"Why Sora 2 broke its own constraints"_, _"ChatGPT Atlas browser launch"_) — agent drafts the full script
- A **title + key facts** — agent uses the facts verbatim, drafts the framing
- A **pre-written `script.txt`** — agent skips drafting (jump to step 6)

If the topic has no real source data and would require fabricated stats/dates, **stop and ask the user for a source URL** before proceeding. Never invent numbers.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with `script.txt`, `audio/narration.wav`, `transcript.json`, filled `index.html`, optional Dynamous overrides in `video.config.js`, and preview studio open in the browser.

The user runs render themselves: `npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4`.

---

## Steps (deltas from new-google-short)

### 1. Confirm slug + title

Kebab-case slug (3-6 words). Suffix with `-short`:

- "GPT-5 launch" → `gpt5-launch-short`
- "Sora 2 deep dive" → `sora-2-deep-dive-short`
- "ChatGPT Atlas browser" → `chatgpt-atlas-launch-short`
- "DALL·E 4 image quality wins" → `dalle-4-quality-short`

Confirm in one line: _"Spawning `videos/gpt5-launch-short/` — title 'GPT-5 Launch'. Proceed?"_

### 2. Copy the template

```bash
cp -r templates/shorts/openai videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/shorts/openai videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `video.config.js`, `sfx-cues.txt`, `tokens/openai-mono.css`, `compositions/dynamous-module-interstitial.html`, `compositions/dynamous-endcard.html`, `DESIGN.md`, `README.md`, `audio/`, `assets/chatgpt-mark.svg`, `assets/openai-wordmark.png`, `assets/dynamous-logo.png`, `assets/shapes/`, `assets/sfx/` should all exist.

### 3. Update meta.json — same as new-google-short.

### 3.5. Confirm Dynamous promotion — same defaults and rules as new-google-short

Defaults: badge ON, 10% OFF bubble ON, endcard ON, module interstitial OFF. Edit `video.config.js` per user answer using the same table as new-google-short Step 3.5.

### 4. Theme + accent picks (DELTA from new-google-short)

Decide three per-video knobs:

| Knob | Default | Pick from | Where to set |
|---|---|---|---|
| **Theme** | `theme-quiet` | `theme-quiet` / `theme-cinematic` / `theme-editorial` | `class` on `#root` in `index.html` |
| **Accent** | mint (`--oai-mint`) | mint / lavender / amber / coral | inline `style="--accent: var(--oai-lavender); --accent-glow: rgba(167,139,250,0.32);"` on `#root` |
| **Light shift on Phase 4** | OFF (dark mono) | ON / OFF | add `class="phase theme-light"` on `#phase4` |
| **Brand mark** | ChatGPT spirograph | spirograph / OpenAI wordmark | edit the `<img>` inside `#brand-mark` |

**Theme picks by content shape:**

- `theme-quiet` (default) — the OpenAI editorial register. Quiet announcements, research releases, system-card-style explainers, postmortems. Maximum brand restraint.
- `theme-cinematic` — single soft mint top-center glow. Use for hero/launch moments where the quiet surface needs a hint of warmth (a new product line, a flagship release).
- `theme-editorial` — faint 60px hairline grid. Documentary feel, methodology explainers, AI-policy reads.

**Accent picks by topic:**

- **Mint** (default): ChatGPT, GPT, Codex, generic OpenAI announcements. The canonical brand hue.
- **Lavender**: Sora 1/2, video-gen, multimodal-vision releases. The "creative" sub-brand surface.
- **Amber**: DALL·E, image-gen, color/light-focused product surfaces.
- **Coral**: regressions, deprecations, safety/policy callouts. Use sparingly — the only "warning" accent.

**Brand mark pick:** spirograph for ChatGPT-specific content; OpenAI wordmark for anything cross-sub-brand (GPT-5 / Sora / DALL·E / Codex / company-wide announcements). When swapping to the wordmark, drop `#brand-mark img { height: 110px; }` to **`80-90px`** — the wordmark is wider and 110px makes it dominate the top safe zone.

**Light-shift on Phase 4**: turn ON for "the shift" / vision / philosophy / inspirational closes. Turn OFF for technical / changelog / "ship it" closes. (Identical to new-google-short; the light surface is warm off-white `#F4F4F2` instead of the bluer Google variant.)

### 5. Draft the script (DELTA)

Two branches — try Branch A first (pipeline output exists at `videos/<slug>/scripts/full-script.md`). Otherwise direct draft.

Map narration to the four phase archetypes — **same shape as new-google-short**, with two text-level deltas:

- **Phase 2 terminal commands**: use real OpenAI CLI / SDK strings (`pip install openai`, `openai responses create --stream`, `python -c "from openai import OpenAI; ..."`, etc.). Color tokens: `cmd` mint (`openai`, `pip install`), `arg` ink-100 (`responses`, `create`), `flag` amber (`--stream`, `--model`), `kw` lavender (`create`, `chat`, `audio`), `str` ink-80 (string literals).
- **Phase 4 CTA pill values**: avoid Google-style verbs (`DROP`, `DEPLOY`, `PUBLISH`). Prefer OpenAI-friendly: `TRY`, `READ`, `BUILD`, `SHIP`, `OPEN`. CTA value: `CHATGPT`, `SORA`, `CODEX`, `API`, `GPT-5`, `PLATFORM`.

Style rules and 4-block save format are identical to new-google-short.

### 6. Generate TTS + transcript — same as new-google-short.

### 7. Compute phase boundaries — same as new-google-short.

### 7.5. Decide single-slide vs multi-sub-slide per phase — same as new-google-short. The template's `<style>` block ships byte-identical sub-slide CSS (`.pX-stage`, `.pX-slide`, `.is-default-visible`, `.p3-bullets`, `.p2-c-bullets`, `.p4-pills`, `.hero-figure`, `.settings-figure`, `.inline-mono`).

### 8. Edit `videos/<slug>/index.html` (DELTA)

Same 18-step edit list as new-google-short with three substitutions:

- Item 2 (`#root` class) → `theme-quiet` (not `theme-cinematic`) unless Step 4 picked otherwise.
- Item 3 (`#root` inline style for accent) → use `var(--oai-lavender)` / `var(--oai-amber)` / `var(--oai-coral)` instead of `var(--g-red)` / `var(--g-yellow)` / `var(--g-green)`. Default leaves no inline style (mint is the token default).
- Item 8 (Phase 3 chips): keep `data-color="mint"` on all chips by default. **Don't** rotate per-chip colors — that's the Google pattern. The only reason to set a non-mint `data-color` is if Step 4 picked a whole-video override (e.g. all chips `data-color="lavender"` for a Sora-flavored video).

Item 18 (SFX wiring) reference cue map for this template:
- Phase 1 hero headline reveal: `impact-slam` at headline anchor word (volume 0.15)
- Phase 2 first terminal entrance: `scale-slam` (volume 0.15)
- Phase 3 chip 1 entrance only: `spring-pop` (volume 0.11)
- Each phase transition (T1, T2, T3): `cinematic-whoosh` (volume 0.11)
- Phase 4 CTA pill entrance: `pop` (volume 0.10)

The brand-mark swap (spirograph → wordmark) is a single `<img src="...">` edit if Step 4 picked the wordmark.

### 9. Discount-bubble timing — same as new-google-short.

### 10. Lint, 11. Inspect, 12. Preview, 13. YouTube description, 14. Report — all same as new-google-short.

The report template:

```
✅ <Title>
   Slug:        <slug>
   Theme:       <quiet|cinematic|editorial> + <accent>
   Brand mark:  <spirograph|wordmark>
   Light shift: <on|off>
   Dynamous:    <badge|moduleInterstitial|discountBubble|endcard> on / off
   Render:      npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4
   Length:      <N>s
   Voice:       <voice-id> @ <speed>×
   YouTube:     videos/<slug>/youtube-description.md (paste-ready)
   Preview:     http://localhost:5173
```

## Quality bar checklist

Before declaring done, confirm:

- [ ] `theme-quiet` is the default (or theme was explicitly picked per Step 4)
- [ ] Mint is the only accent on screen (or a whole-video aux-tint override was applied per Step 4)
- [ ] Chip grid is single-accent — no per-chip color rotation
- [ ] Terminal rim is monochrome (single mint hairline), not four-color
- [ ] ChatGPT spirograph or OpenAI wordmark is correctly picked for the sub-brand
- [ ] Rail labels read INTRO → BUILD → SIGNAL → SHIFT → CTA (not the Google labels)
- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes validate videos/<slug>` → no AA contrast failures on body text (the `#p1-eyebrow` transition-overlap warning at t=2.4s is a known baseline shared with the Google template; ignore)
- [ ] `npx hyperframes inspect videos/<slug>` → 0 overflow

## Don'ts (OpenAI-specific)

1. **Don't rotate four colors across chips.** That's the Google pattern. OpenAI is single-accent. Either every chip mint, or every chip lavender (whole-video Sora override) — never a mix.
2. **Don't use the cinematic theme as default.** `theme-quiet` is the OpenAI register. `theme-cinematic` is opt-in for launch moments only.
3. **Don't use the OpenAI wordmark at 110px.** It's a wider asset than the spirograph and will dominate the top safe zone. Drop to 80-90px when swapping.
4. **Don't use pure black or pure white.** Off-black `#0A0A0A` + off-white `#ECECEC` is the brand register. Pure values read as "stock template".
5. **Don't import shared/lib blocks that hard-code Google-style four-color rims.** Check the recipe before installing. If a block draws a four-color top stroke, either pass it a token override or skip it.
6. **Don't write Sora-flavored hero copy with mint accent.** If the video is Sora-specific, swap `--accent` to `--oai-lavender` for the whole composition (Step 4). Mismatched accent + content reads as "OpenAI used the wrong template".
