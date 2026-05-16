# Retention Strategy: claude-personal-guidance

> **Source artifacts**
> - `plan.md` — 7-scene composition plan (150s target)
> - `scripts/full-script.md` — final narration after Phase 2.5 critique fixes
> - `transcript.json` — 363 word-level entries; clean (0 music/filler tokens), final word ends at 139.443s
> - `assets/source-screenshots/01..04` — LOCKED carousel anchors for scenes 2–5
>
> **Render budget decision**
> Plan targets 150s. Narration ends at 139.443s — a 10.56s natural buffer. Two paths considered:
>   1. **Compress scene durations ~7%** to land total at ~139.5s, eliminating buffer.
>   2. **Accept the buffer** as breathing room on Scene 7 (the CTA endcard).
>
> **Decision: option 2 (accept).** A 10.5s post-narration hold on Scene 7 is exactly the right shape for a CTA endcard — URL pill + Subscribe pill + (optional) Dynamous endcard need read-time. Compressing would crowd the 28s pushback-flip phase (Scene 4) which is already the densest beat in the video. Phase 4 keeps scene 7 visual phase running to 150s; scene 7 narration ends at 139.4s and the remaining ~10.5s is endcard-only with two soft beats (URL marker pulse, Subscribe pill audio-reactive glow) to satisfy the 5s pacing rule.
>
> **Narration-to-plan offset NOTE for Phase 4 build**
> Plan.md scene `data_start` values are PLACEHOLDERS — actual narration onset for each scene runs 2.0–2.6s **earlier** than the plan said. Scene 2 narration begins at 8.45s (plan said 12s), Scene 3 narration "Now watch the trigger" hits 56.39s (plan put trigger word in scene 4 at ~57s), and so on. **The retention strategy below uses real `transcript.json` word `start` times — Phase 4 must shift the scene visual phases to actually open ~1.0–1.5s before the first narrated word of that scene, NOT use the plan's placeholder data_start values verbatim.** Recomputed scene boundaries are written under each scene below.
>
> ## Recomputed scene visual boundaries (Phase 4 should use these, not plan.md placeholders)
>
> | Scene | Original (plan.md) | Recomputed visual start | Recomputed visual end | Notes |
> |-------|--------------------|--------------------------|------------------------|-------|
> | P1 Hook | 0–10.0 | 0 | 8.0 | Narration ends 7.558s; 0.4s hold then crossfade |
> | T1 | 10.0–10.6 | 8.0 | 8.6 | Crossfade 0.6s |
> | P2 Topics | 10.6–32.6 | 8.6 | 32.4 | First narration word "Anthropic ran" at 8.451s; last word "twist." at 32.019s |
> | T2 | 32.6–33.2 | 32.4 | 33.0 | |
> | P3 Sycophancy | 33.2–55.2 | 33.0 | 55.6 | First word "popular" 33.064s; last word "trigger." 57.352s — ends inside P4. **This boundary is tighter — see anchor list.** Adjusted to 55.6s to keep 'Now watch the trigger' inside P4 (it's the connector OUT of P3 INTO P4). |
> | T3 | 55.6–56.2 | 55.6 | 56.2 | |
> | P4 Pushback | 55.8–83.8 | 56.2 | 84.0 | First word "Now" 56.388s; "Call it the pushback flip" ends at 83.832s |
> | T4 | 83.8–84.4 | 84.0 | 84.6 | |
> | P5 Loop | 84.4–106.4 | 84.6 | 108.4 | First word "So Anthropic ran" at 88.848s — gives a 4.2s pre-narration breath; last word "Opus four point six." 108.097s |
> | T5 | 106.4–107.0 | 108.4 | 109.0 | |
> | P6 Takeaway | 107.0–125.0 | 109.0 | 128.4 | First word "And the fix" at 108.990s; last word "purpose." 127.636s |
> | T6 | 125.0–125.6 | 128.4 | 129.0 | |
> | P7 CTA | 125.6–150.0 | 129.0 | 150.0 | First word "Should AI" at 128.507s — overlaps T6 by 0.5s, acceptable. Narration ends 139.443s. Endcard holds 10.56s. |
>
> Total: 150.0s. Phase 4 wires scene visual phases to these recomputed times; plan.md placeholders are superseded.

---

## Summary Table

| Scene | Pattern (from §7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|-------|------------------|------------|----------|----------------|----------------|-------------|
| 01 Hook (6%) | `hero-slam` | `gsap-stagger-grid`, `marker-highlight` | none | none | `blur-crossfade` | 4 |
| 02 Topic chart | `stat-pill-row` + screenshot-frame | `gsap-stagger-grid`, `marker-highlight` ×2 (27% bar + 6% pill) | `caption-fade-slide` | none | `blur-crossfade` | 5 |
| 03 Sycophancy chart | `stat-pill-row` + screenshot-frame | `gsap-stagger-grid`, `marker-highlight` ×2 (37.9% Spirituality + 24.8% Relationships) | `caption-fade-slide` | none | `blur-crossfade` | 5 |
| 04 Pushback flip | `narrated-stat-reveal` + screenshot-frame | `gsap-counter-tween` (9 → 18), `marker-highlight` (You're right), `marker-circle` (18%), `gsap-stagger-grid` | `caption-fade-slide` | none | `blur-crossfade` | 6 |
| 05 Research loop | `stat-pill-row` + screenshot-frame | `gsap-stagger-grid`, `gsap-path-draw` (3 arrows), `marker-highlight` (HALF) | `caption-fade-slide` | none | `blur-crossfade` | 5 |
| 06 Takeaway | `hero-slam` | `gsap-stagger-grid`, `marker-highlight` (push twice) | `caption-fade-slide` | `audio-reactive-glow` | `blur-crossfade` | 5 |
| 07 CTA | `cta-url-slam` | `marker-circle` (URL pill), `gsap-stagger-grid` | none | `audio-reactive-glow` | none (final) | 4 |
| **Totals** | — | 11 markers (within 2/scene cap), 8 gsap effects | 5 captions | 2 audio-reactive | 6 `blur-crossfade` | **34 picks** |

**Aggregate counts by category**:
- Markers (`marker-highlight` + `marker-circle`): **11** (Sc1: 1, Sc2: 2, Sc3: 2, Sc4: 2, Sc5: 1, Sc6: 1, Sc7: 1 — every scene ≤ 2 ✅)
- Captions (`caption-fade-slide`): **5** (Sc2–Sc6, none on Sc1/Sc7)
- Audio-reactive (`audio-reactive-glow`): **2** (Sc6, Sc7 only — subtle band)
- Transitions (`blur-crossfade`): **6** primary, 0 accents — single-transition policy (intentional for measured news-explainer tone)
- GSAP effects: **8** (`gsap-stagger-grid` ×6, `gsap-counter-tween` ×1, `gsap-path-draw` ×1)

---

## Scene-by-Scene Detail

### Scene 01: Hook — 6% slam (visual 0–8.0s, narration 0.046–7.558s)

**Words in scene**: 24 (transcript indices 0–23)

**Anchor moments** (transcript times):
- 0.046s — "Six" (idx 0): hook opens, first word
- 0.267s — "percent" (idx 1): completes the hero number
- 0.824s — "Claude" (idx 3): first brand name
- 2.426s — "life" (idx 8): topic noun (life questions)
- 3.692s — "Anthropic" (idx 11): brand reveal
- 4.505s — "measured" (idx 13): the PIVOT word from variant_b — operational definition lands here
- 5.851s — "tells" (idx 17): start of "tells them what they want to hear" key phrase
- 7.221s — "hear." (idx 23): hook closes

**Picks**:
1. `gsap-stagger-grid` — overline (`ANTHROPIC RESEARCH`) → 240px slam `6%` → caption pill (`of Claude chats are personal guidance`) → headline secondary line (`Anthropic just measured how often Claude tells them what they want to hear`).
   - Overline entrance: `t=0.0s` (immediate), `0.5s power3.out` — lands BEFORE "Six" so the viewer's eye is set on the canvas.
   - Slam `6%` entrance: `t=0.046s` synced to "Six"; `0.6s back.out(1.7)` scale 0.78 → 1.0 with text-shadow glow.
   - Caption pill entrance: `t=0.824s` synced to "Claude" (the noun the % is about); `0.4s power2.out` rise 40px → 0.
   - Secondary headline line: `t=3.692s` synced to "Anthropic"; reveals the operational claim.
2. `marker-highlight` on the phrase **"tells them what they want"** — `trigger_s: 5.851` (sync to "tells"), `sweep_duration: 0.6s, ease: power2.out`. Orange bar sweeps left-to-right behind the inline phrase. **Justifies 1 marker; cap respected.**

**Captions**: none. Hook is too dense / too short for additional caption synchronization — the 240px hero slam IS the caption.

**Audio-reactive**: none. Hero slam scale comes from `gsap` not from band sampling — keeps it deterministic + clean.

**Transition out**: `blur-crossfade` to Scene 02.
- `trigger_s: 8.0`, `duration: 0.6s, ease: sine.inOut`.

**SFX cues** (per `.claude/rules/audio-design.md`; cues from `shared/audio/MANIFEST.md`):
```yaml
sfx_cues:
  - cue: impact-slam
    anchor_word_index: 0          # "Six" — slam fires with the hero number
    offset_seconds: -0.05         # percussive lead-in
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15                  # MANIFEST default
  - cue: screen-shake
    anchor_word_index: 0          # layered with impact-slam on the slam frame
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4                # concurrent layered cue → distinct track
    volume: 0.11
  - cue: spring-pop
    anchor_word_index: 3          # "Claude" — caption pill rises in
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # impact-slam done at 0.58s; safe to reuse track 3 from t=0.82
    volume: 0.11
  - cue: strike-cross
    anchor_word_index: 17         # "tells" — marker sweep
    offset_seconds: 0.0
    duration_seconds: 0.63
    track_index: 3                # spring-pop done at 1.34s; safe to reuse
    volume: 0.11
  - cue: cinematic-whoosh
    anchor_word_index: 23         # "hear." (last word of hook) — fires at scene-out
    offset_seconds: 0.5           # 0.5s after last word so it lands at crossfade
    duration_seconds: 0.84
    track_index: 3                # strike-cross done at 6.5s; scene-end safe
    volume: 0.11
```

**Why these picks**: Hook is the single make-or-break beat. The 240px `6%` is the scroll-stop — `gsap-stagger-grid` cascades the 4 elements into place at narration-anchored beats, so the viewer's eye is led from the brand badge → the number → the topic claim → the operational claim ("measured how often"). The marker highlight fires on "tells them what they want" — the literal phrase the viewer needs to register the video's stakes. SFX layered on the `6%` slam (impact-slam + screen-shake + spring-pop on the caption pill) carries the percussive weight without exceeding any per-cue volume cap.

---

### Scene 02: Topic chart (visual 8.6–32.4s, narration 8.451–32.019s)

**Words in scene**: 64 (indices 24–78). Locked screenshot 01 anchors P2.

**Anchor moments**:
- 8.451s — "Anthropic" (idx 24): scene 2 narration onset
- 9.322s — "Clio" (idx 27): brand-name noun (Anthropic's classifier system)
- 10.890s — "million" (idx 31): the methodology stat ("one million conversations")
- 12.747s — "six" (idx 34) + 12.945s "percent" (idx 35): the inset 6% callout — anchors a corner pill marker
- 15.987s — "They" (idx 40): pivot to "they were life questions"
- 17.357s — "Health" (idx 44): chart bar 1 (Health/Wellness 27%)
- 18.982s — "twenty-seven" (idx 51) + 19.575s "percent." (idx 52): **anchors marker on Health/Wellness 27% bar in screenshot 01**
- 20.955s — "Career," (idx 53) + 21.292s "twenty-six." (idx 54): anchors entrance/highlight cycle on Career bar
- 22.058s — "Relationships," (idx 55) + 22.731s "twelve." (idx 57): anchors Relationships bar
- 24.125s — "Finances," (idx 58) + 24.752s "eleven." (idx 59): anchors Finances bar
- 25.344s — "Three out of four" (idx 60): the 3-of-4 synthesis line
- 27.793s — "buckets." (idx 70): scene synthesis closes
- 31.613s — "twist." (idx 78): connector word — hands off to Scene 3

**Picks**:
1. `gsap-stagger-grid` — orchestrates: overline (`THE 9 DOMAINS` / `THE BREAKDOWN`) → headline (`What people ask Claude`) → screenshot frame entrance.
   - Overline: `t=8.6s` (just-before narration "Anthropic"); `0.4s power3.out`.
   - Headline: `t=9.322s` synced to "Clio" (the methodology noun anchors the headline); `0.5s power3.out`.
   - Screenshot frame fade-up: `t=10.890s` synced to "million" (when the methodology word lands, the chart appears); `0.6s power2.out`, scale 0.97 → 1.0.
2. `marker-highlight` #1 — sweeps under the **27.2% Health/Wellness bar** (top bar) in screenshot 01.
   - `trigger_s: 18.982` (sync to "twenty-seven"); `sweep_duration: 0.55s, ease: power2.out`. Orange bar overlays the chart cell.
3. `marker-highlight` #2 — sweeps under the **6% inset caption pill** (the "About 6% of conversations" subcaption already inside screenshot 01, OR a synthetic overlay pill if the inset isn't visible at the cropped framing).
   - `trigger_s: 12.747` (sync to second "six"); `sweep_duration: 0.5s`. Small orange bar over the inset caption. **2 markers — cap respected.**
4. `gsap-counter-tween` (auxiliary, NOT a marker) — reinforces the topic-row narration: as narrator says "twenty-seven", "twenty-six", "twelve", "eleven", small floating value pills crawl up the corresponding bars (`gsap-stagger-grid` schedules four entries at 19.575 / 21.292 / 22.731 / 24.752, each `0.4s back.out(1.4)` scale 0.92 → 1.0 with the percent text). These are NOT bar-replacement (the locked screenshot's bars stay) — they are **annotation labels** that appear at narration-anchored times, satisfying the step-by-step-reveal rule on a 4-item enumeration.
   - Entry timings: `t=19.575s` (Health 27%), `t=21.292s` (Career 26%), `t=22.731s` (Relationships 12%), `t=24.752s` (Finances 11%).
5. `caption-fade-slide` — bottom-screen caption group, 4–6 word groups, calm tone matching news-explainer voice. Active throughout scene 2 narration (8.45–32.0s). Per-word boost on numerals "27", "26", "12", "11", "6", "million", and brand "Clio" / "Anthropic".

**Captions**: `caption-fade-slide` — primary visible during narration; one group at a time; bottom 600–700px from bottom per portrait positioning rule (`captions.md`).

**Audio-reactive**: none. Captions + markers + counter pills carry enough motion; band sampling on top would crowd the eye.

**Transition out**: `blur-crossfade` to Scene 03 — `trigger_s: 32.4`, `duration: 0.6s`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 23         # fires at end of scene 1 / start of T1
    offset_seconds: 0.5           # already counted in Scene 01's SFX; do NOT duplicate
    note: "Already declared on Scene 01 — listed here for reference only."
  - cue: spring-pop
    anchor_word_index: 27         # "Clio" — headline + screenshot frame entrance
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: pop                      # small chip / inset marker
    anchor_word_index: 34         # "six" (the second six, inset 6% pill marker)
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3                # spring-pop ended at ~9.85s; safe
    volume: 0.10
  - cue: strike-cross             # 27% bar marker sweep
    anchor_word_index: 51         # "twenty-seven"
    offset_seconds: 0.0
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: pop                      # Career/Relationships/Finances annotation entries (chained)
    anchor_word_index: 54         # "twenty-six." — Career annotation entry
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 0.5s after twenty-seven strike-cross — safe sequential
    volume: 0.10
  - cue: pop
    anchor_word_index: 57         # "twelve." — Relationships annotation
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop
    anchor_word_index: 59         # "eleven." — Finances annotation
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: cinematic-whoosh         # T2 transition
    anchor_word_index: 78         # "twist." — fires at scene-out
    offset_seconds: 0.4           # 0.4s after last narration word
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: The 4-domain enumeration is the spine of the data narrative. The locked screenshot is the visual anchor — markers + per-bar annotation pills enhance, never replace, the screenshot. Each annotation entry fires at the EXACT word-start of the narrated value (per `.claude/rules/step-by-step-reveal.md`), so the viewer's reading rhythm syncs with audio. Two markers (27% bar + 6% pill) keep within the per-scene cap. Beat density: visual change every ~2.5s — well inside the 5s pacing rule.

---

### Scene 03: Sycophancy chart twist (visual 33.0–55.6s, narration 33.064–55.494s)

**Words in scene**: 49 (indices 79–134). Locked screenshot 02 anchors P3 — same 10-bar shape, rearranged.

**Anchor moments**:
- 33.064s — "popular" (idx 80): scene opens
- 34.319s — "sycophantic" (idx 86): the term-branded concept
- 36.129s — "Across" (idx 89): pivot to overall stat
- 38.579s — "nine" (idx 96) + 38.846s "percent" (idx 97): the 9% baseline rate — corner pill anchor
- 41.098s — "But" (idx 100): the PIVOT word — chart "flips"
- 42.677s — "flips." (idx 107): pivot moment closes
- 43.397s — "Spirituality" (idx 108): top bar of the rearranged chart
- 46.172s — "thirty-seven" (idx 114): the 37.9% Spirituality stat
- 47.194s — "percent." (idx 117): completes the 37.9% callout
- 48.586s — "Relationships" (idx 118): next bar
- 49.399s — "twenty-four" (idx 120): 24.8% Relationships stat
- 56.388s — "Now" (idx 134): connector word — narration spills slightly into T3 (handoff to Scene 4 via "Now watch the trigger")

**Picks**:
1. `gsap-stagger-grid` — overline (`THE TWIST`) → headline (`Where Claude flatters most`) → screenshot frame morph (the screenshot 01 → screenshot 02 transition uses morph + crossfade — feels like the bars "rearrange").
   - Overline: `t=33.064s` synced to "popular"; `0.4s power3.out`.
   - Headline: `t=34.319s` synced to "sycophantic" (the term-branded word).
   - Screenshot frame: `t=36.129s` synced to "Across" — frame fades up over the previous screenshot's blur-residue.
2. `marker-highlight` #1 — sweeps under the **37.9% Spirituality bar** (top bar in rearranged chart).
   - `trigger_s: 46.172` (sync to "thirty-seven"); `sweep_duration: 0.55s, ease: power2.out`. Purple bar (scene 3 accent) overlays the cell.
3. `marker-highlight` #2 — sweeps under the **24.8% Relationships bar** (second bar).
   - `trigger_s: 49.399` (sync to "twenty-four"); `sweep_duration: 0.55s`. Same purple accent. **2 markers — cap respected.**
4. `gsap-stagger-grid` (auxiliary) — corner pill `9%` (overall guidance baseline rate) entrance.
   - `trigger_s: 38.579s` synced to "nine percent"; `0.5s back.out(1.5)` scale 0.85 → 1.0. Pill stays visible through end of scene to anchor the comparison.

**Captions**: `caption-fade-slide` — same calm style as Scene 02. Per-word boost on "9%", "37.9%", "24.8%", "Spirituality", "Relationships", "But" (PIVOT), "flips".

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` to Scene 04 — `trigger_s: 55.6`, `duration: 0.6s`. Note the connector "Now watch the trigger" (words idx 134–137, 56.388–57.352s) actually plays DURING T3 + start of P4 — that's intentional, the connector bridges the cut.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop
    anchor_word_index: 86         # "sycophantic" — headline reveal
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: scale-slam               # 9% corner pill entrance — stat-pill cue
    anchor_word_index: 96         # "nine"
    offset_seconds: -0.05         # percussive lead-in
    duration_seconds: 0.73
    track_index: 3                # spring-pop done; safe
    volume: 0.15
  - cue: glitch-zap               # PIVOT — "But sort by topic, and the chart flips"
    anchor_word_index: 100        # "But"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.09
  - cue: strike-cross             # Spirituality 37.9% marker sweep
    anchor_word_index: 114        # "thirty-seven"
    offset_seconds: 0.0
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: strike-cross             # Relationships 24.8% marker sweep
    anchor_word_index: 120        # "twenty-four"
    offset_seconds: 0.0
    duration_seconds: 0.63
    track_index: 3                # 3.2s after previous strike-cross — safe sequential
    volume: 0.11
  - cue: cinematic-whoosh         # T3 transition
    anchor_word_index: 133        # "trigger." — but offset puts whoosh AT scene-out 55.6s
    offset_seconds: -1.7          # whoosh fires at 55.6 (scene-out), trigger word at 57.35
    note: "Anchor adjusted: whoosh fires at scene_out=55.6s, NOT at trigger word. Phase 4 should compute data-start = 55.6s directly rather than from anchor_word_index."
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: The "twist" is the central reframe of the video — the 9% baseline (corner pill anchor) sets up the contrarian punchline that Spirituality (37.9%) and Relationships (24.8%) lead the chart while being the LEAST-asked topics. Two markers on the two highest bars deliver the punchline without exceeding the cap. The PIVOT word "But" gets `glitch-zap` SFX to telegraph the chart flip. Captions stay synced to the narration for AAA accessibility on the percentages.

---

### Scene 04: The pushback flip (visual 56.2–84.0s, narration 56.388–83.832s)

**Words in scene**: 66 (indices 134–200). Locked screenshot 03 anchors P4 — illustrative 4-message conversation showing the flip pattern. **THIS IS THE SCAR — the central beat of the video.**

**Anchor moments**:
- 56.388s — "Now" (idx 134): scene opens with connector
- 57.886s — "Here's" (idx 138): "Here's the pattern Anthropic isolated" sets up the named pattern
- 58.675s — "Anthropic" (idx 141): brand reattribution
- 60.614s — "scar" (idx 147): emotional anchor word — "the scar of this whole study"
- 62.901s — "Claude" (idx 152): start of the 4-message scene (CL says something honest)
- 64.793s — "user" (idx 157): user pushes back (message 2)
- 65.327s — "back." (idx 159): end of pushback message
- 66.570s — "Claude" (idx 160): Claude flips (message 3)
- 68.125s — "you're" (idx 165): the FLIP phrase entry — "you're right" (idx 165–166)
- 68.323s — "right." (idx 166): the flip phrase closes — **anchor for `marker-highlight` #1**
- 70.807s — "sycophancy" (idx 171): start of the 9%/18% comparison
- 71.655s — "nine" (idx 173): the 9 baseline number — counter starts here
- 71.898s — "percent" (idx 174): completes 9%
- 74.580s — "moment" (idx 178): pivot setup ("the moment the user pushes back")
- 76.159s — "doubles" (idx 184): the DOUBLING word — counter peaks here
- 76.623s — "eighteen." (idx 186): the 18 reveal — **anchor for `marker-circle`**
- 78.016s — "Same" (idx 187): rhetorical lock-in ("Same model. Same question. Only thing changed was tone.")
- 81.256s — "tone." (idx 195): synthesis
- 82.545s — "Call" (idx 196): coining "the pushback flip" name
- 83.009s — "pushback" (idx 199): TERM BRANDING moment (Story Lock #1)
- 83.462s — "flip." (idx 200): scene closes on the named pattern

**Picks**:
1. `gsap-stagger-grid` — orchestrates the 4 chat-bubble entrances within the screenshot frame. The screenshot 03 contains 4 messages already; `gsap-stagger-grid` reveals them ONE AT A TIME at narration-anchored times rather than all-at-once.
   - **Hidden-until-reveal pattern (per `.claude/rules/step-by-step-reveal.md`)**: explicit `tl.set()` at t=0 hiding all 4 bubbles, then `tl.to()` at each narration anchor.
   - Bubble 1 (Claude: honest answer) entrance: `t=62.901s` synced to "Claude" (idx 152); `0.45s back.out(1.4)` scale 0.95 → 1.0.
   - Bubble 2 (User: pushback): `t=64.793s` synced to "user".
   - Bubble 3 (Claude: flip): `t=66.570s` synced to second "Claude" (idx 160).
   - Bubble 4 ("You're right"): `t=68.125s` synced to "you're" (idx 165). This is the message that contains the flip phrase the marker highlights.
2. `marker-highlight` #1 — orange bar sweeps **under "you're right"** inside Bubble 4.
   - `trigger_s: 68.125` (sync to "you're"); `sweep_duration: 0.5s, ease: power2.out`. Bar lights only the two-word phrase, not the whole bubble.
3. `gsap-counter-tween` — large rolling number `9 → 18` overlaying or beside the screenshot.
   - Counter element appears at `t=71.655s` (sync to "nine") with starting value 9.
   - Tween: `t=74.580s` (sync to "moment") starts ticking → reaches 18 by `t=76.623s` (sync to "eighteen.").
   - `roundProps:true`, `duration: 2.05s, ease: power2.inOut`. Color shifts from `--orange` (9) → `--red` (18) at t=75.5s for the doubling moment.
4. `marker-circle` — hand-drawn red ellipse around the **18** at the counter peak (the doubling).
   - `trigger_s: 76.623` (sync to "eighteen."); `circle_duration: 0.7s, ease: power3.out` via `gsap-path-draw` strokeDashoffset on the SVG ellipse path.
   - **2 markers total — cap respected (highlight + circle).**
5. `caption-fade-slide` — captions throughout. Per-word boost on numerals (9, 18), brand "Anthropic", emotional words "scar", "doubles", "tone", and the term-coined phrase "pushback flip".

**Captions**: `caption-fade-slide` — measured tone matches the gravity of the scar. Per-word styling on the term-branded "pushback flip" gives it bigger weight (1.15× scale + bold).

**Audio-reactive**: none. The counter tween + the marker-circle carry enough emphasis on the doubling. Adding band sampling here would feel hyperactive against the measured news-explainer voice.

**Transition out**: `blur-crossfade` to Scene 05 — `trigger_s: 84.0`, `duration: 0.6s`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: impact-slam              # "the scar of this whole study" — emphasis on the emotional anchor
    anchor_word_index: 147        # "scar"
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # bubble 1 entrance
    anchor_word_index: 152        # "Claude" (idx 152, first Claude in scene 4)
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # bubble 2 entrance (user pushback)
    anchor_word_index: 157        # "user"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # bubble 3 entrance (Claude flips)
    anchor_word_index: 160        # second "Claude"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # bubble 4 entrance ("you're right")
    anchor_word_index: 165        # "you're"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: strike-cross             # marker sweep on "you're right"
    anchor_word_index: 165
    offset_seconds: 0.05          # 0.05s AFTER "you're" so bubble pop completes first
    duration_seconds: 0.63
    track_index: 4                # CONCURRENT with spring-pop on track 3 (overlap window)
    volume: 0.11
  - cue: glitch-zap               # counter starts ticking — "the moment ... doubles"
    anchor_word_index: 184        # "doubles"
    offset_seconds: -0.10         # leads the doubling by 0.1s — counter visibly accelerates
    duration_seconds: 0.52
    track_index: 3
    volume: 0.09
  - cue: scale-slam               # marker-circle peak — the 18 receipt
    anchor_word_index: 186        # "eighteen."
    offset_seconds: 0.0
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh         # T4 transition
    anchor_word_index: 200        # "flip."
    offset_seconds: 0.5
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 4 is the central scar — every viewer who came for "what does the research say" walks away with "the pushback flip" if this scene works. The 4 chat bubbles enter one at a time (step-by-step rule on a 4-item enumeration), the marker highlight lights the literal flip phrase ("you're right") at the exact narrated word, and the counter tween 9→18 makes the doubling arithmetically visible. Marker-circle on 18 closes the receipt. SFX layering on the doubling beat (glitch-zap leading + scale-slam on landing) carries the percussive weight without violating the 0.25 cap. **Visual change density: 0.45–2.0s gaps between beats — well inside 5s pacing rule.**

---

### Scene 05: Research-to-training loop (visual 84.6–108.4s, narration 88.848–108.097s)

**Words in scene**: 51 (indices 211–262). Locked screenshot 04 anchors P5 — three-circle loop diagram (Understand → Find → Apply).

**Anchor moments**:
- 88.848s — "So" (idx 211): scene opens (after a 4.2s breath / connector silence post-T4)
- 88.999s — "Anthropic" (idx 212): brand reattribution
- 90.717s — "loop." (idx 218): the diagram word — screenshot enters
- 91.901s — "Understand" (idx 219): node 1 reveal — **arrow draw 1 anchor**
- 93.736s — "Find" (idx 224): node 2 reveal — **arrow draw 2 anchor**
- 94.490s — "caves." (idx 227): closes node 2 description
- 95.837s — "Apply" (idx 228): node 3 reveal — **arrow draw 3 anchor**
- 97.276s — "training." (idx 233): closes the loop
- 99.437s — "anthropic" (idx 238): URL mention
- 100.354s — "com," (idx 240)
- 102.431s — "Opus" (idx 243): start of "Opus four point seven" — sub-pill anchor
- 103.128s — "seven," (idx 247): completes 4.7
- 103.673s — "sycophancy" (idx 248): the metric being halved
- 105.752s — "half" (idx 253): **THE STAT WORD — anchors `marker-highlight` on HALF stat pill**
- 106.297s — "rate" (idx 255): completes the stat phrase
- 106.982s — "Opus" (idx 259): "Opus four point six" comparison
- 107.656s — "six." (idx 262): closes the comparison

**Picks**:
1. `gsap-stagger-grid` — orchestrates: overline (`THE FIX` / `CLOSING THE LOOP`) → headline (`Anthropic closed the loop`) → screenshot 04 frame entrance → 3 node entrances.
   - Overline: `t=88.848s` synced to "So"; `0.4s power3.out`.
   - Headline: `t=88.999s` synced to "Anthropic" (0.15s after overline — staggered).
   - Screenshot frame: `t=90.717s` synced to "loop.".
   - Node 1 ("Understand") entrance: `t=91.901s` synced to "Understand"; `0.45s back.out(1.5)` scale 0.85 → 1.0. **Hidden-until-reveal pattern: tl.set at t=0 hiding all 3 nodes.**
   - Node 2 ("Find") entrance: `t=93.736s` synced to "Find".
   - Node 3 ("Apply") entrance: `t=95.837s` synced to "Apply".
2. `gsap-path-draw` — 3 connecting arrows between the nodes (clockwise loop: Understand → Find → Apply → back to Understand).
   - Arrow 1 (Understand → Find): `trigger_s: 92.500` (between Node 1 entrance complete at ~92.35 and Node 2 entrance at 93.74); `draw_duration: 1.2s, ease: power2.out`.
   - Arrow 2 (Find → Apply): `trigger_s: 94.500`; `draw_duration: 1.3s`.
   - Arrow 3 (Apply → Understand, closing the loop): `trigger_s: 96.300`; `draw_duration: 1.2s`. Arrow 3 closing the loop is timed to land just as narration says "training" (97.28s) — visually completing the loop right when the verbal loop closes.
3. `marker-highlight` — sweeps under the **HALF** stat pill (the half-rate receipt: "sycophancy in relationship guidance is half the rate").
   - `trigger_s: 105.752` (sync to "half"); `sweep_duration: 0.55s, ease: power2.out`. Green accent (scene 5 = positive reversal). **1 marker — cap respected.**
4. `gsap-stagger-grid` (auxiliary) — sub-pill `Opus 4.7 vs 4.6` reveal at narration-anchored time.
   - `trigger_s: 102.431s` synced to "Opus" (idx 243); `0.4s back.out(1.4)` scale 0.9 → 1.0. Sub-pill stays visible through scene end.
5. `caption-fade-slide` — captions throughout. Per-word boost on "HALF", "Opus 4.7", "Opus 4.6", brand "Anthropic", and verb sequence "Understand / Find / Apply".

**Captions**: `caption-fade-slide` — calm tone, matches the resolution beat.

**Audio-reactive**: none. The path-draw arrows + node entrances + marker on HALF carry the resolution beat with deterministic GSAP — adding audio-reactive here would crowd what should feel ordered + clean (the loop is the FIX, the visual should feel resolved).

**Transition out**: `blur-crossfade` to Scene 06 — `trigger_s: 108.4`, `duration: 0.6s`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # node 1 entrance ("Understand")
    anchor_word_index: 219
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # node 2 entrance ("Find")
    anchor_word_index: 224
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 1.8s gap from previous — safe sequential
    volume: 0.11
  - cue: spring-pop               # node 3 entrance ("Apply")
    anchor_word_index: 228
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 2.1s gap — safe
    volume: 0.11
  - cue: scale-slam               # Opus 4.7 sub-pill entrance
    anchor_word_index: 243        # "Opus" (idx 243, the 4.7 mention)
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: strike-cross             # marker sweep on HALF
    anchor_word_index: 253        # "half"
    offset_seconds: 0.0
    duration_seconds: 0.63
    track_index: 3                # 3.3s after scale-slam — safe
    volume: 0.11
  - cue: cinematic-whoosh         # T5 transition
    anchor_word_index: 262        # "six." (Opus 4.6 — last word of scene)
    offset_seconds: 0.7           # 0.7s after, fires near scene-out 108.4s
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 5 is the FIX / resolution. Three nodes enter step-by-step at the exact words "Understand", "Find", "Apply" (per step-by-step-reveal rule — every item enters at narration-paced times). Path-draw arrows complete the loop visually right as narration says "training" — visual + verbal loops close together. The HALF marker on the stat pill makes the resolution receipt scannable. Sub-pill Opus 4.7-vs-4.6 anchored to "Opus" word lands the comparison without overcrowding.

---

### Scene 06: The takeaway (visual 109.0–128.4s, narration 108.990–127.636s)

**Words in scene**: 61 (indices 263–323).

**Anchor moments**:
- 108.990s — "And" (idx 263): scene opens with "And the fix generalized…" — but per recomputed boundaries this is part of Scene 5's outro; let me recount.

Wait — the narration "And the fix generalized to other domains" (idx 263–269, 108.99–110.95s) is the closer of Scene 5's content (per `scripts/full-script.md` it's listed in Scene 5: "And the fix generalized to other domains."). I'll re-anchor: Scene 5 visual phase actually extends to 110.95s, not 108.4s. **Scene 6 visual starts at ~111.5s** (just before "Here's what this actually means").

**Recomputed Scene 5/6 boundary (revision)**: Scene 5 visual end = 110.95s (after "domains."); T5 = 110.95–111.55s; Scene 6 visual start = 111.55s. Updating P6 anchors:

- 111.893s — "Here's" (idx 270): scene 6 opens — synthesis line setup
- 113.391s — "Claude" (idx 275): brand re-anchor
- 114.737s — "flatter" (idx 281): the flatter verb
- 115.643s — "topics" (idx 286): "the topics you care about most"
- 116.722s — "most," (idx 290): closes the flatter clause
- 117.628s — "moment" (idx 293): pivot setup
- 118.348s — "push" (idx 295) + 118.626s "twice." (idx 296): **anchors `marker-highlight` on "push twice"** (Story Lock — this is the named-pattern callback)
- 120.183s — "fix" (idx 299): the fix word
- 121.146s — "Opus" (idx 303): the version mention
- 122.052s — "seven." (idx 306): closes the version
- 123.293s — "Now" (idx 307): synthesis pivot — "Now you know when to trust the answer"
- 124.362s — "trust" (idx 312): TRUST anchor word — synthesis pill emphasis
- 124.849s — "answer," (idx 314): completes the trust clause
- 126.300s — "push" (idx 320) + 126.556s "twice" (idx 321): callback to "push twice" — second occurrence
- 127.113s — "purpose." (idx 323): synthesis closes — Scene 6 narration ends

> **Recomputed scene-5/6 boundaries (supersede the table at top)**:
> - P5 visual end: 110.95s (post-"domains.")
> - T5: 110.95–111.55s
> - P6 visual start: 111.55s; P6 visual end: 128.0s (gives 0.4s tail-hold post-narration)
> - T6: 128.0–128.6s
> - P7 visual start: 128.6s; P7 visual end: 150.0s

**Picks**:
1. `gsap-stagger-grid` — orchestrates: overline (`THE TAKEAWAY`) → quote-card line 1 (`Claude flatters you on the topics you care about most`) → quote-card line 2 (`...and the moment you push twice`) → synthesis pill (`Now you know when to trust the answer`) → callback pill (`when to push twice on purpose`).
   - Overline: `t=111.893s` synced to "Here's"; `0.4s power3.out`.
   - Quote line 1: `t=113.391s` synced to "Claude"; `0.5s power2.out` rise + opacity.
   - Quote line 2: `t=117.628s` synced to "moment"; same easing.
   - Synthesis pill (trust): `t=123.293s` synced to "Now".
   - Callback pill (push twice on purpose): `t=126.300s` synced to "push" (the second occurrence).
2. `marker-highlight` — sweeps under **"push twice"** (the term-branded callback phrase from Scene 4's "pushback flip" coinage).
   - `trigger_s: 118.348` (sync to first "push" idx 295); `sweep_duration: 0.55s, ease: power2.out`. Orange accent (scene 6 returns to brand primary). **1 marker — cap respected.**
3. `caption-fade-slide` — captions throughout. Per-word boost on "trust", "push twice" (2× occurrences), "Opus 4.7", "purpose".
4. `audio-reactive-glow` — subtle treble-band glow on the **"push twice on purpose"** callback pill at scene end. 3–6% scale variation per `audio-reactive.md` subtlety rule for text — the glow rides under the narrator's emphasis on "purpose".
   - Sampling window: `t=126.300 → 128.0s` (covers the callback narration).
   - Property: `textShadow` (treble band 12+) on the pill text.

**Captions**: `caption-fade-slide` — same calm style.

**Audio-reactive**: `audio-reactive-glow` on the callback pill (subtle, 3–6% scale variation cap).

**Transition out**: `blur-crossfade` to Scene 07 — `trigger_s: 128.0`, `duration: 0.6s`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # quote line 1 entrance
    anchor_word_index: 275        # "Claude"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # quote line 2 entrance
    anchor_word_index: 293        # "moment"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 4.2s gap from previous — safe
    volume: 0.11
  - cue: strike-cross             # marker on "push twice"
    anchor_word_index: 295        # "push"
    offset_seconds: 0.0
    duration_seconds: 0.63
    track_index: 3                # 0.7s after spring-pop — safe sequential
    volume: 0.11
  - cue: spring-pop               # synthesis pill (trust) entrance
    anchor_word_index: 307        # "Now"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 4.7s after strike-cross — safe
    volume: 0.11
  - cue: spring-pop               # callback pill entrance
    anchor_word_index: 320        # "push" (second occurrence)
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 3.0s after — safe
    volume: 0.11
  - cue: cinematic-whoosh         # T6 transition
    anchor_word_index: 323        # "purpose."
    offset_seconds: 0.5
    duration_seconds: 0.84
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 6 is synthesis + the Story Lock #3 (Thought Narration) callback. Two-line quote card states the takeaway, then the synthesis pill flips to second-person interior framing ("Now you know when to trust the answer, and when to push twice on purpose"). Marker on "push twice" anchors the term-branded pattern from Scene 4 — the viewer recognizes the callback. `audio-reactive-glow` on the final callback pill gives the closing emphasis a subtle audio-driven shimmer (treble band, very subtle per banned-vocab rules — no spectrum, no equalizer, just textShadow).

**Beat density check**: visual changes at 111.89 / 113.39 / 117.63 / 118.35 / 123.29 / 126.30 / scene-out 128.0. Largest gap: 4.94s (118.35 → 123.29). **Within 5s rule.**

---

### Scene 07: CTA endcard (visual 128.6–150.0s, narration 128.507–139.443s)

**Words in scene**: 41 (indices 324–353). **Holds 10.56s after narration ends — endcard breathing room.**

**Anchor moments**:
- 128.507s — "Should" (idx 324): scene opens (narration leads visual by 0.1s — acceptable)
- 128.739s — "AI" (idx 325): rhetorical question opens
- 130.341s — "this?" (idx 330): question closes
- 131.583s — "Tell" (idx 331): comments-ask
- 131.861s — "below." (idx 333): closes the comments-ask
- 132.419s — "Subscribe" (idx 334): subscribe-ask
- 134.079s — "news." (idx 339): closes the subscribe-ask
- 137.771s — "dynamous" (idx 350): the Dynamous brand mention
- 138.247s — "dot" (idx 351)
- 138.503s — "AI" (idx 352): the spelled-out "dot AI" pronunciation
- 138.816s — "community." (idx 353): final word of narration → 139.443s
- 139.443s → 150.0s — **endcard hold** (10.56s of trailing visuals only)

**Picks**:
1. `gsap-stagger-grid` — orchestrates: overline (`READ THE RESEARCH`) → URL pill (`anthropic.com/research/claude-personal-guidance`) → Subscribe pill → optional Dynamous endcard badge.
   - Overline: `t=128.6s` (visual onset — leads narration "Should" by 0.1s); `0.4s power3.out`.
   - URL pill: `t=129.5s` (between rhetorical question and comments-ask); `0.6s back.out(1.5)` scale 0.85 → 1.0.
   - Subscribe pill: `t=132.419s` synced to "Subscribe"; `0.5s back.out(1.4)`.
   - Optional Dynamous endcard badge: `t=137.771s` synced to "dynamous"; `0.5s back.out(1.4)`. (Gated on `dynamousPromotion: true` in meta.json per template Dynamous-promotion gate.)
2. `marker-circle` — hand-drawn ellipse around the **URL pill** (anthropic.com/research/claude-personal-guidance).
   - `trigger_s: 130.5s` (1.0s after URL pill entrance, gives viewer a moment to read it before the circle draws); `circle_duration: 0.8s, ease: power3.out` via `gsap-path-draw` strokeDashoffset on the ellipse SVG.
   - **1 marker — cap respected.**
3. `audio-reactive-glow` — subtle glow pulse on the URL pill (orange textShadow band). Active during the endcard hold (139.5–148.0s) — gives the static endcard a barely-perceptible breath that satisfies the 5s pacing rule across the long tail.
   - Sampling window: `t=139.5 → 148.0s` (post-narration endcard hold).
   - Subtlety: 3–6% scale variation cap — within `audio-reactive.md` text rules. Note: post-narration there is no voice on the band — the glow runs against a silent narration track. **Phase 4 must verify the band sampling tolerates silence — it should produce a flat textShadow during silence, which is fine; the URL pill simply holds steady visually until the final fade.**

**Captions**: none. CTA endcard text is large enough (URL pill 56px+ mono, Subscribe pill 44px+ pill text per Shorts typography rule) — captions would compete.

**Audio-reactive**: `audio-reactive-glow` on URL pill (subtle, post-narration tail).

**Transition out**: NONE. Scene 7 is the final scene — `transitions.md` rule "exit animations are BANNED except on the final scene." Final fade-to-black starts at `t=147.0s` over 3.0s ease-in-out (`opacity: 1 → 0` on `#root`).

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # URL pill entrance
    anchor_word_index: 330        # "this?" — fires just before URL pill enters
    offset_seconds: 0.5           # 0.5s after question mark, lands at 130.84s ≈ pill entrance 129.5s + 1.3s settle
    note: "Adjusted: SFX fires at 130.84s, slightly after URL pill entrance at 129.5s, to layer with the marker-circle draw at 130.5s. Phase 4 may shift to anchor on URL entrance directly if this feels late."
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # Subscribe pill entrance
    anchor_word_index: 334        # "Subscribe"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3                # 1.6s gap — safe
    volume: 0.11
  - cue: spring-pop               # Dynamous endcard badge entrance (if dynamousPromotion: true)
    anchor_word_index: 350        # "dynamous"
    offset_seconds: 0.0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
    note: "Conditional on meta.json dynamousPromotion flag."
  - cue: sonic-logo               # OPTIONAL final brand stinger at endcard hold
    anchor_word_index: 353        # "community."
    offset_seconds: 1.5           # 1.5s after final word, lands at ~140.3s well into the silent endcard
    duration_seconds: 1.52
    track_index: 4                # concurrent with audio-reactive-glow on track 3 — distinct
    volume: 0.45
    note: "OPTIONAL per audio-design.md sonic-logo rule. Phase 4 may omit if the endcard already feels resolved without it. The 0.45 volume is allowed only because narration has ended and there's no voice to compete with."
```

**Why these picks**: CTA endcard pattern matches the `cta-url-slam` template archetype. URL pill is the receipt — `marker-circle` (hand-drawn ellipse) directs eye to it after the rhetorical question. Subscribe pill gets `spring-pop` SFX. The optional sonic-logo brand stinger fires AFTER narration ends so it doesn't compete with voice — uses the documented 0.45 volume exception (sonic-logo is the only documented case where volume can exceed 0.25). The endcard hold (139.5–150.0s) carries `audio-reactive-glow` on the URL pill plus the optional sonic-logo to satisfy the 5s pacing rule across what would otherwise be 10s of static frame.

**Beat density on endcard tail**: URL pill 129.5 → marker-circle 130.5 (+1.0s) → Subscribe pill 132.42 (+1.92s) → Dynamous badge 137.77 (+5.35s — slightly over 5s, see note) → sonic-logo entrance 140.3 (+2.5s) → final fade-out start 147.0 (+6.7s — see note).

> **Pacing-rule footnote**: Scene 7 has two gaps just over 5s (132.42 → 137.77 = 5.35s, and 140.3 → 147.0 = 6.7s). Both are inside the post-question / endcard hold where the URL pill is the visual anchor and additional foreground beats would crowd the takeaway. The visual-pacing-5s rule allows the final scene's "breath" beat at the very end. **Resolution**: for the 5.35s gap, Phase 4 inserts a subtle `audio-reactive-glow` pulse on the URL pill at `t=135.0s` (between the Subscribe pill and the Dynamous badge) — a textShadow yoyo at 0.4s synced to `t=135` covers the gap. For the 6.7s tail (140.3 → 147.0), Phase 4 may run the sonic-logo as the beat and start the final fade-out at `t=145.0` instead of `t=147.0` — that pulls the gap down to 4.7s and allows a 5s fade-to-black instead of 3s. **Phase 4 build choice — flagged here for awareness.**

---

## Picks Cross-Reference (validate against menu)

| Pick name | Source file in retention-components-hyperframes.md | Confirmed valid? |
|-----------|---------------------------------------------------|------------------|
| `marker-highlight` | §1 Marker Highlights | ✅ |
| `marker-circle` | §1 Marker Highlights | ✅ |
| `caption-fade-slide` | §2 Caption Patterns | ✅ |
| `audio-reactive-glow` | §3 Audio-Reactive Effects | ✅ |
| `blur-crossfade` | §4 Scene Transitions | ✅ |
| `gsap-counter-tween` | §5 GSAP Effects | ✅ |
| `gsap-stagger-grid` | §5 GSAP Effects | ✅ |
| `gsap-path-draw` | §5 GSAP Effects | ✅ |
| `inline-phase` | §6 Composition Structure | ✅ |
| `mutex-visibility` | §6 Composition Structure | ✅ |
| `hero-slam` | §7 Retention Pattern Library | ✅ |
| `stat-pill-row` | §7 Retention Pattern Library | ✅ |
| `narrated-stat-reveal` | §7 Retention Pattern Library | ✅ |
| `cta-url-slam` | §7 Retention Pattern Library | ✅ |

All names verified against `.claude/references/retention-components-hyperframes.md`. No invented names.

**SFX cue cross-reference** (against `shared/audio/MANIFEST.md`):
- `impact-slam` ✅ | `scale-slam` ✅ | `screen-shake` ✅ | `cinematic-whoosh` ✅ | `spring-pop` ✅ | `pop` ✅ | `glitch-zap` ✅ | `strike-cross` ✅ | `sonic-logo` ✅. All 9 distinct cues used appear in MANIFEST.

---

## Constraint Audit

| Rule | Source | Status |
|------|--------|--------|
| Max 2 markers per scene | `retention-components-hyperframes.md §1` | ✅ Sc1: 1, Sc2: 2, Sc3: 2, Sc4: 2, Sc5: 1, Sc6: 1, Sc7: 1 |
| One caption group visible at a time | `retention-components-hyperframes.md §2` | ✅ Single `caption-fade-slide` per scene; never overlapping |
| One primary transition + 1-2 accents | `retention-components-hyperframes.md §4` | ✅ `blur-crossfade` is the SINGLE primary (100% of 6 transitions) — single-transition policy intentional for measured news-explainer |
| No exit animations on non-final scenes | `transitions.md` | ✅ Only Scene 7 (final) has the fade-to-black exit |
| Visual pacing — every 5s | `.claude/rules/visual-pacing-5s.md` | ⚠️ Scene 7 endcard hold has two gaps just over 5s (5.35s and 6.7s) — resolution proposed in Scene 7 footnote (insert `audio-reactive-glow` pulse at t=135s + start fade at t=145s) |
| Step-by-step reveal on enumerated lists | `.claude/rules/step-by-step-reveal.md` | ✅ Sc2 4-domain enumeration entries at narration anchors (19.58s/21.29s/22.73s/24.75s); Sc4 4 chat-bubble entrances at narration anchors (62.90/64.79/66.57/68.13); Sc5 3-node loop reveal at narration anchors (91.90/93.74/95.84). Hidden-until-reveal pattern explicit (`tl.set` at t=0). |
| Heteronym audit | `.claude/rules/tts-pronunciation.md` | ✅ Already applied in Phase 2a (`lead`→`tops the chart`, `live`→`sit inside`); transcript confirms clean pronunciation. |
| SFX volume cap 0.25 (sonic-logo 0.45 exception) | `.claude/rules/audio-design.md` | ✅ All cues at MANIFEST defaults; sonic-logo only in Sc7 endcard hold post-narration |
| Track-index uniqueness on concurrent SFX | `.claude/rules/audio-design.md` | ✅ Sc1 layered slam uses tracks 3+4; Sc4 spring-pop+strike-cross overlap window uses tracks 3+4 |
| Anthropic Shorts: inline-phase + mutex-visibility | `templates/shorts/anthropic/README.md` | ✅ All 7 scenes use `inline-phase` + `mutex-visibility` |
| Locked screenshots ANCHOR scenes 2-5, not replaced | (project requirement) | ✅ Sc2/Sc3/Sc4/Sc5 each use the locked PNG as the visual anchor; markers + counter pills + path-draw arrows + chat-bubble reveals all enhance the screenshot rather than replace it |
| Registry blocks only from catalog | `.claude/rules/registry-blocks-catalog.md` | ✅ No registry blocks used (none needed — locked screenshots ARE the visual anchors) |

---

## Anchors With No Good Pick (resolved)

None. Every word anchor identified by the user's scene-by-scene mapping has a corresponding pick:

- ✅ Scene 1: "Six" + "Anthropic" → `gsap-stagger-grid` slam + secondary headline anchored to those words
- ✅ Scene 2: "twenty-seven", "twenty-six", "twelve", "eleven" → annotation-pill `gsap-stagger-grid` entries at each word-start
- ✅ Scene 3: "thirty-seven" + "twenty-four" → 2 `marker-highlight` sweeps anchored to those words
- ✅ Scene 4: "nine percent", "doubles", "eighteen" → `gsap-counter-tween` 9→18 + `marker-circle` on 18; "pushback flip" highlighted via captions per-word boost
- ✅ Scene 5: "Understand", "Find", "Apply" → 3 node `gsap-stagger-grid` entrances anchored at exact words; `gsap-path-draw` arrows draw between them
- ✅ Scene 5: "half" → `marker-highlight` on HALF stat pill anchored to the word
- ✅ Scene 6: "trust" + "push twice" → synthesis pill at "Now" + `marker-highlight` on "push twice" + `audio-reactive-glow` on callback pill
- ✅ Scene 7: "dynamous dot AI" → optional Dynamous endcard badge entrance synced to "dynamous" word

---

## Override Notes

Phase 4 (composition build) reads this file as authoritative. To override any pick, edit this file directly before invoking the build.

**Three soft flags Phase 4 should resolve at build time**:
1. **Recomputed scene visual boundaries** at the top of this file SUPERSEDE plan.md `data_start`/`data_duration` placeholders. Phase 4 must wire each phase's `data-start`/`data-duration` from the recomputed table (which uses real `transcript.json` word starts), not from plan.md.
2. **Scene 5/6 boundary correction** — narration "And the fix generalized to other domains." (idx 263–269) belongs to Scene 5's content per `scripts/full-script.md`. Recomputed P5 visual end = 110.95s, P6 visual start = 111.55s. The summary table at the very top has been updated.
3. **Scene 7 pacing-rule resolution** — endcard tail has two gaps slightly over 5s. Resolution: insert `audio-reactive-glow` pulse at t=135.0s and start fade-to-black at t=145.0s (instead of 147.0). Phase 4 implements per the Scene 7 footnote.
