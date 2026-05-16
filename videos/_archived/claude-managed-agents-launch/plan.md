# Composition Plan: claude-managed-agents-launch

## Director's Summary

A 130-second Anthropic-dark-stage Short on the Claude Managed Agents launch (May 6, 2026). Opens with a counterintuitive hook — Anthropic just made Claude agents **DREAM** — then snapbacks: dreaming is the *only* feature still gated. The body walks the four-pillar primitive set (Dreaming RP, Outcomes / Multiagent / Webhooks public-beta), each with one benefit, one receipt, and one visual metaphor, before closing on a trust strip and the Dynamous endcard. The aesthetic spine is the four-pillar status row with badge color encoding research-preview vs public-beta — making the source.md hard distinction visually inescapable.

---

## Template & Structure

- **Template**: `templates/shorts/anthropic` (1080x1920 vertical, dark-stage, 30fps)
- **Composition layout**: `inline-phase` + `mutex-visibility` (template-enforced — see `templates/shorts/anthropic/README.md:11-18` and CLAUDE.md "What NOT to Do" #6 — no background music, narration + SFX only)
- **Total target duration**: ~130s (inside the 90-180s window)
- **Voice profile**: `news-explainer` — every scene-to-scene transition wired with an explanatory connector (Phase 2.5 Pass 6 gate)
- **Tone**: tech-influencer-edgy, "the moat just got real" framing
- **Design tokens**: pulled directly from `templates/shorts/anthropic/DESIGN.md` (no overrides — Anthropic-on-Anthropic palette is correct here)

---

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements |
|---|---|---|---|---|
| **S00 — Preview Hook** | 0 | 7 | Scroll-stop tease — "Anthropic just made Claude agents DREAM" + 3 micro-teasers of upcoming pillars | hero slam "DREAM", 3 rapid-fire pillar chips at 0.5s each |
| **S01 — Open Loop** | 7 | 8 | The Uno-reverse: "Three shipped today. One is gated. Can you guess which?" | velvet-rope-vs-open-door dual frame, "Three / One" stat pair |
| **S02 — Four Pillars** | 15 | 17 | Step-by-step status row — Dreaming (RP) + Outcomes / Multiagent / Webhooks (public-beta) | 4 pillars entering ~3.5s apart, badge color encodes status |
| **S03 — Dreaming** | 32 | 18 | Sleep-time learning visualization — sessions → memory cylinder → curated memories | dream-cycle loop, RP gated badge, "Request access" pill |
| **S04 — Outcomes** | 50 | 18 | Rubric grader auto-iterates — Pass 1 (red) → Pass 2 (green) | rubric checklist with red→green tween, +10 pts counter |
| **S05 — Multiagent** | 68 | 18 | Lead agent delegates parallel specialists — Netflix / Harvey receipt | lead box → 4 columns staggered, Harvey "~6×" stat slam |
| **S06 — Webhooks** | 86 | 13 | Closes the polling loop | polling cron strikethrough → single webhook bell |
| **S07 — Trust Strip** | 99 | 15 | Pricing pill + beta header code chip + 1 anonymized community quote | $0.08/session-hour, `managed-agents-2026-04-01`, ambient quote tile |
| **S08 — CTA + Dynamous Endcard** | 114 | 16 | Form URL slam + handoff to standard Dynamous outro | claude.com/form/claude-managed-agents pill + Dynamous endcard wiring |

`#root` `data-duration` = **130** (sum of all scenes; total below).

---

## Narrative Arc

Kallaway formula mapping (per `news-explainer` voice — every scene exits on a connector word):

1. **Context Lean-In** (S00, 0-7s, 5.4% of duration): "Anthropic just made Claude agents DREAM." Bold scroll-stop, the dream-cycle metaphor anchors instantly.
2. **Scroll-Stop Interjection** (S01, 7-15s): "But the headline isn't dreaming." Stun-gun word "But" lands at ~8s.
3. **Contrarian Snapback** (S01 → S02, 13-17s): "Three other primitives shipped today — and they're the actual moat." Reveal the four-pillar row.
4. **Solution** (S02, 15-32s, 13% of duration): Frame Claude Managed Agents as the platform — four primitives, three shipping, one gated.
5. **Deep Dive — features benefit-led** (S03–S06, 32-99s, 51.5% of duration): one scene per primitive, each opening with the benefit, closing with the connector that bridges to the next.
6. **Social Proof / Trust** (S07, 99-114s, 11.5% of duration): pricing pill + beta header code chip + 1 anonymized community quote ("the orchestration layer is where the real moat lives" — paraphrased, no handle).
7. **CTA** (S08, 114-130s, 12%): form URL slam handed to the standard Dynamous endcard.

**Connector-word plan** (mandatory for `news-explainer` profile):

| From → To | Connector at scene boundary |
|---|---|
| S00 → S01 | "But …" |
| S01 → S02 | "Because …" |
| S02 → S03 | "First, …" / "Start with …" |
| S03 → S04 | "Then …" / "Next …" |
| S04 → S05 | "And while one agent grades, …" |
| S05 → S06 | "Plus, …" / "And to know when they're done, …" |
| S06 → S07 | "Here's why this lands: …" |
| S07 → S08 | "So — …" |

**Explosion timer**: the first true value-payload (the pillar count + status distinction) lands at ~13s — well inside the 60-120s long-form window the brief allows.

---

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Anthropic just made Claude agents DREAM."
    layers_present: [1, 4, 5]   # counterintuitive + stun-gun ('just') + promise (preview teases payoff)
    source_fidelity:
      source_quote: "Live from Code with Claude: we're launching dreaming in Claude Managed Agents as a research preview."
      head_nouns: ["Claude agents", "Anthropic"]
      passes_gate: true
    advisory_score: 8.7   # base = (9*0.4 + 7*0.4 + 8*0.2) = 8.0; alignment +1 (names the feature); narrative_flow 0 (single fragment); promise +0 explicit; total 9.0 → cap 9.0; conservatively 8.7 to leave variance headroom
  variant_b:
    type: "stakes"
    opening_line: "If you're still polling agent endpoints, you're already behind."
    layers_present: [2, 4, 5]
    source_fidelity:
      source_quote: "managed Agents with webhooks finally closes the loop for real production workflows. Big day."
      head_nouns: ["agent endpoints"]
      passes_gate: true
    advisory_score: 7.4   # base = (7*0.4 + 9*0.4 + 6*0.2) = 7.6; alignment +0 (stakes only); narrative_flow 0; promise +0; conservative
  variant_c:
    type: "number"
    opening_line: "1 million views. 6× completion rate. Available today on Claude Platform."
    layers_present: [3, 4, 5]
    source_fidelity:
      source_quote: "(reach metrics from X-post lead) 1M Views · 8K likes · 702 RTs · 3.8K bookmarks; (Harvey stat from blog) ~6× completion rate"
      head_nouns: ["views", "completion rate", "Claude Platform"]
      passes_gate: true
    advisory_score: 7.6   # base = (7*0.4 + 8*0.4 + 10*0.2) = 8.0; alignment +1 (names Claude Platform); but 1M-views opener is hype-heavy and viewer-irrelevant; conservative discount
  recommended: "variant_a"
```

**Selection rationale (autonomous mode)**: variant_a wins on advisory score (8.7) AND on Value Alignment — it names the headline feature ("DREAM") in line 1, which the brief flagged as the strongest scroll-stop using Anthropic's own anthropomorphic framing. Variant C is technically high-spec but its 1M-views lead is a vanity metric that doesn't earn the click for builders. Variant B's pain-first stakes hook is solid but less specific — saved as a fallback if "DREAM" reads as too-clickbait in Phase 2 review.

**Source-Fidelity gate — verified for variant_a**: the source post says "Claude Managed Agents" (the platform); the hook says "Claude agents" (a permitted shorthand of the same noun, not a substitution). No swap of `employees → engineers` style noun-drift. Passes.

---

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "FilmTrailer"
  selected_variant: "variant_a"

  visual_beats:
    - beat: "Cold Open"
      timing_s: [0, 0.8]
      visual: "Pure #0B0F18 → Anthropic wordmark fades into top banner; a dim radial-orange glow pulses on once at center"
      gsap_ease: "power3.out"
      sfx: null
    - beat: "Hero Slam — DREAM"
      timing_s: [0.8, 2.6]
      visual: "240px Inter-900 'DREAM' slams in centered with -4px tracking and accent-orange text-shadow halo. Inline shake (3-frame, ±6px) on impact frame."
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake (own tracks, 0.20 / 0.15)"
    - beat: "Context line"
      timing_s: [2.6, 4.5]
      visual: "Below the slam, 64px Inter-800 'Anthropic just made Claude agents…' rises +40 → 0; 'DREAM' becomes the answer pivoting up to its slot"
      gsap_ease: "power3.out"
      sfx: null
    - beat: "Micro-teaser chip 1"
      timing_s: [4.5, 5.2]
      visual: "First mono pill enters bottom — `DREAMING · research preview` — purple accent border"
      gsap_ease: "back.out(1.7)"
      sfx: "spring-pop (0.15)"
    - beat: "Micro-teaser chip 2"
      timing_s: [5.2, 5.9]
      visual: "Second pill stacks under it — `OUTCOMES · public beta` — green accent"
      gsap_ease: "back.out(1.7)"
      sfx: "spring-pop (0.15)"
    - beat: "Micro-teaser chip 3"
      timing_s: [5.9, 6.6]
      visual: "Third pill — `+ MULTIAGENT · WEBHOOKS` — blue accent"
      gsap_ease: "back.out(1.7)"
      sfx: "spring-pop (0.15)"
    - beat: "Phase exit — whoosh to S01"
      timing_s: [6.6, 7.0]
      visual: "Blur-crossfade out; the 3 chips will be re-cast in S02's full pillar row"
      gsap_ease: "sine.inOut"
      sfx: "cinematic-whoosh (0.15)"

  pivot_word: "But"             # lands at ~7.5s — opens S01
  brand_reveal_word: "Claude"   # in 'Claude agents' at 2.6s; the Anthropic wordmark is already up

  assets_needed:
    - type: "logo"
      description: "Anthropic wordmark — light variant on dark canvas"
      source: "../../shared/logos/anthropic-logo-light.svg (template default; copy locally during composition build)"
    - type: "screenshot/illustration"
      description: "Anthropic blog Dreaming visualization PNG (used as backdrop in S03, NOT in S00 — S00 stays type-only for scroll-stop snap)"
      source: "https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8e9ad765c7eed52dcf468_Claude-Managed-Agents-Blog-Followup-Dreaming.png — download to videos/<slug>/assets/dreaming-hero.png"
    - type: "screenshot/illustration"
      description: "Anthropic blog Sessions UI PNG (S05 multiagent backdrop)"
      source: "https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8ea208aefcf18345ee3ef_Claude-Managed-Agents-Blog-Followup-Sessions-UI.png — download to videos/<slug>/assets/sessions-ui.png"

  music_profile:
    hook_mood: NONE   # template forbids background music on Shorts (templates/shorts/anthropic/DESIGN.md "What NOT to Do" #6)
    hook_bpm: null
    body_bpm: null
    cta_bpm: null

sfx_cues:                          # Phase 3.5 will refine timing in seconds
  - beat: "Hero Slam — DREAM"
    cues: [impact-slam, screen-shake]
  - beat: "Micro-teaser chip 1"
    cues: [spring-pop]
  - beat: "Micro-teaser chip 2"
    cues: [spring-pop]
  - beat: "Micro-teaser chip 3"
    cues: [spring-pop]
  - beat: "Phase exit — whoosh"
    cues: [cinematic-whoosh]
  - beat: "S01 BUT pivot"
    cues: [impact-slam, glitch-zap]
  - beat: "S02 each pillar entrance"
    cues: [spring-pop]                # x4, one per pillar
  - beat: "S02 → S03 transition"
    cues: [cinematic-whoosh]
  - beat: "S03 → S04 transition"
    cues: [cinematic-whoosh]
  - beat: "S04 rubric red→green flip"
    cues: [strike-cross]
  - beat: "S05 Harvey 6× stat slam"
    cues: [scale-slam]
  - beat: "S05 specialist column entrances"
    cues: [pop]                       # x4
  - beat: "S06 polling strikethrough"
    cues: [strike-cross]
  - beat: "S06 webhook bell single ring"
    cues: [spring-pop]
  - beat: "S07 quote tile entrance"
    cues: [spring-pop]
  - beat: "S08 CTA URL slam"
    cues: [scale-slam]
```

All cue names verified against `shared/audio/MANIFEST.md` (no fabricated filenames).

---

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "S01 (Open Loop)"
    setup_line: "Three shipped today. One is gated. Can you guess which?"
    resolution_scene: "S03 (Dreaming) + reinforced in S08 (CTA)"
    resolution_line: "Dreaming — the named flagship — is the gated one. The boring plumbing actually shipped."
    type: "question"
  loop_openers:
    - scene: "S02"
      position: "opening"
      phrase: "Because here's the line-up."
    - scene: "S05"
      position: "transition"
      phrase: "And here's where it gets real."
    - scene: "S07"
      position: "transition"
      phrase: "Here's why this lands."
```

---

## Story Lock Placement

- **Term Branding (Lock #1)** — S03: introduces "**Dreaming**" with marker-circle on the word the first time it's spoken; the brand-coined term carries the rest of the video.
- **Loop Openers (Lock #5)** — S02 ("Because here's the line-up"), S05 ("And here's where it gets real"), S07 ("Here's why this lands").
- **Negative Frame (Lock #4)** — S06 only: "Stop polling. Subscribe to a webhook." Reserved for S06 because the brief calls polling out as the explicit pain point — no other scene gets a Negative Frame (per the project rule that Negative Frames belong post-hook).
- **Thought Narration (Lock #3)** — S05 (post-Harvey-stat reveal): "Six-times completion rate. That's not a demo number — that's a legal-AI production deployment." One thought-narration beat after the biggest receipt.

Scope rule respected — no Negative Frames or Loop Openers in S00/S01 hook.

---

## Composition Layout

```yaml
composition_layout:
  template: "templates/shorts/anthropic"
  model: "inline-phase"
  visibility: "mutex-visibility"
  phase_count: 9                 # S00..S08 → #phase0..#phase8 z-stack
  phase_naming: "P0..P8 with T0..T7 transitions (P/T convention per template README §'Adding more phases')"
  z_stack_floor: 0
  primary_transition: "blur-crossfade"   # 0.4s opacity + 0.5s blur, sine.inOut — used 7× of 8 transitions
  accent_transitions:
    - name: "zoom-through"
      used_at: "T4 (S04→S05) only — gives the Multiagent reveal extra energy aligned with Harvey 6× stat"
  exit_animations: "BANNED on non-final scenes (transitions handle exit)"
  final_scene_exit: "S08 fades to black with Dynamous endcard handoff (final scene allowed)"
```

---

## Retention Component Picks

```yaml
retention_component_picks:

  S00_preview_hook:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam"
    primitives:
      - "gsap-stagger-grid"        # 3 micro-teaser chips enter ~0.7s apart
      - "marker-highlight on DREAM"  # 1 marker — orange bar sweeps behind the slam word
    captions: null                  # too short for synced captions
    audio_reactive: null
    transition_out: "blur-crossfade"

  S01_open_loop:
    structural: "inline-phase"
    pattern: "stat-pill-row (adapted — 'Three' / 'One' as the two pills)"
    primitives:
      - "gsap-counter-tween on the '3' digit (0 → 3 in 0.4s)"
      - "marker-circle on 'gated'"   # 1 marker — hand-drawn circle around the contrarian word
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  S02_four_pillars:
    structural: "inline-phase"
    pattern: "stat-pill-row (4 pills instead of 2 — same archetype, expanded grid)"
    primitives:
      - "gsap-stagger-grid"          # 4 pills enter step-by-step at +0s, +3.5s, +7s, +10.5s — paced to narration
      - "marker-highlight on 'research preview'"  # 1 marker — purple bar to lock the gated-vs-open distinction
    captions: "caption-fade-slide"   # narration is 4 named primitives + status — calm, measured
    audio_reactive: null
    transition_out: "blur-crossfade"

  S03_dreaming:
    structural: "inline-phase"
    pattern: "narrated-stat-reveal (centered around the Dreaming PNG hero shot)"
    primitives:
      - "gsap-stagger-grid"          # 3 session cards enter, then memory cylinder, then curated-memories radiate out
      - "gsap-path-draw"             # arrows from sessions → memory store
      - "marker-circle on 'Dreaming'"  # 1 marker — Term Branding lock
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  S04_outcomes:
    structural: "inline-phase"
    pattern: "narrated-stat-reveal (rubric grader loop)"
    primitives:
      - "gsap-stagger-grid"          # rubric items appear one at a time
      - "gsap-counter-tween"         # +10 pts counter ticks up
      - "marker-highlight on '+10 points'"  # 1 marker on the receipt number
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "zoom-through"   # accent transition — feeds Multiagent reveal energy

  S05_multiagent:
    structural: "inline-phase"
    pattern: "timeline-cards (adapted — 4 vertical specialist columns instead of 3 horizontal cards)"
    primitives:
      - "gsap-stagger-grid"          # 4 specialist columns enter at +0s, +0.5s, +1.0s, +1.5s (this IS a quick stagger — the narrator says 'parallel specialists' once, not 4 names)
      - "gsap-counter-tween"         # Harvey '6×' tweens 0 → 6 with scale-slam
      - "marker-burst on 6×"          # 1 marker — radiating lines on the biggest stat
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  S06_webhooks:
    structural: "inline-phase"
    pattern: "stat-pill-row (polling-vs-webhook side-by-side)"
    primitives:
      - "gsap-stagger-grid"          # left polling cron stack appears first (3 calls), then strikethrough crosses, then webhook bell rings once
      - "marker-scribble across the polling stack"  # 1 marker — chaotic strike-out
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  S07_trust_strip:
    structural: "inline-phase"
    pattern: "stat-pill-row (3 elements — pricing, code chip, quote)"
    primitives:
      - "gsap-stagger-grid"          # pricing pill, beta-header code chip, quote tile each enter ~5s apart
      - "gsap-typewriter on the beta-header code chip"  # `managed-agents-2026-04-01` types out char-by-char
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  S08_cta_dynamous:
    structural: "inline-phase"
    pattern: "cta-url-slam (form URL) → handoff to standard Dynamous endcard"
    primitives:
      - "marker-circle on the form URL"   # 1 marker — drawn around claude.com/form/claude-managed-agents
      - "gsap-stagger-grid"               # form URL pill, then Dynamous endcard component reveals
    captions: null
    audio_reactive: null
    transition_out: null   # final scene — fade to black; Dynamous endcard wiring handled by playbook
```

**Retention pick counts (audit)**:
- Markers: 8 total, max 1/scene (well under cap of 2/scene) — `marker-highlight` ×3 (S00, S02, S04), `marker-circle` ×3 (S01, S03, S08), `marker-burst` ×1 (S05), `marker-scribble` ×1 (S06). Frequency cap respected.
- Captions: 6 scenes use `caption-fade-slide` (S02-S07); S00, S01, S08 omit captions. One caption group visible at a time (mutex-visibility makes this automatic).
- Audio-reactive: NONE. Narration is too information-dense for audio-reactivity to read; this is news-explainer not music-driven.
- Transitions: `blur-crossfade` ×7 (primary, 88%) + `zoom-through` ×1 accent at T4 only. One primary + one accent — within the rule.
- Anti-pattern audit: no Remotion bits, no spectrum visuals, no exit animations on non-final scenes, no caption overlap (mutex), no rainbow-transition (one primary only). Clean.

---

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "S00_preview_hook"
    data_start: 0
    data_duration: 7
    audio_anchor: "narration starts at ~0.5s; 'DREAM' word lands at ~1.2s"

  - scene: "S01_open_loop"
    data_start: 7
    data_duration: 8
    audio_anchor: "'But' connector at ~7.6s; 'gated' lands at ~12.5s"

  - scene: "S02_four_pillars"
    data_start: 15
    data_duration: 17
    audio_anchor: "'Dreaming' named at ~16.5s; 'Outcomes' at ~20s; 'Multiagent' at ~23.5s; 'Webhooks' at ~27s — paced ~3.5s apart per step-by-step-reveal rule"

  - scene: "S03_dreaming"
    data_start: 32
    data_duration: 18
    audio_anchor: "'Reviews past sessions' at ~33s; 'Request access' CTA pill enters at ~46s; visual beats at +5s, +9s, +13s ensure no static gap > 5s"

  - scene: "S04_outcomes"
    data_start: 50
    data_duration: 18
    audio_anchor: "'rubric' at ~51.5s; '+10 points' counter ticks at ~62s; red→green tween at ~64s"

  - scene: "S05_multiagent"
    data_start: 68
    data_duration: 18
    audio_anchor: "'lead agent delegates' at ~69s; specialist columns enter +0s, +0.5s, +1.0s, +1.5s (quick stagger acceptable here per narration that says 'parallel specialists' once); Harvey '6×' slam at ~80s"

  - scene: "S06_webhooks"
    data_start: 86
    data_duration: 13
    audio_anchor: "'Stop polling' Negative Frame at ~87s; webhook bell rings at ~94s with single spring-pop"

  - scene: "S07_trust_strip"
    data_start: 99
    data_duration: 15
    audio_anchor: "pricing pill enters at ~100s; beta header code chip types out 100-103s; community quote tile fades in at ~108s"

  - scene: "S08_cta_dynamous"
    data_start: 114
    data_duration: 16
    audio_anchor: "form URL slam at ~115s; spoken Dynamous outro line ('If you want to learn more about AI, check out the dynamous.ai community.') runs ~119-126s; final breath beat 126-130s"

total_data_duration: 130
```

Notes for Phase 3.5:
- All `audio_anchor` values are placeholders — refine against `transcript.json` once TTS lands.
- S08's `data_duration` of 16 is generous to allow the Dynamous endcard wiring (badge + endcard from `videos/_template-wiring-snippet.md`) without rushing the spoken outro line.
- **Visual pacing audit (5s rule)**: every scene's beat cadence is below — no gap > 5s between visual events:
  - S02 (17s): 4 entrances at +0/+3.5s/+7s/+10.5s → tail-hold 10.5-15.5s with all 4 visible (5s tail) → exit at 17s. Largest gap: 5s tail-hold — at the cap. Acceptable.
  - S03 (18s): hero PNG fade-in @ +0.5s, dream-cycle pulses @ +5s, RP badge @ +9s, "Request access" pill @ +13.5s, exit @ 18s. Gaps ≤ 4.5s.
  - S04 (18s): rubric items entrance × 3 @ +1/+5/+9s, red→green flip @ +13s, +10 pts counter @ +15s, exit @ 18s. Gaps ≤ 4s.
  - S05 (18s): lead agent @ +0.5s, 4 columns staggered @ +3-4.5s, parallel timeline progression with check ticks every ~3s, Harvey 6× slam @ +12s, exit @ 18s. Gaps ≤ 4s.
  - S07 (15s): pricing pill @ +0.5s, beta-header typewriter 1-4s (continuous motion), code chip pop @ +5s, quote tile @ +9s, scale-pulse on quote keyword @ +13s, exit @ 15s. Gaps ≤ 4.5s.
  - S08 (16s): URL slam @ +0.5s, marker-circle draw @ +3s, Dynamous endcard reveal @ +6s, badge components stagger @ +8s/+10s/+12s, fade-to-black @ 14.5-16s. Gaps ≤ 4.5s.

---

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []   # Anthropic-on-Anthropic — palette is canonical for this video; no overrides
  fonts:
    sans: "Inter"               # template default
    mono: "JetBrains Mono"      # template default
  accent_rotation_per_scene:
    S00: "orange"               # hero
    S01: "purple"               # contrarian
    S02: "rotates — purple (Dreaming RP), green (Outcomes/Multiagent/Webhooks public-beta)"
    S03: "purple"               # Dreaming = research preview
    S04: "green"                # Outcomes = public beta + lift = positive
    S05: "blue"                 # Multiagent = technical / orchestration
    S06: "orange"               # Webhooks = closes the loop, primary callback
    S07: "neutral (off-white pill bg + accent borders only)"
    S08: "orange"               # CTA back to brand primary
  badge_color_encoding:
    research_preview: "purple border + 'GATED' chip — `marker-circle` on first appearance"
    public_beta:      "green border + 'TODAY' chip"
```

Accent rotation rule respected: no two adjacent scenes share an accent.

---

## AI Image Prompts

None. The two Anthropic blog PNGs (Dreaming visualization + Sessions UI) carry the heavy visuals — the rest is hand-built type + chips + diagrams. No Imagen / Midjourney needed.

---

## Screenshot Inventory

```yaml
screenshots:
  - name: "dreaming-hero"
    url: "https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8e9ad765c7eed52dcf468_Claude-Managed-Agents-Blog-Followup-Dreaming.png"
    scene: "S03"
    color_scheme: "dark"
    usage: "Background hero illustration for Dreaming scene with our motion overlaid (sessions → memory store → curated memories)"
    download_to: "videos/claude-managed-agents-launch/assets/dreaming-hero.png"

  - name: "sessions-ui"
    url: "https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8ea208aefcf18345ee3ef_Claude-Managed-Agents-Blog-Followup-Sessions-UI.png"
    scene: "S05"
    color_scheme: "dark"
    usage: "Backdrop / context frame for the multiagent orchestration column diagram"
    download_to: "videos/claude-managed-agents-launch/assets/sessions-ui.png"
```

Both PNGs MUST be downloaded into `videos/claude-managed-agents-launch/assets/` — HyperFrames bundler/preview rejects external URLs (CLAUDE.md "shared lib copy-from" rule applies equally to external assets).

---

## HyperFrames Blocks

None. Every visual is composable from primitives (`marker-*`, `gsap-stagger-grid`, `gsap-counter-tween`, `gsap-typewriter`) + the two blog PNGs. No `hyperframes-registry` blocks needed. The Dynamous endcard in S08 is wired via the project's `videos/_template-wiring-snippet.md` artifact 2 (handled by the playbook in Phase 4 composition build, not Phase 1).

---

## Fact-Check Audit

Every concrete claim that will land on screen or in narration is sourced below. Phase 2b will re-verify all of these. **No claim ships without a source URL.**

| # | Claim | On-screen / narration | Source URL | Status |
|---|---|---|---|---|
| 1 | Dreaming = research preview (gated) | S00, S01, S02, S03 | source.md §2 lead post + thread reply 1; https://claude.com/blog/new-in-claude-managed-agents | SOURCED |
| 2 | Outcomes / Multiagent / Webhooks = public beta | S00, S01, S02, S04, S05, S06 | source.md §2 lead post; blog post | SOURCED |
| 3 | "Available today on the Claude Platform" | S08, also S02 chyron | source.md §2 thread reply 4 | SOURCED |
| 4 | Dreaming form URL: claude.com/form/claude-managed-agents | S03, S08 | source.md §2 thread reply 1 | SOURCED — Phase 2b must re-verify URL is live |
| 5 | Dreaming function: "reviews past sessions, extracts patterns, curates memories" | S03 narration | source.md §2 thread reply 1 (verbatim) | SOURCED |
| 6 | Outcomes function: "rubric → separate grader → agent iterates until quality bar met" | S04 narration | source.md §2 thread reply 2 | SOURCED |
| 7 | Outcomes lift: "+10 points task success vs standard prompting" | S04 on-screen counter | content-brief.md proof points table; blog | SOURCED |
| 8 | Multiagent function: "lead agent delegates to specialists working in parallel on complex jobs" | S05 narration | source.md §2 thread reply 3 (verbatim) | SOURCED |
| 9 | Harvey ~6× completion rate | S05 stat slam | content-brief.md proof points; blog | SOURCED |
| 10 | Netflix multiagent use (build-log analysis) | S05 column labels | content-brief.md notable adopters; blog | SOURCED |
| 11 | Webhooks = "closes the loop for real production workflows" | S06 narration / quote | source.md §3 Reaction C (anonymized — paraphrased, no handle) | SOURCED |
| 12 | Pricing $0.08/session-hour + standard token rates | S07 pricing pill | content-brief.md proof points; https://platform.claude.com/docs/en/managed-agents/overview | SOURCED — flagged in content-brief.md "Gaps" as needing Phase 2b primary-source re-verify; if unconfirmed by Phase 2b, drop the pill |
| 13 | Beta header `managed-agents-2026-04-01` | S07 code chip (typewriter) | content-brief.md proof points; platform docs | SOURCED — same Phase 2b re-verify caveat as #12; if unconfirmed, drop the chip |
| 14 | Anonymous community quote: "the orchestration layer is where the real moat lives" | S07 quote tile | source.md §3 Reaction B (paraphrased without attribution per source.md hard rule) | SOURCED |
| 15 | Anthropic announced live at "Code with Claude" event | S00/S01 chyron | source.md §2 lead post | SOURCED |
| 16 | Date: May 6, 2026 | Optional S00/S01 chyron | source.md §2 timestamp | SOURCED |
| 17 | Spoken Dynamous outro line | S08 narration | locked phrase per `feedback_dynamous_short_outro` memory rule (verbatim: "If you want to learn more about AI, check out the dynamous.ai community.") | SOURCED — locked memory |

**Claims rephrased / softened**:
- Item 9 (Harvey 6×) is shown on screen with a `vs their pre-multiagent baseline` caption beneath the digit — preempts the "vs what?" objection from content-brief.md viewer-objections.
- Items 12 and 13 are conditional — if Phase 2b cannot re-verify them at the platform docs URL primary source, both are dropped from S07 rather than risk fabrication. S07 will fall back to just the community quote tile.

**Claims removed (unsourced)**:
- None. Every speculative item from content-brief.md ("Could Include") that didn't have a clear source did not enter this plan. No "+8.4% docx / +10.1% pptx" stats, no Wisedocs 50% line — they're sourceable but lower shock factor and don't fit the 130s budget; saved as B-roll Phase 2 may pull from if needed.

**HARD constraint check (per source.md §3 + §5)**:
- ✓ NO @-handles, display names, or avatars from any community reaction enters the plan
- ✓ Reactions appear only as ambient industry sentiment (S07 quote tile, paraphrased)
- ✓ Research-preview vs public-beta distinction made visually inescapable (S02 four-pillar status row + S03 RP badge + S08 form URL CTA)
- ✓ Dynamous outro reserved for S08 — no narration stuffing in that beat

---

## Notes for Composition Build

**For whoever builds the HTML next (Phase 4 composition / `new-anthropic-short.md` playbook)**:

1. **Asset pre-fetch (mandatory)**: download both blog PNGs into `videos/claude-managed-agents-launch/assets/` BEFORE wiring any `<img>` tags — HyperFrames bundler rejects `https://...` paths at runtime. URLs in the Screenshot Inventory section above.

2. **SFX sync**: run `bash scripts/sync-video-sfx.sh videos/claude-managed-agents-launch` after seeding `sfx-cues.txt` with the cue names from the `sfx_cues:` block above (impact-slam, screen-shake, spring-pop, cinematic-whoosh, glitch-zap, strike-cross, scale-slam, pop). Don't invent files.

3. **Phase mutex pattern**: 9 phases (S00..S08) → use `#phase0..#phase8` with z-index 0..8 and `opacity: 0` defaults. Use the existing P/T crossfade convention from `templates/shorts/anthropic/index.html`. T4 is the one accent transition (`zoom-through`); all others are `blur-crossfade` (0.4s opacity + 0.5s blur).

4. **Dynamous endcard wiring**: S08 reserves 16s for the spoken outro + endcard component. Per `feedback_dynamous_short_outro` memory rule, the spoken line is locked to "If you want to learn more about AI, check out the dynamous.ai community." — do NOT extend or rephrase. Endcard visual artifacts come from `videos/_template-wiring-snippet.md` (Step 0 onward). Update `meta.json` with `"dynamousPromotion": true`.

5. **Step-by-step reveal pattern (REQUIRED for S02)**: 4 pillars at +0/+3.5s/+7s/+10.5s. Use the explicit `tl.set()` at t=0 + `tl.to()` at reveal time pattern from `.claude/rules/step-by-step-reveal.md` — NOT `tl.from()`. Each pillar must be invisible from frame 0 until its reveal beat fires. Same pattern for S03's session cards, S04's rubric items, S05's specialist columns (though S05 uses a quick stagger because narration says "parallel specialists" once — that's the stated exception in the rule).

6. **Shape backdrop rearrangement**: per `feedback_shape_rearrange_on_whoosh_default` memory rule — `#shape-backdrop` rearranges on every phase transition (cinematic-whoosh moment). Default behavior; no extra wiring needed if using the standard template's shape system.

7. **Visual pacing audit before lint**: every scene above respects the 5s rule per the audit in the Data Timing Budget section. If Phase 3.5 retimes anchors against transcript and a gap stretches past 5s, insert a beat (marker sweep, sub-line entrance, or content morph) per `.claude/rules/visual-pacing-5s.md`. Do not let any scene drift static.

8. **Logo path**: when copied to `videos/claude-managed-agents-launch/`, the Anthropic wordmark path becomes `../../shared/logos/anthropic-logo-light.svg` (one less `../` than the template's path).

9. **Source-fidelity at Phase 2b**: the head-noun gate already passed for variant_a in this plan (`Claude agents` ↔ `Claude Managed Agents` is shorthand, not substitution). Phase 2b should still re-check every digit + named-entity in the script before TTS. Specifically, do NOT let "managed-agents-2026-04-01" be read aloud (per content-brief.md TTS pronunciation table — date string, screen-only).

10. **No background music** — narration + SFX only (template constraint, DESIGN.md "What NOT to Do" #6).
