---
description: "Phase 1 — HyperFrames-native composition plan (scenes, durations, hooks, retention picks)"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task
---

<objective>
Execute Phase 1 of the HyperFrames pipeline.
Take the content brief from Phase 0 and produce a structured composition plan that drives the rest of the pipeline.

**Goal**: Transform the content brief into a complete plan with scene breakdowns, hook architecture, retention picks, and a `data-start`/`data-duration` budget — all in HyperFrames vocabulary (seconds, sub-compositions, GSAP, `retention-components-hyperframes.md`).

**Input**: `videos/<slug>/research/content-brief.md` (from Phase 0)
**Output**: `videos/<slug>/plan.md`

All retention picks must come from `.claude/references/retention-components-hyperframes.md` — that's the canonical menu of HyperFrames-supported patterns.
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

If invoked as part of the orchestrator, parameters arrive in context. **DO NOT ask questions** — use the provided values:

- **Duration**: from PARAMS.duration (or content brief)
- **Tone**: from PARAMS.tone (or content brief)
- **Template**: from PARAMS.template (default: `shorts/anthropic`)

Proceed autonomously through all steps.
</autonomous-mode>

<process>

### Phase Gate

Read `videos/<slug>/phase-status.md`.
- **Prerequisites**: Verify `0 - Research` is `done`.
  - If not: STOP and report "Phase 0 (Research) has not run. Run `/diy-yt-creator:phase0-research <topic>` first."
- **Re-run check**: If `1 - Plan` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

### Required Skills (read these before planning)

Before drafting the plan, read the SKILL.md of these skills (and the references they cite). They define the framework patterns this plan must respect:

- `/hyperframes` — composition rules, `data-*` semantics, sub-composition wiring, `class="clip"`, `window.__timelines` registration
- `/gsap` — animation patterns, easing, timelines, performance

Both skills are listed in the project's `skills-lock.json` and live under `.agents/skills/`. **Do not skip this step** — without these patterns, the plan will prescribe things HyperFrames cannot render.

If for some reason the Skill tool can't be invoked from inside a slash command in your environment, treat this as a hard prerequisite the user must run before invoking Phase 1, and ask them to run `/hyperframes` and `/gsap` first.

---

## Step 1 — Read Research & Pick Template

### 1A: Read the content brief

Read `videos/<slug>/research/content-brief.md`. Extract:
- Core value proposition
- Pain points
- Key features and proof points
- Messaging hierarchy (Must / Should / Could / Omit)
- Suggested narrative arc
- Suggested scene structure (Agent D's table)
- Hook architecture (cult-hop refs, contrarian angles, mind-blowing stats)
- Visual concepts and demo opportunities
- Screenshot inventory
- Technical terms (TTS pronunciation)

### 1B: Pick the template

The template determines structural constraints (resolution, layout vocabulary, design tokens):

| Template                | Status        | Resolution | Layout vocabulary                                       |
| ----------------------- | ------------- | ---------- | ------------------------------------------------------- |
| `shorts/anthropic`      | Implemented   | 1080×1920  | 4 mutex `inline-phase` divs (Hero/Stat/Timeline/CTA)    |
| `long-form/*`           | NOT YET BUILT | 1920×1080  | (no template — Phase 1 cannot plan into this until built)|

**Default**: `shorts/anthropic` if not specified.

**If the brief asks for long-form**: STOP and report "No long-form template exists yet. See `templates/long-form/README.md` and offer to build one first." Do not invent a long-form plan.

Read the template's `README.md` and `DESIGN.md` to understand:
- Resolution and design tokens (color CSS variables, padding, fonts)
- The layout primitives the template enforces
- Anti-patterns from the template's "What NOT to do" section
- For `shorts/anthropic` specifically: the 4 mutex phase pattern (Hero slam → Stat pill row → Timeline cards → CTA URL slam)

### 1C: Interactive scoping (standalone mode only)

Ask the user (one question at a time) ONLY if not in autonomous mode:
1. **Duration**: 15s / 30s / 45s / 60s / 90s / 3min?
2. **Tone**: tech-influencer-edgy / professional-corporate / friendly-educational / dramatic-cinematic?
3. **Template**: `shorts/anthropic` (default) — confirm or pick another implemented template

In autonomous mode, use the brief's `Duration` / `Tone` / `Template` fields or sensible defaults.

---

## Step 2 — Scene Architecture

### 2A: Scene count by duration

| Duration | Scenes | Avg scene length | Notes                                        |
| -------- | ------ | ---------------- | -------------------------------------------- |
| 15-30s   | 3-4    | 4-7s             | Anthropic Shorts: typically 4 inline phases  |
| 45s      | 5-6    | 8-10s            | Anthropic Shorts: extend with extra phases   |
| 60s      | 6-7    | 9-10s            |                                              |
| 90s      | 7-8    | 11-13s           |                                              |
| 3min     | 8-10   | 15-22s           |                                              |

For the `shorts/anthropic` template: the 4 base archetypes are `hero-slam`, `stat-pill-row`, `timeline-cards`, `cta-url-slam` (per `templates/shorts/anthropic/README.md:11-18`). To add more scenes, follow the template's "Adding more phases" section — duplicate a `<div class="phase">` block, bump `data-duration` on `#root`, follow the `P1 → T1 → P2 → T2 …` naming convention.

### 2B: Word-count → minimum display duration (seconds, not frames)

For each scene, count the on-screen words (text visible to the viewer, NOT narration) and use this table:

| On-screen word count        | Minimum display duration |
| --------------------------- | ------------------------ |
| 0 (image/diagram only)      | 1.5 – 2.0s               |
| 1 – 3 words                 | 2.0 – 3.0s               |
| 4 – 10 words                | 3.0 – 4.0s               |
| 11 – 20 words               | 4.0 – 6.0s               |
| 21 – 35 words               | 6.0 – 8.0s               |
| 36+ words                   | 8.0s+ (split the scene)  |

**Phase 1 checklist for each scene**:
- Count the on-screen words from the scene's visual spec
- Look up the minimum duration above
- Verify the planned `data-duration` is ≥ that minimum PLUS the narration duration
- If narration covers 40 words in 12s but only 5 words appear on screen → minimum is 4s display but narration forces 12s → use narration-derived duration
- If the scene has 0 narration (pure visual beat) → enforce the table minimum strictly

This prevents the most common pacing bug: text appearing for 0.5-1.0s before the next scene fires, well under the comfortable reading time.

### 2C: Narrative arc (Kallaway Formula)

Structure the scene order as:
1. **Hook — Context Lean-In** (10-15% of duration) — establish topic clarity, mind-blowing fact or shared pain. Viewer self-selects within 4 seconds.
2. **Scroll-Stop Interjection** — "But/However/Yet" stun gun (integrated into Hook or Solution).
3. **Contrarian Snapback** — the Uno Reverse, unexpected path.
4. **Solution** (15-20%) — introduce the topic with benefit-first framing.
5. **Deep Dive** (40-50%) — 3-5 feature scenes, each BENEFIT-LED not feature-led.
6. **Social Proof / Trust** (10-15%) — proof points, cult-hop references.
7. **CTA** (10%) — closing call to action.

### 2D: The Explosion Timer

- **Short-form (< 60s)**: deliver unique value before 4-second mark.
- **YouTube (60s+)**: deliver value within first 60-120s.

Front-load the "Value Loop" — give immediate payoff to earn the right to continue.

### 2E: Story Lock placement

For each scene, note where Story Locks should appear (full taxonomy: `.claude/references/story-locks.md`):
- **Term Branding** (Lock #1): which scene introduces a coined term? (usually Scene 2-3)
- **Loop Openers** (Lock #5): between which scenes? (every 60-90s for long-form, every 20-30s for Shorts)
- **Negative Frame** (Lock #4): which feature/point benefits from "Stop doing X" framing?
- **Thought Narration** (Lock #3): after which major reveal? (usually post-hook or mid-video)

This is lightweight planning guidance — actual application happens in Phase 2.

**Hook scope rule**: Negative Frames and Loop Openers belong in Scene 02+ (post-click retention), NOT in the hook. The hook's job is to validate the click — not shame, manipulate, or create artificial tension.

---

## Step 3 — Open Loop Architecture (MANDATORY for 60s+)

### 3A: Primary Open Loop

Define ONE primary open loop — a question, tension, or promise raised early and resolved late:

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 01 (Hook)"
    setup_line: "<the specific sentence that opens the loop>"
    resolution_scene: "Scene 07 (Trust)"
    resolution_line: "<the specific sentence that closes the loop>"
    type: "<question | tension | promise | mystery>"
```

### 3B: Loop opener placement

| Video length | Min count | Suggested cadence |
| ------------ | --------- | ----------------- |
| < 60s        | 2         | Every 20-30s      |
| 60-180s      | 2-3       | Every 60-90s      |
| 180-420s     | 3-5       | Every 60-90s      |
| 420s+        | 5+        | Every 60-90s      |

```yaml
  loop_openers:
    - scene: "Scene 02"
      position: "opening"
      phrase: "<e.g., 'But that is just the beginning.'>"
    - scene: "Scene 04"
      position: "transition"
      phrase: "<e.g., 'Here is where it gets interesting.'>"
```

For sub-30s Shorts, the script is too short for explicit loop openers — skip this section and rely on the hook variant alone.

---

## Step 4 — Hook Variant Generation (MANDATORY)

Before the script is written, generate three hook variants. The strongest gets selected before committing to the full script.

### 4A: Hook formula by topic type

| Topic type                         | Best formula                  | Rationale                                        |
| ---------------------------------- | ----------------------------- | ------------------------------------------------ |
| New tool / product release         | Stakes                        | Urgency + FOMO                                   |
| Technical concept / tutorial       | Counterintuitive              | Contrast creates curiosity                       |
| Comparison / versus                | Number                        | Benchmarks anchor credibility                    |
| Case study / story                 | Counterintuitive + narrative  | Surprise flip earns investment                   |
| Workflow / productivity            | Stakes                        | Pain-first, solution-second                      |
| AI / emerging tech                 | Number + Counterintuitive     | Stats fight skepticism; contrarian fights hype   |

### 4B: Hook type by video purpose

| Video purpose                          | Preferred hook                                   | Why                                          |
| -------------------------------------- | ------------------------------------------------ | -------------------------------------------- |
| Feature announcement / tutorial        | **Direct Signal** — name the feature in line 1   | Audience clicked for THIS feature; validate immediately |
| Problem-solution / workflow fix        | **Question** or **Input Bias** — open with pain  | Pain earns the right to present the solution |
| Deep dive / architecture               | **Expert Secret** — "Senior engineers never..."  | Positions viewer as insider                  |
| Comparison / benchmark                 | **Contrast** — "[impressive thing], but get this..."| Sets up the comparison frame              |

**CRITICAL for feature videos**: Do NOT default to shame hooks ("Most developers don't know..."). Lead with what they'll learn, not what they're doing wrong. (The full first-liner catalog of 10 hook types lives in `.claude/references/faceless-tech-scriptwriting-playbook.md` §3.)

### 4C: Three variants

Generate exactly three:

- **Variant A — Counterintuitive**: contradicts common belief. Opens with "Wait, what?"
- **Variant B — Stakes**: quantifies cost of inaction. Opens with what the viewer loses by not watching.
- **Variant C — Number**: opens with a surprising stat, benchmark, or data point.

Each must attempt the 5-Layer Hook Stack:

| Layer | Name                          | Function                                  |
| ----- | ----------------------------- | ----------------------------------------- |
| 1     | Counterintuitive Claim        | Breaks the expected frame                 |
| 2     | Stakes Establishment          | Why this matters NOW                      |
| 3     | Number/Specificity Anchor     | Makes the abstract concrete               |
| 4     | Scroll-Stop Interjection      | The stun gun (But/However/Yet)            |
| 5     | Promise of Resolution         | Earns the right to continue               |

Short-form (< 60s) needs minimum layers 1+4. Long-form (60s+) needs all five.

### 4D: Advisory scoring

Score each variant on three dimensions (1-10 each):

| Dimension       | 9-10                                    | 7-8                                         | 5-6                                | 3-4                       |
| --------------- | --------------------------------------- | ------------------------------------------- | ---------------------------------- | ------------------------- |
| Curiosity Gap   | Single sentence creates immediate gap   | Gap takes 2-3 sentences                     | Some curiosity but dismissable     | Informational, no gap     |
| Stakes Clarity  | Specific, quantified stakes             | Clear but general                           | Implied, viewer must infer         | Benefits but no stakes    |
| Specificity     | Specific stat in opening line           | Named tools/examples within 30s             | Some specificity                   | Generic                   |

**Dimension 4 — Value Alignment** (0 or 1): does the hook opening line directly name or preview the video's main feature/concept? 1 if yes, 0 if it relies purely on pain/stat. CRITICAL for feature announcements — your audience clicked for the topic, not to be scolded.

**Stun Gun bonus**: +0.1 if But/However/Yet present.
**Promise bonus**: +1 if explicit promise of resolution.

```
base = (curiosity + stakes + specificity) / 3
hook_score = min(10, round(base + stun_bonus + alignment_bonus + promise, 1))
```

### 4E: Plan output format

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "<exact first sentence>"
    layers_present: [1, 4, 5]
    advisory_score: X.X
  variant_b:
    type: "stakes"
    opening_line: "<exact first sentence>"
    layers_present: [2, 3, 4, 5]
    advisory_score: X.X
  variant_c:
    type: "number"
    opening_line: "<exact first sentence>"
    layers_present: [3, 4, 5]
    advisory_score: X.X
  recommended: "variant_b"
```

In **interactive mode**: present all three variants and ask the user to pick.
In **autonomous mode**: pick the highest advisory score.

---

## Step 5 — Cinematic Hook Blueprint (MANDATORY)

After selecting the variant, write a blueprint that tells the composition build (Phase 4 / `new-anthropic-short.md`) exactly how to assemble the hook visually.

### 5A: Hook pattern selection

Choose a pattern based on content type and hook variant style:

| Pattern             | Best for                                          | Key visual technique                                                        |
| ------------------- | ------------------------------------------------- | --------------------------------------------------------------------------- |
| `FilmTrailer`       | Product launches, announcements, team reveals     | Title cards → pivot → portrait/logo reveal → rapid-fire features            |
| `ContrastPivot`     | Comparisons, myth-busting, contrarian takes       | Build context → smash cut → contrarian reveal → evidence                    |
| `StatCascade`       | Data-driven content, benchmarks, research         | Rapid stat slams with scale springs → context → deep stat                   |
| `RackFocusReveal`   | Tool demos, screenshot-heavy intros               | Blurred screenshot → snap focus → callouts appear on product                |
| `TerminalHacker`    | Technical/coding content, CLI tools               | Typewriter terminal → shatter reveal → product behind                       |
| `SplitScreenDuel`   | Head-to-head comparisons, X vs Y                  | 50/50 split → checks vs crosses → winner expands to 100%                    |

Pattern selection rules:
- Product/team announcement + Stakes/Counterintuitive hook → `FilmTrailer`
- Technical concept + Counterintuitive hook → `ContrastPivot` or `TerminalHacker`
- Comparison/versus + Number hook → `SplitScreenDuel` or `StatCascade`
- Tool demo + any hook → `RackFocusReveal`
- Data/benchmark + Number hook → `StatCascade`

### 5B: Visual beats (in seconds, no frames)

Define each visual beat with timing in seconds, GSAP ease, and SFX:

| GSAP ease (cite by name) | Feel                            | Use for                                 |
| ------------------------ | ------------------------------- | --------------------------------------- |
| `power3.out`             | Grounded, no bounce             | Title cards, context-setting text       |
| `sine.inOut`             | Soft rise                       | Body text, descriptions                 |
| `power4.out`             | Fast, controlled                | Feature names, brand text               |
| `back.out(1.7)`          | Aggressive overshoot            | Pivot words, "BUT.", stat reveals       |
| `elastic.out(1, 0.5)`    | Quick pop with settle           | Brand name, logo entrance               |
| `power2.out` + stagger   | Light rolling motion            | Avatar pop-ins, badge reveals           |

Full ease + stagger guidance: `.agents/skills/gsap/SKILL.md` and `.agents/skills/gsap/references/effects.md`.

### 5C: SFX placement (cue names that resolve to library files)

Pick cue names from `shared/audio/MANIFEST.md` — every name MUST resolve to a real file in `shared/audio/sfx/<cue>.mp3`. Volume caps and the per-cue defaults are canonical in [`.claude/rules/audio-design.md`](../../rules/audio-design.md). Each SFX renders as a separate `<audio>` element on its own `data-track-index` so simultaneous cues don't clash (per `templates/shorts/anthropic/README.md` "Adding SFX").

| Beat                  | Cue(s) from MANIFEST                                                | Default `data-volume` |
| --------------------- | ------------------------------------------------------------------- | --------------------- |
| Cold open             | none (or `sonic-logo` once, optional)                                | sonic-logo: 0.60      |
| Context entrance      | `impact-slam`                                                        | 0.20                  |
| PIVOT moment          | LAYERED: `impact-slam` + `screen-shake` + `glitch-zap` (own tracks)  | 0.20 / 0.15 / 0.12    |
| Brand reveal          | `scale-slam`                                                         | 0.20                  |
| Feature card entrance | `spring-pop`, repeat per card                                        | 0.15                  |
| Strikethrough beat    | `strike-cross`                                                       | 0.15                  |
| Phase / scene change  | `cinematic-whoosh`                                                   | 0.15                  |

Output a structured `sfx_cues:` block alongside the visual beats — Phase 3.5 consumes this directly to map cue names to seconds, track indices, and volumes:

```yaml
sfx_cues:                          # consumable by phase3-5-retention.md
  - beat: "Context entrance"
    cues: [impact-slam]            # MUST come from shared/audio/MANIFEST.md
  - beat: "PIVOT"
    cues: [impact-slam, screen-shake, glitch-zap]
  - beat: "Brand reveal"
    cues: [scale-slam]
  - beat: "Feature card entrance"
    cues: [spring-pop]
```

**Hard rule:** every cue name MUST appear in `shared/audio/MANIFEST.md`. If a needed cue is missing, STOP and propose an addition to the library (new row in MANIFEST + new entry in `scripts/generate-sfx-library.py`) — do **not** invent a filename. The sync hook will fail fast with a helpful message listing the actual library contents.

### 5D: Music profile

| Pattern             | Hook BPM   | Body BPM  | CTA BPM    | Hook mood              |
| ------------------- | ---------- | --------- | ---------- | ---------------------- |
| `FilmTrailer`       | 95-105     | 75-90     | 110-120    | dramatic-cinematic     |
| `ContrastPivot`     | 90-100     | 75-90     | 110-120    | dramatic-cinematic     |
| `StatCascade`       | 100-110    | 75-90     | 110-120    | hype-energetic         |
| `RackFocusReveal`   | 90-100     | 75-90     | 110-120    | tech-influencer-edgy   |
| `TerminalHacker`    | 95-105     | 75-90     | 110-120    | tech-influencer-edgy   |
| `SplitScreenDuel`   | 90-100     | 75-90     | 110-120    | dramatic-cinematic     |

For Anthropic Shorts: per `templates/shorts/anthropic/README.md` "Don'ts", **no background music on Shorts** — narration + SFX only. Skip the music profile section entirely for that template.

### 5E: Blueprint plan output format

```yaml
cinematic_hook_blueprint:
  pattern: "<FilmTrailer | ContrastPivot | StatCascade | RackFocusReveal | TerminalHacker | SplitScreenDuel>"
  selected_variant: "<variant_a | variant_b | variant_c>"

  visual_beats:
    - beat: "Cold Open"
      timing_s: [0, 2]
      visual: "<description: e.g., Pure black → title card slides in>"
      gsap_ease: "power3.out"
      sfx: null
    - beat: "Context"
      timing_s: [2, 8]
      visual: "<description>"
      gsap_ease: "power4.out"
      sfx: "single impact-slam"
    - beat: "PIVOT"
      timing_s: [8, 8.5]
      visual: "<description: e.g., White flash + 'BUT' 240px red>"
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake + glitch-zap"
    - beat: "Reveal"
      timing_s: [8.5, 16]
      visual: "<description>"
      gsap_ease: "elastic.out(1, 0.5)"
      sfx: "scale-slam"
    - beat: "Rapid-Fire"
      timing_s: [16, 35]
      visual: "<description>"
      gsap_ease: "back.out(1.7)"
      sfx: "spring-pop per card"
    - beat: "CTA"
      timing_s: [35, 40]
      visual: "<description>"
      gsap_ease: "sine.inOut"
      sfx: null

  pivot_word: "<exact word in script that triggers the pivot, e.g., 'But'>"
  brand_reveal_word: "<the word where the brand/product name appears>"

  assets_needed:
    - type: "<portrait | logo | screenshot | video>"
      description: "<what it shows>"
      source: "<URL or file path if known, else 'TBD — capture in composition build'>"

  music_profile:
    hook_mood: "<dramatic-cinematic | tech-influencer-edgy | hype-energetic | NONE>"
    hook_bpm: [<min>, <max>]
    body_bpm: [75, 90]
    cta_bpm: [110, 120]
```

For Anthropic Shorts, set `music_profile.hook_mood: NONE` and add a note `# template forbids background music on Shorts`.

---

## Step 6 — Preview Hook Strategy (MANDATORY for 60s+; OPTIONAL for shorter)

Every video 60s+ MUST include a Scene 00 preview that:
- Runs 10-15 seconds
- Shows 4-6 quick teasers from upcoming content
- Changes visuals every 0.3-0.5s
- Creates "open loops" that demand resolution

For sub-30s Shorts, skip the explicit preview — the hook variant IS the preview.

### Preview hook template (60s+)

| Phase            | Time      | Content                                  |
| ---------------- | --------- | ---------------------------------------- |
| Attention Grab   | 0 – 1s    | Bold stat or shocking statement          |
| Teaser 1         | 1 – 3s    | Quick clip from a mid-video scene        |
| Teaser 2         | 3 – 5s    | Quick clip from another mid-video scene  |
| Teaser 3         | 5 – 7s    | Quick clip from final feature            |
| Promise          | 7 – 10s   | "In this video..." value proposition     |

Plan output:

```markdown
### Scene 00 Preview (if duration >= 60s)
- **Type**: <Montage / Stats / Before-After / Question>
- **Duration**: <10-15>s
- **Phases**:
  1. [0-1s]    Attention Grab: <bold statement or stat>
  2. [1-3s]    Teaser 1: <preview of Scene X>
  3. [3-5s]    Teaser 2: <preview of Scene Y>
  4. [5-7s]    Teaser 3: <preview of Scene Z>
  5. [7-10s]   Promise: "In this video, <value proposition>"
```

---

## Step 7 — Composition Layout

HyperFrames composition primitives:

1. **Inline phases** OR **sub-compositions** (`data-composition-src="compositions/scene-NN.html"`) per CLAUDE.md "Key Rules" #5
2. **GSAP timelines** registered on `window.__timelines["composition-id"]` (CLAUDE.md Key Rule #3)
3. **Retention components** from `.claude/references/retention-components-hyperframes.md` (the menu)

### 7A: Choose composition structure

| Layout model         | Use when                                                          | Constraint                                            |
| -------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- |
| `inline-phase`       | Single-file composition with mutex `.phase` divs                  | Required for `shorts/anthropic` template              |
| `sub-composition`    | Each scene is its own HTML file under `compositions/`             | For long-form or scene reuse across videos            |

For Anthropic Shorts, the layout is forced: `inline-phase` + `mutex-visibility`. Sub-compositions are NOT used.

### 7B: Per-scene retention picks

For each scene, pick 1-3 retention components from `.claude/references/retention-components-hyperframes.md`. Cite by canonical name. Examples:

```yaml
retention_component_picks:
  scene_01_hook:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam"           # composite from §7 of retention-components-hyperframes.md
    primitives:
      - "gsap-stagger-grid"        # for the overline → slam → caption pill sequence
      - "marker-highlight on the slam word"   # max 1 marker on this scene
    captions: null                 # hook is too short for synced captions
    audio_reactive: null           # narration too sparse to react against
    transition_out: "blur-crossfade"  # picked from §4 of retention-components-hyperframes.md

  scene_02_stat_row:
    structural: "inline-phase"
    pattern: "stat-pill-row"
    primitives:
      - "gsap-counter-tween"       # numbers tick up
      - "gsap-stagger-grid"        # cards appear in sequence
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_timeline:
    structural: "inline-phase"
    pattern: "timeline-cards"
    primitives:
      - "gsap-stagger-grid"
      - "gsap-path-draw on the connecting line"
    captions: "caption-fade-slide if narration explains the timeline"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_04_cta:
    structural: "inline-phase"
    pattern: "cta-url-slam"
    primitives:
      - "marker-circle on the URL"
      - "gsap-stagger-grid for the subscribe pill"
    captions: null
    audio_reactive: "audio-reactive-glow on the CTA URL (subtle, treble band)"
    transition_out: null    # final scene, no transition
```

**Constraints**:
- Max 2 markers per scene.
- Only one `caption-*` group visible at a time.
- Pick ONE primary transition (60-70% of scene changes) + 1-2 accents — never a different transition for every scene.
- Anti-patterns from `.claude/references/retention-components-hyperframes.md` §8 are HARD bans.

### 7C: data-start / data-duration budget

For each scene, write its `data-start` and `data-duration` in **seconds** (not frames). HyperFrames is seconds-native via the `data-*` attributes on each `.clip` element (CLAUDE.md Key Rule #1).

```yaml
data_timing_budget:
  - scene: "scene_01_hook"
    data_start: 0
    data_duration: 8
    audio_anchor: "narration starts at 0.5s, hook word at 7.2s"
  - scene: "scene_02_stat_row"
    data_start: 8
    data_duration: 7
    audio_anchor: "first stat number spoken at 9.1s"
  - scene: "scene_03_timeline"
    data_start: 15
    data_duration: 8
    audio_anchor: "first date spoken at 16.0s"
  - scene: "scene_04_cta"
    data_start: 23
    data_duration: 7
    audio_anchor: "URL spoken at 25.0s"
total_data_duration: 30   # this becomes #root data-duration
```

`audio_anchor` values are PLACEHOLDERS at Phase 1. Phase 3.5 will refine them against `transcript.json` once TTS + transcribe have run.

### 7D: HyperFrames blocks (optional)

If the plan uses any `hyperframes-registry` blocks (see `/hyperframes-registry`), list them:

```yaml
hyperframes_blocks_used:
  - name: "<block-name>"
    scene: "scene_NN"
    why: "<reason>"
```

Most plans will leave this empty unless the project has registry-installed blocks.

---

## Step 8 — Visual Design Language

For Anthropic Shorts: USE the template's `DESIGN.md` design tokens verbatim (CSS variables on `#root`: `--orange`, `--purple`, `--blue`, `--green`, `--pad-top`, etc.). Do NOT override unless the brand requires it (e.g. Google brand video — swap `--orange` to `#4285F4`).

For other (future) templates: read that template's `DESIGN.md` and follow the same convention.

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides:
    - css_var: "--orange"
      original: "#E97458"
      override: "#4285F4"
      reason: "Google brand video"
  fonts:
    sans: "Inter"        # template default, do not change unless DESIGN.md updated
    mono: "JetBrains Mono"
```

---

## Step 9 — AI Image Prompts (OPTIONAL)

If the video needs custom AI-generated images (hero shots, abstract backgrounds, conceptual visuals — NOT text/diagrams/code/UI mockups), define prompts:

```yaml
images:
  - scene: "scene_01_hook"
    name: "scene-01-hero"
    prompt: "[Detailed description with style, lighting, composition]"
    aspect_ratio: "9:16"   # for Anthropic Shorts; "16:9" for landscape
    usage: "Background image for hook scene"
```

Guidelines:
1. **Be Specific**: Include lighting, style, mood, technical details.
2. **Match video theme**: Use consistent visual language.
3. **Dark backgrounds**: Work best with text overlays.
4. **Avoid text in images**: Imagen / Midjourney can't render text reliably.

Generated images will be created in the composition build phase. Drop into `videos/<slug>/assets/`.

---

## Step 10 — Screenshot Capture Inventory (RECOMMENDED if brief flagged demos)

If the content brief's "Demo Opportunity Inventory" identified web pages worth capturing:

```yaml
screenshots:
  - name: "github-repo-hero"
    url: "https://github.com/org/repo"
    scene: "scene_03"
    color_scheme: "dark"
    usage: "Product intro background"
  - name: "docs-quickstart"
    url: "https://docs.example.com/quickstart"
    scene: "scene_05"
    color_scheme: "dark"
    usage: "Documentation walkthrough"
    scroll_to_selector: "#getting-started"
```

Default `color_scheme: dark` for tech tools. Use `light` only when the product's light mode is canonical. Capture happens in the composition build phase (NOT here in Phase 1).

---

## Step 11 — File Structure (HyperFrames layout)

The plan should result in this layout under `videos/<slug>/` (most files created during composition build, not by this phase):

```
videos/<slug>/
├── meta.json                  # already exists from template copy
├── hyperframes.json           # already exists from template copy
├── DESIGN.md                  # already exists from template copy
├── README.md                  # already exists from template copy
├── plan.md                    # ← THIS PHASE'S OUTPUT
├── phase-status.md            # tracked across phases
├── research/
│   └── content-brief.md       # from Phase 0
├── scripts/                   # from Phase 2 / 2a / 2b
│   └── ...
├── retention-strategy.md      # from Phase 3.5
├── index.html                 # composition build phase
├── compositions/              # composition build phase, only if sub-compositions chosen
│   └── scene-NN-<name>.html
├── assets/                    # screenshots, AI images, sfx
│   └── ...
├── audio/
│   └── narration.wav          # from `npx hyperframes tts`
├── transcript.json            # from `npx hyperframes transcribe`
└── out/                       # rendered MP4 (gitignored)
```

Phase 1 only writes `plan.md` and updates `phase-status.md`. Everything else is created in later phases.

---

## Step 12 — Fact-Check Gate at Phase 1 (C-08)

Fact-checking is a Phase 1 / Phase 2b gate — NOT a post-render step. Fabricated quotes and unverified statistics CANNOT be patched in the rendered video without full audio + sync regeneration.

**Phase 1 plan must include for every claim**:
- Every direct quote attributed to a named person → cited source URL in the plan
- Every statistic (numbers, percentages, dates) → cited source URL
- Every product fact (version numbers, lifecycle labels Preview/GA/Beta, customer deployment specifics) → cited source URL

**Hard rule**: if any claim cannot be sourced, EITHER remove it from the plan OR rephrase as `reportedly` / `according to <source>` with the source named in narration. Do not allow unverified claims to enter Phase 2 script generation.

The Phase 2b fact-check skill (`/diy-yt-creator:phase2b-factcheck`) is the secondary gate that re-verifies all claims after script generation. Run it always — even if Phase 1 was thorough.

**NEVER** generate direct-speech quotes for real people unless the EXACT quote appears in a cited source. Use paraphrase with attribution instead.

</process>

<output>
**Save to**: `videos/<slug>/plan.md`

The plan file is markdown with embedded YAML blocks for the structured sections defined above. Required top-level sections (in this order):

1. `# Composition Plan: <slug>` (heading)
2. `## Director's Summary` (2-3 sentences on the vision)
3. `## Template & Structure` — template choice, composition layout model, design token overrides
4. `## Master Timeline` — table: Scene | data_start | data_duration | Visual Goal | Key Elements
5. `## Narrative Arc` — Kallaway breakdown
6. `## Hook Variants` — the YAML block from Step 4E with the recommended variant
7. `## Cinematic Hook Blueprint` — the YAML block from Step 5E
8. `## Open Loop Architecture` — the YAML block from Step 3 (or "N/A — sub-30s Short")
9. `## Story Lock Placement` — bullet list per scene
10. `## Composition Layout` — `composition_layout` YAML
11. `## Retention Component Picks` — `retention_component_picks` YAML from Step 7B
12. `## Data Timing Budget` — `data_timing_budget` YAML from Step 7C, with `total_data_duration`
13. `## Visual Design Language` — `design_tokens` YAML from Step 8
14. `## AI Image Prompts` — `images` YAML (or "None")
15. `## Screenshot Inventory` — `screenshots` YAML (or "None")
16. `## HyperFrames Blocks` — `hyperframes_blocks_used` YAML (or "None")
17. `## Fact-Check Audit` — table of every claim in the plan with source URL or "REMOVED — unsourced"
18. `## Notes for Composition Build` — free-form guidance for whoever builds the HTML next

**Report to user**:
1. Director's Summary (2-3 sentences)
2. Master Timeline table (Scene | data_start | data_duration | Visual Goal | Key Elements)
3. Recommended hook variant + why
4. Hook pattern + visual beat count
5. Total `data_duration` (sum of all scene durations)
6. Retention component pick count by category (markers, captions, audio-reactive, transitions)
7. Fact-check audit summary (claims with sources / claims removed / claims rephrased)
8. Next step: Run `/diy-yt-creator:phase2-script <slug>`

### Update Phase Status

Update `videos/<slug>/phase-status.md` — set the `1 - Plan` row to `done <YYYY-MM-DD>` (today's date). If the file doesn't exist, create it with all phases as `pending` first (template in `phase0-research.md`).

</output>
