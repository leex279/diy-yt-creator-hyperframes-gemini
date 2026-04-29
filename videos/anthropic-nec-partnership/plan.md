# Composition Plan: anthropic-nec-partnership

## Director's Summary

A 90-second contrarian-news Short that opens with the validated stakes hook ("Anthropic just out-flanked OpenAI in Japan, because a 127-year-old company gave Claude Code to 30,000 engineers."), then unfolds the *full* deal — not just the seat count, but the BluStellar productization, the four regulated verticals (finance / manufacturing / local-gov / SOC), the Client Zero status, and the competitive frame against OpenAI–SoftBank's $3B/yr JV and Microsoft's $10B 5-partner play. Visuals lean on a 1899→2026 timeline morph, a Japan map pin-drop, an org-chart "30K of 105K windows light up" beat, a BluStellar plug-in snap, a 2×2 verticals grid, the Claude Code 17.7M→29M install curve, and a CTA that closes the open loop with "Who's next? Fujitsu, Hitachi, NTT Data?". Built on the `shorts/anthropic` template's mutex inline-phase model extended to 8 phases — narration + SFX, no music, dark stage with rotating orange/purple/blue/green accents.

## Template & Structure

- **Template**: `templates/shorts/anthropic` (1080x1920, 30fps)
- **Composition layout model**: `inline-phase` + `mutex-visibility` (template forces this; no sub-compositions)
- **Phase count**: 8 (Hook, Timeline, First-Japan, Rollout, Eng-Team, BluStellar+Verticals, Why-Now, CTA) — cap lifts above 60s, 8 is the natural count for 90s per the duration→structure quick reference
- **Naming convention**: P1, T1, P2, T2, P3, T3, P4, T4, P5, T5, P6, T6, P7, T7, P8 (per template README "Adding more phases")
- **Design token overrides**: none — using template's `--orange`, `--purple`, `--blue`, `--green` verbatim
- **Background music**: NONE (template forbids it on Shorts)

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements |
|-------|------------|---------------|-------------|--------------|
| 01 — Hook (Stakes Pivot) | 0  | 10 | Slam: "30,000" → strikethrough → BUT → stakes line "Anthropic just out-flanked OpenAI in Japan." | overline ANTHROPIC × NEC · 240px slam "30,000" · strikethrough · pivot beat "BUT." · stakes line + caption pill "because a 127-year-old company gave Claude Code to 30,000 engineers." |
| 02 — The Real Shocker (1899) | 10 | 11 | Timeline morph: 1899 → 2026. NEC's age IS the story. | overline FOUNDED 1899 · timeline rail + year ticks (1899/1950/2000/2026) · slam "127 YEARS" (purple) · subtitle "Edison-era. Now AI-native." |
| 03 — First Japan Partner | 21 | 9  | Japan map + Anthropic pin drop. Status badge. | overline FIRST · Japan silhouette · pin drop · badge "1st Japan-based global partner" (blue) |
| 04 — 30K of 105K Rollout | 30 | 11 | Stat pills: 30,000 (orange) of 105,000 (blue, dimmed). | overline THE ROLLOUT · stat pill "30,000" (orange) · stat pill "105,000" (blue, dimmed) · sublabel "≈29% of the entire NEC Group" |
| 05 — AI-Native Eng Team + Client Zero | 41 | 12 | Org-chart morph (hierarchy → mesh) + Client Zero badge. | overline THE ENGINEERING ORG · mesh org-chart graphic · caption "what they're calling Japan's largest AI-native engineering team" · badge "CLIENT ZERO" (green) |
| 06 — BluStellar + 4 Verticals | 53 | 13 | BluStellar product card + 2×2 verticals grid (finance / manufacturing / local-gov / SOC). | overline THE PRODUCT · BluStellar card · plug-in snap · 2×2 verticals grid (each cell pulses on its label) |
| 07 — Why NOW (Adoption + Competitor Stack) | 66 | 12 | 17.7M → 29M Claude Code install curve + competitor card stack (OpenAI–SoftBank $3B/yr · Microsoft $10B). | overline WHY NOW · line chart "17.7M → 29M Jan→Apr 2026" (Claude Code daily VS Code installs) · two competitor cards (purple OPENAI×SOFTBANK · blue MICROSOFT×5 SIs) sliding behind a foreground card "ANTHROPIC × NEC" (orange) |
| 08 — CTA / Open Loop Close | 78 | 12 | Card stack: Fujitsu / Hitachi / NTT Data. Subscribe pill. Quote line from Yoshizaki (paraphrased). | overline WHO'S NEXT? · 3 stacked cards (purple/blue/green) · subscribe pill · paraphrased Yoshizaki line "NEC's COO calls it 'maximizing AI's potential in the Japanese market.'" · marker-circle on "Fujitsu" |

**Total `data_duration`**: 90s (sum of all scene durations: 10+11+9+11+12+13+12+12 = 90)

## Narrative Arc

Kallaway Formula breakdown for 90s news-explainer:

1. **Context Lean-In + Scroll-Stop** (Scene 01, 0-10s, 11%): "Anthropic just out-flanked OpenAI in Japan — because a 127-year-old company gave Claude Code to 30,000 engineers." Stakes hook validates the click in line 1. Stun-gun "BUT." pivot is built into the visual beat, not the narration.
2. **Contrarian Snapback** (Scene 02, 10-21s, 12%): "Because here's the part nobody's saying out loud — NEC was founded in 1899. Edison-era infrastructure, going AI-native." Reframes the headline.
3. **Solution / Proof** (Scene 03, 21-30s, 10%): "And NEC just became Anthropic's first Japan-based global partner — ever." Anchors the status claim.
4. **Deep Dive Part 1 — Scale** (Scene 04, 30-41s, 12%): "So what does the rollout actually look like? 30,000 of NEC's 105,000 employees getting Claude — about 29% of the entire group." Concrete scale.
5. **Deep Dive Part 2 — Depth** (Scene 05, 41-53s, 14%): "And here's the part OpenAI should worry about — NEC isn't just licensing seats. They're building what they're calling Japan's largest AI-native engineering team, and they're shipping against unreleased Claude features as part of Anthropic's Client Zero program." Loop opener + depth.
6. **Deep Dive Part 3 — Productization** (Scene 06, 53-66s, 14%): "Plus Claude isn't staying internal — it's plugging into NEC's BluStellar Scenario consulting program, which means it ships to NEC's customers in finance, manufacturing, local government, and the security operations center." Productized = real.
7. **Trust / Why Now** (Scene 07, 66-78s, 13%): "Why now? Because Claude Code daily VS Code installs went from 17.7 million to 29 million in four months. And every US AI lab now has a Japan thesis — OpenAI bought distribution via SoftBank's $3 billion-a-year JV, Microsoft spread $10 billion across five Japanese SIs. Anthropic went one company deep." Receipts + competitive frame.
8. **CTA / Open-Loop Close** (Scene 08, 78-90s, 14%): "So who moves next? Fujitsu? Hitachi? NTT Data? NEC's COO calls it 'maximizing AI's potential in the Japanese market' — but the real question is which Japanese SI matches it. The race just got real." Closes the secondary loop with paraphrased Yoshizaki.

**Voice profile**: `news-explainer` — every scene transition uses an explanatory connector (`because`, `so`, `and`, `plus`, `here's why`). Narration is connected sentences, NOT pure fragments — to pass Phase 2.5 Pass 6.

**Explosion timer**: unique value (the stakes reframe — "out-flanked OpenAI") lands at 0-3s — well within the short-form 4s lean-in window.

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "30,000 seats isn't the shocking part — NEC was founded in 1899."
    layers_present: [1, 4, 5]
    advisory_score: 9.7
    # base = 9*0.4 + 7*0.4 + 9*0.2 = 8.2
    # +alignment 1 +narrative_flow 0.5 = 9.7
  variant_b:
    type: "stakes"
    opening_line: "Anthropic just out-flanked OpenAI in Japan, because a 127-year-old company gave Claude Code to 30,000 engineers."
    layers_present: [1, 2, 3, 5]
    advisory_score: 10.0
    # base = 8*0.4 + 9*0.4 + 9*0.2 = 8.6
    # +alignment 1 +narrative_flow 0.5 = 10.1 → capped at 10.0
  variant_c:
    type: "number"
    opening_line: "30,000 engineers. One AI. 127 years of corporate history, rewritten overnight."
    layers_present: [3, 5]
    advisory_score: 8.2
    # base = 7*0.4 + 6*0.4 + 10*0.2 = 7.2
    # +alignment 1, narrative_flow 0 (pure fragments) = 8.2
  recommended: "variant_b"
  rationale: |
    Highest score (10.0) — preserved from prior 45s plan per user constraint. Topic type
    "New tool / product release" → Stakes formula (per §4A). Names the stakes (out-flanks OpenAI),
    anchors with 127 + 30,000 specificity, includes the "because" narrative-flow connector required
    by news-explainer profile, and validates the click in line 1 by naming Anthropic + Claude Code
    directly. At 90s the hook keeps its full one-sentence form (no trim needed).
```

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "ContrastPivot"
  selected_variant: "variant_b"
  rationale: |
    Pattern selection per Step 5A: comparison/contrarian-take + Stakes hook → ContrastPivot.
    Build context with the "30,000 seats" framing, smash-cut on "BUT" to the contrarian reveal
    (OpenAI got out-flanked by a 127-year-old SI), then cascade evidence across the 7 follow-on
    scenes (timeline → map → rollout scale → eng team → product → competitor stack → CTA).
    ContrastPivot is also the cleanest fit for the Anthropic dark-stage motion language
    (slam → pivot word → reveal), reusing back.out(1.7) signature springs.

  visual_beats:
    - beat: "Cold Open"
      timing_s: [0, 1.5]
      visual: "Pure black canvas. Top banner shows ANTHROPIC × NEC wordmark. Mono overline THE ANTHROPIC × NEC DEAL slides up from y:+40."
      gsap_ease: "power3.out"
      sfx: null
    - beat: "Context (Setup)"
      timing_s: [1.5, 4.5]
      visual: "240px '30,000' (orange) slams in from scale 0.78 → 1.0 with inline ±6px shake. Sub-line '...seats. The headline number.' fades in below at 64px."
      gsap_ease: "back.out(1.7)"
      sfx: "impact-slam"
    - beat: "PIVOT (Smash Cut)"
      timing_s: [4.5, 5.0]
      visual: "Strikethrough sweeps across '30,000' (red marker line). White flash 1 frame. 240px 'BUT.' slams in (red, the only red use in the comp)."
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake + glitch-zap"
    - beat: "Stakes Reveal"
      timing_s: [5.0, 9.0]
      visual: "'BUT.' fades out. 64px headline rises: 'Anthropic just out-flanked OpenAI in Japan' (off-white). Caption pill below: 'because a 127-year-old company gave Claude Code to 30,000 engineers.' (mono, secondary text)."
      gsap_ease: "power3.out"
      sfx: "scale-slam"
    - beat: "Phase Crossfade Out → Scene 02"
      timing_s: [9.0, 10.0]
      visual: "Blur + opacity crossfade (0.4s opacity / 0.5s blur) into Scene 02 (Timeline)."
      gsap_ease: "sine.inOut"
      sfx: "cinematic-whoosh"

  pivot_word: "BUT."
  brand_reveal_word: "Anthropic" (in opening overline) + "Claude Code" (in caption pill at 7s)

  assets_needed:
    - type: "logo"
      description: "Anthropic + NEC combined wordmark for top banner (Anthropic wordmark + 'NEC' text)."
      source: "shared/logos/anthropic-logo-light.svg + plain text NEC — final wiring decided in composition build"
    - type: "logo"
      description: "Claude Code wordmark for narration emphasis"
      source: "shared/logos/claude-code-logo-light.svg"
    - type: "screenshot"
      description: "Anthropic announcement page hero (proof-source flash, ~0.6s overlay in Scene 03)"
      source: "https://www.anthropic.com/news/anthropic-nec — capture in composition build (dark mode)"
    - type: "screenshot"
      description: "NEC BluStellar product page (proof flash for Scene 06)"
      source: "https://www.nec.com (search BluStellar) — capture in composition build (light mode, briefly)"

sfx_cues:                          # consumable by phase3-5-retention.md
  - beat: "Context entrance (Scene 01)"
    cues: [impact-slam]
  - beat: "PIVOT (Scene 01)"
    cues: [impact-slam, screen-shake, glitch-zap]
  - beat: "Stakes Reveal (Scene 01)"
    cues: [scale-slam]
  - beat: "Phase change (P1→P2 … P7→P8)"
    cues: [cinematic-whoosh]
  - beat: "Strikethrough '30,000' (Scene 01 PIVOT lead-in)"
    cues: [strike-cross]
  - beat: "Timeline tick entrance (Scene 02 — 1899/1950/2000/2026)"
    cues: [spring-pop]
  - beat: "Pin drop landing (Scene 03)"
    cues: [scale-slam]
  - beat: "Stat pill entrance (Scene 04)"
    cues: [scale-slam]
  - beat: "Org-chart morph snap (Scene 05)"
    cues: [scale-slam]
  - beat: "Client Zero badge entrance (Scene 05)"
    cues: [spring-pop]
  - beat: "BluStellar plug-in snap (Scene 06)"
    cues: [scale-slam]
  - beat: "Vertical-grid cell pulse (Scene 06 — 4 cues, 200ms apart)"
    cues: [spring-pop]
  - beat: "Competitor card stack entrance (Scene 07)"
    cues: [spring-pop]
  - beat: "CTA card entrance (Scene 08 — Fujitsu/Hitachi/NTT Data)"
    cues: [spring-pop]

music_profile:
  hook_mood: NONE   # template forbids background music on Shorts
  # narration + SFX only, per templates/shorts/anthropic/README.md "Don'ts"
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 01 (Hook)"
    setup_line: "Anthropic just out-flanked OpenAI in Japan."
    resolution_scene: "Scene 07 (Why Now)"
    resolution_line: "OpenAI bought distribution via SoftBank's $3 billion-a-year JV. Microsoft spread $10 billion across five Japanese SIs. Anthropic went one company deep — and got the engineering org."
    type: "tension"

  secondary_loop:
    setup_scene: "Scene 02 (Timeline)"
    setup_line: "Edison-era infrastructure, going AI-native."
    resolution_scene: "Scene 08 (CTA)"
    resolution_line: "So who moves next? Fujitsu, Hitachi, NTT Data? The Japan AI race just got real."
    type: "question"
    note: "Frames the deal as a competitive trigger, not a one-off announcement."

  loop_openers:
    - scene: "Scene 02"
      position: "opening"
      phrase: "Because here's the part nobody's saying out loud."
    - scene: "Scene 05"
      position: "opening"
      phrase: "And here's the part OpenAI should worry about."
    - scene: "Scene 07"
      position: "opening"
      phrase: "Why now? Here's the receipt."
```

For a 90s Short with 8 scenes the loop opener cadence target is 2-3 (60-180s band, every 60-90s). This plan ships 3 — within budget and serving the primary tension loop + secondary question loop.

## Story Lock Placement

- **Scene 01 — Hook**: NO Negative Frame, NO Loop Opener (per the hook scope rule — hook validates the click, doesn't shame). Stun-gun "BUT" pivot only.
- **Scene 02 — Term Branding (Lock #1)**: coin "Edison-era → AI-native" as the term that names the contrast. Reuse implicitly in Scene 05 (eng team).
- **Scene 03 — Thought Narration (Lock #3)**: subtle thought-narration moment after the pin drops — "Anthropic didn't have a Japan-based global partner. Until now."
- **Scene 04 — Negative-space anchor**: no lock; pure scale receipt scene.
- **Scene 05 — Loop Opener (Lock #5) #1**: "And here's the part OpenAI should worry about." — sets up the primary tension loop's resolution in Scene 07.
- **Scene 06 — Term Branding reinforcement**: "BluStellar Scenario" repeated as the productization label.
- **Scene 07 — Loop Opener (Lock #5) #2**: "Why now? Here's the receipt." — invites viewer to absorb the comparative numbers.
- **Scene 08 — Loop Close + CTA**: closes the secondary question loop with the named SI competitors and the paraphrased Yoshizaki line.

No Negative Frames in this video — the news-explainer voice profile is observational, not prescriptive.

## Composition Layout

```yaml
composition_layout:
  model: "inline-phase + mutex-visibility"
  template: "templates/shorts/anthropic"
  resolution: [1080, 1920]
  fps: 30
  total_duration_s: 90
  phase_count: 8
  phase_naming: "P1, T1, P2, T2, P3, T3, P4, T4, P5, T5, P6, T6, P7, T7, P8"
  transition_pattern: "blur-crossfade between every phase (0.4s opacity + 0.5s blur)"
  top_banner:
    persistent: true
    content: "ANTHROPIC × NEC text wordmark (Inter 600, mono overline above with date 2026-04-23)"
    src: "Combined: shared/logos/anthropic-logo-light.svg + plain 'NEC' text — final wiring decided in composition build"
  bottom_progress_bar: false   # 90s short — still optional; skip to keep visual surface clean
```

## Retention Component Picks

```yaml
retention_component_picks:
  scene_01_hook:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam"
    primitives:
      - "gsap-stagger-grid"          # overline → slam → strikethrough → pivot → reveal sequence
      - "marker-highlight on 'BUT.'"  # marker #1 of 2 max
      - "marker-scribble (strikethrough on '30,000')"  # marker #2 of 2 max
    captions: null                    # too short and busy for synced caption layer
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_02_timeline_shocker:
    structural: "inline-phase"
    pattern: "timeline-cards"
    primitives:
      - "gsap-stagger-grid"          # year ticks fan out left-to-right (1899/1950/2000/2026)
      - "gsap-path-draw"             # the timeline rail line draws in
      - "gsap-counter-tween"         # year counter ticks 1899 → 2026
      - "marker-highlight on '127 YEARS'"   # marker #1 of 2 max
    captions: "caption-fade-slide"   # narration explains the timeline; calm cadence fits
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_first_japan_partner:
    structural: "inline-phase"
    pattern: "stat-pill-row (single-pill variant — badge + map)"
    primitives:
      - "gsap-stagger-grid"          # map + pin + badge enter staggered
      - "gsap-path-draw"             # Japan silhouette outline draws
      - "marker-circle on '1st'"     # marker #1 of 2 max — hand-drawn ellipse
    captions: null                    # 9s scene, badge IS the headline
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_04_rollout_scale:
    structural: "inline-phase"
    pattern: "stat-pill-row"
    primitives:
      - "gsap-counter-tween"         # 0 → 30,000 (orange) and 0 → 105,000 (blue, dimmed)
      - "gsap-stagger-grid"          # two pills enter with 200ms stagger
      - "marker-highlight on '≈29%'" # marker #1 of 2 max
    captions: "caption-fade-slide"   # narration carries the "of NEC's 105,000" line
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_05_eng_team_client_zero:
    structural: "inline-phase"
    pattern: "stat-pill-row (badge variant)"
    primitives:
      - "gsap-stagger-grid"          # mesh nodes appear, then Client Zero badge
      - "gsap-path-draw"             # mesh edges draw between nodes
      - "marker-highlight on 'AI-native engineering team'"  # marker #1 of 2 max
      - "marker-circle on 'CLIENT ZERO'"                     # marker #2 of 2 max
    captions: "caption-fade-slide"   # narration carries Yoshizaki-attribution-free framing
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_06_blustellar_verticals:
    structural: "inline-phase"
    pattern: "timeline-cards (2x2 grid variant)"
    primitives:
      - "gsap-stagger-grid"          # 4 vertical cells stagger in 200ms apart
      - "gsap-flip-reveal"           # BluStellar product card snaps from offscreen-right
      - "marker-highlight on 'BluStellar Scenario'"   # marker #1 of 2 max
    captions: "caption-fade-slide"   # 4 vertical names spoken — caption tracks each
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_07_why_now_competitor_stack:
    structural: "inline-phase"
    pattern: "timeline-cards (chart + stack variant)"
    primitives:
      - "gsap-path-draw"             # Claude Code adoption curve 17.7M → 29M
      - "gsap-counter-tween"         # 17.7M → 29M number tick
      - "gsap-stagger-grid"          # 3 competitor cards (OpenAI×SoftBank, Microsoft×5, Anthropic×NEC)
      - "marker-highlight on '$3B/yr' and '$10B'"   # 2 markers of 2 max — receipts
    captions: "caption-fade-slide"   # heaviest narration scene; caption tracks competitor names
    audio_reactive: "audio-reactive-glow on the 29M counter (subtle, treble band, 4% scale)"
    transition_out: "blur-crossfade"

  scene_08_cta_who_next:
    structural: "inline-phase"
    pattern: "cta-url-slam (variant — card-stack instead of URL)"
    primitives:
      - "gsap-stagger-grid"          # 3 SI cards enter with 200ms stagger
      - "marker-circle on 'Fujitsu'" # marker #1 of 2 max — implies first-to-react probability
    captions: "caption-fade-slide"   # paraphrased Yoshizaki line carries narration; caption emphasizes "maximize" + "Japanese market"
    audio_reactive: "audio-reactive-glow on the subscribe pill (subtle, treble band, 3-6% scale)"
    transition_out: null              # final scene — no exit
```

**Constraints applied**:
- Markers: max 2/scene → all scenes within budget (Scenes 01, 05, 07 hit 2; others ≤1).
- Captions: only one `caption-*` group visible at a time → enforced by phase mutex.
- Transitions: ONE primary (`blur-crossfade`) used for 100% of phase changes — no accents needed.
- No banned anti-patterns: no spectrum visualizers, no exit animations on non-final scenes, no Remotion bits.

**Pick count summary**:
- Markers: 11 across the comp (Scene 01: 2; Scene 02: 1; Scene 03: 1; Scene 04: 1; Scene 05: 2; Scene 06: 1; Scene 07: 2; Scene 08: 1)
- Captions: 6 scenes with `caption-fade-slide` (Scenes 02, 04, 05, 06, 07, 08)
- Audio-reactive: 2 (`audio-reactive-glow` on Scene 07's 29M counter; `audio-reactive-glow` on Scene 08's subscribe pill)
- Transitions: 7 (`blur-crossfade` between P1→P2, P2→P3, P3→P4, P4→P5, P5→P6, P6→P7, P7→P8)

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene_01_hook"
    data_start: 0
    data_duration: 10
    audio_anchor: "narration starts at 0.4s; pivot word 'BUT' lands at 4.5s; reveal line ends near 9.0s; phase crossfade 9.0-10.0s"
    on_screen_words: ~14 (overline + slam + strikethrough sub + reveal line + caption pill)
    min_display_per_table: 6.0s (11-20 words → 4-6s); narration drives 10s
  - scene: "scene_02_timeline_shocker"
    data_start: 10
    data_duration: 11
    audio_anchor: "year '1899' spoken at 11.5s; '2026' tick lands at 15s; '127 YEARS' slam at 17s; 'Edison-era' subtitle at 19s"
    on_screen_words: ~10 (overline + 4 year labels + slam + subtitle)
    min_display_per_table: 4.0s (4-10 words); narration drives 11s
  - scene: "scene_03_first_japan_partner"
    data_start: 21
    data_duration: 9
    audio_anchor: "'first Japan-based global partner' spoken at 23s; pin drops on the 's' of 'first'; thought-narration line ends at 28s"
    on_screen_words: ~7 (overline + badge text)
    min_display_per_table: 4.0s; narration drives 9s
  - scene: "scene_04_rollout_scale"
    data_start: 30
    data_duration: 11
    audio_anchor: "'30,000 of 105,000' spoken at 31.5s — counters land on the digit; '≈29% of the entire NEC Group' caption synced to 36s"
    on_screen_words: ~14 (overline + 2 stat pill labels + sublabel)
    min_display_per_table: 6.0s (11-20 words); narration drives 11s
  - scene: "scene_05_eng_team_client_zero"
    data_start: 41
    data_duration: 12
    audio_anchor: "'And here's the part OpenAI should worry about' loop-opener at 41.5s; mesh org-chart settles at 45s; 'Client Zero program' at 49s; badge entrance at 50s"
    on_screen_words: ~13 (overline + caption + badge text)
    min_display_per_table: 6.0s (11-20 words); narration drives 12s
  - scene: "scene_06_blustellar_verticals"
    data_start: 53
    data_duration: 13
    audio_anchor: "'BluStellar' spoken at 54s — plug-in snap fires; 4 vertical names spoken 56-60s — grid cells pulse 200ms apart; 'security operations center' at 60.5s"
    on_screen_words: ~16 (overline + product card + 4 vertical names + caption)
    min_display_per_table: 6.0s (11-20 words); narration drives 13s
  - scene: "scene_07_why_now_competitor_stack"
    data_start: 66
    data_duration: 12
    audio_anchor: "'17.7 million to 29 million' spoken at 67s — counter tweens; 'OpenAI/SoftBank $3 billion-a-year' at 70s; 'Microsoft $10 billion' at 73s; 'Anthropic went one company deep' at 76s"
    on_screen_words: ~18 (overline + chart label + 3 competitor cards)
    min_display_per_table: 6.0s (11-20 words); narration drives 12s
  - scene: "scene_08_cta_who_next"
    data_start: 78
    data_duration: 12
    audio_anchor: "'Fujitsu, Hitachi, NTT Data' spoken at 79-81s with 200ms stagger on each card; paraphrased Yoshizaki line at 84s; subscribe call at 88s"
    on_screen_words: ~17 (overline + 3 card titles + paraphrased quote + subscribe pill)
    min_display_per_table: 6.0s (11-20 words); narration + final lock drives 12s
total_data_duration: 90
```

`audio_anchor` values are PLACEHOLDERS — Phase 3.5 refines against `transcript.json` after TTS + transcribe.

**Scene-count check**: 8 scenes for 90s → meets the 7-8 band recommendation for 90s. Avg scene length 11.25s — all scenes ≥9s so news-explainer connectors fit.

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []   # no overrides — Anthropic-branded video, default palette is correct

  fonts:
    sans: "Inter"             # template default
    mono: "JetBrains Mono"    # template default

  per_scene_accent:
    scene_01_hook: "orange (--orange)"           # primary slam + reveal text
    scene_02_timeline: "purple (--purple)"        # 127 YEARS slam, year ticks
    scene_03_first_japan: "blue (--blue)"         # pin + badge
    scene_04_rollout: "orange (--orange)"         # 30K stat pill (105K stat in dimmed --blue)
    scene_05_eng_team: "green (--green)"          # Client Zero badge + mesh node accent
    scene_06_blustellar: "purple (--purple)"      # BluStellar card + verticals grid label
    scene_07_why_now: "blue (--blue)"             # adoption curve + competitor cards (Anthropic×NEC card stays orange foreground)
    scene_08_cta: "green (--green)"               # who's next card stack — green signals positive forward look

  red_usage:
    where: "Scene 01 only — strikethrough on '30,000' + 'BUT.' word"
    rationale: "DESIGN.md restricts red to warnings/regression/pivots. The strikethrough + 'BUT' pivot is the only legitimate red use in this comp."

  accent_rotation_check:
    rule: "no two adjacent phases share the same accent"
    sequence: "orange → purple → blue → orange → green → purple → blue → green"
    note: "No two adjacent phases share an accent. Scene 01/04 both orange but separated by purple+blue. Scene 02/06 both purple but separated by blue+orange+green. Scene 03/07 both blue but separated by orange+green+purple. Scene 05/08 both green but separated by purple+blue. Passes."
```

## AI Image Prompts

None. All visuals composed in HyperFrames (timeline, map silhouette, org-chart pills, BluStellar card mockup, verticals grid, line chart, card stacks). The dark-stage aesthetic + screenshots from the proof sources covers the visual surface.

## Screenshot Inventory

```yaml
screenshots:
  - name: "anthropic-news-anthropic-nec"
    url: "https://www.anthropic.com/news/anthropic-nec"
    scene: "scene_03"
    color_scheme: "dark"
    usage: "Brief proof-source flash behind the badge (~0.6s overlay) — capture in composition build"
  - name: "nec-blustellar-product"
    url: "https://www.nec.com (search BluStellar)"
    scene: "scene_06"
    color_scheme: "light"
    usage: "Brief evidence flash (~0.6s) of the BluStellar product page when narration says 'BluStellar Scenario consulting program' — capture in composition build"
  - name: "claude-code-vscode-trend"
    url: "https://www.uncoveralpha.com/p/anthropics-claude-code-is-having"
    scene: "scene_07"
    color_scheme: "dark"
    usage: "Source attribution flash for the 17.7M → 29M install curve (~0.5s overlay) — capture in composition build"
```

NEC press release screenshot omitted from inventory — it returned 403 in Phase 0 research and is not load-bearing for the narrative; the Anthropic announcement covers the same facts.

## HyperFrames Blocks

None. This composition uses only the template's stock primitives + `shared/lib/` blocks already present in the Anthropic Shorts template (stat-pill-row, timeline-cards, hero-slam, cta-url-slam, phase-crossfade effect). The 2×2 verticals grid (Scene 06) and competitor card stack (Scene 07) are inline custom layouts — no registry installs needed.

## Fact-Check Audit

Every claim that will be referenced in narration, with source URL or remediation. The 90s budget pulls in 5 of the 7 previously-deprioritized facts.

| # | Claim | Source URL | Status |
|---|-------|------------|--------|
| 1 | Claude rolling out to ~30,000 NEC employees | https://www.anthropic.com/news/anthropic-nec | SOURCED — in Scenes 01, 04 |
| 2 | NEC Group total headcount ~105,000 | https://en.wikipedia.org/wiki/NEC | SOURCED — in Scene 04 |
| 3 | NEC founded 1899 (127 years old) | https://en.wikipedia.org/wiki/NEC | SOURCED — in Scenes 01, 02 |
| 4 | First Japan-based global Anthropic partner | https://www.anthropic.com/news/anthropic-nec; https://www.thefastmode.com/technology-solutions/48258-nec-becomes-anthropic-s-first-japan-based-global-partner-for-claude-rollout | SOURCED (dual-confirmed) — in Scene 03 |
| 5 | Claude integrated into NEC BluStellar Scenario | https://www.anthropic.com/news/anthropic-nec | **NOW SOURCED & ACTIVE — Scene 06 (was deprioritized at 45s)** |
| 6 | Joint solutions for finance / manufacturing / local-gov / SOC | https://www.anthropic.com/news/anthropic-nec | **NOW SOURCED & ACTIVE — Scene 06 verticals grid (was deprioritized at 45s)** |
| 7 | NEC joins Anthropic Client Zero program | https://www.anthropic.com/news/anthropic-nec | **NOW SOURCED & ACTIVE — Scene 05 (was deprioritized at 45s)** |
| 8 | "Japan's largest AI-native engineering team" | https://www.anthropic.com/news/anthropic-nec (NEC/Anthropic framing) | SOURCED — REPHRASED with attribution: "what they're calling Japan's largest AI-native engineering team." Phase 0 flagged this as needing Phase 2b verification — keep the "what they're calling" hedge. |
| 9 | OpenAI–SoftBank Japan JV ($3B/yr) | https://www.investing.com/news/company-news/nec-partners-with-anthropic-to-deploy-ai-solutions-in-japan-93CH-4631869 | **NOW SOURCED & ACTIVE — Scene 07 ($3B figure spoken; was deprioritized at 45s)** |
| 10 | Microsoft $10B 5-partner Japan deal | https://news.microsoft.com/source/asia/2026/04/03/microsoft-deepens-its-commitment-to-japan-with-10-billion-investment-in-ai-infrastructure-cybersecurity-workforce/ | **NOW SOURCED & ACTIVE — Scene 07 ($10B figure spoken; was deprioritized at 45s)** |
| 11 | Claude Code VS Code daily installs 17.7M → 29M (Jan→Apr 2026) | https://www.uncoveralpha.com/p/anthropics-claude-code-is-having | **NOW SOURCED & ACTIVE — Scene 07 adoption curve (was deprioritized at 45s)** |
| 12 | "Edison-era infrastructure, going AI-native" | derived rhetorical flourish from claim #3 | DERIVED — not a factual claim; safe metaphor. |
| 13 | "30,000 of 105,000 employees ≈ 29%" math | claims #1 + #2 | DERIVED — arithmetic from sourced facts. |
| 14 | Toshifumi Yoshizaki (COO NEC) — paraphrased | https://www.anthropic.com/news/anthropic-nec | **NOW ACTIVE BUT PARAPHRASED — Scene 08.** No direct-speech quote. Narration says: "NEC's COO calls it 'maximizing AI's potential in the Japanese market'" — phrase appears in the Anthropic announcement; framed as an attributed paraphrase, not a direct verbatim line. Phase 2b must re-verify the exact phrasing against the source before TTS. If the announcement does not contain that exact phrase, REPHRASE to "NEC's COO has framed it as a bid to maximize AI's potential in the Japanese market" (no quotes). |
| 15 | "Fujitsu, Hitachi, NTT Data" as next-to-react SIs | competitive context per https://news.microsoft.com/source/asia/2026/04/03/microsoft-deepens-its-commitment-to-japan-with-10-billion-investment-in-ai-infrastructure-cybersecurity-workforce/ (lists these as Microsoft's other Japan partners) | SOURCED — framed as a question ("Who's next?"), not as a prediction. |

**Summary**:
- **Sourced**: 13 claims with cited URLs (12 in active narration, 0 deprioritized, 1 paraphrased-quote pending Phase 2b verification of exact phrasing)
- **Derived**: 2 claims (Edison-era metaphor, 29% arithmetic) — both rest on already-sourced base facts
- **Removed**: 0 — all previously-deprioritized facts that fit the 90s budget are now in narration
- **Rephrased with hedge**: 1 ("Japan's largest AI-native engineering team" → "what they're calling…")
- **Direct quotes**: 0 verbatim. 1 attributed paraphrase (Yoshizaki) requires Phase 2b cross-check; will downgrade to non-quoted attribution if exact phrase not in source.

**Previously-deprioritized facts now active in 90s narration** (5 of the 7 the user flagged):
1. **BluStellar Scenario** — Scene 06 (productized Claude reaches NEC's customers)
2. **The 4 verticals (finance / manufacturing / local-gov / SOC)** — Scene 06 (2×2 grid)
3. **Client Zero program** — Scene 05 (badge + narration mention)
4. **$3B OpenAI/SoftBank JV figure** — Scene 07 (competitor card)
5. **$10B Microsoft Japan figure** — Scene 07 (competitor card)
6. **Claude Code 17.7M → 29M install curve** — Scene 07 (adoption line chart)
7. **Toshifumi Yoshizaki COO quote** — Scene 08 (paraphrased, attributed; pending Phase 2b exact-phrasing verification)

That's 6 of 7 deprioritized facts now in active narration, plus the Yoshizaki paraphrase, exceeding the user's "at least 4-5" target. Only the per-vertical SOC deep dive (beyond naming the cell on the grid) remains compressed — covered as a label in Scene 06 rather than a dedicated beat.

Phase 2b will re-verify all 13 sourced claims plus the 2 derived claims after script generation. Outstanding items flagged from Phase 0:
- NEC press release at `https://www.nec.com/en/press/202604/global_20260423_01.html` — 403'd in Phase 0; Anthropic's announcement covers the same facts so not blocking, but Phase 2b should attempt re-fetch (mobile UA / cached snapshot) to confirm Yoshizaki phrasing.
- Microsoft $10B Japan timeline — Phase 0 noted "planned 2026–2029" surfaced via competitive-search summary; Phase 2b should re-verify directly against the Microsoft source release.

## Notes for Composition Build

- **Top banner**: combine Anthropic wordmark (from `shared/logos/anthropic-logo-light.svg`) with text "× NEC" in Inter 600. Total banner width ~560px per DESIGN.md safe zone.
- **Scene 01 strikethrough**: the strikethrough on "30,000" must fire at ~4.0s, BEFORE the white-flash + "BUT" slam at 4.5s — so the viewer sees the canonical headline being rejected, not just replaced.
- **Scene 02 timeline rail**: SVG path with `gsap-path-draw` over 1.5s. Year ticks at 1899, 1950, 2000, 2026 with `spring-pop` SFX on each tick (4 cues, staggered ~0.4s apart starting at 11.5s).
- **Scene 03 Japan silhouette**: simplified outline SVG of Japan; place in `assets/` during build. Pin drop animates `y: -200 → 0` with `back.out(1.7)`, `scale-slam` SFX on landing (subtle, single hit). Optional `audio-reactive-pulse` once on landing — keep it 6% scale variation max.
- **Scene 04 stat pills**: 30,000 (orange, full opacity, primary) on the LEFT; 105,000 (blue, 0.55 opacity, secondary) on the RIGHT. Size relationship visually communicates "the 30K is the live part of the 105K." `gsap-counter-tween` runs 0 → target over 1.0s with `power3.out`. The "≈29%" sublabel appears centered between the two pills with `marker-highlight` sweep.
- **Scene 05 mesh org-chart**: start with a hierarchical tree (3 layers, ~12 nodes), then `gsap-flip-reveal` into a mesh (every node connected to ≥3 others). Use `gsap-path-draw` for the connecting edges — draw with 50ms stagger. Client Zero badge enters from below in green with `spring-pop` SFX.
- **Scene 06 BluStellar + 2×2 grid**: BluStellar product card on the LEFT (purple accent, mock dashboard look). 2×2 grid on the RIGHT with cells: FINANCE / MANUFACTURING / LOCAL GOVERNMENT / SOC. Each cell gets a `spring-pop` cue 200ms apart synced to the narrator naming the vertical. SOC is the only abbreviation — render in JetBrains Mono with the spelled-out tooltip "Security Operations Center" appearing as a 24px sub-line briefly.
- **Scene 07 adoption curve + competitor stack**: chart fills the upper half (line goes from 17.7M baseline to 29M, with a vertical marker at "Apr 24" labeled "NEC ANNOUNCEMENT"). Lower half has 3 stacked competitor cards in dimmed purple/blue with the foreground "ANTHROPIC × NEC" card in orange — the orange card slides FORWARD from the back of the stack to communicate the out-flank metaphor. Numbers ($3B, $10B) marked with `marker-highlight` on entrance.
- **Scene 08 card stack**: 3 cards labeled FUJITSU / HITACHI / NTT DATA in JetBrains Mono uppercase. `marker-circle` (hand-drawn) overlays on FUJITSU only — implies first-to-react probability. Subscribe pill bottom-right. Yoshizaki paraphrase appears as a 64px italicized line above the card stack with attribution "— TOSHIFUMI YOSHIZAKI, COO" in 24px mono. **CRITICAL**: if Phase 2b cannot confirm the exact phrasing in the Anthropic source, remove the quotation marks and rewrite as non-quoted attribution.
- **No accent doubling**: per DESIGN.md, max one accent per phase. Scene 04 rolls 105,000 in dimmed `--blue` — secondary tonal use (low opacity, no glow), not a true accent. Scene 03 pin uses neutral white-stroke (NOT blue) so the badge's blue stays the only accent. Scene 07 has multiple competitor cards in different muted tones — treat as a "card-stack rotation" exception per DESIGN.md timeline-cards pattern (each card gets its own accent), which is allowed.
- **Phase mutex**: every phase except the active one must have `opacity: 0` and `visibility: hidden`. Phase fades use the template's `phase-crossfade.js` effect (provenance: `shared/lib/effects/phase-crossfade.js`).
- **Determinism**: no `Date.now()`, no `Math.random()` — all stagger offsets must be numeric literals.
- **Lint after every change**: `npx hyperframes lint videos/anthropic-nec-partnership` — fix all errors; check warnings.
- **Render filename**: per repo memory, `npx hyperframes render videos/anthropic-nec-partnership -o videos/anthropic-nec-partnership/out/anthropic-nec-partnership.mp4` — use the slug, not `short.mp4`.

---

**Next phase**: Run `/diy-yt-creator:phase2-script anthropic-nec-partnership` to draft narration.
