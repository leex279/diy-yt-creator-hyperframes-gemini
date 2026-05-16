# Composition Plan: openclaw-100-codex-fleet

## Director's Summary

A 9-minute news-explainer reaction to Peter Steinberger's "100 codex agents" X post (847.5K views). Curious-but-grounded narrator unpacks the thesis ("what if tokens don't matter?"), the 10 automation use cases, three custom OSS tools (clawsweeper / crabbox.sh / clawpatch.ai), and the community's split-camp reaction — with two locked Hostinger midrolls (1:30 and 5:00), a quick support-the-channel half-step at 8:15, and a debate-sparking CTA ("Would you let an AI agent log into your Telegram to make a PR demo?") on the final held frame. Crab-claw brand: deep crab-red over obsidian stage with paper-white text and cyan accent. Cinematic-fast intro, fragment-friendly mid-section, no slop adjectives — every claim traces to the brief's Section 5 verified-claims list.

---

## Template & Structure

- **Format**: long-form horizontal 1920×1080, 30fps
- **Base template**: `templates/long-form/standard/` (forked structure — sub-composition split per scene, root only orchestrates ambient + crossfades)
- **Composition layout model**: `sub-composition` (each of 13 scenes is its own `compositions/scene-NN-*.html` with its own paused timeline)
- **Voice profile**: `news-explainer` (curious-but-grounded; explanatory connectors mandatory at every scene boundary per Phase 2.5 Pass 6)
- **Tone**: cinematic-hooking fast-paced intro, curiosity-driven middle, debate-bait close
- **Total duration**: 540s (9:00 exactly)
- **Scene count**: 13 (incl. 2 Hostinger midrolls + 1 support-the-channel pillar + 1 dedicated CTA scene)
- **Design token overrides**: full crab/claw palette swap — see `## Visual Design Language` below
- **Background music**: enabled (3-segment: hook/body/cta on track 3 per long-form template; dipped to 0.04 across both midroll windows per `hostinger-midroll/recipe.md` step 6)
- **Captions**: synced word-level via `compositions/captions.html` (transcribe phase populates after TTS)

---

## Master Timeline

| # | Scene id | data_start | data_duration | End time | Archetype | Visual Goal | Key Elements |
|---|---|---|---|---|---|---|---|
| 01 | `scene-01-hook` | 0 | 25 | 0:25 | hook | Scroll-stop cold open | Topic slam "ONE DEV. 100 AI AGENTS. ZERO JUNIOR PR REVIEWERS." + tweet preview frame as receipt + crab logo lockup |
| 02 | `scene-02-thesis` | 25 | 30 | 0:55 | quote | Establish steipete's thesis | Quote-card with verbatim "How would we build software in the future if tokens don't matter?" + attribution chip "@steipete · OpenClaw · May 2026" + steipete avatar |
| 03 | `scene-03-avalanche` | 55 | 35 | 1:30 | list | Ticker reveal of all 10 use cases | 10 use-case cards in a 2×5 grid, fast-staggered entrance ~3s apart, with mini-icons (review / sweep / security / cluster / sandbox / vision-PR / spam / perf / meeting / split) |
| 04 | `scene-04-hostinger-midroll-1` | 90 | 20 | 1:50 | interstitial | First Hostinger midroll (BRAND-LOCKED) | Mounts `compositions/hostinger-midroll.html` (5-phase block, silent — narrator covers) |
| 05 | `scene-05-clawsweeper` | 110 | 60 | 2:50 | explainer | Tool 1 deep-dive | GitHub repo callout card + 4-lane architecture diagram (Review / Apply / Repair / Commit Review) + 0.1% close-rate stat slam + marker-backed-comment mechanic illustration |
| 06 | `scene-06-crabbox` | 170 | 75 | 4:05 | explainer | Tool 2 deep-dive (visual hero) | `brew install openclaw/tap/crabbox` mono-line + multi-cloud broker diagram (Cloudflare Worker → Hetzner / AWS / Azure / E2B) + side-by-side macOS / Linux / Windows VNC streaming demo frame + Telegram-PR-video conceptual frame |
| 07 | `scene-07-clawpatch` | 245 | 55 | 5:00 | explainer | Tool 3 deep-dive | Semantic-split diagram (Routes / Commands / Packages / CLI / Tests) + findings grid (bug / security / perf / docs-gap / test-gap / maintainability) with severity + confidence chips |
| 08 | `scene-08-hostinger-midroll-2` | 300 | 20 | 5:20 | interstitial | Second Hostinger midroll (BRAND-LOCKED) | Mounts `compositions/hostinger-midroll.html` (same block, second instance) |
| 09 | `scene-09-fleet-recap` | 320 | 35 | 5:55 | architecture | How the stack composes | Architecture-stack scene (5 horizontal accent layers): clawsweeper / crabbox / clawpatch / codex / deepsec → labelled "the ~100-agent fleet" |
| 10 | `scene-10-community-split` | 355 | 105 | 7:40 | list | 5 community camps (no names) | 5 bucket cards staggered (~18s apart): A "Lean? Really?" / B "Commodity soon" / C "Cheaper models?" / D "I have so much to learn" / E "What am I looking at?" — paraphrased only, no @-handles |
| 11 | `scene-11-cost-twist` | 460 | 35 | 8:15 | quote | The latency-not-cost reveal | Quote-card: "I could just disable fast mode and cut it down by 70%" — @steipete, 2026-05-16. Sub-line: "It's not cost. It's latency." Codex Speed docs URL chip beneath as receipt. |
| 12 | `scene-12-support` | 495 | 15 | 8:30 | interstitial | Support-the-channel pillar (friendly) | Inline-authored block (no registry source): subscribe icon + bell icon + like icon entering staggered, message "If this was useful — subscribe + drop a like. It's the cheapest way to support the channel.", deep-crab-red brand chrome (smaller scale than Hostinger midrolls — half-step, not full ad) |
| 13 | `scene-13-cta` | 510 | 30 | 9:00 | cta | Debate question + thumbnail-grade final frame | `#cta-question` persistent: "Would you let an AI agent log into your Telegram to make a PR demo?" + Yes/No/Hell No chips + subscribe pulse + final 5s held still (no motion) for thumbnail/loop |

**Total `data_duration`: 540s (9:00) ✓**  
**No gaps. No overlaps.** Every `data_start` of scene N+1 equals the `data_start + data_duration` of scene N.

---

## Narrative Arc (Kallaway breakdown)

- **Hook — Context Lean-In (0:00–0:55 ≈ 10%)** — s01 + s02. "One dev. 100 AI agents." Stakes (jobs). Then steipete's own framing ("tokens don't matter?") earns the right to continue. Self-selection point at ~4s.
- **Scroll-Stop Interjection** — built into s01 (the "zero junior PR reviewers" reversal at the end of the slam) and into s02's connector "But here's the thing he actually said…"
- **Contrarian Snapback** — s03 (the avalanche). The 10 use cases turn "100 codex agents" from abstract to concrete, which is unexpected — most viewers expected one big thing, not ten small things.
- **Solution (1:50–2:50 ≈ 11%)** — s05 (clawsweeper). First custom tool. Benefit-led: "the agent that closes 6-month-old issues automatically."
- **Deep Dive (2:50–5:55 ≈ 35%)** — s06 + s07 + s09. The three tools + how they compose.
- **Social Proof / Trust (5:55–7:40 ≈ 19%)** — s10 (5 community camps) + s11 (steipete's own follow-up). The community split IS the social proof — it's polarizing, which is honest.
- **Support pillar (8:15–8:30)** — s12. Friendly half-step before the hard CTA.
- **CTA (8:30–9:00 ≈ 6%)** — s13. Debate-sparking question + thumbnail-grade final frame.

**News-explainer connector plan** (one per scene transition, narration-level):

| Transition | Connector |
|---|---|
| s01 → s02 | "Because here's the question he's actually trying to answer…" |
| s02 → s03 | "And to do that, his team runs roughly ten automations at once…" |
| s03 → s04 | "Quick break — I've been running my own stuff on Hostinger…" *(Hostinger handoff)* |
| s04 → s05 | "Okay, back to the fleet — and the first custom tool…" |
| s05 → s06 | "But sweeping old issues is the easy part. The next tool is wild." |
| s06 → s07 | "So the sandbox runs the demo. The third tool reviews the code." |
| s07 → s08 | "Quick second break — same partner, different product…" *(Hostinger handoff)* |
| s08 → s09 | "Back in — and here's how all of it stacks together." |
| s09 → s10 | "Which is why the reaction split into roughly five camps." |
| s10 → s11 | "And then steipete himself dropped the line that re-frames everything." |
| s11 → s12 | "Before the question — one quick favor." *(Support handoff)* |
| s12 → s13 | "So here's the debate." |

---

## Hook Variants

```yaml
hook_variants:
  variant_a:
    type: "counterintuitive"
    opening_line: "One developer. A hundred AI agents reviewing every line of code he ships. Zero junior PR reviewers."
    layers_present: [1, 2, 3, 4, 5]
    source_fidelity:
      source_quote: "We constant run ~100 codex in the cloud, reviewing every PR, every issue."
      head_nouns: ["developer", "AI agents", "PR reviewers"]
      passes_gate: true
    advisory_score: 9.0
    notes: |
      Triple-threat aligned: visual slam ("ONE DEV. 100 AI AGENTS. ZERO JUNIOR PR REVIEWERS.")
      + spoken sentence + on-screen text all carry the same three numbers (1 / 100 / 0).
      Violent contrast: 1 vs 100 is a 100× gap; 100 vs 0 inverts expectation.
      One-question-loop: "How does one dev review every PR? He doesn't — 100 agents do."
      Lego-brick deconstruction: steipete's "100 codex" + "every PR, every issue" + the
      audience's implied "junior dev" role → these three pieces snap into the hook line.

  variant_b:
    type: "stakes"
    opening_line: "He's burning so many tokens that people are freaking out. And he says he could cut the bill by seventy percent — but he won't."
    layers_present: [2, 3, 4, 5]
    source_fidelity:
      source_quote: "People freaking out over my AI spend... I could just disable fast mode and cut it down by 70%"
      head_nouns: ["tokens", "bill", "percent"]
      passes_gate: true
    advisory_score: 8.2
    notes: |
      Strong stakes hook but spoils the s11 reveal (the 70% line is the cost-twist payoff).
      Reusing it as the cold open kneecaps the second half. Rejected for that reason
      even though the source-fidelity gate passes.

  variant_c:
    type: "number"
    opening_line: "A hundred AI agents. Three custom tools. One person calling it 'extremely lean'."
    layers_present: [1, 3, 4, 5]
    source_fidelity:
      source_quote: "All that automation allows us to run this project extremely lean."
      head_nouns: ["AI agents", "tools", "person"]
      passes_gate: true
    advisory_score: 8.5
    notes: |
      Number-anchor + community-pushback baked in (the air-quoted "lean").
      Slightly weaker than variant_a on Curiosity because the contrast is "many/few"
      where variant_a's contrast is "one / hundred / zero" — three numbers in
      three syllables. Strong backup if variant_a tests flat in preview.

  recommended: "variant_a"
```

**Locked variant: `variant_a` — first sentence: "One developer. A hundred AI agents reviewing every line of code he ships. Zero junior PR reviewers."**

Engagement-hooks-framework scoring (1-10):
- **Triple-threat alignment**: 10 — visual / text / spoken all carry the same 1/100/0 triplet.
- **Violent contrast**: 10 — 1 vs 100 is a 100× lean; 100 vs 0 inverts expectation; both reversals land in a single breath.
- **One-question-loop**: 9 — "How does one dev review every PR? He doesn't — 100 agents do" plants the loop in the listener's head within the first sentence, then s02 resolves it.
- **Lego-brick deconstruction**: 8 — three concrete bricks from the source (1 dev, 100 codex, every PR) snap together cleanly; the "zero junior PR reviewers" piece is inferred-but-true (steipete is solo on this part).

Total: 37/40. Strongest available variant. Backup is variant_c (35/40) if a more skeptical opener is wanted later.

---

## Cinematic Hook Blueprint

```yaml
cinematic_hook_blueprint:
  pattern: "StatCascade + FilmTrailer hybrid"
  selected_variant: "variant_a"

  visual_beats:
    - beat: "Cold Open — black + crab-red brand stinger"
      timing_s: [0, 2]
      visual: "Pure black canvas → 0.8s 'OPENCLAW' wordmark dim-glow + tiny crab-red claw mark in corner"
      gsap_ease: "power3.out"
      sfx: "sonic-logo (single, optional)"
    - beat: "Numeric slam #1 — ONE DEV."
      timing_s: [2, 5]
      visual: "'ONE DEV.' enters from below, 240px crab-red, single line, glyph-stagger"
      gsap_ease: "back.out(1.7)"
      sfx: "impact-slam"
    - beat: "Numeric slam #2 — 100 AI AGENTS."
      timing_s: [5, 9]
      visual: "Slam #1 shrinks to top, '100 AI AGENTS.' enters 280px paper-white"
      gsap_ease: "back.out(1.7)"
      sfx: "scale-slam"
    - beat: "PIVOT — ZERO JUNIOR PR REVIEWERS."
      timing_s: [9, 12]
      visual: "White flash + 'ZERO JUNIOR PR REVIEWERS.' 220px crab-red, both prior slams compress into a 3-stack header"
      gsap_ease: "back.out(1.7)"
      sfx: "LAYERED: impact-slam + screen-shake (own tracks)"
    - beat: "Receipt — tweet preview frame"
      timing_s: [12, 18]
      visual: "Three-stack header slides left, tweet preview card (steipete avatar + first ~80 chars of post + 847.5K views chip) slides in right"
      gsap_ease: "power4.out"
      sfx: "spring-pop"
    - beat: "Brand handoff — into thesis"
      timing_s: [18, 25]
      visual: "Tweet card blurs slightly, 'How would we build software if tokens don't matter?' question begins to fade in as preview to s02"
      gsap_ease: "sine.inOut"
      sfx: "cinematic-whoosh (transition to s02)"

  pivot_word: "Zero"
  brand_reveal_word: "OpenClaw"

  assets_needed:
    - type: "logo"
      description: "OpenClaw wordmark + small crab/claw glyph in crab-red"
      source: "TBD — to be designed in composition build (or fetched from openclaw repo if available)"
    - type: "screenshot"
      description: "Tweet preview frame — steipete avatar, post text (first ~80 chars), 847.5K views chip"
      source: "C:/Users/Leex279/Pictures/Screenpresso/2026-05-16_15h00_47.png (the brief's source screenshot)"
    - type: "portrait"
      description: "Steipete profile photo (small avatar) for tweet preview and s02 attribution"
      source: "TBD — public X profile photo"

  music_profile:
    hook_mood: "dramatic-cinematic"
    hook_bpm: [95, 105]
    body_bpm: [78, 90]
    cta_bpm: [108, 118]
    notes: |
      Long-form template supports 3-segment bg-music (hook / body / cta) on track 3.
      Hook bed: drone-led cinematic build, ducks under narration.
      Body bed: minimal pulse, -22 dB under voice.
      CTA bed: tempo lifts slightly for the debate question close.
      Both Hostinger midroll windows: bg-music dips to data-volume 0.04 (per
      hostinger-midroll/recipe.md step 6) so the silent midroll feels natural.
```

---

## Open Loop Architecture

```yaml
open_loop_architecture:
  primary_loop:
    setup_scene: "scene-01-hook"
    setup_line: "Zero junior PR reviewers."
    resolution_scene: "scene-11-cost-twist"
    resolution_line: "It's not cost. It's latency."
    type: "tension"
    notes: |
      The hook plants tension: how can one dev run 100 agents and call it lean?
      The community spends scenes 5-10 prosecuting that tension. Scene 11 resolves
      it by quoting steipete himself: the spend is a deliberate latency choice,
      not a constraint. That's the real answer — and it's the line most people
      missed in the original thread.

  loop_openers:
    - scene: "scene-02-thesis"
      position: "opening"
      phrase: "Here's the question he's actually trying to answer."
    - scene: "scene-05-clawsweeper"
      position: "opening"
      phrase: "And the first custom tool is wilder than it sounds."
    - scene: "scene-09-fleet-recap"
      position: "opening"
      phrase: "All of which stacks into one thing."
    - scene: "scene-11-cost-twist"
      position: "opening"
      phrase: "And then steipete dropped the line that re-frames everything."
```

---

## Story Lock Placement

- **scene-01-hook** — Numeric anchor (1 / 100 / 0). No Negative Frame (hook scope rule).
- **scene-02-thesis** — Term Branding: "tokens don't matter" is the coined frame. Use it again at s09 and s11.
- **scene-03-avalanche** — Loop opener via "ten automations, all running at once." Sets the bar for what "100 agents" buys you.
- **scene-05-clawsweeper** — Thought Narration after the 0.1% close-rate reveal: "Which sounds tiny — until you remember it never sleeps."
- **scene-06-crabbox** — Negative Frame: "Stop renting always-on VMs. Lease one, run a task, throw it away."
- **scene-07-clawpatch** — Term Branding reuse: "the semantic-unit split."
- **scene-09-fleet-recap** — Loop opener (mid-video re-anchor): "Three tools + Codex + deepsec = the fleet."
- **scene-10-community-split** — Polarizing tension (the bucket-A / bucket-B split IS the loop).
- **scene-11-cost-twist** — Primary loop resolution. Thought Narration: "It's not cost. It's latency."
- **scene-13-cta** — Debate-spark CTA (per `.claude/rules/engagement-cta.md`).

---

## Composition Layout

```yaml
composition_layout:
  model: "sub-composition"
  root_file: "videos/openclaw-100-codex-fleet/index.html"
  scene_files:
    - "compositions/scene-01-hook.html"
    - "compositions/scene-02-thesis.html"
    - "compositions/scene-03-avalanche.html"
    - "compositions/hostinger-midroll.html"        # copied from shared/lib/blocks, mounted twice
    - "compositions/scene-05-clawsweeper.html"
    - "compositions/scene-06-crabbox.html"
    - "compositions/scene-07-clawpatch.html"
    - "compositions/scene-09-fleet-recap.html"
    - "compositions/scene-10-community-split.html"
    - "compositions/scene-11-cost-twist.html"
    - "compositions/scene-12-support.html"
    - "compositions/scene-13-cta.html"
    - "compositions/captions.html"

  root_orchestration:
    - "ambient radial wash + 14 deterministic shape-backdrop (crab-themed silhouettes)"
    - "noise overlay (SVG fractalNoise, mix-blend-mode overlay, opacity 0.035)"
    - "top-banner-wordmark (OpenClaw + small crab-claw mark)"
    - "progress-bar (bottom edge, crab-red fill)"
    - "13 crossfades (scene N → scene N+1) at scene boundaries -0.4s"
    - "captions-wrap on track 9 (populated by transcribe phase)"
    - "narration audio on track 2 (full 540s)"
    - "3-segment bg-music on track 3 (hook 0-25, body 25-510 with midroll dips at 90-110 and 300-320, cta 510-540)"

  hostinger_midroll_mount_pattern: |
    Both Hostinger midrolls mount the SAME compositions/hostinger-midroll.html file
    (copied once from shared/lib/blocks/hostinger-midroll/block.html). They are
    two separate <div> mounts with different ids and different data-start values:

    <div id="hostinger-midroll-1-mount"
         data-composition-id="hostinger-midroll"
         data-composition-src="compositions/hostinger-midroll.html"
         data-start="90"
         data-duration="20"
         data-track-index="20"
         data-width="1920"
         data-height="1080"></div>

    <div id="hostinger-midroll-2-mount"
         data-composition-id="hostinger-midroll"
         data-composition-src="compositions/hostinger-midroll.html"
         data-start="300"
         data-duration="20"
         data-track-index="20"
         data-width="1920"
         data-height="1080"></div>

    Wiring rule per .claude/rules/sub-composition-wiring.md: parent
    data-composition-id MUST match the child file's <div id="root"
    data-composition-id="hostinger-midroll">. Both mounts share that id —
    that's correct, the framework re-instantiates the same sub-comp per mount.
```

---

## Retention Component Picks

```yaml
retention_component_picks:

  scene_01_hook:
    structural: "sub-composition"
    pattern: "StatCascade hero-slam (3 numeric slams + tweet receipt)"
    primitives:
      - "gsap-stagger-grid for 3-slam vertical stack"
      - "marker-highlight under 'ZERO' (single sweep, crab-red underline)"
      - "spring-pop entrance on tweet preview card"
    captions: null   # hook too dense for synced captions
    audio_reactive: null
    transition_out: "blur-crossfade (root-level, into s02)"

  scene_02_thesis:
    structural: "sub-composition"
    pattern: "quote-card (full-bleed, single sentence)"
    primitives:
      - "glyph-stagger reveal of the quote sentence"
      - "marker-highlight under 'tokens don't matter'"
      - "spring-pop on attribution chip"
    captions: "caption-fade-slide (synced word-level once transcript lands)"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_03_avalanche:
    structural: "sub-composition"
    pattern: "list-grid (2×5 use-case cards, ticker-fast reveal)"
    primitives:
      - "gsap-stagger-grid (10 cards, ~3s apart → 30s for 10 cards in a 35s phase)"
      - "tl.set hidden-until-reveal pattern (per .claude/rules/step-by-step-reveal.md)"
      - "mini-icon scale-pop per card"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_04_hostinger_midroll_1:
    structural: "sub-composition mount (BRAND-LOCKED block)"
    pattern: "hostinger-midroll (5-phase mutex inside the block: intro / web-hosting / vps / ai-builder / cta + outro fade)"
    primitives: "block-internal — DO NOT modify per .claude/rules/sub-composition-wiring.md + recipe slot table"
    captions: null   # block is silent + host narrator covers it
    audio_reactive: null
    transition_out: "block-internal fade-out (root opacity → 0 at DUR-0.7)"

  scene_05_clawsweeper:
    structural: "sub-composition"
    pattern: "explainer (GitHub repo callout + 4-lane diagram + stat slam)"
    primitives:
      - "gsap-stagger-grid for 4 lanes (Review / Apply / Repair / Commit Review)"
      - "gsap-counter-tween on 0.1% close-rate"
      - "marker-circle around the '4 closes / 3,478 scans' fraction"
      - "scale-pulse on the 'never closes maintainer items' safety chip"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_06_crabbox:
    structural: "sub-composition"
    pattern: "explainer (mono brew-line + multi-cloud broker diagram + VNC demo)"
    primitives:
      - "typewriter reveal of 'brew install openclaw/tap/crabbox'"
      - "gsap-path-draw on Cloudflare Worker → backend lines (Hetzner / AWS / Azure / E2B / Daytona / Blacksmith / Semaphore)"
      - "side-by-side reveal of 3 OS-VNC frames (macOS / Linux / Windows)"
      - "conceptual Telegram-PR-video card with phone-mockup chrome"
      - "marker-highlight on 'never holds cloud credentials'"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_07_clawpatch:
    structural: "sub-composition"
    pattern: "explainer (semantic-split diagram + findings grid)"
    primitives:
      - "gsap-stagger-grid for 5 unit types (Routes / Commands / Packages / CLI / Tests)"
      - "gsap-stagger-grid for findings grid (6 categories × severity chips)"
      - "scale-pulse on critical+high chips (subtle)"
      - "marker-highlight under 'categorized findings'"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_08_hostinger_midroll_2:
    structural: "sub-composition mount (BRAND-LOCKED block, second instance)"
    pattern: "hostinger-midroll (identical to scene_04 mount)"
    primitives: "block-internal — DO NOT modify"
    captions: null
    audio_reactive: null
    transition_out: "block-internal fade-out"

  scene_09_fleet_recap:
    structural: "sub-composition"
    pattern: "architecture-stack (5 horizontal accent-striped layers, top-down)"
    primitives:
      - "gsap-stagger-grid for 5 layers (clawsweeper / crabbox / clawpatch / codex / deepsec)"
      - "gsap-path-draw of bracket on the right labelled '~100-agent fleet'"
      - "marker-highlight under 'three thin, well-scoped tools' (the takeaway)"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_10_community_split:
    structural: "sub-composition"
    pattern: "list-grid (5 bucket cards, slow-staggered ~18s apart for 105s phase)"
    primitives:
      - "gsap-stagger-grid (5 cards, ~18s apart → fits 105s phase with 15s tail-hold per .claude/rules/visual-pacing-5s.md)"
      - "tl.set hidden-until-reveal pattern per card"
      - "per-card sub-beats every ~4s (icon scale-pulse, quote-line typewriter) to satisfy 5s visual-pacing rule inside long phase"
      - "marker-highlight under each card's tagline as it enters"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_11_cost_twist:
    structural: "sub-composition"
    pattern: "quote-card (steipete's follow-up reply + sub-line + receipt URL chip)"
    primitives:
      - "glyph-stagger reveal of 'I could just disable fast mode and cut it down by 70%'"
      - "scale-pulse on '70%' (single yoyo)"
      - "marker-highlight under 'It's not cost. It's latency.'"
      - "spring-pop on Codex Speed docs URL chip"
    captions: "caption-fade-slide"
    audio_reactive: null
    transition_out: "blur-crossfade"

  scene_12_support:
    structural: "sub-composition (inline-authored, NOT registry block)"
    pattern: "support-pillar (subscribe + bell + like icon triad + message + brand chrome)"
    primitives:
      - "gsap-stagger-grid for 3 icons (~0.5s apart)"
      - "spring-pop on each icon"
      - "marker-highlight under 'cheapest way to support the channel'"
    captions: null
    audio_reactive: null
    transition_out: "blur-crossfade (root-level into s13)"
    design_notes: |
      Author this fresh in compositions/scene-12-support.html mirroring the structural
      pattern of hostinger-midroll (root composition with paused timeline, single
      phase, fade-in / fade-out at start/end of its 15s window). BUT visually
      LIGHTER than the Hostinger midroll — smaller scale, shorter, no product cards,
      no Werbung badge (this is a creator pillar, not paid ad). Use crab-red brand
      chrome to feel native to the video, not interrupting it.

  scene_13_cta:
    structural: "sub-composition (built on top of templates/long-form/standard/compositions/scene-cta.html pattern)"
    pattern: "cta + thumbnail-grade final frame"
    primitives:
      - "marker-circle on the debate question"
      - "gsap-stagger-grid for Yes / No / Hell No chips"
      - "subscribe pulse (finite repeat count)"
      - "final 5s held still — ALL animations finish by data-start + 25s (i.e., absolute time 535s), then 5s frozen at the thumbnail composition"
    captions: "caption-fade-slide"
    audio_reactive: "audio-reactive-glow on subscribe pill (subtle, treble band) — only during the first 25s; cuts at 535s for the thumbnail freeze"
    transition_out: null   # final scene, no transition
    thumbnail_grade_frame_check: |
      Final 5s (t=535-540) MUST satisfy .claude/rules/shorts-thumbnail-frames.md
      adapted-for-long-form spirit. Required elements visible at t=535:
        1. Topic statement (dominant) — "100 AGENTS. ONE DEV." 160px crab-red
        2. Visual anchor — small claw-mark + tweet ghost
        3. Brand chrome — OpenClaw wordmark + channel mark
        4. Outcome receipt — "3 OSS tools + Codex + deepsec = the fleet"
        5. Debate question (#cta-question persistent) — "Would you let an AI agent
           log into your Telegram to make a PR demo?"
      Held still ≥1.5s (actually 5s) — no motion at all from t=535 to t=540.
```

**Constraints check**:
- Max 2 markers per scene → respected (no scene exceeds 2 marker-* primitives).
- Only one caption-* group visible at a time → respected (single `caption-fade-slide` per scene, captions-wrap on track 9 only).
- Primary transition picked: `blur-crossfade` (root-level, 12 of 12 scene transitions). Per template pattern.
- Anti-patterns: none invoked.

---

## Data Timing Budget

```yaml
data_timing_budget:
  - scene: "scene-01-hook"
    data_start: 0
    data_duration: 25
    audio_anchor: "narration begins at 0.5s (after sonic-logo); 'ONE DEV.' word at ~2.2s; 'ZERO' pivot word at ~9.5s"
  - scene: "scene-02-thesis"
    data_start: 25
    data_duration: 30
    audio_anchor: "quote begins at ~28s; 'tokens don't matter' phrase at ~35s"
  - scene: "scene-03-avalanche"
    data_start: 55
    data_duration: 35
    audio_anchor: "first use-case named at ~57s; cards enter ~3s apart paced to each name in narration"
  - scene: "scene-04-hostinger-midroll-1"
    data_start: 90
    data_duration: 20
    audio_anchor: "host narrator delivers sponsor read across full 20s (block is silent)"
  - scene: "scene-05-clawsweeper"
    data_start: 110
    data_duration: 60
    audio_anchor: "'clawsweeper' first spoken at ~112s; '0.1%' stat slam at ~145s"
  - scene: "scene-06-crabbox"
    data_start: 170
    data_duration: 75
    audio_anchor: "'crabbox' first spoken at ~172s; 'brew install' line at ~178s; Telegram demo callout at ~225s"
  - scene: "scene-07-clawpatch"
    data_start: 245
    data_duration: 55
    audio_anchor: "'clawpatch.ai' first spoken at ~247s; 'semantic units' phrase at ~265s"
  - scene: "scene-08-hostinger-midroll-2"
    data_start: 300
    data_duration: 20
    audio_anchor: "host narrator delivers second sponsor read across full 20s (block is silent)"
  - scene: "scene-09-fleet-recap"
    data_start: 320
    data_duration: 35
    audio_anchor: "'the fleet' phrase at ~325s; stack layers named ~5s apart"
  - scene: "scene-10-community-split"
    data_start: 355
    data_duration: 105
    audio_anchor: "'five camps' phrase at ~358s; each bucket label at ~18s spacing (Bucket A ~363s, B ~381s, C ~399s, D ~417s, E ~435s); tail-hold 435-460"
  - scene: "scene-11-cost-twist"
    data_start: 460
    data_duration: 35
    audio_anchor: "quote begins at ~463s; '70%' word at ~470s; 'it's latency' phrase at ~485s"
  - scene: "scene-12-support"
    data_start: 495
    data_duration: 15
    audio_anchor: "support read begins at ~497s; lasts ~12s; 3s tail-hold before s13 crossfade"
  - scene: "scene-13-cta"
    data_start: 510
    data_duration: 30
    audio_anchor: "debate question spoken at ~515-520s; final spoken word by ~533s; t=535-540 held silent for thumbnail-grade frame freeze"
total_data_duration: 540
```

`audio_anchor` values are PLACEHOLDERS — Phase 3.5 retention will refine them against `transcript.json` once TTS + transcribe have run.

---

## Banner Slot Table (explicit timings for both midrolls + support pillar)

| Slot id | Block source | data_start | data_duration | Mount selector | Notes |
|---|---|---|---|---|---|
| hostinger-midroll-1 | `shared/lib/blocks/hostinger-midroll/block.html` (copy to `videos/openclaw-100-codex-fleet/compositions/hostinger-midroll.html`) | **90** (1:30) | **20** | `#hostinger-midroll-1-mount` | After s03 (use-case avalanche). 20s silent block — host narrator delivers sponsor read. bg-music dips to 0.04 across 90-110. |
| hostinger-midroll-2 | same file (same composition mounted twice) | **300** (5:00) | **20** | `#hostinger-midroll-2-mount` | After s07 (third tool deep-dive). Same block. bg-music dips to 0.04 across 300-320. |
| support-the-channel | `videos/openclaw-100-codex-fleet/compositions/scene-12-support.html` (author inline — NOT a registry block, doesn't exist yet) | **495** (8:15) | **15** | `#scene-12-support-wrap` (standard sub-comp wrapper, not high-z mount) | Mirrors structural pattern of hostinger-midroll (paused timeline, fade-in/out) but visually lighter. Narrator delivers support read. No Werbung badge (creator pillar, not paid ad). |

**Track allocation**:
- Hostinger midroll mounts: track 20 (per recipe.md step 4)
- Support pillar: track 1 (standard scene-wrapper layer — it IS a scene, not an overlay)
- Narration: track 2 (full 540s, no gaps)
- bg-music: track 3 (segmented with midroll dips — see audio bed plan below)

---

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "videos/openclaw-100-codex-fleet/DESIGN.md (forked from templates/long-form/standard/DESIGN.md)"
  tokens_file: "videos/openclaw-100-codex-fleet/tokens/claw.css"

  palette:
    # Stage
    --bg:           "#0a0a0c"   # deep obsidian — darker than the standard template's navy
    --bg-elev-1:    "#13131a"
    --bg-elev-2:    "#1d1d27"
    # Text
    --text:         "#f5f1ea"   # paper-white (warm, not pure white)
    --text-dim:     "#a8a39a"   # muted paper
    --text-faint:   "#5a554d"
    # Brand accent — crab-red (the lead)
    --accent-1:     "#c92a2a"   # deep crab-red — primary brand
    --accent-1-hi:  "#e94545"   # crab-red hover/glow tier
    --accent-1-lo:  "#8c1d1d"   # crab-red shadow/depth
    # Secondary accent — cyan (cool counter-balance)
    --accent-2:     "#22d3ee"   # cyan — used for code chips, mono receipt URLs
    --accent-2-hi:  "#67e8f9"
    # Functional
    --accent-warn:  "#f59e0b"   # amber — for warnings, "REGRESSION" callouts
    --accent-ok:    "#10b981"   # green — for "SAFE TO CLOSE" sweeper chip
    --accent-stat:  "#fcd34d"   # warm yellow — for big stat slams

  typography:
    --sans:         "'Inter', system-ui, sans-serif"
    --mono:         "'JetBrains Mono', 'SF Mono', Consolas, monospace"
    --display:      "'Inter Display', 'Inter', system-ui, sans-serif"   # tighter tracking variant for slams
    # Long-form (1920×1080) sizes — NOT covered by shorts-typography.md
    --size-overline:        "28px"   # SECTION LABELS
    --size-body:            "32px"
    --size-card-title:      "56px"
    --size-card-descriptor: "30px"
    --size-headline:        "100px"  # scene-level headlines
    --size-quote:           "84px"   # quote-card body
    --size-stat-slam:       "200px"  # the big 100 / 70% numbers
    --size-hero-slam:       "240px"  # ONE DEV. / 100 AI AGENTS. / ZERO

  motion_signature:
    # Crab-claw "snap" feel — slightly aggressive overshoot on entrances
    primary_ease:    "back.out(1.7)"   # for slams, pivot words, card entrances
    secondary_ease:  "power3.out"      # for grounded title cards, sub-lines
    soft_ease:       "sine.inOut"      # for ambient breath, fades
    snap_cubic:      "cubic-bezier(.6,.05,.3,1.2)"  # custom claw-snap for one-off accents
    crossfade_dur:   "1.1s"            # root-level scene crossfades (matches standard template)
    stagger_card:    "0.12s"           # stagger between cards in a grid
    stagger_glyph:   "0.04s"           # per-letter on quote reveals

  shape_backdrop:
    # 14 deterministic crab-themed silhouettes scattered, 0.045 opacity, slow drift
    shapes:
      - "assets/shapes/claw-1.svg"     # asymmetric claw silhouette
      - "assets/shapes/claw-2.svg"     # crab-shell hex outline
      - "assets/shapes/circuit-trace.svg"   # subtle circuit-board nod (codex = chips)
    drift: "x±60px, y±60px, rotation±8deg, sine.inOut yoyo, 12s period"

  overrides_from_standard_template:
    - css_var: "--bg"
      original: "#0a0e1a (navy)"
      override: "#0a0a0c (obsidian)"
      reason: "Crab-red is intensely warm — pure navy clashes; obsidian is the closer cool-warm balance"
    - css_var: "--accent-1"
      original: "#3b82f6 (blue)"
      override: "#c92a2a (crab-red)"
      reason: "Brand lock — crab/claw identity"
    - css_var: "--accent-2"
      original: "#8b5cf6 (purple)"
      override: "#22d3ee (cyan)"
      reason: "Cool counter to the warm crab-red; reads as 'code / technical'"
    - css_var: "--accent-3 / --accent-4"
      original: "two extra rotating accents (yellow + mint)"
      override: "DROPPED — palette is now duotone-with-functional (warn / ok / stat as functional only)"
      reason: "Crab brand wants identity dominance; 4-accent rotation dilutes it"

  fonts:
    sans: "Inter"
    mono: "JetBrains Mono"
    display: "Inter Display (or Inter w/ -2% tracking and 900 weight)"
```

---

## AI Image Prompts

```yaml
images:
  - scene: "scene-01-hook (cold-open brand stinger)"
    name: "openclaw-claw-mark"
    prompt: "Minimalist asymmetric crab claw silhouette, deep crab-red (#c92a2a) on pure black background, slight subsurface glow, vector-clean edges, no text, square 1:1 composition"
    aspect_ratio: "1:1"
    usage: "Cold-open brand stinger + persistent corner mark + final-frame anchor"
    fallback: "Hand-author as an SVG if AI image fails — simple geometric claw is achievable"
  - scene: "scene-06-crabbox"
    name: "crab-sandbox-conceptual"
    prompt: "Three minimalist computer windows floating in dark void, each containing a different OS chrome (macOS / Linux / Windows), connected by glowing crab-red cable lines to a central glowing orb labeled with a tiny crab silhouette. Cinematic depth, slight tilt-shift, deep obsidian background"
    aspect_ratio: "16:9"
    usage: "Background hero for the multi-cloud broker section of s06"
  - scene: "scene-09-fleet-recap"
    name: "fleet-architecture-bg"
    prompt: "Five horizontal glowing strata stacked top-to-bottom on deep obsidian background, each stratum a different cool/warm gradient, with faint dotted lines connecting them. Cinematic, minimalist, no text, slight noise grain"
    aspect_ratio: "16:9"
    usage: "Background layer for architecture-stack scene"
```

Generated in composition build phase. Drop into `videos/openclaw-100-codex-fleet/assets/`.

---

## Screenshot Inventory

```yaml
screenshots:
  - name: "tweet-preview"
    source: "C:/Users/Leex279/Pictures/Screenpresso/2026-05-16_15h00_47.png"
    scene: "scene-01-hook + scene-13-cta (ghost reuse)"
    color_scheme: "n/a (existing capture)"
    usage: "Tweet preview card as the cold-open receipt; ghost reuse in final-frame anchor"
    action: "Copy from source path to videos/openclaw-100-codex-fleet/assets/screenshots/tweet-preview.png; may need crop to 16:9 and resize to ≤3840×2160 per hyperframes-pitfalls.md §2"
  - name: "clawsweeper-repo"
    url: "https://github.com/openclaw/clawsweeper"
    scene: "scene-05-clawsweeper"
    color_scheme: "dark"
    usage: "GitHub repo hero — readme above-fold"
  - name: "clawsweeper-site"
    url: "https://clawsweeper.bot/"
    scene: "scene-05-clawsweeper"
    color_scheme: "dark"
    usage: "Marketing site frame for the 4-lane illustration"
  - name: "crabbox-home"
    url: "https://crabbox.sh/"
    scene: "scene-06-crabbox"
    color_scheme: "dark"
    usage: "Tagline 'A short-lived box for every run.' frame"
  - name: "clawpatch-home"
    url: "https://clawpatch.ai"
    scene: "scene-07-clawpatch"
    color_scheme: "dark"
    usage: "Site hero for the semantic-split context"
  - name: "deepsec-blog"
    url: "https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base"
    scene: "scene-09-fleet-recap"
    color_scheme: "dark"
    usage: "Small inline chip showing deepsec is real, released ~2 weeks before steipete's post"
  - name: "codex-speed-docs"
    url: "https://developers.openai.com/codex/speed"
    scene: "scene-11-cost-twist"
    color_scheme: "dark"
    usage: "Receipt URL chip under the 'fast mode' quote — proves fast mode is a real Codex tier"
  # Hostinger midroll screenshots — already in shared/screenshots/hostinger/
  # See compositions/hostinger-midroll.html for paths (block-internal)
```

Capture in composition build phase (NOT here in Phase 1). Use `/agent-browser` skill.

---

## HyperFrames Blocks

```yaml
hyperframes_blocks_used:
  - name: "hostinger-midroll"
    source: "shared/lib/blocks/hostinger-midroll/block.html"
    install_method: "copy (NOT 'hyperframes add' — it's a shared/lib/ block, not a registry block)"
    install_command: |
      # Copy block file
      cp shared/lib/blocks/hostinger-midroll/block.html \
         videos/openclaw-100-codex-fleet/compositions/hostinger-midroll.html

      # Copy required static assets per recipe.md step 2
      cp shared/logos/hostinger-brand/Hostinger_Horizontal_White.svg \
         videos/openclaw-100-codex-fleet/assets/hostinger-horizontal-white.svg
      mkdir -p videos/openclaw-100-codex-fleet/assets/hostinger-screens
      cp shared/screenshots/hostinger/web-hosting.png \
         videos/openclaw-100-codex-fleet/assets/hostinger-screens/web-hosting.png
      cp shared/screenshots/hostinger/vps-hosting.png \
         videos/openclaw-100-codex-fleet/assets/hostinger-screens/vps-hosting.png
      cp shared/screenshots/hostinger/ai-website-builder.png \
         videos/openclaw-100-codex-fleet/assets/hostinger-screens/ai-website-builder.png
    mount_count: 2   # mounted twice (s04 + s08), same file, two <div> mounts
    why: "Two locked Hostinger midrolls per spec; brand-locked block forbids per-video edits"
    constraints:
      - "DO NOT change phase boundaries piecemeal (per recipe.md Don'ts)"
      - "DO NOT shorten data-duration below 20s"
      - "DO NOT extend past 20s"
      - "DO NOT add narration to the block (silent by design)"
      - "DO NOT write 'Sponsored by Hostinger' — affiliate-only, headline stays 'Try Hostinger'"
      - "DO NOT remove Werbung badge (DE UWG ad-disclosure compliance)"
```

The custom support-pillar scene at s12 is NOT a registry block — it's authored fresh in this video. See `## Retention Component Picks` → `scene_12_support.design_notes`.

---

## Engagement Debate Question (LOCKED)

Per `.claude/rules/engagement-cta.md`: the question lives in THREE places that all agree:

**Locked question (from research brief Section 7 winner)**:

> **"Would you let an AI agent log into your Telegram to make a PR demo?"**

| Place | Where | When | Wording |
|---|---|---|---|
| 1. Spoken | `videos/openclaw-100-codex-fleet/scripts/scene-13-cta.txt` (final scene of `scripts/full-script.md`) | Spoken at ~t=515-520s | "So here's the question — would you let an AI agent log into your Telegram to make a PR demo? Yes, no, or hell no — drop your verdict below." |
| 2. Visual | `videos/openclaw-100-codex-fleet/compositions/scene-13-cta.html` → `#cta-question` element | Enters at scene-internal t=2.5s (absolute 512.5s); persists through final-frame freeze t=535-540 | "Would you let an AI agent log into your Telegram to make a PR demo?" |
| 3. Description | `videos/openclaw-100-codex-fleet/youtube-description.md` (Phase YT) | Closing paragraph | "Would you let an AI agent log into your Telegram to make a PR demo? Drop your verdict — yes, no, or hell no — in the comments." |

**HARD criteria check** (per `engagement-cta.md`):

- ✅ **Binary / short-list answerable** — "yes / no / hell no" (3-item short list, every viewer can answer in <2s)
- ✅ **Polarizing stance** — security/trust hot button; ~half the audience will be "absolutely not", the other half will be "show me the recording"
- ✅ **References a specific claim** — use case 5 from the brief (the crabbox + Telegram demo), the most-shareable concrete claim
- ✅ **Low cost to answer** — no domain expertise needed; gut reaction sufficient

**Backup** (per brief Section 7): Candidate 1 `"100 agents on one codebase — the future, or just a flex?"` if the trust-axis question tests flat.

---

## Fact-Check Audit

Every claim that will appear in the script (per brief Section 5) traced to source:

| # | Claim | Source | Status |
|---|---|---|---|
| 1 | ~100 codex agents running continuously in cloud, reviewing every PR + every issue | Source post (X) verbatim quote line 4 of the post | ✅ verbatim — quote-able |
| 2 | clawsweeper finds 6-month-old fixed issues, closes with exact reference | Source post verbatim line 4-5 + [github.com/openclaw/clawsweeper README](https://github.com/openclaw/clawsweeper/blob/main/README.md) | ✅ verbatim + tool docs |
| 3 | 0.1% close rate — ~4 closes per 3,478 scans in one reference week | [github.com/openclaw/clawsweeper README](https://github.com/openclaw/clawsweeper/blob/main/README.md) | ✅ self-reported in repo README |
| 4 | clawsweeper 4 lanes — Review / Apply / Repair / Commit Review | [github.com/openclaw/clawsweeper README](https://github.com/openclaw/clawsweeper/blob/main/README.md) | ✅ |
| 5 | clawsweeper uses GPT-5.5 at high reasoning | [github.com/openclaw/clawsweeper README](https://github.com/openclaw/clawsweeper/blob/main/README.md) | ✅ |
| 6 | clawsweeper never closes maintainer-authored items | [github.com/openclaw/clawsweeper README](https://github.com/openclaw/clawsweeper/blob/main/README.md) | ✅ |
| 7 | crabbox.sh: brew install openclaw/tap/crabbox | [crabbox.sh](https://crabbox.sh/) | ✅ |
| 8 | crabbox.sh: Cloudflare Worker brokers credentials, CLI carries only bearer token | [crabbox.sh](https://crabbox.sh/) | ✅ |
| 9 | crabbox.sh backends: Hetzner / AWS / Azure (brokered) + E2B / Daytona / Blacksmith / Semaphore (delegated) + BYO SSH | [crabbox.sh](https://crabbox.sh/) | ✅ |
| 10 | crabbox.sh OSes: Linux / macOS (EC2 Mac) / Windows (AWS or Azure) with VNC | [crabbox.sh](https://crabbox.sh/) | ✅ |
| 11 | Agent uses crabbox to log into Telegram, record demo, post to PR | Source post verbatim | ✅ verbatim |
| 12 | clawpatch.ai splits projects into Routes / Commands / Packages / CLI / Tests | [clawpatch.ai](https://clawpatch.ai) | ✅ |
| 13 | clawpatch findings categorized: bug / security / perf / docs-gap / test-gap / maintainability with severity + confidence | [clawpatch.ai](https://clawpatch.ai) | ✅ |
| 14 | clawpatch is MIT, "Made with care by the OpenClaw team" | [clawpatch.ai](https://clawpatch.ai) | ✅ |
| 15 | All 3 tools are open-source, MIT, owned by OpenClaw team, built on Codex | Brief Section 3 synthesis (verified against each tool's repo/site) | ✅ |
| 16 | Vercel deepsec released ~2 weeks before steipete's post (early May 2026) | [vercel.com/blog/introducing-deepsec...](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base) | ✅ |
| 17 | Codex "fast mode" = 1.5× speed tier with higher credit consumption | [developers.openai.com/codex/speed](https://developers.openai.com/codex/speed) | ✅ |
| 18 | "I could just disable fast mode and cut it down by 70%" — steipete reply | Source clipping + brief Section 1 | ✅ verbatim — quote-able WITH attribution |
| 19 | "Codex Security" — likely steipete's shorthand for Codex configured for security, NOT a discrete product | Brief Section 4 + Section 6 risk note | ⚠️ FRAME AS AMBIGUOUS in script — "Codex configured for security, possibly what he calls 'Codex Security'" |
| 20 | Steipete's bio details (PSPDFKit exit, joined OpenAI Feb 2026) | [Wikipedia: Peter Steinberger (programmer)](https://en.wikipedia.org/wiki/Peter_Steinberger_(programmer)) | ✅ — but the video does NOT lean on biography; only "Peter Steinberger, builder of OpenClaw" attribution is needed |
| 21 | OpenClaw is Steipete's open-source personal AI assistant, 372K+ stars | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) | ✅ |
| 22 | Source post has 847.5K views | Source screenshot 2026-05-16_15h00_47.png | ✅ — visible in screenshot |
| 23 | "the community split into roughly five camps" framing (no names, no @-handles) | Brief Section 2 explicit framing rule | ✅ — bucket descriptions are paraphrased, NOT direct quotes; NO handles will appear on screen or in narration |
| 24 | Bucket A: cynical-deadpan "Lean? Really?" | Brief Section 2 synthesis | ✅ paraphrase only — no direct attribution |
| 25 | Bucket B: forward-looking "commodity soon" — steipete agreed | Brief Section 2 + steipete's checkmark reply | ✅ paraphrase + the agreement is observable |
| 26 | Bucket C: cost-optimization probing (Cerebras / Grok / Qwen mentions) | Brief Section 2 | ✅ paraphrase, no @-handles |
| 27 | Bucket D: admiring / "I have so much to learn" | Brief Section 2 | ✅ paraphrase |
| 28 | Bucket E: confused / "what am I looking at" | Brief Section 2 | ✅ paraphrase |

**Removed / NOT in script** (per brief Section 6 Risks):

| Claim that would have been tempting | Why removed |
|---|---|
| Specific $ amount of steipete's AI spend | Never disclosed — brief Section 6 forbids speculation |
| "Codex Security" as a distinct product | Brief Section 4 + 6 — frame as ambiguous, not as a product line |
| "Everyone will be doing this in 2026" | Brief Section 6 — bucket B is a *prediction*, not current state |
| Any @-handle from the reply threads | Brief Section 2 + 6 — no names, no handles, only paraphrased camp descriptions |
| Snark about steipete personally | Brief Section 6 — tone is curious admiration + healthy skepticism |
| "Your job is over" / "you'll be replaced" | Brief Section 6 — takeaway is "build small scoped tools", not "AI will replace you" |
| Slop adjectives (groundbreaking, revolutionary, game-changing) | Brief Section 6 — no hype, use receipts |

Phase 2b will re-verify every Yes/✅ row above against the live URL (the brief notes URLs were verified 2026-05-16; Phase 2b confirms they're still live at script-write time).

---

## Notes for Composition Build

For whoever picks this up in Phase 4 (composition build) — read CLAUDE.md "Building New Templates" workflow, but you are NOT building a template, you are spawning from `templates/long-form/standard/`:

1. **Token swap first** — rewrite `videos/openclaw-100-codex-fleet/tokens/long-form.css` (or add `tokens/claw.css` and update `index.html` `<link>` to point at it) with the full crab palette from `## Visual Design Language` above. Re-validate WCAG contrast after — crab-red `#c92a2a` on `#0a0a0c` obsidian is ~6.3:1 contrast which passes AA for large text but should be double-checked for body sizes.
2. **Shape backdrop** — replace the 3 generic shapes in `assets/shapes/` with claw / crab-shell / circuit-trace silhouettes. Keep the deterministic seeded scatter; just swap the source SVGs.
3. **Hostinger midroll wiring** — follow `shared/lib/blocks/hostinger-midroll/recipe.md` steps 1-7 EXACTLY, mounting twice (data-start 90 + 300). Add the mount CSS per step 5 to `index.html`'s `<style>` block. Verify bg-music dips at 90-110 and 300-320 per step 6.
4. **Support pillar (s12)** — author fresh. Mirror hostinger-midroll's structural pattern (paused timeline, single phase, fade-in/out) but ~half the visual weight. NO Werbung badge. NO product cards. Just the icon triad + message + crab-red brand chrome.
5. **Scene 13 thumbnail-grade final frame** — ALL animations finish by absolute t=535s (scene-internal t=25s). The last 5s (535-540) are completely frozen — no scale yoyos, no glow pulses, no marker sweeps, nothing. The frozen frame is what YouTube auto-picks if no thumbnail is uploaded and what gets screenshotted/shared.
6. **Visual-pacing-5s sweep** — for every scene, especially s06 (75s), s07 (55s), s09 (35s), s10 (105s), audit gaps between visible content changes. s10 has the longest phase and the highest risk — plan 5 bucket card entrances ~18s apart, AND mid-card sub-beats every ~4s (icon scale-pulse, quote-line typewriter for each card's tagline) to keep the eye locked. See `.claude/rules/visual-pacing-5s.md`.
7. **Step-by-step reveal** — use the explicit `tl.set` hidden-until-reveal pattern (per `.claude/rules/step-by-step-reveal.md`) for s03 (10 use-case cards), s05 (4 lanes), s07 (5 unit types + 6 findings cards), s09 (5 layers), s10 (5 buckets). NEVER `tl.from()` for these — always `tl.set` at t=0 then `tl.to` at the reveal time.
8. **TTS heteronym audit** (per `.claude/rules/tts-pronunciation.md`) — flag these words in Phase 2a:
   - `live` (in "live on the platform", "we live-build") → swap to `running` / `available`
   - `lead` (in "lead agent") → swap to `primary agent` / `coordinator agent`
   - Tech terms: `nginx` → `engine-x`, `OAuth` → `O auth`, `CI/CD` → `C I C D`, `npm` → `N P M`
   - `crabbox` — pronounce as "crab-box" (two words). Add to Phase 2a per-scene `.txt` if engine consistently mispronounces.
   - `clawpatch` — pronounce as "claw-patch" (compound). Same.
   - `deepsec` — pronounce as "deep-sec" (compound).
   - `codex` — pronounce as "co-decks" (engine should handle).
9. **Engagement CTA triple-check** — verify scene-13 narration, on-screen `#cta-question`, and `youtube-description.md` closing paragraph all carry the EXACT SAME question text (per `.claude/rules/engagement-cta.md`).
10. **Composition duration extender** — last line of root `<script>` block MUST be `tl.set({}, {}, 540);` to pin the timeline at the full 540s duration (per `.claude/rules/hyperframes-pitfalls.md` §1).
11. **Crossfade chain** — 12 crossfades total (s01→s02, s02→s03, s03→s04, s04→s05, s05→s06, s06→s07, s07→s08, s08→s09, s09→s10, s10→s11, s11→s12, s12→s13). All at `<next-label> - 0.4` per standard template pattern.
12. **Captions** — leave `compositions/captions.html` empty until transcribe phase. Then `npx hyperframes transcribe` populates word-level data.
13. **Lint after every scene** — `npx hyperframes lint videos/openclaw-100-codex-fleet` after building each scene. NEVER batch-build all 13 then lint — a wiring bug in s03 cascades into a "no scene loads" mystery in scrubbing.
14. **Render with `--docker`** for final delivery (per `.claude/rules/hyperframes-pitfalls.md` §5) to match preview byte-for-byte.

---

## Next Step

Run `/diy-yt-creator:phase2-script openclaw-100-codex-fleet` to draft the narration script from this plan. Then `/diy-yt-creator:phase2-5-critique`, then `/diy-yt-creator:phase2a-tts-script`, then `/diy-yt-creator:phase2b-factcheck`.
