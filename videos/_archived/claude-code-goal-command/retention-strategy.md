# Retention Strategy: claude-code-goal-command

**Generated**: 2026-05-12 (Phase 3.5)
**Source inputs**: `plan.md` (5 scenes / 120s budget), `scripts/full-script.md`, `transcript.json` (274 words, 0.05–103.18s actual).
**Note on timings**: Narration completed at **103.18s** vs plan budget of **120s**. All retention picks below use **transcript-anchored timestamps in seconds** (canonical for HyperFrames). The plan's `data_start`/`data_duration` budget is preserved for the composition's phase structure (`#phase1`..`#phase5`), but every retention pick is anchored to its real spoken word — Phase 4 composition build will read these times directly.

---

## Summary Table

| Scene | Pattern (§7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|-------|--------------|------------|----------|----------------|----------------|-------------|
| **S01** Hero / Discovery (thumbnail-grade open) | `hero-slam` | `gsap-stagger-grid`, `gsap-typewriter`, `marker-highlight` ×1 | none | none | `blur-crossfade` | 4 |
| **S02** What `/goal` does | `timeline-cards` (4-card variant) | `gsap-stagger-grid`, `marker-circle` ×1 | `caption-fade-slide` | none | `blur-crossfade` | 4 |
| **S03** Terminal Simulation (ANCHOR) | `code-walkthrough` (terminal-adapted) | `gsap-typewriter` ×3, `gsap-stagger-grid` (verdict bubbles + indicator), `marker-highlight` ×2 | none (terminal IS the readable content) | none | `blur-crossfade` | 6 |
| **S04** How it differs (matrix) | `stat-pill-row` (2×2 matrix variant) | `gsap-stagger-grid`, `marker-highlight` ×1, scale-pulse mid-beat ×1, `marker-circle` mid-beat ×1 | `caption-fade-slide` | none | `blur-crossfade` | 5 |
| **S05** Endcard / CTA (thumbnail-grade close) | `cta-url-slam` (with held final frame) | `gsap-stagger-grid`, `marker-circle` ×1 | none | none | none (final scene; static hold) | 3 |

**Total picks by category**:
- Markers: **6** (`marker-highlight` ×4 in S01/S03 ×2/S04; `marker-circle` ×2 in S02 and S05 — plus 1 marker-circle mid-beat in S04 = effectively 7 distinct marker activations across the comp; max 2/scene cap respected in every scene)
- Captions: **2** scenes (`caption-fade-slide` in S02 and S04 only; S01/S03/S05 omit captions per plan)
- Audio-reactive: **0** (news-explainer information-density tone; audio-reactivity reads as music-driven)
- Transitions: **4** × `blur-crossfade` (single-primary discipline — 100% of scene changes)
- GSAP effects: **typewriter** ×4 (S01 hook line + S03 command + S03 turn-1 + S03 turn-2), **stagger-grid** ×5 (every scene), **scale-pulse** ×1 (S04 mid-beat for 5s pacing rule)

---

## Scene-by-Scene Detail

### Scene 01 — Hero / Discovery (data_start=0s, data_duration=12s)

**Plan window**: 0–12s · **Actual narration window**: 0.05s – 9.36s ("Wait." → "obsolete.")
**Words in scene**: 26 (transcript indices 0–25)

**Anchor moments** (from transcript):
- **0.046s** — "Wait." (idx 0): hook slam, paired with thumbnail-grade lockup
- **1.916s** — "command" (idx 5, end of "new slash command"): topic anchor
- **3.320s** — "Haiku" (idx 10): worker-model brand pill entrance
- **3.611s** — "judges" (idx 11): the verb that flips the architecture frame — TARGET FOR `marker-highlight`
- **3.994s** — "Sonnet" (idx 12): second model-pill entrance
- **6.351s** — "goal." (idx 17): "It's called slash goal" — `◎ /goal active` glyph beat
- **8.754s** — "obsolete." (idx 25): scene close + hand-off to S02

**Thumbnail-grade first-frame spec** (per `.claude/rules/shorts-thumbnail-frames.md`, all 5 elements visible at full opacity from `t=0`, no entrance tweens on these elements — use explicit `tl.set()`):

1. **Topic statement (dominant)**: `◎ /goal active` glyph, 160px Inter Black + 100px JetBrains Mono lockup, orange (`var(--orange)`)
2. **Visual anchor**: the `◎` glyph (Unicode `U+25CE`) itself, with `text-shadow: 0 0 30px rgba(255, 138, 38, 0.4)` warm glow
3. **Brand chrome**: Anthropic + Claude Code lockup top-left, ≥48px logo height
4. **Outcome receipt line**: "Set the finish line once", 52px Inter Regular, `var(--fg-dim)`
5. **Version pill**: "NEW IN v2.1.139", 32px JetBrains Mono in neutral border chip

Hold for 2.4s, then `tl.to(opacity:0, duration:0.5, t=2.4)` to fade the lockup as the "Wait." slam takes the dominant slot.

**Picks**:

1. **`gsap-stagger-grid`** — thumbnail lockup elements (brand chrome, glyph, outcome line, version chip) all start at full opacity at `t=0` via `tl.set()`. NOT a from-tween; the stagger grid is the structural layout primitive, no entrance animation on the held lockup.

2. **`gsap-typewriter`** — Hook context line "There's a new slash command in Claude Code, and Haiku judges Sonnet now."
   - **trigger_s**: `2.45` (cued 0.05s after "Wait." slam lands at 0.046s — actually layered, typewriter starts on the next word "There's" at 1.138s)
   - **CORRECTION (transcript-anchored)**: typewriter line begins at `1.10` so glyph types "There's" character-by-character as the spoken word lands. char-per-second rate ≈ 18 (to finish by `~4.5s`)
   - **gsap-ease**: `power3.out`
   - **plugin**: TextPlugin

3. **`marker-highlight` on "judges"** — orange bar sweeps in behind the verb that flips the architecture frame
   - **anchor**: word index 11 ("judges") @ start `3.611s`
   - **trigger_s**: `3.611` (sweep starts as the word is spoken)
   - **sweep_duration_s**: `0.5` (`width: 0 → 100%`, `power2.out`)
   - **color**: `var(--orange)` at 0.35 alpha

4. **`blur-crossfade` to Scene 02**
   - **trigger_s**: `9.36` (end of "obsolete.") + 0.5s breath = **`9.86`**
   - **duration_s**: `0.5` (opacity 0.4s + blur 0.5s, `sine.inOut`)

**SFX cues** (per `.claude/rules/audio-design.md`; volumes from `shared/audio/MANIFEST.md`):

```yaml
sfx_cues:
  - cue: sonic-logo
    anchor_word_index: 0          # "Wait." at 0.046
    offset_seconds: 0.05          # plays in the cold-open silence before "Wait."
    # Actually fires before word 0 — use absolute t=0.05
    data_start_seconds: 0.05
    duration_seconds: 1.52
    track_index: 3
    volume: 0.60                  # documented exception per MANIFEST.md "Hard cap"
  - cue: impact-slam
    anchor_word_index: 0          # "Wait." at 0.046
    offset_seconds: -0.05         # 50ms percussive lead-in
    data_start_seconds: -0.004    # clamped to 0; effective t=0
    duration_seconds: 0.63
    track_index: 4
    volume: 0.20
  - cue: screen-shake
    anchor_word_index: 0          # "Wait." impact frame
    offset_seconds: 0.0
    data_start_seconds: 0.046
    duration_seconds: 0.52
    track_index: 5
    volume: 0.15
  - cue: spring-pop                # Haiku pill entrance
    anchor_word_index: 10         # "Haiku" at 3.320
    offset_seconds: -0.02
    data_start_seconds: 3.300
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # Sonnet pill entrance
    anchor_word_index: 12         # "Sonnet" at 3.994
    offset_seconds: -0.02
    data_start_seconds: 3.974
    duration_seconds: 0.52
    track_index: 3                # reused — Haiku spring-pop ended at 3.820, Sonnet pop starts at 3.974, no overlap
    volume: 0.15
  - cue: cinematic-whoosh
    anchor_word_index: 25         # "obsolete." ends at 9.358
    offset_seconds: 0.5           # whoosh leads the crossfade
    data_start_seconds: 9.86
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Why these picks**: The thumbnail-grade open (held lockup at full opacity from t=0) is a hard requirement per `.claude/rules/shorts-thumbnail-frames.md` for YouTube auto-thumbnail capture. The `marker-highlight` on "judges" lands on the single verb that carries the counterintuitive frame ("Haiku judges Sonnet" — viewer expects worker hierarchy, gets evaluator architecture). Typewriter on the hook line cues the terminal aesthetic that S03 will fully exploit. Single marker in this scene (well under the 2/scene cap) keeps the eye on the architectural punchline.

---

### Scene 02 — What `/goal` does (data_start=12s, data_duration=20s)

**Plan window**: 12–32s · **Actual narration window**: 10.26s – 28.06s ("Because" → 'achieved.')
**Words in scene**: 50 (transcript indices 26–75)

**Anchor moments**:
- **10.262s** — "Because" (idx 26): connector word, opens explanation
- **11.969s** — "state" (idx 32): introduces the verb of the loop ("You state one completion condition")
- **13.002s** — "condition." (idx 35): first appearance of the coined term — TARGET FOR `marker-circle` (Term Branding lock #1)
- **14.419s** — "Claude" (idx 36): "Claude does a turn" — step 2 narrative anchor
- **16.764s** — "Haiku" (idx 45): step 3 — evaluator named
- **19.504s** — "yes" (idx 53): verdict appears in narrative
- **20.897s** — "reason." (idx 60): "with a short reason" — step 3 close
- **22.197s** — "No" (idx 61): step 4 — no-branch behavior
- **25.633s** — "Yes" (idx 69): step 4 — yes-branch behavior
- **27.446s** — '"achieved."' (idx 75): closes scene, sets up S03's payoff

**Step-card timing plan** (4 cards revealed step-by-step per `.claude/rules/step-by-step-reveal.md`):

| Card | Text | Anchor word | trigger_s |
|------|------|-------------|-----------|
| 1 | "State a completion condition" | "condition." (idx 35) | **12.95** (0.05s before word start to lead spoken cue) |
| 2 | "Claude takes a turn" | "Claude" (idx 36) | **14.40** |
| 3 | "Haiku judges yes / no + reason" | "Haiku" (idx 45) | **16.75** |
| 4 | "Yes → auto-clears, writes 'achieved'" | '"achieved."' (idx 75) | **27.40** (0.05s before) — or as the kicker beat |

**5s pacing audit**: Cards 1→2 = 1.45s gap, 2→3 = 2.35s, 3→4 = **10.65s gap — VIOLATES 5s rule**. Insert mid-beats:
- **Mid-beat A** at `19.50s` — `marker-circle` draws around "reason" (idx 59) on card 3, anchored to "yes" word ("returns yes or no, with a short reason") — fills 16.75 → 19.50 gap (2.75s)
- **Mid-beat B** at `22.20s` — scale-pulse on card 3 anchored to "No" (idx 61) — fills 19.50 → 22.20 (2.70s)
- **Mid-beat C** at `25.63s` — `marker-highlight` on card 3 around "Yes" word, anchored to "Yes" (idx 69) — fills 22.20 → 25.63 (3.43s)
- Card 4 enters at 27.40s — fills 25.63 → 27.40 (1.77s). All gaps now ≤ 5s.

**WAIT — recount: cap of 2 markers/scene is at risk.** Recompute:
- `marker-circle` on "condition." (idx 35) at trigger_s 13.00 = marker #1 (Term Branding lock)
- Mid-beat A: `marker-circle` on "reason" on card 3 = marker #2
- Mid-beat C: `marker-highlight` on "Yes" = marker #3 — **VIOLATES 2/scene cap**

**Resolution**: Drop mid-beat C's marker; replace with a scale-pulse on the same card. Net markers in S02 = 2 (within cap). Mid-beat C becomes:
- **Mid-beat C (revised)** at `25.63s` — scale-pulse on card-3 + color shift the "yes" segment of card 3 from neutral to green, anchored to "Yes" (idx 69). Counts as content morph (item replacement of color state), satisfies 5s rule per `.claude/rules/visual-pacing-5s.md` §"Content morph" allowed beat.

**Picks**:

1. **`gsap-stagger-grid`** — 4 step-cards using explicit `tl.set(opacity:0, y:30, t:0)` + `tl.to(opacity:1, y:0)` at each card's reveal time. Per `.claude/rules/step-by-step-reveal.md` hidden-until-reveal pattern (REQUIRED).
   - Card entrances: **12.95, 14.40, 16.75, 27.40** seconds
   - **ease**: `back.out(1.5)`, duration 0.55s each

2. **`marker-circle` on "condition." (Term Branding lock)** — hand-drawn ellipse stroke
   - **anchor**: word index 35 @ 13.002s
   - **trigger_s**: `13.00`
   - **draw_duration_s**: `0.7` (path-draw via `gsap-path-draw` SVG stroke)
   - **color**: `var(--purple)` (S02 accent per plan)

3. **`marker-circle` on "reason" (mid-beat A)** — second hand-drawn ellipse on card 3 around the word "reason"
   - **anchor**: word index 66 ("reason") @ 23.765s — paired with the narration "with that reason as guidance"
   - **trigger_s**: `19.50` (anchored on first 'reason.' utterance idx 59 @ 20.897s — actually trigger at `20.50` for narration-sync alignment)
   - **CORRECTION**: trigger_s = `20.45` (50ms before "reason." word @ 20.897s for narration sync)
   - **draw_duration_s**: `0.6`
   - **color**: `var(--purple)`

4. **Mid-beat B: scale-pulse on card-3** — content morph beat (not a marker)
   - **trigger_s**: `22.20` (paired with "No means keep working" — "No" word @ idx 61 22.197s)
   - **scale**: `1.0 → 1.04 → 1.0`, duration `0.4s`

5. **Mid-beat C: card-3 'yes' segment color shift** — content morph beat (not a marker)
   - **trigger_s**: `25.63` (paired with "Yes auto-clears" — "Yes" word @ idx 69 25.634s)
   - **css transition**: `color` of inline span from `var(--fg-dim)` → `var(--green)`, duration `0.3s`

6. **`caption-fade-slide`** — narration-synced captions for S02
   - **anchor**: transcript word indices 26–75
   - **style**: `caption-fade-slide` per plan (measured/news-explainer tone)
   - **position**: bottom 700px from bottom (portrait), single group visible at a time per `captions.md`
   - **grouping**: 3–5 words per group (conversational rate)
   - **per-word callouts**: bold + `var(--orange)` on "condition", "Haiku", "yes", "no", "achieved"

7. **`blur-crossfade` to Scene 03**
   - **trigger_s**: `28.06` (end of '"achieved."' word) + 0.5s breath = **`28.56`**
   - **duration_s**: `0.5`, `sine.inOut`

**SFX cues**:

```yaml
sfx_cues:
  - cue: spring-pop                # Step card 1
    anchor_word_index: 35          # "condition." at 13.002
    offset_seconds: -0.05
    data_start_seconds: 12.95
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # Step card 2
    anchor_word_index: 36          # "Claude" at 14.419
    offset_seconds: -0.05
    data_start_seconds: 14.37
    duration_seconds: 0.52
    track_index: 3                 # sequential reuse — card 1 spring-pop ended 13.47
    volume: 0.15
  - cue: spring-pop                # Step card 3
    anchor_word_index: 45          # "Haiku" at 16.764
    offset_seconds: -0.05
    data_start_seconds: 16.71
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # Step card 4 (yes-branch beat)
    anchor_word_index: 75          # "achieved." at 27.446
    offset_seconds: -0.05
    data_start_seconds: 27.40
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh
    anchor_word_index: 75          # transition out
    offset_seconds: 1.12
    data_start_seconds: 28.56
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Why these picks**: The 4-step loop is the explanatory backbone of the video — step-by-step reveal (NOT all-at-once) is mandated by `.claude/rules/step-by-step-reveal.md`. Captions reinforce the named primitives ("condition", "Haiku", "yes", "no", "achieved") that S03 will visualize as terminal artifacts — captions here teach vocabulary that the terminal scene then operationalizes. `marker-circle` on "condition" is the Term Branding lock #1 from plan §Story Lock Placement. Mid-beats B and C are intentionally content morphs (color/scale) instead of new markers — staying inside the 2-marker/scene cap.

---

### Scene 03 — Terminal Simulation (ANCHOR; data_start=32s, data_duration=33s)

**Plan window**: 32–65s · **Actual narration window**: 28.91s – 59.92s ("So" → "loop.")
**Words in scene**: 79 (transcript indices 76–154)

**Anchor moments** (the terminal simulation IS the anchor — every beat is a terminal frame change):
- **28.907s** — "So" (idx 76): connector word
- **29.082s** — "here's" (idx 77): typing intro phrase carries audio
- **30.917s** — "terminal." (idx 85, end of "in your terminal."): terminal frame slides in
- **31.822s** — "You" (idx 86): "You type slash goal" — typewriter begins
- **32.530s** — "goal," (idx 88): command word #1 typed
- **33.494s** — "condition," (idx 91): segue into the condition text
- **34.922s** — '"all' (idx 93, start of '"all tests in test/auth pass...'): the verbatim command begins
- **37.882s** — 'clean."' (idx 106): the verbatim command ends
- **39.183s** — "Claude" (idx 107, "Claude runs turn one"): turn-1 narrative
- **39.728s** — "turn" (idx 109)
- **40.065s** — "one." (idx 110): `◎ /goal active` indicator triggers
- **41.354s** — "Two" (idx 111, "Two tests still fail"): turn-1 output cell
- **42.700s** — "Haiku" (idx 115): "Haiku reads the transcript" — segue to verdict
- **44.755s** — '"no.' (idx 121): verdict-no bubble enters
- **46.067s** — "Auth" (idx 122): "Auth login still broken" — verdict-no reason content
- **46.821s** — 'broken."' (idx 125): verdict-no bubble close
- **47.728s** — "That" (idx 126, "That reason becomes turn two's directive")
- **50.722s** — "Claude" (idx 131, "Claude fixes it"): turn-2 output cell
- **51.733s** — "Haiku" (idx 135, "Haiku checks again")
- **52.801s** — '"Yes.' (idx 138): verdict-yes bubble enters — PAYOFF MOMENT
- **54.193s** — 'Achieved."' (idx 139)
- **54.971s** — "goal" (idx 141, "The goal clears itself")
- **55.482s** — "itself." (idx 143): auto-clear animation
- **56.028s** — "Wait." (idx 144): thought-narration beat — Lock #3 from plan
- **57.282s** — "Haiku" (idx 145, "Haiku just told Sonnet")
- **58.025s** — "Sonnet" (idx 148): both names appear concurrently in narration
- **59.580s** — "loop." (idx 154): scene close

**Picks** (constraint: per the user's special context, NO heavy shader transitions over terminal, NO audio-reactive distortion — use only terminal-complementary primitives: typewriter, marker-highlight on verdict bubbles, glow flash on indicator):

1. **`gsap-typewriter` (command line)** — types `/goal all tests in test/auth pass and the lint step is clean`
   - **trigger_s**: `31.80` (0.02s before "You" idx 86 @ 31.822s) — typewriter starts as narration says "You type"
   - **duration_s**: `~6.0` — finishes by `~37.80s` (anchored to 'clean."' end @ 38.335s)
   - **char_rate**: ~12 chars/sec (matches conversational reading)
   - **plugin**: GSAP TextPlugin
   - **cursor**: blinking JetBrains Mono `▌` cursor on the same line — terminal aesthetic

2. **`gsap-stagger-grid` (indicator scale-slam appearance)** — `◎ /goal active · 00:01` indicator chip appears below the typed command
   - **anchor**: word index 110 ("one.") @ 40.065s — end of "Claude runs turn one"
   - **trigger_s**: `38.50` (right after typewriter command finishes, before turn-1 output) — actually anchored to "Claude" idx 107 @ 39.183s minus 0.5s = `38.68`
   - **CORRECTION (anchor-grounded)**: trigger_s = `38.40` (0.78s after typewriter finish at 37.80, providing a "command accepted" beat)
   - **animation**: `scale: 0 → 1`, `back.out(2)`, duration `0.4s`
   - **glow_flash**: `box-shadow: 0 0 0 → 30px var(--orange)`, duration `0.4s`, layered on the scale-in
   - **color**: orange (`var(--orange)`)

3. **`gsap-typewriter` (turn-1 output cell)** — types simulated output: `Running pytest tests/auth/... · 2 failed in tests/auth/login_test.py`
   - **trigger_s**: `40.50` (0.43s after "one." idx 110 @ 40.065s — gives the indicator beat a 1.5s to settle, then turn-1 typewriter starts)
   - **CORRECTION**: trigger_s = `40.20` (paired with "Two tests still fail" — "Two" idx 111 @ 41.354s minus 1.15s lead so output is mid-type when narration says "two tests fail")
   - **duration_s**: `~4.0` — finishes by `~44.20s`
   - **char_rate**: ~22 chars/sec (faster — simulating real terminal output)

4. **`gsap-stagger-grid` (verdict-no bubble)** — verdict bubble slides in from right with muted red border + Haiku label
   - **anchor**: word index 121 ('"no.') @ 44.755s
   - **trigger_s**: `44.70` (0.05s before "no." word lands)
   - **animation**: `x: 80 → 0`, `opacity: 0 → 1`, `back.out(1.7)`, duration `0.5s`
   - **content**: `Haiku · no · "auth/login_test.js still failing"`
   - **color**: `border: var(--red-dim)`, `background: rgba(red, 0.08)`

5. **`gsap-typewriter` (turn-2 output cell)** — types `Fixing login_test.py · Running pytest tests/auth/... · all green · lint OK`
   - **trigger_s**: `50.70` (0.02s before "Claude" idx 131 @ 50.722s — "Claude fixes it")
   - **duration_s**: `~3.5` — finishes by `~54.20s`
   - **char_rate**: ~22 chars/sec

6. **`gsap-stagger-grid` (verdict-yes bubble)** — green-bordered payoff bubble
   - **anchor**: word index 138 ('"Yes.') @ 52.801s
   - **trigger_s**: `52.75` (0.05s before "Yes." word lands)
   - **animation**: `scale: 0.8 → 1.05 → 1`, `opacity: 0 → 1`, `back.out(2)`, duration `0.55s`
   - **content**: `Haiku · yes — achieved`
   - **color**: `border: var(--green)`, glow `box-shadow: 0 0 30px var(--green) 0.4 alpha`

7. **`marker-highlight` on verdict-yes 'yes — achieved' (PAYOFF marker)** — green sweep behind the verdict text
   - **anchor**: word index 139 ('Achieved."') @ 54.193s
   - **trigger_s**: `54.15`
   - **sweep_duration_s**: `0.6` (`width: 0 → 100%`, `power2.out`)
   - **color**: `var(--green)` at 0.30 alpha

8. **`marker-highlight` on 'achieved' transcript line** — second marker sweep at the bottom transcript line "[goal achieved · 2 turns · ...]"
   - **anchor**: word index 143 ("itself.") @ 55.482s — paired with narration "The goal clears itself"
   - **trigger_s**: `55.48`
   - **sweep_duration_s**: `0.6`
   - **color**: `var(--green)` at 0.25 alpha
   - **NOTE**: 2 markers in S03 — exactly at the 2/scene cap. Acceptable because both anchor the payoff moment ("yes" verdict + "achieved" transcript) which is the entire scene's resolution.

9. **Thought-narration beat (Story Lock #3 from plan)** — small overline appears: "That's the loop." in mono
   - **anchor**: word index 154 ("loop.") @ 59.580s
   - **trigger_s**: `58.50` (paired with "That's the loop" — "That's" idx 152 @ 59.186s minus 0.7s)
   - **CORRECTION**: trigger_s = `59.10` (50ms before "loop." word, content morph beat — text fades in over the terminal frame)
   - **animation**: `opacity: 0 → 1`, `y: 8 → 0`, duration `0.45s`, `power2.out`
   - **NOT a marker** — content morph beat (new text on screen), counts toward 5s pacing rule

10. **`blur-crossfade` to Scene 04**
    - **trigger_s**: `59.92` (end of "loop." word) + 0.5s breath = **`60.42`**
    - **duration_s**: `0.5`, `sine.inOut`

**5s pacing audit (S03)**: typewriter (31.80–37.80, continuous 6s motion) → indicator @ 38.40 (0.60s gap) → turn-1 typewriter @ 40.20 (1.80s gap) → verdict-no @ 44.70 (0.50s gap after turn-1 finishes 44.20) → turn-2 typewriter @ 50.70 (6.0s gap — verdict-no settles ~45.20, gap to 50.70 = **5.5s — VIOLATES 5s rule**). Insert mid-beat: **scale-pulse on indicator chip @ 47.50** (paired with "That reason becomes turn two's directive" — "directive." idx 130 @ 49.806s). New gap 45.20 → 47.50 = 2.30s, then 47.50 → 50.70 = 3.20s. ✓
- Re-list S03 beats: 31.80 typewriter start, 38.40 indicator, 40.20 turn-1 type, 44.70 verdict-no, **47.50 indicator scale-pulse mid-beat**, 50.70 turn-2 type, 52.75 verdict-yes, 54.15 marker-highlight, 55.48 second marker, 59.10 thought-narration, 60.42 exit. Largest gap now 47.50 → 50.70 = 3.20s. ✓

**Adding mid-beat (10b)**:

10b. **Indicator scale-pulse (5s pacing mid-beat)**
   - **trigger_s**: `47.50` (paired with "directive." idx 130 @ 49.806s — anchored 2.3s earlier as a "still working" beat)
   - **animation**: `scale: 1 → 1.05 → 1`, duration `0.4s`, plus a quick orange-glow re-flash
   - **NOT a new marker, NOT a new content element** — but the glow re-flash counts as a content morph (the chip visually re-asserts it's "still active") per `.claude/rules/visual-pacing-5s.md` §allowed beats. Acceptable.

**Constraint compliance**: NO shader transitions inside this scene. NO audio-reactive primitives. Captions OMITTED (the terminal IS the readable content — captions would compete per plan §Retention Component Picks). Markers exactly at the 2/scene cap. 

**Terminal-specific component list (per user's special context)**:
- **Typewriter cursor blink**: GSAP `repeat: -1` is BANNED (deterministic rule). Use `Math.floor(duration / 0.8)` finite repeats — a 32s scene at 0.8s/cycle = ~40 finite repeats. Implemented as a CSS keyframe `@keyframes blink { 0%, 50% { opacity: 1 } 50.01%, 100% { opacity: 0 } }` with `animation-iteration-count: 40` — equivalent and deterministic.
- **Marker-highlight on verdict bubbles**: orange (indicator) and green (yes verdict) sweep markers. NEVER red/no — the muted red border on the verdict-no bubble carries the "fail" reading without needing a marker.
- **Glow flash on `◎ /goal active`**: orange glow at `t=38.40` (entrance) and again at `t=47.50` (mid-beat scale-pulse). Counts as terminal-CRT aesthetic — same family as the cursor blink.

**SFX cues**:

```yaml
sfx_cues:
  - cue: pop                       # Keystroke clicks for typewriter command (3 staggered pops simulating typing)
    anchor_word_index: 86          # "You" at 31.822 — typewriter start
    offset_seconds: 0.0
    data_start_seconds: 31.80
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: pop                       # Mid-command keystroke
    anchor_word_index: 93          # "all" at 34.922
    offset_seconds: 0.0
    data_start_seconds: 34.92
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: pop                       # End-of-command keystroke
    anchor_word_index: 106         # 'clean."' at 37.882
    offset_seconds: -0.10
    data_start_seconds: 37.78
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: scale-slam                # ◎ /goal active indicator entrance
    anchor_word_index: 110         # "one." at 40.065 (end of "turn one")
    offset_seconds: -1.65          # lead 1.65s so indicator slam fires when narration says "Claude runs turn one"
    data_start_seconds: 38.40
    duration_seconds: 0.73
    track_index: 3
    volume: 0.20
  - cue: glitch-zap                # verdict-no bubble entrance
    anchor_word_index: 121         # '"no.' at 44.755
    offset_seconds: -0.05
    data_start_seconds: 44.70
    duration_seconds: 0.52
    track_index: 3
    volume: 0.12
  - cue: scale-slam                # verdict-yes bubble entrance (the payoff)
    anchor_word_index: 138         # '"Yes.' at 52.801
    offset_seconds: -0.05
    data_start_seconds: 52.75
    duration_seconds: 0.73
    track_index: 3
    volume: 0.20
  - cue: spring-pop                # thought-narration overline "That's the loop"
    anchor_word_index: 154         # "loop." at 59.580
    offset_seconds: -0.48
    data_start_seconds: 59.10
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh
    anchor_word_index: 154         # transition out
    offset_seconds: 0.84
    data_start_seconds: 60.42
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Why these picks**: S03 is the anchor scene per plan — the proof beat. The verbatim docs example command is the source-grounded truth (`tmp/source.md` §Set a goal). The terminal-specific picks list (typewriter ×3 + indicator scale-slam + verdict bubbles with marker-highlights + glow flash + thought-narration kicker) is purpose-built to KEEP THE TERMINAL VISIBLE while still triggering a content beat at least every 3-5s — satisfying both `.claude/rules/visual-pacing-5s.md` AND the user's special-context constraint ("DO NOT recommend components that would obscure the terminal"). NO heavy shader transitions, NO audio-reactive distortion, NO captions over the terminal. The two marker-highlights cluster at the resolution moment (54.15 + 55.48s) so the eye is locked on the payoff — the rest of the scene's pacing relies on the typewriter+bubble cadence which is organic to terminal aesthetic.

---

### Scene 04 — How it differs (data_start=65s, data_duration=25s)

**Plan window**: 65–90s · **Actual narration window**: 60.83s – 82.35s ("And" → "all eight.")
**Words in scene**: 59 (transcript indices 155–213)

**Anchor moments**:
- **60.834s** — "And" (idx 155): connector — "And here's why it's not just another prompt"
- **62.541s** — "prompt." (idx 162): closes connector
- **63.852s** — "A" (idx 163, "A prompt asks once")
- **64.270s** — "asks" (idx 165)
- **64.804s** — "once." (idx 166): row 1 left cell anchor — "normal prompt = one turn"
- **65.582s** — "Claude" (idx 167): cell entrance content "Claude answers"
- **68.404s** — "re-prompt" (idx 174): user-action cell content
- **69.448s** — "continue." (idx 176): row 1 left cell complete
- **70.354s** — "Slash" (idx 177, "Slash goal keeps checking"): row 1 right cell entrance
- **71.747s** — "Every" (idx 181)
- **72.421s** — "turn," (idx 182, "Every turn")
- **72.560s** — "fresh" (idx 185): TARGET FOR `marker-highlight` (the architectural differentiator)
- **72.816s** — "model," (idx 186)
- **74.755s** — "judges" (idx 192)
- **76.287s** — "conversation." (idx 197): row 1 right cell complete
- **77.970s** — "If" (idx 198, "If you've ever typed keep going eight times in a row")
- **79.689s** — "eight" (idx 205)
- **80.825s** — "row," (idx 209): row 2 cell entrance (the "8 prompts" stat)
- **82.057s** — "eight." (idx 213): scene close

**Picks** (S04 needs explicit mid-beats per plan §13 to satisfy 5s pacing rule):

1. **`gsap-stagger-grid` (row 1: normal prompt vs /goal)** — 2 cells enter in sequence
   - **row-1 left cell** ("Normal prompt: asks once, control returns to you"): anchor "once." idx 166 @ 64.804s
     - **trigger_s**: `64.75` (0.05s before)
     - **animation**: `x: -40, opacity: 0 → 0, 1`, `back.out(1.5)`, duration `0.55s`
   - **row-1 right cell** ("/goal: keeps checking, condition-driven, fresh-model evaluator"): anchor "Slash" idx 177 @ 70.354s
     - **trigger_s**: `70.30`
     - **animation**: same as left, mirrored direction (`x: 40 → 0`)
   - **stagger calc**: 5.55s gap between row-1 cells = right at the 5s edge. Plan flagged this — keep mid-beat insertion at ~70s. Actually 70.30 IS the right-cell entrance (no gap exceeds 5s here because the cell entrance itself fills the slot — gap from 64.75+0.55=65.30 to 70.30 = **5.0s exactly, on the boundary**). To be safe: insert scale-pulse on row-1 LEFT cell at `~67.50` (paired with "re-prompt to continue" — "continue." idx 176 @ 69.448s minus 2.0s = 67.45).

2. **Mid-beat: scale-pulse on row-1 LEFT cell** (per plan §13 — "insert at ~70s")
   - **trigger_s**: `67.50` (paired with "control returns to you" — "you," idx 173 @ 67.452s)
   - **animation**: `scale: 1 → 1.04 → 1`, duration `0.4s`
   - **NOT a marker** — content morph beat. Inside the cap.

3. **`marker-highlight` on "fresh model"** — purple sweep behind the differentiator phrase on row-1 right cell
   - **anchor**: word index 185 ("fresh") @ 72.560s
   - **trigger_s**: `72.50` (0.06s before)
   - **sweep_duration_s**: `0.6` (sweeps under both "fresh" and "model" — 2-word span)
   - **color**: `var(--blue)` (S04 accent per plan) — actually plan says blue for S04, but `fresh model` is the architectural pivot — use `var(--orange)` to tie back to the indicator beat in S03. Recommend **`var(--purple)`** as a neutral accent compatible with S04's blue scheme.
   - **FINAL**: `var(--purple)` (S04 accent rotation lock is blue, marker uses contrasting purple for emphasis)

4. **`gsap-stagger-grid` (row 2: /goal vs /loop)** — 2 cells enter in sequence
   - **row-2 left cell** ("/goal: condition-driven"): anchor "row," idx 209 @ 80.825s
     - **trigger_s**: `78.00` (paired with "If you've ever typed keep going" — "typed" idx 201 @ 78.609s minus 0.6s)
     - **CORRECTION**: trigger_s = `78.50` (paired with "If you've ever typed" — "If" idx 198 @ 77.970s + 0.5s)
     - **animation**: `x: -40, opacity: 0 → 1`, `back.out(1.5)`, duration `0.55s`
   - **row-2 right cell** ("/loop: time-driven, runs N iterations"): trigger_s `79.05` (+0.55s after left cell finishes entering — quick stagger for the second row, since both are named in the same narration breath)
     - **animation**: mirrored, same params
   - **NOTE**: Row 2 cells are wired at faster stagger (0.55s apart) than row 1 (5.55s apart) because the narration treats row 2 as a single comparison utterance ("this replaces all eight") while row 1 is the slow setup ("a prompt asks once... slash goal keeps checking"). Per `.claude/rules/step-by-step-reveal.md` §"Don't stagger by +0.7s between items inside a 35s phase", row 1's 5s pacing is correct; row 2's quick stagger is acceptable because it's the climax-stat reveal (single narration utterance).

5. **Mid-beat: `marker-circle` on `/loop` cell** (per plan §13 tail-hold mid-beat at ~85s)
   - **anchor**: word index 213 ("eight.") @ 82.057s — but tail-hold extends past narration end
   - **NOTE**: Narration ends at 82.057s ("all eight.") — the plan budgets 65–90s but real content ends at 82.057s. The "tail-hold mid-beat at ~85s" the plan called for is NOT NEEDED because the phase exits at 82.85 (0.50s after "eight.") via blur-crossfade.
   - **REVISION**: Drop this mid-beat. Phase 4 should retime S04 to end at `~83s` (after "all eight." + 0.5s breath), shrinking S04 from `data_duration: 25` to `~22s`. Update transition_out trigger accordingly.

6. **`caption-fade-slide`** — narration-synced captions for S04
   - **anchor**: transcript word indices 155–213
   - **style**: `caption-fade-slide`
   - **per-word callouts**: bold + `var(--blue)` on "prompt", "/goal", "fresh", "model", "eight", "row"

7. **`blur-crossfade` to Scene 05**
   - **trigger_s**: `82.35` (end of "eight.") + 0.5s breath = **`82.85`**
   - **duration_s**: `0.5`, `sine.inOut`

**5s pacing audit (S04)** with the picks above:
- 64.75 left cell → 65.30 finish → 67.50 scale-pulse → 67.90 finish → 70.30 right cell → 70.85 finish → 72.50 marker-highlight → 73.10 finish → 78.50 row-2 left → 79.05 row-2 right → 79.60 finish → 82.35 narration end → 82.85 transition.
- Gaps: 65.30→67.50=2.20, 67.90→70.30=2.40, 70.85→72.50=1.65, 73.10→78.50=**5.40s — VIOLATES 5s rule**

**Resolution**: Insert one more content morph mid-beat at `~76.50` paired with "judges" idx 192 @ 74.755s (or paired with "If" idx 198 @ 77.970s — anchored 1.4s earlier = 76.50).
- **Mid-beat (S04 4th)**: scale-pulse on row-1 right cell anchored to "judges" — `trigger_s = 74.70` (0.05s before "judges" idx 192 @ 74.755s). New gap 73.10 → 74.70 = 1.60s, 74.70 → 78.50 = 3.80s. ✓

**Marker count audit for S04**: `marker-highlight` on "fresh model" = 1 marker. Scale-pulses are content morphs, not markers. ✓ Under 2/scene cap.

**SFX cues**:

```yaml
sfx_cues:
  - cue: spring-pop                # row-1 left cell entrance
    anchor_word_index: 166         # "once." at 64.804
    offset_seconds: -0.05
    data_start_seconds: 64.75
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # row-1 right cell entrance
    anchor_word_index: 177         # "Slash" at 70.354
    offset_seconds: -0.05
    data_start_seconds: 70.30
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # row-2 left cell entrance
    anchor_word_index: 198         # "If" at 77.970
    offset_seconds: 0.53
    data_start_seconds: 78.50
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # row-2 right cell entrance
    anchor_word_index: 198         # "If" — sequential, no overlap
    offset_seconds: 1.08
    data_start_seconds: 79.05
    duration_seconds: 0.52
    track_index: 4                 # concurrent with row-2 left spring-pop (left ends 79.02, right starts 79.05 — overlaps for 0.49s) — use different track
    volume: 0.15
  - cue: cinematic-whoosh
    anchor_word_index: 213         # "eight." at 82.057 — transition out
    offset_seconds: 0.79
    data_start_seconds: 82.85
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Why these picks**: S04 is the differentiation matrix scene. Single marker on "fresh model" carries the architectural punchline (the worker-evaluator split is what makes `/goal` not just another prompt). Three scale-pulse mid-beats (67.50, 74.70) plus the row-2 fast stagger (78.50/79.05) handle the 5s pacing rule WITHOUT spending more markers. Captions provide the narration-sync reinforcement that the visual matrix omits. NOTE for Phase 4: real narration ends at 82.057s — recommend shrinking S04 from `data_duration: 25` to `data_duration: 21` and pushing S05's `data_start` up to `83.35` to tighten the comp; or accept the plan's 25s budget with a 3s silent tail-hold (acceptable, news-explainer pace).

---

### Scene 05 — Endcard / CTA (data_start=90s, data_duration=30s)

**Plan window**: 90–120s · **Actual narration window**: 83.26s – 103.18s ("So." → "community.")
**Words in scene**: 60 (transcript indices 214–273)

**Anchor moments**:
- **83.264s** — "So." (idx 214): connector beat
- **84.147s** — "Next" (idx 215, "Next time you're about to type 'keep going' for the eighth time")
- **85.505s** — '"keep' (idx 222)
- **85.819s** — 'going"' (idx 223)
- **86.527s** — "eighth" (idx 226)
- **87.328s** — "type" (idx 228, "type slash goal instead")
- **87.595s** — "slash" (idx 229)
- **87.885s** — "goal" (idx 230)
- **88.210s** — "instead." (idx 231): "Try `/goal` instead" — CTA pill anchor
- **89.603s** — "State" (idx 232, "State the finish line once")
- **89.963s** — "finish" (idx 234)
- **90.288s** — "line" (idx 235)
- **90.578s** — "once." (idx 236): finish-line statement closes
- **91.216s** — "The" (idx 237, "The docs are at claude.com/docs/en/goal")
- **91.379s** — "docs" (idx 238)
- **91.994s** — "claude" (idx 240)
- **94.073s** — "goal." (idx 248): URL chip target word — TARGET FOR `marker-circle`
- **95.396s** — "Shipped" (idx 249, "Shipped in version 2.1.139")
- **95.837s** — "version" (idx 251)
- **97.927s** — "nine." (idx 258): version number close
- **99.192s** — "If" (idx 259, Dynamous outro line starts)
- **101.456s** — "dynamous" (idx 270)
- **102.559s** — "community." (idx 273): END OF NARRATION

**Thumbnail-grade last-frame spec** (per `.claude/rules/shorts-thumbnail-frames.md`, all entrance animations finish by `~92s` so the final ~10s is fully static — final frame held still as YouTube auto-thumbnail / loop-pause frame):

1. **Topic statement (dominant)**: "Try `/goal`" 140px Inter Black + `◎` glyph 160px (hero anchor)
2. **Visual anchor**: `◎ /goal active` glyph in orange (the consistent brand thread from S01 and S03)
3. **Brand chrome**: Anthropic + Claude Code lockup top-left
4. **Outcome receipt line**: "State the finish line once" 52px Inter Regular
5. **CTA pill**: `claude.com/docs/en/goal` URL chip 44px JetBrains Mono with `marker-circle` drawn around it

**Picks** (S05 minimizes new elements after `t=96s` so the final frame is fully static):

1. **`gsap-stagger-grid` (hero entrance sequence)** — `◎` glyph hero, "Try `/goal`" headline, finish-line outcome, URL chip, brand chrome — ALL enter within `83.5s – 95.5s` window
   - **◎ glyph hero**: trigger_s `83.30` (0.04s after "So." idx 214 @ 83.264s) — scale-slam entrance, `scale: 0 → 1.05 → 1`, duration `0.55s`
   - **"Try `/goal`" headline**: trigger_s `88.16` (0.05s before "instead." idx 231 @ 88.210s) — `y: 40 → 0`, `opacity: 0 → 1`, duration `0.45s`
   - **Finish-line outcome line**: trigger_s `89.55` (0.05s before "State" idx 232 @ 89.603s)
   - **URL chip**: trigger_s `91.95` (0.04s before "claude" idx 240 @ 91.994s) — `x: 40 → 0`, `opacity: 0 → 1`, duration `0.5s`
   - **Version chip "v2.1.139"**: trigger_s `95.35` (0.05s before "Shipped" idx 249 @ 95.396s)
   - **Brand chrome lockup**: visible from `t=83.3` onward (no entrance — held static for thumbnail-grade open of the final frame)

2. **`marker-circle` on URL** — hand-drawn ellipse around `claude.com/docs/en/goal`
   - **anchor**: word index 248 ("goal.") @ 94.073s — end of URL spoken
   - **trigger_s**: `94.00` (0.07s before — draw begins as the URL completes)
   - **draw_duration_s**: `1.0` (slower draw for the closing CTA emphasis)
   - **color**: `var(--orange)` (CTA accent — ties to brand)

3. **Dynamous outro narration handoff** — narration carries the audio from `99.19s` to `103.18s`. NO new visual entrance during this window — the final frame is already at full visibility and held static. Per plan §Data Timing Budget: "narration audibility carries 105-114s; final 114-120s is the deliberate thumbnail hold" — adjusted to actual narration times: narration audibility 99.19–103.18s; final hold 103.18s – 120s (~17s static hold; well above the ≥1.5s minimum).
   - **No new picks during Dynamous beat** — static-only, satisfies `.claude/rules/shorts-thumbnail-frames.md` final-frame rule.

4. **No transition out** — S05 is the final scene. Static hold to end. Per plan §Composition Layout: `transition_out: null`. No fade-to-black.

**5s pacing audit (S05)**:
- 83.30 glyph → 83.85 finish
- → 88.16 headline = **4.31s gap (within 5s)** ✓
- → 88.61 finish
- → 89.55 outcome line = 0.94s gap
- → 90.00 finish
- → 91.95 URL chip = 1.95s gap
- → 92.45 finish
- → 94.00 marker-circle draw = 1.55s gap
- → 95.00 finish (1.0s draw)
- → 95.35 version chip = 0.35s gap
- → 95.80 finish
- → 103.18 narration end = **7.38s gap — VIOLATES 5s rule** unless treated as thumbnail-grade hold

**Resolution** (per `.claude/rules/shorts-thumbnail-frames.md` and `.claude/rules/visual-pacing-5s.md` §"When to relax"): the 5s pacing rule is EXPLICITLY RELAXED for the terminal thumbnail-grade hold. Plan also explicitly invokes this exemption ("explicitly relaxed per `.claude/rules/shorts-thumbnail-frames.md` ≤2.5s … but here we extend to 6s for the loop-pause frame, which the rule's final-frame guidance permits as '≥1.5s static hold' with no upper bound after entrance animations finish"). All entrance animations finish by `95.80s`; narration audibility carries 99.19–103.18s; final static hold 103.18s onward. ACCEPTABLE.

**Marker count audit for S05**: `marker-circle` on URL = 1 marker. ✓ Under 2/scene cap.

**SFX cues**:

```yaml
sfx_cues:
  - cue: scale-slam                # ◎ glyph hero entrance
    anchor_word_index: 214         # "So." at 83.264
    offset_seconds: 0.04
    data_start_seconds: 83.30
    duration_seconds: 0.73
    track_index: 3
    volume: 0.20
  - cue: spring-pop                # "Try /goal" headline entrance
    anchor_word_index: 231         # "instead." at 88.210
    offset_seconds: -0.05
    data_start_seconds: 88.16
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # finish-line outcome line
    anchor_word_index: 232         # "State" at 89.603
    offset_seconds: -0.05
    data_start_seconds: 89.55
    duration_seconds: 0.52
    track_index: 3                 # sequential reuse — previous spring-pop ended 88.68
    volume: 0.15
  - cue: spring-pop                # URL chip entrance
    anchor_word_index: 240         # "claude" at 91.994
    offset_seconds: -0.04
    data_start_seconds: 91.95
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: pop                       # version chip entrance — softer, brand-secondary
    anchor_word_index: 249         # "Shipped" at 95.396
    offset_seconds: -0.05
    data_start_seconds: 95.35
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  # NO SFX during Dynamous outro 99.19–103.18s — narration carries audio uninterrupted
  # NO transition SFX — final scene, no exit
```

**Why these picks**: S05 is the thumbnail-grade close. Every entrance animation finishes by `t=95.80s` so the final ~7s is fully static + the post-narration 17s hold = >24s of motionless thumbnail-grade frame. The `marker-circle` on the URL is the lock #1 CTA element — viewer's eye is drawn to the actionable element. NO transitions out (final scene). NO captions (the on-screen text IS the call-out — captions would compete). The held-still final frame doubles as YouTube auto-thumbnail / loop-pause frame, satisfying both `.claude/rules/shorts-thumbnail-frames.md` requirements (topic + anchor + brand + outcome + CTA all visible at full opacity for the entire hold window).

---

## Picks Cross-Reference

| Pick name | Source file in `retention-components-hyperframes.md` | Confirmed valid? |
|-----------|------------------------------------------------------|------------------|
| `gsap-stagger-grid` | §5 GSAP Effects | ✓ |
| `gsap-typewriter` | §5 GSAP Effects | ✓ |
| `gsap-path-draw` (used inside `marker-circle`) | §5 GSAP Effects | ✓ |
| `marker-highlight` | §1 Marker Highlights | ✓ |
| `marker-circle` | §1 Marker Highlights | ✓ |
| `caption-fade-slide` | §2 Caption Patterns | ✓ |
| `blur-crossfade` | §4 Scene Transitions (Calm CSS primary) | ✓ |
| `hero-slam` (composite) | §7 Retention Pattern Library | ✓ |
| `timeline-cards` (composite) | §7 Retention Pattern Library | ✓ |
| `code-walkthrough` (composite, terminal-adapted) | §7 Retention Pattern Library | ✓ |
| `stat-pill-row` (composite, 2×2 matrix variant) | §7 Retention Pattern Library | ✓ |
| `cta-url-slam` (composite) | §7 Retention Pattern Library | ✓ |
| `inline-phase` (structural) | §6 Composition Structure | ✓ |
| `mutex-visibility` (structural) | §6 Composition Structure | ✓ |

All 14 picks resolve to canonical names in `.claude/references/retention-components-hyperframes.md`. No invented names.

---

## SFX Cue Master List

All cues verified against `shared/audio/MANIFEST.md`:

| Cue | Scenes | Count | Volume cap | Track index strategy |
|-----|--------|-------|-----------|----------------------|
| `sonic-logo` | S01 | 1 | 0.60 (documented exception) | track 3 (cold-open silence, no concurrent narration) |
| `impact-slam` | S01 | 1 | 0.20 | track 4 (concurrent with `screen-shake` on track 5) |
| `screen-shake` | S01 | 1 | 0.15 | track 5 |
| `spring-pop` | S01, S02, S03, S04, S05 | 11 | 0.15 | tracks 3/4 (sequential reuse where non-overlapping; concurrent uses track 4) |
| `cinematic-whoosh` | S01→S02, S02→S03, S03→S04, S04→S05 | 4 | 0.15 | track 3 |
| `pop` | S03 (×3 keystrokes), S05 (×1 chip) | 4 | 0.13 | track 3 |
| `scale-slam` | S03 (indicator + verdict-yes), S05 (◎ hero) | 3 | 0.20 | track 3 |
| `glitch-zap` | S03 (verdict-no) | 1 | 0.12 | track 3 |

**Total SFX cues**: 26 instances across 8 unique cues. All volumes ≤ 0.25 except `sonic-logo` (documented exception). Track-index uniqueness verified for all concurrent groups (S01 cold open: 3+4+5; S04 row-2 cells: 3+4 for the 0.49s overlap; all other cues use sequential track 3 reuse).

---

## Constraint Violations Considered & Resolved

| Constraint | Initial violation | Resolution |
|------------|-------------------|------------|
| `≤2 markers per scene` (§1) | S02 was planning 3 markers (condition + reason + Yes-highlight) | Mid-beat C ("Yes" highlight) downgraded to **scale-pulse + color shift** (content morph, not a marker). Net S02 markers: 2 (within cap). |
| `≤2 markers per scene` (§1) | S03 was planning 3 markers (yes-achieved sweep + 'achieved' transcript sweep + thought-narration as marker) | Thought-narration "That's the loop" downgraded from `marker-highlight` to plain **opacity fade-in text** (content morph). Net S03 markers: 2 (within cap). |
| `5s pacing rule` (visual-pacing-5s.md) | S03 had 5.5s static gap between verdict-no settle (45.20s) and turn-2 typewriter start (50.70s) | Inserted **indicator scale-pulse mid-beat at 47.50s** paired with "directive." word — content morph, not a new element. |
| `5s pacing rule` | S04 had 5.40s gap between marker-highlight settle (73.10s) and row-2 left cell entrance (78.50s) | Inserted **scale-pulse mid-beat at 74.70s** paired with "judges" word. |
| `single primary transition` (transitions.md §Selection rule) | Plan locked 4× `blur-crossfade`. Considered adding `cinematic-zoom` for S02→S03 anchor handoff. | **REJECTED**. Kept all 4 transitions as `blur-crossfade`. Single-transition discipline preserved per plan §Composition Layout `accent_transitions: []`. |
| `terminal obscuration` (user's special context) | Considered `audio-reactive-glow` on the ◎ indicator | **REJECTED**. Replaced with deterministic CSS keyframe + GSAP scale-pulse mid-beat. No audio-reactive primitives in S03. |
| `terminal obscuration` | Considered shader transition (`glitch`, `chromatic-radial-split`) between turn-1 → turn-2 | **REJECTED**. Used plain `gsap-typewriter` for both turns + verdict bubble entrance. Terminal remains visible throughout. |
| `thumbnail-grade open` (shorts-thumbnail-frames.md) | Initial draft considered `tl.from()` on the thumbnail lockup elements | **REJECTED**. Per the rule, thumbnail elements MUST be at full opacity at `t=0` — use `tl.set()` only; no entrance tween. Fade-out via `tl.to(opacity:0)` at `t=2.4`. |
| `narration ≠ budget` discrepancy | Plan budgets 120s but narration ends at 103.18s | Documented: all retention picks anchored to **transcript-actual times in seconds**, not plan-budget times. S04 and S05 narration ends earlier than plan budget — S05's terminal thumbnail hold absorbs the extra ~17s as deliberate static frame (acceptable per thumbnail-frames rule's "no upper bound after entrance animations finish"). |

---

## Anchors Without a Good Pick

| Anchor | Reason no pick assigned |
|--------|------------------------|
| "Sonnet" idx 12 @ 3.994s (S01 model pill #2) | Already gets a `spring-pop` SFX on entrance + `marker-highlight` lands on the adjacent verb "judges". A third visual treatment on "Sonnet" would compete with the marker. Leave as plain pill entrance. |
| "command" idx 5 @ 1.916s (S01 topic word) | Carried by the held thumbnail lockup at `t=0` (the lockup IS the topic statement). Adding a marker here would compete with the static thumbnail frame. |
| "Haiku" repeat utterances in S02/S03 (idx 45, 115, 135, 145) | After the first marker-circle on "condition" in S02 establishes the term-branding, repeat "Haiku" utterances don't need re-marking. Captions reinforce the name via per-word callout (bold orange). |
| "loop." idx 154 (S03 close) | The thought-narration text fade-in IS the visual beat (content morph). A marker on the word would be redundant with the overline reveal. |
| Dynamous outro line 99.19–103.18s (S05) | Intentionally NO new visual picks during this window. Final-frame thumbnail rule requires entrance animations to finish ≥1.5s before the hold. Narration carries audio; visuals remain static for thumbnail-grade close. |

---

## Override Notes

Phase 4 (composition build) reads this file as authoritative. To override any pick, edit this file directly before invoking the build. Key Phase 4 wiring reminders:

1. **All marker triggers use word `.start` from transcript.json** — no manual retiming.
2. **Use the hidden-until-reveal pattern** (`tl.set()` at t=0 + `tl.to()` at reveal time) per `.claude/rules/step-by-step-reveal.md` — NEVER `tl.from()` on the step-cards or matrix cells.
3. **S03 cursor blink**: deterministic CSS keyframe with finite `animation-iteration-count`, NOT `repeat: -1`.
4. **S05 final frame**: every entrance animation finishes by `t=95.80s`; narration plays 99.19–103.18s with NO visual changes; static hold 103.18s onward as YouTube auto-thumbnail / loop-pause frame.
5. **S04 narration ends at 82.057s** but plan budgets `data_duration: 25` ending at `t=90s`. Two options: (a) shrink S04 to 17s data_duration (ends at 82.85s) and push S05 to data_start=83.35; OR (b) accept plan budget and allow 7s silent tail-hold of the matrix before transition. **Recommended: option (a)** — tighter pacing, full comp ends at ~103.7s + thumbnail hold to ~110s (well under plan's 120s budget).
6. **No background music** (template constraint). Narration + SFX only.
7. **`meta.json` `dynamousPromotion: false`** per plan §Notes for Composition Build §12.
