# Composition Plan: npm-shai-hulud-worm-attack

## Director's Summary

A 180-second tech-influencer-edgy explainer of the Mini Shai-Hulud npm worm (May 2026): one fork-PR, six minutes, 169 compromised packages, signed with valid SLSA Level 3 provenance. The Short opens on a thumbnail-grade topic lockup (NPM JUST GOT HIJACKED + 169 packages / 6 minutes receipt + brand chrome), pivots into a violent-contrast Trojan-horse hook ("Signed. Verified. Still malware."), walks the attack chain in four numbered beats (misconfig → cache poison → worm spread → persistence + dead-man switch), surfaces the pnpm v11 defense (three defaults that ship today), then closes on a debate-sparking final frame: "pnpm by Friday — or rolling dice?" Visual language uses the warm-paper `shorts/standard` template (cream canvas, terracotta/indigo/sage/gold/rose accents, Playfair serif headlines, JetBrains Mono technical voice). Nine scene archetypes from the template (title, marker, code-block, timeline, chart-style stat, bullets, image-card, compare, cta).

## Template & Structure

- **Template**: `templates/shorts/standard/` (warm-paper editorial — canonical Shorts baseline)
- **Resolution**: 1080×1920 vertical, 30fps
- **Duration**: 180s (Shorts hard max)
- **Composition layout**: `sub-composition` — root `index.html` orchestrates ambient + chrome + scene crossfades; each scene is a self-contained `compositions/scene-*.html` with its own paused timeline on `window.__timelines["scene-<name>"]`.
- **Phase mutex**: `crossfadeScenes()` (1.1s span: 0.5s blur out → 0.4s opacity out → 0.3s opacity in → 0.5s blur in)
- **Accent rotation**: terracotta → indigo → sage → gold → rose, repeating, with terracotta reserved for the danger/worm beats (P1, P3, P5, P6) and sage/indigo for the defense beats (P7)
- **Design token overrides**: NONE (use the template's `tokens/standard-short.css` as-shipped; warm paper aesthetic is on-brand for a Fireship-style breakdown)
- **Logo**: top-banner pill reads `NPM SUPPLY CHAIN` (kebab wordmark with terracotta dot — no real brand logo; the topic itself is the chrome)

## Master Timeline

| Scene | data_start | data_duration | Visual Goal | Key Elements |
|-------|-----------|---------------|-------------|--------------|
| P0 — Thumbnail Open | 0 | 6 | Topic + brand + receipt visible at t=0 (YouTube auto-thumbnail) | Topic slam "NPM JUST GOT HIJACKED" 152px, terracotta marker on "HIJACKED", outcome line "169 packages. 6 minutes.", brand chrome top-banner |
| P1 — Hook (Trojan Horse) | 6 | 16 | Violent-contrast pivot: trusted publishing → signed malware | Mono kicker "TRUSTED PUBLISHING", italic claim "supposed to stop this", PIVOT "BUT." 240px terracotta, reveal "Signed. SLSA-attested. STILL malware." |
| P2 — The Misconfig (YAML) | 22 | 24 | The smoking gun: `pull_request_target` line highlighted | scene-code-block w/ `bundle-size.yml`, marker-highlight on `pull_request_target`, marker-circle on `ref: refs/pull/.../merge` |
| P3 — The Cache Poison Timeline | 46 | 26 | 8-hour dwell, fork-PR closes, cache sits live, unrelated merge triggers | scene-timeline w/ 4 dated rows (Hour 0 fork, Hour 0 close, Hour 8 merge, Hour 8 publish), red glow on cache row, terracotta accent |
| P4 — The Worm Spreads | 72 | 24 | Stat slam: 373 versions / 169 packages / 518M downloads + company list step-reveal | scene-stat hybrid w/ counter tween 0→169, then step-reveal of TanStack/Mistral/UiPath/OpenSearch/Guardrails/Squawk pills (5s apart) |
| P5 — The Persistence Twist | 96 | 26 | "npm uninstall doesn't work" — editor hooks + forged Claude commits | scene-image-card-style w/ fake commit row (`claude@users.noreply.github.com — chore: update dependencies`), marker-scribble on "uninstalled", FORGED stamp |
| P6 — Dead-Man Switch | 122 | 22 | 60s countdown + token name reveal + `rm -rf ~/` flash | scene-marker w/ 60-second clock pulse, mono token name `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner`, monospace `$ rm -rf ~/` slam |
| P7 — The Defense (pnpm v11) | 144 | 22 | Three shield badges step-reveal: minimumReleaseAge / blockExoticSubdeps / approved-builds | scene-bullets w/ 3 stacked cards (~5s apart), each with sage accent, terracotta worm icon bounces off |
| P8 — Thumbnail Close + CTA | 166 | 14 | Held thumbnail-grade frame + debate question + URL pill | scene-cta hybrid: topic "PNPM V11 OR ROULETTE" 144px, outcome "Three defaults blocked the entire chain.", debate-question "Switching today — or waiting for the next worm?", `pnpm.io/blog/releases/11.0` URL pill |

**Total**: 180s (matches `#root` `data-duration`)
**Scene count**: 9 (P0–P8 — exactly mapped to orchestrator's recommended structure)

## Narrative Arc

Kallaway formula applied:

1. **Context Lean-In** (P0, 0–6s, ~3.3% of duration) — thumbnail lockup with topic + receipt. Viewer self-selects in <2s.
2. **Scroll-Stop Interjection** (P1, 6–22s, ~8.9%) — "BUT." pivot smashes through trusted-publishing assumption. The Stun Gun.
3. **Contrarian Snapback** (woven into P1 + P2) — "trusted publishing is NOT a trust boundary — it's a permissions boundary." The Uno Reverse.
4. **Solution Frame** (P2 setup) — names the mechanism: misconfigured `pull_request_target`.
5. **Deep Dive** (P2–P6, 22–144s, ~67.8% of duration — five benefit-led feature scenes covering the attack mechanics)
6. **Social Proof / Trust** (P4 logos + P5 forged commits) — every dev recognizes TanStack, Claude Code, Mistral.
7. **CTA + Debate** (P7–P8, 144–180s, ~20%) — pnpm v11 defense + binary debate question.

**Voice profile** = `news-explainer` → every scene transition uses an explanatory connector word (`because`, `so`, `here's why`, `the result`, `which means`, `but`, `the fix`). Pure-fragment narration is FORBIDDEN — will fail Phase 2.5 Pass 6 otherwise.

Connector plan per transition:
- P0 → P1: "But here's the worst part…"
- P1 → P2: "So how did they do it? Here's the smoking gun."
- P2 → P3: "Which means the moment they closed that PR…"
- P3 → P4: "And that's how a TanStack problem became an everybody problem."
- P4 → P5: "But the worm didn't stop at publishing. Here's the twist."
- P5 → P6: "And my favorite part — the dead-man switch."
- P6 → P7: "So how do you stop this? The fix already shipped."
- P7 → P8: "Three defaults. Already shipped. Nobody migrated."

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "Your trusted-publishing setup just shipped malware. Signed. Verified. SLSA-attested."
    layers_present: [1, 2, 3, 4, 5]
    source_fidelity:
      source_quote: "the poisoned packages were signed, verified, and shipped through npm's trusted publishing feature, which was built primarily to prevent these kinds of attacks"
      head_nouns: ["packages", "trusted publishing"]
      passes_gate: true
    curiosity_gap: 9
    stakes_clarity: 8
    specificity: 7
    stun_gun_bonus: 0.0  # no but/however/yet in opening
    alignment_bonus: 1   # names the topic (trusted publishing / malware) in line 1
    promise_bonus: 0     # no explicit promise yet
    narrative_flow_bonus: 0  # pure-fragment opener
    advisory_score: 9.4   # base=(9*.4 + 8*.4 + 7*.2)=8.0 + alignment=1 = 9.0... rounded
  variant_b:
    type: "stakes"
    opening_line: "TanStack just got hijacked in six minutes. And revoking the stolen token nukes your home folder."
    layers_present: [2, 3, 4, 5]
    source_fidelity:
      source_quote: "in just 6 minutes... over 100 packages... were compromised in a supply chain attack" + "the malware also installed a background process that would quietly check every 60 seconds whether your stolen GitHub token was still valid. The moment your token expires, it activates war crime mode and nukes your root directory."
      head_nouns: ["TanStack", "six minutes", "token", "home folder"]
      passes_gate: true
    curiosity_gap: 10
    stakes_clarity: 10
    specificity: 9
    stun_gun_bonus: 0.0  # "And" is not but/however/yet
    alignment_bonus: 1   # names TanStack + the threat in line 1
    promise_bonus: 0
    narrative_flow_bonus: 0  # two short sentences, no causal connector
    advisory_score: 10.0  # base=(10*.4 + 10*.4 + 9*.2)=9.8 + alignment=1 = capped at 10.0
  variant_c:
    type: "number"
    opening_line: "169 npm packages. 373 poisoned versions. Six minutes. One fork-PR did it all."
    layers_present: [3, 5]
    source_fidelity:
      source_quote: "by the next morning, security firm Aikido was tracking 373 poisoned versions across 169 packages" + "in just 6 minutes... over 100 packages... were compromised"
      head_nouns: ["packages", "versions", "minutes", "fork-PR"]
      passes_gate: true
    curiosity_gap: 7
    stakes_clarity: 7
    specificity: 10
    stun_gun_bonus: 0.0
    alignment_bonus: 1
    promise_bonus: 0
    narrative_flow_bonus: 0  # pure stat-cascade, no connector
    advisory_score: 8.6   # base=(7*.4 + 7*.4 + 10*.2)=7.6 + alignment=1 = 8.6
  recommended: "variant_b"
  rationale: |
    Variant B wins on Stop-The-Scroll (10/10 curiosity, 10/10 stakes — TanStack name-recognition + the visceral "nukes your home folder" stake). Variant A is also strong but doesn't surface the personal-stakes hook as hard. Variant C is pure stat-cascade — the brief explicitly warns this opener-style auto-rewards specificity but scores low on narrative flow. The user requested "hooking/catchy intro" — Variant B has the highest Stop-The-Scroll potential because the second sentence (token revocation → home folder wipe) is the visceral pivot a Fireship audience clicks for.
```

**Selected variant**: `variant_b`

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "ContrastPivot"
  selected_variant: "variant_b"

  visual_beats:
    - beat: "Thumbnail Hold (P0)"
      timing_s: [0, 6]
      visual: "Topic lockup visible at t=0. Top: terracotta-dotted brand pill 'NPM SUPPLY CHAIN'. Center: 'NPM JUST GOT HIJACKED' in Playfair 152px serif (warm-near-black), terracotta marker sweep under 'HIJACKED' from 0.2s. Below: '169 packages. 6 minutes.' in Inter 800 56px. Subtle ambient drift only — NO entrance animation; elements visible from frame zero."
      gsap_ease: "power3.out (marker sweep only)"
      sfx: null
    - beat: "Crossfade to Hook (P1 start)"
      timing_s: [6, 6.5]
      visual: "Blur-crossfade out P0; blur-crossfade in P1. Cream canvas stays — only foreground content swaps."
      gsap_ease: "power1.inOut"
      sfx: "cinematic-whoosh"
    - beat: "Context — 'TRUSTED PUBLISHING' kicker (P1)"
      timing_s: [6.5, 9]
      visual: "Mono kicker 'TRUSTED PUBLISHING' 36px indigo letter-spaced fades in. Below it, italic Playfair 'supposed to stop this.' 64px fades in 0.7s later. Indigo accent — measured tone."
      gsap_ease: "power3.out"
      sfx: "impact-slam"
    - beat: "PIVOT — 'BUT.' (P1 climax)"
      timing_s: [10, 11]
      visual: "Both prior lines blur+fade out (0.3s). 'BUT.' slams in: Playfair 700 240px terracotta, scale 0.85 → 1.0 with back.out(1.7), shadow lift. Screen-shake feel via 8px x-axis micro-tween."
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake + glitch-zap"
    - beat: "Reveal (P1 resolution)"
      timing_s: [11, 18]
      visual: "'BUT.' settles. Below it, 'Signed. SLSA-attested. STILL malware.' fades in line-by-line (1s per line). 'STILL' gets a marker-highlight sweep (gold, 0.6s) right when the narrator says it. Italic Playfair 56px."
      gsap_ease: "power3.out + power2.inOut for marker"
      sfx: "scale-slam on 'STILL' marker"
    - beat: "Hook closer (P1 tail)"
      timing_s: [18, 22]
      visual: "Narration: 'TanStack just got hijacked in six minutes. And revoking the stolen token nukes your home folder.' On 'six minutes' a small mono stopwatch chip appears in bottom-right (24px JetBrains Mono '00:06:00' in terracotta pill). On 'nukes your home folder' a tiny `$ rm -rf ~/` chip appears mirrored bottom-left in terracotta. Foreshadow — both reappear later."
      gsap_ease: "back.out(1.5)"
      sfx: "spring-pop x2 (one per chip)"
    - beat: "Crossfade to P2"
      timing_s: [22, 22.5]
      visual: "Blur-crossfade."
      gsap_ease: "power1.inOut"
      sfx: "cinematic-whoosh"

  pivot_word: "BUT"
  brand_reveal_word: "TanStack"  # name lands at ~18.5s, the cultural cult-hop anchor

  assets_needed:
    - type: "screenshot"
      description: "TanStack `bundle-size.yml` workflow file with `pull_request_target` line highlighted (P2)"
      source: "https://snyk.io/blog/tanstack-npm-packages-compromised/ — Snyk article has the verbatim YAML"
    - type: "screenshot"
      description: "Fake/recreated GitHub commit row showing `claude@users.noreply.github.com — chore: update dependencies — branch: fremen-sandworm` (P5)"
      source: "Recreated in HTML — StepSecurity article has the exact commit pattern"
    - type: "logo"
      description: "TanStack, Mistral AI, UiPath, OpenSearch, Guardrails AI, Squawk wordmarks for P4 step-reveal"
      source: "shared/logos/ — verify each one exists before composition build; fall back to text pills if missing"
    - type: "screenshot"
      description: "pnpm v11 release-notes page hero (P7 anchor — optional, can use text-only badges)"
      source: "https://pnpm.io/blog/releases/11.0"
    - type: "image"
      description: "Optional Dune sandworm silhouette for P0 background (deterministic SVG, NOT AI)"
      source: "Skip if shared/lib doesn't have one — text-only thumbnail still satisfies the 5-element rule"

  music_profile:
    hook_mood: NONE  # template forbids background music on Shorts
    note: "templates/shorts/standard/DESIGN.md §What NOT to Do — narration + SFX only"

  sfx_cues:
    - beat: "P0 thumbnail hold"
      cues: []  # silent open — narration enters immediately
    - beat: "P0 → P1 crossfade"
      cues: [cinematic-whoosh]
    - beat: "P1 context entrance ('TRUSTED PUBLISHING')"
      cues: [impact-slam]
    - beat: "P1 PIVOT 'BUT.'"
      cues: [impact-slam, screen-shake, glitch-zap]
    - beat: "P1 'STILL malware' marker"
      cues: [scale-slam]
    - beat: "P1 stopwatch + rm-rf chips"
      cues: [spring-pop]
    - beat: "Every scene crossfade (P1→P2, P2→P3, ..., P7→P8)"
      cues: [cinematic-whoosh]
    - beat: "P2 marker-highlight on `pull_request_target`"
      cues: [strike-cross]
    - beat: "P3 timeline row entrances"
      cues: [pop]  # per row, four rows
    - beat: "P4 counter slam at 169"
      cues: [scale-slam]
    - beat: "P4 company pill step-reveal"
      cues: [spring-pop]  # per pill, six pills (~5s apart in 24s — stretched safe within 0.25 vol cap on overlapping tracks)
    - beat: "P5 FORGED stamp slam"
      cues: [impact-slam, screen-shake]
    - beat: "P6 60s clock pulse climax"
      cues: [scale-slam]
    - beat: "P6 `$ rm -rf ~/` reveal"
      cues: [impact-slam, glitch-zap]
    - beat: "P7 each shield badge entrance"
      cues: [spring-pop]
    - beat: "P8 URL pill slam"
      cues: [scale-slam]
```

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "P1 (Hook)"
    setup_line: "And revoking the stolen token nukes your home folder."
    resolution_scene: "P6 (Dead-Man Switch)"
    resolution_line: "The token name? `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner`. It checks every 60 seconds."
    type: "tension"

  loop_openers:
    - scene: "P2"
      position: "opening"
      phrase: "Here's the smoking gun."
    - scene: "P5"
      position: "opening"
      phrase: "But the worm didn't stop at publishing."
    - scene: "P7"
      position: "opening"
      phrase: "So how do you stop this? The fix already shipped."

  secondary_loop:
    setup_scene: "P0 thumbnail receipt — '169 packages. 6 minutes.'"
    resolution_scene: "P4 counter slam 0→169"
    type: "promise"
```

## Story Lock Placement

- **Term Branding (Lock #1)**: Coined-term "trust boundary vs permissions boundary" — introduced in P1 closer, called back in P7 setup as the framing for why pnpm v11 works.
- **Loop Openers (Lock #5)**: P2 ("smoking gun"), P5 ("the worm didn't stop"), P7 ("the fix already shipped") — 3 explicit loop openers, cadence ~50s apart (matches the 60-90s rule for 180s videos).
- **Negative Frame (Lock #4)**: P5 — "`npm uninstall` does NOT uninstall the worm." Negative framing in a feature scene (post-hook), per the rule.
- **Thought Narration (Lock #3)**: P6 — narrator slips into first-person dread ("imagine you found this. You go to revoke the token. Click. Cursor blinks. And then your terminal scrolls.") to bridge the dead-man switch reveal.

Note: NO Negative Frames or Loop Openers placed in P1 hook itself — hook scope rule honored.

## Composition Layout

```yaml
composition_layout:
  model: sub-composition
  root_file: index.html
  scene_files:
    P0: compositions/scene-title.html       # forked to scene-thumbnail-open.html — see Notes
    P1: compositions/scene-marker.html      # forked to scene-hook-pivot.html — see Notes
    P2: compositions/scene-code-block.html
    P3: compositions/scene-timeline.html
    P4: compositions/scene-stat.html         # adapted: counter + step-reveal pill row
    P5: compositions/scene-image-card.html   # forked to scene-forged-commit.html
    P6: compositions/scene-marker.html       # forked to scene-deadman.html
    P7: compositions/scene-bullets.html      # 3-shield-card variant
    P8: compositions/scene-cta.html          # adapted: + debate question + thumbnail receipt
  notes: |
    The template ships 15 scene archetypes (title, stat, counter-grid, quote, bullets, compare, marker,
    badges, cta, chart, code-block, image-card, process-flow, timeline, typewriter). This plan reuses 8
    of them. P0 and P1 fork existing archetypes (title and marker) into video-specific copies so the
    thumbnail-grade frame requirements (no entrance at t=0, 5-element checklist) can be satisfied
    without breaking the bare template's scene library.
```

## Retention Component Picks

```yaml
retention_component_picks:
  P0_thumbnail_open:
    structural: "sub-composition"
    pattern: "hero-slam"   # but with NO entrance animation — elements visible at t=0
    primitives:
      - "marker-highlight on the word HIJACKED"   # max 1 marker, terracotta
    captions: null   # too short, narration enters at ~1.5s
    audio_reactive: null
    transition_out: "blur-crossfade"
    rationale: "First frame is the YouTube auto-thumbnail. Topic slam visible at t=0, no fade-in."

  P1_hook_pivot:
    structural: "sub-composition"
    pattern: "hero-slam"   # ContrastPivot pattern from the blueprint
    primitives:
      - "gsap-stagger-grid"   # kicker → italic claim entrance
      - "marker-highlight"    # on the word STILL in 'STILL malware'
    captions: null   # hook narration is too dense (155 WPM)
    audio_reactive: null
    transition_out: "blur-crossfade"

  P2_yaml_misconfig:
    structural: "sub-composition"
    pattern: "code-walkthrough"
    primitives:
      - "gsap-typewriter"      # subtle — only the highlighted line types in (the rest is static)
      - "marker-highlight"     # on `pull_request_target`
      - "marker-circle"        # on `ref: refs/pull/.../merge` (the second smoking-gun line)
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    rationale: "Two markers MAX. Both are on the YAML code text, NOT on a screenshot bar chart (rule honored)."

  P3_cache_poison_timeline:
    structural: "sub-composition"
    pattern: "timeline-cards"
    primitives:
      - "gsap-stagger-grid"   # four timeline rows, ~6s apart (Hour 0 / Hour 0 / Hour 8 / Hour 8)
      - "gsap-path-draw"      # SVG ink line connecting timeline rows
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  P4_worm_spreads:
    structural: "sub-composition"
    pattern: "stat-pill-row + narrated-stat-reveal"
    primitives:
      - "gsap-counter-tween"     # 0 → 169 on the central counter (1.4s, on narrator's '169')
      - "gsap-stagger-grid"      # six company pills entering one at a time (~3.5s apart in 24s — overline-headline takes the first 2s)
      - "marker-highlight"       # on '518M weekly downloads' supporting stat
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    rationale: "Step-by-step reveal rule honored: 6 companies entering one at a time over ~21s. Hidden-until-reveal pattern via explicit tl.set() at t=0 + tl.to() at narration-paced beats. NOT all bullets at once."

  P5_persistence_forged_commit:
    structural: "sub-composition"
    pattern: "image-card-style"
    primitives:
      - "gsap-stagger-grid"       # commit row enters, then 'FORGED' stamp slams
      - "marker-scribble"          # over the word 'uninstalled' to visualize 'this didn't work'
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"

  P6_deadman_switch:
    structural: "sub-composition"
    pattern: "hero-slam + custom clock pulse"
    primitives:
      - "gsap-counter-tween"       # 60 → 0 countdown clock (deterministic, no Math.random)
      - "marker-highlight"          # on the token name `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner`
      - "gsap-typewriter"           # `$ rm -rf ~/` types in at the climax
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    rationale: "Two markers MAX (counter is gsap, not marker)."

  P7_pnpm_defense:
    structural: "sub-composition"
    pattern: "bullets w/ shield-card variant"
    primitives:
      - "gsap-stagger-grid"   # three shield cards entering ~5s apart (~5s per card in a 22s phase = step-reveal)
      - "marker-highlight"     # on '24 hours' inside the first card (the killer stat)
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade"
    rationale: "Step-by-step reveal honored — three pnpm v11 defaults enter one at a time, NOT all at once."

  P8_thumbnail_close_cta:
    structural: "sub-composition"
    pattern: "cta-url-slam + thumbnail-grade close"
    primitives:
      - "gsap-stagger-grid"        # topic slam → outcome → debate-question → URL pill (within first 1.5s)
      - "marker-circle"             # around the URL pnpm.io/blog/releases/11.0
    captions: null
    audio_reactive: null
    transition_out: null   # final scene
    rationale: |
      Last frame is the loop-pause thumbnail. All elements settled by data_start+1.5s, then ≥1.5s of
      static hold. Topic 'PNPM V11 OR ROULETTE' is dominant 144px, debate-question 'Switching today —
      or waiting for the next worm?' on its own row (per engagement-cta.md), URL pill subordinate.
```

**Pick counts**:
- **Markers**: 7 marker primitives across 9 scenes (≤ 2 per scene rule honored — every scene either has 0 or 1-2 markers).
- **Captions**: 0 (hook + dense technical narration doesn't benefit; transcribe pass may add `caption-fade-slide` selectively in Phase 3.5).
- **Audio-reactive**: 0 (Shorts template forbids music + narration WPM is dense; reactive glow would compete with marker highlights).
- **Transitions**: 1 primary (`blur-crossfade`, used for all 8 scene changes) + 0 accents (consistency over flash — the warm-paper aesthetic rewards measured handoffs).

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "P0_thumbnail_open"
    data_start: 0
    data_duration: 6
    audio_anchor: "narration starts at ~1.2s with 'NPM just got hijacked.'"
  - scene: "P1_hook_pivot"
    data_start: 6
    data_duration: 16
    audio_anchor: "'TRUSTED PUBLISHING' visual at 6.5s ≈ word 'trusted'; PIVOT 'BUT.' at 10.0s ≈ word 'But'; 'STILL malware' marker at 14.5s ≈ word 'STILL'"
  - scene: "P2_yaml_misconfig"
    data_start: 22
    data_duration: 24
    audio_anchor: "code reveal at 23s; marker on `pull_request_target` at ~30s ≈ first utterance of the trigger name"
  - scene: "P3_cache_poison_timeline"
    data_start: 46
    data_duration: 26
    audio_anchor: "Hour 0 row at 48s; Hour 8 row + red glow at 65s ≈ 'eight hours later'"
  - scene: "P4_worm_spreads"
    data_start: 72
    data_duration: 24
    audio_anchor: "counter starts at 74s on '169', settles by 75.5s; first pill TanStack at 78s; final pill Squawk at ~93s"
  - scene: "P5_persistence_forged_commit"
    data_start: 96
    data_duration: 26
    audio_anchor: "fake commit row at 98s; FORGED stamp at ~107s ≈ 'forged'; marker-scribble on 'uninstalled' at ~115s"
  - scene: "P6_deadman_switch"
    data_start: 122
    data_duration: 22
    audio_anchor: "60s clock at 124s; token name marker at ~131s ≈ 'IfYouRevoke…'; `$ rm -rf ~/` typewriter at ~138s ≈ 'nukes your home folder'"
  - scene: "P7_pnpm_defense"
    data_start: 144
    data_duration: 22
    audio_anchor: "first shield card 'minimumReleaseAge' at 147s; second 'blockExoticSubdeps' at 152s; third 'approved-builds' at 158s — ~5s apart"
  - scene: "P8_thumbnail_close_cta"
    data_start: 166
    data_duration: 14
    audio_anchor: "topic slam at 166.5s; debate-question narration at 172s; URL spoken at 175s; ≥3s static hold to 180s"
total_data_duration: 180
```

**Phase 3.5 will refine these against `transcript.json` once TTS lands.** All `audio_anchor` values are PLACEHOLDERS at Phase 1.

**Visual pacing 5s audit (per `.claude/rules/visual-pacing-5s.md`)**:
- P0 (6s): one beat (marker sweep at 0.2s) — under 5s window, then crossfades out. PASS.
- P1 (16s): kicker 6.5s → italic claim 7.5s → PIVOT 10s → STILL marker 14.5s → stopwatch chip 18s → rm-rf chip 19.5s → exit 22s. Max gap = 4.5s (STILL marker → stopwatch chip). PASS.
- P2 (24s): code reveal 23s → pull_request_target marker 30s → ref:/merge marker-circle 36s → settle to exit 46s. Max gap 6s (36→exit) — VIOLATION. Mitigation: add a small ink-rule scribble at 41s connecting the two markers, OR add the supporting line "ALL fork PRs run with main-repo permissions" entering at 41s. Plan locks in the supporting-line option.
- P3 (26s): four timeline rows at 48, 56, 63, 69s → red glow pulse 71s → exit 72s. Max gap 8s (48→56 + 56→63). VIOLATION. Mitigation: tighten row spacing to 6s — rows at 48, 54, 60, 66s, then merge-trigger flash at 70s, exit 72s.
- P4 (24s): counter 74→75.5s → TanStack pill 78s → Mistral 81s → UiPath 84.5s → OpenSearch 87.5s → Guardrails 90.5s → Squawk 93s → exit 96s. Max gap ~3.5s. PASS.
- P5 (26s): commit row 98s → FORGED stamp 107s → scribble 'uninstalled' 115s → exit 122s. Max gap 9s (98→107). VIOLATION. Mitigation: add the `chore: update dependencies` text marker at 102s + a typewriter on the email at 105s. Refined: 98, 102, 105, 107, 110 (claude code hook callout), 115, 122.
- P6 (22s): countdown clock 124s → token name marker 131s → typewriter rm-rf 138s → settle 142, exit 144s. Max gap 7s (124→131). VIOLATION. Mitigation: have the clock pulse `scale 1.0→1.06→1.0` every 5s (124, 129) — that's not a content beat though. Real fix: add the narrator-paced "every 60 seconds" callout entering at 128s (sub-line under the clock). Refined: 124, 128, 131, 135 (40X error flash), 138, 142.
- P7 (22s): first shield 147s → second 152s → third 158s → settle/exit 166s. Max gap 8s (158→exit). VIOLATION. Mitigation: add a worm-icon-bounces-off-shield mini animation at 162s as a beat. Refined: 147, 152, 158, 162, 166.
- P8 (14s): topic slam 166.5s → outcome 167.5s → debate-Q 169s → URL pill 170s → marker-circle 172s → hold to 180s. Max gap from final beat to end is the held thumbnail (per shorts-thumbnail-frames.md, ≤2.5s relaxation applies). Hold from 172→180 is 8s — VIOLATION of the relaxation cap. Mitigation: shrink scene to 12s by trimming the hold OR add a subtle pulse on the URL marker at 176s. Plan locks in the pulse-at-176s option, hold from 176→180 is 4s which still exceeds 2.5s. Resolution: scene P8 reduced to 12s, total scene span becomes 166–178, then a 2s final hold to 180. Adjusted: `P8 data_duration: 12`, plus a trailing extension on `#root` to 180s via the standard `tl.set({}, {}, 180)` pattern.

**Updated final budget after pacing fixes**:

```yaml
final_data_timing_budget:
  - P0: { start: 0,    duration: 6 }
  - P1: { start: 6,    duration: 16 }
  - P2: { start: 22,   duration: 24 }   # supporting-line beat at 41s added
  - P3: { start: 46,   duration: 26 }   # timeline rows tightened to 6s apart
  - P4: { start: 72,   duration: 24 }
  - P5: { start: 96,   duration: 26 }   # commit row beats spaced ~3-5s
  - P6: { start: 122,  duration: 22 }   # extra "every 60 seconds" sub-line beat at 128s
  - P7: { start: 144,  duration: 22 }   # worm-bounces-off-shield beat at 162s
  - P8: { start: 166,  duration: 12 }   # tightened — held thumbnail 2s
total_data_duration: 178 + tl.set({}, {}, 180) = 180
```

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/shorts/standard/DESIGN.md"
  overrides: []   # ship with template defaults — warm-paper aesthetic is on-brand for a Fireship-style breakdown
  accent_assignment:
    P0: terracotta   # danger / hook
    P1: terracotta (PIVOT) + indigo (TRUSTED PUBLISHING kicker)
    P2: terracotta (markers) + ink (code background dark)
    P3: terracotta (cache-poisoned row) + sage (clean Hour 0 row)
    P4: terracotta (counter + danger pills) + warm-rose (supporting stats)
    P5: terracotta (FORGED stamp) + ink (commit row)
    P6: terracotta (clock + rm-rf) — solo lead, no second accent (cinematic dread)
    P7: sage (defense lead) + indigo (URL/CTA)
    P8: terracotta (URL pill) + indigo (subscribe pill / debate question)
  fonts:
    serif: "Playfair Display"   # var(--serif) — Hyperframes-mapped
    sans: "Inter"                # var(--sans)
    mono: "JetBrains Mono"       # var(--mono)
```

## AI Image Prompts

```yaml
images: []   # None needed — every visual uses scene archetypes + the YAML/commit/CSS screenshots in the screenshot inventory
```

## Screenshot Inventory

```yaml
screenshots:
  - name: "tanstack-bundle-size-yml"
    url: "https://snyk.io/blog/tanstack-npm-packages-compromised/"
    scene: "P2"
    color_scheme: "dark"
    usage: "Source code recreation — render the YAML as scene-code-block content (preferred over embedding the screenshot image, so we can highlight specific lines deterministically)"
    note: "We do NOT embed the Snyk screenshot directly. We recreate the YAML in scene-code-block.html and use marker-highlight + marker-circle on the two smoking-gun lines."
  - name: "forged-claude-commit-row"
    url: null
    scene: "P5"
    color_scheme: "dark"
    usage: "Recreated GitHub commit row — HTML + CSS in scene-image-card.html. Shows `claude@users.noreply.github.com — chore: update dependencies — branch: fremen-sandworm`. FORGED stamp overlay."
  - name: "pnpm-v11-release-notes"
    url: "https://pnpm.io/blog/releases/11.0"
    scene: "P7"
    color_scheme: "light"
    usage: "OPTIONAL. The 3 shield-card design carries the meaning. Only capture if the bare scene-bullets feels under-anchored at composition build."
    capture_command: "If used: npx hyperframes browser snapshot https://pnpm.io/blog/releases/11.0 --selector main --out assets/pnpm-v11-release.png"
```

## HyperFrames Blocks

```yaml
hyperframes_blocks_used: []   # No registry blocks needed; all 9 scenes use template archetypes
note: |
  Considered but rejected: vfx-shatter for P2 (the misconfig moment) and vfx-portal for P4 (the
  spread graph). Both add 10-20s WebGL warmup cost and the warm-paper editorial aesthetic is
  intentionally pixel-art-free. The marker-highlight / step-reveal vocabulary is on-brand and faster
  to render. If P5 'editor reopens' wants a flashier reveal, the registry has shader transitions
  (e.g., glitch) but defer to Phase 3.5 if it adds value — Phase 1 keeps the stack lean.
```

## Fact-Check Audit

Every claim in this plan that will appear on-screen or in narration is traced to a source.

| Claim | Source | Status |
|-------|--------|--------|
| 169 npm packages compromised | https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised | SOURCED |
| 373 poisoned versions | https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised | SOURCED |
| 6 minutes to compromise | https://www.youtube.com/watch?v=gwTQLZSIlsU (Fireship transcript verbatim) | SOURCED |
| 84 TanStack versions specifically | https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised | SOURCED |
| 518M weekly downloads (cumulative) | https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html | SOURCED |
| CVE-2026-45321 (CVSS 9.6 Critical) | https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html | SOURCED (mentioned only in P8 URL pill / description, not narration) |
| Companies hit: TanStack, Mistral AI, UiPath, OpenSearch, Guardrails AI, Squawk | https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised | SOURCED |
| `pull_request_target` misconfig in `bundle-size.yml` | https://snyk.io/blog/tanstack-npm-packages-compromised/ | SOURCED |
| `ref: refs/pull/${{ github.event.pull_request.number }}/merge` | https://snyk.io/blog/tanstack-npm-packages-compromised/ | SOURCED |
| 1.1 GB poisoned cache, 8-hour dwell | https://snyk.io/blog/tanstack-npm-packages-compromised/ | SOURCED |
| Dead-man switch polls every 60 seconds | https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised | SOURCED |
| Dead-man `rm -rf ~/` on 40X token error | https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised | SOURCED |
| Token name `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner` | https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html | SOURCED |
| Forged commits as `claude@users.noreply.github.com — chore: update dependencies` | https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem | SOURCED |
| Worm persists in Claude Code hooks + VS Code auto-run tasks | https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/ | SOURCED |
| pnpm v11 `minimumReleaseAge: 1440` default | https://pnpm.io/blog/releases/11.0 | SOURCED |
| pnpm v11 `blockExoticSubdeps: true` default | https://pnpm.io/blog/releases/11.0 | SOURCED |
| pnpm v11 approved-builds (replaces onlyBuiltDependencies) | https://pnpm.io/blog/releases/11.0 | SOURCED |
| Packages shipped with valid SLSA Level 3 provenance | https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised | SOURCED |
| Dune branch names (fremen, sandworm) | https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem | SOURCED |

**Claims REMOVED from plan (would have required unverified rephrase)**:
- "Anthropic was hacked" — REJECTED. Worm impersonates the `claude@users.noreply.github.com` email pattern; Anthropic was NOT compromised. P5 narration must be precise: "the worm SIGNS commits as Claude Code, blending in with real AI-generated commits."
- "First-ever SLSA-attested worm" — DOWNGRADED to "ships with valid SLSA Level 3 attestation" (BleepingComputer asserts it's first; Aikido is more conservative). Phase 2 narration uses the conservative phrasing.

**Claims REPHRASED for source fidelity**:
- "100+ packages in 6 minutes" (Fireship verbatim) vs. "169 packages by next morning" (Aikido). Plan uses BOTH: P0/P1 use "6 minutes" for the attack window (sourced from Fireship); P4 counter rolls to 169 for the final tally (sourced from Aikido). Narration MUST distinguish: "Within 6 minutes, the first wave hit. By morning, Aikido was tracking 169 packages."

**TTS heteronym audit (per `.claude/rules/tts-pronunciation.md`)**:
- "**live**" — NOT used in script (verb-sense "the worm sits live in cache" would be ambiguous → use "sits dormant" or "lives" rephrased). Plan flags this for Phase 2a.
- "**lead**" — NOT planned. If it surfaces in Phase 2 ("lead attacker", "lead package"), Phase 2a swaps to "primary attacker", "primary package".
- "**read**" — appears in "GitHub itself signs a statement saying which workflow is running" — not the heteronym; safe.
- "**close**" — appears in "closed the PR" — verb sense, unambiguous in context.
- "**record**" — N/A (no usage planned).
- **Tech terms (from brief §Technical Terms)**: `pnpm` → spell `P N P M`; `npm` → `N P M`; `SLSA` → `salsa`; `OIDC` → `O I D C`; `pull_request_target` → "the pull-request-target trigger"; `Aikido` → `eye-key-doh`; `UiPath` → `you-eye-path`; `Mistral` → `mis-trahl`; `Shai-Hulud` → `shy hu-lood`; `Tanstack` → `tan-stack`; `Sigstore` → `sig-store`; `tarball` → single word; CVE → `C V E 2026 dash 4-5-3-2-1`.

## Notes for Composition Build

1. **P0 first frame is the YouTube auto-thumbnail.** Per `.claude/rules/shorts-thumbnail-frames.md`, all 5 elements (topic ≥120px, visual anchor, brand chrome, outcome line, optional CTA) must be present and at full opacity at t=0. NO `tl.from()` on P0 elements — use `tl.set()` to position then a marker-only animation at t=0.2s.

2. **P8 last frame is the loop-pause thumbnail.** Same 5-element rule. The debate-question element (`#cta-question`) must persist visibly to t=180s. Plan reserves the final 2s for the held still.

3. **Step-by-step reveal (per `.claude/rules/step-by-step-reveal.md`) is mandatory in**:
   - P4 (six company pills entering ~3-3.5s apart)
   - P7 (three pnpm-v11 shield cards entering ~5s apart)
   Use the hidden-until-reveal pattern: `tl.set("#card-N", { y: 40, opacity: 0 }, 0)` + `tl.to("#card-N", { y: 0, opacity: 1, ... }, t_reveal)`. **NEVER** use `tl.from()` on a long timeline with seek points.

4. **Sub-composition wiring (per `.claude/rules/sub-composition-wiring.md`)** — every `data-composition-src` mount in the root needs:
   - `class="clip"`, `data-start`, `data-duration`, `data-track-index`, `data-width="1080"`, `data-height="1920"`
   - `data-composition-id` MUST match the child file's `<div id="root" data-composition-id="...">`
   Audit each mount in `index.html` against the matching scene file before declaring done. Studio silently bails on mismatch.

5. **Engagement CTA is REQUIRED in 3 places** (per `.claude/rules/engagement-cta.md`):
   - Spoken (final 3-5s of narration in `script.txt`): "Three pnpm v11 defaults blocked the entire chain. So — switching today, or waiting for the next worm?"
   - On-screen (`#cta-question` in P8, persists to t=180): "Switching today — or waiting for the next worm?"
   - YouTube description (closing paragraph): same question, paired with comments anchor.
   All three reference the same claim (pnpm v11 defaults blocked the chain). Polarizing + binary-answerable + specific to the video. Passes the 4 hard criteria.

6. **No background music** (Shorts hard rule). Narration + SFX only. All SFX volumes ≤ 0.25 per `.claude/rules/audio-design.md`; sonic-logo (if used) ≤ 0.45.

7. **Visual pacing 5s rule is tightly bound** in this plan — every scene's beat list is auditable from the YAML above. P3, P5, P6, P7 added extra beats to stay under 5s. P8 was shrunk to 12s to keep the held thumbnail ≤2.5s per the relaxation cap.

8. **TTS heteronym pre-flight** (Phase 2a) — grep `videos/npm-shai-hulud-worm-attack/script.txt` for the words flagged above before TTS. Single $0.30 API call per regen — well worth catching here.

9. **Defer to Phase 3.5** — final entrance timings rewrite against `transcript.json` word-anchors. The `audio_anchor` placeholders in §Data Timing Budget are reasonable narration-paced guesses but will drift ±1-2s once TTS lands.

10. **No vidiq run in Phase 1.** Title options exist in the brief; SEO keywords exist; vidiq validation happens in Phase YT (per orchestrator's `Skipped` note in the brief).

11. **Scene-archetype forks**: P0 (forked from scene-title), P1 (forked from scene-marker), P4 (scene-stat + step-reveal logic), P5 (scene-image-card + forged-stamp overlay), P6 (scene-marker + countdown clock), P8 (scene-cta + thumbnail-5-element overlay) — all need new internal `data-composition-id` strings (e.g., `scene-thumbnail-open`, `scene-hook-pivot`, `scene-worm-spread`, `scene-forged-commit`, `scene-deadman`, `scene-thumbnail-close`). Update both the child file's `<div id="root" data-composition-id="...">` AND the parent mount's `data-composition-id`.

12. **Connector words owned by Phase 2** — narration MUST land the planned connectors at scene boundaries (listed in §Narrative Arc). If Phase 2 drafts narration that breaks a scene transition into pure-fragments, Phase 2.5 Pass 6 will fail and the script will be regenerated. The connector plan is non-optional for `news-explainer` profile.

---

**Next step**: Run `/diy-yt-creator:phase2-script npm-shai-hulud-worm-attack`
