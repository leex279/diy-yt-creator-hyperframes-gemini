# Composition Plan: claude-for-small-business

## Director's Summary

A 180-second Anthropic-branded news-explainer Short that positions **Claude for Small Business** as a wedge-product launch — not a new model, but a bundle of 15 pre-wired workflows + 15 reusable skills that lives inside the tools SMBs already pay for (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365). The arc opens on the universal Sunday-night payroll scramble pain (lifted verbatim from Anthropic's own companion demo), pivots into the 15+15 receipt, embeds Anthropic's own 29-second product demo as proof, lands a Lina Ochman quote that contrasts SMB-fit against enterprise AI, and closes on a Copilot-vs-Claude debate-CTA framed against the specific claim of the video. First frame and last frame are both thumbnail-grade per `shorts-thumbnail-frames.md` — the entry tile and the loop-pause tile both communicate topic + brand + receipt + outcome in under a second.

---

## Template & Structure

- **Template**: `templates/shorts/anthropic` — dark-stage Anthropic aesthetic, 1080×1920, 30fps
- **Layout model**: `inline-phase` + `mutex-visibility` (template-enforced — 9 phases including the dedicated thumbnail-grade first hold and a dedicated thumbnail-grade close)
- **Design tokens**: `tokens/anthropic-dark.css` (verbatim — orange #E97458 / purple #A78BFA / blue #6B9AEF / green #7DD3A6)
- **Background music**: NONE (Anthropic Shorts template forbids it — narration + SFX only)
- **Voice profile**: `news-explainer` (per `.claude/references/brand-voice-news-explainer.md`) — every scene transition needs an explanatory connector (`because`, `why`, `to`, `here's why`)

---

## Master Timeline

| # | Scene                          | data_start | data_duration | Visual Goal                                                                                  | Key Elements                                                                                       |
|---|--------------------------------|-----------:|--------------:|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 1 | Thumbnail-grade hook hold      |       0    |        6      | First frame = YouTube auto-thumbnail. "CLAUDE FOR SMB" 160px topic slam + Anthropic mark + outcome receipt | Topic lockup (visible from t=0), Anthropic logo, outcome line "15 workflows. 15 skills. Just shipped." |
| 2 | The Sunday-night scramble      |       6    |       22      | 5 browser tabs flicker open frenetically → slam-cut to single `/plan-payroll` Claude prompt  | Tab cluster reveal step-by-step, slam-cut, kinetic caption "will I make payroll?"                  |
| 3 | The reveal: 15 + 15            |      28    |       24      | Dual-counter pair (15 workflows / 15 skills) with named-skill chips revealing step-by-step   | Two stat-pill counters tick 0→15, then 6 chip rows reveal one at a time (5s spacing)              |
| 4 | Integration constellation      |      52    |       22      | 7 partner logos orbiting central Claude mark, each connects with a glowing edge one at a time | QB, PayPal, HubSpot, Canva, DocuSign, GW, MS365 partner logos, hub-spoke reveals                  |
| 5 | The companion demo embed       |      74    |       32      | Anthropic's own 29s YT clip plays inside a phone-frame; closes with thumbnail-grade pointer  | `assets/clips/anthropic-clip.mp4` in centered horizontal pane, then 2s held pointer to description |
| 6 | The Lina Ochman quote          |     106    |       18      | Quote card with three business-type chips reveal one-at-a-time (HVAC, landscaper, brokerage) | Lina Ochman headshot/wordmark, Anthropic mark, three chip-pops                                    |
| 7 | The article screenshot proof   |     124    |       16      | `article-hero.png` (625×800) centered with marker highlights on key headline                  | Centered screenshot card, marker-sweep on "small business" + scale-pulse on date                  |
| 8 | Trust + customer proof         |     140    |       22      | 3-logo customer strip + approval-required + no-training trust beat                            | Purity/Simple Modern/MidCentral customer rows, Daniela Amodei lower-third cite                    |
| 9 | CTA + thumbnail-grade close    |     162    |       18      | Topic slam + Dynamous pointer + debate CTA question — held still as last-frame thumbnail     | "15 + 15 SHIPPED" 160px slam, Anthropic mark, "Sunday-night payroll → 5 min" receipt, debate-CTA  |
|   | **TOTAL**                      |            |  **180.0**    |                                                                                              |                                                                                                    |

---

## Narrative Arc (Kallaway Formula)

1. **Hook — Context Lean-In** (Scenes 1-2, 28s, 15.5%): Thumbnail-grade first frame establishes brand+topic at t=0 (so YouTube auto-thumbnail picks it). Then the universal pain — "every owner asks before payday: will I make it?" — with the 5-tab scramble visual.
2. **Scroll-Stop Interjection** (Scene 2 → 3 boundary): "But Anthropic just shipped something that answers it in 5 minutes." — explicit "But" pivot at t≈26s.
3. **Contrarian Snapback** (Scene 3): "It's not a new model — it's a bundle." 15 workflows + 15 skills, the Lego brick framing.
4. **Solution** (Scene 4, 22s, 12%): Integration constellation — Claude wires into the tools SMBs already pay for, not a chat window they bolt on.
5. **Deep Dive** (Scenes 5-7, 66s, 37%): The companion demo (proof Anthropic published themselves), the Lina Ochman quote ("not for the 15-person HVAC..."), the article screenshot proof.
6. **Social Proof / Trust** (Scene 8, 22s, 12%): Three customer logos, Daniela Amodei top-of-house cite, approval-required + no-training trust beat.
7. **CTA** (Scene 9, 18s, 10%): Debate-CTA question + Dynamous spoken pointer + thumbnail-grade close.

**Connector words (news-explainer profile)**:
- Scene 1 → 2: (silent transition — opens on pain)
- Scene 2 → 3: **"But"**
- Scene 3 → 4: **"And"** (these tools live inside…)
- Scene 4 → 5: **"Here's what it actually looks like"**
- Scene 5 → 6: **"Because"** (this isn't a generic AI…)
- Scene 6 → 7: **"And"** (the receipts back it up)
- Scene 7 → 8: **"Plus"** (the trust beat)
- Scene 8 → 9: **"So"** (the question)

---

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Anthropic just shipped Claude for Small Business — and it's not a new model."
    layers_present: [1, 4, 5]
    source_fidelity:
      source_quote: "Today, we're introducing Claude for Small Business... a new way to bring AI to the place small businesses spend most of their time — inside the tools they already use."
      head_nouns: ["Anthropic", "Claude for Small Business", "model"]
      passes_gate: true
    advisory_score: 7.6

  variant_b:
    type: "stakes"
    opening_line: "Every owner asks the same question the week before payday — will I make it?"
    layers_present: [2, 4, 5]
    source_fidelity:
      source_quote: "Every owner asks the same question the week before payday — will I make it?" (verbatim from companion video lserpKbUDjc 0:06)
      head_nouns: ["owner", "question", "payday"]
      passes_gate: true
    advisory_score: 8.6

  variant_c:
    type: "number"
    opening_line: "44% of the US economy just got an AI worker — 15 pre-built workflows for small business."
    layers_present: [3, 4, 5]
    source_fidelity:
      source_quote: "Small businesses... account for nearly 44% of US GDP."
      head_nouns: ["economy", "AI worker", "workflows", "small business"]
      passes_gate: true
    advisory_score: 7.8

  recommended: "variant_b"
```

**Scoring rationale**:
- **Variant B** wins (8.6) — universal SMB pain anchor, sourced verbatim from Anthropic's own demo (zero fabrication risk), narrative-flow bonus on the connector ("the week before payday"), promise bonus carried by the implicit "watch to find the answer."
- Variant A scores lower because the negative-framed counterintuitive ("it's not a new model") works mid-video as a contrarian snapback (now planned for Scene 3) but doesn't earn the click in line one.
- Variant C scores well on specificity but the 44% GDP stat is abstract — viewers don't emotionally connect with "the economy" the way they do with "will I make payroll."

---

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "FilmTrailer"
  selected_variant: "variant_b"

  visual_beats:
    - beat: "Cold Open (Thumbnail hold)"
      timing_s: [0, 6]
      visual: "Topic lockup visible from t=0: 'CLAUDE FOR SMB' 160px slam, Anthropic mark top-left, outcome receipt 'Sunday-night payroll → 5 min'. No entrance animation — full opacity at t=0 so YouTube auto-thumbnail picks it."
      gsap_ease: "tl.set() at t=0"
      sfx: null

    - beat: "Thumbnail fade-out → pain"
      timing_s: [5.5, 8]
      visual: "Thumbnail lockup fades out (0.5s) as 5-browser-tab scramble fades in. Tab icons (QuickBooks / PayPal / Gmail / bank / payroll) cascade-stagger over 1s."
      gsap_ease: "power3.out"
      sfx: "cinematic-whoosh (phase transition)"

    - beat: "Context — the Question"
      timing_s: [8, 18]
      visual: "Tab cluster now visible. Caption 'will I make payroll?' marker-sweeps in at t=14s. Tabs subtly jitter to imply chaos."
      gsap_ease: "power4.out"
      sfx: "impact-slam at 14s (caption land)"

    - beat: "PIVOT — But Anthropic"
      timing_s: [26, 27]
      visual: "White flash crossfade (cinematic-whoosh + screen-shake). Slam-cut: tab cluster vanishes, single `/plan-payroll` prompt slams in 240px."
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake + cinematic-whoosh (own tracks)"

    - beat: "Brand reveal (15 + 15)"
      timing_s: [28, 36]
      visual: "Dual-counter pair (15 workflows / 15 skills) counters tick 0→15 with scale-slam each."
      gsap_ease: "elastic.out(1, 0.5)"
      sfx: "scale-slam (x2, one per counter)"

    - beat: "Rapid-Fire (skill chips reveal)"
      timing_s: [36, 50]
      visual: "Six named-skill chips reveal one at a time, ~2s apart: invoice chaser → margin analyzer → month-end prepper → tax-season organizer → contract reviewer → lead triager"
      gsap_ease: "back.out(1.5) with stagger"
      sfx: "spring-pop per chip (6 cues)"

  pivot_word: "But"
  brand_reveal_word: "Anthropic"

  assets_needed:
    - type: "logo"
      description: "Anthropic light-on-dark wordmark for top banner + final-frame brand chrome"
      source: "../../shared/logos/anthropic-logo-light.svg (already in repo)"
    - type: "video"
      description: "29s companion demo embed"
      source: "assets/clips/anthropic-clip.mp4 (already captured)"
    - type: "screenshot"
      description: "Anthropic announcement article hero crop"
      source: "assets/screenshots/article-hero.png (already captured, 625×800)"
    - type: "logo"
      description: "Partner logos for integration constellation (Scene 4) — QB, PayPal, HubSpot, DocuSign, Workspace, M365"
      source: "MISSING from shared/logos/ — flagged below as composition-build gap. Canva + Google + Microsoft already exist."
    - type: "logo"
      description: "Customer logos for Scene 8 — Purity Coffee, Simple Modern, MidCentral Energy"
      source: "MISSING from shared/logos/ — composition build pulls from each company's press kit or substitutes text-only treatment if blocked"

  music_profile:
    hook_mood: NONE   # template forbids background music on Shorts
    hook_bpm: null
    body_bpm: null
    cta_bpm: null
```

---

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 02 (Sunday-night scramble)"
    setup_line: "Every owner asks the same question the week before payday — will I make it?"
    resolution_scene: "Scene 05 (companion demo)"
    resolution_line: "Five minutes. You go into payday knowing the number, not guessing."
    type: "question"

  loop_openers:
    - scene: "Scene 03"
      position: "opening"
      phrase: "And it's not a new model."
    - scene: "Scene 05"
      position: "opening"
      phrase: "Here's what it actually looks like."
    - scene: "Scene 06"
      position: "opening"
      phrase: "Because this isn't built for the Fortune 500."
```

---

## Story Lock Placement

- **Term Branding (Lock #1)** — Scene 3: "the 15 + 15 bundle" as the coined frame. Used again in Scene 9 close.
- **Loop Openers (Lock #5)** — Scenes 3, 5, 6 (cadence ~25-30s, see open_loop_architecture above)
- **Negative Frame (Lock #4)** — Scene 4 ("Generic ChatGPT can't see your QuickBooks. Microsoft Copilot only sees Microsoft.") — frames the competitor problem before the Claude solution.
- **Thought Narration (Lock #3)** — Scene 5 (after demo runs): "If you've ever opened that many tabs on a Friday, you know exactly what just happened in those five minutes."

---

## Composition Layout

```yaml
composition_layout:
  model: "inline-phase + mutex-visibility"
  template_path: "templates/shorts/anthropic"
  total_phases: 9
  phase_pattern: "P1 → T1 → P2 → T2 → ... → P9"
  resolution: "1080x1920"
  fps: 30
  music_track: null     # template-banned on shorts
```

---

## Retention Component Picks

```yaml
retention_component_picks:
  scene_01_thumbnail_hook:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam (modified — no entrance animation; all elements at t=0 opacity 1)"
    primitives:
      - "gsap-stagger-grid"   # only used on the FADE-OUT at t=5.5
    captions: null            # too short for synced captions
    audio_reactive: null      # no narration in this beat
    transition_out: "blur-crossfade"
    micro_beats_to_satisfy_5s_rule: "Single 6s static hold. EXEMPT per shorts-thumbnail-frames.md (opening thumbnail hold ≤2.5s relaxation — extended here to 5.5s held + 0.5s fade because no narration plays underneath. Acceptable variation flagged in notes.md)."

  scene_02_sunday_scramble:
    structural: "inline-phase"
    pattern: "hero-slam (custom — 5-tab grid + slam-cut)"
    primitives:
      - "gsap-stagger-grid"        # 5 browser tabs cascade in
      - "marker-highlight"          # sweep under "will I make payroll?"
      - "gsap-counter-tween"        # subtle clock-spin on tab corner
    captions: "caption-fade-slide"  # for the narrated question
    audio_reactive: null
    transition_out: "blur-crossfade"
    step_by_step_reveal: "5 tabs enter at t=6.0/7.5/9.0/10.5/12.0 (~1.5s apart since narrated quickly), caption 'will I make payroll?' marker-sweep at t=14, slam-cut occurs at t=26 (marker-burst on /plan-payroll prompt)"
    visual_pacing_check: "Beats at 6.0, 7.5, 9.0, 10.5, 12.0, 14.0, 22.0 (sub-line entrance), 26.0 (slam) — max gap 8s between 14→22 — VIOLATION. FIX: insert marker-circle on 'payday' word at t=18.0."

  scene_03_15_plus_15:
    structural: "inline-phase"
    pattern: "stat-pill-row + named-skill-chips-row"
    primitives:
      - "gsap-counter-tween"        # both counters 0→15
      - "gsap-stagger-grid"          # 6 chip reveals
      - "marker-highlight"          # sweep under '15 + 15'
    captions: null                   # numbers visible on screen; caption would compete
    audio_reactive: null
    transition_out: "blur-crossfade"
    step_by_step_reveal: "Workflow counter t=28 → Skills counter t=30 → chip 1 (invoice chaser) t=36 → chip 2 (margin analyzer) t=38 → chip 3 (month-end prepper) t=40 → chip 4 (tax-season organizer) t=42 → chip 5 (contract reviewer) t=44 → chip 6 (lead triager) t=46. Phase exit t=52."
    visual_pacing_check: "Beats every ≤2s — all green."

  scene_04_integration_constellation:
    structural: "inline-phase"
    pattern: "hub-spoke (custom retention pattern — central Claude mark with 7 orbiting logos)"
    primitives:
      - "gsap-stagger-grid"           # 7 logos enter at orbit positions
      - "gsap-path-draw"              # SVG glowing edges connect to center one at a time
      - "marker-highlight"             # sweep under "first CRM connector" caption pill
    captions: "caption-fade-slide"     # for partner names
    audio_reactive: null
    transition_out: "blur-crossfade"
    step_by_step_reveal: "Central Claude mark t=52, then 7 logos enter one per ~2.5s: QB t=54 → PayPal t=56.5 → HubSpot t=59 → Canva t=61.5 → DocuSign t=64 → GW t=66.5 → MS365 t=69. Each path-draw edge animates on logo settle (+0.4s). Phase exit t=74."
    visual_pacing_check: "Beats every ~2.5s — all green."

  scene_05_companion_demo:
    structural: "inline-phase"
    pattern: "video-frame-embed + thumbnail-pointer (custom — uses centered 16:9 pane on 9:16 canvas)"
    primitives:
      - "gsap-stagger-grid"           # frame chrome enters first (border + caption pill)
      - "marker-highlight"             # sweep under "actually" in caption "what it actually looks like"
    captions: "caption-fade-slide"     # caption pill above video pane
    audio_reactive: null               # video has its own audio — narration ducks during clip
    transition_out: "blur-crossfade"
    embed_specifics: |
      assets/clips/anthropic-clip.mp4 plays muted (or audio-on with narration ducked) in a centered horizontal pane.
      Canvas is 1080×1920. Clip is 1920×1080 horizontal — display at width 1000px, height 562.5px,
      centered horizontally at x=40, vertically at y=600 (mid-canvas). The frame chrome (rounded
      corners + Anthropic-orange border glow) frames it as "Anthropic's own demo."
      Phase plan: 74-76 (frame chrome enters), 76-105 (clip plays 29s), 105-106 (hold on
      thumbnail-grade pointer card: "Full demo: link in description").
    step_by_step_reveal: "Frame border t=74, caption pill 'what it actually looks like' t=75, clip starts t=76, hold-card 'Full demo: description' t=105. Marker-sweep on 'actually' t=75.5."
    visual_pacing_check: "Clip plays continuously for 29s (counts as visible foreground motion — not static). After clip ends at t=105, 1s pointer-card hold (≤5s, OK)."

  scene_06_lina_ochman_quote:
    structural: "inline-phase"
    pattern: "quote-card with chip-pop reveals"
    primitives:
      - "gsap-stagger-grid"           # 3 chip pops (HVAC, landscaper, brokerage)
      - "marker-highlight"             # sweep under "not for" key phrase
    captions: null                     # quote text is on-screen typography
    audio_reactive: null
    transition_out: "blur-crossfade"
    step_by_step_reveal: "Quote-card frame t=106, quote text fades in t=107, attribution line (Lina Ochman + Anthropic logo) t=109, chip 1 (HVAC) t=112, chip 2 (landscaper) t=116, chip 3 (brokerage) t=120, marker-sweep on 'not for' at t=110."
    visual_pacing_check: "Beats at 106/107/109/110/112/116/120 — max gap 4s — all green. Final hold 120→124 = 4s OK."

  scene_07_article_screenshot:
    structural: "inline-phase"
    pattern: "screenshot-frame with marker callouts (NO synthetic bars over chart — screenshot is a text article hero, not a chart, so marker-circles and scale-pulses are safe per screenshot-anchor-markers.md)"
    primitives:
      - "gsap-stagger-grid"            # screenshot frame enters first, then callouts
      - "marker-circle"                # circle around the date '2026-05-13' / 'May 13' in article header
      - "marker-highlight"              # sweep under article headline "Claude for Small Business"
    captions: "caption-fade-slide"     # caption pill "Anthropic.com / May 13, 2026"
    audio_reactive: null
    transition_out: "blur-crossfade"
    embed_specifics: |
      assets/screenshots/article-hero.png is 625×800 — narrow article-content crop with no
      empty margin. Display centered on canvas: width 700px (scaled 1.12×), height 896px,
      x=190, y=460 (mid-canvas). Caption pill "Anthropic.com · May 13, 2026" sits at y=380
      above the screenshot.
    step_by_step_reveal: "Screenshot enters t=124 (0.5s fade), caption pill t=125, marker-circle on date t=127, marker-sweep on headline t=130, scale-pulse on Anthropic logo in screenshot t=134. Phase exit t=140."
    visual_pacing_check: "Beats at 124/125/127/130/134 — max gap 4s — all green."

  scene_08_trust_customer_proof:
    structural: "inline-phase"
    pattern: "logo-strip + trust-bullets + daniela-amodei-lower-third"
    primitives:
      - "gsap-stagger-grid"            # 3 customer logo+outcome rows + 2 trust bullets
      - "marker-highlight"              # sweep under "50%" stat in trust bullet
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    step_by_step_reveal: "Customer row 1 (Purity Coffee + outcome) t=140, customer row 2 (Simple Modern + outcome) t=144, customer row 3 (MidCentral Energy + outcome) t=148, trust bullet 1 ('approval-required') t=152, trust bullet 2 ('no training on your data') t=155, marker-sweep on '50%' t=157, Daniela Amodei lower-third t=159. Phase exit t=162."
    visual_pacing_check: "Beats at 140/144/148/152/155/157/159 — max gap 4s — all green. (5 items revealing across 22s satisfies step-by-step-reveal.md cadence.)"

  scene_09_cta_thumbnail_close:
    structural: "inline-phase"
    pattern: "cta-url-slam + thumbnail-grade-close (5-element compliance per shorts-thumbnail-frames.md)"
    primitives:
      - "gsap-stagger-grid"             # all 5 thumbnail elements enter within 0.5s of each other
      - "marker-circle"                 # circle around the debate-CTA question
    captions: null                       # thumbnail elements ARE the typography
    audio_reactive: null
    transition_out: null                 # final scene
    thumbnail_elements:
      brand_chrome: "Anthropic mark, top-left, 48px tall — enters t=162"
      topic_slam: "'15 + 15 SHIPPED' 180px font-weight-900 letter-spacing-tight orange — enters t=162.2"
      visual_anchor: "'Claude for Small Business' subtitle 56px white-dim — enters t=162.4"
      outcome_receipt: "'Sunday-night payroll → 5 min' 48px white-dim — enters t=162.6"
      cta_question: "'Switching from Copilot — or sticking?' 52px white pill bg-orange — enters t=164 (after a 1.5s settle on the static elements, per shorts-thumbnail-frames.md spacing)"
      dynamous_pointer: "'dynamous.ai — learn more' 36px wordmark + URL — enters t=165 (subordinate to CTA question, per engagement-cta.md placement rules)"
    static_hold: "164.5 → 180 = 15.5s held still. Last 14s satisfy 'last frame thumbnail-grade hold ≥1.5s' easily. (Larger hold here because the spoken CTA narration finishes around t=176 and gives the viewer 4 more seconds to absorb. EXEMPT per shorts-thumbnail-frames.md for the terminal hold relaxation.)"
    visual_pacing_check: "Beats at 162/162.2/162.4/162.6/164/165 — all within 3s window. Terminal hold relaxation applies per shorts-thumbnail-frames.md."

# Constraint checks
constraints_audit:
  max_2_markers_per_scene: PASS    # scene 2 has 1, scene 3 has 1, scene 4 has 1, scene 5 has 1, scene 6 has 1, scene 7 has 2, scene 8 has 1, scene 9 has 1
  single_caption_group_at_a_time: PASS
  one_primary_transition: "blur-crossfade is the primary (8 of 8 phase-to-phase transitions — 100%). No accent transitions used because the SFX layering and shape-backdrop rearrange carry the variety. Per shape-rearrange feedback rule, every transition triggers a shape-backdrop reposition."
  no_exit_animations_on_non_final_scenes: PASS
  no_remotion_remnants: PASS
  no_eq_spectrum_visuals: PASS
```

---

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene_01_thumbnail_hook"
    data_start: 0
    data_duration: 6
    audio_anchor: "no narration in this beat (intentional silence so YouTube auto-thumbnail isn't cluttered by speech overlap)"

  - scene: "scene_02_sunday_scramble"
    data_start: 6
    data_duration: 22
    audio_anchor: "narration starts at 7.0s 'every owner asks the same question'; key phrase 'will I make payroll?' lands at ~14.0s; pivot word 'But' at ~26s"

  - scene: "scene_03_15_plus_15"
    data_start: 28
    data_duration: 24
    audio_anchor: "first number '15' spoken at 30.0s; second '15' at 32s; skill names enumerated 36-48s"

  - scene: "scene_04_integration_constellation"
    data_start: 52
    data_duration: 22
    audio_anchor: "first partner name 'QuickBooks' at 54s; 'first CRM connector' phrase at 59-60s"

  - scene: "scene_05_companion_demo"
    data_start: 74
    data_duration: 32
    audio_anchor: "narrator says 'here's what it actually looks like' 74-76; clip plays 76-105 with narration ducked; pointer card 'full demo: description' 105-106"

  - scene: "scene_06_lina_ochman_quote"
    data_start: 106
    data_duration: 18
    audio_anchor: "narrator reads quote 107-118; attribution 118-122; reflection beat 122-124"

  - scene: "scene_07_article_screenshot"
    data_start: 124
    data_duration: 16
    audio_anchor: "narrator says 'this is the announcement' 125-128; key claim restated 128-138; transition 138-140"

  - scene: "scene_08_trust_customer_proof"
    data_start: 140
    data_duration: 22
    audio_anchor: "customer names 140-150; trust beat 150-158; Daniela Amodei cite 158-162"

  - scene: "scene_09_cta_thumbnail_close"
    data_start: 162
    data_duration: 18
    audio_anchor: "CTA narration 162-172; debate question spoken 172-176; Dynamous pointer 176-178; terminal silence + hold 178-180"

total_data_duration: 180
```

`audio_anchor` values are PLACEHOLDERS — Phase 3.5 will refine against `transcript.json` once TTS lands.

---

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  tokens_css: "templates/shorts/anthropic/tokens/anthropic-dark.css"
  overrides: []           # no overrides — Anthropic-branded launch uses the template defaults verbatim
  fonts:
    sans: "Inter"          # template default
    mono: "JetBrains Mono"
  accent_rotation_per_phase:
    scene_01: orange       # CLAUDE FOR SMB topic slam
    scene_02: orange → purple   # 5-tab scramble cool tone → pain
    scene_03: purple + blue     # workflows counter purple, skills counter blue
    scene_04: orange       # Claude hub orange, edges orange
    scene_05: orange       # video frame border
    scene_06: purple       # quote card
    scene_07: blue         # article screenshot frame
    scene_08: green        # customer-proof + trust beat
    scene_09: orange       # final thumbnail slam matches first frame (orange) for visual continuity
  shape_backdrop:
    enabled: true
    repositions_per_transition: true   # default per feedback_shape_rearrange_on_whoosh_default
    sfx_pairing: "cinematic-whoosh on every transition (8 transitions)"
```

---

## AI Image Prompts

None — every visual on screen is either:
- Real captured asset (`anthropic-clip.mp4`, `article-hero.png`)
- Brand logo (Anthropic, partners, customers — sourced from `shared/logos/` or pulled from press kits during composition build)
- Synthetic typography / shape / pill (rendered via HTML+CSS)

No custom AI imagery needed for this video.

---

## Screenshot Inventory

```yaml
screenshots:
  - name: "article-hero"
    url: "https://www.anthropic.com/news/claude-for-small-business"
    file: "assets/screenshots/article-hero.png"
    dimensions: "625x800"
    scene: "scene_07"
    color_scheme: "light"
    usage: "Article-proof screenshot card with marker callouts on headline + date"
    status: "ALREADY CAPTURED 2026-05-14"

  - name: "article-full"
    file: "assets/screenshots/article-full.png"
    dimensions: "625x10839"
    scene: null
    usage: "Reference for fact-checking — NOT shown on screen (too tall)"
    status: "ALREADY CAPTURED"

  - name: "article-top, article-bottom"
    file: "assets/screenshots/article-top.png, article-bottom.png"
    scene: null
    usage: "Reference for fact-checking — backup crops"
    status: "ALREADY CAPTURED"
```

---

## HyperFrames Blocks

```yaml
hyperframes_blocks_used: []
# No registry blocks installed — every visual primitive is inline HTML+CSS+GSAP
# inside index.html, leveraging the shared/lib catalog (stat-pill-row, timeline-cards,
# url-cta) at the pattern level (not via `hyperframes add`) — these are
# composition patterns the template already exemplifies. No vfx-iphone-device or
# WebGL blocks needed for this video.
```

**Optional retention components from `shared/lib/MANIFEST.md`** (to be picked up during composition build, not installed via registry):
- `shared/lib/components/ambient-radial/` — slow-breathing dual-radial background wash (orange + purple) for ambient depth
- `shared/lib/components/top-banner-wordmark/` — persistent Anthropic wordmark in top safe zone
- `shared/lib/components/progress-bar/` — slim 6px bottom-edge progress bar accent-orange (visible runtime indicator for a 180s video — viewer can see they're 1/3 through)
- `shared/lib/components/burst-rays/` — optional accent on the slam-cut at t=26 (PIVOT moment) and on the "15 + 15" reveal at t=28-32

---

## Fact-Check Audit

| # | Claim                                                         | Source                                                                                          | Status |
|---|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------|--------|
| 1 | "Anthropic just shipped Claude for Small Business"             | https://www.anthropic.com/news/claude-for-small-business (May 13, 2026, official launch)        | VERIFIED |
| 2 | "Every owner asks the same question the week before payday"   | https://www.youtube.com/watch?v=lserpKbUDjc (companion video 0:06, verbatim from Anthropic)     | VERIFIED |
| 3 | "15 workflows + 15 skills"                                     | https://www.anthropic.com/news/claude-for-small-business                                        | VERIFIED |
| 4 | "Lives inside QB, PayPal, HubSpot, Canva, DocuSign, GW, MS365" | https://www.anthropic.com/news/claude-for-small-business (partner list)                         | VERIFIED |
| 5 | "First CRM connector for Claude" (Angela DeFranco / HubSpot)   | https://www.anthropic.com/news/claude-for-small-business (partner quote section)                | VERIFIED |
| 6 | "Plan-payroll: Sunday-night → 5 minutes"                       | https://www.youtube.com/watch?v=lserpKbUDjc (companion demo runtime + closing line)             | VERIFIED |
| 7 | Lina Ochman quote: "15-person HVAC, 30-person landscaper, 50-person brokerage" | https://www.axios.com/2026/05/13/anthropic-claude-small-business-smb (on-record)           | VERIFIED |
| 8 | Daniela Amodei: "Half the American economy... close that gap" | https://www.anthropic.com/news/claude-for-small-business (launch post quote)                    | VERIFIED |
| 9 | Customer: Purity Coffee — "problems I didn't know I had"      | https://www.anthropic.com/news/claude-for-small-business (customer-section quote)               | VERIFIED |
| 10 | Customer: Simple Modern — "constraints aren't constraints"   | https://www.anthropic.com/news/claude-for-small-business                                        | VERIFIED |
| 11 | Customer: MidCentral Energy — "tedious clerical work → value-add" | https://www.anthropic.com/news/claude-for-small-business                                    | VERIFIED |
| 12 | "Approval-required execution"                                 | https://www.anthropic.com/news/claude-for-small-business (trust section)                        | VERIFIED |
| 13 | "We don't train on your data by default on Team / Enterprise" | https://www.anthropic.com/news/claude-for-small-business + https://trust.anthropic.com         | VERIFIED |
| 14 | "50% of SMB owners cite data security as #1 AI hesitation"    | https://www.anthropic.com/news/claude-for-small-business (cited within article)                 | VERIFIED |
| 15 | "44% of US GDP from small businesses"                         | https://www.anthropic.com/news/claude-for-small-business (Daniela Amodei contextual cite)       | VERIFIED |
| 16 | "Microsoft Copilot $30-43/user/month" (Scene 9 CTA framing)   | https://www.comparethecloud.net/articles/google-gemini-workspace-vs-microsoft-365-copilot-uk-small-team-pricing | VERIFIED (third-party — not Anthropic source; flagged) |
| 17 | "36M US small businesses" (Scene 2 supplemental, optional)    | https://techcrunch.com/2026/05/13/anthropic-courts-a-new-kind-of-customer-small-business-owners/ | THIRD-PARTY — per ARTICLE_RESPONSE rule, EXCLUDED FROM SCRIPT unless restated in primary article. (Anthropic post may mention this — needs re-verification at Phase 2b against primary source.) |
| 18 | "Anthropic $30B run-rate, up from $9B"                        | https://finance.yahoo.com/news/anthropic-debuts-claude-for-small-business... (Yahoo)            | THIRD-PARTY — EXCLUDED FROM SCRIPT (per ARTICLE_RESPONSE rule, fact-check is source-only) |

**Third-party press claims to verify against primary source at Phase 2b**:
- **Claim 17** (36M US SMBs) and **Claim 18** ($30B run-rate) — these came from TechCrunch and Yahoo coverage. Per memory rule `feedback_factcheck_article_response_scope`, for ARTICLE_RESPONSE videos we fact-check bidirectionally against the source article only and exclude third-party press claims unless the primary source confirms them. **Neither claim is in the planned narration** — both were considered in the content brief but excluded from the script structure. Confirmed: the plan does not depend on either. Phase 2b will re-verify nothing third-party leaked back in.
- **Claim 16** (Copilot pricing) — used in the CTA framing question ("Switching from Copilot?"). The pricing itself is NOT spoken in the script — only the brand name "Copilot." Pricing claim is sourced for context but never broadcast. No risk.

**Excluded by Phase 1 (will not enter Phase 2 script)**:
- 36M US small businesses stat (third-party only)
- $30B Anthropic run-rate (third-party only)
- Specific pricing dollar amounts for any tool (no SMB price published by Anthropic; will not fabricate)
- Specific seat counts at customer businesses (not published)
- Solopreneurship Accelerator funding amounts (not central to thesis, omit)

---

## Notes for Composition Build

### Asset gaps to resolve before Phase 4 (composition build)

1. **Partner logos for Scene 4 (integration constellation)** — `shared/logos/` has `canva-logo.png`, `google-logo.png` / `google-g-logo.png`, `microsoft-logo.png`, `claude-logo-light.svg`, `claude-icon.svg`. **Missing**: QuickBooks (Intuit), PayPal, HubSpot, DocuSign, Google Workspace mark (distinct from Google G), Microsoft 365 mark (distinct from Microsoft corp). Composition build should:
   - Pull each missing logo from the brand's press kit (Brand.intuit.com, paypal.com/brand, hubspot.com/brand, docusign.com/about/brand, workspace.google.com/brand-resources, microsoft.com/brand)
   - Drop into `videos/claude-for-small-business/assets/logos/` (local copy, not shared/logos/ — keeps the video self-contained)
   - If any logo is genuinely unreachable, substitute a text-only chip with the brand name in brand color

2. **Customer logos for Scene 8** — none in `shared/logos/`. Composition build should:
   - Pull Purity Coffee, Simple Modern, MidCentral Energy logos from each company's official press / press-kit / about page
   - Drop into `videos/claude-for-small-business/assets/logos/`
   - Fallback: text-only treatment with the company name in a customer-row card chrome — still satisfies the "3 customer rows" visual but loses brand polish

3. **Lina Ochman / Daniela Amodei headshots** — NOT needed for the planned quote cards. Quote cards use wordmark attribution + Anthropic logo only. If user later wants headshots, source from anthropic.com/team or LinkedIn (with attribution).

### Phase ordering note

The 9-phase structure (vs the brief's 8-phase suggestion) adds the **screenshot-proof phase (Scene 7)** between the Lina Ochman quote and the trust/customer proof. The original brief implicitly bundled the screenshot into Scene 1's "opening receipt anchor," but Scene 1 is now strictly thumbnail-grade hold with no entrance animations — so the article screenshot earns its own phase for the proof beat. This addition is enabled by the user constraint "show article screenshot (narrow width, no empty space)."

### Visual pacing rule self-check

Every phase audited against `.claude/rules/visual-pacing-5s.md`. **Two scenes had >5s gaps in the initial draft** — flagged in the retention picks block as `visual_pacing_check` notes:
- **Scene 2** — gap from caption land at t=14 to slam at t=22 was 8s. **FIX**: insert marker-circle on 'payday' word at t=18 to break the gap (now 4+4).
- All other scenes pass.

### Step-by-step reveal compliance

Every list of ≥3 items is enumerated step-by-step:
- Scene 3: 6 skill chips, ~2s apart (rapid because narration enumerates them rapid-fire — acceptable per step-by-step-reveal.md "quick stagger is fine when narration genuinely names them all in one sentence")
- Scene 4: 7 partner logos, ~2.5s apart
- Scene 6: 3 business-type chips, ~4s apart (HVAC / landscaper / brokerage)
- Scene 8: 3 customer rows + 2 trust bullets, ~4s apart

All use the **hidden-until-reveal pattern** (explicit `tl.set()` at t=0 + `tl.to()` at reveal time) per the rule. Composition build must NOT use `tl.from()` for these — write the `tl.set()` lines explicitly.

### First-frame and last-frame thumbnail compliance

- **First frame (t=0)**: Scene 1 (6s hold) — Anthropic mark (top-left, 48px), "CLAUDE FOR SMB" topic slam (160px orange), outcome receipt "15 workflows. 15 skills. Just shipped." (52px white-dim). 5 elements present per `shorts-thumbnail-frames.md`. No entrance animation — all at full opacity from t=0 so YouTube auto-thumbnail picks a meaningful frame.
- **Last frame (t=180)**: Scene 9 — Anthropic mark, "15 + 15 SHIPPED" topic slam (180px), "Claude for Small Business" subtitle (56px), outcome receipt "Sunday-night payroll → 5 min", debate-CTA question pill "Switching from Copilot — or sticking?", Dynamous pointer "dynamous.ai — learn more." All 5 thumbnail elements + the engagement-CTA element (per `engagement-cta.md`) present. Held still from t=164.5 to t=180 (15.5s) — far exceeds the 1.5s minimum.

### Engagement CTA placement (per `.claude/rules/engagement-cta.md`)

The debate-CTA question "**Switching from Copilot — or sticking?**" appears in three places (all agreeing):
1. **Spoken** (Scene 9, t=172-176): final 3-4s of narration asks the question.
2. **Visual** (Scene 9, `#cta-question` element): on-screen pill that enters at t=164 and persists through the terminal hold (last 15.5s).
3. **YouTube description** (`youtube-description.md`, to be written in YT phase): final paragraph restates the same question verbatim.

CTA satisfies all four HARD criteria:
- Binary answer: "switching" or "sticking" (3 words each, mobile-typable)
- Polarizing: tool-loyalty framing forces team-picking
- References specific claim: the integration constellation in Scene 4 + the Copilot comparison framing in Scene 2's pivot ("ChatGPT can't see your QuickBooks; Copilot only sees Microsoft")
- Low cost to answer: a senior dev AND a 20-person business owner can both fire off "sticking" in 2 seconds

### Dynamous spoken outro (per `feedback_dynamous_short_outro`)

The Dynamous narration line is the SHORT pointer-only version: **"If you want to learn more about AI, check out the dynamous.ai community."** Carried by the visible `dynamous.ai — learn more` element at t=165, narrated at t=176-178. The full Dynamous endcard treatment is NOT used (this is a non-Dynamous-promoted video per the orchestration log — no `dynamousPromotion: true` flag in meta.json).

### SFX cue plan

Per the audit, this video uses ONLY library cues from `shared/audio/MANIFEST.md`:

```
Cue                    Used in                                         Count
─────────────────────  ──────────────────────────────────────────────  ─────
cinematic-whoosh       Every phase transition (8x)                     8
impact-slam            Hook caption land, slam-cut PIVOT                2
screen-shake           Slam-cut PIVOT (layered)                         1
scale-slam             Stat-counter reveals (Scene 3 x2)                2
spring-pop             Skill chips (Scene 3 x6), partner logos (S4 x7), customer rows (S8 x3), chip pops (S6 x3)  19
pop                    Marker-circle / scale-pulse moments              ~5
strike-cross           NOT USED (no strikethrough beats planned)        0
glitch-zap             Slam-cut PIVOT (layered)                         1
sonic-logo             Optional t=0 cold-open stinger                   0 (skipped — thumbnail hold is silent)
```

To sync into `videos/claude-for-small-business/assets/sfx/`, run:
```bash
bash scripts/sync-video-sfx.sh videos/claude-for-small-business cinematic-whoosh impact-slam screen-shake scale-slam spring-pop pop glitch-zap
```

### Anti-pattern check (per retention-components-hyperframes.md §8)

- No Remotion remnants — verified
- No spectrum/equalizer visuals — verified
- No exit animations on non-final scenes — verified (transitions handle exits via blur-crossfade + shape-rearrange)
- Max 2 markers per scene — verified (Scene 7 has 2; all others have 0-1)
- One caption group at a time — verified (captions only in Scenes 2/4/5/7, never overlapping)
- Mixed structural model — N/A (pure inline-phase throughout)
- One primary transition — verified (blur-crossfade 100%)

### Screenshot-anchor markers (per `.claude/rules/screenshot-anchor-markers.md`)

Scene 7's `article-hero.png` is a **text article hero, NOT a bar chart**. Marker overlays (marker-circle on the date, marker-highlight under the headline) are SAFE — they do not duplicate existing bar geometry. Confirmed compliant.

### Heteronym audit (per `.claude/rules/tts-pronunciation.md`)

Pre-flagging for Phase 2a:
- "live" — likely appears as adjective ("Claude is live today"). Phase 2a MUST replace with "shipping" / "available."
- "lead" — likely appears as noun ("lead triager" skill name). The skill IS named "lead triager" in the article — verify pronunciation in TTS, fall back to "lead-triage skill" or "the triager skill" if /lɛd/ pronunciation slips through.
- "read" — low risk; not currently in any planned narration line.
- "SMB" — script MUST spell as "S M B" letter-by-letter per content-brief technical-terms note.
- "P&L" — script MUST spell as "P and L."
- "CRM" — script MUST spell as "C R M."
- "AR / AP" — script MUST spell as "A R" / "A P."

### Composition-duration self-check (per `.claude/rules/hyperframes-pitfalls.md` §1)

The composition's GSAP timeline ends with the last tween at ~t=180. The `<audio id="narration">` element will have `data-duration` matching narration.wav (likely ~178s with 2s padding). The root timeline must include `tl.set({}, {}, 180)` as the LAST line so the studio reports 180s, not the last-tween time. Composition build: ensure this line is present.

### What composition build (Phase 4 / `new-anthropic-short.md`) needs to know

- The 9-phase mutex pattern requires `index.html` z-index escalation: `#phase1` z-index 1, `#phase2` z-index 2 … `#phase9` z-index 9.
- Phase transitions use the standard `blur-crossfade` + shape-rearrange pattern from the template.
- Scene 5 (the embedded clip) needs a `<video>` element inside the phase with `muted` (and the narration audio is independent) OR `autoplay` synced — composition build will decide based on whether the source clip has needed-audio. Default: muted, narration carries.
- Scene 7's `<img>` for `article-hero.png` must be at the resized 700×896 display size — but the source PNG (625×800) is already smaller than 2× canvas dimensions per hyperframes-pitfalls.md §2, so no batch-resize needed.
- The `#cta-question` element in Scene 9 satisfies `engagement-cta.md` requirement #2. Composition build MUST give it the documented id.
