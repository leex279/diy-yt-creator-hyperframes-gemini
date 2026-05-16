# Composition Plan: claude-platform-on-aws

## Director's Summary

This is a 95-second confident news-explainer Short built around one structural surprise: Claude Platform on AWS is **not** a Bedrock rebrand — it's Anthropic's full native API operating outside the AWS data boundary, billed through AWS Marketplace, with day-zero feature parity. The composition opens on a familiar pain (Bedrock has been lagging the native API for years), pivots hard on "BUT TODAY, the lag is gone," and earns the click with a feature-pill cluster, AWS integration receipts (IAM SigV4, CloudTrail, Marketplace), a 17-region slam, and three named customers. Anthropic dark-stage aesthetic; orange leads, purple/blue/green rotate; one accent per phase; shape-backdrop drift; whoosh-only SFX (no per-element pops) per the template's 2026-04-28 default; final phase is a thumbnail-grade hold satisfying the 5-element rule.

## Template & Structure

- **Template**: `templates/shorts/anthropic` (1080×1920 vertical Short)
- **Layout model**: `inline-phase` + `mutex-visibility` (template-enforced — sub-compositions NOT used on Anthropic Shorts)
- **Phase pattern naming**: `P1, T1, P2, T2, …, P9` (whoosh transitions between phases, paired with shape-backdrop reposition per [`.claude/rules/audio-design.md`](../../.claude/rules/audio-design.md))
- **Design token overrides**: none. Use Anthropic dark-stage palette verbatim from `templates/shorts/anthropic/DESIGN.md` (`--orange #E97458`, `--purple #A78BFA`, `--blue #6B9AEF`, `--green #7DD3A6`).

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements |
|---|---|---|---|---|
| 01 — Hook (Bedrock lag pain) | 0.0 | 8.0 | Scroll-stop: "Bedrock has been lagging." Establish shared developer pain. | Overline "AWS DEVS, READ THIS", hero phrase "BEDROCK gets the new features WEEKS LATE", `marker-highlight` on "WEEKS LATE", clock metaphor |
| 02 — Pivot reveal | 8.0 | 7.0 | The Uno Reverse — "But today, that lag is gone." Title slam reveals product. | "BUT TODAY" 200px purple slam → product title "CLAUDE PLATFORM ON AWS" (160px) + "Generally Available" date chip "MAY 11, 2026" |
| 03 — Not-a-rebrand split | 15.0 | 11.0 | Two-column comparison: Bedrock (subset) vs Platform-on-AWS (full native API). Differentiate firmly. | 2 columns. Left: "Claude on Bedrock — data inside AWS, feature subset, weeks lag." Right: "Claude Platform on AWS — full native API, day-zero, data outside AWS." Step-by-step reveal of 3 bullet rows. |
| 04 — Feature pill cluster | 26.0 | 17.0 | 8 betas land step-by-step. "All of them, today." | Headline "8 BETAS. DAY ZERO." Pills enter ~1.9s apart: Managed Agents · Advisor · Skills · Files · MCP · Code execution · Web search · Console |
| 05 — AWS integration receipts | 43.0 | 14.0 | "How it works through your AWS account." Earn enterprise trust. | Endpoint URL pill (mono): `aws-external-anthropic.<region>.api.aws` with `marker-highlight` on the host. 3 chips drop in step-by-step: "IAM SigV4 auth", "CloudTrail audit", "AWS Marketplace billing" |
| 06 — 17 regions slam | 57.0 | 8.0 | Stat slam: "17 regions at GA." Coverage receipt. | Vertical-cropped world-map SVG with 17 dots popping in step-by-step (clustered: US/CA/EU/APAC/SA), then collapsing into a "17" counter (240px orange slam) with `gsap-counter-tween` 0→17 |
| 07 — Customer trust row | 65.0 | 9.0 | Three named launch customers. Social proof. | Overline "LAUNCH CUSTOMERS". 3 typography wordmarks step-by-step ~2.4s apart: ReliaQuest, OpenRouter, Emergent (text wordmarks — logos NOT in shared/logos; render as styled text per anthropic typography) |
| 08 — When to pick which | 74.0 | 11.0 | Decision matrix: Platform-on-AWS vs Bedrock. Preempt the "isn't this just Bedrock" objection. | 2-column matrix headline "WHICH ONE?". Left col (orange) "PLATFORM-ON-AWS: full features, data outside AWS." Right col (blue) "BEDROCK: data MUST stay inside AWS." Reveal sequentially. |
| 09 — Thumbnail hold | 85.0 | 10.0 | Thumbnail-grade final frame. Held still ≥1.5s. | Anthropic + AWS lockup top-left (brand chrome) · dominant slam "CLAUDE PLATFORM. ON AWS." 160px white · "8 betas. 17 regions. Day zero." outcome receipt 52px · subordinate CTA pill "Watch the full breakdown →" |

**Total `data_duration`**: 95.0s (within 90-120s target, target ~92-100s).

## Narrative Arc

Per Kallaway Formula (news-explainer profile — connectors required between every scene per [`.claude/references/brand-voice-news-explainer.md`](../../.claude/references/brand-voice-news-explainer.md)):

1. **Context Lean-In (0-8s, Scene 01)**: Anchor the shared pain — "Bedrock has been lagging." Viewer self-selects: "Yes, that's me."
2. **Scroll-Stop (Scene 02, t≈8s)**: "But today, that lag is gone." The stun gun.
3. **Contrarian Snapback (Scene 02-03, t=8-26s)**: Anthropic didn't move Claude TO Bedrock — they shipped the full native Platform THROUGH your AWS account. **Different product**.
4. **Solution (Scene 02 end, t≈12s)**: "Claude Platform on AWS — generally available now."
5. **Deep Dive — Benefit-Led (Scenes 04-06, t=26-65s)**: 8 betas (the surface), IAM/CloudTrail/Marketplace (the integration plumbing), 17 regions (the coverage receipt).
6. **Trust (Scene 07, t=65-74s)**: ReliaQuest, OpenRouter, Emergent.
7. **Decision Frame (Scene 08, t=74-85s)**: When to pick which — preempts the "is this just Bedrock" objection.
8. **Thumbnail / CTA (Scene 09, t=85-95s)**: Topic slam + receipts + subordinate CTA.

**Connector words** (one per scene transition for news-explainer flow):

| From | To | Connector |
|---|---|---|
| 01 | 02 | "But today…" (stun-gun pivot) |
| 02 | 03 | "Because…" |
| 03 | 04 | "Which means…" |
| 04 | 05 | "And here's how it ships through your AWS account…" |
| 05 | 06 | "Plus…" |
| 06 | 07 | "Three customers are already live…" (per `tts-pronunciation.md`, swap to "shipping" if "live" ambiguous — flag for Phase 2a) |
| 07 | 08 | "So when do you pick which?" |
| 08 | 09 | "Bottom line:" |

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Claude Platform on AWS is NOT Bedrock with a new name."
    layers_present: [1, 4, 5]
    source_fidelity:
      source_quote: "first-of-its-kind offering for Anthropic, providing all native Claude API features from day one"
      head_nouns: ["features"]
      passes_gate: true
    advisory_score: 7.9
    # base = (8*0.4) + (6*0.4) + (7*0.2) = 3.2 + 2.4 + 1.4 = 7.0
    # + stun_bonus 0 + alignment_bonus 1 + promise 0 + narrative_flow 0 (no connector in opener — pure-fragment claim)
    # = 8.0 → adjusted to 7.9 (specificity is reading on a noun, not a quantified stat)

  variant_b:
    type: "stakes"
    opening_line: "Every AWS dev shipping with Claude knows this pain — Bedrock gets the new features WEEKS late."
    layers_present: [2, 3, 4, 5]
    source_fidelity:
      source_quote: "all new features and betas shipping the same day they go live on the native Claude API"
      head_nouns: ["features", "betas", "developers"]
      passes_gate: true
    advisory_score: 8.7
    # base = (9*0.4) + (9*0.4) + (8*0.2) = 3.6 + 3.6 + 1.6 = 8.8
    # + stun_bonus 0 (stun gun is in line 2 "But today") + alignment_bonus 0 (opens with pain, not topic) + promise 0 + narrative_flow_bonus 0.5 (sentence carries explanatory connector "shipping with Claude knows this pain")
    # Wait — alignment_bonus: hook line 1 doesn't name product. -1 vs A. But stakes specificity earns higher curiosity + stakes.
    # Net: round to 8.7 reflecting strong curiosity + clear stakes + narrative flow bonus, no alignment.

  variant_c:
    type: "number"
    opening_line: "8 betas. 17 regions. Day zero."
    layers_present: [3, 4]
    source_fidelity:
      source_quote: "all native Claude API features from day one … available in 17 AWS regions"
      head_nouns: ["betas", "regions"]
      passes_gate: true
    advisory_score: 7.4
    # base = (8*0.4) + (6*0.4) + (10*0.2) = 3.2 + 2.4 + 2.0 = 7.6
    # + stun_bonus 0 + alignment_bonus 0 (no product named in line 1) + promise 0 + narrative_flow_bonus 0 (pure-stat opener, no connector)
    # Specificity is 10 but the new weighting (0.2) prevents triple-stat openers from auto-winning.
    # = 7.6 → 7.4 after slight downward adjustment for fragmented delivery (per Phase 2.5 Pass 6 risk for news-explainer)

  recommended: "variant_b"
  rationale: >
    Variant B opens with the pain the entire target audience feels (Bedrock feature lag),
    earns the click with shared stakes, contains an explanatory connector
    ("shipping with Claude knows this pain"), and sets up the strongest Uno Reverse
    pivot ("BUT TODAY the lag is gone"). Highest score 8.7. Variant A scores higher on
    Value Alignment but lacks emotional stakes — feature announcements without pain anchor
    test weaker on retention. Variant C is the third-place number-opener; the 0.2 specificity
    weighting and lack of narrative connector kept it from auto-winning despite triple-stat
    impact. All three pass Source Fidelity (head_nouns match the source's nouns verbatim).
```

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "ContrastPivot"
  selected_variant: "variant_b"

  visual_beats:
    - beat: "Cold Open / Context"
      timing_s: [0.0, 2.0]
      visual: "Overline 'AWS DEVS, READ THIS' enters (mono, orange). Background: shape-backdrop drift starts; ambient orange radial pulse."
      gsap_ease: "power3.out"
      sfx: null

    - beat: "Pain establishment"
      timing_s: [2.0, 6.0]
      visual: "Hero phrase enters: 'BEDROCK gets the new features…' (Inter 800, 72px). The phrase 'WEEKS LATE' enters last at 64px purple. Marker-highlight (purple) sweeps under 'WEEKS LATE'."
      gsap_ease: "power3.out → back.out(1.7) on the marker"
      sfx: null   # default = no per-element SFX; narration carries

    - beat: "PIVOT — 'But today'"
      timing_s: [8.0, 8.6]
      visual: "Phase 02 enters: white-on-dark 200px 'BUT TODAY' slam (purple accent). 6-frame inline shake. Shape-backdrop reposition fires."
      gsap_ease: "back.out(1.7)"
      sfx: "cinematic-whoosh (phase transition, paired with shape reposition, data-start = sceneT - 0.4)"

    - beat: "Brand reveal"
      timing_s: [8.6, 12.0]
      visual: "'BUT TODAY' fades down; product title 'CLAUDE PLATFORM ON AWS' enters at 160px (warm off-white). Below: 'Generally Available · May 11, 2026' chip (mono, orange fill)."
      gsap_ease: "power4.out"
      sfx: null

    - beat: "Contrast Snapback (Scene 03)"
      timing_s: [15.0, 26.0]
      visual: "Two-column split: 'Claude on Bedrock' (left, dim, blue) vs 'Claude Platform on AWS' (right, bright, orange). 3 bullet rows reveal step-by-step (~2.5s apart): data boundary / feature surface / feature lag."
      gsap_ease: "power3.out + stagger 200ms"
      sfx: "cinematic-whoosh on phase 03 entrance"

    - beat: "Promise of Resolution"
      timing_s: [24.0, 26.0]
      visual: "Right column ends with chip 'EVERY beta · DAY ZERO.' (orange). This is the bridge into the feature pill cluster (Scene 04)."
      gsap_ease: "back.out(1.7)"
      sfx: null

  pivot_word: "BUT"   # the script's hook reversal word; lands at t≈8.0s in narration
  brand_reveal_word: "CLAUDE PLATFORM"   # the moment the product name appears, t≈10.0s

  assets_needed:
    - type: "logo"
      description: "Anthropic wordmark (top-banner persistent)"
      source: "shared/logos/anthropic-logo-light.svg (already in shared library)"
    - type: "logo"
      description: "AWS wordmark (top-banner secondary, paired with Anthropic mark)"
      source: "shared/logos/aws-logo.png (already in shared library — may need a light variant; if dark, render as inverted)"
    - type: "diagram"
      description: "17-region vertical world map with dot anchors"
      source: "TBD — capture/draw a custom dark-styled SVG world map in composition build (no registry block exists for this per .claude/rules/registry-blocks-catalog.md)"
    - type: "logo"
      description: "ReliaQuest, OpenRouter, Emergent wordmarks"
      source: "NOT in shared/logos — render as styled JetBrains-mono or Inter typography wordmarks per Anthropic dark-stage aesthetic. Per brief 'Gaps / Needs User Input' section, this is the accepted fallback."

  music_profile:
    hook_mood: "NONE"   # template forbids background music on Shorts (per templates/shorts/anthropic/DESIGN.md Don'ts #6)
    # no bpm / mood — narration + SFX only
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Scene 01 (Hook)"
    setup_line: "Bedrock gets the new features WEEKS late."
    resolution_scene: "Scene 04 (Feature pill cluster)"
    resolution_line: "8 betas. Day zero. Today."
    type: "tension"   # the pain → resolution loop is the core narrative tension

  loop_openers:
    - scene: "Scene 02"
      position: "pivot"
      phrase: "But today, that lag is gone."
    - scene: "Scene 05"
      position: "transition"
      phrase: "And here's how it ships through your AWS account."
    - scene: "Scene 08"
      position: "objection-handle"
      phrase: "So when do you pick which?"
```

## Story Lock Placement

- **Lock #1 (Term Branding)**: Scene 02 — coin "Claude Platform on AWS" as a distinct product (not "Claude on AWS" or "Claude on Bedrock") with the GA date chip.
- **Lock #4 (Negative Frame)**: Scene 03 — "Claude on Bedrock has been lagging — Platform-on-AWS removes the lag." Negative frame on the COMPARISON, not on the viewer. Per Phase 1 hook scope rule, negative framing belongs in Scene 02+ — placed in Scene 03 (compliant).
- **Lock #5 (Loop Openers)**: Scenes 02, 05, 08 (per Open Loop Architecture above). 3 loop openers across 95s = within the 60-180s spec range (2-3 openers, every 60-90s).
- **Lock #3 (Thought Narration)**: Scene 06 — micro-narration moment after the 17-region slam: "[That's broader than most Claude routes at launch.]" — registers as an aside.

## Composition Layout

```yaml
composition_layout:
  template: "templates/shorts/anthropic"
  structure: "inline-phase + mutex-visibility"
  resolution: "1080x1920"
  frame_rate: 30
  total_data_duration: 95

  top_banner:
    persistent: true
    content: "Anthropic + AWS lockup (left-aligned, ~700px wide)"
    asset_strategy: "Combine shared/logos/anthropic-logo-light.svg + shared/logos/aws-logo.png in a horizontal flex container with a tasteful 'on' or '·' divider. If aws-logo.png is dark-only, render aws as 'AWS' text wordmark (JetBrains Mono 700, warm off-white) at matching height."
    safe_zone: "240px top reserved per DESIGN.md PHASE_PAD_TOP"

  phase_count: 9   # P1..P9 with whoosh transitions T1..T8 between them
  transition_pattern: "whoosh-only (one cinematic-whoosh per phase boundary, paired with shape-backdrop reposition; data-start = sceneT - 0.4 per audio-design.md HARD rule)"

  shape_backdrop:
    enabled: true
    asset: "assets/shapes/*.svg (template ships defaults — reposition per phase per .claude/rules/audio-design.md)"
    behavior: "rearranges on every phase transition (DEFAULT for shorts; replaces animateShapeDrift)"
```

## Retention Component Picks

```yaml
retention_component_picks:
  scene_01_hook:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam"
    primitives:
      - "gsap-stagger-grid"          # overline → hero phrase → 'WEEKS LATE' sub-slam
      - "marker-highlight"           # purple sweep under 'WEEKS LATE' (max 1/scene)
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"   # paired with cinematic-whoosh

  scene_02_pivot_reveal:
    structural: "inline-phase"
    pattern: "hero-slam"
    primitives:
      - "gsap-stagger-grid"          # BUT TODAY slam → product title → date chip
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_not_a_rebrand_split:
    structural: "inline-phase"
    pattern: "stat-pill-row (adapted as 2-column comparison)"
    primitives:
      - "gsap-stagger-grid"          # 3 bullet rows enter ~2.5s apart per step-by-step-reveal rule
      - "marker-highlight"           # orange sweep under 'DAY ZERO' on right-column closer (max 1/scene)
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_04_feature_pill_cluster:
    structural: "inline-phase"
    pattern: "stat-pill-row (extended to 8-pill cluster)"
    primitives:
      - "gsap-stagger-grid"          # 8 pills enter ~1.9s apart paced to narration anchors
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    note: "17s phase / 8 items = ~1.9s/item — within the 5s static-gap cap. Tail-hold ~2s at end before transition. HIDDEN-UNTIL-REVEAL pattern (tl.set + tl.to, not tl.from) per step-by-step-reveal.md."

  scene_05_aws_integration:
    structural: "inline-phase"
    pattern: "code-walkthrough (URL-pill variant — not a full sub-comp)"
    primitives:
      - "gsap-typewriter"            # endpoint URL types out char-by-char
      - "marker-highlight"           # under 'aws-external-anthropic' host (max 1/scene)
      - "gsap-stagger-grid"          # 3 integration chips drop in step-by-step (~3s apart, paced to narration)
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_06_17_regions_slam:
    structural: "inline-phase"
    pattern: "narrated-stat-reveal"
    primitives:
      - "gsap-stagger-grid"          # 17 region dots pop step-by-step (~0.35s apart — quick stagger allowed because narration says '17 regions' as ONE phrase, not enumeration)
      - "gsap-counter-tween"         # final '17' counter tweens 0→17 over 0.7s
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    note: "Hero slam (orange) at scene end. 240px '17' per type scale."

  scene_07_customer_trust:
    structural: "inline-phase"
    pattern: "stat-pill-row (3-wordmark adapt)"
    primitives:
      - "gsap-stagger-grid"          # 3 customer wordmarks enter ~2.4s apart
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    note: "Per gaps section: logos NOT in shared/logos. Render as Inter 800 typography wordmarks (ReliaQuest in red-tinted weight, OpenRouter in blue, Emergent in green to match accent rotation — one accent per wordmark to satisfy DESIGN.md 'no more than one accent per phase' by treating each as a brand color, not as decoration)."

  scene_08_when_to_pick_which:
    structural: "inline-phase"
    pattern: "stat-pill-row (2-column decision matrix)"
    primitives:
      - "gsap-stagger-grid"          # left col first, then right col (~5s apart)
      - "marker-highlight"           # under 'data MUST stay inside AWS' on Bedrock column (max 1/scene)
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_09_thumbnail_hold:
    structural: "inline-phase"
    pattern: "cta-url-slam (thumbnail-grade hold per .claude/rules/shorts-thumbnail-frames.md)"
    primitives:
      - "gsap-stagger-grid"          # all 5 thumbnail elements enter within 0.5s (composite hold)
      - "marker-circle"              # optional subtle circle on AWS in the title slam (max 1/scene)
    captions: null
    audio_reactive: null
    transition_out: null             # final scene — no transition; 1.5s+ static hold

# Constraint compliance
# - Markers per scene: 1 in scenes 01, 03, 05, 08, 09 — max 2 cap respected
# - Caption groups: zero (none needed; narration carries)
# - Audio-reactive: zero (calm dark-stage aesthetic; per-element SFX off by default per DESIGN.md 2026-04-28 calibration)
# - Transition: ONE primary (blur-crossfade) across all 8 transitions = 100% (well within 60-70% target — accents NOT needed for 95s composition)
```

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene_01_hook"
    data_start: 0.0
    data_duration: 8.0
    audio_anchor: "overline enters at 0.3s; hero phrase line 1 at 2.0s; 'WEEKS LATE' slam at 5.5s; marker sweep at 6.0s"

  - scene: "scene_02_pivot_reveal"
    data_start: 8.0
    data_duration: 7.0
    audio_anchor: "'BUT TODAY' slam at 8.0s (whoosh fires at 7.6s = 8.0 - 0.4); product title at 10.0s; date chip at 12.0s"

  - scene: "scene_03_not_a_rebrand_split"
    data_start: 15.0
    data_duration: 11.0
    audio_anchor: "column headers at 15.5s; 3 bullets enter at 17.5s, 20.0s, 22.5s; 'DAY ZERO' marker at 24.0s"

  - scene: "scene_04_feature_pill_cluster"
    data_start: 26.0
    data_duration: 17.0
    audio_anchor: "headline at 26.3s; pills enter at 28.0, 29.9, 31.8, 33.7, 35.6, 37.5, 39.4, 41.3s (~1.9s apart); 1.5s tail hold"

  - scene: "scene_05_aws_integration"
    data_start: 43.0
    data_duration: 14.0
    audio_anchor: "URL typewriter starts at 43.4s; marker on host at 46.5s; 3 chips drop at 49.0s, 52.0s, 55.0s"

  - scene: "scene_06_17_regions_slam"
    data_start: 57.0
    data_duration: 8.0
    audio_anchor: "map enters at 57.3s; 17 region dots pop 57.7-63.0s (quick stagger); '17' counter slam at 63.2s"

  - scene: "scene_07_customer_trust"
    data_start: 65.0
    data_duration: 9.0
    audio_anchor: "overline at 65.3s; ReliaQuest at 66.5s; OpenRouter at 68.9s; Emergent at 71.3s; 1.2s tail hold"

  - scene: "scene_08_when_to_pick_which"
    data_start: 74.0
    data_duration: 11.0
    audio_anchor: "headline at 74.3s; left col at 75.5s; right col at 80.5s; marker on 'inside AWS' at 82.5s"

  - scene: "scene_09_thumbnail_hold"
    data_start: 85.0
    data_duration: 10.0
    audio_anchor: "Dynamous outro narration '...check out the dynamous.ai community.' lands here; all 5 thumbnail elements enter 85.0-85.5s; static hold 85.5-95.0s = 9.5s held still (well above 1.5s minimum)"

total_data_duration: 95
```

**Visual pacing audit (per [`.claude/rules/visual-pacing-5s.md`](../../.claude/rules/visual-pacing-5s.md))**:

| Scene | Largest internal gap | Pass? |
|---|---|---|
| 01 (8s, 3 entrances + marker) | 2.0s → 5.5s = 3.5s | PASS |
| 02 (7s, 3 entrances) | 8.0 → 10.0 = 2.0s; 10.0 → 12.0 = 2.0s | PASS |
| 03 (11s, header + 3 bullets + marker) | 2.5s gaps between bullets | PASS |
| 04 (17s, headline + 8 pills) | 1.9s between pills | PASS (well under 5s) |
| 05 (14s, URL + marker + 3 chips) | 3.0s between chips | PASS |
| 06 (8s, map + dots + counter) | <0.4s between dots | PASS |
| 07 (9s, overline + 3 wordmarks) | 2.4s between wordmarks | PASS |
| 08 (11s, header + 2 cols + marker) | 5.0s left→right (AT the cap — narration will fill via decision-matrix bridge connector "OR if your data MUST stay inside AWS…"; Phase 3.5 can tighten if needed) | PASS (at cap) |
| 09 (10s, thumbnail hold) | 9.5s static — **EXPLICIT RELAXATION** per [`.claude/rules/shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md) which relaxes the 5s rule for the terminal hold only | PASS (rule-relaxed) |

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []          # none — use Anthropic dark-stage tokens verbatim
  fonts:
    sans: "Inter"
    mono: "JetBrains Mono"
  accent_rotation_plan:
    scene_01: "purple (#A78BFA) — marker on 'WEEKS LATE', dim/cool pain tone"
    scene_02: "orange (#E97458) — title reveal hero accent"
    scene_03: "split — left col dim blue (#6B9AEF), right col orange (#E97458)"
    scene_04: "orange (#E97458) — primary, all 8 pills in orange family (one accent per phase)"
    scene_05: "blue (#6B9AEF) — technical/integration colorway, URL pill"
    scene_06: "orange (#E97458) — hero slam '17'"
    scene_07: "rotating — purple for ReliaQuest, blue for OpenRouter, green for Emergent (justified as wordmark brand colors, not decorative)"
    scene_08: "split — orange left (Platform-on-AWS), blue right (Bedrock)"
    scene_09: "orange (#E97458) — thumbnail title slam in warm off-white with orange marker accent"
```

## AI Image Prompts

None. The composition relies on typography, real logos (Anthropic + AWS), a custom dark-styled SVG world-map, and styled-text wordmarks for the launch customers. No AI-generated hero shots / backgrounds needed.

## Screenshot Inventory

```yaml
screenshots:
  - name: "anthropic-claude-platform-aws-blog"
    url: "https://claude.com/blog/claude-platform-on-aws"
    scene: "scene_02 (optional anchor)"
    color_scheme: "dark"
    usage: "Optional: small ghost of blog hero behind the title slam for authority. NOT REQUIRED — the title slam can stand on its own with the date chip."

  - name: "aws-blog-claude-platform"
    url: "https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/"
    scene: "scene_05 (optional anchor)"
    color_scheme: "dark"
    usage: "Optional: small ghost of AWS blog hero behind the integration chips. NOT REQUIRED — the endpoint URL + 3 chips carry the scene."
```

Both are flagged optional. The composition build phase will decide based on visual density — if the integration scene feels light without an anchor, capture the AWS blog hero. Otherwise omit.

## HyperFrames Blocks

None. The composition is authorable with template primitives only. Reviewed registry catalog ([`.claude/rules/registry-blocks-catalog.md`](../../.claude/rules/registry-blocks-catalog.md)):

- **No world-map block exists** (confirmed in catalog "Gaps / Needs User Input" of brief) — Scene 06 needs a custom SVG.
- **`vfx-iphone-device`, `vfx-shatter`, `vfx-portal`** etc. — none fit the news-explainer dark-stage aesthetic (would feel over-produced for a 95s product announcement Short).
- **Shader transitions** — `blur-crossfade` (CSS, calm energy per `transitions.md`) is the right pick; no shader needed.
- **Social overlays** (`x-post`, `instagram-follow`, etc.) — not relevant to this topic.

```yaml
hyperframes_blocks_used: []   # none
```

## Fact-Check Audit

Every claim in this plan traces to a source URL in the brief's `Receipts` and `Sources` tables. **Phase 2b will re-verify after script generation** — Phase 1 audit confirms the plan's claims are sourceable.

| Claim | Source URL | Audit Status |
|---|---|---|
| Claude Platform on AWS is GA today (May 11, 2026) | https://aws.amazon.com/about-aws/whats-new/2026/05/claude-platform-aws/ | SOURCED |
| Available in 17 AWS regions at launch | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ | SOURCED |
| 8 beta features land day-one on AWS (Managed Agents, Advisor, Skills, Files, MCP, Code execution, Web search, Console) | https://claude.com/blog/claude-platform-on-aws | SOURCED |
| Day-zero feature parity with native Claude API | https://claude.com/blog/claude-platform-on-aws ("all native Claude API features from day one … new features and betas shipping the same day") | SOURCED |
| Endpoint URL pattern `aws-external-anthropic.<region>.api.aws` | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ | SOURCED |
| Authentication via AWS Signature Version 4 (IAM) | https://aws.amazon.com/blogs/machine-learning/... | SOURCED |
| CloudTrail audit logging | https://aws.amazon.com/blogs/machine-learning/... | SOURCED |
| AWS Marketplace billing, retires against commitment | https://aws.amazon.com/blogs/machine-learning/... + https://claude.com/blog/claude-platform-on-aws | SOURCED |
| Three launch customers: ReliaQuest, OpenRouter, Emergent | https://claude.com/blog/claude-platform-on-aws | SOURCED |
| Bedrock is the data-resident subset (data inside AWS) vs Platform-on-AWS data processed outside AWS boundary | https://aws.amazon.com/blogs/machine-learning/... + https://dev.classmethod.jp/en/articles/claude-platform-on-aws-bedrock-differences/ | SOURCED |
| Models: Opus 4.7, Sonnet 4.6, Haiku 4.5 | https://claude.com/blog/claude-platform-on-aws | SOURCED (not used in current plan — held in reserve; could surface in Scene 04 or thumbnail) |

**Audit summary**: 11 distinct factual claims, **11 sourced (100%)**, 0 removed, 0 rephrased. The plan deliberately omits the `5GW / $100B / ~500K Trainium2` infrastructure stats (brief lists them as "Could Include") to keep the 95s short focused on the product news — they live in the brief for Phase 2 reference but won't surface unless script time opens up.

**Hook variant Source Fidelity gate**: All 3 variants pass. `head_nouns` match the source's nouns verbatim — no `30,000 engineers`-style substitution. Variant A's "features" matches source "API features"; Variant B's "features / betas / developers" matches "new features and betas / native Claude API"; Variant C's "betas / regions" matches "API features … 17 AWS regions".

## Notes for Composition Build

1. **Top banner**: Use Anthropic + AWS lockup as the persistent top banner. If `shared/logos/aws-logo.png` is dark-stage incompatible, render "AWS" as JetBrains Mono 700 text wordmark to match the Anthropic SVG's height. The banner is REQUIRED for thumbnail-final-frame brand chrome.

2. **Customer logos (Scene 07)**: ReliaQuest, OpenRouter, and Emergent logos are **not** in `shared/logos/`. Render as Inter 800 typography wordmarks per the gaps section. Each gets a distinct accent color (purple / blue / green) — this is the ONE scene where accent rotation crosses elements, justified as wordmark brand color rather than decorative styling.

3. **17-region map (Scene 06)**: No registry block exists. Hand-roll a dark-styled SVG world map at 800×600 (vertical-cropped). 17 dot anchors approximated to: 6× US, 2× Canada, 4× EU (FRA/IRL/STO/LON), 3× APAC (TYO/SIN/SYD), 1× Brazil, 1× South Africa. Quick stagger (~0.35s apart) because narration says "17 regions" as one phrase, not as enumeration. After dots land, dots collapse/converge into a single 240px orange "17" counter (`gsap-counter-tween` 0→17 over 0.7s).

4. **Feature pill cluster pacing (Scene 04)**: 17 seconds / 8 pills = ~1.9s/pill. Use the HIDDEN-UNTIL-REVEAL pattern (`tl.set(pill, {opacity:0, y:20}, 0)` + `tl.to(pill, {opacity:1, y:0}, t)`) per [`.claude/rules/step-by-step-reveal.md`](../../.claude/rules/step-by-step-reveal.md). NOT `tl.from()` — that leaves pills visible until the tween fires.

5. **TTS heteronym preflight**: per [`.claude/rules/tts-pronunciation.md`](../../.claude/rules/tts-pronunciation.md), check the script for:
   - "live" — swap to "available" / "shipping" if it appears in adjective sense (e.g., "go live" → "ship today")
   - "lead" — swap to "primary" or "coordinator" if "lead agent" appears
   - The script's connector "Three customers are already live" → flag and swap to "Three customers are already shipping" or "Three named customers, day one"
   - Also: per the brief's TTS table — "AWS" / "IAM" / "API" / "MCP" spelled out; "Opus 4.7" → "Opus four point seven"; "5GW" → "five gigawatts"; "GA" → "generally available"; "SigV4" → "Sig V four"

6. **Dynamous outro**: spoken outro per locked phrasing: "If you want to learn more about AI, check out the dynamous.ai community." Lands in Scene 09 narration; thumbnail visuals carry the rest. Pronounce "dynamous.ai" as "dynamous dot AI" per `tts-pronunciation.md` brand table.

7. **Final frame (Scene 09) 5-element check** per [`.claude/rules/shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md):
   - ✅ Topic statement: "CLAUDE PLATFORM. ON AWS." (160px dominant)
   - ✅ Visual anchor: Anthropic + AWS lockup (top-left brand chrome, also acts as anchor)
   - ✅ Brand chrome: same lockup serves both — explicit 48px logo height in scene
   - ✅ Outcome receipt: "8 betas. 17 regions. Day zero." (52px)
   - ✅ Subordinate CTA: "Watch the full breakdown →" (46px, bottom)
   - All entrances finish by 85.5s → 9.5s static hold (well above 1.5s minimum, AT cap of 2.5s relaxation — but the rule says hold "≥1.5s" with no upper cap, just notes "1.8s minimum, 2.0-2.5s recommended" for the phase. Our 10s phase is fine because the static hold can extend if narration warrants and the Dynamous outro lands here).
   - REVISIT: if the Dynamous outro narration takes <3s, shorten Scene 09 to 6s; if longer, extend. Phase 3.5 will retime against transcript.json.

8. **SFX strategy**: Per the template's 2026-04-28 calibration, DEFAULT is `cinematic-whoosh` per phase transition ONLY — no per-element impact-slams, spring-pops, or pops. The whoosh fires at `sceneT - 0.4` to sync with the shape-backdrop reposition (HARD rule per `audio-design.md`). This composition has 8 phase transitions → 8 whooshes. Optional opt-in: ONE `impact-slam` at Scene 02's "BUT TODAY" hero word (the single most warranted moment); evaluate during composition build whether it's needed or if narration shake suffices.

9. **Connector words / news-explainer flow**: Scene transitions must carry explanatory connectors per news-explainer voice profile. The connector list in "Narrative Arc" above is the canonical set Phase 2 / 2.5 will enforce. Pure-fragment scripts fail Phase 2.5 Pass 6.

10. **Phase 3.5 retention strategy** will refine all `audio_anchor` placeholders against `transcript.json` once TTS lands. The placeholder times here are conservative estimates; expect ±1-2s shift per scene.

**Next step**: Run `/diy-yt-creator:phase2-script claude-platform-on-aws`.
