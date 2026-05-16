# Composition Plan: anthropic-claude-plan-programmatic-credits

## Director's Summary

A 180-second Anthropic-branded news-explainer Short on the **June 15 programmatic-credits unlock for paid Claude plans** — with the actual story being the *quietly bigger* third-party twist: tools like **Conductor** and **OpenClaw** now draw from your Claude plan credit, not raw API billing. The video opens thumbnail-grade (topic + brand + date locked at t=0), pivots through the four covered surfaces, lands the Conductor/OpenClaw shift, walks the Pro / Max / Team / Enterprise tier reach, anchors the June 8 → June 15 timeline, stacks the +50% Claude Code weekly limits bonus, surveys 5 anonymized community reactions across three sentiment buckets, frames the debate, and closes on a single binary question on screen + spoken + held still.

## Template & Structure

```yaml
template: shorts/anthropic
canvas: 1080x1920
duration_s: 180
fps: 30
phases: 9
composition_layout: inline-phase + mutex-visibility (per templates/shorts/anthropic/README.md)
sub_compositions: none
voice_profile: news-explainer
wpm: 160-170
word_budget: 480-510
background_music: none           # Anthropic Shorts forbid BG music
shape_backdrop_reposition: on every phase transition (default per template)
design_token_overrides: none     # use --orange / --purple / --blue / --green / --red as shipped
```

## Master Timeline

| Phase | id          | data_start | data_duration | Words | Narrative beat                                             | Visual archetype                                        | Key assets (registry / template)                          | Retention notes |
| ----- | ----------- | ---------- | ------------- | ----- | ---------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------- | --------------- |
| 1     | `#phase1`   | 0          | 2.5           | 0     | Thumbnail-grade open (topic locked from t=0, no narration) | beat-1a topic lockup (Anthropic template)               | template `#p1-topic-lockup`, brand logo, `#p1-ga-receipt`  | first-frame thumbnail; YouTube auto-pick |
| 2     | `#phase1b`  | 2.5        | 9.5           | 26    | Hook pivot — name the 4 covered surfaces                   | beat-1b hero slam → 4-surface fast reveal               | template `#p1-hero-content` extended w/ 4 mini chips       | step-by-step reveal (4 chips, ~1.6s apart) |
| 3     | `#phase2`   | 12         | 28            | 78    | The shift explained (Conductor + OpenClaw quietly bigger)  | overline + headline + 2 stat-pill cards (Conductor / OpenClaw) | template stat-pill-row (`shared/lib/blocks/stat-pill-row/`) | marker-highlight on "draws from YOUR credit" |
| 4     | `#phase3`   | 40         | 20            | 56    | Who gets it — Pro / Max / Team / Enterprise pill row       | 4-row pill list (purple → blue → green → orange) | adapted timeline-cards as a 4-pill column row              | step-by-step reveal (4 pills, ~4s apart) |
| 5     | `#phase4`   | 60         | 20            | 55    | Timeline — today / June 8 / June 15                        | 3-card dated timeline + `macOS-notification` block for June 8 email | template timeline-cards + registry `macOS-notification` | step-by-step reveal (3 cards, ~5s apart) |
| 6     | `#phase5`   | 80         | 30            | 84    | Bonus stack — +50% Claude Code weekly limits through Jul 13 | 50% hero stat-pill + 4-surface chip row + countdown chip | stat-pill-row + chip row (CLI / IDE / desktop / web)       | counter tick 0→50 + step-by-step chips |
| 7     | `#phase6`   | 110        | 40            | 105   | Community reactions montage (5 anonymized x-post cards)    | 5 sequential `x-post` blocks cycling across 3 sentiment buckets | registry `x-post` block (Social Media Overlays family)     | step-by-step reveal (5 cards, ~7s apart, mutex visibility) |
| 8     | `#phase7`   | 150        | 20            | 60    | The big question — debate framing                          | split-headline (game changer / backdoor price hike) + URL pill | adapted `cta-url-slam` pattern with `support.claude.com/en/articles/15036540` | marker-highlight on "vault" claim |
| 9     | `#phase8`   | 170        | 10            | 36    | Thumbnail-grade close — recap + brand + CTA question       | thumb-frame: topic + Anthropic mark + CTA question + date | template `#p4` adapted to held-still frame                 | terminal hold ≥1.5s; 5-element thumb check |
|       | **TOTAL**   |            | **180.0**     | **500** |                                                            |                                                         |                                                            |             |

**Total check**: 2.5 + 9.5 + 28 + 20 + 20 + 30 + 40 + 20 + 10 = **180.0s** (no overlap, no gap).

## Narrative Arc

Kallaway breakdown (news-explainer profile — every transition uses an explanatory connector):

1. **Hook — Context Lean-In** (Phases 1–2, 0–12s, ~7% of duration). Topic locked thumbnail-grade at t=0, then hook pivot names the 4 covered surfaces.
2. **Scroll-Stop Interjection** (Phase 2 → Phase 3 transition at ~12s). "But here's the part Anthropic *didn't* lead with." (connector: *but here's*).
3. **Contrarian Snapback** (Phase 3, 12–40s). Conductor and OpenClaw — third-party tools draw from YOUR plan credit. The headline is hiding something.
4. **Solution / context delivery** (Phase 4, 40–60s, ~11%). Pro / Max / Team / Enterprise — who actually unlocks this.
5. **Deep Dive** (Phases 5–6, 60–110s, ~28%). The timeline (Phase 5: today → June 8 → June 15), then the bonus stack (Phase 6: +50% through Jul 13).
6. **Social Proof / Trust** (Phase 7, 110–150s, ~22%). Anonymized community reactions across 3 buckets — pragmatic / confused / critical.
7. **CTA Lead-in + CTA** (Phases 8–9, 150–180s, ~17%). Frame the debate, then close on the binary question — spoken + on-screen + thumbnail-grade.

**Connector words planned** (Phase 2.5 Pass 6 gate — required for news-explainer):

| Transition           | Connector word/phrase            |
| -------------------- | -------------------------------- |
| P1→P2 (silent → hook) | "Starting June 15…" (anchor)    |
| P2→P3                | "But the headline is hiding…"   |
| P3→P4                | "And who gets it? …"            |
| P4→P5                | "Here's the timeline…"          |
| P5→P6                | "Plus — stacking on top…"       |
| P6→P7                | "So how is the community taking it?" |
| P7→P8                | "Which leaves one question…"    |
| P8→P9                | "So…" (CTA spoken closer)       |

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Anthropic just changed who you're paying for."
    layers_present: [1, 4, 5]
    source_fidelity:
      source_quote: "third-party tools built on the Agent SDK like Conductor and OpenClaw work with your Claude plan, but will draw from your credit the same way your own scripts do."
      head_nouns: ["tools", "credit", "plan"]
      passes_gate: true
    advisory_score: 7.9
    rationale: "Counterintuitive opener — the 'who you're paying for' framing is provocative but source-grounded (Conductor + OpenClaw drawing from your credit IS a who-you're-paying-for shift). No digits to drift on. Strong curiosity gap but lighter on stakes specificity."
  variant_b:
    type: "stakes"
    opening_line: "Starting June 15, third-party tools like Conductor and OpenClaw will pull from your Claude plan credit — the same way your own scripts do."
    layers_present: [2, 3, 5]
    source_fidelity:
      source_quote: "Starting June 15, paid Claude plans can claim a dedicated monthly credit for programmatic usage. … third-party tools built on the Agent SDK like Conductor and OpenClaw work with your Claude plan, but will draw from your credit the same way your own scripts do."
      head_nouns: ["tools", "credit", "Claude plan"]
      passes_gate: true
    advisory_score: 7.2
    rationale: "Stakes-led, named entities up front, source-direct. Slightly slow open — 22 words pre-pivot. Lacks the stop-the-scroll punch of variant C."
  variant_c:
    type: "number"
    opening_line: "Four surfaces. One credit. One quiet shift."
    layers_present: [3, 4, 5]
    source_fidelity:
      source_quote: "The credit covers usage of: Claude Agent SDK, claude -p, Claude Code GitHub Actions, Third-party apps built on the Agent SDK"
      head_nouns: ["surfaces", "credit", "shift"]
      passes_gate: true
    advisory_score: 9.1
    rationale: "Triple-punch open — '4. 1. 1.' creates fast tempo cohesion. The 'quiet shift' tees up the contrarian snapback in Phase 3. Stun-gun bonus (implicit pivot). High specificity, strong curiosity gap. Source-grounded: 4 = the 4 surfaces in Post 1; 1 credit = the monthly credit in Post 1; 1 shift = the Conductor/OpenClaw twist in Post 2. WINNER."
  recommended: "variant_c"
```

**Selected — Variant C** opens on a triple-stat punch ("Four surfaces. One credit. One quiet shift.") that immediately scoops the viewer's attention and tees up the contrarian Phase 3 reveal without burning the punchline. Source-clean: every numeral traces to source §1 Post 1 (4 surfaces) and §1 Post 2 (the third-party shift = "one quiet shift"). Highest advisory score (9.1) and best fit for the news-explainer skeptical-edge tone.

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "StatCascade"          # triple-stat punch into contrarian pivot
  selected_variant: "variant_c"

  visual_beats:
    - beat: "Thumbnail-grade open (beat 1a)"
      timing_s: [0, 2.5]
      visual: "Topic lockup at full opacity from frame zero. Anthropic logo + topic slam 'CLAUDE PLANS GET PROGRAMMATIC CREDITS' (160px, accent on 'CREDITS' in orange) + receipt line 'JUNE 15 · 4 SURFACES · PRO / MAX / TEAM / ENTERPRISE'."
      gsap_ease: "none (static, t=0)"
      sfx: null

    - beat: "Hook pivot — Four surfaces (chip 1)"
      timing_s: [3.5, 4.5]
      visual: "Topic lockup fades out at 2.4s. Hero overline + 'Four surfaces.' hero word (200px orange) lands at ~2.7s. First surface chip 'Claude Agent SDK' enters at 3.5s."
      gsap_ease: "back.out(1.7)"
      sfx: null  # default Anthropic = no per-element SFX

    - beat: "Hook pivot — chips 2/3/4 (step-by-step)"
      timing_s: [4.5, 9.5]
      visual: "Three remaining surface chips enter at ~1.6s intervals — 'claude -p' (4.5s), 'Claude Code GitHub Actions' (6.1s), 'Third-party apps' (7.7s). Each pops in via spring (scale 0.85→1, opacity 0→1)."
      gsap_ease: "back.out(1.5) + stagger"
      sfx: null

    - beat: "Pivot teaser — 'One credit. One quiet shift.'"
      timing_s: [9.5, 12.0]
      visual: "Caption pill below chips '1 monthly credit · 1 quiet shift' (mono 32px). Subtle marker-highlight sweeps under 'quiet shift' from 10.5s to 11.2s. Phase 1b begins exit blur/crossfade at T1 = 11.6s."
      gsap_ease: "power3.out + marker sweep"
      sfx: cinematic-whoosh (at sceneT-0.4 = 11.2s, paired with shape reposition; 1.5s duration; 0.11 volume)

  pivot_word: "shift"               # the marker-highlight word in caption pill
  brand_reveal_word: "Anthropic"    # visible from t=0 via top-banner + brand-lockup logo

  assets_needed:
    - type: "logo"
      description: "Anthropic wordmark light SVG (top banner + brand lockup)"
      source: "shared/logos/anthropic-logo-light.svg (already copied into assets/ during template spawn)"

  music_profile:
    hook_mood: "NONE"   # template forbids background music on Shorts
    hook_bpm: null
    body_bpm: null
    cta_bpm: null
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "Phase 2 (hook pivot, ~10s)"
    setup_line: "Four surfaces. One credit. One quiet shift."
    resolution_scene: "Phase 3 (the shift explained, ~12-40s)"
    resolution_line: "The shift: Conductor and OpenClaw — third-party tools built on the Agent SDK — now draw from your Claude plan credit, the same way your own scripts do."
    type: "mystery"

  loop_openers:
    - scene: "Phase 5 (timeline)"
      position: "opening"
      phrase: "Here's the timeline — and the part most people are about to miss."
    - scene: "Phase 7 (reactions)"
      position: "opening"
      phrase: "So how is the community taking it?"
    - scene: "Phase 8 (debate)"
      position: "transition"
      phrase: "Which leaves one question."
```

## Story Lock Placement

- **Term Branding (Lock #1)** — Phase 3 coins **"programmatic credit"** as the consistent label for the monthly pool. Used identically in spoken script and on-screen pill labels.
- **Negative Frame (Lock #4)** — Phase 7 (community reactions) carries the critical-bucket frame: "*This is how you know when a startup becomes enterprisey.*" (anonymized handle @cynicop). Does NOT appear in the hook.
- **Loop Opener (Lock #5)** — Phase 5 opening "Here's the timeline — and the part most people are about to miss." cued at ~60s. Phase 7 opening at ~110s. Phase 8 transition at ~150s.
- **Thought Narration (Lock #3)** — Phase 8 ("Which leaves one question…") just before CTA reveal. Models the viewer's mental beat at the moment of decision.

## Composition Layout

```yaml
composition_layout:
  pattern: "inline-phase + mutex-visibility (extended from 4 to 9 phases)"
  base_template_phases:
    - "phase1 (thumbnail intro + hero slam)"
    - "phase2 (stat pill row)"
    - "phase3 (timeline cards)"
    - "phase4 (CTA URL slam)"
  extension:
    - "phase1 split into beat 1a (lockup, 0-2.5s) + beat 1b (hook pivot, 2.5-12s, renamed #phase1b internally)"
    - "phase2 (the shift explained) — adapts template stat-pill-row to Conductor / OpenClaw cards"
    - "phase3 (Pro/Max/Team/Enterprise) — adapts timeline-cards as a 4-pill column row"
    - "phase4 (timeline) — uses template timeline-cards with macOS-notification block overlay on the June 8 card"
    - "phase5 (bonus stack) — adapts stat-pill-row with one hero 50% pill + chip row underneath"
    - "phase6 (reactions montage) — NEW phase using registry x-post block 5x cycling"
    - "phase7 (debate framing) — adapts URL slam to split-headline + URL pill"
    - "phase8 (thumbnail close) — adapts CTA URL slam to thumbnail-grade held still"
  total_phase_divs_in_html: 9    # one #phaseN per beat
  z_index_stack: "phase1=1 .. phase8=8 (per template 'Adding more phases' convention)"
  transitions: "P→T pattern at every boundary, 0.4s blur+crossfade, shape-backdrop reposition starts at sceneT-0.4"
```

## Retention Component Picks

```yaml
retention_component_picks:
  phase_01_thumbnail_open:
    structural: "inline-phase + mutex-visibility (beat 1a)"
    pattern: "thumbnail-grade-open"   # template's beat 1a
    primitives: ["static-lockup at t=0 (no entrance tween)"]
    captions: null
    audio_reactive: null
    transition_out: "opacity fade (template default) at 2.4s into beat 1b"

  phase_02_hook_pivot:
    structural: "inline-phase (beat 1b inside #phase1)"
    pattern: "hero-slam → 4-chip step-by-step reveal"
    primitives:
      - "gsap-stagger-grid"          # 4 chip entrances
      - "marker-highlight on 'quiet shift'"   # 1 marker
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T1 = 11.6s (cinematic-whoosh sync at 11.2s)"

  phase_03_the_shift:
    structural: "inline-phase"
    pattern: "stat-pill-row adapted (Conductor / OpenClaw cards)"
    primitives:
      - "gsap-stagger-grid"          # card entrances
      - "marker-highlight on 'draws from YOUR credit'"   # 1 marker
      - "scale-pulse on 'the same way your own scripts do' line at ~28s"
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T2 = 39.6s"

  phase_04_who_gets_it:
    structural: "inline-phase"
    pattern: "4-pill column row (adapted timeline-cards)"
    primitives:
      - "gsap-stagger-grid (4 pills, 4s apart per step-by-step rule)"
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T3 = 59.6s"

  phase_05_timeline:
    structural: "inline-phase"
    pattern: "timeline-cards + macOS-notification overlay on June 8 card"
    primitives:
      - "gsap-stagger-grid (3 timeline cards)"
      - "gsap-path-draw on connecting line between cards"
      - "macOS-notification block fires at ~66s ('Claim your credits — Anthropic')"
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T4 = 79.6s"

  phase_06_bonus_stack:
    structural: "inline-phase"
    pattern: "stat-pill-row + chip-row (hero 50% pill + 4 surface chips)"
    primitives:
      - "gsap-counter-tween (50% counter, 0→50 over 1.5s)"
      - "gsap-stagger-grid (4 chips: CLI / IDE / desktop / web)"
      - "marker-highlight on 'through July 13'"   # 1 marker
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T5 = 109.6s"

  phase_07_reactions_montage:
    structural: "inline-phase with sub-phase mutex (5 x-post cards swap inside #phase6)"
    pattern: "x-post block cycling (registry)"
    primitives:
      - "registry x-post block × 5 (each ~6.5s on screen, 0.5s crossfade between)"
      - "sentiment bucket label chip swap (PRAGMATIC / CONFUSED / CRITICAL)"
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T6 = 149.6s"

  phase_08_debate_frame:
    structural: "inline-phase"
    pattern: "split-headline + URL pill"
    primitives:
      - "gsap-fromto on split halves ('GAME CHANGER' green / 'BACKDOOR PRICE HIKE' red)"
      - "marker-highlight under URL pill 'support.claude.com/en/articles/15036540'"
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade at T7 = 169.6s"

  phase_09_thumbnail_close:
    structural: "inline-phase (terminal hold)"
    pattern: "thumbnail-grade-close (5-element checklist)"
    primitives:
      - "static held frame after 0.5s entrance burst (≥1.5s terminal hold per shorts-thumbnail-frames.md)"
    captions: null
    audio_reactive: null
    transition_out: null   # final phase
```

**Inventory check:**

- **Markers**: 5 total (1 per phase max, 0 in 4 phases) — well within the 2-per-phase cap.
- **Captions**: 0 (Short is dense; no synced caption tracks).
- **Audio-reactive**: 0 (template default for news-explainer + no BG music).
- **Transitions**: 7 blur-crossfades + shape-backdrop reposition + cinematic-whoosh per boundary. ONE transition style — passes "60-70% same transition" rule.

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "phase_01_thumbnail_open"
    data_start: 0
    data_duration: 2.5
    data_track_index: 1
    audio_anchor: "no narration in this window — pure visual lockup; YouTube auto-thumbnail catches t=0"

  - scene: "phase_02_hook_pivot"
    data_start: 2.5
    data_duration: 9.5
    data_track_index: 2
    audio_anchor: "narration starts at ~2.7s with 'Four surfaces.'; chip 1 lands ~3.5s; pivot at ~10.5s"

  - scene: "phase_03_the_shift"
    data_start: 12
    data_duration: 28
    data_track_index: 3
    audio_anchor: "Conductor named at ~17s; OpenClaw at ~19s; 'draws from your credit' marker at ~24s"

  - scene: "phase_04_who_gets_it"
    data_start: 40
    data_duration: 20
    data_track_index: 4
    audio_anchor: "Pro pill at ~42s; Max at ~46s; Team at ~50s; Enterprise at ~54s; tail-hold to 60s"

  - scene: "phase_05_timeline"
    data_start: 60
    data_duration: 20
    data_track_index: 5
    audio_anchor: "TODAY card at ~62s; June 8 card + macOS notif at ~66s; June 15 card at ~71s"

  - scene: "phase_06_bonus_stack"
    data_start: 80
    data_duration: 30
    data_track_index: 6
    audio_anchor: "+50% slam at ~82s; surface chips 84-95s; 'through July 13' marker at ~98s; 'stacks with' beat at ~103s"

  - scene: "phase_07_reactions_montage"
    data_start: 110
    data_duration: 40
    data_track_index: 7
    audio_anchor: "Card 1 @cardholder 110-117s; Card 2 @oldschool 117-124s; Card 3 @cynicop 124-131s; Card 4 @builderx 131-138s; Card 5 @skeptic42 138-145s; tail-hold 145-150s"

  - scene: "phase_08_debate_frame"
    data_start: 150
    data_duration: 20
    data_track_index: 8
    audio_anchor: "split halves enter 151-153s; URL pill at ~159s; 'which leaves one question' connector at ~166s"

  - scene: "phase_09_thumbnail_close"
    data_start: 170
    data_duration: 10
    data_track_index: 9
    audio_anchor: "CTA spoken at 170-174s; terminal hold 174.5-180s with CTA question on screen"

total_data_duration: 180     # this becomes #root data-duration
total_check: "0+2.5=2.5; +9.5=12; +28=40; +20=60; +20=80; +30=110; +40=150; +20=170; +10=180 ✓"
gap_check: "no gaps, no overlaps"
```

`audio_anchor` values are PLACEHOLDERS — Phase 3.5 retimes against `transcript.json` after TTS.

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/anthropic/DESIGN.md"
  overrides: []   # use as shipped — Anthropic brand video on Anthropic template
  accent_rotation:
    phase_02_hook_pivot: orange (hero) + neutral chips
    phase_03_the_shift: orange (Conductor card) + purple (OpenClaw card)
    phase_04_who_gets_it: purple (Pro) → blue (Max) → green (Team) → orange (Enterprise)   # 1 per pill, not 1 per phase — pill-row exception
    phase_05_timeline: orange (TODAY) → purple (June 8) → blue (June 15)
    phase_06_bonus_stack: orange (50% hero) + neutral chips
    phase_07_reactions_montage: per-card sentiment color — green (pragmatic) / blue (confused) / red (critical, used as chip border not text)
    phase_08_debate_frame: green (left half) + red (right half)
    phase_09_thumbnail_close: orange (topic accent) + green (CTA question)
  fonts:
    sans: "Inter"        # template default
    mono: "JetBrains Mono"
  typography_minimums:
    topic_slam_first_frame: 160px
    hero_slam_phase_2: 200px
    headline_phase_3: 64px
    pill_primary_phase_4: 48px
    pill_descriptor_phase_4: 30px
    timeline_card_title_phase_5: 40px
    fifty_percent_hero_phase_6: 240px
    x_post_card_handle_phase_7: 36px
    x_post_card_body_phase_7: 44px
    cta_question_phase_9: 52px
    receipt_caption: 44px
```

## AI Image Prompts

```yaml
images: []   # None — all visuals synthesized via template + registry blocks; no AI hero shots needed
```

## Screenshot Inventory

```yaml
screenshots: []   # None — source is X-thread text only; no demo URLs in scope per content brief
```

## HyperFrames Blocks

```yaml
hyperframes_blocks_used:
  - name: "x-post"
    scene: "phase_07_reactions_montage"
    why: "5 anonymized community-reaction cards cycling across 3 sentiment buckets — exactly the use case the registry catalog flags for the social-media-overlays family. Source §4 + content-brief.md §5."
  - name: "macOS-notification"
    scene: "phase_05_timeline"
    why: "Lands the 'June 8 — email to claim credits' beat as a desktop-style notification banner. Registry catalog suggests this exact use case. Source §1 Post 3."
```

Both blocks require `npx hyperframes add x-post --dir videos/anthropic-claude-plan-programmatic-credits` and `... add macOS-notification --dir ...` during the composition build phase (Phase 4). Wiring follows `shared/lib/MANIFEST.md` host-snippet convention.

## Fact-Check Audit

Every claim cross-referenced against `tmp/source.md` only (ARTICLE_RESPONSE mode — no WebSearch).

| Claim                                                                          | Source                                | Used in phase | Status |
| ------------------------------------------------------------------------------ | ------------------------------------- | ------------- | ------ |
| Programmatic credits launch on **June 15** for paid Claude plans              | source.md §1 Post 1, §1 Post 3        | P1, P2, P5    | ✓ verbatim |
| Credit covers: **Claude Agent SDK**                                            | source.md §1 Post 1 (bullet 1)        | P2 chip 1, P3 | ✓ verbatim |
| Credit covers: **`claude -p`**                                                 | source.md §1 Post 1 (bullet 2)        | P2 chip 2     | ✓ verbatim |
| Credit covers: **Claude Code GitHub Actions**                                  | source.md §1 Post 1 (bullet 3)        | P2 chip 3     | ✓ verbatim |
| Credit covers: **Third-party apps built on the Agent SDK**                     | source.md §1 Post 1 (bullet 4)        | P2 chip 4, P3 | ✓ verbatim |
| **Conductor** and **OpenClaw** named as examples of third-party tools          | source.md §1 Post 2                   | P3            | ✓ verbatim |
| Third-party tools **"draw from your credit the same way your own scripts do"** | source.md §1 Post 2 (direct quote)    | P3            | ✓ verbatim |
| **June 8** — email to claim credits                                            | source.md §1 Post 3                   | P5            | ✓ verbatim |
| Plans covered: **Pro / Max / Team / Enterprise (seat-based)**                  | source.md §3 + §2 Post A              | P1 receipt, P4 | ✓ verbatim |
| **Claude Code weekly limits +50%** through **July 13**                         | source.md §2 Post A + quote image     | P6            | ✓ verbatim |
| All surfaces for +50%: **CLI / IDE extensions / desktop / web**                | source.md §2 Post B (bullet 1)        | P6 chip row   | ✓ verbatim |
| **"Nothing to opt into / already applied"** for +50%                           | source.md §2 Post B (bullet 3) + image | P6           | ✓ verbatim |
| **Stacks with last week's 2× 5-hour limit increase**                           | source.md §2 Post B (bullet 4)        | P6 closing    | ✓ verbatim |
| Live now / runs through **July 13 at 6PM PDT / 1AM GMT**                       | source.md §2 Post B (bullet 2)        | P6 (omit GMT time — too granular for Short; keep "through July 13") | ✓ summarized faithfully |
| Support URL: `support.claude.com/en/articles/15036540`                         | source.md §1 end                      | P8            | ✓ verbatim |
| 5 anonymized handles (@cardholder, @oldschool, @cynicop, @builderx, @skeptic42) | content-brief §5 (Phase-2/4 convention) | P7         | ✓ anonymized per source §4 instruction |
| Reaction 1 (@cardholder, pragmatic): "Makes the paid plan easier to justify…"  | source.md §4 Positive bullet 1        | P7 card 1     | ✓ verbatim |
| Reaction 2 (@oldschool, critical, paraphrased): "Your competitors will thank you…" | source.md §4 Critical bullet 3 (f-bombs paraphrased) | P7 card 2 | ✓ paraphrase per §4 note |
| Reaction 3 (@cynicop, critical): "This is how you know when a startup becomes enterprisey." | source.md §4 Critical bullet 2 | P7 card 3 | ✓ verbatim |
| Reaction 4 (@builderx, pragmatic): "Anthropic quietly making it easier to go from idea to production." | source.md §4 Positive bullet 2 | P7 card 4 | ✓ verbatim |
| Reaction 5 (@skeptic42, confused): "Does previous usage remain the same alongside monthly credits?" | source.md §4 Confused bullet 3 | P7 card 5 | ✓ verbatim |
| CTA question: **"OpenClaw and Conductor on your plan — game changer or backdoor price hike?"** | source.md §7 candidate 1 + content-brief §8 lock | P8, P9, spoken closer, description | ✓ verbatim |

**Removed / rephrased claims**: NONE. Every claim in the plan traces to source.md. No dollar amounts, no token volumes, no Conductor/OpenClaw pricing, no "in response to competitor X" framing, no permanent / will-renew language, no Education-tier mention — all per content-brief §11 / §12 anti-fabrication ledger.

## TTS Heteronym Audit (Phase 2a Flag-Ahead)

Per `.claude/rules/tts-pronunciation.md` — `eleven_multilingual_v2` has no per-word semantic disambiguation. Pre-empt these in Phase 2a:

| Word / phrase                          | Risk                                                | Default fix at script-level                           |
| -------------------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| **"live now"** (Phase 6 +50% beat)     | "live" → /lɪv/ (verb "reside") instead of /laɪv/ (adj "available") | Replace with **"available now"** or **"already running"** |
| **"live on June 15"** (Phase 5)        | Same — verb misread                                | Replace with **"goes into effect June 15"** (already used in source.md §1 Post 3) or **"available June 15"** |
| **"lead beat"** (any director-summary phrasing in narration) | n/a — only used in this plan, not narration | No fix needed |
| **`claude -p`** (Phase 2 chip 2)       | TTS pronounces hyphen + letter awkwardly           | Spell as **"claude dash P"** in script.txt (per .claude/rules/tts-pronunciation.md tech-term audit) |
| **"SDK"** (Phase 2, Phase 3)           | TTS may compress to "essdeekay"                    | Spell as **"S D K"** with spaces in script.txt |
| **"CLI"** (Phase 6 chips)              | TTS may say "klee"                                  | Spell as **"C L I"** in script.txt |
| **"IDE"** (Phase 6 chips)              | TTS may say "eye-dee"                              | Spell as **"I D E"** in script.txt |
| **"OpenClaw"**                         | Brand name — TTS may say "open-claw" vs "OpenClaw" | Probe-test in Phase 2a; if it slurs, spell as **"Open Claw"** with space |
| **"Conductor"**                        | Common word — should read correctly                | No fix needed |
| **"+50%"** (Phase 6)                   | TTS may say "plus fifty percent" — usually fine    | Confirm in Phase 2a probe; if odd, write as **"fifty percent higher"** |

**Critical:** the source uses "Live now" repeatedly (§2 Post A + Post B). Phase 2a MUST replace every adjective-sense "live" before generating TTS. This is the #1 known failure mode for this video's vocabulary.

## Notes for Composition Build (Phase 4 / `new-anthropic-short.md`)

1. **Phase mutex extension**: the template ships with 4 phase divs. This plan needs **9 phase divs** (phase1 = beat-1a thumbnail lockup + beat-1b hook pivot, but they share `#phase1` per template default; phases 2–9 add 8 new `<div class="phase">` blocks following the template's "Adding more phases" convention — bump z-index, opacity:0 default).
2. **Beat 1a topic slam content** (verbatim): `CLAUDE PLANS GET <span class="accent">PROGRAMMATIC CREDITS</span>` on two lines. Receipt line: `JUNE 15 · 4 SURFACES · PRO / MAX / TEAM / ENTERPRISE`.
3. **Phase 1b chip layout**: 4 chip rows in a column inside `#p1-hero-content` — replace the existing `#p1-pre` / `#p1-hero` / `#p1-caption` with overline + hero word "Four surfaces." + 4 chip rows + caption pill ("1 monthly credit · 1 quiet shift"). Step-by-step reveal at 3.5s, 4.5s, 6.1s, 7.7s.
4. **Phase 3 (the shift)**: 2 stat-pill cards but with TEXT content not just numbers — left card "CONDUCTOR" (orange), right card "OPENCLAW" (purple). Below: headline `Third-party tools, your credit.` (64px) + body line "draws from your credit the same way your own scripts do." (40px) with marker-highlight under "draws from your credit".
5. **Phase 4 (Pro/Max/Team/Enterprise)**: 4 pill rows in a vertical column (NOT timeline-cards 2-column hybrid). Use `tl.set()` at t=0 to hide all 4 (required hidden-until-reveal pattern from `step-by-step-reveal.md`). Reveal at 4s intervals.
6. **Phase 5 timeline + macOS-notification**: `npx hyperframes add macOS-notification --dir videos/...` before authoring. Trigger the notification 1s after the June 8 card lands (~67s), let it persist 3s, dismiss before June 15 card enters.
7. **Phase 6 (+50% bonus)**: hero stat-pill at top with `gsap-counter-tween` (0→50 over 1.5s starting ~82s). Below: 4 surface chips (CLI / IDE / desktop / web) staggered 84-95s. Bottom line: `Through July 13 · already applied · stacks with last week's 2× boost` with marker-highlight under "through July 13".
8. **Phase 7 reactions**: `npx hyperframes add x-post --dir videos/...` before authoring. 5 instances of the x-post block, mutex-stacked inside `#phase6`. Each card swaps via 0.5s crossfade. Sentiment-bucket label chip (top-right): `PRAGMATIC` (green) / `CRITICAL` (red) / `CONFUSED` (blue) swaps with each card. **No real handles** — use exact assignments from content-brief §5.
9. **Phase 8 (debate frame)**: split-screen horizontal — top half "GAME CHANGER" (green, 120px), bottom half "BACKDOOR PRICE HIKE?" (red, 120px), divider line in the middle. URL pill below: `support.claude.com/en/articles/15036540` (mono 56px). Marker-highlight under URL at ~165s.
10. **Phase 9 (thumbnail close)**: 5-element thumbnail checklist —
   1. Topic statement (160px): `PROGRAMMATIC CREDITS` (orange accent on "CREDITS")
   2. Visual anchor: Anthropic logo (`#p9-brand-logo`, ~120px height)
   3. Brand chrome: top-banner Anthropic wordmark (persists, already shipped by template)
   4. Outcome receipt: `JUNE 15 · 4 SURFACES · 4 PLANS` (44px mono)
   5. CTA pill (subordinate): the debate question — **"OpenClaw + Conductor on your plan — *game changer* or *backdoor price hike*?"** (52px, orange with italic emphasis on accent words). MUST match the spoken closer verbatim AND the YouTube description's closing paragraph.
   - All elements enter inside 0.5s of phase start (170-170.5s). Terminal hold = 174.5-180s = 5.5s static (well above the 1.5s minimum).
11. **Engagement CTA locked** — verbatim across all 3 placements:
    - **Spoken** (Phase 9 narration 174-178s): "So — OpenClaw and Conductor on your plan. Game changer, or backdoor price hike? Drop your pick below."
    - **On-screen** (`#p9-cta-question` element, visible 170.5-180s): `OpenClaw + Conductor on your plan — game changer or backdoor price hike?`
    - **YouTube description** (closing paragraph): same wording. Phase YT writes it.
12. **Shape-backdrop reposition timing** (HARD per template DESIGN.md): each `cinematic-whoosh` MUST start at `sceneT - 0.4`. Transition times: T1=11.6, T2=39.6, T3=59.6, T4=79.6, T5=109.6, T6=149.6, T7=169.6 → whoosh `data-start` values: 11.2, 39.2, 59.2, 79.2, 109.2, 149.2, 169.2. Each `data-duration=1.5`, `data-volume=0.11`, `data-track-index=3` (sequential — no overlap so single track fine).
13. **No per-element SFX** — Anthropic default. Only the 7 cinematic-whooshes. (If Phase 2.5 critique flags a moment as dramatically under-punctuated, opt-in ONE scale-slam on the +50% counter peak in Phase 6 — but this is a discretionary call, not a plan requirement.)
14. **Hidden-until-reveal pattern (CLAUDE.md rule #9 / step-by-step-reveal.md)**: every enumerated list in this plan (4 chips Phase 2, 4 pills Phase 4, 3 timeline cards Phase 5, 4 chips Phase 6, 5 reaction cards Phase 7) MUST use explicit `tl.set(target, { opacity: 0 }, 0)` at t=0 PLUS `tl.to(target, { opacity: 1, ... }, revealTime)`. Do NOT use `tl.from()` for these.
15. **Visual-pacing-5s audit** — every phase has beats at least every 5s:
    - P1 (2.5s lockup): single static frame, opening hold relaxation per shorts-thumbnail-frames.md
    - P2 (9.5s): chips at 3.5/4.5/6.1/7.7 + marker at 10.5 → max gap 1.6s ✓
    - P3 (28s): card 1 at ~15, card 2 at ~19, marker at ~24, scale-pulse at ~28, headline tighten at ~32, body line at ~35 → max gap ~4s ✓ (verify in Phase 4 build)
    - P4 (20s): pill 1 at ~42, pill 2 at ~46, pill 3 at ~50, pill 4 at ~54, tail-hold 54-60 (6s gap risks violation — add subtle scale-pulse on Enterprise pill at ~58s to stay under 5s)
    - P5 (20s): card 1 at ~62, macOS notif at ~66, card 2 fade-up at ~67, card 3 at ~71, marker sweep at ~76 → max gap ~5s ✓
    - P6 (30s): counter starts ~82, chips 84/87/90/93, marker at ~98, beat at ~103, "stacks" at ~107 → max gap ~5s ✓ (tight)
    - P7 (40s): card 1 110-117, card 2 117-124, card 3 124-131, card 4 131-138, card 5 138-145, tail 145-150 — each swap IS a beat (~7s apart), with internal scale-pulse on key-quote word at +3s of each card → max gap 3s ✓
    - P8 (20s): split halves 151+153 + URL pill at 159 + marker at 165 + connector line at 167 → max gap ~6s (insert subtle scale-pulse on URL pill at 162s to stay under 5s)
    - P9 (10s): all elements at 170-170.5 + terminal hold relaxation per shorts-thumbnail-frames.md
    - **Compliance gates to verify post-build**: P4 tail-hold scale-pulse, P8 URL-pill scale-pulse.
16. **Thumbnail-grade frame check** (per `.claude/rules/shorts-thumbnail-frames.md`):
    - **t=0 (first frame)**: topic statement "CLAUDE PLANS GET PROGRAMMATIC CREDITS" (160px) + Anthropic logo (~100px height) + receipt "JUNE 15 · 4 SURFACES · PRO / MAX / TEAM / ENTERPRISE" + Anthropic top banner. **All 5 mandatory elements present**: topic ✓, visual anchor (logo) ✓, brand chrome (top banner) ✓, outcome receipt ✓, CTA pill (n/a at t=0 — topic carries scroll-stop). PASS.
    - **t=180 (last frame, held 174.5-180s)**: topic recap "PROGRAMMATIC CREDITS" (160px, accent) + Anthropic logo (120px) + receipt "JUNE 15 · 4 SURFACES · 4 PLANS" (44px) + CTA question "OpenClaw + Conductor on your plan — game changer or backdoor price hike?" (52px, orange). **All 5 mandatory elements present**: topic ✓, visual anchor ✓, brand chrome ✓, outcome receipt ✓, CTA pill (the debate question itself) ✓. PASS.

## Next step

Run `/diy-yt-creator:phase2-script anthropic-claude-plan-programmatic-credits`.
