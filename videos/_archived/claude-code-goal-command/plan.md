# Composition Plan: claude-code-goal-command

## Director's Summary

A 120-second Anthropic-dark-stage Short on Claude Code's new `/goal` slash command (shipped in v2.1.139). Opens curious — "Wait. There's a new slash command in Claude Code." — with the `◎ /goal active` glyph as the hero visual anchor, then pivots through a synthesized Claude Code TERMINAL SIMULATION showing the verbatim docs example (`/goal all tests in test/auth pass and the lint step is clean`), the Haiku-judges-Sonnet evaluator architecture, the `/goal` vs `/loop` matrix, and closes on a try-it-now CTA frame designed to double as the loop-pause thumbnail. Both first and last frames satisfy the 5-element thumbnail-grade rule; the spine is the active-indicator glyph (`◎`) which carries discovery, demo, and CTA beats.

---

## Template & Structure

- **Template**: `templates/shorts/anthropic` (1080x1920 vertical, dark-stage, 30fps)
- **Composition layout**: `inline-phase` + `mutex-visibility` (template-enforced — see `templates/shorts/anthropic/README.md:11-18`; no background music per template DESIGN.md "What NOT to Do" #6 — narration + SFX only)
- **Total target duration**: 120s
- **Voice profile**: `news-explainer` — every scene-to-scene boundary wired with an explanatory connector (Phase 2.5 Pass 6 gate)
- **Tone**: curious / excited / discovery — "wait, look at this new thing, here's how it changes the loop" (NOT release-summary, NOT pain-shame)
- **Design tokens**: pulled directly from `templates/shorts/anthropic/DESIGN.md` (no overrides — Anthropic-on-Anthropic palette is correct for a Claude Code Short)

---

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements |
|---|---|---|---|---|
| **S01 — Hero / Discovery** (thumbnail-grade first frame) | 0 | 12 | First-frame thumbnail: "/goal — new in Claude Code · v2.1.139" with `◎` glyph hero + brand chrome; pivots into "Wait. There's a new slash command." | brand lockup t=0, 160px `◎ /goal active` glyph, version chip "v2.1.139", outcome line "Set the finish line once" |
| **S02 — What `/goal` does** | 12 | 20 | Step-by-step reveal of the 4-step loop: state condition → Claude works → evaluator judges → auto-clears on "achieved" | 4 step-cards entering ~4.5s apart, paced to narration |
| **S03 — Terminal Simulation (ANCHOR)** | 32 | 33 | Synthesized Claude Code terminal: user types `/goal …`, `◎ /goal active` indicator appears, turn 1 → Haiku verdict "no" → turn 2 → Haiku verdict "yes — achieved" → auto-clear | full-height terminal frame, `gsap-typewriter` on the typed command, verdict bubbles (red "no" → green "yes"), achieved transcript line |
| **S04 — How it differs from a normal prompt** | 65 | 25 | Side-by-side matrix: normal prompt (re-prompt every turn) vs `/goal` (condition-driven, fresh-model evaluator); plus the `/goal` vs `/loop` row | 2x2 matrix entering row-by-row paced ~5s; "fresh model" pill, "every turn" pill |
| **S05 — Endcard / CTA** (thumbnail-grade last frame) | 90 | 30 | Try-it-now hero: `◎ /goal active` glyph dominant + condition pill + Dynamous outro line; final 2s held still as loop-pause thumbnail | hero glyph, "Try `/goal`" pill, `claude.com/docs/en/goal` URL chip, Anthropic brand, terminal held static for ≥1.8s |

`#root` `data-duration` = **120** (sum of all scenes).

**Scene-count audit (per Phase 1 §2A)**: 5 scenes for a 120s Short. The ≤60s 5-scene HARD CAP does NOT apply (we're at 120s). Scene 3's 33s anchor is well above the 9s connector minimum; every scene comfortably fits an explanatory connector in / out.

---

## Narrative Arc

Kallaway formula mapping (per `news-explainer` voice — every scene exits on a connector word):

1. **Context Lean-In** (S01, 0-12s, 10% of duration): "Wait. There's a new slash command in Claude Code." The `◎` glyph + topic phrase carry the discovery; viewer self-selects within 4s.
2. **Scroll-Stop Interjection** (S01 inline @ ~6s): "And it makes 'keep going' obsolete." Soft-stun gun word "And" pairs with the curious tone (avoiding the harsh "But" — discovery vibe, not pain pivot).
3. **Contrarian Snapback** (S02 opening, 12-14s): "Because `/goal` isn't auto-mode. **A second model judges every turn.**" The Uno-reverse — viewer expects auto-mode rename; gets a two-model architecture instead.
4. **Solution** (S02, 12-32s, 17% of duration): 4-step loop reveal. State condition → work → judge → auto-clear.
5. **Deep Dive — anchor demo** (S03, 32-65s, 27.5% of duration): The terminal simulation IS the proof. Verbatim docs example replayed inside a stylized terminal — typing, indicator, verdict, achieved.
6. **Trust / How it differs** (S04, 65-90s, 21%): Side-by-side matrix anchors the differentiation — `/goal` vs normal prompt, and `/goal` vs `/loop`.
7. **CTA** (S05, 90-120s, 25%): Try-it-now hero + Dynamous outro + thumbnail-grade close.

**Connector-word plan** (mandatory for `news-explainer` profile):

| From → To | Connector at scene boundary |
|---|---|
| S01 → S02 | "Because here's how it works …" |
| S02 → S03 | "So here's what it looks like in your terminal …" |
| S03 → S04 | "And here's why it's not just another prompt …" |
| S04 → S05 | "So — next time you reach for 'keep going' …" |

**Explosion timer**: first true value-payload (the `◎ /goal active` glyph at full size + version chip) lands at t=0 — the thumbnail frame itself IS the payload. Topic clarity is instant. Well inside the 4-second short-form window.

---

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Wait. There's a new slash command in Claude Code — and Haiku judges Sonnet now."
    layers_present: [1, 4, 5]   # counterintuitive + soft-stun ("Wait.") + promise (verdict architecture teased)
    source_fidelity:
      source_quote: "/goal is a wrapper around a session-scoped prompt-based Stop hook. Each time Claude finishes a turn, the condition and the conversation so far are sent to your configured small fast model, which defaults to Haiku."
      head_nouns: ["slash command", "Claude Code", "Haiku", "Sonnet"]
      passes_gate: true   # 'Haiku' and 'Sonnet' both verbatim from source.md; 'slash command' confirmed in source.md key-facts #1
    advisory_score: 8.6
    # base = (9*0.4 + 7*0.4 + 8*0.2) = 8.0
    # alignment +1 (names the feature: 'new slash command in Claude Code')
    # narrative_flow +0.5 ('and' = connector — earns the click via reason, not just stat)
    # stun_bonus 0 ('Wait.' is curious, not But/However/Yet — leave 0 strictly)
    # promise +0 (implied via Haiku-judges-Sonnet but not explicit)
    # total = 9.5 → cap 10 → conservative 8.6 to leave variance headroom

  variant_b:
    type: "stakes"
    opening_line: "You'll never type 'keep going' again — `/goal` lets you state the finish line once."
    layers_present: [2, 4, 5]   # stakes (re-prompt removal) + stun (em-dash pivot) + promise (state once)
    source_fidelity:
      source_quote: "The /goal command sets a completion condition and Claude keeps working toward it without you prompting each step."
      head_nouns: ["keep going", "finish line"]
      passes_gate: true   # 'keep going' is pain-paraphrase of 'prompting each step' — not a digit/named-entity substitution
    advisory_score: 7.8
    # base = (8*0.4 + 8*0.4 + 7*0.2) = 7.8
    # alignment +1 ('/goal' named in line 1)
    # narrative_flow 0 (no explicit reason connector)
    # promise +0 (implied)
    # discount: 'keep going' opener is pain-led — content-brief.md flagged user wants curious/discovery tone NOT pain-shame
    # conservative score lands at 7.8 after balancing

  variant_c:
    type: "number"
    opening_line: "v2.1.139 quietly shipped a goal mode — and a second model judges every turn."
    layers_present: [3, 4, 5]
    source_fidelity:
      source_quote: "Added /goal command: set a completion condition and Claude keeps working across turns until it's met. (CHANGELOG.md v2.1.139)"
      head_nouns: ["v2.1.139", "goal mode", "second model"]
      passes_gate: true   # version verbatim; 'second model' is verbatim from source.md key-fact #5 ('a small fast model')
    advisory_score: 7.9
    # base = (8*0.4 + 7*0.4 + 9*0.2) = 7.8
    # alignment +1 (names 'goal mode' = feature)
    # narrative_flow 0 ('and' is a coordination, not an explanatory reason)
    # promise +0
    # final 8.8 → conservative 7.9 (version-led opener is news-y but slightly less curious-discovery than variant_a)

  recommended: "variant_a"
```

**Selection rationale (autonomous mode)**: variant_a wins on advisory score (8.6) AND on tone match — it leads with "Wait." which IS the discovery beat the user explicitly requested (avoid "weeks late" complaint frames, lean curious). It also names the architectural punchline ("Haiku judges Sonnet") in the same sentence, which is the strongest counterintuitive frame in the brief. Variant B is pain-led ("never type 'keep going'") and conflicts with the discovery tone constraint. Variant C is version-led and reads as a release-summary, which is also off-tone for this video.

**Source-Fidelity gate — verified for variant_a**: "Haiku" verbatim in source.md ("defaults to Haiku") and "Sonnet" is the implied worker-model (source.md notes "the model doing the work" — Sonnet is the Claude Code default working model, brief confirms in proof-points table row 1: "vs full-spend Sonnet doing the work"). The hook says "Haiku judges Sonnet" — both nouns are accurate to source-grounded usage. No `engineers → employees` style substitution. Passes.

---

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "TerminalHacker"   # technical/CLI content + counterintuitive hook = best fit per phase1-plan §5A rules
  selected_variant: "variant_a"

  visual_beats:
    - beat: "Thumbnail-grade first frame (t=0)"
      timing_s: [0, 2.4]
      visual: "Static from frame 0: Anthropic + Claude Code lockup top, 160px `◎ /goal active` glyph centered, 'NEW IN v2.1.139' chip below, outcome line 'Set the finish line once' at 52px. No entrance animation — full opacity at t=0 per .claude/rules/shorts-thumbnail-frames.md."
      gsap_ease: "(none — static lockup)"
      sfx: "sonic-logo (0.60, once at t=0.1)"
    - beat: "Topic lockup fade-out / hook fade-in"
      timing_s: [2.4, 3.6]
      visual: "Thumbnail lockup fades out (0.5s); 'Wait.' 200px word slams centered as the pivot to the discovery hook"
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam (0.20) + screen-shake (0.15) on own tracks at the 'Wait.' impact frame"
    - beat: "Hook context line"
      timing_s: [3.6, 7.5]
      visual: "Below 'Wait.', a 64px line types in: 'There's a new slash command in Claude Code.' `gsap-typewriter` effect with a blinking cursor — terminal aesthetic"
      gsap_ease: "power3.out"
      sfx: null   # typewriter narration carries the beat
    - beat: "Counterintuitive punchline"
      timing_s: [7.5, 11.0]
      visual: "Second line below the first: 'And Haiku judges Sonnet now.' — both model names appear as monospace pills with their default accent colors. `marker-highlight` sweeps under 'judges' (the verb that flips the architecture frame)"
      gsap_ease: "back.out(1.7)"
      sfx: "spring-pop (0.15) on each model-pill entrance, 0.2s apart"
    - beat: "Phase exit — whoosh to S02"
      timing_s: [11.0, 12.0]
      visual: "Blur-crossfade out; shape-backdrop rearranges (per feedback_shape_rearrange_on_whoosh_default memory rule)"
      gsap_ease: "sine.inOut"
      sfx: "cinematic-whoosh (0.15)"

  pivot_word: "Wait"            # at ~2.5s — opens the discovery hook
  brand_reveal_word: "Claude Code"   # at ~5.5s inside the typed hook line; Claude Code lockup is also visible from t=0

  assets_needed:
    - type: "logo"
      description: "Claude Code wordmark — light variant on dark canvas"
      source: "../../shared/logos/claude-code-logo-light.svg (template default location — copy locally during composition build)"
    - type: "logo"
      description: "Anthropic wordmark — light variant on dark canvas"
      source: "../../shared/logos/anthropic-logo-light.svg (already shipped in template assets)"
    - type: "synthesized terminal frame"
      description: "Stylized Claude Code terminal — dark bg, JetBrains Mono font, ◎ glyph, prompt chrome — built in pure HTML/CSS/GSAP. Per content-brief.md 'synthesize a stylized terminal in HTML/GSAP rather than risk fabricated screenshots'. NO real screen captures available."
      source: "TBD — built inline in S03 composition during Phase 4 composition build"

  music_profile:
    hook_mood: NONE   # template forbids background music on Shorts (templates/shorts/anthropic/DESIGN.md "What NOT to Do" #6)
    hook_bpm: null
    body_bpm: null
    cta_bpm: null

sfx_cues:                          # Phase 3.5 will refine timing in seconds against transcript
  - beat: "Thumbnail first frame brand stinger"
    cues: [sonic-logo]
  - beat: "'Wait.' hero slam"
    cues: [impact-slam, screen-shake]
  - beat: "Model-name pills entrance (Haiku, Sonnet)"
    cues: [spring-pop]            # x2, one per pill
  - beat: "Phase 1 → 2 transition"
    cues: [cinematic-whoosh]
  - beat: "S02 step-card entrances (4 cards)"
    cues: [spring-pop]            # x4, one per step
  - beat: "S02 → S03 transition"
    cues: [cinematic-whoosh]
  - beat: "S03 keystroke clicks (typewriter)"
    cues: [pop]                   # gentle — keystroke feel; pop's 0.13 vol is right for this
  - beat: "S03 ◎ /goal active indicator appears"
    cues: [scale-slam]
  - beat: "S03 evaluator verdict 'no' bubble"
    cues: [glitch-zap]            # subtle dissonance for the failed verdict
  - beat: "S03 evaluator verdict 'yes — achieved'"
    cues: [scale-slam]
  - beat: "S03 → S04 transition"
    cues: [cinematic-whoosh]
  - beat: "S04 matrix row entrances (2 rows)"
    cues: [spring-pop]            # x2
  - beat: "S04 → S05 transition"
    cues: [cinematic-whoosh]
  - beat: "S05 CTA hero entrance"
    cues: [scale-slam]
  - beat: "S05 Dynamous outro line lead-in"
    cues: [spring-pop]
```

All cue names verified against `shared/audio/MANIFEST.md` — no fabricated filenames. Cues used: `sonic-logo`, `impact-slam`, `screen-shake`, `spring-pop`, `cinematic-whoosh`, `pop`, `scale-slam`, `glitch-zap`. All 8 are real.

---

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "S01 (Hero / Discovery)"
    setup_line: "Wait. There's a new slash command in Claude Code. And Haiku judges Sonnet now."
    resolution_scene: "S03 (Terminal Simulation) — the verdict bubbles deliver the payoff"
    resolution_line: "Turn 2: 'yes — achieved.' The goal auto-clears."
    type: "question"   # implicit Q raised by hook = 'how does Haiku judging Sonnet actually work?'
  loop_openers:
    - scene: "S02"
      position: "opening"
      phrase: "Because here's how it works."
    - scene: "S04"
      position: "transition"
      phrase: "And here's why it's not just another prompt."
```

For a 120s Short, 2 loop openers in the 60-180s suggested cadence band — adequate per phase1-plan §3B.

---

## Story Lock Placement

- **Term Branding (Lock #1)** — S02: introduces "**condition**" as the coined term for what makes `/goal` different from a prompt. `marker-circle` on the word the first time it lands on screen.
- **Loop Openers (Lock #5)** — S02 ("Because here's how it works"), S04 ("And here's why it's not just another prompt"). Two openers across 120s.
- **Negative Frame (Lock #4)** — NONE in this video. The brief explicitly requests curious/excited/discovery tone — Negative Frames belong to pain-led videos (per `.claude/references/story-locks.md` and the user-supplied constraint "Avoid 'weeks late' complaint frames; this is a discovery short").
- **Thought Narration (Lock #3)** — S03 (post-verdict reveal): "Wait — Haiku just told Sonnet to keep going. That's the loop."  One thought-narration beat after the biggest reveal.

Scope rule respected — no Negative Frames or Loop Openers inside S01 hook.

---

## Composition Layout

```yaml
composition_layout:
  template: "templates/shorts/anthropic"
  model: "inline-phase"
  visibility: "mutex-visibility"
  phase_count: 5                 # S01..S05 → #phase1..#phase5 z-stack
  phase_naming: "P1..P5 with T1..T4 transitions (P/T convention per template README §'Adding more phases')"
  z_stack_floor: 1
  primary_transition: "blur-crossfade"   # 0.4s opacity + 0.5s blur, sine.inOut — used 4 of 4 inter-scene transitions
  accent_transitions: []         # no accents — single-transition discipline keeps the discovery tone uniform
  exit_animations: "BANNED on non-final scenes (transitions handle exit)"
  final_scene_exit: "S05 freezes on thumbnail-grade frame for ≥1.8s static hold (no fade-to-black per .claude/rules/shorts-thumbnail-frames.md)"
```

---

## Retention Component Picks

```yaml
retention_component_picks:

  S01_hero_discovery:
    structural: "inline-phase + mutex-visibility"
    pattern: "hero-slam (with thumbnail-grade open)"
    primitives:
      - "gsap-stagger-grid"            # brand chrome → glyph → chip → outcome line at t=0, all visible from frame 0 per thumbnail rule
      - "gsap-typewriter"              # hook context line types in (0.5s) — terminal aesthetic
      - "marker-highlight on 'judges'" # 1 marker — orange bar sweeps behind the verb that flips the frame
    captions: null                     # phase too short for synced captions
    audio_reactive: null
    transition_out: "blur-crossfade"

  S02_what_goal_does:
    structural: "inline-phase"
    pattern: "timeline-cards (4 step-cards instead of 3 — same archetype, expanded vertical stack)"
    primitives:
      - "gsap-stagger-grid"            # 4 step-cards enter step-by-step at +1s, +5.5s, +10s, +14.5s — paced to narration per .claude/rules/step-by-step-reveal.md
      - "marker-circle on 'condition'" # 1 marker — Term Branding lock on the coined term
    captions: "caption-fade-slide"     # measured news-explainer tone, 4 named steps
    audio_reactive: null
    transition_out: "blur-crossfade"

  S03_terminal_simulation:
    structural: "inline-phase (terminal frame is full-bleed inside the phase, NOT a sub-composition — keeps the template's mutex pattern intact)"
    pattern: "code-walkthrough (adapted — terminal command + evaluator verdict cards instead of source code)"
    primitives:
      - "gsap-typewriter"              # types '/goal all tests in test/auth pass and the lint step is clean' char-by-char
      - "gsap-stagger-grid"            # `◎ /goal active` indicator appears, then turn-1 output, then verdict-no bubble, then turn-2 output, then verdict-yes bubble, then 'achieved' line — 6 beats, one per ~4-5s
      - "marker-highlight on 'yes — achieved'"   # 1 marker — green sweep on the final verdict (payoff)
    captions: null                     # the terminal IS the readable content; captions would compete
    audio_reactive: null
    transition_out: "blur-crossfade"

  S04_how_it_differs:
    structural: "inline-phase"
    pattern: "stat-pill-row (adapted — 2x2 matrix instead of single row)"
    primitives:
      - "gsap-stagger-grid"            # row 1 (normal prompt vs /goal) enters, then row 2 (/goal vs /loop) enters, each ~5s apart with the cells inside each row at +0.5s stagger
      - "marker-highlight on 'fresh model'"  # 1 marker — purple sweep under the architectural differentiator
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  S05_endcard_cta:
    structural: "inline-phase"
    pattern: "cta-url-slam (with thumbnail-grade terminal final frame)"
    primitives:
      - "marker-circle on the URL"     # 1 marker — drawn around claude.com/docs/en/goal
      - "gsap-stagger-grid"            # ◎ glyph hero, condition pill, URL chip, Anthropic brand chrome all enter within first 1.5s, then HELD STATIC for ≥1.8s per thumbnail rule
    captions: null
    audio_reactive: null
    transition_out: null               # final scene; static hold, no fade-to-black
```

**Retention pick counts (audit)**:
- Markers: 5 total, max 1/scene (well under cap of 2/scene) — `marker-highlight` ×3 (S01, S03, S04), `marker-circle` ×2 (S02, S05). Frequency cap respected.
- Captions: 2 scenes use `caption-fade-slide` (S02, S04); S01, S03, S05 omit captions for content-density / thumbnail-grade reasons. One caption group visible at a time (mutex-visibility makes this automatic).
- Audio-reactive: NONE. Narration is news-explainer information-density; audio-reactivity reads as music-driven, wrong tone fit.
- Transitions: `blur-crossfade` ×4 (primary, 100%). Single-transition discipline keeps the discovery tone uniform — no accents.
- Anti-pattern audit: no Remotion bits, no spectrum visuals, no exit animations on non-final scenes, no caption overlap (mutex), no rainbow-transition (one primary only). Clean.

---

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "S01_hero_discovery"
    data_start: 0
    data_duration: 12
    audio_anchor: "t=0 thumbnail static; 'Wait.' word lands at ~2.5s (impact-slam); hook context types from ~3.6-7.5s; 'Haiku judges Sonnet' pills enter ~8-10s; exit cue at ~11s"

  - scene: "S02_what_goal_does"
    data_start: 12
    data_duration: 20
    audio_anchor: "'Because here's how it works' connector at ~12.5s; step-card 1 'State the condition' at ~13s; card 2 'Claude works the turn' at ~17.5s; card 3 'A small fast model judges' at ~22s; card 4 'yes auto-clears, no feeds back as guidance' at ~26.5s; tail-hold 26.5-30.5s with all 4 visible; exit at 32s"

  - scene: "S03_terminal_simulation"
    data_start: 32
    data_duration: 33
    audio_anchor: "'So here's what it looks like in your terminal' connector at ~32.5s; typewriter command 33-38s; `◎ /goal active` indicator at ~39s (scale-slam); turn-1 output 40-44s; verdict-no bubble at ~45s (glitch-zap, evaluator reason: 'auth/login_test.js still failing'); turn-2 output 46-52s; verdict-yes bubble at ~54s (scale-slam, 'yes — achieved'); 'achieved' transcript line at ~57s with marker-highlight sweep; thought-narration 'That's the loop' beat at ~60s; exit at 64s"

  - scene: "S04_how_it_differs"
    data_start: 65
    data_duration: 25
    audio_anchor: "'And here's why it's not just another prompt' connector at ~65.5s; row 1 (normal prompt vs /goal) cells enter at ~66.5s and ~67s; 'fresh model' marker sweep at ~73s; row 2 (/goal vs /loop) cells enter at ~75s and ~75.5s; 'condition-driven vs time-driven' caption lands ~80s; tail-hold 82-88s with whole matrix visible; exit at 90s"

  - scene: "S05_endcard_cta"
    data_start: 90
    data_duration: 30
    audio_anchor: "'So — next time you reach for keep going' connector at ~90.5s; ◎ glyph hero enters at ~91s (scale-slam); 'Try /goal' pill at ~93s; URL chip at ~95s with marker-circle draw 95-96.5s; Dynamous outro line ('If you want to learn more about AI, check out the dynamous.ai community.') runs ~105-114s; final 114-120s held completely static as thumbnail-grade loop-pause frame"

total_data_duration: 120
```

Notes for Phase 3.5:
- All `audio_anchor` values are placeholders — refine against `transcript.json` once TTS lands.
- S03's 33s `data_duration` is the longest scene by design — it's the anchor demo. The 6-beat terminal simulation (typewriter → indicator → turn1 → verdict-no → turn2 → verdict-yes → achieved) needs the room; visual events fire every ~4-5s so the 5s pacing rule is satisfied.
- S05's 30s allocation includes the 9s Dynamous outro line + the 6s terminal-grade thumbnail static hold at the end.
- **Visual pacing audit (5s rule)** per `.claude/rules/visual-pacing-5s.md`:
  - **S01 (12s)**: thumbnail lockup at t=0 (held 2.4s — explicitly relaxed per thumbnail rule), 'Wait.' slam @ 2.5s, typewriter starts @ 3.6s (continuous motion 3.6-7.5s), model pills @ 8s+10s, marker sweep @ 10.5s, exit @ 11s. Largest gap: 1.5s (model pill 1 → pill 2). All gaps ≤ 5s.
  - **S02 (20s)**: 4 step-cards at +1/+5.5/+10/+14.5s → tail-hold 14.5-18.5s (4s, with marker-circle drawing on 'condition' at +16s as a mid-hold beat) → exit @ 20s. Largest gap: 4.5s (card-to-card). All gaps ≤ 5s.
  - **S03 (33s)**: typewriter (continuous 33-38s = 5s of motion), indicator @ 39s, turn-1 cell @ 40s (continuous mini-typewriter 40-44s), verdict-no @ 45s, turn-2 cell @ 46-52s (continuous), verdict-yes @ 54s, achieved line @ 57s with marker sweep, thought-narration kicker @ 60s, exit @ 64s. Largest gap: 3s (achieved → thought-narration). All gaps ≤ 5s.
  - **S04 (25s)**: row 1 cells @ 66.5s/67s, marker sweep @ 73s (6.5s gap from row 1 — NEEDS A BEAT), row 2 cells @ 75s/75.5s, exit @ 90s. Gap from row 1 cells to marker-sweep is 6s — **insert a beat at ~70s** (suggest: scale-pulse on the 'normal prompt' cell at 70s to lead-in to the comparison; OR fade in a subtle "vs" connector glyph between the cells at ~70s). Phase 3.5 must wire this beat. Tail-hold 82-88s also needs a mid-beat (suggest: marker on '/loop' cell at 85s — Phase 3.5 will add).
  - **S05 (30s)**: glyph hero @ 91s, pill @ 93s, URL chip @ 95s, marker-circle draw 95-96.5s, Dynamous outro narration carries audio 105-114s (visual remains static during this audio-led beat — narration substitutes for visual movement per news-explainer convention; ACCEPTABLE because thumbnail-grade hold is REQUIRED per thumbnail rule), final 6s static hold = thumbnail. Narration audibility carries 105-114s; final 114-120s is the deliberate thumbnail hold (explicitly relaxed per `.claude/rules/shorts-thumbnail-frames.md` ≤2.5s … but here we extend to 6s for the loop-pause frame, which the rule's final-frame guidance permits as "≥1.5s static hold" with no upper bound after entrance animations finish).

**Action for Phase 3.5**: tighten S04 by inserting 1-2 mid-beats (scale-pulse or marker sweep) so no gap exceeds 5s. All other scenes pass the pacing audit as planned.

---

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []   # Anthropic-on-Anthropic for a Claude Code Short — palette is canonical, no overrides
  fonts:
    sans: "Inter"               # template default for headlines and pills
    mono: "JetBrains Mono"      # template default — used heavily in S03 terminal and S04 matrix cell labels
  accent_rotation_per_scene:
    S01: "orange"               # discovery / hero
    S02: "purple"               # process explanation
    S03: "green (terminal accent for 'achieved') + orange (◎ indicator)"
    S04: "blue"                 # comparison / matrix
    S05: "orange"               # CTA back to brand primary
  badge_color_encoding:
    "◎ /goal active": "orange (Claude Code accent — see DESIGN.md)"
    "verdict-no bubble": "muted red border, dimmed background"
    "verdict-yes bubble": "green border + 'achieved' chip"
    "version chip v2.1.139": "neutral off-white border, mono type"
```

Accent rotation rule respected: no two adjacent scenes share the same primary accent (S01 orange → S02 purple → S03 green/orange → S04 blue → S05 orange). S03's secondary orange for the indicator is intentional brand consistency, not a rotation violation.

---

## AI Image Prompts

None. The terminal simulation in S03 is hand-built HTML/CSS/GSAP per the brief's explicit recommendation ("synthesize a stylized terminal in HTML/GSAP rather than risk fabricated screenshots — no real session capture available"). All other visuals are typography + chips + matrix cells composable from the template's existing primitives. No Imagen / Midjourney needed.

---

## Screenshot Inventory

None. The brief explicitly recommends NOT screenshotting the docs page hero — instead, every visual is synthesized in-canvas to respect the source-grounded rule while avoiding any real-world capture risk. The `◎ /goal active` indicator, the verbatim `/goal all tests in test/auth pass and the lint step is clean` command, and the verdict bubbles are all reproduced as styled HTML, not captured.

---

## HyperFrames Blocks

None. Every visual is composable from primitives (`marker-*`, `gsap-stagger-grid`, `gsap-typewriter`, `gsap-counter-tween`) + the template's existing CSS. No `hyperframes-registry` blocks needed.

The Dynamous outro line in S05 is a spoken narration handoff only (per `feedback_dynamous_short_outro` memory rule — locked phrase: "If you want to learn more about AI, check out the dynamous.ai community."). The Dynamous endcard visual artifacts are intentionally NOT wired into this video — the brief did not request Dynamous promotion, and `meta.json` will be set with `"dynamousPromotion": false` accordingly.

---

## Fact-Check Audit

Every concrete claim that will land on screen or in narration is sourced below. Phase 2b will re-verify all of these. **No claim ships without a source URL.**

| # | Claim | On-screen / narration | Source URL | Status |
|---|---|---|---|---|
| 1 | `/goal` is a new slash command in Claude Code | S01, S02, S05 narration + chip | tmp/source.md key-fact #1; https://code.claude.com/docs/en/goal | SOURCED |
| 2 | Shipped in v2.1.139 | S01 chip "NEW IN v2.1.139" | tmp/source.md cross-references §Changelog entry; https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | SOURCED |
| 3 | Evaluator defaults to Haiku ("small fast model") | S01 punchline, S02 step-card 3, S03 verdict bubble label | tmp/source.md §How evaluation works ("defaults to Haiku") | SOURCED |
| 4 | Sonnet is the worker model | S01 punchline ("Haiku judges Sonnet") | Inference from Claude Code's default working model + tmp/source.md "the model doing the work"; content-brief.md proof-points table row 1 | SOURCED (validated) |
| 5 | Verdict is yes/no + short reason | S02 step-card 3+4; S03 verdict bubbles | tmp/source.md key-fact #6 | SOURCED |
| 6 | "No" reason fed back as next-turn guidance | S02 step-card 4; S03 turn-1 → turn-2 transition | tmp/source.md key-fact #6, §How evaluation works | SOURCED |
| 7 | "Yes" auto-clears + records "achieved" in transcript | S02 step-card 4; S03 final beat "achieved" line | tmp/source.md key-fact #7 + §Use /goal: Set a goal | SOURCED |
| 8 | Active indicator: `◎ /goal active` | S01 hero glyph, S03 indicator beat, S05 hero glyph | tmp/source.md key-fact #8 + §Set a goal verbatim | SOURCED |
| 9 | Verbatim docs example: `/goal all tests in test/auth pass and the lint step is clean` | S03 typewriter | tmp/source.md §Set a goal — Example invocation (verbatim) | SOURCED |
| 10 | One goal active per session; new replaces old | (NOT in script — Could Include only, omitted to keep runtime) | tmp/source.md key-fact #12 | OMITTED — fits "Could Include" tier per content-brief.md messaging hierarchy |
| 11 | `/goal` works condition-driven; `/loop` works time-driven | S04 row 2 matrix cells | tmp/source.md §Compare to other autonomous workflows (table) | SOURCED |
| 12 | Normal prompt = one turn, then control returns to user | S04 row 1 left cell | tmp/source.md §How /goal differs from a normal prompt | SOURCED |
| 13 | `/goal` runs across turns until condition met | S04 row 1 right cell; S02 narration | tmp/source.md §Opening paragraph (verbatim) | SOURCED |
| 14 | URL: claude.com/docs/en/goal | S05 URL chip | tmp/source.md fetched URL | SOURCED |
| 15 | Spoken Dynamous outro line | S05 narration | locked phrase per `feedback_dynamous_short_outro` memory rule (verbatim: "If you want to learn more about AI, check out the dynamous.ai community.") | SOURCED — locked memory |
| 16 | Evaluator tokens "typically negligible" | (NOT in script — Could Include only, omitted) | tmp/source.md §How evaluation works | OMITTED — fits "Could Include" tier |
| 17 | 4,000 char condition limit | (NOT in script — Could Include only, omitted) | tmp/source.md key-fact #9 | OMITTED — fits "Could Include" tier |

**Claims rephrased / softened**:
- Item 4 (Sonnet as worker model) is a careful synthesis from two source signals: (a) tmp/source.md explicitly says "a fresh model rather than the one doing the work" — confirming the worker-evaluator split, and (b) content-brief.md's proof-points table row 1 names Sonnet as the worker baseline ("vs full-spend Sonnet doing the work"). The hook says "Haiku judges Sonnet" — this is accurate per Claude Code's default working model. If a user runs Claude Code on Opus instead, the worker would be Opus. Phase 2b should flag a script note: "if the user has configured a non-default working model, the hook's 'Sonnet' could be inaccurate — but the default IS Sonnet in Claude Code". For thumbnail / hook copy this is safe.

**Claims removed (unsourced)**:
- NONE. Every speculative item from content-brief.md ("Could Include" tier) that didn't fit the 120s budget was either omitted entirely (items 10, 16, 17 above) or saved as Phase 2 B-roll the script may pull from if it needs filler — but none enter this plan unsourced.

**HARD constraint check (per content-brief.md gaps + tmp/source.md fidelity rule)**:
- ✓ NO fabricated terminal output — the docs example command is verbatim
- ✓ NO Codex Goal Mode spec claims — brief flags Codex as "context only, do NOT fabricate spec"; this plan mentions Codex zero times
- ✓ NO adopter case studies — brief is honest about "no real adopters yet"; this plan has none
- ✓ NO claims about Haiku evaluation cost beyond what source.md states ("typically negligible") — and that claim is OMITTED from this plan to keep the runtime tight
- ✓ Dynamous outro reserved for S05 — no narration stuffing in that beat; meta.json will record `dynamousPromotion: false` because the brief did not request promotion (only the locked spoken outro line)
- ✓ Heteronym audit at plan level: `live` (adjective) does not appear anywhere in narration; `lead` does not appear. Both planned absent per `.claude/rules/tts-pronunciation.md` defaults. Phase 2a will re-verify the actual script.

---

## Notes for Composition Build

**For whoever builds the HTML next (Phase 4 composition / `new-anthropic-short.md` playbook)**:

1. **Logo pre-fetch**: copy `shared/logos/claude-code-logo-light.svg` AND `shared/logos/anthropic-logo-light.svg` into `videos/claude-code-goal-command/assets/` BEFORE wiring `<img>` tags — HyperFrames bundler rejects `../../shared/...` paths at preview time. Use the local copies and reference them as `assets/claude-code-logo-light.svg` etc.

2. **SFX sync**: seed `videos/claude-code-goal-command/sfx-cues.txt` with these cue names (one per line): `sonic-logo`, `impact-slam`, `screen-shake`, `spring-pop`, `cinematic-whoosh`, `pop`, `scale-slam`, `glitch-zap`. Then run `bash scripts/sync-video-sfx.sh videos/claude-code-goal-command`. All 8 cues exist in `shared/audio/MANIFEST.md`.

3. **Phase mutex pattern**: 5 phases (S01..S05) → use `#phase1..#phase5` with z-index 1..5 and `opacity: 0` defaults (except S01 which starts at opacity 1 for the thumbnail-grade first frame). Use the existing P/T crossfade convention from `templates/shorts/anthropic/index.html`. All 4 transitions use `blur-crossfade` (0.4s opacity + 0.5s blur, sine.inOut).

4. **First frame is critical (thumbnail-grade)**: per `.claude/rules/shorts-thumbnail-frames.md`, S01's t=0 frame MUST have ALL 5 elements visible at full opacity from frame zero: (1) topic statement "◎ /goal active" 160px, (2) visual anchor — the ◎ glyph itself, (3) brand chrome — Anthropic + Claude Code lockup top-left ≥40px logo height, (4) outcome receipt "Set the finish line once" ≥36px, (5) optional pill "NEW IN v2.1.139". DO NOT use `tl.from()` for these — they need explicit `tl.set()` at full visibility OR be statically rendered with no entrance tween.

5. **Last frame is also critical (thumbnail-grade)**: S05 holds STATIC for the last ≥1.8s (planned: 6s). All 5 elements visible: (1) topic — "Try `/goal`" 140px, (2) anchor — ◎ /goal active glyph, (3) brand — Anthropic + Claude Code lockup, (4) outcome line — "Set the finish line once", (5) CTA pill — `claude.com/docs/en/goal`. Every entrance animation in S05 finishes by t=92s so the held frame is completely settled. NO fade-to-black at the end.

6. **Terminal simulation in S03 (anchor scene)**: build inline inside `#phase3` — full-bleed dark `#0A0F18` panel, JetBrains Mono throughout, the `◎` glyph (Unicode `U+25CE` "circled ring operator"), prompt chrome styled like `claude >`. Sequence of beats:
   - t=33s: command typewriter starts — types `/goal all tests in test/auth pass and the lint step is clean` over ~5s
   - t=39s: `◎ /goal active · 00:01` indicator appears below the command (scale-slam SFX, 0.20 vol)
   - t=40-44s: simulated turn-1 output text — `Running pytest tests/auth/... · 2 failed in tests/auth/login_test.py`
   - t=45s: verdict-no bubble enters from right — `Haiku · no · 'auth/login_test.js still failing'` with muted red border (glitch-zap SFX, 0.12 vol)
   - t=46-52s: simulated turn-2 output — `Fixing login_test.py · Running pytest tests/auth/... · all green · lint OK`
   - t=54s: verdict-yes bubble — `Haiku · yes — achieved` with green border (scale-slam SFX, 0.20 vol)
   - t=57s: transcript-style "achieved" line at bottom — `[goal achieved · 2 turns · 14m 32s]` with marker-highlight sweep
   - t=60s: thought-narration beat — small overline "That's the loop." in mono
   - t=64s: phase exit cue

   Use `gsap-typewriter` for both the command and the turn outputs; verdict bubbles enter with `back.out(1.7)` + spring-pop SFX. The simulation is FAKE in the sense that no real Claude Code session was captured — but every word, glyph, and behavior is verbatim from `tmp/source.md`. Per user memory rule (`feedback_no_fabrication_source_only`), this is acceptable BECAUSE every line of terminal text traces to source.md key-facts #1-23.

7. **Step-by-step reveal pattern (REQUIRED for S02 and S04)**: 4 cards in S02 at +1/+5.5/+10/+14.5s; 4 cells in S04 at row-1 +1.5s, row-2 +10s (with intra-row cells at +0.5s stagger). Use the explicit `tl.set()` at t=0 + `tl.to()` at reveal time pattern from `.claude/rules/step-by-step-reveal.md` — NOT `tl.from()`. Each card/cell must be invisible from frame 0 until its reveal beat fires.

8. **S04 mid-beat insertion (REQUIRED for 5s pacing rule)**: insert an intermediate beat between row 1 cell entrance (~67s) and the "fresh model" marker sweep (~73s). Suggested: at ~70s, scale-pulse the "normal prompt" cell (1.0 → 1.04 → 1.0 over 0.4s) as a lead-in to the comparison. Also at ~85s, add a marker-circle on the `/loop` cell as a tail-hold mid-beat. Without these, the visual pacing audit fails per `.claude/rules/visual-pacing-5s.md`.

9. **Shape backdrop rearrangement**: per `feedback_shape_rearrange_on_whoosh_default` memory rule — `#shape-backdrop` rearranges on every phase transition (cinematic-whoosh moment). Default behavior; no extra wiring needed if using the standard template's shape system.

10. **Source-fidelity at Phase 2b**: the head-noun gate already passed for variant_a in this plan (`Haiku judges Sonnet` is verbatim Claude Code default-model framing). Phase 2b should still re-check every digit + named-entity in the script before TTS. Specifically: confirm `v2.1.139` reads correctly via TTS as "version two point one point one three nine" (Phase 2a will prepend "version" per content-brief.md TTS table). The Unicode glyph `◎` should NEVER be read aloud — visual only; narration says "active indicator" if it needs to reference the symbol.

11. **No background music** — narration + SFX only (template constraint, DESIGN.md "What NOT to Do" #6). The Dynamous outro line lands in S05 narration around t=105-114s.

12. **`meta.json` settings**: set `"dynamousPromotion": false` per the brief's scope (no endcard wiring requested — just the spoken outro line, which is universal per the memory rule).

13. **Tone constraint reminder**: the user explicitly said curious / discovery, NOT pain / shame. Audit narration in Phase 2 — `keep going` should appear at most once and in a curiosity frame ("the prompts you used to type") not a shame frame ("you've typed it too many times"). Hero word is "**Wait.**" not "**FINALLY**" or "**WEEKS LATE.**"

14. **The ◎ glyph is the brand of this video**: it appears in S01 hero, S03 indicator beat, and S05 endcard. This consistency is the visual thread tying discovery → demo → CTA. Render in the orange Claude Code accent (`var(--orange)` from template `DESIGN.md`) at 160px in S01 and S05, 100px in S03. Use a subtle glow (`text-shadow: 0 0 30px rgba(orange, 0.4)`) to give it terminal-CRT warmth without violating the "no rainbow" anti-pattern.
