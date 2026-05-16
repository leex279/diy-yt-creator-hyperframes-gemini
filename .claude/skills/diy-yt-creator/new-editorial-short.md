# new-editorial-short — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames Short in the **editorial-light, single-accent** aesthetic — warm cream paper, Source Serif 4 italic, single terracotta accent. Zero manual steps; ends at preview, never renders.

> **Use this playbook when** the topic deserves the mood of a long-form publication — deep-explainer overviews of a spec/standard/open protocol, essay-style "what is X and why" deep-dives, cross-tool comparisons, companion videos for long-form on the same topic. For brand-neutral 5-accent rotation use [`new-standard-short`](./new-standard-short.md). For Anthropic / Claude product launches use [`new-anthropic-short`](./new-anthropic-short.md).

> **Architecture note:** This template uses **sub-compositions** (not phase mutex). 15 scene archetypes live as separate files under `videos/<slug>/compositions/scene-*.html`, each with its own paused timeline. The root `index.html` only orchestrates ambient + chrome + scene crossfades + shape reposition.

> **For research + scriptwriting first**: see `/diy-yt-creator:full-auto`. That orchestrator runs phases 0-3.5 and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A.

This is a **delta-from-`new-standard-short`** playbook. Every step that's identical to standard is referenced rather than duplicated. The editorial-template differences are called out under "Deltas vs standard" inline.

## Inputs / Outputs

Same as [`new-standard-short`](./new-standard-short.md#inputs--outputs).

## Steps

### 1. Confirm slug + title

Same as standard. Editorial slugs lean to topic-specific kebab-case (`agent-skills-standard-short`, `mcp-protocol-explained-short`, `llms-txt-explained-short`).

### 2. Copy the template

```bash
cp -r templates/shorts/editorial videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/shorts/editorial videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `tokens/editorial-short.css`, `audio/`, `assets/shapes/`, `assets/sfx/`, `compositions/` should all exist.

### 3. Update meta.json

Same as standard.

### 3.5. Ask: Add Dynamous promotion?

Same as [`new-anthropic-short` step 3.5](./new-anthropic-short.md#35-ask-add-dynamous-promotion).

### 4. Draft the script

Same Branch A / Branch B logic as standard. **Delta:** map narration to whichever subset of the **15 editorial scene archetypes** fits the script. The bare template ships all 15 (210s default total); per video, drop scenes you don't need and stretch others. Typical editorial-mode mappings:

| Scene archetype | File | Default duration | Editorial use |
|---|---|---|---|
| **title** | `compositions/scene-title.html` | 13.9s | Italic accent on the central word in the headline |
| **stat** | `compositions/scene-stat.html` | 12.9s | Single hero number + serif italic suffix (no rainbow accents) |
| **chart** | `compositions/scene-chart.html` | 13.9s | Use SPARINGLY — chart implies dashboard, not editorial |
| **counter-grid** | `compositions/scene-counter-grid.html` | 13.2s | Same caution as chart |
| **typewriter** | `compositions/scene-typewriter.html` | 13.7s | Strong fit — type-on with italic accent + small visual |
| **code-block** | `compositions/scene-code-block.html` | 13.4s | For specs/standards/protocols — show the actual artifact |
| **quote** | `compositions/scene-quote.html` | 13.4s | Core editorial archetype — italic body + ink rule + mono attribution |
| **bullets** | `compositions/scene-bullets.html` | 13.2s | "Three things worth knowing" — central editorial pattern |
| **process-flow** | `compositions/scene-process-flow.html` | 12.7s | For specs — discovery / activation / execution etc. |
| **compare** | `compositions/scene-compare.html` | 13.4s | Before/after, old way vs new way |
| **timeline** | `compositions/scene-timeline.html` | 13.4s | Dated milestones (origins, releases) |
| **marker** | `compositions/scene-marker.html` | 14.4s | Marker-sweep highlight on the central claim |
| **image-card** | `compositions/scene-image-card.html` | 13.2s | Real screenshot of the article / standard / repo |
| **badges** | `compositions/scene-badges.html` | 14.4s | Use SPARINGLY — palette badges fight editorial restraint |
| **cta** | `compositions/scene-cta.html` | 20.9s | URL pill + subscribe + closing hold |

All other style rules (short sentences, no semicolons, digits not words, ~150-180s narration target for a 3-min editorial Short) — same as standard.

**Scene-text style notes specific to this template:**

- Source Serif 4 headlines at 96-132px hold ~10-12 chars per line. Aim for short emphatic phrasing.
- Italic accents inside serif headlines (`<span class="em">word</span>`, `<span class="word accent">word</span>`) work best on 1-2 emphasis words per beat, NEVER more.
- Marker sweep targets a SINGLE word — pick the most important word in the headline.
- The top-banner mono wordmark is a chapter heading (centered, no card pill). Pick a label that survives across all scenes: the standard / protocol / spec name itself usually works (e.g. `AGENT SKILLS`, `MCP`, `LLMS.TXT`).
- The bottom-right `#source-url` chip persists across all scenes. Use it to pin the canonical URL (the spec page, the GitHub repo, the article). Pure aesthetic flourish OR functional reference, your call — but always one or the other, never empty placeholder.

### 4.5. (Optional) Ground the script in real source content

Same as standard. Editorial Shorts are typically **source-grounded** (overview of an existing spec / article / standard), so this step is usually NOT optional — pull `tmp/source.md` from `llms.txt` or the canonical URL before drafting Phase 2.

### 5. Generate TTS + transcript

Same as standard:

```bash
python scripts/elevenlabs-tts.py videos/<slug> --shorts
```

### 6. Transcript verification

Same as standard.

### 7. Compute phase boundaries

Same anchor formulas as standard. Editorial pacing tends to LONGER per-scene than standard — typical 15-25s per scene at 150-180 WPM. Tail-holds inside each scene should be longer than for standard (3-5s vs 1-2s) so the editorial breath lands.

### 8. Edit `videos/<slug>/index.html` AND scene files

Always invoke the `/hyperframes` skill before this step. The architecture is sub-composition based.

**A. Root `index.html` — orchestrator only:**

1. **`<title>`** → the video title
2. **`<div id="root">`** `data-duration` → `total_duration`
3. **Top banner** — replace `<span id="top-banner-wordmark">YOUR TOPIC</span>` text. Editorial uses centered mono wordmark + thin rule (no card pill). For a brand logo, replace the entire `<div id="top-banner">…</div>` block with a centered `<img>`. Use **dark variants** of brand logos on the warm cream canvas.
4. **Source URL chip** — update or remove the `<div id="source-url">…</div>` block. If keeping, update both `.source-url-label` text (UPPERCASE category) and `.source-url-text` URL.
5. **Scene wrapper list** — drop scenes you don't need. Keep wrappers in display order.
6. **`tl.addLabel(...)` calls + `repositionShapesPerScene(...)` start-time array + `crossfadeScenes(...)` chain** — update all three to match the kept scenes and their new `data-start` values.
7. **`TOTAL_DURATION`** — update to match `total_duration`.
8. **Narration `<audio>`** — wire under `<div id="source-url">` with `src="audio/narration.wav"`, `data-start="0"`, `data-duration="<total_duration>"`, `data-track-index="2"`, `data-volume="1"`.
9. **SFX `<audio>` elements** — whoosh on each scene transition (track 3, `data-duration="1.5"`, `data-volume="0.11"`). Per `.claude/rules/audio-design.md`, whoosh fires at the visual transition moment, NOT 0.4s before. The shape-reposition tween starts at `sceneT - 0.4` but the whoosh peaks at the visual swap. Use `data-start="<sceneT>"`.
10. **Source-URL fade-in** — `tl.to("#source-url", { opacity: 1, duration: 0.6, ease: "power2.out" }, 0.6)` already in template — adjust the `0.6` start time if you want it to land later.

**B. Per-scene `compositions/scene-*.html` — content + timing:**

Same as standard. Each kept scene's content needs to be replaced with the video's actual content. The `window.__timelines["scene-<name>"]` timeline registration MUST stay — it's what the studio uses to drive each scene's animation.

**Editorial deltas inside scenes:**

- Use `<em>` / `<span class="em">` / `<span class="word accent">` to put ONE word in italic terracotta per beat. Never more than one per scene.
- `accent-warm` (= `accent-1` = terracotta) is the default lead.
- `accent-deep` (= warm brown, NOT indigo) is the secondary chrome. Use sparingly.
- `accent-sage`/`accent-gold`/`accent-rose` exist via the standard-alias layer but you should treat them as rarely-used. If a scene needs 4+ accents you've drifted to standard territory — reconsider.
- Keep `--shadow-warm` use light. The editorial card is meant to be nearly flat.

### 9. Validate the build

Same as standard:

```bash
npx hyperframes lint     videos/<slug>
npx hyperframes validate videos/<slug>
npx hyperframes inspect  videos/<slug>
```

Editorial videos may inherit 3 pre-existing contrast warnings from the standard scene files (icon "A"/"B" glyphs in scene-bullets at t=105s; cta-url in scene-cta at t=189s). These are baseline-acceptable.

### 10. Preview

```bash
npx hyperframes preview videos/<slug>
```

Per `sub-composition-wiring.md`, manually confirm the duration display matches `total_duration` — lint won't catch a silent mount mismatch.

### 11. Final-frame thumbnail audit

Same as standard. Editorial Shorts especially must close on a thumbnail-grade final frame because the editorial mood is slower → the loop benefits hardest from a strong terminal still.

### 11.5. Engagement CTA self-check

Same as standard. Editorial closes on a debate-sparking binary question per `.claude/rules/engagement-cta.md`.

### 11.7. YouTube description

Same as standard.

### 12. End at preview

Same as standard. Never auto-render.

## Quality bar

- **Editorial restraint maintained**: no scene paints 3+ accents simultaneously. The lead is always `--accent-1` (terracotta).
- **Single italic emphasis per beat**: one word in italic terracotta per spoken sentence, never two.
- **Source Serif 4 only**: fallback chain doesn't drift to sans.
- **Tail-holds 3-5s**: per scene before crossfade, so the editorial breath lands.
- **Source URL chip is meaningful**: pinned to a canonical URL that survives the whole video.
- **First AND last frames are thumbnail-grade**: per `.claude/rules/shorts-thumbnail-frames.md`.
- **Engagement CTA in three places**: spoken (last 3-5s) + on-screen (`#cta-question`) + YouTube description final paragraph. All three agree on wording.
- **Heteronym audit completed**: `live/lead/read/close` checked against `.claude/rules/tts-pronunciation.md` before TTS.

## Don'ts

- **Don't restore the 5-accent rotation.** If the topic genuinely wants rainbow accents, switch to `templates/shorts/standard/`. The editorial template's whole point is restraint.
- **Don't ship a chart or counter-grid scene by reflex.** Editorial scenes lean to quote / bullets / typewriter / marker / code-block / image-card. Charts and grids fight the mood.
- **Don't substitute Playfair Display.** Source Serif 4 is the editorial voice; Playfair Display gives a magazine-cover feel that fights restraint.
- **Don't drop the top-banner rule.** The thin terracotta rule under the mono wordmark is what makes it read as a chapter heading rather than a UI element.
- **Don't add box-shadow to cards.** Editorial cards are flat. Depth comes from contrast against warm cream, not drop shadows.
