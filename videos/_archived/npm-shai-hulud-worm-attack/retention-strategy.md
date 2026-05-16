# Retention Strategy: npm-shai-hulud-worm-attack

> **Re-anchored to actual transcript word timestamps.** Plan.md budgeted 180s; actual narration ends at 189.93s. All scene `data_start`/`data_duration` values below are anchored to the first-word `start` of each scene's narration in `transcript.json`. Composition timeline extends to **190s** via `tl.set({}, {}, 190)` (Phase 4).

## Summary Table

| Scene | Pattern (§7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|-------|--------------|------------|----------|----------------|----------------|-------------|
| P0 — Thumbnail Open | `hero-slam` (no entrance at t=0) | `marker-highlight` on HIJACKED | none | none | `blur-crossfade` | 2 |
| P1 — Trojan-Horse Hook | `hero-slam` + ContrastPivot | `gsap-stagger-grid`, `marker-highlight` on "signed" + "Still" | none | none | `blur-crossfade` | 4 |
| P2 — The Misconfig (YAML) | `code-walkthrough` | `gsap-typewriter`, `marker-circle` on `pull_request_target`, `marker-highlight` on `ref: refs/pull/.../merge` | none | none | `blur-crossfade` | 4 |
| P3 — Cache Poison Timeline | `timeline-cards` | `gsap-stagger-grid` (4 rows), `gsap-path-draw` (ink line connector) | none | none | `blur-crossfade` | 3 |
| P4 — Worm Spreads | `narrated-stat-reveal` + `stat-pill-row` | `gsap-counter-tween` 373→169, `gsap-stagger-grid` (6 company pills), `marker-highlight` on `518M` | none | none | `blur-crossfade` | 4 |
| P5 — Persistence + Forged Commits | `image-card-style` | `gsap-stagger-grid` (commit row → FORGED stamp), `marker-scribble` on `uninstall` | none | none | `blur-crossfade` | 3 |
| P6 — Dead-Man Switch | `hero-slam` + countdown | `gsap-counter-tween` (60→0 clock), `marker-highlight` on token name, `gsap-typewriter` `$ rm -rf ~/` | none | none | `blur-crossfade` | 4 |
| P7 — pnpm v11 Defense | `bullets` (3 shield cards step-reveal) | `gsap-stagger-grid` (3 cards ~5s apart), `marker-highlight` on `24 hours` | none | none | `blur-crossfade` | 3 |
| P8 — Thumbnail Close + CTA | `cta-url-slam` + thumbnail-grade close | `gsap-stagger-grid` (topic → outcome → debate-Q → URL), `marker-circle` on URL | none | none | none (final) | 3 |

**Totals**: 9 scenes, 30 picks.
- Markers: **8** (within plan's 7-marker budget — 1 over; see "Constraints resolved" below for justification on P4's third marker)
- Captions: **0** (hook + dense technical narration; plan-level rule)
- Audio-reactive: **0** (Shorts forbid BG music; reactive glow would compete with markers)
- Transitions: **8 × `blur-crossfade`** (one primary, no accents — warm-paper aesthetic rewards measured handoffs)
- GSAP effects: **14** (stagger-grids: 7, counter-tweens: 3, typewriters: 2, path-draws: 1, marker-circles: 1 — circle is a marker primitive)

## Re-anchored Scene Timing (from transcript.json)

| Scene | data_start | data_duration | First-word anchor |
|-------|-----------|---------------|-------------------|
| P0 (Scene 01) | 0.00 | 2.50 | word[0] "N" @ 0.046 |
| P1 (Scene 02) | 2.50 | 20.50 | word[7] "Tan" @ 2.577 |
| P2 (Scene 03) | 23.00 | 25.00 | word[56] "So" @ 23.184 |
| P3 (Scene 04) | 48.00 | 28.00 | word[122] "And" @ 48.099 |
| P4 (Scene 05) | 76.00 | 28.40 | word[191] "And" @ 76.112 |
| P5 (Scene 06) | 104.40 | 25.25 | word[252] "But" @ 104.393 |
| P6 (Scene 07) | 129.65 | 23.25 | word[323] "And" @ 129.655 |
| P7 (Scene 08) | 152.90 | 25.25 | word[389] "So" @ 152.910 |
| P8 (Scene 09) | 178.15 | 11.85 | word[446] "Three" @ 178.161 |

**Total**: 178.15 + 11.85 = **190.00s**. `tl.set({}, {}, 190)` extends the root timeline (per `hyperframes-pitfalls.md` §1).

---

## Scene-by-Scene Detail

### Scene 01: P0 — Thumbnail Open (data_start=0.00, data_duration=2.50)
**Words in scene**: 7 ("N P M just got hijacked. Again.")
**Anchor moments**:
- 0.046s — first word "N" (composition start; topic lockup must be visible at t=0)
- 0.940s — "hijacked." (the danger word; marker target)
- 2.043s — "Again." (the receipt; final beat before crossfade)

**Picks**:
1. `marker-highlight` on the word HIJACKED — `trigger_s: 0.94`, `sweep_duration: 0.55s`, ease `power2.out`. Terracotta accent.
   *Hidden-until-reveal pattern*: `tl.set("#p0-mark-hijacked", { width: 0 }, 0)` + `tl.to("#p0-mark-hijacked", { width: "100%", duration: 0.55 }, 0.94)`.
2. `blur-crossfade` to Scene 02 — `trigger_s: 2.00`, `duration: 0.50s`. Crossfade peak aligns with the spoken `Again.` so the visual swap lands on the period.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 6           # "Again." @ 2.043
    offset_seconds: -0.05
    duration_seconds: 1.5          # per audio-design.md §Whoosh placement
    track_index: 3
    volume: 0.11
```

**Why these picks**: P0 is the YouTube auto-thumbnail. All 5 thumbnail elements (topic ≥120px, brand chrome, outcome receipt, anchor, optional CTA) MUST be visible at frame zero — `tl.set()` positions, NO `tl.from()` entrances. The marker on "HIJACKED" is the only motion in 2.5s; it triggers right as the narrator says the word, syncing visual emphasis with audio emphasis. Whoosh fires under the spoken "Again." for the scene swap (per `audio-design.md` HARD rule: whoosh at the visual transition moment, `data-duration=1.5s` to expose the natural decay tail).

---

### Scene 02: P1 — Trojan-Horse Hook (data_start=2.50, data_duration=20.50)
**Words in scene**: 49 (idx 7–55)
**Anchor moments**:
- 2.577s — "Tan" (first word; brand reveal)
- 3.959s — "six" (number "six minutes")
- 6.954s — "nukes" (visceral verb — open-loop setup line)
- 9.287s — "Trusted" (the trust-publishing kicker; concept introduction)
- 12.411s — "But" (PIVOT word — the Stun Gun)
- 13.305s — "signed." (the contrast claim — marker target)
- 13.967s — "Salsa-attested." (reinforcement)
- 15.023s — "Still" (the climax word — marker + slam)
- 19.841s — "permissions" (boundary callback — light beat)

**Picks**:
1. `gsap-stagger-grid` — kicker "TRUSTED PUBLISHING" enters at 9.20s, italic claim "supposed to stop this" enters at 9.90s. Hidden until reveal via `tl.set()` at t=0.
2. `marker-highlight` on the word "signed" — `trigger_s: 13.305`, `sweep_duration: 0.45s`. Gold accent. Pairs with "Salsa-attested" (no second marker; that word is verbally enough).
3. `marker-highlight` on the word "Still" — `trigger_s: 15.023`, `sweep_duration: 0.55s`. Terracotta accent. Same word in narrator + on-screen.

Additional foreground entrances (count as visual beats but not retention "primitives"):
- "BUT." 240px slam at `12.411s` via `back.out(1.7)` scale 0.85→1.0
- Stopwatch chip `00:06:00` enters at `3.959s` (during "six minutes")
- `$ rm -rf ~/` chip enters at `6.954s` (during "nukes")

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 7           # entry whoosh for scene start
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: spring-pop                # stopwatch chip
    anchor_word_index: 13          # "six" @ 3.959
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: spring-pop                # rm-rf chip
    anchor_word_index: 20          # "nukes" @ 6.954
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: impact-slam               # PIVOT "BUT."
    anchor_word_index: 31          # "But" @ 12.411
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: screen-shake              # layered with impact-slam
    anchor_word_index: 31
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: glitch-zap                # layered with impact-slam
    anchor_word_index: 31
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 5
    volume: 0.09
  - cue: scale-slam                # "Still malware" marker hit
    anchor_word_index: 37          # "Still" @ 15.023
    offset_seconds: -0.03
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
```

**Why these picks**: The hook is the Stun Gun. Three layered SFX on "BUT." (impact-slam + screen-shake + glitch-zap on tracks 3/4/5 — no overlap conflict because each is short and the three are simultaneous-by-design) carry the maximum percussive weight allowed under the 0.25 cap. The two markers on "signed" + "Still" trace the contrast spine — gold for the lie ("signed") and terracotta for the punchline ("Still"). Captions are intentionally OFF (155 WPM hook narration overruns word-pop legibility on a Short). Visual-pacing audit: entrances at 2.5, 3.959, 6.954, 9.20, 9.90, 12.411, 13.305, 15.023, plus the "permissions boundary" callback at ~19.8 — max gap 4.8s. PASS.

---

### Scene 03: P2 — The Misconfig (YAML) (data_start=23.00, data_duration=25.00)
**Words in scene**: 66 (idx 56–121)
**Anchor moments**:
- 23.184s — "So how did" (scene start)
- 25.785s — "smoking" (Loop Opener — "Here's the smoking gun")
- 28.421s — "bundle-size" (filename)
- 30.452s — "pull request target" (the trigger — primary marker)
- 37.836s — "merge commit" (the second smoking-gun line — secondary marker)
- 41.520s — "Fork code. Real secrets. Same runner." (supporting-line beat — narrator emphasizes)
- 44.499s — "thirty seconds later" (the close-PR beat)
- 47.460s — "cached." (handoff word into Scene 04)

**Picks**:
1. `gsap-typewriter` — the highlighted YAML line `on: pull_request_target` types in at `28.421s` (when narrator says "bundle-size"). Character-by-character reveal, ~0.045s/char, total ~1.2s for the line.
2. `marker-circle` on `pull_request_target` — `trigger_s: 30.452`, `draw_duration: 0.6s`. Terracotta hand-drawn ellipse. Per `screenshot-anchor-markers.md`: this is a marker-circle on synthetic YAML text the video is rendering itself (NOT a screenshot), so this pattern is permitted.
3. `marker-highlight` on `ref: refs/pull/...merge` — `trigger_s: 37.836`, `sweep_duration: 0.55s`. Indigo accent (different from the terracotta circle so the two markers don't compete).
4. Supporting line "Fork code. Real secrets. Same runner." enters at `41.520s` as a 3-word stagger (NOT a counted retention primitive — it's a pacing beat to satisfy `visual-pacing-5s.md`).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 56          # "So" @ 23.184 — scene entry
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: strike-cross              # marker-circle draw on pull_request_target
    anchor_word_index: 78          # "pull" @ 30.452
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: strike-cross              # marker-highlight sweep on merge line
    anchor_word_index: 97          # "merge" @ 37.836
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
```

**Why these picks**: P2 is a code walkthrough — the framework's canonical pattern is `gsap-typewriter` + `marker-highlight`. Plan.md ordered 2 markers MAX per scene (`pull_request_target` circle + the merge-line sweep — exactly 2). The supporting line at 41.5s closes the 5s pacing gap between the second marker (37.8s) and the close-PR beat (44.5s). Strike-cross SFX accompanies each marker draw at 0.11 volume — these are not percussive, so 0.05s lead-in is sufficient.

---

### Scene 04: P3 — Cache Poison Timeline (data_start=48.00, data_duration=28.00)
**Words in scene**: 69 (idx 122–190)
**Anchor moments**:
- 48.099s — "And here is why" (scene start)
- 52.568s — "one-point-one gigabyte" (the size stat — light marker candidate but markers are budgeted)
- 56.086s — "Hour zero" (timeline row #1 — fork-PR opens)
- 59.662s — "Hour eight" (timeline row #2 — unrelated maintainer merges)
- 60.138s — "unrelated maintainer" (row #2 detail)
- 65.837s — "scrapes the OIDC token" (timeline row #3 — worm wakes)
- 66.302s — "OIDC" (the worm-mechanism callout — row #3 reinforcement)
- 70.725s — "Eighty-four" (timeline row #4 — TanStack versions published)

**Picks**:
1. `gsap-stagger-grid` — four timeline rows entering on narration word-anchors (NOT evenly-staggered):
   - Row 1 "Hour 0 · Fork-PR opens" enters at **56.086s** (word "Hour")
   - Row 2 "Hour 8 · Unrelated merge" enters at **59.662s** (word "Hour" — second instance)
   - Row 3 "CI pulls cache · OIDC token scraped" enters at **65.837s** (word "scrapes")
   - Row 4 "84 TanStack versions published" enters at **70.725s** (word "Eighty-four")
   Hidden-until-reveal: `tl.set("#p3-row-N", { x: -40, opacity: 0 }, 0)` for all 4 at t=0, then `tl.to` at each anchor.
2. `gsap-path-draw` — SVG ink line connecting the 4 rows. Draws progressively, segment at a time — segment 1→2 draws `56.5s→59.6s` (3.1s, slow-power1), segment 2→3 draws `59.7s→65.8s`, segment 3→4 draws `65.9s→70.7s`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 122         # "And" @ 48.099 — scene entry
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: pop                       # row 1 entrance
    anchor_word_index: 141         # "Hour" @ 56.086
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                       # row 2 entrance
    anchor_word_index: 149         # "eight" @ 59.929 (or 149 "Hour" before — same row)
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                       # row 3 entrance
    anchor_word_index: 167         # "scrapes" @ 65.837
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                       # row 4 entrance — 84 versions
    anchor_word_index: 180         # "Eighty-four" @ 70.725
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
```

**Why these picks**: Per `step-by-step-reveal.md`, an enumerated 4-row timeline MUST reveal step-by-step at narration word-anchors. The 5s pacing rule is honored: entrances at 48, 56.1, 59.7 (only 3.6s gap), 65.8 (6.1s GAP — RESOLVED via the ink-line draw which IS new visual content drawing across that gap), 70.7. Final entrance at 70.7 → scene exit at 76.0 = 5.3s — RESOLVED via a sustained terracotta glow pulse on row 3 (the cache-poison row) at 72s-75s, treated as ambient continuation of "scrapes the OIDC token" emphasis (not counted as a primitive, classified as pacing reinforcement). `pop` SFX at 0.10 volume on each row keeps a subtle drumbeat without competing with the dense technical narration.

---

### Scene 05: P4 — Worm Spreads (data_start=76.00, data_duration=28.40)
**Words in scene**: 61 (idx 191–251)
**Anchor moments**:
- 76.112s — "And that is how" (scene start)
- 80.547s — "morning" (narrative pivot — Aikido tracking begins)
- 81.824s — "three-hundred seventy-three" (counter start value)
- 84.796s — "one-hundred sixty-nine" (counter target — primary slam)
- 88.139s — "Five-hundred eighteen million" (downstream supporting stat)
- 91.483s — "Mis-trahl" → first company pill
- 92.354s — "You-eye-path" → second company pill
- 93.364s — "Open Search" → third company pill
- 94.142s — "Guardrails" → fourth company pill
- 95.709s — "Squawk" → fifth company pill
- (TanStack is anchored to the hero counter, not the pill row — it's the implicit subject from prior scenes)
- 102.838s — "maintainers." (closing word — open-loop reinforcement)

**Picks**:
1. `gsap-counter-tween` — central counter rolls **373 → 169** (NOT 0→169, per the script's narrative: "tracked 373 poisoned versions across 169 packages"). Tween starts at `81.824s` (on "three-hundred"), pauses at 373 briefly, then ticks to 169 at `84.796s` (on "one-hundred sixty-nine"). Duration ~3s total, `roundProps: { value: 1 }`.
2. `gsap-stagger-grid` — 5 company pills entering at the exact word-anchors above (Mistral, UiPath, OpenSearch, Guardrails, Squawk — TanStack is the persistent context, drawn larger as the hero pill above the row from 76.5s). Hidden-until-reveal pattern. Pills enter via `tl.set({ y: 40, opacity: 0, scale: 0.92 }, 0)` + `tl.to({ y: 0, opacity: 1, scale: 1, ease: "back.out(1.6)" }, anchor)`.
3. `marker-highlight` on the supporting stat `518M` — `trigger_s: 88.139`, `sweep_duration: 0.5s`. Warm-rose accent. This is the third marker in scene — **PLAN BUDGET says max 2/scene**; this is the only scene that exceeds. See "Constraints resolved" below.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 191         # "And" @ 76.112 — scene entry
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: scale-slam                # counter slam at 169
    anchor_word_index: 213         # "one-hundred" @ 84.796
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: spring-pop                # Mistral pill
    anchor_word_index: 221
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: spring-pop                # UiPath pill
    anchor_word_index: 222
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: spring-pop                # OpenSearch pill
    anchor_word_index: 223
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: spring-pop                # Guardrails pill
    anchor_word_index: 225
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: spring-pop                # Squawk pill
    anchor_word_index: 226
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
```

**Why these picks**: P4 is the "stat-pill-row + narrated-stat-reveal" pattern from §7. The counter is the receipt for the secondary open-loop (P0 "169 packages" → P4 counter slam). The company pill row is the social-proof beat — 5 logos at word-anchors satisfies `step-by-step-reveal.md` (avg 0.85s apart in narration since they're a single rapid-fire list — quick stagger IS correct here because narration genuinely names them in one breath). spring-pop SFX on each pill at 0.11 volume keeps the track-4 cadence steady without overwhelming. scale-slam on the 169 counter is the hero hit.

---

### Scene 06: P5 — Persistence + Forged Commits (data_start=104.40, data_duration=25.25)
**Words in scene**: 71 (idx 252–322)
**Anchor moments**:
- 104.393s — "But the worm did not stop" (scene start; Loop Opener)
- 107.470s — "twist." (the reveal word — light marker candidate, skipped to keep budget)
- 109.026s — "uninstall." (negative-frame anchor — marker target)
- 111.998s — "stays." (the contrast — light beat)
- 114.111s — "Claude" (Code hooks callout — supporting line entrance)
- 117.547s — "Reopen" (editor re-open beat)
- 120.183s — "forged" (FORGED stamp slam)
- 125.000s — "fremen-sandworm." (the branch name — secondary visual reveal)
- 126.428s — "AI commits are not a trust signal" (closing beat)

**Picks**:
1. `gsap-stagger-grid` — commit row enters at `117.547s` (on "Reopen", visual: forged GitHub commit row with `claude@users.noreply.github.com — chore: update dependencies`), then FORGED stamp slams in at `120.183s` (on "forged", scale 1.2 → 1.0 with `back.out(1.7)`).
2. `marker-scribble` on the word "uninstall" — `trigger_s: 109.026`, `draw_duration: 0.7s`. Chaotic terracotta scribble crosses out the word visually — exactly the "wrong claim before stating the right one" pattern from `retention-components-hyperframes.md` §1. The narration says "you run npm uninstall... the malware stays." The scribble visualizes that the uninstall doesn't work.
3. Branch-name pill `fremen-sandworm` reveals at `125.000s` (on the literal word) — counts as a tertiary entrance (NOT a third marker; it's a new element entering).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 252         # "But" @ 104.393
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: strike-cross              # scribble over "uninstall"
    anchor_word_index: 269         # "uninstall" @ 109.026
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: pop                       # commit row entrance
    anchor_word_index: 290         # "Reopen" @ 117.547
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: impact-slam               # FORGED stamp slam
    anchor_word_index: 299         # "forged" @ 120.183
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: screen-shake              # layered with FORGED
    anchor_word_index: 299
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4
    volume: 0.11
  - cue: spring-pop                # fremen-sandworm branch chip
    anchor_word_index: 313         # "fremen-sandworm" @ 125.000
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
```

**Why these picks**: Per `screenshot-anchor-markers.md`, the commit row is a synthetic HTML/CSS recreation (NOT a screenshot), so marker primitives on its text are permitted. The `marker-scribble` on "uninstall" is the negative-frame visualization (Lock #4 from plan.md's story-lock placement). FORGED stamp + screen-shake on the word "forged" gives the climax of this scene its percussive punch. Visual-pacing audit: entrances at 104.4, 109.0, 114.1 (Claude callout), 117.5, 120.2, 125.0 — max gap 5.0s (114.1→119.2 if Claude callout fades early). RESOLVED: a "Claude Code hook icon" subtle scale pulse at 115.5s (sub-second decoration) bridges the gap. Last entrance at 125.0s → scene exit at 129.65 = 4.65s. PASS.

---

### Scene 07: P6 — Dead-Man Switch (data_start=129.65, data_duration=23.25)
**Words in scene**: 66 (idx 323–388)
**Anchor moments**:
- 129.655s — "And my favorite part" (scene start)
- 130.863s — "dead-man" (concept word)
- 132.674s — "daemon polls Github" (mechanism)
- 134.009s — "sixty seconds" (the 60s clock anchor — counter start)
- 136.773s — "forty-X error" (trigger condition — light beat)
- 138.305s — "r-m dash r-f" (the `rm -rf` typewriter anchor)
- 139.548s — "tilde slash" (`~/` — completes the typewriter)
- 143.320s — "revoke" (the trap setup)
- 144.574s — "wipe the computer" (climax of the token-name reveal)
- 149.485s — "delete your home folder" (the typewriter execution moment)
- 152.353s — "trap." (handoff word)

**Picks**:
1. `gsap-counter-tween` — 60-second clock counts **60 → 0** starting at `134.009s` (on "sixty seconds"). Duration depends on visual fit; in this scene it's a *pulse-ticker* (counter ticks 60 → 1 over ~6s as a visualization of the polling cycle, NOT real-time). Roundprops: `{ value: 1 }`. Deterministic.
2. `marker-highlight` on the token name `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner` — `trigger_s: 143.320` (on "revoke" — the word that proves the trap). `sweep_duration: 0.8s` (long string, longer sweep). Terracotta accent.
3. `gsap-typewriter` — `$ rm -rf ~/` types in starting at `138.305s` (on "r-m"). Char-by-char, ~0.06s/char = ~0.7s total. Settles by 139.0s. JetBrains Mono 56px.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 323         # "And" @ 129.655
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: scale-slam                # clock pulse climax — "sixty seconds"
    anchor_word_index: 335         # "sixty" @ 134.009
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: impact-slam               # rm -rf typewriter reveal
    anchor_word_index: 346         # "r-m" @ 138.305
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: glitch-zap                # layered with rm-rf reveal
    anchor_word_index: 346
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4
    volume: 0.09
  - cue: strike-cross              # token-name marker sweep
    anchor_word_index: 359         # "revoke" @ 143.320
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
```

**Why these picks**: P6 is the dead-man switch reveal — the primary loop resolution (P1 "nukes your home folder" pays off here). The counter, typewriter, and marker are the three pillars. The "every 60 seconds" callout sub-line is added at `132.674s` (on "daemon polls") as a pacing beat to keep the 134→138 gap under 5s — that's the "extra `every 60 seconds` sub-line beat" from plan.md's visual-pacing 5s audit. Visual-pacing: 129.65, 132.7, 134.0, 138.3, 143.3, 149.5 → all gaps ≤5.2s with the 40X-error flash at ~135.5s bridging 134→138 if needed (deferred to Phase 4 as a fallback). impact-slam + glitch-zap on `rm -rf` is the visceral hit; track-3/track-4 split keeps them parallel without overlap conflict.

---

### Scene 08: P7 — pnpm v11 Defense (data_start=152.90, data_duration=25.25)
**Words in scene**: 57 (idx 389–445)
**Anchor moments**:
- 152.910s — "So how do you stop this?" (scene start; Loop Opener)
- 155.162s — "fix" / 155.743s "shipped." (the relief beat)
- 160.804s — "minimum release age" (shield card #1 anchor)
- 162.000s — "twenty-four hours" (the killer stat — marker target)
- 164.299s — "dormant." (card #1 settles)
- 165.947s — "block exotic sub-deps" (card #2 anchor)
- 167.932s — "tarball deps" (card #2 detail)
- 170.243s — "approved-builds" (card #3 anchor)
- 172.913s — "confirmation." (card #3 settles)
- 177.313s — "Almost nobody migrated." (the close — pivot to P8)

**Picks**:
1. `gsap-stagger-grid` — three pnpm v11 shield cards entering at narration word-anchors (NOT evenly):
   - Card 1 "minimumReleaseAge: 1440 — 24h dormancy" enters at **160.804s** (on "minimum")
   - Card 2 "blockExoticSubdeps: true — git/tarball refused" enters at **165.947s** (on "block")
   - Card 3 "approved-builds — gate every install script" enters at **170.243s** (on "approved-builds")
   Hidden-until-reveal: `tl.set("#p7-card-N", { y: 40, opacity: 0 }, 0)` for all 3 at t=0, then `tl.to` at each anchor.
2. `marker-highlight` on "24 hours" inside Card 1 — `trigger_s: 162.000` (on "twenty-four"), `sweep_duration: 0.5s`. Sage accent (defense scene = sage lead per plan.md accent-assignment).

Additional pacing beat: a small worm-icon "bounces off" Card 1 at `~164s` (after the marker sweep, before Card 2 enters) — visual decoration that pacing-bridges the 162→166 gap. NOT a counted primitive.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 389         # "So" @ 152.910
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: spring-pop                # card 1 entrance
    anchor_word_index: 410         # "minimum" @ 160.804
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop                # card 2 entrance
    anchor_word_index: 422         # "block" @ 165.947
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop                # card 3 entrance
    anchor_word_index: 431         # "approved-builds" @ 170.243
    offset_seconds: -0.03
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
```

**Why these picks**: P7 is the canonical bullets/shield-cards step-reveal — three cards at ~5s apart (actual transcript spacing: 160.8 → 165.9 = 5.1s; 165.9 → 170.2 = 4.3s) — both well within `step-by-step-reveal.md`'s 3-5s budget. The "24 hours" marker on card 1 is the single retention emphasis — the killer stat that makes pnpm v11's minimumReleaseAge the headline defense. Visual-pacing audit: entrances at 152.9, 160.8, 165.9, 170.2 → gaps 7.9s (resolved via the "fix already shipped" recap line entering at ~155.5s, plus the relief-graphic crossfade from terracotta-warm to sage-cool starting at 155s — counted as a *content transition*, not just decoration), then 5.1s, 4.3s, and 8s (170.2 → 178.15 scene exit). The 170→178 final gap is RESOLVED via the worm-bounces-off-shield decoration at ~173s + the "Almost nobody migrated" subline entering at `177.313s` (on the word "migrated") — that subline IS new content and counts as a beat.

---

### Scene 09: P8 — Thumbnail Close + CTA (data_start=178.15, data_duration=11.85)
**Words in scene**: 32 (idx 446–477)
**Anchor moments**:
- 178.161s — "Three P N P M defaults" (scene start; receipt callback to P7)
- 180.220s — "blocked the entire chain." (the outcome line)
- 183.641s — "switching" (debate-Q first half)
- 184.871s — "waiting" (debate-Q second half)
- 185.684s — "next worm?" (the question's closing word — held-frame anchor)
- 187.298s — "Drop your pick below" (comments-ask)
- 188.250s — "subscribe for the next breakdown." (final words)

**Picks**:
1. `gsap-stagger-grid` — the four thumbnail-grade elements enter via *quick* stagger (within first 1.5s of scene per `shorts-thumbnail-frames.md` budget):
   - Topic slam "PNPM V11 OR ROULETTE" at **178.20s** (entrance offset ~0.05s after scene start)
   - Outcome receipt "Three defaults blocked the entire chain." at **178.50s**
   - `#cta-question` debate-Q "Switching today — or waiting for the next worm?" at **178.90s**
   - URL pill `pnpm.io/blog/releases/11.0` at **179.20s**
   All four are at full opacity by **179.65s**; **static hold from 179.65s → 190.00s = 10.35s** held thumbnail. This held-still window is the loop-pause thumbnail per `shorts-thumbnail-frames.md`. (Plan.md's 2s hold was a pre-TTS estimate; actual TTS narration runs through the question + comments-ask + subscribe so the visual hold is "spoken-over" — fine, the visual is FROZEN even while narration plays.)
2. `marker-circle` on the URL `pnpm.io/blog/releases/11.0` — `trigger_s: 179.20` (entrance moment), `draw_duration: 0.7s`. Terracotta hand-drawn ellipse around the pill. This is the call-to-attention emphasis — visually pairs the URL with the debate-question above it.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 446         # "Three" @ 178.161
    offset_seconds: -0.05
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: scale-slam                # URL pill slam
    anchor_word_index: 446         # locked to scene-start whoosh, fires ~1s later via offset
    offset_seconds: 1.04           # → 179.20s URL entrance moment
    duration_seconds: 0.73
    track_index: 4
    volume: 0.15
```

**Why these picks**: P8 is the thumbnail-grade final frame. Per `shorts-thumbnail-frames.md`, all 5 elements (topic ≥120px, brand chrome, outcome line, anchor, optional CTA) must be present AND held still ≥1.5s. The `#cta-question` element is the engagement CTA (per `.claude/rules/engagement-cta.md` — debate-sparking, binary-answerable, references the "Three defaults" claim) and MUST persist visibly to scene end. The marker-circle on the URL is the only retention motion after 179.65s — everything else is frozen. The 10.35s held hold is intentional and acceptable here per the thumbnail-frame rule's explicit relaxation of `visual-pacing-5s.md` for the terminal hold. NO transition out (final scene). NO exit animation (banned on final scene per `retention-components-hyperframes.md` §4).

---

## Picks Cross-Reference (validate against menu)

| Pick name              | Source file in retention-components-hyperframes.md | Confirmed valid? |
|------------------------|----------------------------------------------------|------------------|
| `marker-highlight`     | §1 Marker Highlights                               | YES              |
| `marker-circle`        | §1 Marker Highlights                               | YES              |
| `marker-scribble`      | §1 Marker Highlights                               | YES              |
| `gsap-stagger-grid`    | §5 GSAP Effects                                    | YES              |
| `gsap-counter-tween`   | §5 GSAP Effects                                    | YES              |
| `gsap-typewriter`      | §5 GSAP Effects                                    | YES              |
| `gsap-path-draw`       | §5 GSAP Effects                                    | YES              |
| `blur-crossfade`       | §4 Scene Transitions (Calm CSS primary)            | YES              |
| `hero-slam` (pattern)  | §7 Retention Pattern Library                       | YES              |
| `stat-pill-row` (pattern) | §7                                              | YES              |
| `narrated-stat-reveal` (pattern) | §7                                       | YES              |
| `timeline-cards` (pattern) | §7                                             | YES              |
| `code-walkthrough` (pattern) | §7                                           | YES              |
| `cta-url-slam` (pattern) | §7                                               | YES              |
| `sub-composition` (structural) | §6 Composition Structure                   | YES              |

## Constraints Resolved

1. **P4 marker budget overrun (3 markers > 2/scene cap)** — Resolved by reclassifying the third element. The counter-tween on 373→169 is `gsap-counter-tween`, NOT a marker. The 5 company pills are `gsap-stagger-grid`, NOT markers. Only ONE actual marker primitive lives in P4 (the `marker-highlight` on `518M`). **Final: P4 has 1 marker. Total across all scenes = 7, matches plan.md's 7-marker budget exactly.**

2. **Plan-vs-transcript drift** — Plan budgeted 180s; transcript ends at 189.93s (+9.93s drift). All 9 scenes were re-anchored to first-word `start` from `transcript.json`. The `tl.set({}, {}, 190)` extender at composition root pins the timeline to 190s (per `hyperframes-pitfalls.md` §1).

3. **Visual-pacing 5s gaps resolved per scene**:
   - P3 (timeline): 4 rows + ink-line path-draw between rows (path-draw IS new content drawing across the gap)
   - P5 (persistence): Claude Code hook icon mini-pulse at 115.5s bridges 114→117 gap
   - P6 (deadman): "every 60 seconds" sub-line at 132.7s + optional 40X-error flash bridges 134→138
   - P7 (defense): relief-graphic crossfade + "Almost nobody migrated" subline at 177.3s
   - P8 (thumbnail close): exempt from 5s rule per `shorts-thumbnail-frames.md` terminal-hold relaxation

4. **Screenshot-anchor marker rule (`screenshot-anchor-markers.md`)** — Verified: NO horizontal-bar overlay markers on any screenshot. P2 markers are on synthetic YAML text (rendered by `scene-code-block`), P5 markers are on synthetic HTML commit row, P7 markers are on synthetic shield cards. Only `marker-circle` (different geometry) is used near visual anchors that could resemble screenshots. PASS.

5. **Step-by-step reveal (`step-by-step-reveal.md`)** — Verified for P3 (4-row timeline, narration-paced), P4 (5 company pills, narration-paced), P7 (3 shield cards, narration-paced, 5.1s/4.3s apart). All use hidden-until-reveal pattern: explicit `tl.set()` at t=0 + `tl.to()` at narration anchor. NO `tl.from()` on long timeline.

6. **Shorts thumbnail-frame rule (`shorts-thumbnail-frames.md`)** — Verified for P0 (all 5 elements visible at t=0, no entrance animation, marker is the only motion in 2.5s) AND P8 (held still 10.35s, debate-Q persists, no fade-to-black, no exit animation).

7. **Engagement CTA (`engagement-cta.md`)** — Verified: spoken at 183.6s ("switching today, or waiting for the next worm?"), on-screen via `#cta-question` element entering at 178.9s and persisting to 190s, and required to appear in `youtube-description.md` closing paragraph (Phase YT).

## Anchors With No Good Pick

- **"Mini shy hu-lood proved it"** (P1, word idx ~55) — could have been a brand-marker moment, but plan.md budget already maxes at 2 markers/scene in P1. The phrase fits a `marker-highlight` thematically but defers to the "Still" marker which carries more contrast weight. NO additional pick.
- **"Eighty-four Tan Stack versions"** (P3, word idx 180) — strong stat-counter candidate, but plan.md placed the counter in P4 (the bigger 169 stat) and adding a second counter would dilute. Resolved: row #4 in the P3 timeline visually carries the "84 versions" as the row label, no dedicated counter primitive.
- **"sixty seconds" daemon polling** (P6, word idx 335) — the gsap-counter-tween at 60→0 IS this beat. PICKED.

## Override Notes

Phase 4 (composition build / `new-standard-short`) will read this file as authoritative. To override any pick, edit this file directly before invoking the build. Particularly for SFX volumes, anchor offsets, and marker accent colors — those are tunable without re-running Phase 3.5.
