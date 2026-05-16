# Composition Plan: anthropic-amazon-compute

## Director's Summary

A 45-second punchy news-explainer that frames Anthropic's $100B / 5 GW Amazon compute pact as the structural fix for the April-2026 Claude reliability crunch — not just a press-release dollar number, but a chip-supply-chain pivot away from Nvidia. The hook leverages the "ditching Nvidia" contrarian angle paired with a city-scale power metaphor (5 GW = NYC), then earns trust with Pfizer/Lyft proof and lands on a dev-facing CTA. Tone is informed, slightly contrarian, edge-of-tech-influencer — the Anthropic Shorts dark-stage aesthetic stays serious; the energy comes from cadence and percussive SFX, not visual chaos.

## Template & Structure

- **Template**: `templates/shorts/anthropic` (1080x1920, 30fps)
- **Composition layout model**: `inline-phase` + `mutex-visibility` (template-forced — single `index.html` with eight `.phase` divs P0–P7, no sub-compositions)
- **Duration target**: 45s
- **Background music**: NONE (Anthropic Shorts forbids BG music — narration + SFX only)
- **Design token overrides**: none — use template defaults verbatim. Accent rotation per the rule "no two adjacent phases share the same accent": orange (P0) → orange/red glow (P1, tension) → orange (P2, hero stat) → purple (P3, chip swap) → blue (P4, Rainier) → green (P5, multi-cloud anchor) → green/orange (P6, proof) → orange (P7, CTA).

## Master Timeline

| Scene | data_start | data_duration | Visual Goal                                                                 | Key Elements                                                                                          |
| ----- | ---------- | ------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 00 — Preview Hook   | 0   | 4 | Anthropic + AWS lockup with `$100B` stamp slam — set stakes in 4s          | Title-card "100 BILLION" 240px slam, Anthropic+AWS lockup, JetBrains-Mono overline "APRIL 2026"        |
| 01 — The Tension    | 4   | 6 | Rate-limit error toast / status-page red — pain of the crunch              | "rate_limit_exceeded" red toast, status-dot row turning red, secondary line "Claude was throttling paid users" |
| 02 — The Reveal     | 10  | 6 | Power-meter sweep to 5 GW; NYC skyline — contrarian snapback                | 240px slam "5 GIGAWATTS", NYC skyline silhouette behind, caption pill "≈ New York City"               |
| 03 — Chip Swap      | 16  | 6 | H100 → Trainium2 morph + price flip — "not Nvidia"                          | Two stat pills "$3/hr H100" → "$1/hr Trainium2", purple accent, headline "Bypassing Nvidia"           |
| 04 — Project Rainier| 22  | 6 | Indiana site reveal; chip counter rolls to 1M — proves it's real            | Counter "0 → 1,000,000+ chips", blue accent, sublabel "$11B · 1,200 acres · Indiana · live today"    |
| 05 — Multi-cloud anchor | 28 | 5 | 3-cloud diagram, AWS edge thickens — answer the lock-in objection         | 3 mono pills "AWS · GCP · AZURE", green accent on AWS, headline "still multi-cloud"                  |
| 06 — Proof          | 33  | 6 | Pfizer / Lyft stat cards — Fortune-500 social proof                         | Two timeline-style cards: "Pfizer −55% infra cost / 16,000 hrs saved" and "Lyft 87% faster"           |
| 07 — CTA            | 39  | 6 | Claude logo + URL pill — "the crunch is easing"                             | URL pill `claude.com`, subscribe pill, marker-circle on URL                                           |

**Total `data_duration`: 45s** (sum: 4+6+6+6+6+5+6+6 = 45)

## Narrative Arc

Kallaway formula mapping (45s short, slightly compressed):

1. **Context Lean-In** (Scene 00, 4s — 9% of duration): "Anthropic just bet $100 billion on Amazon's chips." → topic clarity in line 1.
2. **Scroll-Stop Interjection** (start of Scene 02, transition word "But"): "But the dollar amount isn't the real story."
3. **Contrarian Snapback** (Scene 02): "It's 5 gigawatts of custom silicon — bypassing Nvidia."
4. **Solution** (Scenes 03 + 04, 12s — 27%): chip cost flip + Project Rainier proof — already running, not vaporware.
5. **Deep Dive / Feature Beats** (Scenes 03–05, 17s — 38%): chip swap, Rainier scale, multi-cloud preserved.
6. **Social Proof / Trust** (Scene 06, 6s — 13%): Pfizer / Lyft stat cards.
7. **CTA** (Scene 07, 6s — 13%): "If you build on Claude — peak-hour limits are easing."

**Explosion timer**: unique value (the $100B + 5 GW number) lands inside the first 4 seconds via Scene 00.

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Wait — Anthropic just ditched Nvidia for 5 gigawatts of Amazon's own chips."
    layers_present: [1, 4, 5]
    scoring:
      curiosity_gap: 9
      stakes_clarity: 6
      specificity: 8
      base: 7.7
      stun_bonus: 0.0          # no But/However/Yet
      alignment_bonus: 1       # names Anthropic + Nvidia + 5 GW (the topic)
      promise: 0               # no explicit "here's why"
    advisory_score: 8.7

  variant_b:
    type: "stakes"
    opening_line: "If you got rate-limited on Claude this April — Anthropic just spent $100 billion to fix it."
    layers_present: [2, 3, 4, 5]
    scoring:
      curiosity_gap: 8
      stakes_clarity: 10       # quantified $100B + named pain (rate-limit)
      specificity: 9           # specific stat in opening line
      base: 9.0
      stun_bonus: 0.0
      alignment_bonus: 1       # names the problem and the spend in line 1
      promise: 1               # "to fix it" = explicit promise
    advisory_score: 10.0

  variant_c:
    type: "number"
    opening_line: "5 gigawatts. $100 billion. One million chips. None of them Nvidia."
    layers_present: [1, 3, 4, 5]
    scoring:
      curiosity_gap: 9
      stakes_clarity: 7
      specificity: 10          # three specific stats in opening line
      base: 8.7
      stun_bonus: 0.0
      alignment_bonus: 1
      promise: 0
    advisory_score: 9.7

  recommended: "variant_b"
  rationale: "Variant B opens with named viewer pain (rate-limited on Claude this April), quantified stakes ($100B), and an explicit promise of resolution (to fix it). It validates the click for the dev audience — they CLICKED because they hit rate limits — instead of leading with abstract scale (variant C) or pure contrarian flex (variant A). Highest advisory score (10.0) and best Value Alignment for the primary audience (developers building on Claude)."
```

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "ContrastPivot"
  pattern_rationale: "Stakes hook with a contrarian payload (the real story isn't the dollars, it's the Nvidia bypass). Build the rate-limit context, smash-cut to the $100B reveal, then to the contrarian 5 GW / not-Nvidia framing. ContrastPivot beats StatCascade here because the script needs the BUT pivot from pain → fix; pure stat cascade would skip the emotional setup that earns the click."
  selected_variant: "variant_b"

  visual_beats:
    - beat: "Cold Open"
      timing_s: [0, 1]
      visual: "Pure #0B0F18 canvas; Anthropic + AWS lockup fades up at top; 'APRIL 2026' overline mono-pulses in"
      gsap_ease: "power3.out"
      sfx: null
    - beat: "Stakes Slam"
      timing_s: [1, 4]
      visual: "240px '$100B' slam-in (orange), inline shake on impact; caption pill '10-year compute deal' under"
      gsap_ease: "back.out(1.7)"
      sfx: "single impact-slam"
    - beat: "Pain Context (P1)"
      timing_s: [4, 10]
      visual: "Red 'rate_limit_exceeded' toast slides in; status-dot row flips red one-by-one; mono caption 'Pro/Max users · peak hours · April 2026'"
      gsap_ease: "power4.out"
      sfx: "single impact-slam (subdued)"
    - beat: "PIVOT"
      timing_s: [10, 10.4]
      visual: "Hard cut: red toast crossed-out; 240px '5 GW' slam-in (orange) over NYC skyline silhouette; small mono pivot word 'BUT'"
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake + glitch-zap (each on its own data-track-index)"
    - beat: "Reveal (P2)"
      timing_s: [10.4, 16]
      visual: "Skyline lights tick on across the meter; caption pill '≈ New York City' snaps in; subhead 'custom silicon. not Nvidia.'"
      gsap_ease: "power3.out"
      sfx: "scale-slam"
    - beat: "Rapid-Fire Body (P3 → P6)"
      timing_s: [16, 39]
      visual: "Chip swap → Rainier counter → 3-cloud diagram → Pfizer/Lyft cards. Each phase is a `.phase` div using its archetype (stat-pill-row, narrated-stat-reveal, timeline-cards)."
      gsap_ease: "back.out(1.7) on slams; power2.out on chips; stagger 200-280ms between cards"
      sfx: "spring-pop per card; scale-slam on each stat number"
    - beat: "CTA (P7)"
      timing_s: [39, 45]
      visual: "URL pill 'claude.com' rises; marker-circle hand-draws around it; subscribe pill enters from right"
      gsap_ease: "expo.out on URL slam; power2.out on subscribe pill"
      sfx: "single spring-pop on URL settle"

  pivot_word: "But"
  brand_reveal_word: "Anthropic"  # appears in Scene 00 narration line 1 alongside Amazon

  assets_needed:
    - type: "logo"
      description: "Anthropic wordmark (light variant for dark stage)"
      source: "shared/logos/anthropic-logo-light.svg"
    - type: "logo"
      description: "AWS wordmark (light variant)"
      source: "shared/logos/aws-logo-light.svg or aws-light.png — verify in shared/logos/"
    - type: "logo"
      description: "Nvidia wordmark for the Scene 03 'bypassing' beat (greyed/struck-through)"
      source: "shared/logos/nvidia-logo-light.svg — verify; else stylized text"
    - type: "logo"
      description: "GCP + Azure wordmarks for Scene 05 multi-cloud diagram"
      source: "shared/logos/google-cloud-logo-light.svg, shared/logos/azure-logo-light.svg — verify"
    - type: "logo"
      description: "Pfizer + Lyft wordmarks for Scene 06 proof cards"
      source: "shared/logos/pfizer-logo-light.svg, shared/logos/lyft-logo-light.svg — verify"
    - type: "screenshot"
      description: "Anthropic announcement page (anthropic.com/news/anthropic-amazon-compute) — used as background fragment in Scene 00 if room"
      source: "TBD — capture in composition build via /agent-browser"
    - type: "screenshot"
      description: "status.claude.com peak-hour incident view (use historical date, not live)"
      source: "TBD — capture in composition build"
    - type: "image"
      description: "NYC skyline silhouette (vector or stylized) for Scene 02 power-meter background"
      source: "TBD — generate or source CC0 vector in composition build"
    - type: "image"
      description: "Indiana state outline + Project Rainier site marker for Scene 04"
      source: "TBD — vector outline + marker in composition build"

  music_profile:
    hook_mood: "NONE"  # template forbids background music on Shorts
    note: "Anthropic Shorts: narration + SFX only (DESIGN.md, README.md 'Don'ts')"
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 00 (Preview Hook) + Scene 01 (Tension)"
    setup_line: "If you got rate-limited on Claude this April — Anthropic just spent $100 billion to fix it."
    resolution_scene: "Scene 07 (CTA)"
    resolution_line: "If you build on Claude — peak-hour limits are easing."
    type: "promise"
    why: "The hook promises a fix; the CTA delivers the resolution. Loop pays off in 45s."

  loop_openers: []
  loop_opener_note: "45s short — too compressed for explicit cadenced loop openers. Hook variant carries the loop alone. The 'But the dollar amount isn't the real story' transition into Scene 02 functions as an implicit mid-video re-hook."
```

## Story Lock Placement

- **Term Branding (Lock #1)**: "the reliability crunch" / "the compute crunch" — coin in Scene 01, echo in Scene 07. Frames the entire narrative around a named problem.
- **Negative Frame (Lock #4)**: skip — would shame the user (e.g. "stop using rate-limited APIs"). Brief is news-explainer, not how-to.
- **Thought Narration (Lock #3)**: optional one beat after Scene 02 reveal: "(That's a city's worth of power going to one company.)" — parenthetical, low volume.
- **Loop Openers (Lock #5)**: see open_loop_architecture above — none cadenced; the BUT pivot at Scene 02 is the only mid-video tension reset.

## Composition Layout

```yaml
composition_layout:
  template: "shorts/anthropic"
  structural_model: "inline-phase + mutex-visibility"
  total_phases: 8       # P0 through P7
  phase_naming: "P0 → T0 → P1 → T1 → P2 → T2 → P3 → T3 → P4 → T4 → P5 → T5 → P6 → T6 → P7"
  primary_transition: "blur-crossfade"      # 60-70% of scene changes
  accent_transitions:
    - name: "zoom-through"
      where: "T1 → T2 (the Pain → Reveal pivot, scenes 01 → 02)"
      why: "Punchy handoff matching the BUT pivot beat"
    - name: "staggered-blocks"
      where: "T5 → T6 (multi-cloud → proof, scenes 05 → 06)"
      why: "Card-style handoff into proof cards"
  background_music: false
```

## Retention Component Picks

```yaml
retention_component_picks:
  scene_00_preview:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam"
    primitives:
      - "gsap-stagger-grid"           # overline → slam → caption pill
      - "marker-highlight on '$100B'" # max 1 marker on this scene
    captions: null                    # 4s too tight for synced captions
    audio_reactive: null              # narration too short to react against
    transition_out: "blur-crossfade"

  scene_01_tension:
    structural: "inline-phase"
    pattern: "stat-pill-row (adapted — single red status pill instead of dual stat)"
    primitives:
      - "gsap-stagger-grid"            # status dots flip red in sequence
      - "marker-scribble on 'rate_limit_exceeded'"  # crossing out the wrong state
    captions: null
    audio_reactive: null
    transition_out: "zoom-through"     # accent transition — the BUT pivot

  scene_02_reveal:
    structural: "inline-phase"
    pattern: "hero-slam"
    primitives:
      - "gsap-counter-tween"           # power meter ticks 0 → 5
      - "marker-highlight on 'New York City'"   # 1 marker
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_chip_swap:
    structural: "inline-phase"
    pattern: "stat-pill-row"
    primitives:
      - "gsap-counter-tween"           # $3 → $1 price flip
      - "gsap-stagger-grid"            # H100 pill exits, Trainium pill enters staggered
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_04_rainier:
    structural: "inline-phase"
    pattern: "narrated-stat-reveal"
    primitives:
      - "gsap-counter-tween"           # 0 → 1,000,000+ chips
      - "gsap-stagger-grid"            # sublabel chips ($11B / 1,200 acres / Indiana) stagger in
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_05_multicloud:
    structural: "inline-phase"
    pattern: "timeline-cards (adapted as 3-pill row instead of dated cards)"
    primitives:
      - "gsap-stagger-grid"            # AWS / GCP / AZURE pills enter L→R
      - "marker-highlight on 'multi-cloud'"
    captions: null
    audio_reactive: null
    transition_out: "staggered-blocks" # accent transition into proof cards

  scene_06_proof:
    structural: "inline-phase"
    pattern: "timeline-cards"
    primitives:
      - "gsap-stagger-grid"            # 2 cards stagger 200-280ms
      - "gsap-counter-tween"           # 55%, 87%, 16,000 hrs all tween
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_07_cta:
    structural: "inline-phase"
    pattern: "cta-url-slam"
    primitives:
      - "marker-circle on 'claude.com'"
      - "gsap-stagger-grid"            # subscribe pill follows URL
    captions: null
    audio_reactive: null
    transition_out: null               # final scene
```

**Component pick counts (for the dashboard summary):**
- Markers: 5 total across all scenes (1 highlight in P0, 1 scribble in P1, 1 highlight in P2, 1 highlight in P5, 1 circle in P7) — under cap of 2/scene
- Captions: 0 (45s short — narration carries it; transcript-driven captions would crowd 240px slam words)
- Audio-reactive effects: 0 (narration too sparse / scenes too short for per-frame sampling to read)
- Transitions: 1 primary (`blur-crossfade`) + 2 accents (`zoom-through`, `staggered-blocks`) — within "1 primary + 1-2 accents" rule
- GSAP effects: `gsap-stagger-grid` (7 scenes), `gsap-counter-tween` (4 scenes)
- Composite patterns used: `hero-slam` x2, `stat-pill-row` x2, `timeline-cards` x2, `narrated-stat-reveal` x1, `cta-url-slam` x1

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene_00_preview"
    data_start: 0
    data_duration: 4
    audio_anchor: "narration starts at 0.4s; '$100B' spoken at ~2.0s"
    on_screen_words: ~6   # "$100B / 5 GW / Not Nvidia / APRIL 2026" — minimum 3-4s ✓
  - scene: "scene_01_tension"
    data_start: 4
    data_duration: 6
    audio_anchor: "'rate-limited' spoken at ~5.0s; 'April 2026' anchor at ~8.5s"
    on_screen_words: ~10  # toast + caption — minimum 4-6s ✓
  - scene: "scene_02_reveal"
    data_start: 10
    data_duration: 6
    audio_anchor: "'But' pivot at 10.1s; '5 gigawatts' spoken at ~10.8s; 'New York City' at ~13.5s"
    on_screen_words: ~7   # slam + caption — minimum 4-6s ✓
  - scene: "scene_03_chip_swap"
    data_start: 16
    data_duration: 6
    audio_anchor: "'$3 an hour' spoken at ~17.5s; '$1' flip at ~19.0s; 'bypassing Nvidia' at ~20.5s"
    on_screen_words: ~12  # two pills + headline — minimum 4-6s ✓
  - scene: "scene_04_rainier"
    data_start: 22
    data_duration: 6
    audio_anchor: "'Project Rainier' at ~22.5s; 'one million chips' at ~25.0s"
    on_screen_words: ~14  # counter + 4 sublabel chips — minimum 4-6s ✓
  - scene: "scene_05_multicloud"
    data_start: 28
    data_duration: 5
    audio_anchor: "'still on AWS, GCP and Azure' span ~28.5s–31.5s"
    on_screen_words: ~6   # 3 pills + headline — minimum 3-4s ✓
  - scene: "scene_06_proof"
    data_start: 33
    data_duration: 6
    audio_anchor: "'Pfizer' at ~33.7s; 'Lyft' at ~36.2s"
    on_screen_words: ~16  # 2 cards w/ stat + label — minimum 4-6s ✓
  - scene: "scene_07_cta"
    data_start: 39
    data_duration: 6
    audio_anchor: "'If you build on Claude' at ~39.5s; URL spoken at ~42.5s"
    on_screen_words: ~5   # URL pill + subscribe pill — minimum 3-4s ✓
total_data_duration: 45
notes: "audio_anchor values are PLACEHOLDERS — Phase 3.5 will refine against transcript.json once TTS+transcribe have run."
```

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []           # use template defaults verbatim
  accent_rotation:
    scene_00: "orange"     # hero stat $100B
    scene_01: "red"        # WARNING accent only — rate_limit_exceeded
    scene_02: "orange"     # hero stat 5 GW (orange leads hero per DESIGN.md rule)
    scene_03: "purple"     # secondary feature — chip swap
    scene_04: "blue"       # technical — Rainier facility
    scene_05: "green"      # positive — still multi-cloud
    scene_06: "orange"     # back to hero accent for proof cards (no adjacency conflict — green precedes)
    scene_07: "orange"     # CTA always orange
  fonts:
    sans: "Inter"            # 500/600/800/900 — DO NOT change
    mono: "JetBrains Mono"   # 700/900 — DO NOT change
  red_accent_note: "Scene 01 uses #D14343 only on the 'rate_limit_exceeded' toast badge per DESIGN.md ('never decorative'). Scene 06 if any regression callouts surface — none currently planned."
```

## AI Image Prompts

```yaml
images:
  - scene: "scene_02_reveal"
    name: "scene-02-nyc-skyline-silhouette"
    prompt: "Minimal vector silhouette of the New York City skyline (Empire State Building, One World Trade, Chrysler Building, generic mid-rise filler) rendered as a single warm off-white (#F5F1EB) shape on transparent background, 9:16 aspect, low ink coverage (~15% pixels filled), no text, no labels, no detail above building outlines, suitable as a subtle background under a 240px hero slam word. Vector-clean edges, no photoreal lighting, no sky, no foreground."
    aspect_ratio: "9:16"
    usage: "Background silhouette behind the '5 GIGAWATTS' slam word in Scene 02"
  - scene: "scene_04_rainier"
    name: "scene-04-indiana-outline"
    prompt: "Minimal vector outline of the U.S. state of Indiana, single 2px stroke in warm off-white (#F5F1EB), with a small filled circle marker at New Carlisle (northwest corner near South Bend). Transparent background, 1:1 aspect, no text labels, no other states, no compass rose, no shading. Suitable as a small inline diagram element."
    aspect_ratio: "1:1"
    usage: "Inline diagram in the Scene 04 sublabel row to anchor 'Indiana'"
```

Note: prompts deferred to composition-build phase; Imagen/Midjourney will not render text reliably so we keep both prompts text-free.

## Screenshot Inventory

```yaml
screenshots:
  - name: "anthropic-announcement-hero"
    url: "https://www.anthropic.com/news/anthropic-amazon-compute"
    scene: "scene_00_preview"
    color_scheme: "light"
    usage: "Optional faint background fragment behind the $100B slam (≤30% opacity); alternative is pure dark canvas"
    capture_via: "/agent-browser at composition-build time"
  - name: "claude-status-page-incident"
    url: "https://status.claude.com/"
    scene: "scene_01_tension"
    color_scheme: "light"
    usage: "Optional small inset showing red status dot — use historical capture, not live"
    capture_via: "/agent-browser at composition-build time"
    note: "If live status is green at capture time, fall back to a stylized recreation — DO NOT fake a red incident on the live page."
  - name: "aws-trainium-chip-hero"
    url: "https://aws.amazon.com/ai/machine-learning/trainium/"
    scene: "scene_03_chip_swap"
    color_scheme: "light"
    usage: "Crop the Trainium chip die-shot for the morph target (H100 → Trainium2)"
    capture_via: "/agent-browser at composition-build time"
  - name: "aws-project-rainier-aerial"
    url: "https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster"
    scene: "scene_04_rainier"
    color_scheme: "light"
    usage: "Aerial concept-render thumbnail behind the chip counter"
    capture_via: "/agent-browser at composition-build time"
```

## HyperFrames Blocks

```yaml
hyperframes_blocks_used: []
note: "No registry blocks required — the 8 phases are all template-native (hero-slam / stat-pill-row / timeline-cards / cta-url-slam from templates/shorts/anthropic)."
```

## Fact-Check Audit

Every claim that will appear in script narration or on-screen text, with a source URL or a removal/rephrase note. Phase 2b will re-verify these against the live sources.

| # | Claim (as it will appear in narration or on screen)                              | Source URL                                                                                                                                                              | Status                            |
|---|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| 1 | "$100 billion over 10 years" (Anthropic AWS spend commitment)                    | https://www.anthropic.com/news/anthropic-amazon-compute                                                                                                                  | sourced — primary                  |
| 2 | "5 gigawatts" of new compute capacity                                            | https://www.anthropic.com/news/anthropic-amazon-compute                                                                                                                  | sourced — primary                  |
| 3 | "5 GW ≈ New York City scale"                                                     | https://asteriskmag.com/issues/09/can-we-build-a-five-gigawatt-data-center                                                                                               | sourced — analytical proxy; phrase as "roughly New York City scale" not exact equivalence |
| 4 | "Trainium2, 3, 4" chip family / "bypassing Nvidia"                              | https://www.anthropic.com/news/anthropic-amazon-compute + https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-launches-trainium3-ai-accelerator-competing-directly-against-blackwell-ultra-in-fp8-performance-new-trn3-gen2-ultraserver-takes-vertical-scaling-notes-from-nvidias-playbook | sourced                            |
| 5 | "$3/hr H100 vs $1/hr Trainium" pricing                                           | https://knowledge.businesscompassllc.com/aws-trainium2-vs-nvidia-h100-a-complete-comparison-for-ai-workloads/                                                            | sourced — phrase as "roughly" since pricing varies by region/contract |
| 6 | "30–40% better price-performance" Trainium2 vs H100                              | https://knowledge.businesscompassllc.com/aws-trainium2-vs-nvidia-h100-a-complete-comparison-for-ai-workloads/                                                            | sourced                            |
| 7 | "Project Rainier — already running, 1M+ Trainium2 chips in use"                  | https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai + https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster | sourced                            |
| 8 | "Rainier site: $11B, 1,200 acres, Indiana" / "500K Trainium2 chips live"         | https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html + https://datacentremagazine.com/news/aws-how-500-000-trainium2-chips-power-project-rainier | sourced                            |
| 9 | "Claude on AWS, GCP, and Azure" (multi-cloud)                                    | https://www.anthropic.com/news/anthropic-amazon-compute                                                                                                                  | sourced                            |
| 10 | "Pfizer: 16,000 hours/year saved, 55% lower infra cost"                         | https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai                                                                           | sourced                            |
| 11 | "Lyft: 87% faster customer-service resolution"                                  | https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai                                                                           | sourced                            |
| 12 | "Claude was rate-limiting paid users in April 2026 / peak hours 8am–2pm ET"     | https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/                            | sourced — phrase as "this April" (ties to recency) |
| 13 | "$30B run-rate, ahead of OpenAI's $25B"                                          | https://www.bloomberg.com/news/articles/2026-04-06/broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic                                                          | DEFER — likely cut for time; if used, attribute "according to Bloomberg" |
| 14 | "Trainium3 4.4× compute over Trainium2"                                          | https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-launches-trainium3-ai-accelerator-competing-directly-against-blackwell-ultra-in-fp8-performance-new-trn3-gen2-ultraserver-takes-vertical-scaling-notes-from-nvidias-playbook | DEFER — likely cut for time per brief's "Could Include" tier |
| 15 | "OpenAI Stargate $500B"                                                          | https://time.com/7273288/amazon-anthropic-openai-microsoft-stargate-datacenters/                                                                                         | DEFER — out of scope for 45s; not in current scene plan |
| 16 | Direct-speech quotes attributed to Andy Jassy / Dario Amodei                    | n/a                                                                                                                                                                      | NOT USED — paraphrase only if used; Phase 2 will not generate fabricated quotes |

**Audit summary**: 16 candidate claims tracked. 12 sourced and IN-PLAN; 3 deferred (likely cut for 45s budget — must be removed by Phase 2 or rephrased with attribution); 1 explicitly excluded (no fabricated quotes). Zero unsourced claims survive in the plan.

## Notes for Composition Build

1. **Phase naming convention**: Follow the template's `P1, T1, P2, T2…` pattern but extend to 8 phases — this plan uses P0–P7 so the index.html will need ids `phase0` through `phase7` with z-index matching scene order. Bump `#root` `data-duration="45"`.
2. **Top banner**: Use `shared/logos/anthropic-logo-light.svg` for the persistent top banner (240px safe zone). DO NOT add an AWS lockup to the persistent banner — only Scene 00 shows the lockup as inline content.
3. **Red accent in Scene 01**: Use `#D14343` ONLY on the rate_limit_exceeded toast badge. Per DESIGN.md, red is "never decorative" — keep it on the chip/badge, never headline body.
4. **`<br>` ban**: Per DESIGN.md "What NOT to Do" — every multi-line text element uses `max-width` for natural wrapping, never `<br>`.
5. **Padding rule**: Every `.phase-content` MUST be `padding: var(--pad-top) var(--pad-x) var(--pad-bottom)` — never `position: absolute; top: Npx`.
6. **SFX volumes**: per DESIGN.md cap (≤0.20 on most beds; layered hooks count as separate tracks). Scene 02 PIVOT layers 3 SFX (impact-slam @ 0.20, screen-shake @ 0.13, glitch-zap @ 0.12) on three different `data-track-index` values so they don't clash.
7. **No background music**: per template README "Don'ts" — narration + SFX only. The composition build phase MUST NOT add a music track.
8. **Determinism**: no `Date.now()`, no `Math.random()`, no runtime fetch — pre-compute counter end values, stagger offsets, and any "random-looking" delays at script-write time.
9. **Asset capture order**: Phase 2 (script) → Phase 2a (TTS markup) → Phase 2b (fact-check) → TTS handoff → Phase 3.5 (retention refinement against transcript.json) → composition build (where /agent-browser captures the screenshots listed above and downloads any missing logos from `shared/logos/`).
10. **Logo gap risk**: this plan assumes `aws-logo-light.svg`, `nvidia-logo-light.svg`, `google-cloud-logo-light.svg`, `azure-logo-light.svg`, `pfizer-logo-light.svg`, and `lyft-logo-light.svg` exist under `shared/logos/`. The composition build phase MUST verify with `ls shared/logos | grep -i <brand>` before swapping; if any are missing, capture or stylize during that phase — do not stub a styled text div over a brand without confirming there's no real logo available.
11. **Rate-limit toast in Scene 01**: render it as styled HTML (red border, mono "rate_limit_exceeded" text, `<code>`-style background) rather than a screenshot. The status-page screenshot is OPTIONAL secondary content. This keeps the scene resilient even if /agent-browser fails to capture status.claude.com.

**Next step**: Run `/diy-yt-creator:phase2-script anthropic-amazon-compute`
