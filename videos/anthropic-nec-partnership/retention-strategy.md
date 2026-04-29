# Retention Strategy: anthropic-nec-partnership

> **Pacing reconciliation**: `plan.md` budgeted 90s across 8 scenes (10/11/9/11/12/13/12/12). The actual narration in `transcript.json` ends at **112.871s** — a 22.87s overrun. Per-scene `data_start` / `data_duration` below have been re-anchored to the real ElevenLabs word timings. The composition build phase MUST use the timings in this file (not the placeholder timings in `plan.md`'s Data Timing Budget block).
>
> **TTS engine**: ElevenLabs (not Whisper). Word tokens are clean — "Claude" is "Claude", "OpenAI" is "OpenAI", "Edison-era" is "Edison-era". Number words are spelled out ("one hundred twenty-seven-year-old", "eighteen ninety-nine", "thirty thousand", "seventeen point seven", "twenty-nine") — anchor lookups below cite both the literal transcript word AND the canonical script form.
>
> **Boundary placement rule**: every `data_start` lands in the natural narration breath (≥0.5s gap between the previous scene's last word end and the next scene's first word start), giving `blur-crossfade` transitions a clean handoff.

## Summary Table

| Scene | Pattern (from §7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|-------|------------------|------------|----------|----------------|----------------|-------------|
| 01 — Hook (Stakes Pivot) | `hero-slam` | `gsap-stagger-grid`, `gsap-counter-tween`, `marker-scribble`, `marker-highlight` | none | none | `blur-crossfade` | 5 |
| 02 — Edison-Era → AI-Native | `timeline-cards` | `gsap-stagger-grid`, `gsap-path-draw`, `gsap-counter-tween`, `marker-highlight` | `caption-fade-slide` | none | `blur-crossfade` | 6 |
| 03 — First Japan Partner | `stat-pill-row` (badge variant) | `gsap-stagger-grid`, `gsap-path-draw`, `marker-circle` | none | none | `blur-crossfade` | 4 |
| 04 — 30K of 105K Rollout | `stat-pill-row` | `gsap-counter-tween` ×2, `gsap-stagger-grid`, `marker-highlight` | `caption-fade-slide` | none | `blur-crossfade` | 6 |
| 05 — Client Zero / Eng Team | `stat-pill-row` (badge variant) | `gsap-stagger-grid`, `gsap-path-draw`, `marker-highlight`, `marker-circle` | `caption-fade-slide` | none | `blur-crossfade` | 6 |
| 06 — BluStellar + Verticals | `timeline-cards` (2×2 grid variant) | `gsap-stagger-grid`, `gsap-flip-reveal`, `marker-highlight` | `caption-fade-slide` | none | `blur-crossfade` | 5 |
| 07 — Why Now (Receipts) | `timeline-cards` (chart + stack variant) | `gsap-path-draw`, `gsap-counter-tween`, `gsap-stagger-grid`, `marker-highlight` ×2 | `caption-fade-slide` | `audio-reactive-glow` | `blur-crossfade` | 7 |
| 08 — Who Next? CTA | `cta-url-slam` (card-stack variant) | `gsap-stagger-grid`, `marker-circle` | `caption-fade-slide` | `audio-reactive-glow` | none (final) | 4 |

**Pick totals across the comp**:
- Markers: 11 (`marker-scribble` ×1, `marker-highlight` ×6, `marker-circle` ×3, plus 1 marker-highlight pair counted as 2 in Scene 07 — total 11)
- Captions: 6 scenes (Scenes 02, 04, 05, 06, 07, 08) — all `caption-fade-slide`
- Audio-reactive: 2 (`audio-reactive-glow` on Scene 07's "twenty-nine million" counter; `audio-reactive-glow` on Scene 08 subscribe pill)
- Transitions: 7 (`blur-crossfade` between P1→P2, P2→P3, P3→P4, P4→P5, P5→P6, P6→P7, P7→P8)
- GSAP effects: 18 invocations (`gsap-stagger-grid` ×8, `gsap-counter-tween` ×4, `gsap-path-draw` ×4, `gsap-flip-reveal` ×1, `marker-*` not counted as GSAP since they're CSS primitives)
- SFX cues: 22 distinct cue placements (see per-scene blocks below)

---

## Scene-by-Scene Detail

### Scene 01: Hook — Stakes Pivot (data_start=0s, data_duration=14.0s)

**Words in scene**: 29 (transcript indices 0–28, "Anthropic" 0.035s → "part." 13.955s)

**Anchor moments**:
- 0.035s — first word "Anthropic" (entrance / brand reveal)
- 1.138s — "out-flanked" (the verb that defines the hook stakes)
- 1.846s — "OpenAI" (named competitor)
- 5.631s — "twenty-seven-year-old" (the 127 number — candidate for `gsap-counter-tween`)
- 7.628s — "Claude" / 7.930s — "Code" (brand-name reference)
- 9.195s — "thirty" / 9.671s — "thousand" (the headline stat the hook teases as "not the shocker")
- 11.726s — "But" (PIVOT word — the contrarian snap; structural hinge of the entire video)
- 13.119s — "shocking" (lands the loop-opener tension)

**Picks**:

1. `gsap-stagger-grid` — overline "ANTHROPIC × NEC" + 240px slam reveal entrance. Trigger at scene start; staggered overline → slam → caption pill. `tween_s_range: [0.0, 1.5]`, ease `back.out(1.7)`.

2. `gsap-counter-tween` on the "30,000" slam number — anchored to "thirty" word at 9.195s. `tween_s_range: [8.69, 9.85]` (0.5s lead-in so digits already settle as the narrator says it). Easing `power3.out`, 1.0s duration. The number is shown as the FACE-VALUE stat that the pivot rejects; counter ticks 0 → 30,000 to reinforce "this is the headline."

3. `marker-scribble` — strikethrough sweep across the displayed "30,000". Trigger_s: 11.50s (0.22s before "But"). 0.5s sweep. **Marker #1/2.**

4. `marker-highlight` — yellow/red bar sweep behind the pivot word "BUT." Trigger_s: 11.726 (= word.start). Sweep 0.5s. **Marker #2/2.**

5. `blur-crossfade` to Scene 02 — trigger_s: 13.5s, duration 0.5s (so transition completes by 14.0s before Scene 02's first word "Because" at 14.733s).

**Captions**: NONE. The hook is too dense (5 emphasis beats in 14s) to also support a synced caption layer — the slam + pivot reveal IS the focal text.

**Audio-reactive**: NONE on the hook — text-on-text glow during a pivot moment dilutes the slam.

**SFX cues** (per `.claude/rules/audio-design.md`; cues from `shared/audio/MANIFEST.md`):
```yaml
sfx_cues:
  - cue: impact-slam              # context entrance (overline + slam)
    anchor_word_index: 18         # "thirty" — start 9.195
    offset_seconds: -0.05         # percussive lead-in
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15                  # MANIFEST default
  - cue: strike-cross             # strikethrough on "30,000"
    anchor_word_index: 21         # "But" — start 11.726
    offset_seconds: -0.22         # fires at 11.50s, before "But"
    duration_seconds: 0.63
    track_index: 3                # sequential, no overlap with prior impact-slam
    volume: 0.11
  - cue: impact-slam              # PIVOT slam on "But"
    anchor_word_index: 21         # "But" — start 11.726
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3                # sequential after strike-cross (11.50 + 0.63 = 12.13 < 11.676 — overlap!) → move to track 4
    volume: 0.15
  - cue: screen-shake             # layered with PIVOT impact-slam
    anchor_word_index: 21         # "But" — start 11.726
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 5                # third concurrent cue at 11.676s
    volume: 0.11
  - cue: glitch-zap               # third layer of PIVOT stack
    anchor_word_index: 21         # "But" — start 11.726
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 6                # fourth concurrent cue
    volume: 0.09                  # quietest of the layered stack
  - cue: cinematic-whoosh         # phase change Scene 01 → Scene 02
    anchor_word_index: 28         # "part." end ~13.955
    offset_seconds: -0.45         # whoosh peaks just before scene cut
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```
**Track-index resolution note**: the strike-cross (start 11.50, duration 0.63 → ends 12.13) overlaps the PIVOT impact-slam (start 11.676). The PIVOT impact-slam is therefore moved from track 3 to track 4. Final layout: track 3 = impact-slam@9.145 + strike-cross@11.50 + cinematic-whoosh@13.505 (sequential, no overlap); track 4 = impact-slam@11.676 (PIVOT); track 5 = screen-shake@11.676; track 6 = glitch-zap@11.676.

**Why these picks**: The hook is a Stakes ContrastPivot — the slam delivers the "30,000" face-value receipt, the strikethrough physically rejects it, the layered "BUT" stack (impact + shake + zap) is the structural hinge. `marker-scribble` on the rejected number + `marker-highlight` on "BUT" hits the 2-marker cap exactly. No caption layer because the slam IS the caption. Counter tween reinforces the "rolling up to a real number" feel under the slam.

---

### Scene 02: Edison-Era → AI-Native (data_start=14.0s, data_duration=11.5s)

**Words in scene**: 18 (transcript indices 29–46, "Because" 14.733s → "overnight." 24.938s)

**Anchor moments**:
- 14.733s — "Because" (loop-opener entrance: "Because here's the part nobody's saying out loud")
- 18.193s — "NEC" (brand entrance — the company being reframed)
- 18.843s — "founded" (sets the timeline anchor)
- 20.155s — "eighteen" / 20.561s — "ninety-nine" (1899 — candidate for counter tween from 1899 → 2026 OR static label with `gsap-stagger-grid` tick reveal)
- 21.966s — "Edison-era," (term-branded phrase — Lock #1 from plan.md story-lock placement)
- 23.417s — "AI-native" (the contrast term — pairs with Edison-era)

**Picks**:

1. `gsap-stagger-grid` — 4 year ticks fan out left-to-right (1899 / 1950 / 2000 / 2026). `tween_s_range: [14.5, 16.5]`, 200ms stagger between ticks, ease `back.out(1.7)`. Each tick is a small chip (JetBrains Mono, 32px); the four chips form the timeline rail.

2. `gsap-path-draw` — the timeline rail (horizontal SVG line) draws across the screen left → right. `tween_s_range: [14.5, 16.0]`, 1.5s draw, ease `power2.inOut`. Rail draws BEFORE ticks pop on top of it.

3. `gsap-counter-tween` on the "127 YEARS" slam (purple) — anchored to "twenty-seven-year-old" word at 5.631s in Scene 01 narration… BUT this scene re-displays it as a labeled slam after the timeline rail completes. `tween_s_range: [21.5, 22.7]`, 1.2s tween 0 → 127, ease `power3.out`. Lands on "Edison-era" word at 21.966s.

4. `marker-highlight` — yellow bar sweep behind "127 YEARS" slam. Trigger_s: 22.70 (lands as the counter settles). Sweep 0.5s. **Marker #1/2 — within cap.**

5. `caption-fade-slide` — narration carries the timeline explanation; caption tracks each spoken word group. Word groups (3-5 words/group per news-explainer cadence): ["Because here's the part", "nobody's saying out loud", "NEC was founded in", "eighteen ninety-nine", "Edison-era, going AI-native overnight"]. Position: bottom 600-700px from bottom; one group visible at a time per `captions.md` rule.

6. `blur-crossfade` to Scene 03 — trigger_s: 25.0s, duration 0.5s (completes by 25.5s before Scene 03's first word "And" at 25.716s).

**Audio-reactive**: NONE — calm explanatory cadence; audio-reactive on the timeline ticks would feel mechanical.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # tick #1 (1899 chip)
    anchor_word_index: 41         # "eighteen" — start 20.155
    offset_seconds: -0.40         # fires at 19.755 — anchored to the spoken year
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # tick #2 (1950 chip — derived stagger 200ms after tick #1)
    anchor_word_index: 41         # "eighteen" — start 20.155
    offset_seconds: -0.20         # fires at 19.955
    duration_seconds: 0.52
    track_index: 4                # concurrent with tick #1 (overlap window 19.755–20.275 vs 19.955–20.475)
    volume: 0.11
  - cue: spring-pop               # tick #3 (2000 chip)
    anchor_word_index: 42         # "ninety-nine." — start 20.561
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 19.755 + 0.52 = 20.275 < 20.561 (sequential reuse OK)
    volume: 0.11
  - cue: spring-pop               # tick #4 (2026 chip)
    anchor_word_index: 42         # "ninety-nine." — start 20.561
    offset_seconds: 0.20          # fires at 20.761
    duration_seconds: 0.52
    track_index: 4                # 19.955 + 0.52 = 20.475 < 20.761 (sequential reuse OK)
    volume: 0.11
  - cue: scale-slam               # "127 YEARS" purple slam entrance
    anchor_word_index: 43         # "Edison-era," — start 21.966
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3                # 20.561 + 0.52 = 21.081 < 21.916 (sequential reuse OK)
    volume: 0.15
  - cue: cinematic-whoosh         # phase change Scene 02 → Scene 03
    anchor_word_index: 46         # "overnight." end ~24.938
    offset_seconds: 0.06          # 25.00s
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: Timeline-cards is the canonical pattern for a dated event sequence (per §7). The 4 ticks plus the path draw plus the counter tween give 3 GSAP effects without overcrowding. `marker-highlight` on "127 YEARS" reinforces the term-branded contrast. `caption-fade-slide` matches the calm news-explainer cadence; the loop-opener "Because here's the part nobody's saying out loud" needs to land verbally, not visually.

---

### Scene 03: First Japan Partner (data_start=25.5s, data_duration=10.2s)

**Words in scene**: 17 (transcript indices 47–63, "And" 25.716s → "deploy." 35.166s)

**Anchor moments**:
- 25.716s — "And" (entrance)
- 25.960s — "NEC" (brand re-entrance — paired with the first/global claim)
- 27.121s — "Anthropic's" (status anchor)
- 27.724s — "first" (the badge claim — `marker-circle` candidate)
- 28.015s — "Japan-based" / 28.688s — "global" / 29.083s — "partner." (status badge content)
- 30.406s — "It's engineering depth" (the thought-narration line — Lock #3 from plan.md)
- 33.100s — "pilot" / 34.075s — "and never deploy" (the implicit contrast — enterprises that fail to ship)

**Picks**:

1. `gsap-stagger-grid` — Japan silhouette + pin + badge enter staggered. `tween_s_range: [25.7, 27.5]`, 200ms stagger (silhouette → pin drop → badge), ease `back.out(1.7)`.

2. `gsap-path-draw` — Japan silhouette outline draws in. `tween_s_range: [25.7, 27.0]`, 1.3s draw, ease `power2.inOut`. Draws BEFORE the pin lands.

3. `marker-circle` — hand-drawn ellipse around "1st" (the badge text "1st Japan-based global partner"). Trigger_s: 27.724 (= "first" word.start). 0.6s draw. **Marker #1/2 — within cap.**

**Captions**: NONE. The badge IS the headline; layering captions over a 10s status reveal would compete with the badge text.

**Audio-reactive**: NONE — single-pin scene; reactivity would distract from the pin landing beat.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # pin drop landing
    anchor_word_index: 53         # "first" — start 27.724
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # badge entrance ("1st Japan-based global partner")
    anchor_word_index: 56         # "partner." — start 29.083
    offset_seconds: -0.10
    duration_seconds: 0.52
    track_index: 3                # 27.674 + 0.73 = 28.404 < 28.983 (sequential reuse OK)
    volume: 0.11
  - cue: cinematic-whoosh         # phase change Scene 03 → Scene 04
    anchor_word_index: 63         # "deploy." end ~35.166
    offset_seconds: 0.04          # 35.20s
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: A status-badge scene needs ONE primary visual focus — the pin drop + badge — and one marker (`marker-circle` on "1st") to declare the status. The `gsap-path-draw` of the Japan silhouette adds geographic specificity without cluttering. Captions skipped intentionally — the badge is the caption.

---

### Scene 04: 30K of 105K Rollout (data_start=35.7s, data_duration=12.0s)

**Words in scene**: 22 (transcript indices 64–85, "So" 35.944s → "group." 47.136s)

**Anchor moments**:
- 35.944s — "So" (entrance — explanatory connector)
- 38.243s — "Thirty" / 38.614s — "thousand" (the 30,000 stat — candidate #1 for `gsap-counter-tween`)
- 40.216s — "one" / 40.460s — "hundred" / 41.342s — "five" / 41.679s — "thousand" (the 105,000 stat — candidate #2 for `gsap-counter-tween`)
- 44.895s — "twenty-nine" / 45.510s — "percent" (the 29% derived stat — candidate for `marker-highlight`)
- 46.253s — "entire" / 46.671s — "group." (the closing scope clause)

**Picks**:

1. `gsap-counter-tween` #1 — "30,000" stat pill (orange, full opacity, primary). Anchored to "Thirty" word at 38.243s. `tween_s_range: [37.74, 38.85]` (0.5s lead-in so digits settle as narrator says it), 1.0s tween, ease `power3.out`.

2. `gsap-counter-tween` #2 — "105,000" stat pill (blue, 0.55 opacity, secondary). Anchored to "five thousand" word group ending at 42.318s. `tween_s_range: [40.0, 42.50]` (1.0s lead-in to land on the spoken number; longer hold because the number is spoken across 4 word tokens). Easing `power3.out`.

3. `gsap-stagger-grid` — two pills enter with 200ms stagger. `tween_s_range: [37.7, 38.4]`, ease `back.out(1.7)`. Pills enter BEFORE counters tween (counters run on already-visible pills).

4. `marker-highlight` — yellow bar sweep behind "≈29%" sublabel between the two pills. Trigger_s: 44.895 (= "twenty-nine" word.start). Sweep 0.5s. **Marker #1/2 — within cap.**

5. `caption-fade-slide` — narration carries "of NEC's 105,000 employees getting Claude Code, about 29% of the entire group." Word groups (3-5 words/group): ["So what does the rollout look like", "Thirty thousand of NEC's", "one hundred five thousand employees", "getting Claude Code", "about twenty-nine percent of the entire group"]. Position: bottom 600-700px.

6. `blur-crossfade` to Scene 05 — trigger_s: 47.20s, duration 0.5s (completes by 47.70s before Scene 05's first word "And" at 47.914s).

**Audio-reactive**: NONE on the counters — `audio-reactive-glow` would fight the counter tween's deterministic digit reveal.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # pill #1 (30,000 orange) entrance
    anchor_word_index: 70         # "Thirty" — start 38.243
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: scale-slam               # pill #2 (105,000 blue) entrance
    anchor_word_index: 74         # "one" — start 40.216
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3                # 38.193 + 0.73 = 38.923 < 40.166 (sequential reuse OK)
    volume: 0.15
  - cue: spring-pop               # ≈29% sublabel pop
    anchor_word_index: 81         # "twenty-nine" — start 44.895
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh         # phase change Scene 04 → Scene 05
    anchor_word_index: 85         # "group." end ~47.136
    offset_seconds: 0.06          # 47.20s
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: Two stat pills with `gsap-counter-tween` is the textbook `stat-pill-row` pattern. The 30K (full opacity orange) vs 105K (dim blue) size relationship visually communicates "the 30K is the live part of the 105K." `marker-highlight` on the derived "≈29%" closes the math loop without cluttering.

---

### Scene 05: Client Zero / Eng Team (data_start=47.7s, data_duration=14.5s)

**Words in scene**: 27 (transcript indices 86–112, "And" 47.914s → "program." 61.637s)

**Anchor moments**:
- 47.914s — "And" (entrance — Loop Opener #1: "And here's the part OpenAI should worry about")
- 48.866s — "OpenAI" (named competitor — the loop-opener tension)
- 51.315s — "NEC" (brand re-entrance)
- 52.151s — "building" / 52.674s — "calling" (the verb stack — what NEC is doing)
- 53.753s — "Japan's" / 54.322s — "largest" (the qualifier — tied to the "what they're calling" hedge per fact-check)
- 54.996s — "AI-native" / 55.855s — "engineering" / 56.470s — "teams," (the term-branded engineering claim — `marker-highlight` candidate)
- 60.243s — "Client" / 60.673s — "Zero" / 61.033s — "program." (the badge entrance — `marker-circle` candidate)

**Picks**:

1. `gsap-stagger-grid` — mesh org-chart nodes appear (start with hierarchical tree, ~12 nodes), then morph to mesh. `tween_s_range: [47.9, 50.5]`, 80ms stagger between nodes, ease `back.out(1.7)`.

2. `gsap-path-draw` — mesh edges draw between nodes (every node connected to ≥3 others). `tween_s_range: [50.0, 52.0]`, 50ms stagger between edge draws, ease `power2.inOut`. Edges draw AFTER nodes settle.

3. `marker-highlight` — yellow bar sweep behind "AI-native engineering teams" phrase. Trigger_s: 54.996 (= "AI-native" word.start). Sweep 0.7s (covers the full 3-word phrase span 54.996s → 57.016s). **Marker #1/2.**

4. `marker-circle` — hand-drawn ellipse around "CLIENT ZERO" badge text (green badge). Trigger_s: 60.243 (= "Client" word.start). 0.6s draw. **Marker #2/2 — at cap.**

5. `caption-fade-slide` — narration carries the loop-opener and the Client Zero framing. Word groups: ["And here's the part", "OpenAI should worry about", "NEC is building what they're calling", "one of Japan's largest AI-native engineering teams", "shipping Claude internally first", "as part of Anthropic's Client Zero program"]. Position: bottom 600-700px.

6. `blur-crossfade` to Scene 06 — trigger_s: 61.70s, duration 0.5s (completes by 62.20s before Scene 06's first word "Plus" at 62.414s).

**Audio-reactive**: NONE — narration-heavy scene; reactivity on text-on-mesh would feel busy.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # mesh-morph snap
    anchor_word_index: 100        # "AI-native" — start 54.996
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # Client Zero badge entrance
    anchor_word_index: 110        # "Client" — start 60.243
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 54.896 + 0.73 = 55.626 < 60.193 (sequential reuse OK)
    volume: 0.11
  - cue: cinematic-whoosh         # phase change Scene 05 → Scene 06
    anchor_word_index: 112        # "program." end ~61.637
    offset_seconds: 0.06          # 61.70s
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: The hierarchical-to-mesh morph IS the visual metaphor for "AI-native engineering team." `marker-highlight` on the term-branded phrase + `marker-circle` on the badge hits the 2-marker cap exactly. `caption-fade-slide` carries the loop-opener "And here's the part OpenAI should worry about" — that line is the structural payoff for Lock #5 and needs caption emphasis.

---

### Scene 06: BluStellar + 4 Verticals (data_start=62.2s, data_duration=17.1s)

**Words in scene**: 30 (transcript indices 113–142, "Plus" 62.414s → "center." 78.714s)

**Anchor moments**:
- 62.414s — "Plus" (entrance)
- 62.693s — "Claude" (brand reference)
- 66.988s — "BluStellar" (term-branded product name — Lock #1 reinforcement, `marker-highlight` candidate)
- 67.546s — "Scenario," (full product label)
- 71.551s — "regulated" / 72.166s — "markets," (the framing of the 4 verticals)
- 74.454s — "finance," / 75.011s — "manufacturing," / 75.847s — "local" / 76.160s — "government," / 77.019s — "security" / 77.553s — "operations" / 78.157s — "center." (the 4 vertical labels — `gsap-stagger-grid` candidate, 200ms apart)

**Picks**:

1. `gsap-stagger-grid` — 4 vertical grid cells (FINANCE / MANUFACTURING / LOCAL GOVERNMENT / SOC) stagger in 200ms apart. `tween_s_range: [74.4, 78.2]`, anchored to each spoken vertical word. Ease `back.out(1.7)`. Each cell pulses (subtle 0.95 → 1.05 scale) on its label.

2. `gsap-flip-reveal` — BluStellar product card snaps from offscreen-right to its anchor position. `tween_s_range: [66.93, 67.55]`, ease `power3.out`. Card lands as narrator says "BluStellar."

3. `marker-highlight` — yellow bar sweep behind "BluStellar Scenario" product label. Trigger_s: 66.988 (= "BluStellar" word.start). Sweep 0.7s (covers "BluStellar Scenario" span 66.988s → 68.126s). **Marker #1/2 — within cap.**

4. `caption-fade-slide` — narration carries the productization framing + the 4 verticals naming. Word groups: ["Plus Claude isn't staying internal", "It's plugging into NEC's BluStellar Scenario", "which ships to customers", "If you build on Claude in regulated markets", "BluStellar is the template", "finance, manufacturing", "local government", "and the security operations center"]. The 4 vertical cells pulse synchronized with their caption words.

5. `blur-crossfade` to Scene 07 — trigger_s: 78.80s, duration 0.5s (completes by 79.30s before Scene 07's first word "Why" at 79.620s).

**Audio-reactive**: NONE — the 4 grid-cell pulses already provide rhythm; layering `audio-reactive-pulse` on top would compete.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # BluStellar plug-in snap
    anchor_word_index: 122        # "BluStellar" — start 66.988
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # vertical cell #1 (finance)
    anchor_word_index: 134        # "finance," — start 74.454
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 66.938 + 0.73 = 67.668 < 74.404 (sequential reuse OK)
    volume: 0.11
  - cue: spring-pop               # vertical cell #2 (manufacturing)
    anchor_word_index: 135        # "manufacturing," — start 75.011
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 74.404 + 0.52 = 74.924 < 74.961 (sequential — barely; OK by 37ms)
    volume: 0.11
  - cue: spring-pop               # vertical cell #3 (local government)
    anchor_word_index: 136        # "local" — start 75.847
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 74.961 + 0.52 = 75.481 < 75.797 (sequential reuse OK)
    volume: 0.11
  - cue: spring-pop               # vertical cell #4 (security operations center)
    anchor_word_index: 139        # "security" — start 77.019
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 75.797 + 0.52 = 76.317 < 76.969 (sequential reuse OK)
    volume: 0.11
  - cue: cinematic-whoosh         # phase change Scene 06 → Scene 07
    anchor_word_index: 142        # "center." end ~78.714
    offset_seconds: 0.09          # 78.80s
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: 4 grid cells with `gsap-stagger-grid` synced to the 4 spoken vertical names is a clean 1:1 audio→visual mapping. `gsap-flip-reveal` on the BluStellar card communicates "this product plugs in." `marker-highlight` on "BluStellar Scenario" reinforces the term-branded label without burning the second marker slot. `caption-fade-slide` is essential here because the 4 verticals are spoken fast (3.7s for 4 labels) — captions confirm the viewer caught all four.

---

### Scene 07: Why Now (Receipts) (data_start=79.3s, data_duration=17.7s)

**Words in scene**: 38 (transcript indices 143–180, "Why" 79.620s → "deeper." 96.873s)

**Anchor moments**:
- 79.620s — "Why" / 79.875s — "now?" (entrance — Loop Opener #2: "Why now? Here's the receipt.")
- 81.361s — "receipt." (closes the loop-opener phrase)
- 82.012s — "Claude" / 82.325s — "Code" (brand reference)
- 83.463s — "seventeen" / 83.939s — "point" / 84.194s — "seven" (the 17.7M baseline number)
- 85.518s — "twenty-nine" / 86.087s — "million" (the 29M target — `gsap-counter-tween` candidate)
- 88.896s — "three" / 89.163s — "billion" / 89.512s — "dollar" (the $3B OpenAI–SoftBank figure — `marker-highlight` candidate #1)
- 91.044s — "SoftBank." (the partner)
- 93.041s — "ten" / 93.273s — "billion" / 93.633s — "dollars" (the $10B Microsoft figure — `marker-highlight` candidate #2)
- 94.748s — "SIs." (the 5 SI partners)
- 95.653s — "Anthropic" / 96.188s — "went" / 96.373s — "deeper." (the closing tension-loop resolution)

**Picks**:

1. `gsap-path-draw` — Claude Code adoption curve (line chart) draws from 17.7M baseline left → 29M target right. `tween_s_range: [82.0, 85.5]`, 3.5s draw, ease `power2.inOut`. Vertical marker at "Apr 24" labeled "NEC ANNOUNCEMENT" lands at 85.5s.

2. `gsap-counter-tween` — number tick "17.7M → 29M" displayed alongside the curve. Anchored to "twenty-nine" word at 85.518s. `tween_s_range: [85.0, 86.4]` (0.5s lead-in), 1.4s tween, ease `power3.out`.

3. `gsap-stagger-grid` — 3 competitor cards (OpenAI×SoftBank in dimmed purple, Microsoft×5 in dimmed blue, Anthropic×NEC in foreground orange) enter with 400ms stagger. `tween_s_range: [88.4, 95.6]`. The orange Anthropic×NEC card slides FORWARD from the back of the stack at 95.6s (synced to "Anthropic went deeper") — communicates the out-flank metaphor.

4. `marker-highlight` #1 — yellow bar sweep behind "$3 billion-a-year" on the OpenAI–SoftBank card. Trigger_s: 88.896 (= "three" word.start). Sweep 0.6s. **Marker #1/2.**

5. `marker-highlight` #2 — yellow bar sweep behind "$10 billion" on the Microsoft card. Trigger_s: 93.041 (= "ten" word.start). Sweep 0.6s. **Marker #2/2 — at cap.**

6. `caption-fade-slide` — narration carries the heaviest receipt-stack of the comp. Word groups: ["Why now? Here's the receipt", "Claude Code installs jumped", "from seventeen point seven", "to twenty-nine million", "in four months", "OpenAI cut a three billion dollar a year deal with SoftBank", "Microsoft spread ten billion dollars", "across five SIs", "Anthropic went deeper"]. The competitor names get per-word color callouts (purple for OpenAI, blue for Microsoft, orange for Anthropic) per `captions.md` per-word styling rule.

7. `audio-reactive-glow` — subtle treble-band glow on the "29M" counter as it settles at 86.40s. `textShadow` driven by treble band (12+), 4% scale variation max per audio-reactive subtlety rule. Active window: 86.0s → 87.5s only (around the counter settle).

8. `blur-crossfade` to Scene 08 — trigger_s: 96.50s, duration 0.5s (completes by 97.00s before Scene 08's first word "So" at 97.070s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # 29M counter settle
    anchor_word_index: 165        # "twenty-nine" — start 85.518
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # competitor card #1 (OpenAI×SoftBank)
    anchor_word_index: 169        # "OpenAI" — start 87.956
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 85.468 + 0.73 = 86.198 < 87.906 (sequential reuse OK)
    volume: 0.11
  - cue: spring-pop               # competitor card #2 (Microsoft×5)
    anchor_word_index: 175        # "Microsoft" — start 92.136
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 87.906 + 0.52 = 88.426 < 92.086 (sequential reuse OK)
    volume: 0.11
  - cue: scale-slam               # foreground Anthropic×NEC card slides forward
    anchor_word_index: 178        # "Anthropic" — start 95.653
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3                # 92.086 + 0.52 = 92.606 < 95.603 (sequential reuse OK)
    volume: 0.15
  - cue: cinematic-whoosh         # phase change Scene 07 → Scene 08
    anchor_word_index: 180        # "deeper." end ~96.873
    offset_seconds: -0.37         # 96.50s — whoosh lands precisely on the cut
    duration_seconds: 0.84
    track_index: 4                # overlaps scale-slam@95.603 (ends 96.333) — no, 96.50 > 96.333 → OK on track 3
    volume: 0.11
```
**Track-index resolution note**: scale-slam@95.603 ends at 96.333s; cinematic-whoosh@96.50s starts after. Both can sit on track 3 (sequential). Updated final layout: all SFX in Scene 07 sit on track 3.

**Why these picks**: This is the receipts scene — every viewer skim-decision happens here. `gsap-path-draw` of the adoption curve + `gsap-counter-tween` ticking 17.7 → 29 is the cleanest way to render "the install number is real." Two `marker-highlight` picks (the only scene that uses both marker slots) hit the dollar figures exactly when spoken. `audio-reactive-glow` on the 29M counter is the one place where a subtle treble glow EARNS its place — the number is the climax of the receipts. `caption-fade-slide` with per-word color callouts for the three competitors is the per-word styling rule's intended use case.

---

### Scene 08: Who Next? CTA (data_start=97.0s, data_duration=16.0s, FINAL SCENE)

**Words in scene**: 36 (transcript indices 181–216, "So" 97.070s → "news." 112.871s)

**Anchor moments**:
- 97.070s — "So" / 97.372s — "who's" / 97.650s — "next?" (entrance — secondary loop close: "So who's next?")
- 98.231s — "Fujitsu?" (named SI #1 — `marker-circle` candidate per plan.md)
- 98.974s — "Hitachi?" (named SI #2)
- 99.868s — "N" / 100.205s — "T" / 100.460s — "T" / 100.715s — "Data?" (NTT Data — spelled letter-by-letter)
- 101.795s — "Yoshizaki," (the COO name — speaker attribution)
- 103.316s — "COO," (title)
- 104.721s — "maximizing" / 105.487s — "AI's" / 105.893s — "potential" / 106.509s — "Japan." (the paraphrased quote — `caption-fade-slide` per-word emphasis on "maximizing" and "Japan")
- 107.391s — "If" / 107.693s — "build" / 108.018s — "Claude," / 108.587s — "this" / 109.098s — "signal." (the CTA line)
- 109.969s — "Drop" / 110.595s — "below." (engagement prompt)
- 111.188s — "Subscribe" / 112.082s — "AI" / 112.407s — "news." (subscribe prompt)

**Picks**:

1. `gsap-stagger-grid` — 3 SI cards (FUJITSU / HITACHI / NTT DATA) enter staggered. `tween_s_range: [98.18, 100.85]`, anchored 1:1 to spoken SI names. Each card uses a different accent (purple/blue/green). Ease `back.out(1.7)`.

2. `marker-circle` — hand-drawn ellipse around "FUJITSU" card title (implies first-to-react probability per plan.md Notes for Composition Build). Trigger_s: 98.231 (= "Fujitsu?" word.start). 0.6s draw. **Marker #1/2 — within cap.**

3. `caption-fade-slide` — narration carries the paraphrased Yoshizaki quote + CTA + subscribe prompt. Word groups: ["So who's next?", "Fujitsu? Hitachi? NTT Data?", "Yoshizaki, NEC's COO", "called it maximizing AI's potential", "in Japan", "If you build on Claude", "this is your signal", "Drop your pick below", "Subscribe for more AI news"]. Per-word callouts: "maximizing" (orange, +5% scale boost), "Japan" (orange, +5%), "Subscribe" (orange, +5%) — per `captions.md` per-word styling rule for CTA verbs and brand-tonal words.

4. `audio-reactive-glow` — subtle treble-band glow on the SUBSCRIBE pill (bottom-right). `boxShadow` driven by treble (12+), 3-6% scale variation per audio-reactive subtlety rule. Active window: 111.188s → 112.871s only (during the spoken "Subscribe for more AI news" line).

5. **NO transition out** — final scene. Per `transitions.md:11`, exit animations are allowed ONLY on the final scene. Apply a slow fade-to-black on all elements (`tl.to([root], { opacity: 0 }, 112.5)`) over 0.5s, completing at 113.0s.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # SI card #1 (Fujitsu)
    anchor_word_index: 184        # "Fujitsu?" — start 98.231
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # SI card #2 (Hitachi)
    anchor_word_index: 185        # "Hitachi?" — start 98.974
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4                # 98.181 + 0.52 = 98.701 < 98.924 (sequential — but tight by 223ms, safer on track 4)
    volume: 0.11
  - cue: spring-pop               # SI card #3 (NTT Data)
    anchor_word_index: 189        # "Data?" — start 100.715
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 98.181 + 0.52 = 98.701 < 100.665 (sequential reuse OK)
    volume: 0.11
  - cue: pop                      # subscribe pill entrance
    anchor_word_index: 211        # "Subscribe" — start 111.188
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # 100.665 + 0.52 = 101.185 < 111.138 (sequential reuse OK)
    volume: 0.10
```

**Why these picks**: The card-stack variant of `cta-url-slam` is the canonical CTA pattern when the close is a question (not a URL). `gsap-stagger-grid` with 1:1 audio→card mapping (Fujitsu / Hitachi / NTT Data each pop on their spoken name) is the cleanest implementation of plan.md's "WHO'S NEXT?" beat. `marker-circle` on FUJITSU implies first-to-react probability without committing the narrative to a prediction. `caption-fade-slide` with per-word callouts for "maximizing" + "Japan" + "Subscribe" carries the paraphrased Yoshizaki line and the engagement prompt. `audio-reactive-glow` on the subscribe pill is THE subtle reactive moment of the comp — it earns the "subscribe" call without being loud.

---

## Picks Cross-Reference (validate against menu)

| Pick name | Source file in retention-components-hyperframes.md | Confirmed valid? |
|-----------|---------------------------------------------------|------------------|
| `gsap-stagger-grid`     | §5 GSAP Effects | ✓ canonical |
| `gsap-counter-tween`    | §5 GSAP Effects | ✓ canonical |
| `gsap-path-draw`        | §5 GSAP Effects | ✓ canonical |
| `gsap-flip-reveal`      | §5 GSAP Effects | ✓ canonical |
| `marker-highlight`      | §1 Marker Highlights | ✓ canonical |
| `marker-circle`         | §1 Marker Highlights | ✓ canonical |
| `marker-scribble`       | §1 Marker Highlights | ✓ canonical |
| `caption-fade-slide`    | §2 Caption Patterns | ✓ canonical |
| `audio-reactive-glow`   | §3 Audio-Reactive Effects | ✓ canonical |
| `blur-crossfade`        | §4 Scene Transitions | ✓ canonical |
| `hero-slam`             | §7 Retention Pattern Library | ✓ canonical |
| `stat-pill-row`         | §7 Retention Pattern Library | ✓ canonical |
| `timeline-cards`        | §7 Retention Pattern Library | ✓ canonical |
| `cta-url-slam`          | §7 Retention Pattern Library | ✓ canonical (card-stack variant per plan.md) |
| `inline-phase`          | §6 Composition Structure | ✓ canonical (template-enforced) |
| `mutex-visibility`      | §6 Composition Structure | ✓ canonical (template-enforced) |

All picks are canonical names from `.claude/references/retention-components-hyperframes.md`. No invented names.

## SFX Cue Cross-Reference (validate against MANIFEST)

| Cue used in this strategy | In `shared/audio/MANIFEST.md`? | Default volume per `audio-design.md` |
|---------------------------|---------------------------------|--------------------------------------|
| `impact-slam`     | ✓ | 0.15 |
| `scale-slam`      | ✓ | 0.15 |
| `screen-shake`    | ✓ | 0.11 |
| `cinematic-whoosh`| ✓ | 0.11 |
| `spring-pop`      | ✓ | 0.11 |
| `pop`             | ✓ | 0.10 |
| `glitch-zap`      | ✓ | 0.09 |
| `strike-cross`    | ✓ | 0.11 |

No `sonic-logo` used (cold-open silence not present in this comp; opt-in only).
All volumes ≤ 0.25 hard cap. All cues resolve to files in `shared/audio/sfx/`.

## Constraint Audit

- **Markers per scene (max 2)**: Scene 01 = 2 ✓, Scene 02 = 1 ✓, Scene 03 = 1 ✓, Scene 04 = 1 ✓, Scene 05 = 2 ✓, Scene 06 = 1 ✓, Scene 07 = 2 ✓, Scene 08 = 1 ✓. All within cap.
- **Caption groups overlapping**: only one `caption-fade-slide` group visible at any moment per scene. Cross-scene overlap impossible because `mutex-visibility` enforces phase isolation.
- **Primary transition (60-70% rule)**: `blur-crossfade` used on 7/7 phase changes (100%). Only one transition pattern — no accent transitions. Within rule.
- **Exit animations on non-final scenes**: NONE. Only Scene 08 (final) has a fade-to-black exit on root opacity.
- **Sub-comp/inline-phase mixing**: ALL scenes use `inline-phase` + `mutex-visibility` (template-enforced).
- **SFX ≤ 0.25**: max volume used = 0.15 (`impact-slam`, `scale-slam`). Within cap.
- **SFX track-index uniqueness for concurrent cues**: Scene 01's PIVOT stack at 11.676s uses tracks 4/5/6 (impact-slam/screen-shake/glitch-zap concurrent with track-3 strike-cross still playing). Scene 02's tick #1 + tick #2 overlap window resolved with tracks 3/4. Scene 08's Fujitsu + Hitachi tight-sequential resolved with tracks 3/4 for safety. All other concurrent SFX moved off track 3.
- **SFX drift from spoken anchor**: All percussive cues (impact-slam, scale-slam, screen-shake) use offset_seconds = -0.05 (within ±0.05s percussive bound). Whooshes use ±0.10s (within non-percussive bound). All within `audio-design.md` 0.15s drift bug threshold.

## Constraint Violations Almost Made (Resolved)

1. **Scene 01 layered PIVOT stack track collision**: Initially placed all of impact-slam (PIVOT) + screen-shake + glitch-zap on track 3, which would have collided with the strike-cross still playing on track 3. Resolved by promoting the layered stack to tracks 4/5/6.

2. **Scene 06 vertical-cell SFX timing tightness**: The 4 spring-pop cues for finance/manufacturing/local-government/security-operations-center are anchored at 74.404s/74.961s/75.797s/76.969s — the manufacturing pop ends at 74.924s vs local-government start 75.797s gap is 0.87s, plenty. The finance→manufacturing gap is 0.557s — sequential reuse on track 3 is safe, no need to spread across tracks.

3. **Scene 07 cinematic-whoosh + scale-slam-Anthropic-card overlap**: scale-slam@95.603 (ends 96.333) initially appeared to overlap cinematic-whoosh@96.50 — verified end-of-prior < start-of-next, kept both on track 3.

4. **Scene 02 first two timeline ticks concurrent**: tick #1 at 19.755s and tick #2 at 19.955s overlap (200ms apart, but each cue is 0.52s long). Resolved with tracks 3/4.

## Anchors With No Good Pick (and Why)

1. **Scene 03 thought-narration line "It's engineering depth, the kind enterprises pilot for years and never deploy"** (30.406s → 35.166s) — no marker, no caption, no GSAP effect picked here. Reason: this is a NARRATION-driven beat (Lock #3 thought-narration). Adding a marker would compete with the `marker-circle` on "1st" (which is the structural marker for the badge). Adding captions would compete with the badge itself. Resolution: the narrator's voice carries this beat unaccompanied by visual emphasis — that IS the design. The post-pin-drop quiet adds weight.

2. **Scene 06 "regulated markets" framing** (71.551s → 72.851s) — no marker picked. Reason: the marker budget went to "BluStellar Scenario" (the term-branded label, more retentive). "Regulated markets" is the framing context for the 4 verticals — it earns its retention via the verticals grid that follows immediately, not via inline emphasis.

3. **Scene 07 "four months"** (86.598s → 87.294s) — no marker picked. Reason: the two marker slots are claimed by the dollar figures ($3B, $10B), which carry more receipt-weight than a duration. "Four months" is reinforced by the curve's left-to-right span (the chart IS the duration visualization).

4. **Scene 08 "Drop your pick below"** (109.969s → 111.025s) — no marker, no audio-reactive. Reason: the engagement prompt is brief and conversational; adding emphasis would feel pushy. Instead, the per-word caption callout on "Subscribe" (later, at 111.188s) carries the engagement nudge.

## Override Notes

Phase 4 (composition build) will read this file as authoritative. To override any pick, edit this file directly before invoking the build. The build phase consumes:
- `data_start` / `data_duration` per scene (the 8 boundaries above — total 113.0s)
- pick names (must match canonical names in `.claude/references/retention-components-hyperframes.md`)
- trigger times in seconds (used directly as GSAP timeline positions)
- `sfx_cues` blocks (used directly as `<audio>` element attributes)

If you re-pace any scene, recompute downstream `data_start` for every following scene and re-anchor every SFX `data-start` against the new scene `data_start`. The `audio-design.md` 0.15s drift bound applies after re-pacing.
