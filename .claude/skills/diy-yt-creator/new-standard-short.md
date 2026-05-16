# new-standard-short — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames Short in the **brand-neutral warm-paper editorial** aesthetic. Zero manual steps; ends at preview, never renders.

> **Use this playbook when** the topic isn't anchored to a specific brand (general explainers, how-tos, news, opinion, comparisons, tips) and benefits from a warm, editorial feel. For Anthropic / Claude product launches use [`new-anthropic-short`](./new-anthropic-short.md). For Archon workflow showcases use [`new-archon-short`](./new-archon-short.md).

> **Architecture note (2026-04-29 rework):** This template uses **sub-compositions** (not phase mutex). Nine scene archetypes live as separate files under `videos/<slug>/compositions/scene-*.html`, each with its own paused timeline. The root `index.html` only orchestrates ambient + chrome + scene crossfades. The step-8 instructions below have been adapted to this architecture; old phase-mutex references have been removed.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 (research → plan → script → critique → fact-check → retention strategy) and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A.

This is a **delta-from-`new-anthropic-short`** playbook. Every step that's identical to anthropic is referenced rather than duplicated. The standard-template differences are called out under "Deltas vs anthropic" inline.

## Inputs / Outputs

Same as [`new-anthropic-short`](./new-anthropic-short.md#inputs).

## Steps

### 1. Confirm slug + title

Same as anthropic. Examples:

- "How to ship a side project in 5 hours" → `ship-side-project-5-hours`
- "Why most YouTube hooks fail" → `youtube-hooks-fail`
- "Three lessons from building 10 LLM apps" → `three-lessons-llm-apps`

### 2. Copy the template

```bash
cp -r templates/shorts/standard videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/shorts/standard videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `tokens/standard-short.css`, `audio/`, `assets/shapes/`, `assets/sfx/`, `compositions/` should all exist.

### 3. Update meta.json

Same as anthropic.

### 3.5. Ask: Add Dynamous promotion?

Same as [`new-anthropic-short` step 3.5](./new-anthropic-short.md#35-ask-add-dynamous-promotion).

### 4. Draft the script

Same Branch A / Branch B logic as anthropic. **Delta:** map narration to whichever subset of the **nine scene archetypes** fits the script. The bare template ships all nine (~68s default total); per video, drop scenes you don't need and stretch others. Typical mappings:

| Scene archetype | File | Default duration | Use for |
|---|---|---|---|
| **title** | `compositions/scene-title.html` | 7s | Editorial intro / chapter card with serif word reveal |
| **stat** | `compositions/scene-stat.html` | 7s | One huge counter + serif italic suffix |
| **counter-grid** | `compositions/scene-counter-grid.html` | 8s | Three parallel counters (dashboard feel) |
| **quote** | `compositions/scene-quote.html` | 8s | Pull-quote with italic body + attribution |
| **bullets** | `compositions/scene-bullets.html` | 8s | Three icon+text rows with circular badges |
| **compare** | `compositions/scene-compare.html` | 8s | Before (line-through) vs After (terracotta) |
| **marker** | `compositions/scene-marker.html` | 8s | Headline with marker-sweep highlight on key word |
| **badges** | `compositions/scene-badges.html` | 7s | 2x3 pill grid showcasing the 5-accent palette |
| **cta** | `compositions/scene-cta.html` | 7s | URL pill + subscribe button |

All other style rules (short sentences, no semicolons, digits not words, ~90s narration target) — same as anthropic.

**Scene-text style notes specific to this template:**

- The serif headlines (Playfair Display 132px) hold ~11 chars per line. Aim for short emphatic words.
- Italic accents inside serif headlines (`<span class="em">word</span>` in scene-bullets/badges, `<span class="word accent">word</span>` in scene-title) work best on 8-12 char words.
- Marker sweep targets a SINGLE word — pick the most important word in the headline.

### 4.5. (Optional) Ground the script in real source content

Same as anthropic.

### 5. Generate TTS + transcript

Same as anthropic:

```bash
python scripts/elevenlabs-tts.py videos/<slug> --shorts
```

### 6. Transcript verification

Same as anthropic.

### 7. Compute phase boundaries

Same anchor formulas as anthropic (T1, T2, T3, P2, P3, P4, slam_t, shake_offsets).

### 8. Edit `videos/<slug>/index.html` AND scene files

Always invoke the `/hyperframes` skill before this step. The architecture is sub-composition based, so editing happens in TWO places:

**A. Root `index.html` — orchestrator only:**

1. **`<title>`** in `<head>` → the video title
2. **`<div id="root">`** `data-duration` → `total_duration` (rounded to 0.1s)
3. **Top banner** — the standard template ships with a styled wordmark pill (`<div id="top-banner-text">…</div>`), NOT an `<img>`. Operator decision per video:
   - **No brand**: tweak the placeholder text inside `<span>Your Topic</span>` to a 1-2 word topic label.
   - **Real brand logo**: replace the entire `<div id="top-banner-text">…</div>` block with an `<img>`. First copy the logo: `cp shared/logos/<logo-file> videos/<slug>/assets/`. The warm cream canvas is light, so use **dark variants** of brand logos (`*-dark.svg` or default if there's only one) — light logos will be near-invisible.
4. **Scene wrapper list** — drop scenes you don't need by removing their `<div class="scene-wrapper">` block. Keep the wrappers in display order.
5. **`data-start`** on each scene wrapper — set to the absolute time (in seconds) the scene begins in the root timeline. Compute from your transcript using the same formulas as anthropic (use word `start` times for spoken-word landmarks).
6. **`TOTAL_DURATION`** in the `<script>` tag → match `data-duration` from step 2.
7. **`tl.addLabel(...)`** chain in the `<script>` — labels must match the `data-start` values from step 5. Labels drive the crossfade chain.
8. **`crossfadeScenes(...)`** chain — if you removed a scene, remove the two crossfades pointing at it and add a single direct crossfade between its neighbors.

**B. Per-scene `compositions/scene-*.html` files — content + per-scene timeline:**

For each scene you're using, edit only the content inside its `<template>` and tune its internal timeline if the entrance pacing needs to change:

- **scene-title**: `#title-kicker`, `#title-headline` (3 word spans, middle one is `.accent`), `#title-byline`. Keep word count low — Playfair 132px wraps ~11 chars per line.
- **scene-stat**: `#stat-label`, `#stat-num` (counter target — set the JS `target` constant to your number), `#stat-suffix`, `#stat-caption`. Numbers > 99 may overflow the 240px font; drop to 200px if so.
- **scene-counter-grid**: 3 rows, each with its own counter target (`c1.v: <target>` etc.) and label. Target values are integers; non-integer endpoints will display rounded.
- **scene-quote**: `#quote-body` (italic body, wrap key word in `<span class="em">`), `#quote-attrib`. Attribution starts with em-dash.
- **scene-bullets**: `#bullets-header` (italic accent in `<span class="em">`), 3 `.row` blocks (`.icon` letter/symbol + `.title` + `.sub`). Icons use single chars (A/B/C or symbols).
- **scene-compare**: `#compare-header`, before card (`.claim` line-through), after card (`.claim` accented), `.support` italic line under each.
- **scene-marker**: `#marker-pretitle`, `#marker-headline` (wrap ONE highlighted word in `<span class="marker-wrap">`), `#marker-subline`. Marker sweep clip-path animates the band behind the word.
- **scene-badges**: `#badges-header` (italic em), 6 pill chips with rotating accents (`.warm` / `.deep` / `.sage` / `.gold` / `.rose` / `.ink`).
- **scene-cta**: `#cta-kicker`, `#cta-lede`, `#cta-url` (real URL — terracotta pill is wide enough for 18-22 chars at default 56px), `#cta-subscribe`.

**C. Audio (after content is wired):**

9. **Insert `<audio id="narration">`** just before `</div>` of `#root` in `index.html`:

    ```html
      <audio id="narration"
             class="clip"
             src="audio/narration.wav"
             data-start="0"
             data-duration="<narration_end>"
             data-track-index="2"
             data-volume="1"></audio>
    ```

10. **Wire SFX** from `retention-strategy.md` if it exists. The template ships `sfx-cues.txt` with `impact-slam scale-slam cinematic-whoosh spring-pop pop`:

    ```bash
    bash scripts/sync-video-sfx.sh videos/<slug>
    ```

    All other rules (volume cap 0.25, track-index uniqueness, sonic-logo at 0.45 exception) same as anthropic. The most useful cue here is `cinematic-whoosh` at each scene transition (root timeline label times - 0.4s, matching the crossfade window).

#### Per-video palette swap (optional)

This template's warm palette works for most topics — but if the video has a strong color identity (finance green, fitness orange, tech-blue counterpoint), override the `--accent-*` vars inside `#root`:

```css
#root {
  --accent-warm: #C9A96E;   /* muted gold for a finance video */
  --accent-deep: #2D3142;   /* darker indigo */
  --accent-sage: #87BBA2;
  --accent-gold: #D9A05B;
  --accent-rose: #E5989B;
}
```

For a darker overall feel: change `--bg` to `#2B2A28` and `--text` to `#FBF7EF`. Re-run `npx hyperframes validate` to confirm WCAG contrast.

### 8.5. Lib pick (optional but recommended)

Same as anthropic, but read [`shared/lib/visual-styles/standard-short.md`](../../../shared/lib/visual-styles/standard-short.md) instead of `anthropic-dark.md` for which lib entries fit this aesthetic.

### 9. Lint

```bash
npx hyperframes lint videos/<slug>
```

Must report `0 errors`. Same error catalog as anthropic.

### 10. Inspect for layout overflow

```bash
npx hyperframes inspect videos/<slug>
```

Common overflows on this template:

- **Hero slam word too wide** — the 200px font + the chosen word exceeds 1080px - 120px padding. Either shorten the word (synonym) or drop `#p1-hero` font-size to 180px.
- **Stat pill labels wrap onto 3 lines** — labels >18 chars overflow the 460px pill. Shorten the label.
- **Step card title overflows** — 40px font + long title overflows the card's 940px width minus the number badge (100px). Shorten or drop title to 36px.

Fix overflow at the CSS or content level, then re-run `inspect` until clean.

### 11. Open preview (final step — never render)

```bash
npx hyperframes preview videos/<slug>
```

Run in background. Capture the URL it prints (typically `http://localhost:5173`).

### 11.5. (Optional) QA the rendered preview visually

Same as anthropic.

### 11.7. Generate YouTube description (MANDATORY — never skip)

Same step as in [`new-anthropic-short.md`](./new-anthropic-short.md) §11.7. Follow [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md) end-to-end. LEAN structure: vidIQ keyword research → write `videos/<slug>/youtube-description.md` (SEO hook → Dynamous block in `----` **MANDATORY on every Short** (independent of `dynamousPromotion` in `meta.json`, which only gates ON-SCREEN promotion) → Resources: → Hostinger affiliate block in `----` MANDATORY → engagement question → 15-25 hashtags) → validate every URL with `WebFetch`. **Shorts skip the Chapters section entirely. NO Key Changes / Key Concepts / Key Stats / "What's in this short" bullet sections — explicitly cut.**

### 12. Report to the user

Same fields as anthropic (including `YouTube description: videos/<slug>/youtube-description.md`), plus:

- **Template**: `standard` (so the user knows which aesthetic is in play).

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow on hero word, stat pills, or step cards
- [ ] All four phases have real content (no leftover template placeholders: "THIS", "your-url.com", "First, set the scene / Then, show the move / Finally, close the loop", "10x / 5", "Your Topic")
- [ ] Phase transition timestamps computed from transcript, NOT left at template defaults
- [ ] Audio element wired with correct `data-duration`
- [ ] Top banner shows either a real logo (copied to `assets/`) OR a topic-appropriate text wordmark — never the literal placeholder `Your Topic`
- [ ] Preview URL is reachable (the `hyperframes preview` background command is still running)

If any item fails, fix it before reporting.

---

## Real logos — same rules as anthropic

The repo ships a shared logo library at `shared/logos/` (84 PNG/SVG brand wordmarks and icons). **Never use styled text or pseudo-logos when a real one exists for the topic's brand.** All copy/path/light-vs-dark rules from [`new-anthropic-short.md`](./new-anthropic-short.md#real-logos--always-use-them-when-they-exist) apply unchanged.

**Standard-template specific**: when there's NO single brand for the topic (e.g. a generic "How to negotiate a raise" video), the styled wordmark pill (with a topic label) is the *correct* choice — that's what the bare template ships for. Replace the placeholder text inside `<span>Your Topic</span>` with a 1-2 word topic label and you're done.

## Don'ts

All anthropic don'ts apply, plus:

- **Never use dated chips on this template.** If the content needs dated cards (e.g. a postmortem), you're using the wrong template — switch to [`new-anthropic-short`](./new-anthropic-short.md).
- **Never ship a video with the literal placeholder text `Your Topic` in the top banner.** Replace with either a real logo or a topic label.
- **Never override `--accent-1..4` to colors below 4.5:1 contrast on `#0B0F1A`.** Run `npx hyperframes validate` after any palette swap to confirm the WCAG audit still passes.
