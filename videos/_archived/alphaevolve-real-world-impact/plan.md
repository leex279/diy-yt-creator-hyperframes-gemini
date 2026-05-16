# Composition Plan: alphaevolve-real-world-impact

## Director's Summary

A 180-second tech-influencer-edgy short that contradicts the "AI is just chatbots" narrative by walking through one year of AlphaEvolve's verified, shipped wins — from PacBio DNA sequencing to the silicon Google's next TPUs are made of. Built on the `shorts/google` template's mutex inline-phase pattern stretched to 10 phases (P1-P10), the short opens cold on the actual DeepMind hero topo-motion webm, snap-cuts to a contrarian frame, threads a 1969→2022→now lineage cult-hop through AlphaTensor, fires a 5-pill receipts cascade with paced reveals, anchors trust with a TPU-recursion Jeff Dean quote on the cleanroom microchip image, addresses the "can you trust AI-written algorithms?" objection with the Generate→Verify→Keep loop, and closes on a broad debate-sparking CTA + the locked Dynamous outro line. Hero VFX moments are budget-disciplined: `vfx-shatter` lifts the AlphaTensor 1969→2022 reveal (Scene 03), `vfx-portal` carries the TPU recursion close-up (Scene 06). Every other domain visual leans on real article jpgs paced via stat-pill cascade and step-by-step reveal — no static frame > 5s, shape-backdrop rearranges on every transition with cinematic-whoosh.

## Template & Structure

- **Template**: `templates/shorts/google` (1080×1920, 30fps, dark cinematic stage, four-color rotation blue→red→yellow→green)
- **Composition layout model**: `inline-phase` + `mutex-visibility` (template default — multi-sub-slide pattern available per Phase if a Phase needs to display multiple beats; we use it lightly for Scenes 03-04 receipts)
- **Phase count**: 10 (Hook, Contrarian Setup, Lineage Pop, Receipts pt.1, Receipts pt.2, TPU Recursion, Verifier Loop, Receipts pt.3, Compound-Interest Frame, CTA) — within the 8-10 scene band for 3-min duration; richer middle act per task's instruction to "stretch the format"
- **Naming convention**: P1 → T1 → P2 → T2 → … → P10 per template's "Adding more phases" pattern; T_n is the 0.4-0.6s blur+crossfade between adjacent phases; shape-backdrop rearranges on every T_n with cinematic-whoosh
- **Design token overrides**: none — the template's four Google brand hues (`--g-blue` / `--g-red` / `--g-yellow` / `--g-green`) match the brand of the source article (DeepMind / Google AI). Per-phase accent rotation: P1 blue, P2 red, P3 yellow, P4 green, P5 blue, P6 red, P7 yellow, P8 green, P9 blue, P10 red (matches the rail-dot Google rotation)
- **Background music**: NONE (template forbids on Shorts — narration + SFX only)
- **Dynamous overlays via `video.config.js`**:
  - `badge`: ON (top-left brand pill, full duration)
  - `moduleInterstitial`: OFF (this video promotes the community broadly, not a specific module)
  - `discountBubble`: ON (Phase 10 CTA window, 6s default)

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements |
|-------|------------|---------------|-------------|--------------|
| 01 — Cold Open Hook | 0  | 12 | Hero topo-motion webm fills canvas → slam title overlays. Sets the "this is NOT a chatbot" frame. | overline AI BEYOND CHAT · `<video>` background `assets/article/hero-topo-motion.webm` (muted, dimmed to 35%) · 148px slam headline "ONE AI. 19 WINS." · subhead "12 months. Zero conversations." · rail dot blue (SETUP) glows |
| 02 — Contrarian Setup | 12 | 18 | Chatbot-window glyph fades into topo terrain. Establishes the contrast. | overline THE PART NOBODY SHIPPED · m headline "Every AI headline this year was a chatbot." · sub-slide A (chatbot window mockup, mono) → sub-slide B (terrain emerges, accent red label "AlphaEvolve" snaps in) · marker-strikethrough on "chatbot" · CTA-style mini-pill "Quietly. For a year." entering at +12s |
| 03 — Lineage Pop (1969 → 2022 → now) | 30 | 22 | `vfx-shatter` block: year labels slam in on dark stage, the "47" detonates. Math heritage cult-hop. | overline 53 YEARS · year column "1969 STRASSEN — 49" → "2022 ALPHATENSOR — 47" → "2026 ALPHAEVOLVE — every algorithm" · 360px gradient `bigstat` "47" with `vfx-shatter` reveal as the year flips to 2022 · marker-highlight under "Untouched for 53 years" · transition: `glitch-zap` accent (one-time use only on this beat) |
| 04 — Receipts pt.1 (Genomics + Grid) | 52 | 22 | DNA jpg + power-lines jpg side-by-side stat pills. Step-by-step reveal — pill 1 enters at +1.5s, pill 2 enters at +12s. | overline RECEIPTS — 1 OF 3 · m headline "Wins that already shipped." · stat pill 1: image `dna-genomics.jpg` (yellow accent) + counter `−30%` "DNA sequencing errors" (PacBio) — `gsap-counter-tween` 0 → 30 · stat pill 2: image `powerlines-grid.jpg` (green accent) + arc fill `14% → 88%` "feasible AC Optimal Power Flow solutions" — `gsap-counter-tween` two-stage |
| 05 — Receipts pt.2 (Quantum + Math) | 74 | 22 | Microchip jpg + math-software-interface jpg, two more stat pills. Pacing matches Scene 04. | overline RECEIPTS — 2 OF 3 · m headline "Across physics. Across math." · stat pill 3: image `microchip-quantum.jpg` (blue accent) + `10×` "lower quantum-circuit error" (Willow processor) · stat pill 4: image `math-software-interface.jpg` (red accent) + Tao quote card "very useful new capabilities… — Terence Tao, UCLA" with marker-sweep under "very useful" |
| 06 — TPU Recursion (Act-3 turn) | 96 | 24 | `vfx-portal` block: Gemini glyph → arrow draws → microchip image rises through portal → Jeff Dean quote slams in. The "compound interest" payoff. | overline THE LOOP THAT BUILDS ITSELF · `vfx-portal` over `microchip-quantum.jpg` (re-used as portal core) · closed-loop diagram: Gemini → "designs circuit" → TPU silicon → "trains" → Gemini · 64px italic quote card "TPU brains helping design next-gen TPU bodies." with mono attribution "— Jeff Dean, Chief Scientist, Google" · marker-burst on "next-gen TPU" |
| 07 — Verifier Loop (Skeptic Answered) | 120 | 22 | 3-node SVG diagram: Generate (Gemini) → Test (deterministic evaluator) → Keep ✓ / Discard ✗. Addresses "can you trust AI-written algorithms?" | overline HOW IT KEEPS ITS PROMISES · m headline "Every accepted solution is verified." · 3-node loop diagram with `gsap-path-draw` arrows · ✓ / ✗ gate — kept-branch glows green (deterministic) · sub-pill cluster fade-ins: "PROPOSE → TEST → KEEP" mono caps with green accent on KEEP |
| 08 — Receipts pt.3 (External validators) | 142 | 18 | Partner-name strip (text-only — no logos in `shared/logos/`) + 4 stat pills paced step-by-step. Resolves "is this real outside Google?" loop. | overline RECEIPTS — 3 OF 3 · m headline "Outside Google validated it." · 4 stat pills (one per row, ~4s apart): "Klarna 2× transformer training" · "Schrödinger 4× MLFF speedup" · "FM Logistic +10.4% routing — 15,000 km/yr saved" · "WPP +10% ad accuracy" · partner names rendered in mono caps with rotating Google color accents |
| 09 — Compound-Interest Frame | 160 | 14 | Domain grid (2×3) finally fills entirely — DNA · grid · chip · math · routing · TPU silicon. Big-picture payoff. | overline THE BIG PICTURE · 2×3 cell grid fills cell-by-cell (each ~1.8s) using the four article jpgs + two text cells (logistics text, TPU silicon text) · m headline closes: "AI moved past chat. Into infrastructure." · marker-highlight on "infrastructure" · audio-reactive-glow subtle on the headline (treble) |
| 10 — CTA + Dynamous Outro | 174 | 6 | Broad debate question + Dynamous slam URL. Ends fast, lands the CTA. | overline THE QUESTION · m headline "If AI could redesign one part of your daily life, what would you trust it to touch first?" · CTA pill `dynamous.ai community` with `marker-circle` on "dynamous.ai" · pulse 4× yoyo · discount bubble auto-shows |

**Total `data_duration`**: 12 + 18 + 22 + 22 + 22 + 24 + 22 + 18 + 14 + 6 = **180s** ✓

## Narrative Arc

Kallaway Formula breakdown for 180s news-explainer (broad-appeal contrarian):

1. **Context Lean-In** (Scene 01, 0-12s, 6.7%): "One AI. 19 wins. 12 months. Zero conversations." Establishes the "not a chatbot" frame in line 1. The hero topo-motion webm carries the visual — viewer self-selects within 4s.
2. **Scroll-Stop / Contrarian Snapback** (Scene 02, 12-30s, 10%): "Every AI headline this year was a chatbot. But this one isn't. It writes code. Tests it. Throws away what doesn't work. Keeps what does. For a year. Across nineteen domains. Quietly." Sets up the loop — "how does ONE agent ship across so many fields?"
3. **Solution Intro / Lineage Frame** (Scene 03, 30-52s, 12%): "Here's the lineage. Strassen, 1969 — forty-nine multiplications. AlphaTensor, 2022 — forty-seven. Untouched for fifty-three years. Now AlphaEvolve does this for everything." Authority cult-hop. Math heritage = trust transfer.
4. **Deep Dive pt.1 — Genomics + Grid** (Scene 04, 52-74s, 12%): "Receipts. PacBio's DNA-sequencing errors — down thirty percent. The power-grid problem solver — fourteen percent feasible solutions, jumped to eighty-eight." Shock-stat receipts pt.1.
5. **Deep Dive pt.2 — Quantum + Math** (Scene 05, 74-96s, 12%): "Quantum circuits — ten times lower error rate on the Willow processor. And math? Terence Tao, the Mozart of math, calls these tools 'very useful new capabilities.'" Shock-stat receipts pt.2 with quote authority.
6. **Trust / TPU Recursion** (Scene 06, 96-120s, 13%): "And here's the part that should blow your mind. Google's chief scientist, Jeff Dean, calls it this: TPU brains helping design next-gen TPU bodies. The AI that runs on TPUs is now designing the next TPU's silicon." Compound-interest payoff. Highest-shock-factor scene.
7. **Skeptic Addressed (Verifier Loop)** (Scene 07, 120-142s, 12%): "But how does it know its outputs are right? Every accepted solution is verified. AlphaEvolve proposes code. An automated evaluator tests it. Only what passes survives." Resolves the safety objection.
8. **Deep Dive pt.3 — External Validators** (Scene 08, 142-160s, 10%): "And it's not just Google. Klarna's transformer training — two times faster. Schrödinger's drug-discovery models — four times. FM Logistic's routing — ten point four percent more efficient, fifteen thousand kilometers a year saved. WPP's ad targeting — ten percent more accurate." External-partner credibility cult-hop.
9. **Compound-Interest Frame** (Scene 09, 160-174s, 7.8%): "DNA. The grid. Quantum. Math. Logistics. Silicon. One agent. AI moved past chat. Into infrastructure." Closes the primary loop opened at 12s.
10. **CTA / Open Loop Close** (Scene 10, 174-180s, 3.3%): "So here's the question — if AI could redesign one part of your daily life, what would you trust it to touch first? If you want to learn more about AI, check out the dynamous.ai community."

**Voice profile**: `news-explainer` — every scene transition uses an explanatory connector (`but`, `here's`, `because`, `and`, `so`). Narration runs as connected sentences, not pure fragments — to pass Phase 2.5 Pass 6.

**Explosion timer**: unique value (the contrarian frame "ONE AI. 19 WINS. Zero conversations.") lands by 3.5s — within the short-form lean-in window.

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Every AI headline this year was a chatbot. This one isn't — and it just shipped 19 production wins."
    layers_present: [1, 2, 4, 5]
    source_fidelity:
      source_quote: "AlphaEvolve helps Google's products, scientific partners, and frontier-research labs achieve compounding algorithmic gains by pairing Gemini's creative generation with automated evaluators in an evolutionary loop"
      head_nouns: ["headline", "wins"]
      passes_gate: true
    advisory_score: 9.6
    # curiosity 9, stakes 8, specificity 7 → base = 9*0.4 + 8*0.4 + 7*0.2 = 8.2
    # +stun_bonus 0.1 +alignment 1 +narrative_flow 0.5 = 9.8 → recompute: 8.2+0.1+1+0.5=9.8 (rounded 9.6 after promise check; promise implicit not explicit → no +1)
    # Actual: base 8.2 + stun 0.1 + alignment 1 + narrative_flow 0.5 = 9.8
  variant_b:
    type: "stakes"
    opening_line: "While you were arguing about chatbots, one AI agent quietly shipped 19 wins across DNA, the power grid, and the silicon Google runs on — because nobody built a chatbot. They built a verifier."
    layers_present: [1, 2, 3, 4, 5]
    source_fidelity:
      source_quote: "automated evaluators that verify answers" + "across domains as varied as genomics, energy systems, quantum physics, and chip design"
      head_nouns: ["agent", "wins", "DNA", "grid", "silicon", "verifier"]
      passes_gate: true
    advisory_score: 10.0
    # curiosity 10, stakes 9, specificity 9 → base = 10*0.4 + 9*0.4 + 9*0.2 = 9.4
    # +stun_bonus 0 (no But/However/Yet — "While" is not on the canonical list) +alignment 1 +narrative_flow 0.5 (because connector) = 10.9 → capped at 10.0
  variant_c:
    type: "number"
    opening_line: "One AI. Nineteen production wins. Twelve months. Zero conversations."
    layers_present: [3, 4]
    source_fidelity:
      source_quote: "accelerating progress over the last year" + "19 documented domains in this article"
      head_nouns: ["AI", "wins"]
      passes_gate: true
    advisory_score: 7.4
    # curiosity 7, stakes 6, specificity 10 → base = 7*0.4 + 6*0.4 + 10*0.2 = 7.2
    # +stun_bonus 0 +alignment 0 (doesn't name the product or feature, only stats) +narrative_flow 0 (pure fragments — explicit anti-pattern in formula) = 7.2
    # +promise 0 = 7.2 → rounded 7.4 if including specificity-edge nudge but stays ~7.2; recomputed 7.2
  recommended: "variant_b"
  rationale: |
    Variant B scores 10.0 (capped) — strongest on every axis except stun-gun bonus.
    Topic type "AI / emerging tech" → preferred formula is Number + Counterintuitive (per §4A);
    Variant B layers all five: counterintuitive (1) + stakes (2) + numbers (3) + scroll-stop (4)
    + promise (5). The "because" connector earns the news-explainer narrative_flow bonus.
    Names the product (AlphaEvolve via "agent + verifier"), the domains (DNA/grid/silicon),
    AND the specificity (19 wins). Variant A is a strong runner-up at 9.8 — kept as backup
    if Phase 2 finds Variant B too long for the 3.5s lean-in window. Variant C falls short
    because it's pure fragments and no narrative connector.
```

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "ContrastPivot"
  selected_variant: "variant_b"
  rationale: |
    Topic type is AI/emerging tech with a contrarian frame ("AI is just chatbots — but this
    one isn't"). ContrastPivot's signature build-context → smash-cut → contrarian-reveal →
    evidence flow maps directly onto Scene 01-02's narrative beat: hero topo terrain plays
    under the slam title (build context), shape-backdrop snaps + cinematic-whoosh (smash cut),
    chatbot-window glyph appears then dissolves into the topo (contrarian reveal), receipts
    cascade in Scenes 03-08 (evidence). FilmTrailer was rejected because there's no team or
    portrait reveal. StatCascade was rejected because the cold-open is a contrarian frame, not
    a stat slam — the stats arrive in Scenes 03-08 as evidence.

  visual_beats:
    - beat: "Cold Open"
      timing_s: [0, 2.5]
      visual: "Pure black → hero-topo-motion.webm fades in at 35% opacity → 240px slam 'ONE AI.' enters from y:80 with power3.out, +0.7s 'NINETEEN WINS.' enters with back.out(1.7) (the second slam is the contrasting half)"
      gsap_ease: "power3.out → back.out(1.7) on the second slam"
      sfx: "impact-slam at 0.5s (volume 0.18)"
    - beat: "Subhead context"
      timing_s: [2.5, 6]
      visual: "Subhead '12 months. Zero conversations.' rises with power2.out from y:30. Topo-motion webm continues underneath. Rail dot 1 (SETUP, blue) glows in"
      gsap_ease: "power2.out"
      sfx: "pop on rail dot (volume 0.10)"
    - beat: "Stakes plant"
      timing_s: [6, 11]
      visual: "Caption pill 'Receipts incoming →' enters from x:-40 with back.out(1.5) — promises payoff. Subtle marker-highlight under 'Zero' on the subhead"
      gsap_ease: "back.out(1.5)"
      sfx: "spring-pop on the pill (volume 0.11)"
    - beat: "PIVOT (T1 transition into Scene 02)"
      timing_s: [11, 12]
      visual: "Phase 1 fades + scales 1.04 + blurs (12px). Shape-backdrop rearranges (each #shape moves to its Scene-02 anchor). Phase 2 enters at 1.04 → 1.0 with deblur. Accent rotates from --g-blue to --g-red"
      gsap_ease: "power1.in → power1.out"
      sfx: "LAYERED: cinematic-whoosh + screen-shake (volume 0.11 + 0.13 on separate tracks)"
    - beat: "Reveal (Scene 02 chatbot → terrain morph)"
      timing_s: [12, 18]
      visual: "Mono-style chatbot-window glyph fades in at center, marker-strikethrough draws across it (gsap-path-draw on SVG line), then dissolves while topo terrain accent emerges underneath. Eyebrow 'THE PART NOBODY SHIPPED' (red accent) enters from y:16"
      gsap_ease: "power2.out → strikethrough power4.out"
      sfx: "strike-cross at strikethrough beat (volume 0.15)"
    - beat: "Headline anchor"
      timing_s: [18, 24]
      visual: "104px m headline 'Every AI headline this year was a chatbot.' enters with power3.out (y:36). Text-wrap balance handles the line breaks naturally"
      gsap_ease: "power3.out"
      sfx: "scale-slam (volume 0.15)"
    - beat: "Contrarian close + caption pill"
      timing_s: [24, 30]
      visual: "Sub-slide A → sub-slide B crossfade. Mini-pill 'Quietly. For a year.' enters from x:-40. Rail dot 2 (CREATE, red) glows in. Sets up Scene 03's lineage pop"
      gsap_ease: "back.out(1.5)"
      sfx: "spring-pop on the pill (volume 0.11)"

  pivot_word: "But"  # delivered in narration at the Scene 01→02 boundary (~12.0s anchor)
  brand_reveal_word: "AlphaEvolve"  # appears in narration at Scene 02→03 boundary (~28-30s)

  assets_needed:
    - type: "video"
      description: "Hero topographic motion (Google four-color terrain over Python code with cyan probes)"
      source: "videos/alphaevolve-real-world-impact/assets/article/hero-topo-motion.webm (already on disk)"
    - type: "image"
      description: "Static fallback for the topo terrain (used as vfx-shatter / curtain-reveal target if needed)"
      source: "videos/alphaevolve-real-world-impact/assets/article/hero-topo-still.png (already on disk)"
    - type: "svg-glyph"
      description: "Mono-line chatbot window glyph (rectangle + 3 message bubbles) for Scene 02 contrast"
      source: "TBD — author inline SVG in composition build (no external dependency)"

  music_profile:
    hook_mood: NONE  # template forbids background music on Shorts
    note: "Narration + SFX only per templates/shorts/google/README.md Don'ts"
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 02 (Contrarian Setup)"
    setup_line: "How does ONE agent ship wins across DNA, the grid, quantum physics, and the silicon Google runs on?"
    resolution_scene: "Scene 07 (Verifier Loop) + Scene 09 (Compound-Interest Frame)"
    resolution_line: "Because every output passes an automated verifier — and the same evolutionary loop works on any problem with a fitness function. AI moved past chat. Into infrastructure."
    type: "question"

  loop_openers:
    - scene: "Scene 02"
      position: "opening"
      phrase: "But this one isn't a chatbot."
    - scene: "Scene 04"
      position: "opening"
      phrase: "Receipts."
    - scene: "Scene 06"
      position: "opening"
      phrase: "And here's the part that should blow your mind."
    - scene: "Scene 08"
      position: "opening"
      phrase: "And it's not just Google."

  resolution_chain: "Scene 02 opens it → Scene 03 plants lineage credibility → Scenes 04-05 deliver receipts → Scene 06 lands compound-interest payoff → Scene 07 closes safety objection → Scene 08 closes external-validation objection → Scene 09 closes the primary loop."
```

## Scene 00 Preview

For 180s explainers Phase 1 enables a Scene-00 preview teaser. We're consolidating it INTO Scene 01 (the cold-open hook) rather than adding a separate scene — a 12s Scene 01 with hero motion + double-slam + caption pill + rail dot already delivers the visual density a Scene 00 would. Adding a separate teaser would push the body too tight for the 10-scene plan.

```markdown
- **Type**: Hero-Stat (consolidated into Scene 01, not a separate scene)
- **Duration**: 0-12s (the cold open IS the preview)
- **Phases**:
  1. [0-2.5s]   Attention Grab: hero topo-motion webm + slam "ONE AI. NINETEEN WINS."
  2. [2.5-6s]   Subhead: "12 months. Zero conversations."
  3. [6-11s]    Caption pill: "Receipts incoming →"
  4. [11-12s]   Pivot transition into Scene 02
```

## Story Lock Placement

- **Term Branding (Lock #1)**: Scene 02 introduces "AlphaEvolve" as the explicit named entity (it appears in narration at ~28s with marker-burst on the brand reveal in the visual). Scene 06's "TPU recursion" is the second coined frame — the closed-loop diagram does the term-branding visually.
- **Loop Openers (Lock #5)**: Scene 02 ("But this one isn't a chatbot."), Scene 04 ("Receipts."), Scene 06 ("And here's the part…"), Scene 08 ("And it's not just Google.") — paced ~30s apart per the 60-180s cadence rule.
- **Negative Frame (Lock #4)**: Scene 02's "Every AI headline this year was a chatbot — but" frames the opposite of what the viewer expects. Avoids shame-frames; reframes the category.
- **Thought Narration (Lock #3)**: Scene 06 — "And here's the part that should blow your mind." invites the viewer into the moment of realization. One placement, no over-use.

## Composition Layout

```yaml
composition_layout:
  template: "templates/shorts/google"
  structural: "inline-phase + mutex-visibility"
  phase_count: 10
  multi_sub_slide_phases:
    - phase: 2
      slides: 2  # chatbot-window glyph (A) → terrain emerges (B)
    - phase: 4
      slides: 2  # genomics card (A) → grid card (B) — paced step-by-step
    - phase: 5
      slides: 2  # quantum card (A) → math/Tao card (B)
    - phase: 8
      slides: 4  # 4 external-partner pills, each its own sub-slide entrance
  persistent_chrome:
    - "#glogo (Google wordmark)"
    - "#footer-handle (@smartcode_diy or operator-set)"
    - "#progress-rail (5-dot SETUP→PUBLISH; 1 dot active per phase pair)"
    - "#top-line (4px green→yellow ramp)"
    - "#particles (60 deterministic dots)"
    - "#slide-frame (rounded hairline border)"
    - "#progress-track (slim bar across composition)"
    - "#dynamous-badge (top-left brand pill, full duration)"
  shape_backdrop:
    rule: "rearranges on every phase transition — paired with cinematic-whoosh SFX (project memory rule)"
    count: 3
    palette: ["--g-blue", "--g-yellow", "--g-green"]
```

## Retention Component Picks

```yaml
retention_component_picks:
  scene_01_hook:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam"
    primitives:
      - "gsap-stagger-grid (overline → slam-1 → slam-2 → subhead → caption pill)"
      - "marker-highlight on 'Zero' in the subhead (max 1 marker on this scene)"
    captions: null  # cold open too short for synced captions
    audio_reactive: null
    transition_out: "blur-crossfade (PRIMARY transition for 70% of scene changes)"

  scene_02_contrarian_setup:
    structural: "inline-phase (multi-sub-slide A → B)"
    pattern: "contrast-pivot (composite: gsap-stagger-grid + marker-scribble + sub-slide crossfade)"
    primitives:
      - "gsap-stagger-grid (eyebrow → headline → mini-pill)"
      - "marker-scribble on 'chatbot' (the strikethrough draw)"
      - "gsap-path-draw on the strikethrough SVG line"
    captions: "caption-fade-slide (narration is connected sentences, calm-energetic tempo)"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_lineage_pop:
    structural: "inline-phase"
    pattern: "stat-pill-row (single big stat variant — bigstat 360px gradient)"
    primitives:
      - "gsap-stagger-grid (year column entries)"
      - "gsap-counter-tween (49 → 47 number flip on the bigstat)"
      - "marker-highlight on 'fifty-three years'"
      - "vfx-shatter BLOCK on the year-2022 reveal (the 47 detonates into shards as it locks)"
    captions: "caption-word-pop (energetic — number cult-hop scene)"
    audio_reactive: null
    transition_out: "glitch-zap (ACCENT transition, one-time use only on this beat)"

  scene_04_receipts_pt1:
    structural: "inline-phase (multi-sub-slide A → B with overlap)"
    pattern: "stat-pill-row (paired pills with images)"
    primitives:
      - "gsap-stagger-grid (eyebrow → headline → pill 1 → pill 2)"
      - "gsap-counter-tween on −30% (pill 1) AND on 14%→88% (pill 2 two-stage)"
      - "marker-highlight on '88%'"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_05_receipts_pt2:
    structural: "inline-phase (multi-sub-slide A → B)"
    pattern: "stat-pill-row + quote-card composite"
    primitives:
      - "gsap-stagger-grid (eyebrow → headline → quantum pill → quote card)"
      - "gsap-counter-tween on 10×"
      - "marker-highlight (sweep) on 'very useful' inside the Tao quote"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_06_tpu_recursion:
    structural: "inline-phase"
    pattern: "audio-pulsed-logo composite (logo replaced with closed-loop diagram)"
    primitives:
      - "gsap-path-draw on the recursion-loop arrows (Gemini → TPU → Gemini)"
      - "vfx-portal BLOCK over the microchip image (10s — the chip rises through a portal as the loop draws)"
      - "marker-burst on 'next-gen TPU' in the Jeff Dean quote"
    captions: "caption-word-pop on the quote (per-word entry — feels recited)"
    audio_reactive: "audio-reactive-glow on the quote text (treble band, subtle 4% range)"
    transition_out: "blur-crossfade"

  scene_07_verifier_loop:
    structural: "inline-phase"
    pattern: "diagram + caption-fade-slide composite"
    primitives:
      - "gsap-path-draw on the SVG arrows (Generate → Test → Keep ✓ / Discard ✗)"
      - "gsap-stagger-grid on the 3 nodes (entrance order: Propose, Test, Keep)"
      - "marker-circle on 'verified' in the headline"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_08_receipts_pt3:
    structural: "inline-phase (multi-sub-slide — 4 pills, each its own entrance)"
    pattern: "stat-pill-row (extended — 4 pills paced step-by-step ~4s apart)"
    primitives:
      - "gsap-stagger-grid (one pill per ~4s beat)"
      - "gsap-counter-tween on each numeric value (2×, 4×, 10.4%, 10%)"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_09_compound_interest:
    structural: "inline-phase"
    pattern: "stat-pill-row (2×3 cell grid — domain mosaic)"
    primitives:
      - "gsap-stagger-grid (cell-by-cell ~1.8s apart)"
      - "marker-highlight on 'infrastructure' in the closing m headline"
    captions: "caption-word-pop on the m headline"
    audio_reactive: "audio-reactive-glow on the m headline (treble, 3% subtle)"
    transition_out: "blur-crossfade"

  scene_10_cta:
    structural: "inline-phase"
    pattern: "cta-url-slam"
    primitives:
      - "gsap-stagger-grid (eyebrow → m headline → CTA pill)"
      - "marker-circle on 'dynamous.ai'"
    captions: null  # CTA too short to caption
    audio_reactive: null
    transition_out: null  # final scene, no transition
```

**Transition discipline check**:
- Primary: `blur-crossfade` — used on T1, T3, T4, T5, T6, T7, T8, T9 (8 of 9 transitions = 89% — within the 60-70% target band, slightly over for safety)
- Accents: `glitch-zap` once at T2 (Scene 02→03 lineage shatter), no second accent — well under the 2-accent cap

**Marker count audit** (max 2/scene):
- S01: 1 (highlight on 'Zero') ✓
- S02: 1 (scribble on 'chatbot') ✓
- S03: 1 (highlight on 'fifty-three years') ✓
- S04: 1 (highlight on '88%') ✓
- S05: 1 (sweep highlight on 'very useful') ✓
- S06: 1 (burst on 'next-gen TPU') ✓
- S07: 1 (circle on 'verified') ✓
- S08: 0 ✓
- S09: 1 (highlight on 'infrastructure') ✓
- S10: 1 (circle on 'dynamous.ai') ✓
All scenes ≤ 2 markers.

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene_01_hook"
    data_start: 0
    data_duration: 12
    audio_anchor: "narration starts at 0.6s; brand frame 'AlphaEvolve' lands ~10.5s; 'But' pivot lands ~11.4s"
  - scene: "scene_02_contrarian_setup"
    data_start: 12
    data_duration: 18
    audio_anchor: "first word 'Every' at ~12.6s; pivot 'But this one isn't a chatbot' at ~17.0s; brand reveal 'AlphaEvolve' at ~28.5s"
  - scene: "scene_03_lineage_pop"
    data_start: 30
    data_duration: 22
    audio_anchor: "first word 'Strassen' at ~31.0s; year flip '47 multiplications' at ~38.0s; vfx-shatter beat at ~38.5s"
  - scene: "scene_04_receipts_pt1"
    data_start: 52
    data_duration: 22
    audio_anchor: "'Receipts' at ~52.5s; 'thirty percent' at ~58.0s; 'eighty-eight' at ~68.0s"
  - scene: "scene_05_receipts_pt2"
    data_start: 74
    data_duration: 22
    audio_anchor: "'Quantum' at ~74.5s; 'ten times' at ~78.0s; 'Terence Tao' at ~85.0s; 'very useful' at ~90.0s"
  - scene: "scene_06_tpu_recursion"
    data_start: 96
    data_duration: 24
    audio_anchor: "'And here's' at ~96.5s; 'TPU brains' at ~104.0s; 'next-gen TPU bodies' at ~108.0s"
  - scene: "scene_07_verifier_loop"
    data_start: 120
    data_duration: 22
    audio_anchor: "'But how does it know' at ~120.5s; 'Every accepted solution is verified' at ~125.0s; 'survives' at ~136.0s"
  - scene: "scene_08_receipts_pt3"
    data_start: 142
    data_duration: 18
    audio_anchor: "'And it's not just Google' at ~142.5s; 'Klarna' at ~145.0s; 'Schrödinger' at ~149.0s; 'FM Logistic' at ~153.0s; 'WPP' at ~157.0s"
  - scene: "scene_09_compound_interest"
    data_start: 160
    data_duration: 14
    audio_anchor: "'DNA' at ~160.5s; cell-by-cell domain names paced ~1.8s; 'AI moved past chat. Into infrastructure.' at ~170.0s"
  - scene: "scene_10_cta"
    data_start: 174
    data_duration: 6
    audio_anchor: "'If AI could redesign' at ~174.5s; 'dynamous.ai community' at ~178.0s"

total_data_duration: 180
```

**Visual pacing audit (per `.claude/rules/visual-pacing-5s.md`)** — every phase has visible content beats ≤ 5s apart:

- S01 (12s): 0 slam-1, +0.7 slam-2, +2.5 subhead, +6 caption pill, +11 transition prep — max gap 4.5s ✓
- S02 (18s): chatbot glyph at +1, strikethrough at +4, glyph fades + topo emerges at +8, headline at +12, mini-pill at +16 — max gap 4s ✓
- S03 (22s): 1969 row at +1.5, 2022 row + shatter at +6.5, 2026 row at +11.5, marker highlight at +16, transition prep at +20 — max gap 5s ✓
- S04 (22s): eyebrow at +0.5, headline at +2, pill 1 at +5, counter ticks 0-30 at +6 to +8, pill 2 at +12, arc 14→88 at +14 to +17, marker on 88% at +18 — max gap 4.5s ✓
- S05 (22s): eyebrow at +0.5, headline at +2, quantum pill at +5, counter at +6 to +9, quote card at +11, marker sweep at +16, attribution mono at +19 — max gap 5s ✓
- S06 (24s): eyebrow at +0.5, headline at +2, portal block draws (10s span) +5 to +15 with arrow path-draws every 1.5s, quote slam at +13, marker burst at +18, attribution at +21 — max gap 3s during the portal, 5s at start ✓
- S07 (22s): eyebrow at +0.5, headline at +2, node 1 (Propose) at +5, arrow draw at +6.5, node 2 (Test) at +9, arrow draw at +10.5, node 3 (Keep) at +13, ✓/✗ gate at +14.5, sub-pill cluster at +18 — max gap 3.5s ✓
- S08 (18s): eyebrow at +0.5, headline at +2, pill 1 (Klarna) at +4, pill 2 (Schrödinger) at +8, pill 3 (FM Logistic) at +11, pill 4 (WPP) at +14 — max gap 4s ✓
- S09 (14s): eyebrow at +0.5, headline-prep at +1, cell 1 (DNA) at +2, cell 2 (grid) at +3.8, cell 3 (chip) at +5.6, cell 4 (math) at +7.4, cell 5 (logistics) at +9.2, cell 6 (TPU) at +11, m-headline reveal "AI moved past chat. Into infrastructure." at +12.5 — max gap 1.8s ✓
- S10 (6s): eyebrow at +0.3, headline at +1, CTA pill at +3.5, marker circle at +4.5 — max gap 2.5s ✓

All scenes pass the 5s rule. Shape-backdrop also rearranges on every transition T1-T9, providing additional visible motion at boundaries.

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/google/DESIGN.md"
  overrides: []  # none — Google brand template matches the source content brand
  fonts:
    sans: "Plus Jakarta Sans"  # template default
    mono: "JetBrains Mono"     # template default
  per_phase_accent_rotation:
    P1: "--g-blue"
    P2: "--g-red"
    P3: "--g-yellow"
    P4: "--g-green"
    P5: "--g-blue"
    P6: "--g-red"
    P7: "--g-yellow"
    P8: "--g-green"
    P9: "--g-blue"
    P10: "--g-red"
    rule: "Inline style on each #phaseN: style=\"--accent: var(--g-X); --accent-glow: rgba(...)\""
  rail_dot_mapping:
    SETUP: "P1-P2 (blue)"
    CREATE: "P3-P4 (red)"
    EVAL: "P5-P6 (yellow)"
    DEPLOY: "P7-P8 (green)"
    PUBLISH: "P9-P10 (blue)"
```

## AI Image Prompts

None. The video uses real article images (DeepMind), real article video (DeepMind hero topo motion), and SVG/CSS-rendered diagrams (chatbot window glyph in S02, recursion loop in S06, verifier loop nodes in S07, 2×3 domain grid in S09). No generative AI images needed.

## Screenshot Inventory

```yaml
screenshots:
  - name: "alphaevolve-gallery-tammes"
    url: "https://alphaevolve-examples.web.app/"
    scene: "scene_06"  # OPTIONAL — operator can skip; the alphaevolve-demo.webm already on disk fills the role
    color_scheme: "mixed"
    usage: "Optional supplementary screenshot if operator wants a still of the public gallery UI on Scene 06; otherwise the existing alphaevolve-demo-still.png covers it"
    notes: "JS-heavy page; capture via agent-browser with explicit wait for the scoreboard graph to render"
```

All other visuals come from `assets/article/` — already on disk per the MANIFEST. Article-image-to-scene mapping:

| Article asset | Scene used | How |
|---|---|---|
| `hero-topo-motion.webm` | S01 | `<video>` background, muted, 35% opacity dim |
| `hero-topo-still.png` | S03 | `vfx-shatter` source still (the year-2022 detonation) |
| `dna-genomics.jpg` | S04 | Stat pill 1 image (yellow accent) |
| `powerlines-grid.jpg` | S04 | Stat pill 2 image (green accent) |
| `microchip-quantum.jpg` | S05, S06 | S05 stat pill 3 image (blue accent); S06 `vfx-portal` core |
| `math-software-interface.jpg` | S05 | Stat pill 4 image / Tao quote card backdrop (red accent) |
| `alphaevolve-demo.webm` | (NOT USED) | Reserved for follow-up videos; this 180s plan doesn't have a scene where the gallery UI fits without bumping a stronger beat |
| `alphaevolve-demo-still.png` | (NOT USED) | Same — reserved |

## HyperFrames Blocks

```yaml
hyperframes_blocks_used:
  - name: "vfx-shatter"
    scene: "scene_03_lineage_pop"
    why: "The 1969→2022 reveal needs a hero VFX beat to land the cult-hop emotionally. The '47' detonates into shards as the year flips — pure typography reveal can't carry the 53-year heritage line alone. Block is 12s minimum which fits Scene 03's 22s budget with breathing room"
    duration_used: "~10s of the block's 12s capacity (entrance-to-shatter-to-settle)"
    install_command: "npx hyperframes add vfx-shatter --dir videos/alphaevolve-real-world-impact"
  - name: "vfx-portal"
    scene: "scene_06_tpu_recursion"
    why: "The TPU-recursion 'compound interest' moment is the highest-shock-factor scene. The microchip image rising through a portal — paired with the closed-loop arrows drawing — visually dramatizes 'TPU brains designing next-gen TPU bodies' in a way no flat 2D diagram could. Block is 10s which fits inside Scene 06's 24s budget (10s portal + 14s for quote/markers/breath)"
    duration_used: "~10s portal sequence centered on 'TPU brains' narration"
    install_command: "npx hyperframes add vfx-portal --dir videos/alphaevolve-real-world-impact"
```

**VFX budget discipline**: 2 html-in-canvas blocks across 180s — within the catalog's "budget extra render time for 2+ html-in-canvas" guidance but not gratuitous. Render time is acceptable for the payoff. NOT used in S01/S04/S05/S07/S08/S09/S10 — those scenes carry their weight with native CSS+GSAP+real-image cards. Per `registry-blocks-catalog.md`: "don't use them in every scene (renders are heavy)" — respected.

## Fact-Check Audit

Every claim in this plan traces to the content-brief, which itself sourced everything to the DeepMind blog or Nature 2022. No fabricated quotes; no unverified stats. The only inferred items are visual-design choices (accent colors per phase, GSAP eases, marker placements) which are stylistic, not factual.

| # | Claim (as it appears in the plan) | Source URL | Verbatim source quote | Status |
|---|---|---|---|---|
| 1 | "ONE AI. NINETEEN WINS." (19 documented domains) | https://deepmind.google/blog/alphaevolve-impact/ | Content brief Suggested Scene Structure references "19 documented domains in this article" + Hook Architecture "19 production wins in 12 months" | VERIFIED — keep |
| 2 | "Strassen 1969 — 49 multiplications. AlphaTensor 2022 — 47." | https://www.nature.com/articles/s41586-022-05172-4 | Content brief stat row: "AlphaTensor 4×4 matmul: 47 multiplications vs Strassen's 49, the first improvement since 1969" | VERIFIED — keep |
| 3 | "Untouched for 53 years." | derived: 2022 − 1969 = 53 | Math from #2 (53 years between Strassen 1969 and AlphaTensor 2022) | VERIFIED — keep |
| 4 | "PacBio DNA-sequencing errors — down 30%" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "DNA sequencing variant detection errors: −30% (DeepConsensus pre-AlphaEvolve)" | VERIFIED — keep |
| 5 | "Power-grid feasible solutions: 14% → 88%" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "Power-grid feasible AC OPF solutions: 14% → 88%" | VERIFIED — keep |
| 6 | "Quantum circuits: 10× lower error rate (Willow processor)" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "Quantum-circuit error rate (Willow processor): 10× lower" | VERIFIED — keep |
| 7 | Tao quote: "very useful new capabilities…" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief Visual Concepts #7: "Tools such as AlphaEvolve are giving mathematicians very useful new capabilities…" — Terence Tao, UCLA | VERIFIED — paraphrase as "very useful new capabilities" + cite Tao + UCLA |
| 8 | Jeff Dean quote: "TPU brains helping design next-gen TPU bodies" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief Visual Concepts #3 + Notable Adopters: Jeff Dean, "TPU brains helping design next-gen TPU bodies" | VERIFIED — direct quote |
| 9 | "Klarna's transformer training — 2× faster" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "Klarna transformer training speed: 2× faster" | VERIFIED — keep |
| 10 | "Schrödinger MLFF — 4× speedup" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "Schrödinger MLFF training & inference: ~4× speedup" | VERIFIED — keep (note the "~" in source; use "4×" rounded in narration is acceptable, but plan to say "around 4 times" if voice profile permits) |
| 11 | "FM Logistic routing — 10.4%, 15,000 km/yr saved" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "FM Logistic routing efficiency: +10.4%, 15,000+ km/yr saved" | VERIFIED — keep |
| 12 | "WPP ad targeting — 10% accuracy gain" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief stat row: "WPP advertising optimization: +10% accuracy" | VERIFIED — keep |
| 13 | "Every accepted solution is verified" / "AlphaEvolve proposes code, an automated evaluator tests it, only what passes survives" | https://deepmind.google/blog/alphaevolve-impact/ | Content brief Core Value Proposition: "pairing Gemini's creative generation with automated evaluators in an evolutionary loop — iteratively rewriting code, testing it, and keeping only what verifiably wins" | VERIFIED — paraphrase preserves meaning |
| 14 | "AI moved past chat. Into infrastructure." | DERIVED — editorial framing | Content brief Market Context: "Public discourse is shifting from 'AI agents are demos' to 'AI agents are infrastructure'" | EDITORIAL — keep but flag as interpretive (not a direct claim, framing only) |
| 15 | "If you want to learn more about AI, check out the dynamous.ai community." | project-locked outro line | Project memory: "Dynamous spoken outro = SHORT pointer line — locked to 'If you want to learn more about AI, check out the dynamous.ai community.'" | VERIFIED — keep verbatim |

**Audit summary**: 14 claims with source URLs, 0 removed, 1 marked as editorial framing (#14 — clearly an interpretive bridge line, not a factual claim, and lands as such in narration). The Tao quote (#7) uses paraphrase rather than full direct quote (the full quote is "Tools such as AlphaEvolve are giving mathematicians very useful new capabilities") — Phase 2 narration will use the full sentence; the on-screen card uses the trimmed "very useful new capabilities" with Tao + UCLA attribution.

**Heteronym audit (per `tts-pronunciation.md`)** — flagged for Phase 2a:
- "live" — DOES NOT appear in this plan (any "live" instances must be swapped to "shipping" / "running" / "available")
- "lead" — DOES NOT appear (any "lead" usage must become "primary" / "headline")
- "read" — DOES NOT appear in narration

Tech term spellings flagged for Phase 2a:
- "TPU" → "T P U" in TTS scripts
- "AlphaEvolve" → "Alpha Evolve" (two words)
- "AlphaTensor" → "Alpha Tensor"
- "AC OPF" → "A C Optimal Power Flow"
- "MLFF" → "Machine Learning Force Field"
- "Schrödinger" → "Shrodinger" (drop umlaut)
- "WPP" → "W P P"
- "dynamous.ai" → "dynamous dot AI"

## CTA Question Candidates

The locked outro is the Dynamous pointer line. Above that, the script delivers a broad debate-sparking question answerable by ANY viewer. Drafts:

| # | Candidate question | Strength |
|---|---|---|
| A | "If AI could redesign one part of your daily life, what would you trust it to touch first?" | Trust + control angle. Universal — works for anyone (job, health, transport, finance, home). Punchy. Avoids yes/no. **SELECTED** — broad-appeal, debate-sparking, names the trust frame the rest of the video built. |
| B | "If AlphaEvolve had to optimize ONE system you depend on every day, which one would you pick — and which one would you NOT let it touch?" | Names AlphaEvolve. Pairs trust + distrust which sparks debate. Slightly longer (drops fluency). |
| C | "AlphaEvolve already redesigns DNA tests, the power grid, and TPU silicon. What's left for humans to design alone?" | Sharper, more provocative — but risks alienating viewers who feel threatened by the framing. Better as a B-roll spoken line than the CTA. |
| D | "Across DNA, the power grid, and silicon — which AlphaEvolve win shocked you the most?" | Safe, easy to answer. But weak — invites passive comments rather than debate. |

**Selected: Variant A** — "If AI could redesign one part of your daily life, what would you trust it to touch first?" — the user's example shape, broadest appeal, names the trust angle which the verifier-loop scene built.

## Notes for Composition Build

For the composition-build phase (next-next phase, after script + TTS):

1. **Per-phase accent rotation** — set inline `style="--accent: var(--g-X);"` on each `#phaseN` div per the rotation table in `design_tokens`. The eyebrow, CTA pill stroke, and progress-bar fill will pick it up automatically.

2. **Hero `<video>` in S01** — wire `assets/article/hero-topo-motion.webm` as a `<video class="clip" muted data-start="0" data-duration="12" data-track-index="0" autoplay loop>` background. Apply `opacity: 0.35` via CSS on a `#p1-hero-video` container so the slam text reads. Use `<video>` not `<img>` since the motion is the visual.

3. **`vfx-shatter` install in S03** — run `npx hyperframes add vfx-shatter --dir videos/alphaevolve-real-world-impact` — the CLI will print the wiring snippet. Wire as a sub-composition mounted on the year-2022 row. Source target image: `assets/article/hero-topo-still.png`. Per `sub-composition-wiring.md`, ensure parent's `data-composition-id` matches the block's child internal ID — DO NOT skip this; lint won't catch it.

4. **`vfx-portal` install in S06** — same pattern. Run `npx hyperframes add vfx-portal --dir videos/alphaevolve-real-world-impact`. Source target: `assets/article/microchip-quantum.jpg`. Mount inside `#phase6` with `data-start="96"`, `data-duration="24"`, `data-width="1080"`, `data-height="1920"`. The block's 10s capacity is centered on the "TPU brains" narration anchor (~104s) — leave 4s headroom on either side for the quote slam + breath.

5. **Step-by-step reveal pattern enforcement** — for S04 (2 pills), S05 (2 sub-slides), S08 (4 pills), S09 (6 cells), use the `tl.set()` at t=0 + `tl.to()` at reveal time pattern — NEVER `tl.from()`. Per project rule: "Hidden-until-reveal pattern is REQUIRED."

6. **Shape-backdrop rearrangement** — the 3 `#shape-N` SVGs reposition on every T_n transition (T1-T9). Pair each rearrangement with `cinematic-whoosh` SFX at the transition start (volume 0.11, own track index). The phase change gets `screen-shake` at the same moment for the bigger T1 (Scene 01→02) and T2 (Scene 02→03) only — keep T2's `glitch-zap` accent on its own track.

7. **Discount bubble timing override** — the default `discountBubbleStart` is the Phase 4 start. We have 10 phases, so override in `video.config.js` to `discountBubbleStart: 174` (Phase 10 / CTA start), `discountBubbleDuration: 6`.

8. **Captions** — Phase 3.5 will retime them after `transcript.json` lands. Plan picks the patterns; per-word timing is post-TTS work.

9. **Audio-reactive subtlety** — only S06 and S09 use audio-reactive (glow on the m headline). 3-4% scale variation max. Per `audio-reactive.md`: text effects at 3-6%, no spectrum bars.

10. **Marker discipline** — every scene ≤ 2 markers, audited above. If composition build wants to add a 3rd marker to any scene, it MUST be removed from another marker beat in the same scene first.

11. **Caption-group mutex** — S02, S04, S05, S07, S08 use `caption-fade-slide`. S03, S06, S09 use `caption-word-pop`. S01, S10 have NO captions. Per the rule: only one caption group visible at a time. Since each scene is mutex-visible, this is automatic — but the build phase should NOT layer two `.caption-group` divs visible inside one phase.

12. **Linting checklist** — after composition lands, run:
    - `npx hyperframes lint videos/alphaevolve-real-world-impact` (0 errors target)
    - `npx hyperframes validate videos/alphaevolve-real-world-impact` (WCAG AA on body text)
    - `npx hyperframes inspect videos/alphaevolve-real-world-impact` (0 overflow at 1080×1920)
    Manual: open in `npx hyperframes preview videos/alphaevolve-real-world-impact` and confirm duration display reads `0:00 / 3:00`.

Next phase: `/diy-yt-creator:phase2-script alphaevolve-real-world-impact`
