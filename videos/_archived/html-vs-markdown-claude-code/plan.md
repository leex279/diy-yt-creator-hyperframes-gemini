# Composition Plan — html-vs-markdown-claude-code

## Director's Summary

An 8-minute long-form essay-video about why Thariq (Claude Code @ Anthropic)
publicly switched his agent output format from Markdown to HTML — and why
others on the team are doing the same. Visually, the video itself adopts
**the same editorial-light aesthetic as Thariq's example gallery** (cream
canvas, bold black serif headlines, terracotta italic accents, numbered
section chrome, 3-column card grid) — so form mirrors content. We deliver
the article's thesis (information density + visual clarity + sharing +
two-way interaction + data ingestion + joy), tour the 5 use cases as a card
grid, surface the 2-4× tradeoff honestly, and close on the human payoff:
*"more in the loop than ever before."*

## Template & Structure

- **Template**: `templates/long-form/standard/` (canvas 1920×1080, sub-composition split)
- **Voice**: cloned voice via `.env` (`ELEVENLABS_VOICE_ID=7kXNOCqiaLdszL0OEXks`, model `eleven_multilingual_v2`, speed `1.10`)
- **Total target duration**: 8 min ≈ 480 s
- **Audio bed**: narration-only (the editorial-light aesthetic + essay tone is steadier *without* bg-music; matches the quiet energy of Thariq's gallery)
- **Captions**: `compositions/captions.html` populated via `npx hyperframes transcribe` (default-on per long-form template)
- **Token override**: `videos/html-vs-markdown-claude-code/tokens/long-form.css` → editorial-light palette + serif type families. Replaces, not extends, the dark-navy default.

### Token override (editorial-light) — exact values

These values come from the gallery hero screenshot. The composition build
(Task 11) writes them into `tokens/long-form.css`.

```css
:root {
  /* Surface */
  --bg:               #F4F1EA;     /* warm cream */
  --bg-card:          #FBF8F1;     /* card paper */
  --bg-surface:       #EFEBE0;     /* raised pill */
  --border:           rgba(28,26,24,0.10);
  --border-bright:    rgba(199,90,63,0.50);

  /* Type */
  --text:             #1A1815;     /* charcoal — body */
  --text-secondary:   #5C544B;     /* warm gray */
  --text-muted:       #8A8175;     /* metadata */

  /* Accent (terracotta-led, single accent — no rotation) */
  --accent-1:         #C75A3F;     /* terracotta — italic title accent + section numbers */
  --accent-2:         #B14938;     /* deeper red — overline text "COMPANION TO…" */
  --accent-3:         #586F4F;     /* muted olive — for the few "good" callouts */
  --accent-4:         #C75A3F;     /* alias #1 (single-accent system) */
  --accent-warn:      #B14938;
  --accent-stat:      #1A1815;     /* hero stats stay charcoal — let the size do the work */

  /* Type families */
  --serif:            'Source Serif 4', 'Playfair Display', Georgia, serif;
  --sans:             'Inter', system-ui, sans-serif;
  --mono:             'JetBrains Mono', ui-monospace, monospace;
}
```

Headlines use `--serif` weight 800. The italic title accent (the "effectiveness"
treatment from Thariq's hero) uses `font-style: italic; color: var(--accent-1);`
on a `<em>` element inside the headline. Overlines use `--mono` 700 uppercase
in `--accent-2`. Section numbers (01 / 02 / …) use `--mono` 700 in `--accent-1`
at 0.55× the headline size, sitting in the left margin.

## Master Timeline

| # | Scene file | data_start (s) | data_dur (s) | Visual goal | Key elements |
|---|---|---|---|---|---|
| 0 | `scene-hook` | 0 | 32 | Cold open: the article cover floats in, social proof receipts (751K views) tick up, then the thesis snaps in: *"the unreasonable effectiveness *of* HTML"* in serif italic. | Article cover screenshot, three small receipt pills (202 replies / 341 reposts / 2.7K likes / 751K views), serif italic title slam |
| 1 | `scene-image-hero` | 32 | 75 | The 8 information types HTML can carry — an information-density argument. Cream card grid with mono labels. | 3×3 minus-1 card grid: tables, CSS, SVG, code snippets, JS+CSS interactions, workflows, spatial canvas, images. Numbered "01 Information density" overline. |
| 2 | `scene-side-by-side` | 107 | 70 | Markdown vs HTML head-to-head: the ASCII-diagram fail vs the rendered HTML chart. Same data, two formats. | Left card: ".md" mono badge + a stale ASCII bar chart that breaks alignment. Right card: ".html" mono badge + a clean SVG bar chart. Score below. |
| 3 | `scene-stat-pill-row` | 177 | 50 | The honest tradeoff: 2-4× longer to generate, but Opus 4.7's 1MM context absorbs the extra tokens. | Two huge stats: `2-4×` (generation cost) + `1MM` (context window). Caption underneath: *"the math actually works."* |
| 4 | `scene-source-cards` | 227 | 110 | The 5 use cases as a card grid mirroring Thariq's gallery layout. | 5 cards: Specs & Planning, Code Review, Design & Prototypes, Reports & Research, Custom Editors. Each card has icon + numbered overline + title + 1-line role + the verbatim prompt hint as a mono code block. |
| 5 | `scene-architecture-stack` | 337 | 55 | Why Claude Code specifically (not ClaudeAI / Claude Design): the data-ingestion stack. | 5 stacked bars: Filesystem, MCPs (Slack/Linear/etc.), Browser (Claude in Chrome), Git history, MCPs again — labels in mono. Numbered overline "05 Why Claude Code specifically". |
| 6 | `scene-cta` | 392 | 88 | Closing: the human payoff + Dynamous handoff. | Pull-quote treatment ("more in the loop than ever before"), fade to a hand-off card with the dynamous.ai community. Subscribe pulse + comment-prompt question. |

**total_data_duration = 480** seconds (8 min).

`scene-video-embed` is **dropped** (no clip available, and the editorial tone
doesn't need a moving demo). Its wrapper `<div>` and corresponding
`crossfadeScenes()` call are removed from `index.html` per the long-form
playbook step 4 / step 7.

## Narrative Arc (Kallaway / news-explainer)

| Beat | Time | Function |
|------|------|----------|
| Hook — Context Lean-In | 0–10s | "Markdown is the default. But the team that built Claude Code stopped using it." |
| Scroll-Stop Interjection | 10–18s | "751K people read this. Most of the replies were 'wait, you too?'." |
| Contrarian Snapback | 18–32s | The thesis: HTML beats Markdown for agent output. Serif italic title slam. |
| Solution — Why HTML | 32–107s | Information density argument with 8 carriers. |
| Deep Dive — Compare | 107–177s | Side-by-side proof. ASCII fail vs SVG chart. |
| Receipts — Honest Tradeoff | 177–227s | The 2-4× cost + the 1MM context that absorbs it. |
| Use Cases | 227–337s | The 5 categories as a card grid. |
| Why Claude Code (not Claude Design) | 337–392s | Data-ingestion stack — the ground-truth advantage. |
| Trust + CTA | 392–480s | "More in the loop than ever before." Dynamous handoff. |

Connector words across transitions: *"because"*, *"so"*, *"here's what changed"*, *"and yet"*, *"the trick is"*, *"why this works"* — every scene boundary carries a connector to satisfy the news-explainer Pass 6 gate.

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: counterintuitive
    opening_line: "The team that built Claude Code stopped using markdown."
    layers_present: [1, 2, 5]
    source_fidelity:
      source_quote: "I've started preferring HTML as an output format instead of Markdown and increasingly see this being used by others on the Claude Code team, this is why."
      head_nouns: ["team", "markdown"]
      passes_gate: true
    advisory_score: 8.4

  variant_b:
    type: stakes
    opening_line: "Right now your agent is writing markdown specs nobody reads."
    layers_present: [2, 4, 5]
    source_fidelity:
      source_quote: "I've found I tend to not actually read more than a 100-line markdown file, and I certainly am not able to get anyone else in my organization to read it."
      head_nouns: ["agent", "markdown"]
      passes_gate: true
    advisory_score: 7.6

  variant_c:
    type: number
    opening_line: "751,000 people read this post. The thesis: HTML beats markdown for agent output."
    layers_present: [3, 4, 5]
    source_fidelity:
      source_quote: "[X engagement screenshot] 751K views"
      head_nouns: ["people", "post"]
      passes_gate: true
    advisory_score: 8.1

  recommended: variant_a
  rationale: |
    Variant A wins on Curiosity (single sentence, immediate gap — "stopped using
    *what*?") and Value Alignment (names the thing in line 1: Claude Code +
    markdown). Variant C's number is strong but the click came from the article;
    the viewer already knows "lots of people read this." Variant B leads with
    shame which the project rules explicitly de-prioritise for feature/positive
    content.
```

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: ContrastPivot
  selected_variant: variant_a

  visual_beats:
    - beat: Cold Open
      timing_s: [0, 3.5]
      visual: |
        Cream canvas. Mono overline in deep red fades in:
        "USING CLAUDE CODE". Below it, the article cover screenshot
        (article-cover.png) tilts gently into frame from below.
      gsap_ease: power3.out
      sfx: null
    - beat: Receipts
      timing_s: [3.5, 10]
      visual: |
        Three small receipt pills count up underneath the cover:
        "202 replies", "341 reposts", "2.7K likes", "751K views" —
        mono, with the underline-marker treatment from the source page.
      gsap_ease: back.out(1.4)
      sfx: null
    - beat: Pivot
      timing_s: [10, 18]
      visual: |
        The cover shrinks 30% to the right. To its left a serif headline
        appears word-by-word: "The team that built Claude Code stopped
        using markdown." The word "stopped" gets a hand-drawn
        terracotta underline (marker-highlight, 0.6s sweep).
      gsap_ease: power4.out
      sfx: null
    - beat: Title Slam
      timing_s: [18, 28]
      visual: |
        Cover fades, the full title slams in serif:
        "The unreasonable *effectiveness* of HTML"
        — "effectiveness" set in serif italic terracotta, mirroring
        the source page hero exactly.
      gsap_ease: power3.out
      sfx: null
    - beat: Promise
      timing_s: [28, 32]
      visual: |
        Mono caption fades in below: "Why every tier of your work is
        about to look different." Then crossfade to scene 1.
      gsap_ease: sine.inOut
      sfx: null

  pivot_word: "stopped"
  brand_reveal_word: "effectiveness"

  assets_needed:
    - type: screenshot
      description: Article cover (Thariq's X-post hero card)
      source: assets/article-cover.png   # already in place
    - type: screenshot
      description: Thariq profile (used briefly in trust beat at scene 6 if needed)
      source: assets/thariq-profile.png  # already in place
    - type: screenshot
      description: Reference for the editorial-light aesthetic
      source: assets/source-pages/gallery-hero.png  # already in place

  music_profile:
    hook_mood: NONE   # narration-only; the editorial tone reads cleaner without bg-music
    note: "Departing from long-form template default of 3-segment bg-music. Rationale logged in this plan."
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 0 (Hook)"
    setup_line: "The team that built Claude Code stopped using markdown."
    resolution_scene: "Scene 6 (CTA)"
    resolution_line: "He says it best himself: more in the loop than ever before."
    type: question

  loop_openers:
    - scene: "Scene 1"
      position: opening
      phrase: "Here's what HTML can carry that markdown can't."
    - scene: "Scene 3"
      position: transition
      phrase: "And yes — there's a price. The honest one."
    - scene: "Scene 4"
      position: opening
      phrase: "Five places this changes everything."
```

## Story Lock Placement

- **Scene 0 — Direct Signal hook** (validate the click on Claude Code + HTML).
- **Scene 1 — Term Branding**: introduce the phrase *"information density"* as the named tradeoff lens.
- **Scene 2 — Negative Frame**: ASCII-diagram failure mode is the foil — *"this is what happens when the agent has no choice but markdown."*
- **Scene 3 — Thought Narration**: *"two-to-four-times longer to generate. Worth it? Here's why the math works."*
- **Scene 4 — Loop Opener at top**: *"five places this changes everything."*
- **Scene 5 — Trust beat**: not Claude Design — Claude Code, because of context ingestion.
- **Scene 6 — Resolution**: closes the primary loop with Thariq's own line.

## Composition Layout

```yaml
composition_layout:
  model: sub-composition          # long-form pattern; each scene is its own HTML file
  root_orchestration:
    - ambient breath (sine.inOut yoyo)
    - shape backdrop drift (deterministic)
    - 6 scene crossfades at the data_start values above
    - top banner with project wordmark (replace template's anthropic logo)
    - bottom progress bar fill across TOTAL_DURATION

  scenes:
    - id: scene-hook
      file: compositions/scene-hook.html
      data_start: 0
    - id: scene-image-hero
      file: compositions/scene-image-hero.html
      data_start: 32
    - id: scene-side-by-side
      file: compositions/scene-side-by-side.html
      data_start: 107
    - id: scene-stat-pill-row
      file: compositions/scene-stat-pill-row.html
      data_start: 177
    - id: scene-source-cards
      file: compositions/scene-source-cards.html
      data_start: 227
    - id: scene-architecture-stack
      file: compositions/scene-architecture-stack.html
      data_start: 337
    - id: scene-cta
      file: compositions/scene-cta.html
      data_start: 392

  scene_video_embed_dropped: true
  reason: "No clip available; editorial tone doesn't require moving demo. Wrapper div + crossfade call removed from index.html."
```

## Retention Component Picks

```yaml
retention_component_picks:
  scene_0_hook:
    structural: "sub-composition"
    pattern: "ContrastPivot — article cover → receipt pills → serif italic title slam"
    primitives:
      - gsap-stagger-grid    # receipts count-up in 4-pill row
      - marker-highlight     # under "stopped" (terracotta sweep)
      - serif-italic-accent  # NEW pattern for this token system: <em> word in serif italic + accent-1
    captions: null
    audio_reactive: null
    transition_out: blur-crossfade

  scene_1_image_hero:
    structural: "sub-composition"
    pattern: "8-card information-types grid (3 cols × 3 rows minus 1, or 4×2)"
    primitives:
      - gsap-stagger-grid    # cards reveal step-by-step (per .claude/rules/step-by-step-reveal.md)
      - mono-badge           # ".html" / ".md" file-extension badges
    captions: caption-fade-slide
    audio_reactive: null
    transition_out: blur-crossfade

  scene_2_side_by_side:
    structural: "sub-composition"
    pattern: "Side-by-side: ASCII (fail) vs SVG (win)"
    primitives:
      - svg-path-draw        # the SVG bar chart draws on
      - strikethrough-marker # struck-through ASCII bars in the failure card
    captions: caption-fade-slide
    audio_reactive: null
    transition_out: blur-crossfade

  scene_3_stat_pill_row:
    structural: "sub-composition"
    pattern: "Two-pill receipt: 2-4× and 1MM"
    primitives:
      - gsap-counter-tween   # 1MM ticks 0 → 1,000,000
      - scale-pulse          # 2-4× scale-pop on emphasis
    captions: null
    audio_reactive: null
    transition_out: blur-crossfade

  scene_4_source_cards:
    structural: "sub-composition"
    pattern: "5-card use-case grid (3-col mirrors Thariq's gallery)"
    primitives:
      - gsap-stagger-grid    # cards reveal one beat at a time, ~5s apart
      - mono-overline        # numbered "USE CASE 01" treatment per card
      - example-prompt-mono  # verbatim prompt as code-block inside each card
    captions: caption-fade-slide
    audio_reactive: null
    transition_out: blur-crossfade

  scene_5_architecture_stack:
    structural: "sub-composition"
    pattern: "Stacked layers — data sources Claude Code can ingest"
    primitives:
      - gsap-stagger-grid    # layers reveal bottom-up
      - layer-fill           # each layer fills horizontally on entrance
    captions: caption-fade-slide
    audio_reactive: null
    transition_out: blur-crossfade

  scene_6_cta:
    structural: "sub-composition"
    pattern: "Pull-quote → handoff card"
    primitives:
      - serif-pull-quote     # large serif quote treatment with terracotta italic accent on key word
      - dynamous-handoff     # community card + spoken outro alignment
      - subscribe-pulse      # finite repeat: 4
    captions: caption-fade-slide
    audio_reactive: null
    transition_out: null     # final scene
```

**Hard rules respected:**
- Max 2 markers per scene (only Scene 0 uses one; others rely on motion + type).
- Single accent per scene (terracotta `--accent-1` leads everything; muted olive `--accent-3` only for "good" callouts in the side-by-side).
- One primary transition (`blur-crossfade`) across all 6 scene changes.
- No `repeat: -1` anywhere. Subscribe pulse has finite `repeat: 4`.
- Step-by-step reveal in scenes 1, 4, 5 (no all-bullets-at-once).
- 5-second visual-pacing rule applied to every scene (no static gap > 5s).

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: scene_0_hook
    data_start: 0
    data_duration: 32
    audio_anchor: "narration starts at 0.6s; pivot word 'stopped' at ~12.5s; title slam after 'markdown.' at ~18.5s"
  - scene: scene_1_image_hero
    data_start: 32
    data_duration: 75
    audio_anchor: "first information-type word ('tables') at ~35s; final ('images') at ~95s"
  - scene: scene_2_side_by_side
    data_start: 107
    data_duration: 70
    audio_anchor: "ASCII fail demo cue at ~115s; SVG draw cue at ~135s"
  - scene: scene_3_stat_pill_row
    data_start: 177
    data_duration: 50
    audio_anchor: "'2 to 4 times longer' at ~182s; '1 million context' at ~200s"
  - scene: scene_4_source_cards
    data_start: 227
    data_duration: 110
    audio_anchor: "card-1 'specs and planning' at ~232s; card-5 'custom editors' at ~315s"
  - scene: scene_5_architecture_stack
    data_start: 337
    data_duration: 55
    audio_anchor: "'filesystem' at ~342s; 'MCPs' at ~355s; 'git history' at ~375s"
  - scene: scene_6_cta
    data_start: 392
    data_duration: 88
    audio_anchor: "pull-quote build-up starts ~395s; dynamous spoken outro at ~460s"

total_data_duration: 480
```

`audio_anchor` values are **placeholders**. Phase 3.5 / composition-build replaces every value with the exact `transcript.json[<word>].start` once TTS lands.

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/long-form/standard/DESIGN.md"
  override_file: "videos/html-vs-markdown-claude-code/tokens/long-form.css"
  override_kind: "complete-replacement"   # NOT extending the dark-navy default
  rationale: |
    The video's thesis is "form should match content." Source page is editorial-
    light cream + serif italic + numbered sections. Reusing dark-navy would
    disconnect the video from the article it discusses.

  fonts:
    serif:  "Source Serif 4, Playfair Display, Georgia, serif"   # body + headlines
    sans:   "Inter, system-ui, sans-serif"                        # ui chrome only
    mono:   "JetBrains Mono, ui-monospace, monospace"             # filenames, overlines, numbers

  type_scale_overrides_long_form:
    hero_stat:        130px   # unchanged from template
    hero_headline:    100px   # serif weight 800, line-height 0.95
    hero_italic_accent: 100px # same size, italic, terracotta — the "of HTML" treatment
    section_overline_mono: 28px
    section_number_mono:   56px   # the big "01"/"02" in left margin
    section_h2_serif:      72px
    body_serif:            26px   # source uses larger body than the dark template
    card_title:            32px
    card_meta_mono:        18px

  per_scene_accent:
    scene_0_hook:               accent-1   # terracotta — single accent across the whole video
    scene_1_image_hero:         accent-1
    scene_2_side_by_side:       accent-1 + accent-3  # accent-3 (muted olive) on the "win" side only
    scene_3_stat_pill_row:      accent-1
    scene_4_source_cards:       accent-1
    scene_5_architecture_stack: accent-1
    scene_6_cta:                accent-1
```

## AI Image Prompts

None. Every visual asset is either a real screenshot from the article / Thariq's gallery, the project's own logo, or composed in pure HTML/CSS/SVG inside the scenes themselves.

## Screenshot Inventory

```yaml
screenshots:
  - name: article-cover
    file: assets/article-cover.png
    source: user-supplied screenshot of the X-post hero
    scene: scene_0_hook
    color_scheme: light
    usage: "Cold-open hero artifact (proves the article exists)"
    status: in_place

  - name: thariq-profile
    file: assets/thariq-profile.png
    source: user-supplied screenshot of @trq212 X profile
    scene: scene_6_cta
    color_scheme: light
    usage: "Author attribution chip in CTA scene"
    status: in_place

  - name: gallery-hero
    file: assets/source-pages/gallery-hero.png
    source: agent-browser capture of https://thariqs.github.io/html-effectiveness/ (above-the-fold)
    scene: scene_0_hook + scene_4_source_cards
    color_scheme: light
    usage: "Design ground truth + brief on-screen reveal in CTA"
    status: in_place

  - name: gallery-grid
    file: assets/source-pages/gallery-grid.png
    source: agent-browser capture (full page)
    scene: scene_4_source_cards
    color_scheme: light
    usage: "Background-card placement reference + brief social-proof flash"
    status: in_place

  - name: tile-spec-comparison
    file: assets/source-pages/tile-spec-comparison.png
    source: 01-exploration-code-approaches.html
    scene: scene_4_source_cards (use-case 1 illustration)
    usage: "Inset on the 'Specs & Planning' card"
    status: in_place

  - name: tile-pr-annotated
    file: assets/source-pages/tile-pr-annotated.png
    source: 03-code-review-pr.html
    scene: scene_4_source_cards (use-case 2 illustration)
    usage: "Inset on the 'Code Review' card"
    status: in_place

  - name: tile-design-system
    file: assets/source-pages/tile-design-system.png
    source: 05-design-system.html
    scene: scene_4_source_cards (use-case 3 illustration)
    usage: "Inset on the 'Design & Prototypes' card"
    status: in_place

  - name: tile-rate-limiter
    file: assets/source-pages/tile-rate-limiter.png
    source: 14-research-feature-explainer.html
    scene: scene_4_source_cards (use-case 4 illustration)
    usage: "Inset on the 'Reports & Research' card"
    status: in_place

  - name: tile-flag-editor
    file: assets/source-pages/tile-flag-editor.png
    source: 19-editor-feature-flags.html
    scene: scene_4_source_cards (use-case 5 illustration)
    usage: "Inset on the 'Custom Editors' card"
    status: in_place

  - name: tile-implementation-plan
    file: assets/source-pages/tile-implementation-plan.png
    source: 16-implementation-plan.html
    scene: scene_2_side_by_side
    usage: "Optional 'win' visual on the HTML side"
    status: in_place
```

## HyperFrames Blocks

```yaml
hyperframes_blocks_used: []   # everything is hand-rolled inside the scene archetypes; no registry blocks needed
```

## Fact-Check Audit

Every claim below must trace to `tmp/source.md` or to the user's two screenshots. Any claim without a source → REMOVED.

| Claim in plan | Source | Status |
|---|---|---|
| "Markdown has become the dominant file format used by agents" | source.md → article body, opening line | OK |
| "I've started preferring HTML as an output format" | source.md → opening, Thariq verbatim | OK |
| "Increasingly see this being used by others on the Claude Code team" | source.md → opening, Thariq verbatim | OK |
| "I find it difficult to read a markdown file of more than a hundred lines" | source.md → "Visual Clarity & Ease of Reading" | OK |
| "8 information types HTML can carry" (tables, CSS, SVG, code, JS+CSS interactions, workflows, spatial canvas, images) | source.md → "Information Density" bullet list | OK — verbatim |
| "ASCII diagrams or estimating colors with unicode characters" | source.md → "Information Density" closing | OK |
| "HTML can take 2-4x longer than Markdown" | source.md → FAQ "Doesn't this take longer to generate" | OK — verbatim |
| "1MM context window in Opus 4.7" | source.md → FAQ "Isn't it less token efficient" | OK — verbatim |
| "5 use cases" (Specs/Planning/Exploration, Code Review, Design/Prototypes, Reports/Research, Custom Editing Interfaces) | source.md → Use Cases section | OK — verbatim category names |
| "I attach a HTML code explainer to every PR I make now" | source.md → Code Review section | OK — verbatim |
| "Claude Design is based on HTML" | source.md → Design & Prototypes section | OK — verbatim |
| "Claude Code can find additional context using your MCPs (like Slack, Linear, etc.), your web browser (with Claude in Chrome), your git history" | source.md → Data Ingestion section | OK — verbatim |
| "More in the loop than ever before" | source.md → "Stay in the Loop" closing | OK — verbatim |
| "751K views, 2.7K likes, 341 reposts, 202 replies" | screenshot → article-cover.png | OK |
| "Thariq, Claude Code @ Anthropic, prev YC W20" | screenshot → thariq-profile.png | OK |
| Community-reaction themes | source.md → Community reactions block | OK — themes only, no individual handles |
| "If you want to learn more about AI, check out the dynamous.ai community" | locked outro per user memory `feedback_dynamous_short_outro.md` | OK |

**No claim removed.** All quoted lines stay verbatim.

## Notes for Composition Build

1. **Token override is the single biggest deviation from the template.** Write `videos/html-vs-markdown-claude-code/tokens/long-form.css` as a complete replacement (Task 11) before editing any scene file. Use the values in the "Token override" block above.

2. **Top banner**: the template ships an `anthropic-logo-light.svg` reference. Replace with a small mono wordmark — *"diy-yt-creator"* in JetBrains Mono 700 uppercase letterspaced 4px in `--accent-2`. No image, just type. Include the swap in the index.html edit step.

3. **Article cover shrink-to-thumbnail**: the cold open has the cover scale from 1.0 → 0.65 between t=10 and t=18 to make room for the headline. Use `back.out(1.4)` on scale, `power3.out` on `x` translation. Do NOT add rotation — the editorial aesthetic stays steady.

4. **Serif italic accent — the "effectiveness" treatment**: every scene with a major headline that contains an emphasis word should set that word in `<em>` and style as `font-style: italic; color: var(--accent-1);`. This is the visual signature Thariq's hero leans on, and reusing it across our scenes locks in the form-mirrors-content thesis.

5. **Numbered section chrome**: every scene's overline pairs a small-mono-cap label with a big "01" / "02" / … in the left margin (`position: absolute; left: 60px; top: same as overline`). The number is `--mono` 700 56px in `--accent-1`. Pair with a 1px horizontal divider (`border-bottom: 1px solid var(--border)`) immediately under the overline+H2 row, exactly like the source page.

6. **Card patterns**: scenes 1 (8 info types) and 4 (5 use cases) use a 3-column card grid mirroring the source page. Card spec: 28px radius, `var(--bg-card)` fill, 1px border `var(--border)`, no shadow (the source has no card shadows — keep it flat). Inner padding 32px. Title in serif 32px, meta in mono 18px in `--text-muted`. Each card reveals on its own narration anchor (step-by-step rule).

7. **The "01-exploration-code-approaches.html" mono filename appearing in the source**: include filename badges in the use-case cards (Scene 4) as a love-letter to the source page's exact treatment — `.html` files referenced directly. They also serve as visual anchors for the viewer.

8. **Audio bed**: narration-only (override the long-form template default). Comment out the bg-music elements per template README. Update `data-duration` on the narration `<audio>` to 480.

9. **Dynamous spoken outro**: locked verbatim — *"If you want to learn more about AI, check out the dynamous.ai community."* (Per user memory.) The endcard visual is a small handoff card with the community URL — no Werbung disclosure needed (long-form, not Shorts; that rule is per-format and Shorts-only).

10. **No SFX cues**: editorial tone. The scenes carry themselves on type + motion. If any beat feels under-dressed at preview, add a single subtle `cinematic-whoosh` at the title-slam moment (t=18) and the dynamous handoff (t=460) — but only if needed. Default ship: no SFX.

## Phase status

Phase 1 (this plan): **done 2026-05-09**.
Next phase: Phase 2 (script draft) — Task #4 in TaskList.
