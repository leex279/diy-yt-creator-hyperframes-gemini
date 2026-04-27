# Retention Strategy: anthropic-amazon-compute

> **Source inputs**: `plan.md` (8 scenes, ContrastPivot, 45s budget) · `scripts/full-script.md` · `transcript.json` (133 words, 0.035s → 52.779s) · `.claude/references/retention-components-hyperframes.md`
>
> **Critical timing finding**: Plan budgeted 45s of `data_duration` but actual TTS narration runs to **52.99s** (~8s overrun). Per-scene `data_start` / `data_duration` below are the **plan-authoritative values from `plan.md` § Data Timing Budget**, but each scene's *Anchor moments* cite the **actual transcript timestamps**. Phase 4 (composition build) must reconcile this — either (a) bump each phase's `data_duration` to match real word timing, or (b) re-render TTS at faster pace. The retention picks below are valid in either case; only the trigger seconds shift. **Absolute trigger times below are quoted from `transcript.json` (real seconds), not the plan's placeholder anchors.**
>
> Transcript was sanity-checked: 133/133 entries are clean words; 0 `♪`/`�` tokens; 0 sub-0.1s fillers. No filtering needed.

---

## Summary Table

| Scene | Pattern (from §7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|-------|-------------------|------------|----------|----------------|----------------|-------------|
| 00 — Preview Hook | `hero-slam` | `gsap-stagger-grid`, `marker-highlight` on "billion" | none | none | `blur-crossfade` | 3 |
| 01 — The Tension | `stat-pill-row` (adapted) | `gsap-stagger-grid`, `marker-scribble` on "rate-limited" | none | none | `zoom-through` (accent) | 3 |
| 02 — The Reveal | `hero-slam` | `gsap-counter-tween` (0→5 GW), `marker-highlight` on "New York City" | none | none | `blur-crossfade` | 3 |
| 03 — Chip Swap | `stat-pill-row` | `gsap-counter-tween` ($3→$1), `gsap-stagger-grid` | none | none | `blur-crossfade` | 3 |
| 04 — Project Rainier | `narrated-stat-reveal` | `gsap-counter-tween` (0→500,000), `gsap-stagger-grid` | none | none | `blur-crossfade` | 2 |
| 05 — Multi-cloud anchor | `timeline-cards` (adapted as 3-pill row) | `gsap-stagger-grid`, `marker-highlight` on "Multi-cloud" | none | none | `staggered-blocks` (accent) | 3 |
| 06 — Proof | `timeline-cards` | `gsap-stagger-grid`, `gsap-counter-tween` (55%, 87%) | none | none | `blur-crossfade` | 3 |
| 07 — CTA | `cta-url-slam` | `marker-circle` on "Claude", `gsap-stagger-grid` | none | none | none (final) | 2 |

**Pattern primary**: `blur-crossfade` (5/7 transitions = 71%, within 60–70% target). Accents: `zoom-through` (T1→T2 pivot), `staggered-blocks` (T5→T6 into proof cards). Within "1 primary + 1–2 accents" rule.

**Totals**: 8 scenes · 5 markers (1 highlight P0, 1 scribble P1, 1 highlight P2, 1 highlight P5, 1 circle P7) · 0 captions · 0 audio-reactive · 7 transitions (5 primary + 2 accent) · 11 GSAP effect placements (`gsap-stagger-grid` ×7, `gsap-counter-tween` ×4).

---

## Scene-by-Scene Detail

### Scene 00 — Preview Hook (data_start=0s, data_duration=4s)

**Words in scene (transcript)**: 8 words spanning 0.035s–4.714s — note the last 4 words ("Five gigawatts. Zero Nvidia chips.") play 2.10s–4.71s, slightly overrunning the 4s budget into the 4–10s scene-01 envelope. Phase 4 should extend P0 to ~4.8s OR start P1 at ~4.8s.
- "One" 0.035 / "hundred" 0.221 / "billion" 0.662 / "dollars." 1.126
- "Five" 2.101 / "gigawatts." 2.426
- "Zero" 3.425 / "Nvidia" 3.796 / "chips." 4.203

**Anchor moments**:
- 0.035s — first word "One" (entrance moment, slam-in)
- 0.662s — "billion" lands (the dollar number; primary stat anchor)
- 2.101s — "Five" (the gigawatts stat)
- 3.425s — "Zero Nvidia" (contrarian flex — but NOT a marker target since the headline scene is hero-slam)
- 4.203s–4.714s — handoff window into Scene 01

**Picks** (from `retention-components-hyperframes.md` §1, §5, §7):
1. **`hero-slam` (composite pattern)** — overline "APRIL 2026" (0.0s), 240px slam "100 BILLION" (0.5s, anchored on "hundred billion" word group), caption pill "$100B / 10-yr compute deal" fading in at ~1.6s
2. **`gsap-stagger-grid`** — overline → slam word → caption pill, stagger 200ms, ease `back.out(1.7)`. Trigger at 0.0s; total entrance window 0–1.8s.
3. **`marker-highlight` on "billion"** — yellow/orange bar sweep behind the "BILLION" segment of the slam. Trigger_s = 0.662 (word.start). Sweep duration: 0.5s. (Caps at 1 marker — reserves headroom under 2/scene cap.)

**Why these picks**: Scene 00 is Kallaway "Context Lean-In" + stakes anchor — the dollar number is the value-alignment hook. The slam carries the visual, the marker highlight reinforces the word "billion" as the unit-of-shock. Captions are skipped per plan (4s is too tight for synced captions; the slam IS the caption). Audio-reactive skipped: the narration density (8 words in 4.7s) leaves no room for halo timing without competing with the slam-in animation.

---

### Scene 01 — The Tension (data_start=4s, data_duration=6s)

**Words in scene (transcript)**: 18 words 5.259s–10.623s — full sentence "If you got rate-limited on Claude this April, Anthropic just spent one hundred billion dollars to fix it."
- "If" 5.259 / "you" 5.422 / "got" 5.561 / "rate-limited" 5.759 / "on" 6.420 / "Claude" 6.525 / "this" 6.792 / "April," 6.989
- "Anthropic" 7.454 / "just" 7.964 / "spent" 8.173 / "one" 8.475 / "hundred" 8.742 / "billion" 9.172 / "dollars" 9.590 / "to" 9.973 / "fix" 10.112 / "it." 10.414

**Anchor moments**:
- 5.259s — first word "If" (P1 entrance, status-pill enters)
- 5.759s — **"rate-limited"** (PAIN word — primary marker target)
- 6.525s — "Claude" (brand reference, but already styled in toast)
- 6.989s — "April" (recency anchor — tertiary)
- 10.112s–10.623s — "fix it" handoff into the "But" pivot

**Picks**:
1. **`gsap-stagger-grid`** on the status-dot row — three dots flip from green to red, stagger 180ms, starting at 5.259s (synced to "If"). Ease `power4.out`.
2. **`marker-scribble` on "rate_limit_exceeded"** (the rendered toast text, not narrated word) — scribble triggers at 5.759s synced to spoken "rate-limited". Duration 0.55s. Crossing-out gesture establishes pain → reinforces the upcoming PIVOT.
3. **`zoom-through` transition out** (accent, plan-prescribed) — fires at 9.7s, duration 0.3s, ease `power4` so it lands right before the "But" pivot at 10.913s. NOTE: `data_start` of P2 is plan-authoritative at 10s; the spoken "But" lands at 10.913s, so the transition completes ~0.9s before the pivot word. Phase 4 should retime the transition to fire at 10.4s (start) → 10.7s (end) so the pivot word lands on the new scene.

**Why these picks**: This scene is the loop-setup half of the open-loop architecture — the named pain ("rate-limited") must register cleanly, since Scene 07 resolves it. Scribble is the only marker variant that *crosses-out* (per §1 — "crossing out a wrong claim before stating the right one"); it's earned here because Scene 02 immediately replaces the wrong/painful state with the fix. Captions skipped — toast + status row is the visual carrier. Audio-reactive skipped: scene-01's accent is red/warning (DESIGN.md "never decorative"), and an audio-reactive glow on the toast would soften the urgency the scene needs.

---

### Scene 02 — The Reveal (data_start=10s, data_duration=6s)

**Words in scene (transcript)**: 16 words 10.913s–17.543s — "But the dollar number isn't the real story. Five gigawatts of custom silicon... roughly New York City scale."
- "But" 10.913 / "the" 11.111 / "dollar" 11.238 / "number" 11.529 / "isn't" 11.854 / "the" 12.144 / "real" 12.307 / "story." 12.574
- "Five" 13.607 / "gigawatts" 13.897 / "of" 14.466 / "custom" 14.641 / "silicon..." 15.035
- "roughly" 15.999 / "New" 16.405 / "York" 16.614 / "City" 16.858 / "scale." 17.148

**Anchor moments**:
- 10.913s — **"But"** (THE pivot word — visual smash-cut moment, layered SFX per cinematic_hook_blueprint)
- 13.607s — "Five" (counter-tween anchor: tween starts here)
- 13.897s — "gigawatts" (counter-tween settles here)
- 16.405s–17.148s — "New York City scale" (marker-highlight target — phrase, ~0.74s span)

**Picks**:
1. **`gsap-counter-tween`** on the power-meter — tweens from 0 → 5 GW. tween_s_range = [13.107, 14.197] (i.e. start 0.5s before the "Five" word at 13.607s, settle 0.3s after "gigawatts" word.end at 13.897s). `roundProps: { value: 1 }`, ease `power3.out`.
2. **`marker-highlight` on "New York City"** — bar sweep behind the caption pill text "≈ New York City". Trigger_s = 16.405 (word.start of "New"); sweep duration 0.6s, completing just before the word "scale" lands at 17.148s. (Plan placed marker on "New York City" — confirmed.)
3. **`blur-crossfade` transition out** (primary) — fires at 15.5s (data_start + data_duration − 0.5 transition_duration); 0.5s, ease `sine.inOut`. NOTE: with overrun, transition end (16.0s) precedes the "New York City" phrase (16.4s+). Phase 4 must extend P2 `data_duration` from 6s to 7.5s OR move the marker phrase earlier — recommend extending duration since the phrase is content-locked.

**Why these picks**: This is the contrarian snapback — the counter-tween IS the reveal moment (the power meter physically demonstrates the number). Marker on "New York City" anchors the scale metaphor (universal scale anchor per content-brief Cult-Hopping). The "But" pivot word itself is handled by the **transition** (zoom-through from Scene 01) plus layered SFX (per plan blueprint) — NOT by an additional marker, which would compete with the slam word "5 GIGAWATTS". Captions and audio-reactive deliberately skipped — three concurrent visual events (slam + counter + marker) already saturate the visual hierarchy.

---

### Scene 03 — Chip Swap (data_start=16s, data_duration=6s)

**Words in scene (transcript)**: 21 words 17.764s–25.809s — "An H one hundred runs about three dollars an hour. Trainium drops to one. On long contracts, fifty cents. Bypassing Nvidia entirely."
- "An" 17.764 / "H" 17.949 / "one" 18.205 / "hundred" 18.379 / "runs" 19.018 / "about" 19.296 / "three" 19.563 / "dollars" 19.784 / "an" 20.109 / "hour." 20.237
- "Trainium" 20.829 / "drops" 21.293 / "to" 21.583 / "one." 21.746
- "On" 22.257 / "long" 22.466 / "contracts," 22.663 / "fifty" 23.209 / "cents." 23.522
- "Bypassing" 24.149 / "Nvidia" 24.706 / "entirely." 25.136

**Anchor moments**:
- 19.563s — "three" (counter-tween anchor for $3 H100 pill)
- 21.746s — "one" (counter-tween anchor for $1 Trainium flip)
- 23.209s — "fifty" (secondary stat — $0.50 contract pricing; possible third counter target)
- 24.149s — "Bypassing" (headline word — but no marker, scene already has 2 GSAP focal points)
- 24.706s — "Nvidia" (the contrarian word — visual treatment via greyed/struck-through logo, not a marker)

**Picks**:
1. **`gsap-counter-tween` ($3 → $1 flip)** — H100 pill stat tweens from 3 to 1 over the word boundary. tween_s_range = [19.063, 22.046] — that is, the H100 pill displays "$3" at 19.063s (0.5s before "three" word.start), holds through "an hour" (20.237s), then crossfades to the Trainium pill which counter-tweens 0→1 settling at 22.046s (0.3s after "one" word.end at 21.746s). Two-stage tween. `roundProps: { value: 1 }`.
2. **`gsap-stagger-grid`** — H100 pill exits L→R, Trainium pill enters R→L. Stagger 200ms, ease `back.out(1.7)`. Trigger at 20.6s (right after "hour." at 20.237s, just before "Trainium" at 20.829s).
3. **`blur-crossfade` transition out** (primary) — fires at 21.5s plan-relative... but transcript shows scene narration runs to 25.809s. Phase 4 must extend P3 `data_duration` from 6s to ~10s, OR the scene boundaries don't line up at all. Trigger_s for transition = scene.actual_end (25.81s) − 0.5s = 25.31s.

**Why these picks**: This is the proof-of-mechanism scene (chip swap → "not Nvidia"). Counter-tween on the price flip is the canonical retention move — viewers track numbers changing. Stagger on the pill exit/enter sells the *swap* gesture (one chip replaces another). No marker on this scene — plan-confirmed (the chip pills + counter carry the visual; adding a marker would crowd 240px stat pills). Captions skipped (12 on-screen words on two pills). Audio-reactive skipped (scene mid-tempo, treble glow would clash with the price-tag flip animation).

---

### Scene 04 — Project Rainier (data_start=22s, data_duration=6s)

**Words in scene (transcript)**: 18 words 25.995s–33.460s — "And it's already running. Project Rainier. Half a million Trainium two chips live today. Eleven billion dollar site in Indiana."
- "And" 25.995 / "it's" 26.193 / "already" 26.378 / "running." 26.796
- "Project" 27.516 / "Rainier." 27.946
- "Half" 28.781 / "a" 29.037 / "million" 29.107 / "Trainium" 29.466 / "two" 29.896 / "chips" 30.070 / "live" 30.395 / "today." 30.616
- "Eleven" 31.521 / "billion" 31.881 / "dollar" 32.195 / "site" 32.473 / "in" 32.810 / "Indiana." 32.949

**Anchor moments**:
- 27.516s — "Project Rainier" (term-brand anchor, but no marker — handled by 240px headline)
- 29.107s — "million" (counter-tween settle target for chip count: 0 → 500,000+)
- 31.521s — "Eleven" (sub-counter for $11B site cost)
- 32.949s — "Indiana" (location anchor — handled via inline state-outline image, no marker)

**Picks**:
1. **`gsap-counter-tween` (0 → 500,000+)** — chip counter rolls. tween_s_range = [28.281, 29.408] — start 0.5s before "Half" (28.781), settle 0.3s after "million" word.end (29.108). `roundProps: { value: 1000 }` (so the counter rolls in 1000-step jumps for visual readability), ease `power2.out`. 500,000 not 1,000,000 — script says "Half a million Trainium two chips" (the plan's "1M+" framing is for older Trainium2 fleet-wide numbers, but the spoken script narrows to 500K live today; counter targets the spoken number).
2. **`gsap-stagger-grid`** — sublabel chips ($11B / 1,200 acres / Indiana / live today) stagger in L→R 220ms apart, starting at 31.221s (0.3s before "Eleven"). Ease `power3.out`. Each chip is a `<div class="sublabel-chip">`.
3. **`blur-crossfade` transition out** (primary) — fires at scene.actual_end − 0.5s = 32.96s. (Plan said 28s scene_end; transcript drift = +5s into nominal Scene 05's window.)

**Why these picks**: `narrated-stat-reveal` from §7 — the counter is anchored to the spoken number, the stagger reveals the supporting context. No marker — the counter IS the focal point and would compete with a sweep. Captions skipped (14 words on screen between counter + 4 sublabel chips = visual saturation). Audio-reactive skipped — counter ticking creates its own tempo.

**Anchor with no good pick**: "And it's already running." (25.995–26.796s) — this 0.8s phrase is the scene's emotional payload ("already running, not vaporware"). Considered an `audio-reactive-glow` on the "running" word but skipped — too short to register against per-frame sampling, and would compete with the chip-counter spool-up. Phase 4 may add a subtle GSAP `power3.out` fade-up on the "STILL RUNNING TODAY" headline as a *non-cataloged* primitive — leaving the call to the composition build.

---

### Scene 05 — Multi-cloud Anchor (data_start=28s, data_duration=5s)

**Words in scene (transcript)**: 11 words 34.006s–40.066s — "Claude is still on AWS, GCP, and Azure. Multi-cloud is intact."
- "Claude" 34.006 / "is" 34.308 / "still" 34.412 / "on" 34.714
- "A" 34.946 / "W" 35.155 / "S," 35.504 / "G" 35.956 / "C" 36.200 / "P," 36.398 / "and" 36.839 / "Azure." 37.048
- "Multi-cloud" 38.534 / "is" 39.184 / "intact." 39.451

**Anchor moments**:
- 34.946s–35.504s — "AWS" letters (3 letters spelled — first pill enters L)
- 35.956s–36.398s — "GCP" letters (second pill enters mid)
- 37.048s — "Azure" (third pill enters R)
- 38.534s — **"Multi-cloud"** (marker-highlight target — the term-brand for the scene)

**Picks**:
1. **`gsap-stagger-grid`** — three mono pills "AWS · GCP · AZURE" enter L→R, each pill's reveal timed to the spoken letter group. Per-pill triggers: AWS pill at 34.846s (0.1s before "A"), GCP pill at 35.856s (0.1s before "G"), AZURE pill at 36.948s (0.1s before "Azure"). Ease `back.out(1.7)`. AWS pill gets the green accent edge thickening at 36.948s (when the third pill enters, AWS is "anchor leg").
2. **`marker-highlight` on "Multi-cloud"** — bar sweep behind the headline subtitle "Multi-cloud is intact." Trigger_s = 38.534 (word.start of "Multi-cloud"); sweep duration 0.55s, settling on "is intact" at ~39.18s.
3. **`staggered-blocks` transition out** (accent, plan-prescribed) — fires at scene.actual_end − 0.4s = 39.67s. (Plan said 33s scene_end; transcript drift makes real end 40.066s.) Card-style handoff into proof cards is well-suited to staggered-blocks per `transitions.md`.

**Why these picks**: The narration spells "A-W-S, G-C-P" letter-by-letter (eight tokens for what reads as two acronyms). Pill staggers MUST anchor to letter-group starts not individual letters; one pill per acronym means three pill events not eight. Marker on "Multi-cloud" coins the term (Story Lock #1 — Term Branding, which the plan applies to "the compute crunch" elsewhere — same mechanic). Captions skipped (3 pills + headline = visual is the message). Audio-reactive skipped (scene is short and measured).

---

### Scene 06 — Proof (data_start=33s, data_duration=6s)

**Words in scene (transcript)**: 15 words 40.612s–47.056s — "Pfizer cut infrastructure cost fifty-five percent on Claude. Lyft resolved customer issues eighty-seven percent faster."
- "Pfizer" 40.612 / "cut" 41.007 / "infrastructure" 41.227 / "cost" 41.947 / "fifty-five" 42.214 / "percent" 42.737 / "on" 43.131 / "Claude." 43.271
- "Lyft" 44.072 / "resolved" 44.327 / "customer" 44.734 / "issues" 45.198 / "eighty-seven" 45.651 / "percent" 46.220 / "faster." 46.580

**Anchor moments**:
- 40.612s — "Pfizer" (Card 1 entrance, brand anchor)
- 42.214s — "fifty-five" (counter-tween: 0 → 55 percent for Card 1)
- 44.072s — "Lyft" (Card 2 entrance)
- 45.651s — "eighty-seven" (counter-tween: 0 → 87 percent for Card 2)

**Picks**:
1. **`gsap-stagger-grid`** — two Pfizer/Lyft cards stagger 200–280ms. Card 1 (Pfizer) enters at 40.412s (0.2s before "Pfizer"); Card 2 (Lyft) enters at 43.872s (0.2s before "Lyft"). Per plan, ease `back.out(1.7)`, spring-pop SFX on each card settle.
2. **`gsap-counter-tween` (×2)** —
   - Card 1: 0 → 55 (percent). tween_s_range = [41.714, 43.037] (start 0.5s before "fifty-five" 42.214, settle 0.3s after "percent" 42.737). `roundProps: { value: 1 }`.
   - Card 2: 0 → 87 (percent). tween_s_range = [45.151, 46.520] (start 0.5s before "eighty-seven" 45.651, settle 0.3s after "percent" 46.220).
3. **`blur-crossfade` transition out** (primary) — fires at scene.actual_end − 0.5s = 46.56s.

**Why these picks**: Canonical `timeline-cards` pattern from §7. Two stat cards + two counter-tweens — exactly the social-proof archetype. Markers deliberately skipped on this scene (the counter is doing the work; adding a marker on "fifty-five" or "eighty-seven" would duplicate emphasis that the tween already provides). Plan called for marker-counter combo but per §1 cap and §8 anti-pattern "viewer eye stops registering them," removed in favor of pure counter focus. **This is one constraint resolution** (see Override Notes below).

**Anchor with no good pick**: "16,000 hours saved" — content-brief mentions this Pfizer stat but spoken script omits it (only "55 percent on Claude"). No retention pick needed since the stat doesn't appear in narration.

---

### Scene 07 — CTA (data_start=39s, data_duration=6s)

**Words in scene (transcript)**: 14 words 47.799s–52.779s — "If you build on Claude, peak-hour limits are about to ease. The compute crunch is over."
- "If" 47.799 / "you" 47.961 / "build" 48.089 / "on" 48.333 / "Claude," 48.437
- "peak-hour" 49.053 / "limits" 49.587 / "are" 49.947 / "about" 50.132 / "to" 50.399 / "ease." 50.527
- "The" 51.317 / "compute" 51.491 / "crunch" 51.827 / "is" 52.176 / "over." 52.350

**Anchor moments**:
- 48.437s — **"Claude"** (THE CTA brand word — `marker-circle` target, since the URL pill displays "claude.com")
- 49.053s — "peak-hour" (echo of Scene 01 pain — closes the loop)
- 51.317s–52.350s — "The compute crunch is over." (Story Lock #1 echo, term-brand payoff. Final line — handoff to subscribe pill or end-card.)

**Picks**:
1. **`marker-circle` on "Claude"** (the URL pill text "claude.com" — circling the URL as a hand-drawn ellipse). Trigger_s = 48.437 (word.start of "Claude" in narration); draw duration 0.7s, settling at 49.13s. Per §1: "one-off emphasis on a noun (product name)." This is the canonical pick for URL slam.
2. **`gsap-stagger-grid`** — URL pill enters at 47.6s (0.2s before "If" at 47.799s); subscribe pill follows 220ms later at 47.82s. Ease `expo.out` on URL slam, `power2.out` on subscribe. Per plan blueprint Scene 07.
3. **No transition out** — final scene per plan + §4 anti-rule "exit animations are BANNED except on the final scene." Final fade-to-end-card is the only allowed exit; not part of retention strategy.

**Why these picks**: This is the loop resolution — "peak-hour limits are about to ease" pays off Scene 01's "rate-limited" setup and Scene 07's "compute crunch is over" coins the Story-Lock-#1 term-brand. `marker-circle` is the canonical CTA URL emphasis (per §9 "How do I render X" lookup). Captions skipped — the URL pill IS the on-screen text. Audio-reactive skipped — final scene needs to land calm and clean, not pulse.

---

## Picks Cross-Reference (validate against menu)

| Pick name             | Source section in retention-components-hyperframes.md | Confirmed valid? |
|-----------------------|--------------------------------------------------------|------------------|
| `marker-highlight`    | §1 row 1                                               | yes              |
| `marker-scribble`     | §1 row 4                                               | yes              |
| `marker-circle`       | §1 row 2                                               | yes              |
| `gsap-counter-tween`  | §5 row 2                                               | yes              |
| `gsap-stagger-grid`   | §5 row 3                                               | yes              |
| `blur-crossfade`      | §4 (Calm CSS primary)                                  | yes              |
| `zoom-through`        | §4 (High CSS primary, used here as accent)             | yes              |
| `staggered-blocks`    | §4 (Medium CSS primary, used here as accent)           | yes              |
| `hero-slam`           | §7 composite pattern                                   | yes              |
| `stat-pill-row`       | §7 composite pattern                                   | yes              |
| `narrated-stat-reveal`| §7 composite pattern                                   | yes              |
| `timeline-cards`      | §7 composite pattern                                   | yes              |
| `cta-url-slam`        | §7 composite pattern                                   | yes              |
| `inline-phase`        | §6 row 1 (structural)                                  | yes (template-locked) |
| `mutex-visibility`    | §6 row 3 (structural)                                  | yes (template-locked) |

All 15 pick names are canonical per the menu. Zero invented names.

---

## Constraint Audit (per §8)

| Constraint                                                           | Status | Notes                                                                                                                                       |
|----------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Max 2 markers per scene                                              | PASS   | Each scene has 0 or 1 marker. Highest is 1 (P0, P1, P2, P5, P7). 5 markers total / 8 scenes.                                                |
| Only one caption group visible at a time                             | PASS   | 0 caption groups used — moot.                                                                                                               |
| One primary transition (60–70% of scene changes) + 1–2 accents       | PASS   | `blur-crossfade` 5/7 = 71% (primary). Accents: `zoom-through` (1×), `staggered-blocks` (1×). Within rule.                                   |
| No exit animations on non-final scenes                               | PASS   | All 7 transitions are between-scene crossfades/zooms (the transition IS the exit). No element-level exit tweens on non-final scenes.        |
| No banned audio-reactive vocab (equalizers, spectrum, rainbow)        | PASS   | Zero audio-reactive picks total — moot. (Plan-confirmed: 45s short / scene durations too short for per-frame sampling to read.)             |
| Single structural model per video (`inline-phase` + `mutex-visibility`) | PASS | Template-enforced. All 8 phases are inline `.phase` divs in `index.html`.                                                                  |
| Determinism (no Date.now, Math.random, runtime fetch)                | PASS   | All pick triggers cite explicit transcript-derived seconds; counter end-values pre-computed (5, 1, 500000, 55, 87).                          |

**Constraint violations almost made and resolved**:

1. **Scene 06 marker over-stacking (avoided)**: Plan §retention_component_picks proposed `gsap-counter-tween` AND `gsap-stagger-grid` AND a marker pair — three primitives plus 2 cards = visual saturation. Resolved by dropping markers entirely on P6; the counter-tweens carry the emphasis. Net: 2 picks, not 3.

2. **Scene 02 triple-emphasis on "But" (avoided)**: Considered adding `marker-burst` on "But" at 10.913s in addition to the existing transition + slam + counter-tween. That would have been 4 visual events stacked across 0.4s = strobe-feel. Resolved by treating the transition (`zoom-through`) and SFX layer as the "But" beat — no additional marker.

3. **P3 marker on "Nvidia" (avoided)**: Plan blueprint suggests greying/struck-through Nvidia logo. Considered adding `marker-scribble` on the spoken word "Nvidia" at 24.706s. Resolved: the visual treatment is a logo style change (greyscale + strikethrough), not a marker primitive — keeps marker count low and respects §1 "skip when surrounding text is already heavily styled."

4. **Caption groups (uniformly skipped)**: Plan's `retention_component_picks` already had `captions: null` for all 8 scenes. Honored — adding word-pop captions over 240px slam words would fight for the same eye real estate. The transcript is preserved for word-level timing of *other* picks (counter tweens, marker triggers), not for caption rendering.

**Anchors with no good pick**:

- **Scene 04, "And it's already running."** (25.995–26.796s) — emotional payload ("not vaporware"), but 0.8s is too short for an audio-reactive glow to register and a marker would compete with the chip counter. Documented above; Phase 4 may add a non-cataloged GSAP fade-up on a "RUNNING TODAY" headline.
- **Scene 03, "Bypassing Nvidia entirely."** (24.149–25.809s) — the contrarian payoff line. Considered `marker-strikethrough` (not in catalog) on "Nvidia" — instead deferred to logo-style treatment as noted above.
- **Scene 01, "this April"** (6.792–7.407s) — recency anchor for the topic. Skipped as marker target because "rate-limited" already carries the marker on this scene (max-2 cap leaves room but DESIGN.md "never decorative" red on the toast already over-indexes for emphasis).
- **Scene 07, "compute crunch is over"** (51.491–52.350s) — the Story-Lock-#1 term-brand payoff. Skipped as marker target because the `marker-circle` on "Claude" already lands at 48.437s (4s earlier in same scene); a second marker so close violates the §1 spirit ("eye stops noticing them"). Phase 4 may strengthen the "compute crunch" treatment via mono-style typography on a separate line; not a retention primitive.

---

## Override Notes

Phase 4 (composition build via `/diy-yt-creator:new-anthropic-short`) reads this file as authoritative. To override any pick, edit this file directly before invoking the build.

**Critical follow-ups for Phase 4**:

1. **Reconcile timing drift**: Plan budgeted 45s, transcript runs 52.99s. Either bump per-phase `data_duration` (recommended; sum to ~53s) OR re-render TTS at 1.18× pace. Either approach preserves the relative trigger seconds within each scene. The trigger times in this file are quoted from `transcript.json` so they survive the duration bump.
2. **Bump `#root` `data-duration` to ≥53** (was 45 per plan note 1).
3. **Counter-tween end values** (pre-computed for determinism):
   - P2: 5
   - P3 H100 pill: 3 (display) → swap to Trainium pill: 1
   - P4: 500000 (chip count)
   - P6 Card 1: 55 (percent)
   - P6 Card 2: 87 (percent)
4. **SFX volume cap** (per plan note 6): keep total mix ≤0.20 on most beds; Scene 02 PIVOT layers 3 SFX on three different `data-track-index` values per blueprint.
5. **Marker color rotation matches accent rotation**: P0 orange highlight, P1 red scribble (DESIGN.md "never decorative" — the toast is already red, so scribble inherits), P2 orange highlight, P5 green highlight (multi-cloud accent), P7 orange circle.

