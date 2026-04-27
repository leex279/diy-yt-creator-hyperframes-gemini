# new-anthropic-short — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames Short in the Anthropic dark-stage aesthetic. Zero manual steps; ends at preview, never renders.

## Inputs

User provides ONE of:

- A **topic / prompt** (e.g. _"Anthropic just shipped Claude Code Skills"_) — agent drafts the full script
- A **title + key facts** (e.g. _"Opus 4.7 launch — 1M context, 47% on SWE-bench, $5/M tokens"_) — agent uses the facts verbatim, drafts the framing
- A **pre-written `script.txt`** — agent skips drafting (jump to step 5)

If the topic has no real source data and would require fabricated stats/dates, **stop and ask the user for a source URL** before proceeding. Never invent numbers.

## Outputs

A previewable HyperFrames project at `videos/<slug>/` with:

- `script.txt` — narration script
- `audio/narration.wav` — Kokoro TTS narration
- `transcript.json` — word-level timestamps
- `index.html` — composition filled with real content, transitions sync'd to spoken-word frames
- Preview studio open in the browser at the URL printed by `hyperframes preview`

The user runs render themselves: `npx hyperframes render videos/<slug> -o videos/<slug>/out/short.mp4`.

---

## Steps

### 1. Confirm slug + title

Derive a kebab-case slug from the topic (3-6 words, no stopwords). Examples:

- "Anthropic just shipped Claude Code Skills" → `claude-code-skills-launch`
- "Opus 4.7 ships with 1M context" → `opus-47-1m-context`
- "Why GPT-5 lost the SWE-bench crown" → `gpt5-swe-bench-loss`

Confirm with the user in one line: _"Spawning `videos/claude-code-skills-launch/` — title 'Claude Code Skills Launch'. Proceed?"_ Skip confirmation if the user already gave you both.

### 2. Copy the template

```bash
cp -r templates/shorts/anthropic videos/<slug>
```

PowerShell: `Copy-Item -Recurse templates/shorts/anthropic videos/<slug>`

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `audio/`, `assets/`, `compositions/` should all exist.

### 3. Update meta.json

Replace the placeholders:

```json
{
  "id": "<slug>",
  "name": "<Title Case Name>"
}
```

### 4. Draft the script (skip if user provided one)

Map narration to the four phase archetypes the template ships:

| Phase | Duration target | What to write |
|---|---|---|
| **1 — Hero hook** | 5-7s | Mono overline (2-3 words, ALL CAPS): the section label. Secondary line (5-9 words): the setup. ONE slam word (1-2 syllables, ALL CAPS): the emotional payoff. Caption pill (4-8 words): the receipt. |
| **2 — Stat row** | 5-7s | Mono overline. Headline (5-9 words). Two huge numbers with 2-3 word labels each. Numbers MUST be real. |
| **3 — Timeline** | 6-8s | Mono overline. 3 dated cards: date (e.g. "Mar 4"), title (3-5 words), sub (3-6 words). Real dates only. |
| **4 — CTA** | 4-6s | Mono overline. URL pill (real, working URL). Subscribe pill ("Subscribe" or short variant). |

**Style rules for narration text:**

- Short sentences. Kokoro TTS reads commas as breaths and periods as full pauses.
- Never use semicolons or em-dashes in script.txt — Kokoro stumbles. Use periods.
- Numbers: write digits, not words ("3 bugs", not "three bugs") — matches the visual stat pills.
- Total target: 24-45s of narration. Going past 60s is fine for content-dense topics.

Save to `videos/<slug>/script.txt`. Use this exact format (one phase per blank-line block):

```
[phase 1 narration]

[phase 2 narration]

[phase 3 narration]

[phase 4 narration]
```

The blank lines are NOT spoken; they help you map narration to phases when you read the transcript back later.

### 5. Generate TTS

```bash
npx hyperframes tts videos/<slug>/script.txt \
  -o videos/<slug>/audio/narration.wav \
  -v af_heart \
  -s 1.0
```

**Voice picker** (default: `af_heart` — warm female):

| Voice | Use when |
|---|---|
| `af_heart` | Default. Warm, confident female. Works for almost everything. |
| `af_nova` | Brighter, younger female. Good for product launches. |
| `am_adam` | Confident American male. Good for news / postmortems. |
| `bm_george` | British male. Good for documentary / explainer. |
| `am_michael` | Deeper American male. Good for warning / heavy topics. |

Speed: keep at `1.0` for the first pass. If the script feels rushed at preview, regenerate at `0.95`. Never go above `1.15` — Kokoro distorts.

If TTS fails or the model isn't downloaded, the CLI prints a download prompt — accept it, then re-run.

### 6. Transcribe for word-level sync

```bash
npx hyperframes transcribe videos/<slug>/audio/narration.wav -d videos/<slug>
```

This writes `videos/<slug>/transcript.json` with the shape `[{ word, start, end, ... }, ...]` (seconds).

Default model is `small.en` — fine for 24-60s clips. If accuracy looks off on technical jargon, re-run with `-m medium.en`.

### 7. Compute phase boundaries

Read `transcript.json` and identify, in seconds:

- `phase1_end` — `end` time of the last word of the phase 1 narration block
- `phase2_end` — same for phase 2
- `phase3_end` — same for phase 3
- `phase4_end` — `end` time of the last word in the file
- `total_duration` = `phase4_end + 1.5` (1.5s tail for reading the CTA before loop)

Then compute the GSAP timeline anchors:

```
T1 = phase1_end - 0.2     // start phase1→phase2 transition 0.2s before last word ends
T2 = phase2_end - 0.2
T3 = phase3_end - 0.2

P2 = T1 + 0.4             // phase2 entrance anchor (after crossfade settles)
P3 = T2 + 0.4
P4 = T3 + 0.4
```

Also identify the timestamp of the **slam word** in phase 1 — the single ALL-CAPS payoff word. That's the new value for the inline-shake offsets in the template (the four `tl.to("#p1-hero", { x: ... })` lines, currently at 1.55-1.70).

```
slam_t = transcript[<slam-word-index>].start
shake_offsets = [slam_t, slam_t + 0.05, slam_t + 0.10, slam_t + 0.15]
```

### 8. Edit `videos/<slug>/index.html`

Always invoke the `/hyperframes` skill before this step — it has the framework-specific rules.

Edit in this exact order (one Edit per change):

1. **`<title>`** in `<head>` → the video title
2. **`<div id="root">`** `data-duration` → `total_duration` (rounded to 0.1s)
3. **`#top-banner-logo`** `src` → **always reference `assets/<file>` (a copy inside the project)**, never `../../shared/logos/<file>`. The studio's preview server can only serve files inside the project directory, so external paths render as a broken 21px placeholder even though `hyperframes render` handles them. Copy the logo first: `cp shared/logos/anthropic-logo-light.svg videos/<slug>/assets/`, then set `src="assets/anthropic-logo-light.svg"`. For other brands, copy the relevant file from `shared/logos/` into the project's `assets/` (see "Real logos" below). NEVER use a styled text div when a real logo exists in `shared/logos/`.
4. **Phase 1**: `#p1-overline`, `#p1-pre`, `#p1-hero` (the slam word), `#p1-caption`
5. **Phase 2**: `#p2-overline`, `#p2-headline`, both `.stat-pill` blocks (`.stat-num` and `.stat-label`)
6. **Phase 3**: `#p3-overline`, all three `.tl-card` blocks (`.tl-date`, `.tl-title`, `.tl-sub`). Rotate accent classes (`orange` → `purple` → `blue`) so no two adjacent cards share an accent. If the user's data needs `green`, swap that in — but only one accent per card.
7. **Phase 4**: `#p4-overline`, `#p4-url` (real URL), `#p4-subscribe` (usually leave as "Subscribe")
8. **Transition timestamps**: replace `const T1 = 5.6;`, `const T2 = 11.6;`, `const T3 = 17.6;` with computed values
9. **Phase anchors**: replace `const P2 = 6.4;`, `const P3 = 12.4;`, `const P4 = 18.4;` with computed values
10. **Progress bar tween**: change `duration: 24` (in the `#progress-fill` `fromTo`) to the new `total_duration`
11. **Ambient breath**: change `duration: 12` (yoyo half-period) to `total_duration / 2`
12. **Slam shake**: replace the four `tl.to("#p1-hero", { x: ...}, <time>)` offsets with `shake_offsets`
13. **Audio element**: insert just before `</div>` (the closing tag of `#root`), at the same indent level as `<div id="phase4">`:

```html
  <audio id="narration"
         src="audio/narration.wav"
         data-start="0"
         data-duration="<phase4_end>"
         data-track-index="2"
         data-volume="1"></audio>
```

### 8.5. Lib pick (optional but recommended)

The repo ships a shared visual library at [`shared/lib/`](../../../shared/lib/). It has reusable cards, components, effects, and named visual styles — extracted from this very template. Before treating any phase as "fully custom", check whether a lib entry already does what you need.

1. Read [`shared/lib/MANIFEST.md`](../../../shared/lib/MANIFEST.md) — the catalog of every entry, with description + tags.
2. Read [`shared/lib/visual-styles/anthropic-dark.md`](../../../shared/lib/visual-styles/anthropic-dark.md) — the named-style fragment that ALSO maps which lib entries fit this aesthetic.
3. For each lib entry you want to reuse:
   - **Block** (sub-composition): copy `shared/lib/blocks/<name>/block.html` into `videos/<slug>/compositions/<name>.html`. Wire it in `index.html` per the entry's `recipe.md`.
   - **Component** (paste-in snippet): read `shared/lib/components/<name>/component.html`. Merge its HTML / CSS / JS sections into the host `index.html` per the comments at the top of the file.
   - **Effect** (GSAP recipe): read `shared/lib/effects/<name>.js`. Paste the function body into the host `<script>` (above the timeline construction) and call it from the timeline.
   - **Tokens**: copy `shared/lib/tokens/<name>.css` into `videos/<slug>/tokens/<name>.css` and add a `<link rel="stylesheet" href="tokens/<name>.css">` in `<head>`.

**Never reference `shared/lib/` paths from `data-composition-src`, `<img src>`, `<audio src>`, `<video src>`, `<link href>`, or `<script src>` at runtime.** The HyperFrames bundler / preview server (`isSafePath` / `safePath` in `@hyperframes/core`) silently rejects paths outside the project directory. Always copy the file into `videos/<slug>/` first; reference it from the local copy.

This step is optional because the spawned template already inlines the equivalents — but as you customize, lib entries are a way to swap one piece without divergence. They're also the canonical source for any new template you might author later.

### 9. Lint

```bash
npx hyperframes lint videos/<slug>
```

Must report `0 errors`. Fix any errors before continuing:

| Error | Likely cause | Fix |
|---|---|---|
| `audio_src_not_found` | `narration.wav` missing or path wrong | Check `videos/<slug>/audio/narration.wav` exists; case-sensitive paths |
| `overlapping_gsap_tweens` | Two tweens hit the same prop at the same time | Add `overwrite: "auto"` to the later tween, or shift its start |
| `duplicate_media_discovery_risk` | Stray `<img src=...>` text in an HTML comment | Rephrase the comment |
| `missing_track_index` | Element has timing attrs but no `data-track-index` | Add it (use 2 for narration, 3+ for SFX) |

Warnings are advisory — read them but don't block on them.

### 10. Inspect for layout overflow

```bash
npx hyperframes inspect videos/<slug>
```

Common overflows on this template:

- **Hero slam word too wide** — the 240px font + the chosen word exceeds 1080px - 120px padding. Either shorten the word (synonym) or drop `#p1-hero` font-size to 200px.
- **Stat pill labels wrap onto 3 lines** — labels >18 chars overflow the 440px pill. Shorten the label.
- **Timeline card title overflows** — 40px font + long title overflows the card's 940px width minus the date chip (160px) and index badge (56px). Shorten or drop title to 36px.

Fix overflow at the CSS or content level, then re-run `inspect` until clean.

### 11. Open preview (final step — never render)

Run in background so the studio stays open while you report:

```bash
npx hyperframes preview videos/<slug>
```

Capture the URL it prints (typically `http://localhost:5173`).

### 12. Report to the user

One concise message containing:

- **Slug + path**: `videos/<slug>/`
- **Total duration**: `XX.Xs`
- **Voice**: `af_heart` (or whichever was used)
- **Preview URL**: `http://localhost:5173`
- **Render command** (do NOT run it): `npx hyperframes render videos/<slug> -o videos/<slug>/out/short.mp4`
- **Any inspect findings** that needed manual content tradeoffs (e.g. "shortened slam word from BREAKTHROUGH to MAJOR for fit")

That's it. Stop. Wait for user to iterate or trigger render manually.

---

## Quality bar — required before reporting done

- [ ] `npx hyperframes lint videos/<slug>` → 0 errors
- [ ] `npx hyperframes inspect videos/<slug>` → no overflow on hero word, stat pills, or timeline cards
- [ ] All four phases have real content (no leftover template placeholders: "DUMBER?", "anthropic.com/postmortem", "Mar 4 / Mar 26 / Apr 16", "3 separate bugs / 6 weeks stacked")
- [ ] Phase transition timestamps computed from transcript, NOT left at template defaults
- [ ] Audio element wired with correct `data-duration`
- [ ] Preview URL is reachable (the `hyperframes preview` background command is still running)

If any item fails, fix it before reporting. Don't claim success on a half-built composition.

---

## Real logos — always use them when they exist

The repo ships a shared logo library at `shared/logos/` (84 PNG/SVG brand wordmarks and icons — Anthropic, Claude, Claude Code, OpenAI, GitHub, Canva, Asana, Slack, Discord, AWS, Cloudflare, Stripe, Vercel, and many more). **Never use styled text or pseudo-logos when a real one exists.**

**Important: copy logos into the project's `assets/`, do NOT reference `shared/logos/` directly.** The studio's preview server only serves files inside the project directory; an `../../shared/logos/...` path 404s in the studio (it'll work in `hyperframes render` but the preview shows a broken 21px placeholder, which silently fails lint).

**Workflow:**

```bash
# Copy each logo you need into the project's assets folder
cp shared/logos/anthropic-logo-light.svg videos/<slug>/assets/
cp shared/logos/canva-logo.png            videos/<slug>/assets/   # if used in phase 3, etc.
```

**Common picks** (`src` value after copying):

| Where | Anthropic-style video | Other brands |
|---|---|---|
| Top banner (`#top-banner-logo` `src`) | `assets/anthropic-logo-light.svg` | Match the video's host brand (e.g. `assets/claude-logo-light.svg`, `assets/claude-code-logo-light.svg`) |
| Per-app step in phase 3 (if applicable) | `assets/<app>-logo.png` (e.g. `assets/canva-logo.png`, `assets/asana-logo.png`, `assets/slack-logo.svg`) | Same |

**Workflow inside step 8:**

1. Before editing phase 3 timeline cards, check `shared/logos/` for each named app/brand: `ls shared/logos | grep -i <app>`.
2. If a logo exists, **copy it into the project's `assets/`** and render it as `<img src="assets/<file>" alt="<App>">` inside the card's `.tl-app` slot (or replace the entire app text with the logo). Style with `height: 36-44px; width: auto; vertical-align: middle`.
3. If a logo does NOT exist, do NOT fabricate one. Either:
   - Ask the user for the logo file (preferred), OR
   - Fall back to the styled mono-text app name (current default in the template), OR
   - Pick a different app already in `shared/logos/` IF the script-content allows substitution without losing factual accuracy.

**Light vs dark variants**: this template is dark-stage (`--bg: #0B0F18`). Always pick the `*-light.svg` or `*-light.png` variant when available — it has white/cream marks that contrast on dark. Avoid `*-dark` variants on this template (they'll be near-invisible).

**Never commit a video that ships with the placeholder text logo (`CLAUDE` styled div) when a real logo exists.** Lint will not catch this — it's a content rule.

## Don'ts

- Never auto-render — user explicitly always triggers render manually.
- Never fabricate stats, dates, URLs, or quotes. Ask for source if missing.
- Never use a styled-text pseudo-logo when a real one exists in `shared/logos/`. See "Real logos" above.
- Never modify `templates/shorts/anthropic/` — only the copy under `videos/<slug>/`.
- Never reference `shared/lib/` paths from `data-composition-src`, `<img src>`, `<audio src>`, `<video src>`, `<link href>`, or `<script src>` at runtime — the HyperFrames bundler silently rejects paths outside the project directory. Always copy the file into `videos/<slug>/` first.
- Never use `Math.random()` / `Date.now()` in the generated composition (HyperFrames is deterministic).
- Never write `<br>` in content text — use `max-width` for natural wrapping (HyperFrames `/hyperframes` skill rule).
- Never animate `visibility` or `display` — use opacity (HyperFrames rule).
- Never skip the `/hyperframes` skill before editing the composition HTML.
- Never run multiple `new-anthropic-short` invocations in parallel against the same slug.
