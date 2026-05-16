# Orchestration Log: anthropic-amazon-compute

Pipeline started: 2026-04-27
Topic: Anthropic × Amazon compute announcement (https://www.anthropic.com/news/anthropic-amazon-compute)
Template: shorts/anthropic (user-confirmed; suggested by orchestrator — Anthropic announcement URL, no duration hint, dark-stage aesthetic fit)
Duration: 45s

## Phase Summaries (<200 words each)

### Phase 0 — Research (2026-04-27)
**Depth**: STANDARD (upgraded from LIGHT — fresh April 2026 announcement, $100B stakes warrant deeper research). 1 primary WebFetch + 5 supplementary web searches + 1 secondary WebFetch.

**Agent findings** (executed inline as 4 research lanes):
- **A (Core)**: $100B / 10-yr commitment, 5 GW capacity, 1M+ Trainium2 chips deployed, 100,000+ orgs on Bedrock. Pfizer −55% infra cost, Lyft 87% faster.
- **B (Competitive)**: Stargate ($500B aspirational, execution friction) vs Rainier (running today). Anthropic at $30B run-rate just passed OpenAI's $25B. Trainium ~$1/hr vs H100 ~$3/hr.
- **C (Hooks)**: Strong contrarian angle — "Anthropic's biggest threat was its own success" (April 2026 rate limits + quality-decline backlash). Cult-hops: NYC (5GW scale), Nvidia, Costco-Kirkland metaphor.
- **D (Visual)**: 7 visual concepts incl. power-meter-to-NYC sweep, chip-swap morph (H100 → Trainium2 + price flip), Project Rainier Indiana reveal, three-cloud diagram. 8-scene structure mapped to 45s.

**vidiq**: USED. 8 keywords captured; 3 title scores (top: "Anthropic Just Bet $100B on Amazon Chips" = 84/100). `vidiq_trending_videos` errored transiently — non-blocking.

**Quality gates**: 7 PASS / 0 WARN / 0 FAIL.

**Gaps for user**: (1) asset-capture strategy (live vs stylized); (2) contrarian vs neutral tone; (3) keep Trainium3 4.4× stat in tight 45s budget?

### Phase 1 — Plan (2026-04-27)
**Scene count**: 8 (Scene 00 Preview Hook + Scenes 01–07: Tension → Reveal → Chip Swap → Rainier → Multi-cloud → Proof → CTA).

**Hook variant**: **B (Stakes)** — *"If you got rate-limited on Claude this April — Anthropic just spent $100 billion to fix it."* Score **10.0/10** (curiosity 8 + stakes 10 + specificity 9 + alignment +1 + promise +1). Beats Variant A Counterintuitive (8.7) and Variant C Number (9.7) — picked because it validates the dev audience's actual click-pain (rate limits) and explicitly promises the resolution.

**Hook pattern**: **ContrastPivot** — 7 beats: Cold Open → Stakes Slam → Pain Context → PIVOT → Reveal → Rapid-Fire Body → CTA. Pivot word "But"; brand-reveal word "Anthropic" in Scene 00 line 1.

**Total data_duration**: **45s** (4+6+6+6+6+5+6+6).

**Retention picks**: 5 markers (highlight×3, scribble×1, circle×1), 0 caption groups (narration carries 45s), 0 audio-reactive effects (timeline too compressed), 3 transitions (1 primary blur-crossfade + 2 accents: zoom-through, staggered-blocks). Composite patterns: hero-slam×2, stat-pill-row×2, timeline-cards×2, narrated-stat-reveal×1, cta-url-slam×1.

**Fact-check audit**: 16 claims tracked — 12 sourced & in-plan, 3 deferred ($30B run-rate, Trainium3 4.4×, Stargate $500B — likely cut for 45s budget), 1 hard-excluded (no fabricated direct-speech quotes). 0 unsourced claims survive.

### Phase 2 — Script (2026-04-27)
**Word count**: 126 words / 45s ≈ 168 WPM (slightly above 150-165 target; acceptable for tech-influencer-edgy, Phase 2.5 will validate).
**Scene count**: 8 scenes (Scene 0–7) matching plan P0–P7.
**Hook locked (Scene 1, Variant B — score 10.0)**: *"If you got rate-limited on Claude this April, Anthropic just spent 100 billion dollars to fix it."* (Em-dash → comma per brand-voice rule #5; pause preserved.)
**Scar insert**: YES — Scene 3: *"On long contracts, 50 cents."* (Trainium pricing detail buried in BusinessCompass deep-dive; credibility signal a casual search would miss.)
**Banned phrases**: PASS — no "but here's the thing," "changes everything," "in this video," "delve/leverage/paradigm/seamless," "imagine," em dashes, or "we" pronoun. Contractions present.
**Story Locks**: Term Branding — *"the compute crunch"* coined Scene 7. Embedded Truths — no internal hedging. Contrast Words — explicit "But" pivot at Scene 2.
**Open loop**: Scene 1 hook → Scene 7 payoff *"peak-hour limits are about to ease. The compute crunch is over."*

### Phase 2.5 — Critique (2026-04-27) — **BLOCKED on QG-3**

Script: 124 words / ~49.6s / 150 WPM. Required loop openers: 2.

- **QG-1 Hook Strength**: PASS — **10.0/10** ($100B / 5GW / 0 Nvidia chips stat-cascade + named viewer pain + explicit promise).
- **QG-2 Story Arc**: PASS — **8.0/10** (hook-to-value 10, benefit-led 9, cohesion 9, **CTA strength 4** — "compute crunch is over" lacks debate question, 16 words).
- **QG-3 Loop Openers**: **FAIL — 1 found, 2 required.** Only "But the dollar number isn't the real story" (Scene 2). Plan deferred cadenced openers due to 45s budget; spec floor is hard at 2.
- **QG-4 AI-Phrasing**: PASS — 0 banned phrases.

**Overall**: **FAIL** (QG-3 only).

**Recommended fix**: prepend Scene 4 with `And it's already running.` (Option A) OR prepend Scene 6 with `But the proof isn't in the diagram.` (Option B). ~3 words, clears QG-3, no other gates affected.

Pipeline stopped at this gate per orchestrator spec.

### Phase 2.5 — Critique re-run (2026-04-27) — **PASS**

User picked Option A. Scene 4 edited: `"And it's already running. Project Rainier. Half a million Trainium2 chips live today. 11 billion dollar site in Indiana."` (cleaned up to avoid duplicate "is already running"; +1 word net).

- **QG-1 Hook**: PASS **10.0/10** (Curiosity 9, Stakes 10, Specificity 10, Stun-Gun 0/2, Alignment +0.5, Promise +1)
- **QG-2 Arc**: PASS **8.5/10** (Hook-to-Value 10, Benefit-Led 9, CTA 5, Cohesion 10)
- **QG-3 Loop Openers**: PASS — **2/2** (S2 "But the dollar number..." + S4 "And it's already running.")
- **QG-4 AI-Phrasing**: PASS — 0 banned phrases

**Overall**: PASS. Advisories (non-blocking): CTA could be a sub-15-word debate question; Scenes 1–4 run 3–7 words over per-scene targets (~51.6s actual vs 45s plan) — defer to Phase 2a.

### Phase 2a — TTS Script (2026-04-27)
**Scene count**: 8 (00 preview + 01–07). All scenes <800 chars (max 133 chars at Scene 03 chip-swap).
**TTS skill**: `text-to-speech` invoked successfully (no fallback). ElevenLabs defaults loaded: Shorts speed 1.13, voice `7kXNOCqiaLdszL0OEXks`, model `multilingual_v2`.
**Optimizations applied**:
- Numbers spelled out: `100`→`one hundred`, `5`→`five`, `3`→`three`, `50`→`fifty`, `11`→`eleven`, `55`→`fifty-five`, `87`→`eighty-seven`
- `%` → `percent`; `$` → `dollars`
- Acronyms letter-spaced: `AWS`→`A W S`, `GCP`→`G C P` (Azure kept; pronounces cleanly)
- `H100`→`H one hundred` (avoids `H-one-zero-zero`); `Trainium2`→`Trainium two`
- Em-dash for "...roughly New York City scale" → ellipsis for natural pause
- No `<break>` tags (period/ellipsis boundaries handle pacing)
- Brand names kept as-is (Nvidia, Anthropic, Pfizer, Lyft, Rainier, Indiana, Claude, Bedrock)

**Flat `script.txt`**: written to `videos/anthropic-amazon-compute/script.txt` (815 chars / 133 words, single paragraph, no headers, trailing newline). Format matches claude-connectors-everyday-life. Ready for `npx hyperframes tts`.

### Phase 2b — Fact-Check (2026-04-27) — **PASS**
**Claims by tier**: 11 total (9 T1 Critical, 2 T2 Important, 0 T3).
**Verdicts**: **10 VERIFIED**, **1 VERIFIED-WITH-CAVEAT** (Scene 03 chip pricing $1/hr Trainium, $0.50/hr long-contract — directional claim supported by BusinessCompass + TrendForce; bulk-contract rates not published verbatim by AWS; script's softening language "about / drops to / On long contracts" signals approximation), 0 CORRECTED, 0 STALE, 0 UNVERIFIED, 0 FAILED.

**URL audit**: 7 sources / 6 LIVE / 1 BROKEN_SOURCE (CNBC Project Rainier article returned 403 to automated fetch; non-blocking — $11B/Indiana facts independently confirmed via primary aboutamazon.com Project Rainier post).

**Auto-corrections applied**: NONE. Every numeric claim survived clean:
- $100B and 5 GW match Anthropic press release verbatim ("more than $100 billion over the next ten years", "up to 5GW of new capacity")
- Pfizer 55% / Lyft 87% match AWS press release verbatim
- Project Rainier "fully operational" + "nearly half a million Trainium2 chips" confirmed by primary AWS source
- "Got rate-limited on Claude this April" confirmed by The Register (March 26 2026) + Fortune (April 14 2026) — temporally fair on 2026-04-27
- "Zero Nvidia chips" / "Bypassing Nvidia entirely" accurate for THIS $100B commitment (Graviton + Trainium2-4 only)

**Files NOT modified**: all 8 `scripts/scene-*.txt`, `script.txt`, `scripts/full-script.md` — no corrections required.

---

Pipeline reached PAUSE 1 (TTS handoff). User authorized "do all next actions" → resumed.

### TTS + Transcribe (2026-04-27)
- `python scripts/elevenlabs-tts.py videos/anthropic-amazon-compute --shorts` produced:
  - `audio/narration.wav` — 52.99s, 4.67 MB (voice `7kXNOCqiaLdszL0OEXks`, model `eleven_multilingual_v2`, stability 0.65 / similarity 0.65 / style 0.0 / speed 1.1 / speaker_boost on)
  - `transcript.json` — 133 words, word-level alignment from ElevenLabs API (same schema as claude-connectors-everyday-life)
- Skipped explicit `npx hyperframes transcribe` — ElevenLabs alignment is canonical for its own output.
- **Note**: actual duration 52.99s vs 45s plan — ~18% overrun. Phase 1 plan and Phase 2.5 advisory both flagged ~51s estimate. Composition build can absorb via faster pacing/trim or accept as 53s short.

### Phase 3.5 — Retention Strategy (2026-04-27)
**Scenes**: 8 (P0 Preview Hook → P7 CTA).

**Picks by category**:
- **Markers**: 5 (1 highlight P0 on "billion", 1 scribble P1 on "rate_limit_exceeded", 1 highlight P2 on "New York City", 1 highlight P5 on "Multi-cloud", 1 circle P7 on "Claude/claude.com"). All under 2/scene cap.
- **Captions**: 0 (45s short + 240px slams crowd captions; plan-confirmed).
- **Audio-reactive**: 0 (scenes too short / narration too sparse for per-frame sampling).
- **Transitions**: 7 total — 5× `blur-crossfade` (primary, 71%) + 1× `zoom-through` (T1→T2 PIVOT accent) + 1× `staggered-blocks` (T5→T6 into proof cards). Within 1-primary + 1-2-accents rule.
- **GSAP effects**: 11 placements — `gsap-stagger-grid` ×7 + `gsap-counter-tween` ×4 (5 GW, $3→$1, 500K chips, 55%, 87%).

**Constraint violations resolved**: dropped P6 marker stack (counter-tweens carry emphasis); avoided `marker-burst` on "But" (transition + SFX handles pivot); kept Nvidia "bypass" as logo-style not marker; deferred captions uniformly per plan.

**Anchors with no good pick**: P4 "already running" (too short, conflicts with counter); P3 "Bypassing Nvidia" (deferred to logo); P1 "this April" (over-emphasis); P7 "compute crunch is over" (would crowd P7 marker-circle).

**Critical finding (override note #1)**: plan budget 45s but transcript runs **52.99s** (~8s overrun). Trigger times in strategy quoted from real transcript.json seconds, so they survive a `data_duration` bump — but Phase 4 MUST extend per-phase durations to sum to ~53s OR re-render TTS faster.

All 15 pick names validated against `.claude/references/retention-components-hyperframes.md` — zero invented names.

---

Pipeline reached PAUSE 2 (composition-build handoff). User authorized "ok run" → resumed.

### Composition Build — new-anthropic-short (2026-04-27)
**Output**: `videos/anthropic-amazon-compute/index.html` — 8 phases (P0–P7), `#root` `data-duration="54.5"` (52.78s narration + 1.72s tail; up from 45s plan per Phase 3.5 override).

**Per-phase durations** (transcript-boundary aligned): P0 0–4.85s · P1 5.0–10.50s · P2 10.85–17.20s · P3 17.70–25.40s · P4 25.85–33.10s · P5 33.55–39.70s · P6 40.15–47.20s · P7 47.85–54.5s.

**Retention wired**:
- 5/5 markers: highlight `$100B` @0.66s · scribble `rate_limit_exceeded` @5.76s · highlight `New York City` @16.40s · highlight `Multi-cloud` @38.53s · circle `claude.com` @48.44s.
- 7 transitions: 5× blur-crossfade (primary, 71%) + 1× zoom-through @T1 PIVOT @10.50s + 1× staggered-blocks @T5 @39.70s.
- 11 GSAP effects: 7× stagger-grid + 4× counter-tween (5GW, $3→$1, 0→500k chips, 0→55%, 0→87%).
- Hero slam shake: 4 ticks anchored to "billion" @0.66s.

**Lint**: 0 errors, 0 warnings (verbose).
**Inspect**: 0 layout issues across 9 samples.
**Preview**: http://localhost:3003 (port 3002 occupied by claude-connectors-everyday-life).

**Deviations**:
1. SFX deferred — assets not captured; DESIGN.md ≤0.20 mix; tracks 3+ left unwired.
2. Auxiliary images (NYC silhouette, Indiana outline, Trainium die-shot, Rainier aerial) deferred — strategy's primitives don't require them.
3. P1 status dots: 5 instead of 3 — same primitive (stagger-grid), stronger cadence in 0.9s window.

Render command (user runs manually): `npx hyperframes render videos/anthropic-amazon-compute -o videos/anthropic-amazon-compute/out/short.mp4`

### Background pattern port (2026-04-27)
User flagged that the visual chrome from old Remotion project (`diy-yt-creator/src/shared/templates/anthropic-short/AnthropicShortShell.tsx`) was missing. Ported two layers from the old `AnthropicShapeBackground` + `NoiseOverlay` components:

**Assets**: `assets/shapes/shape{1,2,3}.svg` copied from `diy-yt-creator/public/images/claude-code-routines/shapes/` into both `templates/shorts/anthropic/assets/shapes/` (canonical) and `videos/anthropic-amazon-compute/assets/shapes/` (mirror).

**Implementation**:
- `#shape-backdrop` div (z-index 0, between #ambient and phases) — populated at boot by `spawnShapes(seedPrefix, container)`. Mirrors React component: 14 shapes, 5% opacity, deterministic positions via xmur3-style hash (no Math.random / Date.now). Per-video seed prefix means each video gets a slightly different scatter pattern.
- `#noise-overlay` SVG (z-index 11, mix-blend-mode overlay, opacity 0.035) — feTurbulence fractalNoise filter, breaks up gradient banding. Mirrors `NoiseOverlay.tsx`.
- Video uses seed `anthropic-amazon-compute`; template uses seed `anthropic-short`.

**Verification**: `npx hyperframes lint` 0/0 on both. `npx hyperframes inspect` 0 layout issues across 9 samples.
