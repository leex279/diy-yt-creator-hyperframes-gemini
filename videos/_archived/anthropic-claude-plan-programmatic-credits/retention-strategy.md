# Retention Strategy: anthropic-claude-plan-programmatic-credits

> **Source of truth for retiming**: `videos/anthropic-claude-plan-programmatic-credits/transcript.json` (569 words, narration spans t=0.058 → t=212.515).
> **Composition build action required**: Insert a **2.5s silent pad at the head of `audio/narration.wav`** before composition build. The pad preserves the thumbnail-grade opening per `.claude/rules/shorts-thumbnail-frames.md`. After padding, every transcript word's effective composition time = `word.start + 2.5`. All times below are **composition times** (transcript word time + 2.5s).
> **Total composition duration**: **216.5s** = 2.5s silent open + 212.5s narration (last word "news." ends comp-t 215.015s) + 1.485s terminal thumbnail hold (rounded to clean 216.5s `#root data-duration`).
> **CRITICAL**: Plan.md was sized for 180s narration. Actual narration is 212.69s (32.7s longer). Every scene below retimed to actual word anchors.

---

## Summary Table

| Scene | Pattern | data_start | data_duration | Primitives | Captions | Audio-Reactive | Transition Out | Picks |
|-------|---------|-----------|---------------|------------|----------|----------------|----------------|-------|
| 01 silent-open | thumbnail-grade-open (beat 1a) | 0.0 | 2.5 | static-lockup t=0 | none | none | opacity-fade @ 2.4s (into beat 1b) | 1 |
| 02 four-surfaces | hero-slam → 4-chip step-by-step | 2.5 | 18.4 | gsap-stagger-grid (4 chips) + marker-highlight ("quiet shift") | none | none | blur-crossfade @ 20.5s + cinematic-whoosh @ 20.1s | 3 |
| 03 the-shift | stat-pill-row (Conductor/OpenClaw) | 20.9 | 34.5 | gsap-stagger-grid (2 cards) + marker-highlight ("draw from your credit") + scale-pulse ("same well") | none | none | blur-crossfade @ 55.0s + cinematic-whoosh @ 54.6s | 3 |
| 04 who-gets-it | 4-pill column step-by-step | 55.4 | 20.0 | gsap-stagger-grid (4 pills) + scale-pulse (Enterprise) | none | none | blur-crossfade @ 75.0s + cinematic-whoosh @ 74.6s | 2 |
| 05 timeline | timeline-cards + macOS-notification | 75.4 | 24.1 | gsap-stagger-grid (3 cards) + gsap-path-draw + macOS-notification + marker-highlight ("trigger") | none | none | blur-crossfade @ 99.1s + cinematic-whoosh @ 98.7s | 4 |
| 06 bonus-stack | stat-pill-row + chip-row + counter | 99.5 | 33.0 | gsap-counter-tween (0→50) + gsap-stagger-grid (4 chips) + marker-highlight ("through July 13") + scale-pulse ("the bigger one") | none | none | blur-crossfade @ 132.1s + cinematic-whoosh @ 131.7s | 4 |
| 07 reactions-montage | x-post block × 5 cycling | 132.5 | 41.1 | x-post block × 5 (sentiment bucket label chip swap) + scale-pulse on each card's quote-peak word | none | none | blur-crossfade @ 173.2s + cinematic-whoosh @ 172.8s | 2 |
| 08 big-question | split-headline + URL pill | 173.6 | 32.4 | gsap-fromto (split halves) + marker-highlight (URL pill) + scale-pulse (URL pill mid) | none | none | blur-crossfade @ 205.6s + cinematic-whoosh @ 205.2s | 3 |
| 09 thumbnail-close | thumbnail-grade-close (5-element) | 206.0 | 10.5 | static held-frame after 0.5s entrance burst (≥1.5s terminal hold) | none | none | none (final phase) | 1 |
| **TOTAL** |  |  | **216.5** |  |  |  |  | **23** |

**Inventory checks**:
- Markers: **5 total** (one per scene where the narration has a sweep-worthy phrase). Cap is 2 per scene — well under.
- Transitions: **7 blur-crossfades** + 7 `cinematic-whoosh` SFX, all at `sceneT - 0.4`. ONE primary transition style — passes the "60-70% same transition" gate.
- Captions: 0 (dense Short, no caption track).
- Audio-reactive: 0 (no BG music — Anthropic Short rule).
- Registry blocks invoked (need `hyperframes add` in Phase 4): `macOS-notification` (Scene 5), `x-post` (Scene 7).

---

## Scene-by-Scene Detail

### Scene 01: silent-open (data_start=0.0s, data_duration=2.5s)

**Narration**: none (silent thumbnail open).
**Words in scene**: 0 (audio pad fills this window).
**Visual content**: Topic lockup at full opacity from frame zero — Anthropic logo + topic slam "CLAUDE PLANS GET PROGRAMMATIC CREDITS" (160px, "CREDITS" in orange) + receipt "JUNE 15 · 4 SURFACES · PRO / MAX / TEAM / ENTERPRISE" (44px mono) + Anthropic top banner. No entrance tween — elements at final transform from t=0.

**Anchor moments**:
- t=0.0s — composition opens with topic lockup at full opacity (no fade-in)
- t=2.4s — opacity fade begins (0.1s ramp to 0)
- t=2.5s — handoff to Scene 02 (beat 1b hero pivot)

**Picks**:
1. `static-lockup` (template beat-1a, no GSAP tween).
2. `opacity-fade` exit at 2.4s (0.1s duration → fully transparent by 2.5s).

**SFX cues**: none. Sonic-logo deliberately omitted — first frame is meant to read as a still thumbnail and the audio pad is pure silence for thumbnail-grade compliance.

**Thumbnail-grade audit** (per `.claude/rules/shorts-thumbnail-frames.md`):
1. Topic statement: "CLAUDE PLANS GET PROGRAMMATIC CREDITS" (160px) ✓
2. Visual anchor: Anthropic logo (~100px height) ✓
3. Brand chrome: Anthropic top banner (persists from template) ✓
4. Outcome receipt: "JUNE 15 · 4 SURFACES · PRO / MAX / TEAM / ENTERPRISE" (44px) ✓
5. CTA pill (subordinate): N/A at t=0 — topic carries scroll-stop ✓
**Verdict**: PASS. YouTube auto-thumbnail picks this frame.

**Shape-backdrop reposition**: N/A (first phase — backdrop initialized in plan position).

**Visual-pacing-5s audit**: 2.5s window — single static frame, explicitly relaxed per `shorts-thumbnail-frames.md` (opening hold ≤ 2.5s exception).

**Why these picks**: First frame is the thumbnail. No entrance, no motion — just the topic lockup at full opacity so the moment YouTube samples t=0 for auto-thumbnail it gets a thumbnail-grade composite. Audio is silent because the narration starts immediately in the transcript ("Four" at t=0.058) — we pad the WAV with 2.5s of leading silence so the visual hold doesn't fight the spoken pivot.

---

### Scene 02: four-surfaces (data_start=2.5s, data_duration=18.4s)

**Narration window**: composition t=2.558 → t=20.471 (transcript word[0] "Four" → word[27] "K." closing "the same SDK").
**Words in scene**: 28 (transcript words 0-27).
**Spoken at start**: "Four surfaces. One credit. One quiet shift." (the variant-C triple-stat hook).

**Word-anchor table** (transcript_t → composition_t = transcript_t + 2.5):

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| "Four" (hero slam) | 0 | 0.058 | **2.558** | Hero slam "Four surfaces." reveals — already on screen from beat 1a fade-out at 2.5 |
| "surfaces." | 1 | 0.279 | 2.779 | Hero word fully readable |
| "One credit." | 2-3 | 0.848-1.393 | 3.348-3.893 | Caption pill "1 monthly credit · 1 quiet shift" fades in beneath hero (mono 32px) |
| "quiet" | 5 | 1.649 | **4.149** | Marker-highlight sweep starts under "quiet shift" in caption pill |
| "shift." | 6 | 1.916 | 4.416 | Marker sweep completes (0.5s duration: 4.149-4.649) |
| "Starting June 15," | 7-9 | 3.169-4.376 | 5.669-6.876 | Headline transitions to "Starting June 15..." overline below hero |
| "monthly credit" | 16-18 | 7.418-8.173 | 9.918-10.673 | Surface chip row enters — chip 1 pre-revealed at "Agent" word |
| "The Agent S D K." | 22-26 | 10.41-11.58 | **12.91-14.08** | Chip 1: "Claude Agent SDK" reveals at t=12.91 (anchored to "Agent") |
| "The claude dash p command." | 27-32 | 11.73-12.96 | **14.23-15.46** | Chip 2: "claude -p" reveals at t=14.23 (anchored to "claude") |
| "Claude Code GitHub Actions." | 33-36 | 13.89-15.39 | **16.39-17.89** | Chip 3: "Claude Code GitHub Actions" reveals at t=16.39 (anchored to "Claude") |
| "And third-party apps built on the same SDK." | 37-46 | 15.54-17.97 | **18.04-20.47** | Chip 4: "Third-party apps (Agent SDK)" reveals at t=18.04 (anchored to "third-party"). Marker on "third-party" word |

**Anchor moments**:
- t=2.558 — narration enters; hero slam visible from beat-1a fade-out
- t=4.149 — marker-highlight on "quiet shift" (the open-loop word per plan.md)
- t=12.91 — chip 1 enters at "Agent S D K"
- t=14.23 — chip 2 enters at "claude dash p"
- t=16.39 — chip 3 enters at "Claude Code GitHub Actions"
- t=18.04 — chip 4 enters at "third-party apps" (the pivot setup)
- t=20.47 — narration ends "the same SDK"; scene exits 0.4s later at 20.5

**Picks**:
1. **`gsap-stagger-grid`** on 4 surface chips — 4 entrances at word-anchored times (12.91 / 14.23 / 16.39 / 18.04). NOT a quick stagger — each chip is its own narration beat.
2. **`marker-highlight`** sweep under "quiet shift" in caption pill — trigger_s=4.149, duration=0.5s, sweep ease `power2.out`.
3. **`blur-crossfade`** exit at scene end — trigger_s=20.5, duration=0.4s, paired with shape-backdrop reposition + `cinematic-whoosh`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh           # transition to Scene 03
    anchor_word_index: 45           # transcript[45] "same" at t=16.93; we shift to scene-end (20.5 - 0.4 = 20.1)
    offset_seconds: 0               # whoosh data-start = 20.1 (composition time)
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Step-by-step reveal cadence**: 4 chips at 12.91 / 14.23 / 16.39 / 18.04 — spacings 1.32s / 2.16s / 1.65s. All under 5s ✓; each anchored to the narration moment naming the surface. **Hidden-until-reveal pattern REQUIRED**: `tl.set("#p1b-chip-N", { y: 30, opacity: 0 }, 0)` at t=0 for all 4 chips, then `tl.to(..., { y: 0, opacity: 1, duration: 0.55, ease: "back.out(1.5)" }, revealTime)`.

**Visual-pacing-5s audit** (every beat in scene 02):
- 2.558 (hero readable) → 4.149 (marker) = 1.6s ✓
- 4.149 → 4.416 (marker complete) — same beat
- 4.416 → 12.91 (chip 1) = **8.5s gap — VIOLATION**

**Resolution**: Insert a `scale-pulse` (1.0→1.04→1.0, duration 0.3, yoyo) on the caption pill "1 monthly credit" element at **t=6.876** (anchored to word[9] "15,"). Then:
- 4.416 → 6.876 (caption pulse) = 2.5s ✓
- 6.876 → 9.918 (chip pre-fade-in at "monthly credit") = 3.0s ✓  *(if you stage chip-row container reveal at this time)*
- Then chip beats: 12.91 / 14.23 / 16.39 / 18.04 / 20.5 (exit) — all ≤ 4.5s gaps ✓

**Shape-backdrop reposition**: scheduled at t=20.1 (scene-end - 0.4) paired with whoosh.

**Why these picks**: The narration packs the hook tempo into the first 2.3s ("Four surfaces. One credit. One quiet shift.") and then enumerates the 4 surfaces sequentially over ~7s of explanation. The chip reveals must anchor to the NAME being spoken, not the start of the surface section. The marker on "quiet shift" pre-loads the open-loop that Scene 03 resolves.

---

### Scene 03: the-shift (data_start=20.9s, data_duration=34.5s)

**Narration window**: composition t=21.40 → t=54.92 (transcript word[47] "But" → word[136] "well." closing "drinking from the same well").
**Words in scene**: 90 (transcript words 47-136).
**Spoken at start**: "But the headline is hiding the actually new thing. Because that fourth surface is where the platform play lives."

**Word-anchor table**:

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| "But the headline is hiding..." | 47-54 | 18.90-21.34 | **21.40-23.84** | Phase 3 enters via blur-crossfade; overline "THE PART ANTHROPIC DIDN'T LEAD WITH" fades in at 21.40 |
| "the actually new thing." | 51-54 | 20.24-21.34 | 22.74-23.84 | Headline "Third-party tools, your credit." (64px) lands at 22.74 |
| "fourth surface" | 58-59 | 22.73-23.33 | 25.23-25.83 | Subtle scale-pulse on overline (1.0→1.03→1.0) at 25.23 |
| "Conductor" | 65 | 26.40 | **28.90** | Stat-pill card LEFT (orange) "CONDUCTOR" enters at 28.90 |
| "OpenClaw" | 67 | 27.10 | **29.60** | Stat-pill card RIGHT (purple) "OPENCLAW" enters at 29.60 |
| "Agent S D K" | 71-75 | 29.44-30.29 | 31.94-32.79 | Mini chip "Built on Agent SDK" appears between cards at 31.94 |
| "now work with your Claude plan." | 76-81 | 30.94-32.51 | 33.44-35.01 | "now work with YOUR plan" sub-line fades in beneath cards |
| "And here's the part Anthropic didn't lead with." | 82-89 | 33.44-35.42 | 35.94-37.92 | Body line transitions; caption pill swap |
| "They draw from your credit" | 90-94 | 36.33-37.39 | **38.83-39.89** | Marker-highlight sweep starts under "draws from your credit" body text at 38.83 (anchored to word "draw") |
| "the same way your own scripts do." | 95-101 | 37.44-38.96 | 39.94-41.46 | Marker completes at 39.89; body line "the same way your own scripts do" appears underlined |
| "if you've been running heavy external tools" | 103-108 | 40.15-41.93 | 42.65-44.43 | Direct-address pill "If you've been on raw API billing..." enters from the left |
| "raw A P I billing" | 109-113 | 42.17-43.28 | 44.67-45.78 | Strike-through animation on the words "raw API billing" |
| "June 15 quietly moves you" | 114-117 | 43.50-45.40 | 46.00-47.90 | Arrow svg morphs from "raw API" → "seat-plan economics" pill |
| "onto seat-plan economics." | 118-120 | 45.73-47.23 | 48.23-49.73 | "seat-plan economics" pill scales up (1.0→1.06→1.0) at 48.23 |
| "Same credit pool, your scripts and someone else's product" | 121-128 | 48.12-51.12 | 50.62-53.62 | Metaphor-line fade-in beneath cards: 2 small icons (you + 3rd-party) drinking from one well-shaped svg |
| "drinking from the same well." | 129-132 | 51.16-52.42 | 53.66-54.92 | Scale-pulse on "well" icon at 53.66 (1.0→1.08→1.0, 0.5s) — completes 54.16 |

**Anchor moments**:
- t=21.40 — Phase 3 begins (overline + headline)
- t=28.90 — Conductor card enters
- t=29.60 — OpenClaw card enters (0.7s after Conductor — quick stagger because narration names them in one sentence)
- t=38.83 — Marker-highlight on "draw from your credit" (the core revelation)
- t=46.00 — Arrow morph from raw API billing to seat-plan
- t=53.66 — Scale-pulse on the "well" metaphor icon (final beat before exit)

**Picks**:
1. **`gsap-stagger-grid`** on Conductor/OpenClaw cards (28.90 / 29.60 — 0.7s gap, the only quick-stagger in the deck because narration names both in one breath).
2. **`marker-highlight`** under "draw from your credit" body line — trigger_s=38.83, duration=0.6s.
3. **`scale-pulse`** on "well" metaphor at 53.66 (yoyo, 0.5s) — pre-exit beat.
4. **`blur-crossfade`** exit at 55.0s, paired with `cinematic-whoosh` @ 54.6.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 136          # word "well." end at 52.42 → comp 54.92; whoosh anchors to scene end
    offset_seconds: -0.32           # whoosh data-start = 54.6
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Visual-pacing-5s audit** (every beat in scene 03):
- 21.40 (overline) → 22.74 (headline) = 1.3s ✓
- 22.74 → 25.23 (scale-pulse overline) = 2.5s ✓
- 25.23 → 28.90 (Conductor card) = 3.7s ✓
- 28.90 → 29.60 (OpenClaw card) = 0.7s ✓
- 29.60 → 31.94 (chip) = 2.3s ✓
- 31.94 → 33.44 (sub-line) = 1.5s ✓
- 33.44 → 35.94 (body swap) = 2.5s ✓
- 35.94 → 38.83 (marker on "draw") = 2.9s ✓
- 38.83 → 44.67 (strike "raw API billing") = 5.84s — **VIOLATION**

**Resolution**: Insert a `scale-pulse` (1.0→1.04→1.0, 0.3s yoyo) on the marker'd body line "draws from your credit" at **t=41.46** (anchored to word "do."). Then:
- 38.83 → 41.46 (scale-pulse) = 2.6s ✓
- 41.46 → 44.67 = 3.2s ✓
- 44.67 → 46.00 (arrow morph) = 1.3s ✓
- 46.00 → 48.23 (seat-plan pill scale) = 2.2s ✓
- 48.23 → 50.62 (metaphor icons) = 2.4s ✓
- 50.62 → 53.66 (well icon pulse) = 3.0s ✓
- 53.66 → 55.0 (exit) = 1.3s ✓ — ALL GAPS UNDER 5s

**Step-by-step reveal cadence**: 2 cards quick-stagger (one narrative breath = OK). The remaining elements are sequential reveals, not enumerated bullets — visual-pacing-5s rule governs.

**Shape-backdrop reposition**: scheduled at t=54.6 paired with whoosh.

**Why these picks**: Scene 3 is the **core revelation** — the open-loop opened in Scene 2's "quiet shift" resolves here. The marker-highlight on "draw from your credit" carries the punchline. The "well" metaphor (last 2s) is the say-it-twice technique — needs a small visual beat to anchor the metaphor.

---

### Scene 04: who-gets-it (data_start=55.4s, data_duration=20.0s)

**Narration window**: composition t=55.86 → t=74.98 (transcript word[137] "And" → word[197] "only." closing "paid plans only").
**Words in scene**: 61 (transcript words 137-197).
**Spoken at start**: "And who actually gets it? Pro. Max. Team. And seat-based Enterprise."

**Word-anchor table**:

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| "And who actually gets it?" | 137-141 | 53.36-54.50 | **55.86-57.00** | Phase 4 overline "WHO ACTUALLY GETS IT" enters at 55.86 |
| "Pro." | 142 | 54.65 | **57.15** | Pill 1 (purple) "PRO" enters — anchored to word "Pro" |
| "Max." | 143 | 55.04 | **57.54** | Pill 2 (blue) "MAX" enters — 0.4s after Pro (quick stagger — narration lists them in one breath) |
| "Team." | 144 | 55.49 | **57.99** | Pill 3 (green) "TEAM" enters — 0.45s after Max |
| "And seat-based Enterprise." | 145-147 | 56.74-58.19 | **59.24-60.69** | Pill 4 (orange) "ENTERPRISE (seat-based)" enters at 59.24 — anchored to "seat-based" |
| "If you're on any of those four tiers" | 148-156 | 58.37-60.27 | 60.87-62.77 | "4 tiers" badge pulses (scale 1.0→1.05→1.0) at 60.87 |
| "the credit is yours on June 15" | 157-162 | 60.37-62.22 | 62.87-64.72 | Mini date-chip "JUNE 15" lights up at 62.87 (the credit-arrives-on date) |
| "no new SKU, no upsell, no migration ticket." | 163-171 | 62.77-65.88 | 65.27-68.38 | Three rapid strike-through chips — "SKU" / "UPSELL" / "MIGRATION TICKET" with cross-out lines, each appears at narration word |
| "If you're on free, this announcement isn't for you." | 172-179 | 66.77-69.30 | 69.27-71.80 | Direct-address pill "Free tier? Not this one." fades in at 69.27 |
| "Anthropic was specific: paid plans only." | 180-185 | 70.20-72.48 | **72.70-74.98** | Closing line "PAID PLANS ONLY." emphasizes at 72.70; tail-hold to 75.0 |

**Anchor moments**:
- t=55.86 — Phase 4 overline (post-crossfade)
- t=57.15 / 57.54 / 57.99 / 59.24 — 4 plan pills enter (quick stagger because narration names them all in 3 seconds)
- t=60.87 — "4 tiers" badge pulse (the direct-address moment)
- t=65.27 / 66.27 / 67.27 — three strike-through chips (no/no/no)
- t=72.70 — "PAID PLANS ONLY." closing emphasis

**Picks**:
1. **`gsap-stagger-grid`** on 4 plan pills — entrances 57.15 / 57.54 / 57.99 / 59.24 (quick stagger justified by single-breath enumeration: "Pro. Max. Team. And seat-based Enterprise.").
2. **`scale-pulse`** on Enterprise pill at 59.94 (1.0→1.06→1.0 yoyo) — Enterprise is the largest/most-emphasized tier in the source.
3. **`blur-crossfade`** exit at 75.0s, paired with `cinematic-whoosh` @ 74.6.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 185          # word "only." end at 72.48 → comp 74.98
    offset_seconds: -0.38           # whoosh data-start = 74.6
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Step-by-step reveal cadence**: The 4 tier pills are an **exception** to the "5s apart" rule because the narration genuinely lists them in a single sentence (one breath, ~1.5s of audio). Quick stagger (0.4s apart) is correct here per `step-by-step-reveal.md` ("For 2–3 items, quick stagger is acceptable if narration genuinely names them all in one sentence" — extended here to 4 because all four are named in 2.5s). Plan.md called for 4s spacing assuming the original 20s spoken — but actual narration delivers all 4 names inside 2.5s, so visual must match.

**Visual-pacing-5s audit** (every beat in scene 04):
- 55.86 (overline) → 57.15 (pill 1) = 1.3s ✓
- 57.15 → 57.54 → 57.99 → 59.24 (4 pills) — internal gaps 0.4/0.45/1.25s ✓
- 59.24 → 60.87 (4-tiers badge pulse) = 1.6s ✓
- 60.87 → 62.87 (June 15 mini-chip) = 2.0s ✓
- 62.87 → 65.27 (strike "SKU") = 2.4s ✓
- 65.27 → 66.27 (strike "UPSELL") = 1.0s ✓
- 66.27 → 67.27 (strike "MIGRATION TICKET") = 1.0s ✓
- 67.27 → 69.27 (direct-address pill) = 2.0s ✓
- 69.27 → 72.70 ("PAID PLANS ONLY") = 3.4s ✓
- 72.70 → 75.0 (exit) = 2.3s ✓ — ALL GAPS UNDER 5s

**Shape-backdrop reposition**: scheduled at t=74.6 paired with whoosh.

**Why these picks**: Plan.md scheduled 4s/pill but the actual narration delivers 4 tier names inside 2.5s. The retiming forces quick-stagger which is GOOD here — the viewer reads each pill as it's named. The tail of the scene has plenty of beats from the "no SKU / no upsell / no migration ticket" trio, so the scene stays alive even after the pills are static.

---

### Scene 05: timeline (data_start=75.4s, data_duration=24.1s)

**Narration window**: composition t=75.93 → t=99.12 (transcript word[198] "Here's" → word[279] "lands." closing "before the credit lands").
**Words in scene**: 82 (transcript words 198-279).
**Spoken at start**: "Here's the timeline, and the part most people are about to miss." (loop opener)

**Word-anchor table**:

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| "Here's the timeline" | 198-200 | 73.43-74.31 | **75.93-76.81** | Phase 5 overline "THE TIMELINE" enters at 75.93 |
| "the part most people are about to miss." | 201-208 | 74.35-76.40 | 76.85-78.90 | Loop-opener teaser pill "MOST PEOPLE WILL MISS THIS" pulses at 78.0 |
| "Today, you do nothing." | 209-212 | 77.32-78.64 | **79.82-81.14** | Timeline card 1 (orange) "TODAY · do nothing" enters at 79.82 (anchored to "Today,") |
| "On June 8," | 213-215 | 78.79-79.54 | **81.29-82.04** | Timeline card 2 (purple) "JUNE 8" begins to enter at 81.29 |
| "you'll get an email to claim your credits" | 216-222 | 79.69-81.52 | 82.19-84.02 | macOS-notification block fires at **82.74** (anchored to word "email" comp-t 82.74) — banner from top-right, persists 3.5s |
| "that's the one beat that needs you." | 223-230 | 81.67-83.59 | 84.17-86.09 | Notification banner stays on screen; "needs you" gets scale-pulse via banner emphasis |
| "And on June 15," | 231-234 | 84.52-85.56 | **87.02-88.06** | Timeline card 3 (blue) "JUNE 15" enters at 87.02 (anchored to "June" word in "June 15"); notification dismisses at 87.5 (slide-out right) |
| "the change goes into effect." | 235-239 | 85.66-87.08 | 88.16-89.58 | Connecting line draws between cards 1→2→3 via gsap-path-draw, completing at 89.58 |
| "If you miss the June 8 email" | 240-246 | 88.00-89.65 | 90.50-92.15 | Sub-line beneath cards: "Missed June 8? Still in — but that email wires the SDK." fades in at 90.50 |
| "but that email is the trigger to wire up the SDK side" | 251-262 | 92.34-95.37 | **94.84-97.87** | Marker-highlight on "trigger" word at **94.84** (anchored to word "trigger" idx 256 t=93.32 → comp 95.82) sweeps 95.82-96.42 |
| "before the credit lands." | 263-266 | 95.42-96.62 | 97.92-99.12 | "before credit lands" body line emphasizes; phase exits 99.5 |

**Anchor moments**:
- t=75.93 — Phase 5 overline (loop opener line landing)
- t=78.0 — "MOST PEOPLE WILL MISS THIS" pulse pill (the loop-opener tension marker)
- t=79.82 — Card 1 "TODAY"
- t=81.29 — Card 2 "JUNE 8"
- t=82.74 — macOS-notification fires (anchored to word "email")
- t=87.02 — Card 3 "JUNE 15"
- t=87.5 — macOS-notification dismisses
- t=89.58 — Connecting line (path-draw) completes
- t=95.82 — Marker-highlight on "trigger" word in the SDK callout

**Picks**:
1. **`gsap-stagger-grid`** on 3 timeline cards — 79.82 / 81.29 / 87.02 (5.7s gap between cards 2 & 3 is justified — the notification fills that window; without it the 5.7s gap would violate). Hidden-until-reveal pattern required.
2. **`gsap-path-draw`** on connecting SVG line between cards 1→2→3 — begins at 87.02 (card 3 enter), completes 89.58.
3. **`macOS-notification`** (registry block) — fires at 82.74 (anchored to word "email" comp-t 82.74), title "Anthropic", message "Claim your programmatic credits", duration ~5s on screen (82.74-87.50). Replaces a card-internal pulse — the notification IS the beat.
4. **`marker-highlight`** on "trigger" word at 95.82, duration 0.6s — emphasizes the action requirement.
5. **`blur-crossfade`** exit at 99.1s, paired with `cinematic-whoosh` @ 98.7.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 279          # word "lands." end at 96.62 → comp 99.12
    offset_seconds: -0.42           # whoosh data-start = 98.7
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Step-by-step reveal cadence**: 3 timeline cards at 79.82 / 81.29 / 87.02. Card 1→2 gap is 1.5s (narration delivers TODAY and JUNE 8 in quick succession, both 4-5 word phrases). Card 2→3 gap is 5.7s — bridged by the macOS-notification which counts as a major visual beat at 82.74 and persists until 87.5. **Hidden-until-reveal**: `tl.set("#p5-card-N", { y: 30, opacity: 0 }, 0)` for all 3 cards at t=0.

**Visual-pacing-5s audit** (every beat in scene 05):
- 75.93 (overline) → 78.0 (loop-opener pulse) = 2.1s ✓
- 78.0 → 79.82 (card 1) = 1.8s ✓
- 79.82 → 81.29 (card 2) = 1.5s ✓
- 81.29 → 82.74 (macOS-notif fires) = 1.5s ✓
- 82.74 → 87.02 (card 3 + notif dismiss) = 4.3s ✓ *(notification body change at 84.17 "needs you" provides a sub-beat)*
- 87.02 → 89.58 (path-draw completes) = 2.6s ✓
- 89.58 → 90.50 (sub-line) = 0.9s ✓
- 90.50 → 95.82 (marker on "trigger") = 5.3s — **VIOLATION**

**Resolution**: Insert a `scale-pulse` (1.0→1.04→1.0, 0.3s yoyo) on the sub-line text at **t=93.34** (anchored to word "trigger" idx 256 transcript t=93.32 + 2.5 = 95.82 — but for the SUB-LINE pulse we anchor 2.5s earlier, at word idx 253 "but" transcript t=92.34 → comp 94.84). Then:
- 90.50 → 94.84 (sub-line scale-pulse on "but that email") = 4.3s ✓
- 94.84 → 95.82 (marker on "trigger") = 1.0s ✓
- 95.82 → 99.5 (exit) = 3.7s ✓ — ALL GAPS UNDER 5s

**Shape-backdrop reposition**: scheduled at t=98.7 paired with whoosh.

**Why these picks**: The 3-card timeline is the spine. The macOS-notification (registry block — `npx hyperframes add macOS-notification --dir videos/anthropic-claude-plan-programmatic-credits` before authoring) is anchored to the word "email" which is itself the source-verbatim noun. The path-draw line ties the 3 cards into a single timeline reading, not 3 isolated cards. The trigger-word marker carries the urgency.

---

### Scene 06: bonus-stack (data_start=99.5s, data_duration=33.0s)

**Narration window**: composition t=99.997 → t=132.05 (transcript word[280] "Plus" → word[366] "one." closing "the bigger one").
**Words in scene**: 87 (transcript words 280-366).
**Spoken at start**: "Plus — stacking on top of all of this — Claude Code weekly limits just went up fifty percent."

**Word-anchor table**:

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| "Plus -- stacking on top of all of this" | 280-289 | 97.50-99.45 | **100.00-101.95** | Phase 6 overline "PLUS — STACKING ON TOP" enters at 100.00 (anchored to word "Plus") |
| "Claude Code weekly limits just went up" | 290-297 | 99.92-101.86 | 102.42-104.36 | Hero stat-pill container appears at 102.42 with placeholder "0%" |
| "fifty percent." | 298-299 | 101.94-102.68 | **104.44-105.18** | **gsap-counter-tween 0→50** fires at 104.44, completes at 105.94 (1.5s duration) — anchored to word "fifty" |
| "Already applied." | 300-301 | 103.59-104.35 | 106.09-106.85 | Side-chip "ALREADY APPLIED" (green check) appears at 106.09 |
| "Nothing to opt into." | 302-305 | 104.39-105.44 | 106.89-107.94 | Side-chip "NOTHING TO OPT INTO" pops at 106.89 |
| "It runs through July 13" | 306-310 | 106.16-107.64 | **108.66-110.14** | Surface chip row container fades in at 108.66 |
| "and it works everywhere you actually use Claude Code" | 311-318 | 107.86-110.78 | 110.36-113.28 | Body line "Works everywhere" fades in at 110.36 |
| "the C L I" | 319-322 | 111.36-112.23 | **113.86-114.73** | Chip 1: "C L I" enters at 113.86 (anchored to "C") |
| "the I D E extensions" | 323-327 | 112.62-114.04 | **115.12-116.54** | Chip 2: "IDE extensions" enters at 115.12 (anchored to "I") |
| "the desktop app" | 328-330 | 114.14-115.08 | **116.64-117.58** | Chip 3: "desktop app" enters at 116.64 (anchored to "desktop") |
| "and the web." | 331-333 | 115.19-115.83 | **117.69-118.33** | Chip 4: "web" enters at 117.69 (anchored to "web") |
| "So if you maxed out last week, you've got more headroom right now." | 334-345 | 116.70-119.60 | 119.20-122.10 | Direct-address pill "Maxed last week? More headroom now." appears at 119.20 |
| "And here's the kicker: this stacks with last week's two-times boost to the five-hour limits." | 346-360 | 120.55-125.06 | **123.05-127.56** | Marker-highlight on "through July 13" body line at **123.05** (anchored to "kicker"); sub-card "+2× 5-hr limits (last week)" enters at 124.5 |
| "Two limit increases inside seven days," | 361-364 | 125.94-127.86 | 128.44-130.36 | "2 INCREASES / 7 DAYS" badge fades in at 128.44 |
| "and the second one is the bigger one." | 365-372 | 127.89-129.55 | **130.39-132.05** | Scale-pulse on the +50% counter at 130.39 (1.0→1.10→1.0, 0.6s) — "the bigger one" emphasis |

**Anchor moments**:
- t=100.00 — Phase 6 overline ("Plus — stacking on top")
- t=104.44 — Counter starts rolling 0→50 (anchored to spoken "fifty")
- t=106.09 / 106.89 — Side chips "ALREADY APPLIED" / "NOTHING TO OPT INTO"
- t=113.86 / 115.12 / 116.64 / 117.69 — 4 surface chips (CLI / IDE / desktop / web)
- t=119.20 — Direct-address pill
- t=123.05 — Marker-highlight on "through July 13"
- t=128.44 — "2 INCREASES / 7 DAYS" badge
- t=130.39 — Scale-pulse on +50% counter ("the bigger one" emphasis)

**Picks**:
1. **`gsap-counter-tween`** 0→50 on hero stat-pill — starts at 104.44 (word "fifty" anchor), duration 1.5s, ease `power2.out`. Hidden-until-reveal: counter shows "0%" until 104.44 then animates.
2. **`gsap-stagger-grid`** on 4 surface chips — entrances 113.86 / 115.12 / 116.64 / 117.69 (anchored to spoken surface names). Hidden-until-reveal pattern.
3. **`marker-highlight`** on "through July 13" body line — trigger_s=123.05, duration=0.6s.
4. **`scale-pulse`** on counter at 130.39 (yoyo 1.0→1.10→1.0, 0.6s) for "the bigger one" emphasis.
5. **`blur-crossfade`** exit at 132.1s, paired with `cinematic-whoosh` @ 131.7.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam                 # discretionary opt-in per plan.md item #13 — counter peak
    anchor_word_index: 299          # word "percent." at t=102.68 → comp 105.18 (counter completes)
    offset_seconds: -0.04           # scale-slam data-start = 105.14
    duration_seconds: 0.73
    track_index: 3
    volume: 0.20
  - cue: cinematic-whoosh
    anchor_word_index: 366          # word "one." end at 129.55 → comp 132.05
    offset_seconds: -0.35           # whoosh data-start = 131.7
    duration_seconds: 0.84
    track_index: 3                  # sequential — scale-slam ends at 105.87, whoosh at 131.7 (no overlap)
    volume: 0.15
```

**Step-by-step reveal cadence**: 4 surface chips at 113.86 / 115.12 / 116.64 / 117.69 — anchored to spoken surface names (CLI / IDE / desktop / web). Spacings 1.3s / 1.5s / 1.05s. Each chip is its own narration beat. **Hidden-until-reveal**: `tl.set("#p6-surface-N", { y: 25, opacity: 0 }, 0)` for all 4 chips at t=0.

**Visual-pacing-5s audit** (every beat in scene 06):
- 100.00 (overline) → 102.42 (stat-pill container) = 2.4s ✓
- 102.42 → 104.44 (counter starts) = 2.0s ✓
- 104.44 → 105.94 (counter completes) — same beat
- 105.94 → 106.09 (side-chip 1) = 0.15s ✓
- 106.09 → 106.89 → 108.66 → 110.36 → 113.86 (surface chip 1) — gaps 0.8 / 1.8 / 1.7 / 3.5s ✓
- 113.86 → 115.12 → 116.64 → 117.69 → 119.20 (direct-address) — gaps 1.3 / 1.5 / 1.05 / 1.5s ✓
- 119.20 → 123.05 (marker on "through July 13") = 3.85s ✓
- 123.05 → 124.5 (sub-card "+2× 5-hr") = 1.45s ✓
- 124.5 → 128.44 (2 INCREASES badge) = 3.94s ✓
- 128.44 → 130.39 (scale-pulse counter) = 1.95s ✓
- 130.39 → 132.1 (exit) = 1.7s ✓ — ALL GAPS UNDER 5s

**Shape-backdrop reposition**: scheduled at t=131.7 paired with whoosh.

**Why these picks**: The counter is the hero element — it MUST anchor to the spoken word "fifty". The chip row maps 1:1 to source bullets (CLI / IDE / desktop / web). The discretionary `scale-slam` SFX on the counter peak is the one place plan.md item #13 allows opt-in beyond Anthropic-default no-per-element-SFX — justified here because "+50%" is the dramatic numeric reveal of the bonus segment.

---

### Scene 07: reactions-montage (data_start=132.5s, data_duration=41.1s)

**Narration window**: composition t=132.99 → t=173.22 (transcript word[367] "So" → word[503] "answer." closing "Anthropic didn't answer").
**Words in scene**: 137 (transcript words 367-503).
**Spoken at start**: "So how is the community taking it?"

This scene cycles **5 anonymized x-post reaction cards** (one per sentiment beat). Each card persists ~7-8s, with a 0.4s crossfade between cards. Mutex visibility — only one card visible at a time inside `#phase6` (per plan.md). The sentiment bucket label chip (top-right) swaps colors with each card: GREEN (pragmatic) / RED (critical) / BLUE (confused) / GREEN (pragmatic) / BLUE (confused).

**Card sequence and word anchors**:

| # | Handle | Sentiment | Quote (verbatim from source.md §4) | First word | Transcript t | Comp t (card enters) | Card exits |
|---|---|---|---|---|---|---|---|
| 1 | **@cardholder** | PRAGMATIC (green) | "makes the paid plan easier to justify to whoever approves the card." | "Card-approval crowd is happy..." (word 374) | 132.81 | **135.31** | 142.30 |
| 2 | **@oldschool** | CRITICAL (red) | "your competitors will thank you, genius way to relocate customers." | "The veterans are more sour..." (word 392) | 141.14 | **143.64** | 150.10 |
| 3 | **@cynicop** | CRITICAL (red) | "this is how you know when a startup becomes enterprisey." | "The cynics call it..." (word 411) | 148.16 | **150.66** | 156.50 |
| 4 | **@builderx** | PRAGMATIC (green) | "Anthropic quietly making it easier to go from idea to production." | "The builder camp sees the platform play..." (word 433) | 153.44 | **155.94** | 163.00 |
| 5 | **@skeptic42** | CONFUSED (blue) | "does previous usage remain the same alongside the new monthly credits?" | "And then there's the still-confused..." (word 452) | 160.66 | **163.16** | 171.50 |

(Note: card 3 enters at 150.66s but card 2 only exits at 150.10 — so cards 2→3 transition uses a 0.5s crossfade overlapping 150.10-150.60. Card 4 enters 155.94 but card 3 exits 156.50 — 0.5s overlap 155.94-156.44. Card 5 enters 163.16 but card 4 exits 163.00 — 0.16s overlap; tighten to 0.3s crossfade by adjusting card 5 entry to 163.00.)

**Adjusted card timings** (clean 0.4s crossfades, mutex):

| # | Handle | Sentiment | Card data_start (comp) | Card data_duration | Notes |
|---|---|---|---|---|---|
| 1 | @cardholder | PRAGMATIC | 135.31 | 7.0s (135.31-142.31) | enters at "Card-approval" word |
| 2 | @oldschool | CRITICAL | 142.00 | 7.7s (142.00-149.70) | 0.4s crossfade overlap with card 1 at 141.91-142.31 |
| 3 | @cynicop | CRITICAL | 149.40 | 6.2s (149.40-155.60) | 0.4s crossfade overlap with card 2 at 149.30-149.70 |
| 4 | @builderx | PRAGMATIC | 155.30 | 7.6s (155.30-162.90) | 0.4s crossfade overlap with card 3 at 155.20-155.60 |
| 5 | @skeptic42 | CONFUSED | 162.60 | 8.5s (162.60-171.10) | 0.4s crossfade overlap with card 4 at 162.50-162.90; persists through "That last one is the question Anthropic didn't answer." |
| (tail) | — | — | 171.10-173.2 | 2.1s tail-hold + "Anthropic didn't answer" line emphasis below the card | |

**Word-anchor table for in-card retention beats** (scale-pulse on each card's quote-peak word):

| Card | Quote-peak word | Transcript idx | Transcript t | Comp t | Scale-pulse |
|---|---|---|---|---|---|
| 1 @cardholder | "justify" | 386 | 138.07 | 140.57 | Scale-pulse on quote text (1.0→1.04→1.0, 0.3s) at 140.57 |
| 2 @oldschool | "genius" | 401 | 145.03 | 147.53 | Scale-pulse on "genius way to relocate" at 147.53 |
| 3 @cynicop | "enterprisey." | 422 | 151.75 | 154.25 | Scale-pulse on "enterprisey" at 154.25 |
| 4 @builderx | "idea to production." | 449-451 | 158.73-159.82 | 161.23-162.32 | Scale-pulse on "idea to production" at 161.23 |
| 5 @skeptic42 | "monthly credits?" | 469-470 | 166.45-167.37 | 168.95-169.87 | Scale-pulse on "credits?" at 168.95 |

**Anchor moments**:
- t=132.99 — Phase 7 enters via crossfade; question overline "HOW IS THE COMMUNITY TAKING IT?"
- t=135.31 → 171.10 — 5 reaction cards cycling
- t=171.10 → 173.2 — tail hold on card 5; "Anthropic didn't answer" line emphasizes underneath
- t=172.8 — `cinematic-whoosh` SFX
- t=173.2 — phase exits

**Picks**:
1. **`x-post` block × 5** (registry block — requires `npx hyperframes add x-post --dir videos/anthropic-claude-plan-programmatic-credits` before authoring). Each instance configured with handle / quote / sentiment color. Mutex-stacked inside `#phase6` per plan.md.
2. **`scale-pulse`** on each card's quote-peak word (5 mini-pulses) — visual-pacing-5s compliance inside each card.
3. **`blur-crossfade`** exit at 173.2s, paired with `cinematic-whoosh` @ 172.8.

(Sentiment chip swap is part of the x-post block configuration, not a separate primitive.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 503          # word "answer." end at 170.72 → comp 173.22
    offset_seconds: -0.42           # whoosh data-start = 172.8
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
  # NOTE: Per plan.md item #13, no per-card-swap SFX — the visual transition between cards is enough.
  # Adding 5 spring-pops here would muddy the narration's emotional arc.
```

**Step-by-step reveal cadence**: 5 cards swap at ~7s intervals (135.31 / 142.00 / 149.40 / 155.30 / 162.60). Each swap IS a beat. Internal scale-pulse on quote-peak word inside each card provides a sub-beat ~3-4s into each card (so no 5s gap inside any single card).

**Visual-pacing-5s audit** (every beat in scene 07):
- 132.99 (Phase 7 overline) → 135.31 (card 1 enters) = 2.3s ✓
- Card 1: 135.31 (entry) → 140.57 (scale-pulse on "justify") → 142.00 (card 2 enters) — gaps 5.26 / 1.43s — **5.26 marginal**. Pulse a bit earlier — move card 1 quote-pulse to 138.7 anchored to "easier" (transcript idx 384 t=137.42 → comp 139.92). Re-audit: 135.31 → 139.92 = 4.6s ✓, 139.92 → 142.00 = 2.1s ✓.
- Card 2: 142.00 → 147.53 (scale-pulse "genius") → 149.40 (card 3) — gaps 5.53 / 1.87s. **5.53 violation** — move pulse earlier to anchor on "sour" word (idx 397 t=142.16 → comp 144.66). Re-audit: 142.00 → 144.66 = 2.66s ✓; 144.66 → 147.53 add a second pulse on "genius" at 147.53; 144.66 → 147.53 = 2.87s ✓; 147.53 → 149.40 = 1.87s ✓.
- Card 3: 149.40 → 154.25 (scale-pulse "enterprisey") → 155.30 (card 4) — gaps 4.85 / 1.05s ✓
- Card 4: 155.30 → 161.23 (scale-pulse "idea to production") → 162.60 (card 5) — gaps **5.93 / 1.37s**. Move pulse earlier to "platform play" (word 438-439 idx 154.82 transcript → comp 157.32). Re-audit: 155.30 → 157.32 = 2.02s ✓; 157.32 → 161.23 = 3.91s ✓; 161.23 → 162.60 = 1.37s ✓.
- Card 5: 162.60 → 168.95 (scale-pulse "credits?") → 171.10 (card stays, tail hold begins) — gaps **6.35 / 2.15s**. Add a second pulse at 166.00 anchored to "alongside" word (transcript 165.50 → comp 168.00 — actually use "remain the same" word 466 t=164.50 → comp 167.00). Re-audit: 162.60 → 167.00 = 4.4s ✓; 167.00 → 168.95 = 1.95s ✓; 168.95 → 171.10 = 2.15s ✓.
- 171.10 → 173.2 (tail hold + "didn't answer" line emphasis at 172.5) = 2.1s with internal beat ✓ — ALL GAPS UNDER 5s

**Updated card-internal scale-pulse anchors** (corrected for 5s rule):

| Card | Pulse anchor word | Comp t | Notes |
|---|---|---|---|
| 1 @cardholder | "easier" | 139.92 | (was "justify" at 140.57 — too late; "easier" is earlier in same quote) |
| 2 @oldschool | "sour" + "genius" (DUAL) | 144.66 + 147.53 | (single pulse left a 5.5s gap; dual pulse compliant) |
| 3 @cynicop | "enterprisey." | 154.25 | (unchanged — already compliant) |
| 4 @builderx | "platform play" | 157.32 | (was "idea to production" at 161.23 — too late; "platform play" is the overline word) |
| 5 @skeptic42 | "remain the same" + "credits?" (DUAL) | 167.00 + 168.95 | (single pulse left a 6.35s gap; dual pulse compliant) |

**Shape-backdrop reposition**: scheduled at t=172.8 paired with whoosh.

**Why these picks**: 5 cards × 5 sentiment buckets is the social-proof scene's load-bearing structure. The `x-post` registry block solves the visual presentation cleanly. The sentiment chip swap (PRAGMATIC/CRITICAL/CONFUSED) creates a meta-rhythm — viewer reads "happy people, critics, builders, confused" as one cohesive sentiment-spectrum tour, not 5 disconnected quotes. Per-card scale-pulse on a peak word ensures no card holds static for >5s.

---

### Scene 08: big-question (data_start=173.6s, data_duration=32.4s)

**Narration window**: composition t=174.14 → t=205.62 (transcript word[504] "Which" → word[638] "zero." closing the URL spelling).
**Words in scene**: 135 (transcript words 504-638).
**Spoken at start**: "Which leaves one question. Is letting Conductor and OpenClaw draw from your plan credit a real unlock for builders — or the polite way to migrate heavy programmatic users off raw API billing..."

**Word-anchor table**:

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| "Which leaves one question." | 504-507 | 171.64-172.87 | **174.14-175.37** | Phase 8 enters; overline "THE QUESTION" + transition setup |
| "Is letting Conductor and OpenClaw draw from your plan credit" | 508-517 | 173.48-176.19 | **175.98-178.69** | TOP HALF: "GAME CHANGER" (green, 120px) slides UP into view from below at 175.98 (anchored to "Is letting") |
| "a real unlock for builders" | 518-521 | 176.80-178.56 | 179.30-181.06 | "real unlock for builders" caption fades in below "GAME CHANGER" header at 179.30 |
| "or the polite way to migrate heavy programmatic users off raw API billing" | 522-535 | 178.74-184.00 | **181.24-186.50** | BOTTOM HALF: "BACKDOOR PRICE HIKE?" (red, 120px) slides DOWN into view from above at 181.24 (anchored to "or") |
| "and into a predictable seat-credit bucket?" | 536-541 | 184.29-186.45 | 186.79-188.95 | "polite migration off raw API" caption fades in below "BACKDOOR PRICE HIKE?" at 186.79 |
| "Anthropic frames it as a vault opening." | 542-547 | 187.32-189.41 | **189.82-191.91** | Center-screen divider line emphasizes; "vault opening" word gets marker-highlight at 189.82 |
| "Some users frame it as a vault being repointed." | 548-557 | 189.81-192.55 | 192.31-195.05 | Center icon: vault SVG morphs — opens at "frames it as a vault opening" (190.5), then morphs to "repointed" at 193.5 |
| "Both readings hold up under the same support article" | 558-566 | 192.94-195.64 | **195.44-198.14** | Subtitle pill "Both readings hold up — same article" at 195.44 |
| "link on screen" | 567-569 | 195.66-196.92 | 198.16-199.42 | URL pill begins enter animation at 198.16 |
| "support dot claude dot com..." | 570-575 | 197.03-198.45 | **199.53-200.95** | URL pill fully visible at 199.53: `support.claude.com/en/articles/15036540` (mono 56px) |
| "...slash articles slash one-five-zero-three-six-five-four-zero." | 576-580 | 198.51-203.12 | 201.01-205.62 | Marker-highlight sweep under URL pill — begins at **201.01** (anchored to "articles"), 0.7s sweep — completes 201.71 |
| (URL spelled, exit setup) | — | — | 203.62-205.6 | URL pill scale-pulse (1.0→1.04→1.0, 0.4s yoyo) at 203.62; phase exits 205.6 |

**Anchor moments**:
- t=174.14 — Phase 8 overline "THE QUESTION"
- t=175.98 — "GAME CHANGER" (green) slides up
- t=181.24 — "BACKDOOR PRICE HIKE?" (red) slides down
- t=189.82 — Marker on "vault opening" in narration body
- t=192.31 — Vault icon morphs (visual metaphor)
- t=199.53 — URL pill enters
- t=201.01 — Marker-highlight sweep under URL
- t=203.62 — Scale-pulse on URL pill (final beat before exit)

**Picks**:
1. **`gsap-fromto`** on split halves — GAME CHANGER slides up from y=200, BACKDOOR PRICE HIKE? slides down from y=-200. Hidden-until-reveal pattern. Halves enter at 175.98 / 181.24.
2. **`marker-highlight`** under URL pill — trigger_s=201.01, duration=0.7s, sweep ease `power2.out`.
3. **`scale-pulse`** on URL pill at 203.62 (yoyo 1.0→1.04→1.0, 0.4s) — pre-exit beat.
4. **`blur-crossfade`** exit at 205.6s, paired with `cinematic-whoosh` @ 205.2.

(The vault-icon morph is a sub-beat handled inline in the composition build, not a separate primitive pick.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 638          # word "zero." end at 203.12 → comp 205.62
    offset_seconds: -0.42           # whoosh data-start = 205.2
    duration_seconds: 0.84
    track_index: 3
    volume: 0.15
```

**Visual-pacing-5s audit** (every beat in scene 08):
- 174.14 (overline) → 175.98 (GAME CHANGER slide) = 1.8s ✓
- 175.98 → 179.30 (real-unlock caption) = 3.3s ✓
- 179.30 → 181.24 (BACKDOOR slide) = 1.9s ✓
- 181.24 → 186.79 (polite-migration caption) = **5.55s — VIOLATION**

**Resolution**: Insert a `scale-pulse` (1.0→1.04→1.0, 0.3s yoyo) on the divider line between the two halves at **t=184.50** (anchored to word "into" idx 535 t=184.64 → comp 187.14 — actually use word "off" idx 530 t=182.53 → comp 185.03). Then:
- 181.24 → 185.03 (divider pulse) = 3.8s ✓
- 185.03 → 186.79 (polite-migration caption) = 1.8s ✓
- 186.79 → 189.82 (vault-opening marker) = 3.0s ✓
- 189.82 → 192.31 (vault icon morph) = 2.5s ✓
- 192.31 → 195.44 (Both readings pill) = 3.1s ✓
- 195.44 → 198.16 (URL pill enter begin) = 2.7s ✓
- 198.16 → 199.53 (URL pill visible) = 1.4s ✓
- 199.53 → 201.01 (URL marker sweep) = 1.5s ✓
- 201.01 → 203.62 (URL scale-pulse) = 2.6s ✓
- 203.62 → 205.6 (exit) = 2.0s ✓ — ALL GAPS UNDER 5s

**Shape-backdrop reposition**: scheduled at t=205.2 paired with whoosh.

**Why these picks**: Scene 8 is the **debate frame** — split-headline carries the binary framing visually before the spoken CTA. The marker on the URL is the only marker in the scene (cap respected). The URL pill scale-pulse at 203.62 immediately before the final exit primes the viewer for the closing thumbnail frame.

---

### Scene 09: thumbnail-close (data_start=206.0s, data_duration=10.5s)

**Narration window**: composition t=206.50 → t=215.01 (transcript word[639] "So" → word[657] "news." closing "Claude news").
**Words in scene**: 19 (transcript words 639-657).
**Spoken at start**: "So -- OpenClaw and Conductor on your plan. Game changer, or backdoor price hike? Drop your pick below, and subscribe for more Claude news."

**Word-anchor table**:

| Narration phrase | Transcript idx | Transcript t | Comp t | On-screen action |
|---|---|---|---|---|
| (All thumbnail elements pre-positioned, opacity 0 until 206.0) | — | — | 206.0 | Phase 9 enters via crossfade from Phase 8 |
| (entrance burst 0.5s) | — | — | **206.0-206.5** | All 5 thumbnail elements enter together within 0.5s (0.3s stagger total): topic recap → logo → receipt → URL pill → CTA question |
| "So -- OpenClaw and Conductor on your plan." | 639-647 | 204.00-206.15 | 206.50-208.65 | Narration overlays held-still thumbnail frame |
| "Game changer," | 648-649 | 207.13-207.77 | **209.63-210.27** | CTA question element scale-pulses (1.0→1.04→1.0, 0.4s yoyo) at 209.63 (anchored to "Game changer,") |
| "or backdoor price hike?" | 650-653 | 207.87-209.11 | 210.37-211.61 | CTA question element pulses again on "backdoor price hike?" at 210.37 — dual pulse for "either/or" emphasis |
| "Drop your pick below, and subscribe for more Claude news." | 654-657 | 209.51-212.52 | 212.01-215.01 | Subscribe-ask pill emphasizes; URL pill subtle glow at 213.0 |
| (terminal hold) | — | — | 215.01-216.5 | Static held frame — composition tail (1.49s held still, qualifying as terminal thumbnail) |

**Anchor moments**:
- t=206.0-206.5 — All 5 thumbnail elements enter together (0.3s stagger inside 0.5s)
- t=209.63 — CTA question scale-pulse on "Game changer," 
- t=210.37 — CTA question scale-pulse on "backdoor price hike?"
- t=215.01 — Narration ends; terminal hold begins
- t=215.01-216.5 — Held static thumbnail-grade frame (1.49s)

**Picks**:
1. **`static held-frame`** after 0.5s entrance burst — all 5 thumbnail elements at final transform from 206.5s onward.
2. **`scale-pulse`** on CTA question (dual: 209.63 + 210.37) for "game changer / backdoor price hike" emphasis. Both compliant with visual-pacing-5s.

**SFX cues**: none. The terminal hold is silent (narration ends at 215.01, then 1.49s of pure visual). Per plan.md item #13, no per-element SFX in final phase.

**Thumbnail-grade audit** (per `.claude/rules/shorts-thumbnail-frames.md`):
1. **Topic statement** (160px): "PROGRAMMATIC CREDITS" (orange accent on "CREDITS") ✓
2. **Visual anchor**: Anthropic logo (~120px height) ✓
3. **Brand chrome**: Anthropic top banner (persists from template) ✓
4. **Outcome receipt** (44px): "JUNE 15 · 4 SURFACES · 4 PLANS" ✓
5. **CTA pill** (52px): "OpenClaw + Conductor on your plan — game changer or backdoor price hike?" (orange with italic accents) — matches spoken closer verbatim ✓
**Verdict**: PASS. Terminal hold = 1.49s (216.5 - 215.01) — under the recommended ≥1.5s but acceptable given the dual-pulse before the hold gives the eye a settled-then-still beat. **If Phase 4 wants extra safety, extend composition to 216.6s for a clean 1.59s hold** — minor adjustment, no other timing impact.

**Visual-pacing-5s audit** (every beat in scene 09):
- 206.0-206.5 (entrance burst) → 209.63 (CTA pulse 1) = 3.13s ✓
- 209.63 → 210.37 (CTA pulse 2) = 0.74s ✓
- 210.37 → 213.0 (URL glow) = 2.6s ✓
- 213.0 → 215.01 (narration end) = 2.0s ✓
- 215.01 → 216.5 (terminal hold) — explicitly relaxed per `shorts-thumbnail-frames.md` (terminal hold ≤ 2.5s exception)
- ALL GAPS UNDER 5s (or under the exception)

**Shape-backdrop reposition**: N/A — final phase, backdrop holds final position.

**Why these picks**: This is the thumbnail-grade close. 5 elements + dual scale-pulse on the CTA question to mirror the spoken "Game changer / backdoor price hike" beat. The 1.49s held-still tail is the YouTube-loop frame: a viewer pausing on the last frame, screenshotting, or seeing the loop-restart preview gets a clean topic + brand + question composite. Engagement-CTA rule satisfied: spoken (this scene), on-screen (`#p9-cta-question`), and YouTube description (Phase YT) all agree.

---

## Picks Cross-Reference (validate against menu)

| Pick name | Where it lives | Confirmed valid? |
|-----------|----------------|------------------|
| `static-lockup` | Anthropic template beat-1a pattern (CLAUDE.md, plan.md) | ✓ |
| `opacity-fade` | GSAP primitive (`tl.to(target, { opacity: 0, ... })`) | ✓ |
| `gsap-stagger-grid` | GSAP idiom — multiple `tl.to()` with `+= delta` (CLAUDE.md Key Rule #3) | ✓ |
| `marker-highlight` | Standard HyperFrames sweep marker (width 0→100% on a `<span class="marker">`) | ✓ |
| `scale-pulse` | GSAP idiom — `tl.to(target, { scale: 1.04, yoyo: true, repeat: 1 })` | ✓ |
| `gsap-counter-tween` | GSAP `tl.to({ val: 0 }, { val: 50, onUpdate })` pattern (CLAUDE.md / hyperframes-pitfalls.md) | ✓ |
| `gsap-path-draw` | SVG `stroke-dasharray` / `stroke-dashoffset` GSAP tween — standard HyperFrames | ✓ |
| `gsap-fromto` | GSAP `tl.fromTo()` — standard | ✓ |
| `blur-crossfade` | Template default transition (plan.md `composition_layout.transitions`) | ✓ |
| `macOS-notification` | **Registry block** — `.claude/rules/registry-blocks-catalog.md` "Animation & effects" table | ✓ (`hyperframes add macOS-notification`) |
| `x-post` | **Registry block** — `.claude/rules/registry-blocks-catalog.md` "Social media overlays" table | ✓ (`hyperframes add x-post`) |
| `cinematic-whoosh` | SFX cue from `shared/audio/MANIFEST.md` | ✓ (Duration 0.84s, default volume 0.15) |
| `scale-slam` | SFX cue from `shared/audio/MANIFEST.md` (Scene 6 discretionary opt-in) | ✓ (Duration 0.73s, default volume 0.20) |

All pick names verified against the canonical sources. **No invented names.**

---

## Override Notes

Phase 4 (composition build via `/diy-yt-creator:new-anthropic-short`) reads this file as authoritative. To override any pick:

1. **Edit `data_start` / `data_duration`**: keep total = 216.5s; preserve scene order; preserve crossfade overlap windows.
2. **Swap a registry block**: must come from `.claude/rules/registry-blocks-catalog.md`. Update the Picks Cross-Reference table.
3. **Adjust word anchors**: re-derive from `transcript.json` (transcript_t + 2.5s = composition_t). Never use the original plan.md timings — those were sized for 180s narration.
4. **Add/remove markers**: cap is 2 per scene. Currently 5 markers across 9 scenes — room for ~13 more if needed.
5. **Add/remove SFX**: per plan.md item #13, Anthropic-default is no per-element SFX. The 7 cinematic-whoosh + 1 scale-slam are the full audio plan. Adding more requires explicit justification.

**Build-time action items for Phase 4**:
1. Insert 2.5s silent pad at head of `audio/narration.wav` before wiring `<audio>` element. Use `ffmpeg -i narration.wav -af "adelay=2500|2500" narration-padded.wav` (or equivalent), then rename. **VERIFY**: `ffprobe narration-padded.wav` should report duration ≈215.0s (original 212.5 + 2.5 pad).
2. Run `npx hyperframes add macOS-notification --dir videos/anthropic-claude-plan-programmatic-credits` before authoring Scene 5.
3. Run `npx hyperframes add x-post --dir videos/anthropic-claude-plan-programmatic-credits` before authoring Scene 7.
4. Set `#root data-duration="216.5"`. Adjust if Phase 4 finds the terminal hold needs extending (recommend 216.6s for ≥1.5s clean hold).
5. Add `tl.set({}, {}, 216.5)` as the LAST line of every scene's timeline to extend GSAP timeline length to full composition duration (per `.claude/rules/hyperframes-pitfalls.md` §1).
