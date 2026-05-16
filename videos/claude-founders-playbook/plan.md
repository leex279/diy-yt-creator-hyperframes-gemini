# Composition Plan: claude-founders-playbook

## Director's Summary

A 90-second Anthropic-dark-stage Short that reframes the freshly published 35-page Founder's Playbook as a unit-economics rewrite: Anthropic itself is warning that Claude Code helps founders **fail faster** unless they run the 4-stage discipline (Idea → MVP → Launch → Scale) and pick the right Claude surface (Chat / Cowork / Code) for each move. Hook opens on the playbook PDF as visual receipt, pivots into the 42% failure stat with a contrarian snapback, then walks the viewer through the compass, the decision table, and the Vulcan Tech receipt (4 months → state contract → $11M seed) before closing on a `CLAUDE.md` warning and a debate-sparking CTA. Visual anchor for the middle: the Chat/Cowork/Code decision table screenshot from PDF p.11. Visual anchor for the receipt: Vulcan stat pills.

## Template & Structure

- **Template**: `templates/shorts/anthropic` (V3 — operator-rebuilt 1220-line index.html, 15 phase archetypes available, 79s baseline that we extend to 90s)
- **Composition layout**: `inline-phase` + `mutex-visibility` (Anthropic V3 enforces this; no sub-compositions)
- **Resolution**: 1080×1920, 30fps, 90.0s `data-duration` on `#root`
- **Voice profile**: `news-explainer` — narrative-flow connectors mandatory between scenes
- **Persistent atmosphere (V3 defaults, kept)**: cinematic chrome (REC dot, timecode, viewfinder corners, letterbox, phase ticks), particle constellation field (30 dots + connecting lines), Anthropic shape backdrop (re-scatters on every phase transition per CLAUDE.md), token-stream edges, anamorphic flare (used ONCE on the Vulcan receipt slam), CSS film grain, soft-light scanlines
- **No background music** (Anthropic Shorts hard rule per `.claude/rules/audio-design.md`). Narration + SFX only.

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements (V3 archetype) |
|------|------------|----------------|-------------|------------------------------|
| 01 — Hook A: Topic lockup (THUMBNAIL-GRADE OPEN) | 0.0 | 3.0 | First frame is thumbnail-grade: "THE FOUNDER'S PLAYBOOK" 160px slam + Anthropic brand chrome + receipt "35 pages · May 2026" — frame is visible at t=0 with NO entrance fade | `hero-slam` archetype, topic lockup pattern (no entrance delay, fade out at 2.5s) |
| 01b — Hook B: 42% pain slam | 3.0 | 6.0 | "42% FAIL." in 240px orange with `.rgb-split` + sub: "and the playbook says that number is going to climb." | `hero-slam` archetype + chromatic split + impact frame |
| 02 — Krieger drop (annotated mockup / quote card) | 9.0 | 9.0 | Tweet-style social proof card with Krieger avatar + quote "I could have built Instagram with just myself and my co-founder." + Instagram cult-hop chip | V3 `quote-card` archetype (social-proof) |
| 03 — The 4-stage compass | 18.0 | 25.0 | Vertical 4-row stack: Idea → MVP → Launch → Scale. Each row enters ~6s apart with stage name (88px) + exit-criteria headline + matching Claude surface chip | V3 `timeline-cards` archetype (vertical orientation, SVG connector spine + traveling playhead, accent rotation orange/purple/blue/green) |
| 04 — Decision table | 43.0 | 14.0 | 3-column annotated mockup mirroring PDF p.11: Chat / Cowork / Code, each column reveals one beat at a time with "use when…" subline | V3 `feature-grid-2×3` archetype repurposed as 3-column annotated-mockup with `gsap-stagger-grid` |
| 05 — Vulcan receipt slam | 57.0 | 11.0 | Stat-pill row: "4 MONTHS · 3 FOUNDERS · 1 TECHNICAL · $11M SEED" with `gsap-counter-tween` on the 4 / 3 / 1 / 11; anamorphic flare fires once here | V3 `big-metric-badge` + `stat-pill-row` archetypes layered |
| 06 — CLAUDE.md warning | 68.0 | 11.0 | Code card with a `CLAUDE.md` file (~6 lines mono), glow pulse + marker-highlight on "five minutes of documentation per session is cheap insurance." | V3 `code-snippet` archetype with `marker-highlight` |
| 07 — CTA + thumbnail-grade close | 79.0 | 11.0 | Brand chrome top-left + dominant topic "RUN THE PLAYBOOK" (160px orange) + #cta-question 48px persistent + outcome receipt "4 stages · 3 surfaces · 1 founder" + URL/subscribe pill subordinate | V3 `cta-url-slam` archetype + thumbnail-grade frame holds the last ≥1.5s static |

**Total `data-duration`**: 90.0s (sum: 3 + 6 + 9 + 25 + 14 + 11 + 11 + 11 = 90).

## Narrative Arc

Kallaway formula mapped to the timeline:

1. **Context Lean-In (0.0 – 3.0s)** — Topic lockup. THIS IS THE THUMBNAIL: PDF receipt + brand. No question asked yet — just topic ownership for the YouTube auto-thumbnail pick.
2. **Scroll-Stop Interjection (3.0 – 9.0s)** — "BUT 42%." The stun gun is the stat itself; chromatic RGB split hits on "FAIL".
3. **Contrarian Snapback (9.0 – 18.0s)** — Krieger drop: a billion-dollar product would now ship with two people, and Anthropic just published the operating manual. Frames why this matters NOW.
4. **Solution (18.0 – 43.0s)** — 4-stage compass. The narrative spine of the Short. Each stage takes ~6s.
5. **Deep Dive (43.0 – 68.0s)** — Decision table (Chat/Cowork/Code) + Vulcan receipt. Two benefit-led features.
6. **Social Proof / Trust (Vulcan inside Deep Dive at 57.0 – 68.0s)** — Vulcan is both receipt AND trust beat.
7. **CTA + warning (68.0 – 90.0s)** — `CLAUDE.md` warning sets the stake for whoever ignores the discipline; CTA forces a stage-pick debate.

**News-explainer connectors** (mandatory per voice profile): each scene boundary carries a connector word to preview in Phase 2 — `because` (01→02), `which is why` (02→03), `so` (03→04), `because` (04→05), `and that's why` (05→06), `so` (06→07).

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Anthropic just published a 35-page playbook — and the first warning is that Claude Code will help you fail FASTER."
    layers_present: [1, 2, 4, 5]
    source_fidelity:
      source_quote: "Even before the current era of agentic coding, 42% of startups failed because they built something nobody wanted. Now, though, agentic coding solutions… that failure rate is only going to climb."
      head_nouns: ["playbook", "warning", "Claude Code", "you"]
      passes_gate: true
    advisory_score: 9.2

  variant_b:
    type: "stakes"
    opening_line: "42 percent of founders will still fail in 2026 — and the playbook everyone is downloading right now is the only reason that number isn't already 50."
    layers_present: [2, 3, 4, 5]
    source_fidelity:
      source_quote: "Even before the current era of agentic coding, 42% of startups failed because they built something nobody wanted… that failure rate is only going to climb."
      head_nouns: ["percent", "founders", "playbook", "number"]
      passes_gate: true
    advisory_score: 8.5

  variant_c:
    type: "number"
    opening_line: "Three Claude products. One 35-page playbook. Forty-two percent of founders are still about to fail."
    layers_present: [3, 4, 5]
    source_fidelity:
      source_quote: "Even before the current era of agentic coding, 42% of startups failed because they built something nobody wanted."
      head_nouns: ["products", "playbook", "percent", "founders"]
      passes_gate: true
    advisory_score: 7.6

  recommended: "variant_a"
```

**Scoring math** (Variant A): Curiosity 9 (single sentence creates immediate gap — "help you fail FASTER" is a contradiction), Stakes 9 (specific + quantified upside on the resolution), Specificity 9 (35-page, named tool, "FAIL"), Value Alignment 1 (names the playbook in line 1), Stun Gun +0.1 (no but/however/yet — set to +0.0; the contradiction "help you fail" carries the stun without the word), Promise +1 (implicit "here's the map"), Narrative Flow +0.5 (explanatory connector "and" + "is that"). `base = (9×0.4 + 9×0.4 + 9×0.2) = 9.0`. Final = `min(10, 9.0 + 0 + 1 + 0 + 0.5) ≈ 9.2`. Highest of the three → autonomously selected.

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "ContrastPivot"      # build context (playbook is real) → smash cut → contrarian reveal (you'll still fail)
  selected_variant: "variant_a"

  visual_beats:
    - beat: "Thumbnail-grade topic lockup (FIRST FRAME)"
      timing_s: [0.0, 2.5]
      visual: "Anthropic wordmark top-center · 'THE FOUNDER'S PLAYBOOK' 160px slam mid-frame · 'May 2026 · 35 pages' mono receipt under the slam · NO entrance fade — elements at full opacity at t=0 so YouTube auto-thumbnail picks this"
      gsap_ease: "n/a (static at t=0)"
      sfx: null
    - beat: "Fade-out to context lean-in"
      timing_s: [2.4, 3.0]
      visual: "Topic lockup fades to opacity 0.0 (duration 0.5)"
      gsap_ease: "sine.inOut"
      sfx: "cinematic-whoosh @ t=3.0"
    - beat: "42% FAIL slam (CONTRARIAN PIVOT)"
      timing_s: [3.0, 5.5]
      visual: "Pure black flash 60ms → 'BUT.' 200px mono overline → '42% FAIL' 240px orange slam with .rgb-split for 0.25s on impact frame → sub 'and the playbook says it's CLIMBING' fades in"
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake + glitch-zap (separate tracks)"
    - beat: "Pain hold — counter ticks"
      timing_s: [5.5, 9.0]
      visual: "Counter rolls 0 → 42 via gsap-counter-tween, % suffix lands hard; small mono caption pill 'CB Insights × Anthropic Founder's Playbook p.10' enters from below at t=7.2s"
      gsap_ease: "expo.out (counter), power3.out (caption)"
      sfx: null

  pivot_word: "BUT"
  brand_reveal_word: "PLAYBOOK"   # appears in t=0 topic lockup; reinforced in narration

  assets_needed:
    - type: "logo"
      description: "Anthropic wordmark (already in templates/shorts/anthropic/assets/)"
      source: "videos/claude-founders-playbook/assets/anthropic-logo-light.svg (copied on spawn)"
    - type: "screenshot"
      description: "PDF page 1 (cover) — small thumbnail visible in topic lockup as 'receipt' chip"
      source: "Render from videos/claude-founders-playbook/research/source-playbook.pdf p.1"
    - type: "screenshot"
      description: "PDF page 11 — Chat/Cowork/Code decision table (Scene 04 visual anchor)"
      source: "Render from videos/claude-founders-playbook/research/source-playbook.pdf p.11"
    - type: "logo"
      description: "5 founder logos: HumanLayer, Ambral, Vulcan, Carta Healthcare, Anything (used as small chips in compass + receipt scenes)"
      source: "TBD — capture in composition build (shared/logos/ may have some)"

  sfx_cues:
    - beat: "Topic lockup hold"
      cues: []                              # silence under narration intro
    - beat: "Hook B pivot (t=3.0)"
      cues: [cinematic-whoosh]              # phase transition whoosh, fires AT t=3.0
    - beat: "42% FAIL slam (t=3.6)"
      cues: [impact-slam, screen-shake, glitch-zap]   # layered on tracks 3/4/5
    - beat: "Scene 02 → 07 transitions (t=9, 18, 43, 57, 68, 79)"
      cues: [cinematic-whoosh]              # one whoosh per transition, AT sceneT
    - beat: "Compass card entrances (Scene 03)"
      cues: [spring-pop]                    # one per card, 4 total
    - beat: "Decision-table column entrances (Scene 04)"
      cues: [pop]                           # one per column, 3 total
    - beat: "Vulcan stat-pill row (Scene 05)"
      cues: [scale-slam]                    # ONE big stat-slam for the whole row; restraint per Anthropic SFX rule
    - beat: "CLAUDE.md marker (Scene 06)"
      cues: [strike-cross]                  # accent on the marker-highlight sweep

  music_profile:
    hook_mood: "NONE"   # template forbids background music on Shorts
    note: "Anthropic Shorts hard rule — no BG music. Narration + SFX only."
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 01b (Hook B — 42% FAIL slam)"
    setup_line: "Anthropic just published a 35-page playbook — and the first warning is that Claude Code will help you fail FASTER."
    resolution_scene: "Scene 05 (Vulcan receipt)"
    resolution_line: "Vulcan: four months, three founders, one technical — beat the consulting firms. Eleven million dollar seed. The discipline works."
    type: "tension"

  loop_openers:
    - scene: "Scene 03 (compass)"
      position: "opening"
      phrase: "Because Anthropic remapped startup-building into four stages."
    - scene: "Scene 05 (Vulcan)"
      position: "transition"
      phrase: "Here's what running the playbook actually looks like."
```

## Story Lock Placement

- **Term Branding (Lock #1)**: Scene 03 introduces "the 4-stage compass" as the coined frame for the Short. Phase 2 should treat this phrase as the term we own.
- **Loop Openers (Lock #5)**: Scene 03 ("Because Anthropic remapped…") + Scene 05 ("Here's what running the playbook actually looks like.")
- **Negative Frame (Lock #4)**: Scene 06 — "No CLAUDE.md = your codebase eventually collapses." (Negative reframe of the discipline, AFTER the hook — never IN the hook.)
- **Thought Narration (Lock #3)**: Scene 02 (post-Krieger drop) — "Mike Krieger said that out loud. Anthropic just made it operational."

## Composition Layout

```yaml
composition_layout:
  structural: "inline-phase + mutex-visibility"
  template: "templates/shorts/anthropic"
  total_phases: 8           # phases 1a, 1b, 2, 3, 4, 5, 6, 7
  shape_backdrop_reposition: true   # rearranges per phase per CLAUDE.md default
  particle_field: "kept (V3 default)"
  anamorphic_flare: "fire ONCE on Vulcan slam (Scene 05 @ t≈57.5)"
  cinematic_chrome: "kept (REC, timecode, viewfinder corners, letterbox, phase ticks 01/08 → 08/08)"
  thumbnail_grade_frames:
    first_frame: "Scene 01 topic lockup — visible at t=0 with no entrance fade"
    last_frame: "Scene 07 CTA + close — held still ≥1.5s after t=88.5, dominant 'RUN THE PLAYBOOK' 160px topic + brand + outcome + #cta-question persistent"
```

## Retention Component Picks

```yaml
retention_component_picks:
  scene_01_hook_a_topic_lockup:
    pattern: "hero-slam"
    primitives:
      - "inline-phase + mutex-visibility"
      - "gsap-stagger-grid"           # subtle stagger on overline → slam → receipt at t=0 (instant, not animated; thumbnail-grade)
    markers: []                       # NONE in scene 01 — clean topic lockup
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_01b_hook_b_pain_slam:
    pattern: "hero-slam"
    primitives:
      - "inline-phase"
      - "gsap-counter-tween"          # 0 → 42 ticker on the % stat
      - "marker-highlight"            # on the word 'CLIMBING' in the sub
    markers: 1
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_02_krieger_quote:
    pattern: "quote-card"             # V3 archetype
    primitives:
      - "inline-phase"
      - "gsap-stagger-grid"           # avatar → name → quote → engagement counts
      - "gsap-counter-tween"          # engagement stats tick up (likes / reposts / views)
    markers: 0
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_four_stage_compass:
    pattern: "timeline-cards"         # V3 archetype, vertical orientation
    primitives:
      - "inline-phase"
      - "gsap-path-draw"              # SVG connector spine drawn top-to-bottom (Idea→MVP→Launch→Scale)
      - "gsap-stagger-grid"           # 4 cards step-by-step (~6s apart per step-by-step-reveal rule)
      - "marker-highlight"            # on the stage-name word the narrator emphasizes (max 1; pick 'LAUNCH')
    markers: 1
    captions: null                    # narration carries the labels; captions would over-density
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_04_decision_table:
    pattern: "feature-grid-2x3"       # V3 archetype repurposed as 3-column
    primitives:
      - "inline-phase"
      - "gsap-stagger-grid"           # 3 columns enter one beat at a time
      - "marker-circle"               # on the Claude Code column header (the one the viewer probably DEFAULTS to wrong)
    markers: 1
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_05_vulcan_receipt:
    pattern: "stat-pill-row + big-metric-badge"
    primitives:
      - "inline-phase"
      - "gsap-counter-tween"          # 0→4, 0→3, 0→1, 0→11 (the $11M counts via formatter)
      - "anamorphic flare"            # V3 helper, fires ONCE here only — this is THE impact moment
      - "marker-highlight"            # on 'beat the consulting firms' sub
    markers: 1
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_06_claude_md_warning:
    pattern: "code-snippet"           # V3 archetype
    primitives:
      - "inline-phase"
      - "gsap-typewriter"             # CLAUDE.md file types in line-by-line (~6 lines)
      - "marker-highlight"            # on 'five minutes' in the warning sub
    markers: 1
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_07_cta_close:
    pattern: "cta-url-slam"           # V3 archetype + thumbnail-grade close
    primitives:
      - "inline-phase"
      - "gsap-stagger-grid"           # brand + topic + outcome + #cta-question + URL pill enter in 0.5s stagger
      - "marker-circle"               # on the URL/handle text (subordinate to topic slam)
    markers: 1
    captions: null
    audio_reactive: "audio-reactive-glow on #cta-question (subtle, treble band, ≤6% scale variation)"
    transition_out: null              # final scene — holds for ≥1.5s thumbnail-grade hold
```

**Retention component pick counts**:
- Markers: 6 total across the short (max 2/scene cap respected — every scene with markers has ≤1)
- Captions: 0 (none — narration density is already high; on-screen text carries the load)
- Audio-reactive: 1 (subtle treble glow on `#cta-question` only)
- Transitions: 1 primary (`blur-crossfade`) used on all 6 mid-cuts; no accent transition needed at this length
- GSAP effects: 8 (typewriter ×1, counter-tween ×4 instances, stagger-grid ×7, path-draw ×1, marker variants ×6)

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene_01_hook_a_topic_lockup"
    data_start: 0.0
    data_duration: 3.0
    audio_anchor: "narration starts at ~0.4s with 'Anthropic just published…'"
  - scene: "scene_01b_hook_b_pain_slam"
    data_start: 3.0
    data_duration: 6.0
    audio_anchor: "'42%' spoken at ~3.6s; 'climbing' at ~7.5s"
  - scene: "scene_02_krieger_quote"
    data_start: 9.0
    data_duration: 9.0
    audio_anchor: "Krieger name spoken at ~9.6s; Instagram name at ~12.0s"
  - scene: "scene_03_four_stage_compass"
    data_start: 18.0
    data_duration: 25.0
    audio_anchor: "'Idea' at ~19.0s; 'MVP' at ~24.8s; 'Launch' at ~30.6s; 'Scale' at ~36.4s; outro line at ~41.0s"
  - scene: "scene_04_decision_table"
    data_start: 43.0
    data_duration: 14.0
    audio_anchor: "'Chat' at ~44.0s; 'Cowork' at ~48.0s; 'Claude Code' at ~52.0s"
  - scene: "scene_05_vulcan_receipt"
    data_start: 57.0
    data_duration: 11.0
    audio_anchor: "'four months' at ~58.0s; 'eleven million' at ~63.5s"
  - scene: "scene_06_claude_md_warning"
    data_start: 68.0
    data_duration: 11.0
    audio_anchor: "'CLAUDE.md' spelled at ~69.0s; 'five minutes' at ~73.5s"
  - scene: "scene_07_cta_close"
    data_start: 79.0
    data_duration: 11.0
    audio_anchor: "CTA question spoken at ~80.5s; final beat lands at ~85.5s; ≥1.5s static hold to t=90"
total_data_duration: 90.0
```

`audio_anchor` values are PLACEHOLDERS. Phase 3.5 retimes them to word-level transcript anchors after TTS.

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []                       # no brand overrides; use Anthropic palette as-is
  accent_rotation:
    - scene_01_hook_a:   "orange"     # topic lockup
    - scene_01b_hook_b:  "orange"     # same accent for both halves of the hook (single 'phase 1' identity)
    - scene_02_krieger:  "purple"     # quote-card calm tone
    - scene_03_compass:  "rotation"   # Idea=orange, MVP=purple, Launch=blue, Scale=green (matches stage-energy progression)
    - scene_04_decision: "blue"       # tech/decision-tree colorway
    - scene_05_vulcan:   "orange"     # hero receipt — primary slam color
    - scene_06_claude_md:"green"      # code/positive reinforcement
    - scene_07_cta:      "orange"     # CTA URL primary
  no_adjacent_same_accent: true       # verified — adjacent pairs are (orange,orange same-phase ok), (orange,purple), (purple,rotation), (rotation,blue), (blue,orange), (orange,green), (green,orange)
  fonts:
    sans: "Inter"
    mono: "JetBrains Mono"
```

## AI Image Prompts

None. All visuals come from PDF screenshots, the founder logos, and synthesized HTML/CSS (counters, code cards, decision-table columns).

## Screenshot Inventory

```yaml
screenshots:
  - name: "playbook-cover-thumbnail"
    source: "videos/claude-founders-playbook/research/source-playbook.pdf p.1"
    scene: "scene_01_hook_a_topic_lockup"
    color_scheme: "mixed"
    usage: "Small receipt-chip thumbnail inside the topic lockup (proves it's a real publication)"
  - name: "decision-table-p11"
    source: "videos/claude-founders-playbook/research/source-playbook.pdf p.11"
    scene: "scene_04_decision_table"
    color_scheme: "light-on-dark-after-crop"
    usage: "Anchored behind the synthesized 3-column card — provides authority via real visual receipt"
  - name: "anthropic-blog-hero"
    source: "https://claude.com/blog/the-founders-playbook"
    scene: "scene_01_hook_a_topic_lockup"
    color_scheme: "dark"
    usage: "OPTIONAL secondary receipt under the playbook cover (only if topic lockup space allows)"
```

Screenshot capture happens in Phase 4 (composition build), not here.

## HyperFrames Blocks

```yaml
hyperframes_blocks_used: []
```

The V3 template already provides every archetype we need natively. No registry blocks required (the template's `quote-card`, `code-diff`, `timeline-cards`, etc. cover all 7 scenes).

## Fact-Check Audit

| # | Claim | Scene | Source URL | Status |
|---|-------|-------|------------|--------|
| 1 | Anthropic published a 35-page founder's playbook | 01a | https://claude.com/blog/the-founders-playbook + research/source-playbook.pdf (cover) | SOURCED |
| 2 | "42% of startups failed because they built something nobody wanted" + "that failure rate is only going to climb" | 01b | research/source-playbook.txt line 181-184 (PDF p.10) + https://www.cbinsights.com/research/report/startup-failure-reasons-top/ | SOURCED — exact wording from PDF |
| 3 | Mike Krieger "I could have built Instagram with just myself and my co-founder" | 02 | https://www.buildmvpfast.com/blog/one-person-unicorn-ai-agents-solo-founder-billion-dollar-2026 (surfaced via public statements) | **REPHRASE-WITH-ATTRIBUTION** — Phase 2b must verify primary source OR swap for the playbook's own "founder as orchestrator" framing. Plan-level note: use "Mike Krieger said publicly that…" framing, NOT direct quotation marks, unless primary source confirmed |
| 4 | 4-stage remap: Idea / MVP / Launch / Scale | 03 | research/source-playbook.txt line 10-16, 48-49 (PDF TOC + intro) | SOURCED |
| 5 | Each stage has goals + exit criteria + failure modes | 03 | research/source-playbook.txt line 152-167 (PDF p.8+ pattern repeats for each stage) | SOURCED |
| 6 | Chat / Claude Cowork / Claude Code decision table on PDF p.11 | 04 | research/source-playbook.txt line 215-222 + PDF p.11 directly | SOURCED |
| 7 | Vulcan Technologies: 4 months, 3 founders, 1 technical, $11M seed, beat consulting firms | 05 | https://claude.com/blog/building-companies-with-claude-code (PDF references Vulcan Technologies S25 on line 913) | SOURCED — Phase 2b must verify the $11M seed figure against the linked blog post |
| 8 | `CLAUDE.md` as persistent project memory + "five minutes of documentation per session is cheap insurance" | 06 | research/source-playbook.txt (PDF p.16 — agentic technical debt section) | SOURCED — exact wording "five minutes" is from the PDF |
| 9 | "Codebase inevitably collapses" without CLAUDE.md | 06 | research/source-playbook.txt (PDF p.16) | SOURCED |
| 10 | Sean Ellis test 40% threshold | (cut from plan to save time) | research/source-playbook.txt line 496-497 | **OMITTED** — kept in brief's "Could Include"; trimmed for 90s budget |
| 11 | Anthropic ~90% Claude code AI-written | (cut from plan) | Anthropic engineering posts — no single canonical URL | **OMITTED** — flagged in brief as unverifiable single-source; not used to keep audit tight |

**Audit summary**: 8 of 8 used claims sourced. 1 claim (Krieger quote, #3) flagged for Phase 2b primary-source verification — Phase 2 script should default to attributed paraphrase ("Mike Krieger said publicly…") unless a primary source is found. 2 nice-to-have claims (#10 Sean Ellis, #11 90% AI-written) explicitly omitted for tightness and to avoid an unverifiable single-source stat in-screen.

## Notes for Composition Build

1. **Thumbnail-grade first frame is non-negotiable**. Scene 01a must render at full opacity at t=0 (no fade-in, no entrance animation) so the YouTube auto-thumbnail pick is the topic + brand + receipt, not a black frame.
2. **Thumbnail-grade last frame**: Scene 07 must finish all entrances by t≈80.5s and hold static from t≈88.5–90.0. Dominant element is "RUN THE PLAYBOOK" 160px orange topic slam, NOT the URL pill. `#cta-question` persists through this final hold.
3. **Engagement CTA wording** (per `.claude/rules/engagement-cta.md`): The on-screen `#cta-question` in Scene 07 carries: **"Running this playbook — or still validating with vibes?"** This is binary-or-short-list answerable, polarizing (vibes-vs-discipline framing), references the playbook's specific contrarian claim, and low-cost to answer (any founder can pick a side in 3 seconds). The same wording must appear in the narration's final 3-5s AND in `youtube-description.md`'s closing paragraph.
4. **Step-by-step reveal rule** (`.claude/rules/step-by-step-reveal.md`): Scene 03's four stages enter ~6.0s apart, NOT in a quick stagger. Scene 04's three decision-table columns enter ~3.5s apart. Scene 05's four stat pills (4 / 3 / 1 / $11M) enter ~2s apart (acceptable quick-stagger since narration genuinely names them in one sentence).
5. **Visual pacing 5s rule** (`.claude/rules/visual-pacing-5s.md`): Scenes 03 (25s long) and 06 (11s long) are the highest risk. For Scene 03, the entrances are paced ~6s — add ONE sub-beat between Launch and Scale (a marker-highlight on "every decision goes through you" at t≈38.0s) to keep the gap ≤5s. For Scene 06, after the typewriter completes at t≈73s, add a glow pulse on the CLAUDE.md filename header at t≈76s.
6. **Hidden-until-reveal pattern** (`.claude/rules/step-by-step-reveal.md`): Every stage card / decision column / stat pill must use explicit `tl.set({..., opacity: 0}, 0)` at t=0 + `tl.to({..., opacity: 1}, ...)` at reveal time. Never `tl.from()` at a late timestamp without `immediateRender: false`.
7. **Shorts typography minimums** (`.claude/rules/shorts-typography.md`): Stage names 88px+, exit-criteria headlines 56px+, decision-column "use when…" 32px+, Vulcan stat numbers 200px (hero stat), Krieger quote text 52px+, CLAUDE.md code lines 36px (mono), `#cta-question` 48px+, CTA "RUN THE PLAYBOOK" 160px.
8. **TTS heteronym pre-audit** (`.claude/rules/tts-pronunciation.md`): Watch for "lead" (rewrite to "primary"), "live" (rewrite to "shipping"), `CLAUDE.md` (spell as "claude dot M D"), `MVP` ("M V P"), `MCP` (if it appears — "M C P"). Pre-flagged in brief's TTS table.
9. **Screenshot-anchor markers** (`.claude/rules/screenshot-anchor-markers.md`): When the PDF p.11 decision-table screenshot anchors Scene 04, do NOT overlay horizontal-bar marker-highlights on top of the table's existing rows. Use a marker-circle on the column header instead.
10. **Whoosh timing** (`.claude/rules/audio-design.md`): Every `cinematic-whoosh` `data-start` = sceneT exactly (not sceneT − 0.4). `data-duration` = 1.5s. Six whooshes total at t=3.0, 9.0, 18.0, 43.0, 57.0, 68.0, 79.0.
11. **Anamorphic flare**: Fire ONCE in the whole composition, at Scene 05 t≈57.5 (the Vulcan slam impact frame). Per V3 design system — use sparingly.
12. **No background music** — Anthropic Shorts hard rule. Skip Phase 3.2 music generation entirely for this video.
