# Retention Strategy: openclaw-100-codex-fleet

Per-scene retention picks, with timings anchored to `transcript.json` (1298 words, 527.01s actual narration vs 540s planned composition). Phase 4 (composition build) reads this file as authoritative.

**Narration-vs-plan drift note**: Total narration ends at 527.01s; plan duration is 540s. The two Hostinger midrolls (s04, s08) are silent blocks — no narration runs during them, yet the audio file appears to have NO 20s gaps (narration runs continuously from s03 → s05 and s07 → s09). This means: either (a) the host sponsor reads are missing from the audio and must be added later, or (b) Phase 4 should keep the plan's scene boundaries at 540s and accept a 13s narration shortfall (the last scene will hold visually for 13s of silence). Either way, retention picks below use the plan's scene `data_start`/`data_duration` for sub-comp authoring, but anchor marker / card / counter triggers to the ACTUAL narration words found in `transcript.json`. Phase 4 must reconcile.

**Primary transition (per `retention-components-hyperframes.md` §4)**: `blur-crossfade` — used at 12 of 12 scene boundaries (calm news-explainer voice profile). 1.1s duration, `sine.inOut` ease. No exit animations on non-final scenes (per §8 anti-pattern).

**Caption pattern (one only across all scenes)**: `caption-fade-slide` — measured news-explainer voice; word groups of 3-5; positioned 80-120px from bottom of 1080-tall canvas (long-form per §2 positioning rule). Block-internal scenes (s04, s08) and the held-still terminal window (post-525s in s13) have captions paused.

**Marker cap audit (per §1 frequency cap, max 2 markers per scene)**: every scene below has ≤ 2 marker-* primitives. Confirmed.

---

## Summary Table

| Scene | Pattern (§7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|---|---|---|---|---|---|---|
| s01 hook | `hero-slam` + receipt | `gsap-stagger-grid` (3-slam stack), `marker-highlight` (ZERO), `gsap-counter-tween` (847.5K views), `spring-pop` (tweet card) | none (too dense) | none | `blur-crossfade` | 4 |
| s02 thesis | `narrated-stat-reveal`-quote hybrid | `gsap-typewriter` (quote glyph-stagger), `marker-highlight` (tokens don't matter), `spring-pop` (attribution chip) | `caption-fade-slide` | none | `blur-crossfade` | 4 |
| s03 avalanche | `timeline-cards` x10 | `gsap-stagger-grid` (10 use-case cards, narration-paced), per-card `pop` chip entrance, `gsap-counter-tween` (10 cards counter top-right) | `caption-fade-slide` | none | `blur-crossfade` | 3 |
| s04 midroll-1 | block-internal | hostinger-midroll block (BRAND-LOCKED, no per-scene picks) | none | none | block-internal fade | 0 (block carries its own retention) |
| s05 clawsweeper | explainer + `stat-pill-row` | `gsap-stagger-grid` (4 lanes), `gsap-counter-tween` (3,478 / 4 / 0.1%), `marker-circle` (4 / 3,478 fraction), `gsap-stagger-grid` (3 safety chips at tail) | `caption-fade-slide` | `audio-reactive-glow` (subtle on 0.1% stat at reveal) | `blur-crossfade` | 5 |
| s06 crabbox | explainer + hero | `gsap-typewriter` (brew install line), `gsap-path-draw` (Cloudflare → 7 backends), `gsap-stagger-grid` (3 OS-VNC frames), `marker-highlight` (never holds cloud credentials), Telegram-demo phone-mockup with `spring-pop` | `caption-fade-slide` | none | `blur-crossfade` | 5 |
| s07 clawpatch | explainer + grid | `gsap-stagger-grid` (5 semantic units), `gsap-stagger-grid` (6 findings categories with severity chips), `marker-highlight` (semantic units), `gsap-stagger-grid` (markdown + JSON output chips tail) | `caption-fade-slide` | none | `blur-crossfade` | 4 |
| s08 midroll-2 | block-internal | hostinger-midroll block (BRAND-LOCKED, no per-scene picks) | none | none | block-internal fade | 0 (block carries its own retention) |
| s09 fleet-recap | architecture-stack | `gsap-stagger-grid` (5 layers), `gsap-path-draw` (right-bracket "~100-agent fleet" label), `marker-highlight` (three thin, well-scoped tools) | `caption-fade-slide` | none | `blur-crossfade` | 3 |
| s10 community-split | `timeline-cards` x5 paced | `gsap-stagger-grid` (5 bucket cards, ~18s apart, hidden-until-reveal `tl.set` pattern), per-card mid-beat `gsap-typewriter` for sub-quote, per-card `pop` icon, `marker-highlight` (each card's tagline as it enters — but max 2 active at once per §1) | `caption-fade-slide` | none | `blur-crossfade` | 4 |
| s11 cost-twist | quote + reveal | `gsap-typewriter` (quote glyph-stagger), `gsap-counter-tween` (70% scale-pulse), `marker-highlight` (It's not cost. It's latency.), `spring-pop` (Codex Speed docs URL chip) | `caption-fade-slide` | none | `blur-crossfade` | 4 |
| s12 support pillar | `cta-url-slam`-light | `gsap-stagger-grid` (3 icons: subscribe + bell + like, 0.5s apart), per-icon `spring-pop`, `marker-highlight` (cheapest way to support the channel) | none (15s, narrator covers) | none | `blur-crossfade` | 3 |
| s13 cta + final frame | `cta-url-slam` + terminal hold | `gsap-stagger-grid` (Yes/No/Hell No chips), `marker-circle` (debate question), `audio-reactive-glow` (subscribe pill subtle treble — first 15s only, cuts at 525s for freeze), final 5s+ frozen at thumbnail composition | `caption-fade-slide` (cuts at 525s) | `audio-reactive-glow` (subscribe pill, 510-525s only) | none (final scene) | 4 |

**Totals**: 11 active scenes (s04 + s08 are block-mounts, zero picks). 43 primitives + components + effects across the 11 active scenes. Plus 12 root-level `blur-crossfade` transitions at scene boundaries (offset `data_start - 0.4s` per long-form template pattern).

---

## Scene-by-Scene Detail

### Scene 01 — Cold-open hook (data_start=0s, data_duration=25s)

Narration excerpt: "One developer. A hundred AI agents reviewing every line of code he ships. Zero junior PR reviewers."

Anchors (from `transcript.json`):
  - "One developer" — idx=0, t=0.04-0.81s (hook slam #1)
  - "A hundred AI agents" — idx=2-5, t=0.99-2.17s (hook slam #2)
  - "Zero junior PR reviewers" — idx=13-16, t=5.17-7.06s (PIVOT — hook slam #3)
  - "847,000" — NOT FOUND verbatim; spoken phrase "847,000 viewers" appears around idx=43 area; needs ffprobe re-check OR script-source phrasing differs (script says "847,000 viewers"; check transcript more carefully if exact verbatim needed)
  - "People started freaking out" — idx=50, t=22.07s (transition-out narration; tail content)

Retention picks:
  1. `gsap-stagger-grid` — at t=0.0s (slam 1), 1.0s (slam 2), 5.0s (slam 3) — purpose: 3-slam vertical stack reveals "ONE DEV." → "100 AI AGENTS." → "ZERO JUNIOR PR REVIEWERS." synced to spoken word boundaries — source: GSAP effects (`gsap-stagger-grid`)
  2. `marker-highlight` — at t=5.17s (sweep starts when "Zero" begins) — purpose: crab-red underline sweep under "ZERO" — the pivot word — source: marker primitives (`marker-highlight`)
  3. `gsap-counter-tween` — at t=11-15s — purpose: tweet preview card includes "847.5K views" chip ticking 0 → 847500 over 1.2s as the receipt card enters — source: GSAP effects (`gsap-counter-tween`)
  4. `spring-pop` — at t=14.5s — purpose: tweet preview card enters from right after the 3-stack header slides left, settled in 0.45s — source: shared lib (`shared/lib/components/spring-pop` analog via GSAP `back.out(1.7)`)
  5. Trailing pivot — at t=22.07s ("People started freaking out") — soft scale-pulse on the tweet card to re-anchor eye before s02 crossfade

Visual-pacing audit:
  - Gaps: 0→1s, 1→5s, 5→11s (6s — VIOLATION), 11→14.5s, 14.5→22s (7.5s — VIOLATION), 22→25s
  - Two gaps exceed 5s. Add beats:
    - At t=8.5s: shape-backdrop reposition pulse (counted as ambient, NOT a foreground beat — still need a foreground beat); use a sub-line entrance "847,000 viewers this week" (script word "viewers" if anchorable; else mid-sentence underline beat on "every PR")
    - At t=18s: `marker-highlight` (second; brings scene to cap of 2) under "freaking out about the bill" — anchors the transition narrative
  - Re-audit: 0→1→5→8.5→11→14.5→18→22→25, max gap 4.5s. ✓

Step-by-step audit: 3 hero slams enter at narration word starts (NOT all at once — explicitly `tl.set` hidden-until-reveal per `step-by-step-reveal.md`).

GSAP / motion notes:
  - Slams use `back.out(1.7)` for snap-in
  - Glyph-stagger per word for slam 1/2/3 — `stagger: 0.04`
  - Use shared lib `magnet-snap-letters` (per `shared/lib/components/magnet-snap-letters/`) on slam 3 ("ZERO JUNIOR PR REVIEWERS.") for tactile pivot impact
  - Use shared lib `hero-slam-shake.js` (per `shared/lib/effects/hero-slam-shake.js`) on slam 1 and slam 2 for ±5px inline shake
  - SFX cues (from `shared/audio/MANIFEST.md`): `sonic-logo` at t=0 (one-shot brand stinger, vol 0.60), `impact-slam` at t=0.04 (slam 1, vol 0.20), `scale-slam` at t=1.0 (slam 2, vol 0.20), `impact-slam` + `screen-shake` LAYERED at t=5.0 (slam 3 pivot, vol 0.20 + 0.15), `spring-pop` at t=14.5 (tweet card, vol 0.15), `cinematic-whoosh` at t=24.6 (scene crossfade lead-in, vol 0.15)

---

### Scene 02 — The thesis (data_start=25s, data_duration=30s)

Narration excerpt: "Here's the question he's actually trying to answer. Quote. How would we build software in the future if tokens don't matter?"

Anchors (from `transcript.json`):
  - "the question he's actually" — idx=72, t=31.10s
  - "Quote" — idx=79, t=34.14-34.55s (script signal)
  - "future if tokens" — idx=87, t=36.80-37.89s
  - "don't matter" — idx=90, t=37.95-38.59s (THE key phrase)
  - "scarcity is already gone" — idx=145, t=58.20-59.79s (scene-tail key phrase, anchors transition)

Note: Plan says scene starts at t=25s but actual narration moves from s01 tail ("freaking out about the bill" at ~22s) directly into "Here's the question" at 31.1s. There's a ~6s gap between s01 narration end and s02 narration start. Phase 4 should align the s01→s02 crossfade to land somewhere in this gap (e.g., crossfade fires at 28-29s) and let the s02 visual settle before the quote enters.

Retention picks:
  1. `gsap-typewriter` — at t=34.14s (when "Quote" is spoken) → reveal kicks off at t=35s — purpose: glyph-stagger reveal of the quote sentence "How would we build software in the future if tokens don't matter?" paced so each clause lands ~1s before the spoken anchor — source: GSAP effects (`gsap-typewriter`)
  2. `marker-highlight` — at t=37.55s (sweep starts on "tokens") — purpose: crab-red sweep under "tokens don't matter" — the term-branded concept (per plan story-lock) — source: marker primitives
  3. `spring-pop` — at t=41s — purpose: attribution chip "@steipete · OpenClaw · May 2026" + steipete avatar enters AFTER the quote settles, before the second-half narration continues — source: shared lib spring-pop analog
  4. Visual-pacing breath beat at t=46-50s — sub-line "tokens still feel scarce" (from narration) underline-marker — uses the 2nd allowed marker slot

Captions: `caption-fade-slide` synced word-level via captions sub-composition.

Visual-pacing audit:
  - Gaps: 25→31 (6s VIOLATION at scene open — fill with quote-card frame settling + steipete portrait fade-in placeholder before quote text fires), 31→35→37.5→41→46→50→55, max gap 5s
  - Fix: settle quote-card frame at t=25.5s (sub-composition fade-in animation), add overline "THE THESIS" entering at t=27s as a beat. Now 25.5→27→31→35→37.5→41→46→50→55 all ≤5s.

Step-by-step audit: N/A (single quote scene, not enumerated).

GSAP / motion notes:
  - Glyph-stagger per word in quote, `stagger: 0.05`, `back.out(1.4)` for soft snap
  - Marker-highlight sweep `width: 0 → 100%` over 0.6s, `power2.out`
  - SFX cues: `cinematic-whoosh` at t=24.6 (carryover from s01 transition), no SFX during quote reveal (let glyph-stagger carry texture), `spring-pop` at t=41 (attribution chip)

---

### Scene 03 — Use-case avalanche (data_start=55s, data_duration=35s)

Narration excerpt: "And to do that, his team runs roughly ten automations at once. Codex reviews every PR and every issue. A bot called clawsweeper hunts down old issues..."

Anchors (from `transcript.json` — 10 use-case word entry points):
  - Scene narration open: "And to do that" — idx=149, t=60.74s
  - Item 1 "Codex reviews every PR" — idx=161, t=65.18s
  - Item 2 "A bot called clawsweeper" — idx=168, t=67.95-69.29s (clawsweeper word at 68.60s)
  - Item 3 "Codex reviews every commit" — idx=182, t=73.44s (security holes)
  - Item 4 "de-duplicates issues" — idx=191, t=77.70s
  - Item 5 "cloud sandboxes" — idx=199, t=81.59s (record demos)
  - Item 6 "watches new issues" — idx=206, t=85.78s (drafts the PR)
  - Item 7 "polices spam" — idx=215, t=89.65s
  - Item 8 "performance regressions" — idx=220, t=91.81s (Discord)
  - Item 9 "team meetings" — idx=227, t=95.38s
  - Item 10 "clawpatch reviews everything" — idx=237, t=98.97s

Plan boundary note: Plan says s03 ends at t=90s, but the 10-item list narration actually runs to t=100.5s. Phase 4 should extend s03 to t=~101s OR have items 8-10 enter via a "fall-through" pattern that overlaps with the s04 midroll fade-in. Recommended: extend s03 to t=101s, shrink the buffer before s04 to ~9s of midroll. Either way: the 10 cards must enter at the actual transcript word starts above, NOT at synthetic ~3s intervals.

Retention picks:
  1. `gsap-stagger-grid` — at the 10 anchor times above — purpose: 10 use-case cards in a 2×5 grid enter one per spoken anchor (per `step-by-step-reveal.md` hidden-until-reveal pattern) — source: GSAP effects (`gsap-stagger-grid`)
  2. `pop` chip entrance per card — at each anchor — purpose: each card's mini-icon (review / sweep / security / cluster / sandbox / vision-PR / spam / perf / meeting / split) scale-pops as the card enters — source: shared lib `shared/lib/effects/stat-pill-pop.js` analog
  3. `gsap-counter-tween` — at t=61.5s — purpose: a top-right "Automations: 1 → 10" counter ticks up by one each time a card enters, visible reinforcement of the "ten automations" framing — source: GSAP effects (`gsap-counter-tween`)
  - NO markers (would clash with 10 simultaneous reveals — captions carry emphasis)

Captions: `caption-fade-slide` word-level — particularly important here since the narrator names each item.

Visual-pacing audit:
  - Gaps: 60.7→65.2→67.95→73.44→77.70→81.59→85.78→89.65→91.81→95.38→98.97
  - Max gap: 5.49s (item 2 → item 3, 67.95→73.44). Just over 5s. Add a sub-beat at t=71s: counter ticks (the "Automations: 2" → "Automations: 3" tick is the beat), plus a subtle scale-pulse on the freshly-entered card 2 lock-in.
  - All other gaps ≤ 4.3s. ✓

Step-by-step audit (REQUIRED per `step-by-step-reveal.md`):
  - Item 1 (Codex/PR): at t=65.18s
  - Item 2 (clawsweeper): at t=68.60s (anchor on the WORD "clawsweeper", not "A bot called")
  - Item 3 (Codex/security): at t=73.44s
  - Item 4 (de-duplicates): at t=77.70s
  - Item 5 (cloud sandboxes): at t=81.59s
  - Item 6 (watches new issues): at t=85.78s
  - Item 7 (polices spam): at t=89.65s
  - Item 8 (perf regressions): at t=91.81s
  - Item 9 (team meetings): at t=95.38s
  - Item 10 (clawpatch): at t=98.97s

GSAP / motion notes:
  - `tl.set` HIDDEN at t=0 for all 10 cards (per rule)
  - `tl.to` reveal at each anchor with `x: -40 → 0, opacity: 0 → 1, scale: 0.95 → 1, duration: 0.55, ease: back.out(1.5)`
  - Counter uses `roundProps` for integer animation
  - SFX cues: `pop` at each card anchor (vol 0.13, 10 instances — track-index 4, sequential no overlap), `cinematic-whoosh` at scene crossfade lead-in

---

### Scene 04 — HOSTINGER MIDROLL #1 (data_start=90s, data_duration=20s)

Narration excerpt: [SILENT in source script; host sponsor read intended per plan but NOT in current `transcript.json` — Phase 4 to reconcile]

Anchors: N/A (block carries its own visual timing per `shared/lib/blocks/hostinger-midroll/recipe.md`)

Retention picks:
  - **Block carries its own retention.** The `hostinger-midroll` block is BRAND-LOCKED — 5-phase mutex inside the block (intro / web-hosting / vps / ai-builder / cta + outro fade). No per-scene Phase-4-author primitives allowed (per `.claude/rules/sub-composition-wiring.md` + recipe Don'ts).
  - Mount selector: `#hostinger-midroll-1-mount`, `data-composition-id="hostinger-midroll"`, `data-track-index="20"`
  - Block has internal `blur-crossfade`-style fade-out at `DUR - 0.7s`

Captions: none (block is silent + sponsor narrator covers it).

Audio-reactive: none.

Transition out: block-internal fade-out. Root-level `blur-crossfade` from s04 to s05 fires at t=109.6s.

SFX cues: none mid-block (block doesn't include SFX; bg-music dips to 0.04 across 90-110 per plan music profile). `cinematic-whoosh` at t=109.6 for the s04→s05 crossfade.

---

### Scene 05 — clawsweeper deep-dive (data_start=110s, data_duration=60s)

Narration excerpt: "Okay, back to the fleet, and the first custom tool. It's called clawsweeper. Open source, MIT licensed, lives under the OpenClaw GitHub org..."

Anchors (from `transcript.json`):
  - "Okay back to the fleet" — idx=243, t=102.58s — NOTE: this is BEFORE s05's planned t=110 start. Plan boundary drift: actual narration for s05 begins at t=102.58s, not t=110. Phase 4 alignment options: (a) shift s05's data_start to 102.58s and shrink s04 to ~10s (NOT recommended — Hostinger block is fixed 20s); (b) hold s05 visuals frozen at t=110 even though narration started at 102.58 (creates 7s of narration leading silent visuals — BAD); (c) Phase 4 inserts 7-8s of sponsor-read narration into the audio file for s04 to push s05 content to its planned t=110 start. **Recommended: option (c).** Until that's fixed, the anchor times below are RELATIVE to the actual narration; absolute times are listed but Phase 4 must shift them by the s04 sponsor-read offset (estimated +7.4s) if option (c) is implemented.
  - "called claw-sweeper" — idx=170/171, t=68.60s — wait, this is the s03 use-case-list mention, NOT the s05 dedicated mention. The s05 NARRATION DOES NOT include a fresh "It's called clawsweeper" — the script says it but the TTS apparently rolled the script's repeated "claw-sweeper" into the s03 utterance. Phase 4 lint check: confirm s05 visual lockup ("clawsweeper" tool name slam) anchors to the s05-scene window word, which begins right after "fleet" at t=104.03s.
  - "Open source MIT" — idx=256, t=107.23s (anchor for badge entrance)
  - "OpenClaw GitHub" — idx=263, t=109.93s
  - "four lanes" — idx=305, t=123.91s (anchor for 4-lane diagram reveal)
  - Lane 1 "Review proposes closures" — idx=307, t=125.53s
  - Lane 2 "Apply executes" — idx=310, t=127.28s
  - Lane 3 "Repair runs autofix" — idx=316, t=130.36s
  - Lane 4 "Commit Review analyzes" — idx=324, t=134.82s
  - "In one reference week" — idx=338, t=140.99s (stat reveal anchor)
  - "three thousand four hundred" — idx=344, t=143.08s (the 3,478 number — spoken as "three thousand four hundred seventy-eight" probably; the transcript shows the spelled-out word form, so the stat is `gsap-counter-tween` end-anchored at t=145.03s)
  - "closed about four" — idx=351, t=147.84s
  - "zero point one percent" — idx=358, t=149.92-151.18s (the 0.1% reveal — HERO STAT)
  - "Which sounds tiny" — idx=364, t=152.79s
  - "never sleeps" — idx=371, t=154.95s
  - "Conservative by design" — idx=393, t=164.78s (scene-tail signal)

Retention picks:
  1. `gsap-stagger-grid` — at t=125.53s, 127.28s, 130.36s, 134.82s — purpose: 4 lane cards (Review / Apply / Repair / Commit Review) enter on each lane's spoken anchor — source: GSAP effects (`gsap-stagger-grid`)
  2. `gsap-counter-tween` — at t=142.5-145.0s — purpose: large stat tile counts `0 → 3,478` (issues scanned) anchored to "three thousand four hundred" word arc — source: GSAP effects (`gsap-counter-tween`)
  3. `gsap-counter-tween` — at t=147.8-148.7s — purpose: smaller adjacent tile counts `0 → 4` (closed) — same effect, second instance — source: GSAP effects
  4. `marker-circle` — at t=149.92s — purpose: hand-drawn ellipse around the `4 / 3,478` fraction the moment "zero point one percent" begins — source: marker primitives (`marker-circle`)
  5. `audio-reactive-glow` — at t=149.92-152.79s — purpose: SUBTLE treble-band glow on the `0.1%` mega-stat as it locks in (per §3 subtlety: 3-6% scale + soft `textShadow`) — source: audio-reactive (`audio-reactive-glow`)
  6. `gsap-stagger-grid` (tail) — at t=155-163s — purpose: 3 safety chips reveal one-per-narration-beat ("never closes maintainer items" / "never touches protected labels" / "re-fetches GitHub state before any change") — source: GSAP effects

Captions: `caption-fade-slide` word-level (60s scene with heavy named-entity content; captions essential for "clawsweeper" / "GitHub" / "3,478" pronunciation safety).

Visual-pacing audit:
  - Gaps: 102.6→107.2→110→123.9→125.5→127.3→130.4→134.8→140.99→143→147.8→149.9→152.8→155→160→164.8→170
  - Tightest segment of any scene — densest is the 4-lane entry sequence (125→134, every 2-4s). All sub-5s. ✓
  - Longest gap: 110→123.9 (13.9s VIOLATION). Add 3 sub-beats:
    - At t=112s: GitHub repo callout card enters (full settle by 113s, narration "first custom tool" land-anchor)
    - At t=116s: "MIT" badge `spring-pop`
    - At t=120s: "OpenClaw" wordmark badge underline-sweep (`marker-highlight` ← but this would push s05 to 3 markers, exceeding cap — drop the highlight, use scale-pulse on the badge instead)
  - Other long gap: 134.8→140.99 (6.2s VIOLATION) → add sub-beat at t=137.5s "stat-block frame" entrance (the empty stat slate slides in, ready to be filled by the counters at 142.5s)
  - Other long gap: 164.8→170 (5.2s — marginal) → 3rd safety chip enters at t=165, "Conservative by design" overline pulses at t=167. Sub-5s ✓

Step-by-step audit (per `step-by-step-reveal.md`): 4 lanes + 3 safety chips, ALL using `tl.set` hidden-until-reveal pattern.

GSAP / motion notes:
  - 4 lane cards: `tl.set` at t=0 (scene-internal) → `tl.to` at each anchor with `back.out(1.5)`
  - Big stat `gsap-counter-tween` uses `roundProps: "n"` over 2.5s, `power2.out`
  - 0.1% number gets `scale: 1 → 1.06 → 1` yoyo over 0.4s (subtle, single pulse) on top of glow
  - `audio-reactive-glow` per §3 sampling: `tl.call()` per frame inside reveal window
  - SFX cues: `pop` at each lane anchor (4 cues, track-index 4 sequential vol 0.13), `scale-slam` at t=145 (big number lock-in, vol 0.20), `impact-slam` at t=151.18 (the 0.1% reveal, vol 0.20), `cinematic-whoosh` at t=169.6 (scene crossfade)

---

### Scene 06 — crabbox.sh deep-dive (data_start=170s, data_duration=75s)

Narration excerpt: "But sweeping old issues is the easy part. The next tool is wild. It's called crabbox dot sh. Install with brew install openclaw slash tap slash crabbox..."

Anchors (from `transcript.json`):
  - "But sweeping old issues" — idx=396, t=166.23s (scene-open hook; pre-plan-boundary)
  - "next tool is wild" — idx=405, t=169.36s (the spectacle teaser)
  - "Its called crab-box" — idx=409, t=170.52s (tool name slam anchor)
  - "Install with brew" — idx=412, t=172.57s
  - "brew install" — idx=414, t=173.12s (typewriter trigger)
  - "short-lived box" — idx=433, t=181.27s (tagline anchor)
  - "Cloudflare Worker" — idx=465, t=195.37s (architecture diagram reveal)
  - "Backends include" — idx=490, t=205.87s
  - "Hetzner AWS and Azure" — idx=492, t=206.72-208.97s (brokered backends)
  - "E2B Daytona" — idx=501, t=210.55-211.86s (delegated backends)
  - "lease Linux macOS" — idx=512, t=216.44s (OS list)
  - "stream over VNC" — idx=528, t=222.79s (VNC frames anchor)
  - "use case that sent" — idx=535, t=225.46s (viral-use-case set-up)
  - "agent leases a fresh" — idx=543, t=228.45s
  - "fresh box" — idx=546, t=229.35s
  - "logs into Telegram" — idx=550, t=230.75s (THE moment)
  - "reproduces a bug" — idx=558, t=234.11s
  - "records the screen" — idx=561, t=235.23s
  - "pull request" — multiple occurrences; in s06 context likely around t=240-244 area (script says "posts the video as a comment on the pull request")

Retention picks:
  1. `gsap-typewriter` — at t=173.12s — purpose: monospace reveal of `brew install openclaw/tap/crabbox` char-by-char anchored to "brew install" word (per heteronym rule: TTS says "openclaw slash tap slash crabbox" — visual shows the literal `/` chars) — source: GSAP effects (`gsap-typewriter`)
  2. `gsap-path-draw` — at t=195.37-211.86s — purpose: SVG architecture diagram. Cloudflare Worker node enters at t=195.37s, then 7 backend lines (Hetzner / AWS / Azure brokered + E2B / Daytona / Blacksmith / Semaphore delegated) draw one-by-one paced to "Backends include" → "Hetzner AWS and Azure" → "E2B Daytona" anchors. Each `strokeDashoffset` animation 0.4s — source: GSAP effects (`gsap-path-draw`)
  3. `gsap-stagger-grid` — at t=216.44-223s — purpose: 3 OS-VNC frame mockups (macOS / Linux / Windows) enter side-by-side, paced to "Linux", "macOS", "Windows" word anchors (Linux at 217s; macOS at ~218s; Windows at ~219s) — source: GSAP effects
  4. `marker-highlight` — at t=199-200s (during "CLI on your laptop only carries a bearer token / remote machines never hold cloud credentials") — purpose: crab-red sweep under "never holds cloud credentials" (the security punchline) — source: marker primitives
  5. `spring-pop` — at t=228.45s — purpose: phone-mockup card for the Telegram-PR-video moment enters from below ("agent leases a fresh box") — source: shared lib spring-pop analog. Then internal phone-screen content reveals at t=230.75 (Telegram chat UI) — t=234.11 (bug screen) — t=235.23 (record indicator) — t=240+ (PR comment post)

Captions: `caption-fade-slide` — heavy named-entity scene (crabbox, Cloudflare, Hetzner, E2B, Daytona, Blacksmith, Semaphore, VNC, Telegram).

Visual-pacing audit:
  - Gaps: 170→172.6→173.1→181.3→195.4→205.9→206.7→210.55→216.4→222.8→225.5→228.5→230.8→234.1→235.2→240
  - Longest: 173.1→181.3 (8.2s VIOLATION). Add sub-beat at t=177s: tagline "a short-lived box for every run" fade-in card.
  - Other long: 181.3→195.4 (14.1s VIOLATION). Add 2 sub-beats: t=185s ("Lease a machine, sync your code, run the task" word-pop reveal sequence as 4-step pictogram), t=190s ("release the machine" punchline card fade)
  - Other long: 211.86→216.4 (4.5s ✓), 222.8→225.5 (2.7s ✓), 235.2→240 (4.8s ✓)
  - Final long: scene-end gap 240→245 (5s ✓ marginal). Hold the phone-mockup card with "PR comment posted" badge.

Step-by-step audit: 7 backend lines + 3 OS frames + 4 phone-internal phases ALL `tl.set` hidden-until-reveal.

GSAP / motion notes:
  - Typewriter uses `text` plugin with `power1.in` ease, ~30ms per char
  - Path-draw uses `strokeDashoffset: total → 0` with `stagger` between paths (7 paths, ~1.5s apart)
  - Phone-mockup uses `back.out(1.7)` entrance, then phone-internal scenes mutex-swap on track-9 (so prior phone-screen content fades as new one enters)
  - SFX cues: `cinematic-whoosh` at t=169.6 (carryover s05→s06), `pop` at t=173.12 (typewriter start, vol 0.13), `pop` per path-draw (7 cues at backend reveals, track 4 sequential), `pop` per OS frame (3 cues), `spring-pop` at t=228.45 (phone-mockup card, vol 0.15), `cinematic-whoosh` at t=244.6 (s06→s07 crossfade)

---

### Scene 07 — clawpatch.ai deep-dive (data_start=245s, data_duration=55s)

Narration excerpt: "So the sandbox runs the demo. The third tool reviews the code. It's called clawpatch dot ai. Same pattern. Open source, MIT, made by the OpenClaw team..."

Anchors:
  - "So the sandbox runs" — idx=596, t=246.55s
  - "third tool reviews" — idx=603, t=248.60s
  - "claw-patch dot A I" — idx=610, t=251.56s (tool name slam)
  - "Open source MIT made" — idx=616, t=254.66s
  - "trick is how" — idx=625, t=258.29s
  - "semantic units first" — idx=650, t=267.57s (KEY phrase — term-brand)
  - "Routes for Next" — idx=653, t=269.77s (unit 1)
  - "Commands for npm" — idx=659, t=271.53s (unit 2)
  - "Packages CLI" — idx=668, t=275.53s (units 3+4 — paired in narration)
  - "Tests" — idx=671, t=277.36s (unit 5)
  - "Each unit gets" — idx=672, t=278.25s
  - "findings come back" — idx=695, t=287.37s
  - "Bug security performance" — idx=699, t=289.45-291.39s (findings categories)
  - "severity and a confidence" — idx=712, t=296.25s
  - "markdown report" — idx=728, t=302.28s (tail anchor)
  - "JSON report" — idx=732, t=303.34s (tail anchor)

Plan boundary note: s07 ends at t=300 per plan, but tail content runs to t=304+. Same midroll-narration-missing pattern as s05. Phase 4 to insert ~4-5s of s08 sponsor-read narration to align.

Retention picks:
  1. `gsap-stagger-grid` — at t=269.77s, 271.53s, 275.53s, 275.9s, 277.36s — purpose: 5 semantic-unit cards (Routes / Commands / Packages / CLI / Tests) enter ONE PER spoken anchor. Packages and CLI are tightly paired in narration (275.53s and 275.9s estimated) — small stagger is OK there — source: GSAP effects (`gsap-stagger-grid`)
  2. `marker-highlight` — at t=267.57s — purpose: crab-red sweep under "semantic units" the moment the term is coined (term-brand story-lock per plan §Story Lock Placement) — source: marker primitives
  3. `gsap-stagger-grid` — at t=289.45-296.25s — purpose: 6 findings cards (Bug / Security / Performance / Docs gap / Test gap / Maintainability) enter as the narrator names them, each with a severity + confidence chip — source: GSAP effects
  4. `gsap-stagger-grid` — at t=302.28-304s — purpose: 2 output chips (markdown report / JSON report) enter at the spoken anchors — source: GSAP effects

Captions: `caption-fade-slide` — heavy on technical terms (Next.js, npm, semantic units, severity).

Visual-pacing audit:
  - Gaps: 246.6→248.6→251.6→254.7→258.3→267.6→269.8→271.5→275.5→277.4→278.3→287.4→289.5→291.4→296.3→302.3→303.3
  - Longest: 258.3→267.6 (9.3s VIOLATION). Add 2 sub-beats: t=261s ("Most AI code review tools see one giant codebase" placeholder schematic appears — single block labeled "monolithic"), t=264s ("and choke" — `marker-scribble` over the monolithic block — BUT this exceeds 2-marker cap, so use scale-pulse pulse instead). Net: t=261s and t=264s have foreground entrance beats. ✓
  - Other long: 278.3→287.4 (9.1s VIOLATION). Add 2 sub-beats: t=282s (per-unit detail line "entrypoints, owned files, context files" reveals as a sub-line under the 5-unit grid), t=285s (a "Then the review runs per unit, not per file" emphasis pop on the per-unit grid). ✓
  - All other gaps ≤ 4s. ✓

Step-by-step audit: 5 semantic units + 6 findings cards = 11 staggered reveals total. ALL `tl.set` hidden-until-reveal.

GSAP / motion notes:
  - Semantic units use color rotation per the crab palette (Routes = crab-red, Commands = cyan, Packages = paper-white, CLI = warn-amber, Tests = ok-green)
  - Findings cards include severity-chip color per severity (red high / amber med / yellow low) — DO NOT animate the severity chip independently (would push marker count over)
  - SFX cues: `cinematic-whoosh` at t=244.6 (carryover), `pop` per unit reveal (5 cues, track 4 sequential), `pop` per findings reveal (6 cues, track 4 sequential), `cinematic-whoosh` at t=299.6 (s07→s08 crossfade)

---

### Scene 08 — HOSTINGER MIDROLL #2 (data_start=300s, data_duration=20s)

Same as Scene 04. Block carries its own retention. Mount selector `#hostinger-midroll-2-mount`, `data-track-index="20"`. SFX: `cinematic-whoosh` at t=319.6 for the s08→s09 crossfade.

Phase 4 reconciliation note: same as s05/s07. The sponsor-read narration for s08 is missing from `transcript.json` — Phase 4 must inject narration for s08 to align s09 narration's actual start (t=306.82s per "Back in and") to plan's s09 data_start=320s. Estimated injection: ~13s of sponsor-read narration into s08.

---

### Scene 09 — Fleet recap (data_start=320s, data_duration=35s)

Narration excerpt: "Back in, and here's how all of it stacks together. Clawsweeper at the top, closing the dead issues. Crabbox in the middle..."

Anchors:
  - "Back in and" — idx=740, t=306.82s (scene-open; PRE-plan-boundary by 13.2s; reconciliation note above)
  - "Claw-sweeper at the top" — idx=750, t=310.98s (layer 1)
  - "Crab-box in the middle" — idx=758, t=314.54s (layer 2)
  - "Claw-patch underneath" — idx=769, t=318.64s (layer 3)
  - "Codex sitting across" — idx=777, t=323.13s (layer 4 — cross-cutting)
  - "Vercel's deep-sec" — idx=788, t=327.68s (layer 5)
  - "two weeks before" — idx=791, t=329.30s (the deepsec timing receipt)
  - "Thats it" — idx=809, t=338.41s (recap-tail beat)
  - "Three thin well-scoped" — idx=815, t=341.38s (TAKEAWAY)
  - "Composable not magical" — idx=823, t=345.47s (final beat)

Retention picks:
  1. `gsap-stagger-grid` — at t=310.98s, 314.54s, 318.64s, 323.13s, 327.68s — purpose: 5 horizontal architecture layers (clawsweeper / crabbox / clawpatch / codex / deepsec) enter top-down on each layer's spoken anchor — source: GSAP effects (`gsap-stagger-grid`)
  2. `gsap-path-draw` — at t=329-333s — purpose: SVG bracket on the right of the stack draws + label "the ~100-agent fleet" enters as text at the bracket midpoint — source: GSAP effects (`gsap-path-draw`)
  3. `marker-highlight` — at t=341.38s — purpose: crab-red sweep under "three thin, well-scoped tools" — the takeaway phrase — source: marker primitives

Captions: `caption-fade-slide`.

Visual-pacing audit:
  - Gaps: 306.8→311→314.5→318.6→323.1→327.7→329→338.4→341.4→345.5
  - Longest: 329→338.4 (9.4s VIOLATION). Add 2 sub-beats: t=332s (small chip with "released 2 weeks before this post" anchored to deepsec layer), t=335s ("Codex configured for security" sub-line underneath layer 4 enters)
  - All other gaps ≤ 4.5s. ✓

Step-by-step audit: 5 layers all `tl.set` hidden-until-reveal.

GSAP / motion notes:
  - Each layer is a horizontal strip with accent stripe + tool wordmark + 1-line role descriptor
  - Layers enter with `y: -20 → 0, opacity: 0 → 1, duration: 0.5, ease: back.out(1.4)`
  - Bracket path-draw uses `strokeDashoffset` 0.8s + label fade-in 0.4s
  - SFX cues: `pop` per layer (5 cues, track 4 sequential, vol 0.13), `cinematic-whoosh` at t=354.6 (s09→s10 crossfade)

---

### Scene 10 — Community split — 5 camps (data_start=355s, data_duration=105s)

Narration excerpt: "Which is why the reaction split into roughly five camps. Camp one is the dry skeptics. Steipete called the operation 'extremely lean.'..."

Anchors:
  - Scene open: "Which is why the" — idx=826, t=347.14s (pre-plan-boundary by 8s — same drift pattern)
  - "roughly five camps" — idx=833, t=348.78s (the framing slam)
  - **Camp 1** "Camp one is the dry" — idx=836, t=350.87s
    - sub-anchor "extremely lean" — t=354.67s
    - sub-anchor "pushback is wry" — t=364.22s
    - sub-anchor "dictionary needs an update" — t=366.61s
  - **Camp 2** narration: Plan boundary said 18s apart; actual ~370s for "Camp two" (NOT FOUND verbatim — see transcript context idx 879 region "ahead-looking" / "forward")
    - sub-anchor "eighteen to thirty-six" — t=378.64s
    - sub-anchor "Steipete agreed with this" — t=383.83s
  - **Camp 3** "Camp three is the cost" — idx=923, t=386.75s
    - sub-anchor "Cerebras" — t=392.59s
    - sub-anchor "Grok Qwen" — t=393.33s
  - **Camp 4** "Camp four is admiring" — idx=974, t=407.74s
    - sub-anchor "narrow my thinking" — t=414.19s
  - **Camp 5** "camp five smallest" — idx=1010, t=421.22s
    - sub-anchor "cant parse the stack" — t=434.78s
  - Tail "If you've ever scrolled" — idx=1049, t=436.94s
  - Closing "which camp is yours" — idx=1070, t=443.04s
  - Final "next part matters" — idx=1093, t=451.18s

Retention picks:
  1. `gsap-stagger-grid` — at t=350.87s, ~370s, 386.75s, 407.74s, 421.22s — purpose: 5 bucket cards enter ONE PER CAMP, ~18s apart (105s scene / 5 cards = 21s nominal spacing; actual narration drives spacing 19s / 16s / 21s / 14s). `tl.set` hidden-until-reveal pattern — source: GSAP effects
  2. Per-card sub-beats (`gsap-typewriter` or `pop`) — at each card's sub-anchor (extremely lean / eighteen to thirty-six / Cerebras / narrow my thinking / cant parse the stack) — purpose: a typewriter sub-quote anchored to the camp's punchline mid-narration; satisfies `visual-pacing-5s.md` inside the long phase — source: GSAP effects (`gsap-typewriter`) + shared lib `shared/lib/effects/stat-pill-pop.js`
  3. `marker-highlight` — at t=354.67s — purpose: crab-red sweep under "extremely lean" (the snarky-quote moment, anchors camp 1's tagline) — source: marker primitives
  4. `marker-highlight` — at t=476.11s — NO wait this is s11. Drop this. Use second `marker-highlight` at t=434.78s — sweep under "what am I looking at" type phrase or under "cant parse the stack" (camp 5's punchline) — source: marker primitives. CAP CHECK: 2 markers in scene ✓

Captions: `caption-fade-slide` (long scene with dense paraphrased content).

Visual-pacing audit:
  - With ONLY 5 card entrances at 21s spacing → enormous violation. The plan calls this out and pre-prescribes "per-card sub-beats every ~4s (icon scale-pulse, quote-line typewriter)".
  - Per-card sub-beats inside camp 1 (entrance at 350.87, next camp at ~370):
    - t=351 card 1 enters
    - t=355 typewriter "extremely lean" sub-quote
    - t=360 icon scale-pulse on camp 1 mini-icon
    - t=364 marker-sweep under "wry" or sub-quote second half
    - t=367 sub-line "the dictionary needs an update" entrance
    - t=370 camp 2 enters → camp 1 mutex-fade-to-half (visually de-emphasize, don't remove)
  - Apply same pattern to camps 2-5: 4-5 sub-beats per camp window. Total scene beats: ~25 (5 entrances + ~4 sub-beats × 5).
  - All gaps stay ≤ 5s. ✓
  - Tail-hold from t=445 to t=460 (scene exit) — needs a beat: at t=448s, all 5 cards fade-up to equal opacity (the "now hold them all" composite), at t=452s overline "Notice none of them are the camp the post is arguing for" enters. ✓

Step-by-step audit (REQUIRED): 5 buckets ALL `tl.set` hidden-until-reveal, paced ~18-21s apart.

GSAP / motion notes:
  - Each bucket card uses crab-red bucket-label header + paper-white body + cyan accent chip for the camp's quote-fragment
  - Cards enter from below with `y: 40 → 0, opacity: 0 → 1, scale: 0.96 → 1, duration: 0.6, ease: back.out(1.3)`
  - Active card has full opacity; previously-entered cards fade to opacity 0.55 (mutex-prominence, not mutex-visibility)
  - Sub-quote typewriters use `text` plugin, paced char-by-char to the spoken narration sub-anchor
  - SFX cues: `pop` per camp entrance (5 cues spread across 105s; track 4 reused, no overlap), `pop` per sub-beat icon-pulse (up to 4 per camp = ~16 small pops, track 5, vol 0.13), `cinematic-whoosh` at t=459.6 (s10→s11 crossfade)

---

### Scene 11 — Cost twist (data_start=460s, data_duration=35s)

Narration excerpt: "And then steipete dropped the line that re-frames everything. When the cost-optimization camp pushed him on cheaper models and deterministic hooks, his reply was four words long. Quote. I could just disable fast mode and cut it down by 70%..."

Anchors:
  - "And then steipete dropped" — idx=1096, t=453.04s (scene-open; PRE-plan-boundary by 7s)
  - "line that re-frames" — idx=1101, t=454.33s
  - "When the cost-optimization" — idx=1105, t=456.83s
  - "reply was four words" — idx=1118, t=461.75s
  - "I could just disable" — idx=1124, t=465.28s (quote anchor; the four-word reply visual moment)
  - "disable fast mode" — idx=1127, t=465.89s
  - "Fast mode is OpenAI" — idx=1137, t=469.57s (definition entrance)
  - "deliberate choice" — idx=1167, t=480.96s
  - "Its not cost" — idx=1170, t=481.99s
  - "Its latency" — idx=1173, t=483.75s (THE REVEAL — primary loop resolution)
  - "real-time" — idx=1188, t=488.22s (scene-tail key word)

Note: "70" not found as standalone word; transcript likely shows "70%" with punctuation. Phase 4 check: search transcript words for "70%" with normalization tolerating "%". Approximate position: idx=1130-1132, t=~467s.

Retention picks:
  1. `gsap-typewriter` — at t=465.28s — purpose: glyph-stagger reveal of the quote "I could just disable fast mode and cut it down by 70%" — quote-card with the 4 words spotlighted ("disable fast mode" word-pop emphasized) — source: GSAP effects (`gsap-typewriter`)
  2. `gsap-counter-tween` — at t=466.5-467.5s — purpose: scale-pulse on the `70%` numeral; brief yoyo `scale: 1 → 1.06 → 1` (per `step-by-step-reveal.md` decorations-aren't-beats rule, but combined with the typewriter entrance this IS the beat) — source: GSAP effects (`gsap-counter-tween`) — note: not really a counter, more a stat-emphasis; use `gsap-stagger-grid` style scale-pop with `gsap-counter-tween` if number really ticks 0→70
  3. `marker-highlight` — at t=483.75s — purpose: crab-red sweep under "It's not cost. It's latency." — primary-loop RESOLUTION (per plan story-lock) — source: marker primitives
  4. `spring-pop` — at t=488.22s — purpose: Codex Speed docs URL chip enters from below (the receipt for "fast mode" claim) — source: shared lib spring-pop analog

Captions: `caption-fade-slide` — quote moment + technical aside; captions reinforce the 70% number visually.

Visual-pacing audit:
  - Gaps: 453→454.3→456.8→461.8→465.3→465.9→469.6→481→482→483.8→488.2→495
  - Longest: 469.6→481 (11.4s VIOLATION). Add 2 sub-beats: t=473s ("1.5x speed tier" callout chip enters), t=477s ("higher credits in exchange for lower latency" mini-fact line enters)
  - Other: 488.2→495 (6.8s VIOLATION). Add sub-beat at t=491s: "paying 70% more to stay real-time" punchline line enters under the quote-card. ✓
  - All other gaps ≤ 4s. ✓

Step-by-step audit: 1 quote + 3 sub-content pieces. `tl.set` for the quote and the latency punchline.

GSAP / motion notes:
  - Quote-card is full-bleed with the 4 words at 100px Inter Display weight 900
  - The numeral "70%" gets `--accent-stat` warm yellow color emphasis
  - Latency punchline at 84px weight 800
  - SFX cues: `cinematic-whoosh` at t=459.6 (carryover s10→s11), `impact-slam` at t=465.28 (quote anchor, vol 0.20), `glitch-zap` at t=483.75 (the "It's latency" reveal — pivot/contrarian moment, vol 0.12), `spring-pop` at t=488.22 (URL chip, vol 0.15), `cinematic-whoosh` at t=494.6 (s11→s12 crossfade)

---

### Scene 12 — Support pillar (data_start=495s, data_duration=15s)

Narration excerpt: "If this was useful, drop a like, subscribe, hit the bell. It's the cheapest way to support the channel and tell YouTube to send this to more devs. Now back to the question that actually matters."

Anchors:
  - "If this was useful" — idx=1189, t=489.79s (PRE-plan-boundary by 5.2s)
  - "drop a like" — idx=1193, t=490.97s (subscribe trigger)
  - "hit the bell" — idx=1197, t=492.47s (bell trigger)
  - "cheapest way to support" — idx=1202, t=494.28s (KEY phrase for marker)
  - "tell YouTube" — idx=1209, t=496.47s
  - "back to the question" — idx=1218, t=499.05s (scene-tail handoff signal)

Retention picks:
  1. `gsap-stagger-grid` — at t=490.97s (like), 491.5s (subscribe), 492.47s (bell) — purpose: 3 icons enter 0.5s apart paced to the spoken anchor words (the narration says them in different order than the plan; align to actual order: "like" → "subscribe" → "bell") — source: GSAP effects (`gsap-stagger-grid`)
  2. `spring-pop` per icon — at each anchor — purpose: each icon scale-pops in with `back.out(1.7)` — source: shared lib spring-pop analog
  3. `marker-highlight` — at t=494.28s — purpose: crab-red sweep under "cheapest way to support the channel" — source: marker primitives

Captions: none — 15s scene, narrator delivers tight, captions would compete.

Audio-reactive: none.

Visual-pacing audit:
  - Gaps: 491→491.5→492.5→494.3→496.5→499→510
  - Longest: 499→510 (11s VIOLATION). The narration tail "Now back to the question that actually matters" lands at ~499s and the scene exits at 510. Add 2 sub-beats: t=502s (overline "back to the question" entrance + crab-red brand chrome strengthen), t=506s (the icon triad does a subtle bounce-yoyo as final "press it" emphasis before the s13 crossfade fires at 509.6s)
  - All other gaps ≤ 2s. ✓

Step-by-step audit: 3 icons reveal at narration word starts (per `step-by-step-reveal.md`).

GSAP / motion notes:
  - Icons are SVG, each ~80px square in deep crab-red
  - "press it" emphasis is a `scale: 1 → 1.04 → 1` yoyo, 0.3s, no glow
  - Visually LIGHTER than Hostinger midroll (per plan §s12 design_notes) — smaller scale, no Werbung badge, no product cards
  - SFX cues: `pop` per icon (3 cues, track 4 sequential, vol 0.13), `cinematic-whoosh` at t=509.6 (s12→s13 crossfade)

---

### Scene 13 — Engagement CTA + held-still final frame (data_start=510s, data_duration=30s)

Narration excerpt: "So here's the debate. The whole fleet runs on the assumption that tokens don't matter. The most polarizing piece of it is that demo workflow. An AI agent leasing a fresh machine, logging into your Telegram, recording a video, and posting it on a pull request. So here's the question. Would you let an AI agent log into your Telegram to make a PR demo? Yes, no, or hell no — drop your verdict."

Anchors:
  - "So heres the debate" — idx=1225, t=502.24s (scene-open; PRE-plan-boundary by 7.8s)
  - "whole fleet runs on" — idx=1230, t=503.69s
  - "tokens dont matter" — NOT s13-local; s13 uses "tokens don't matter" callback but transcript matched s02 instance. Phase 4 to verify the second instance exists in s13 narration text and find its actual t.
  - "most polarizing piece" — idx=1241, t=507.86s
  - "demo workflow" — idx=1248, t=509.60s
  - "AI agent leasing" — idx=1251, t=511.50s
  - "fresh machine" — idx=1255, t=512.65s
  - "logging into your Telegram" — idx=1257, t=513.62s (THE setup)
  - "So heres the question" — idx=1271, t=519.01s (the question lead-in)
  - "Would you let" — idx=1275, t=520.25s
  - "let an AI agent" — idx=1277, t=520.60s
  - "into your Telegram" — idx=1258, t=513.98s (earlier instance) — for the question itself, find next occurrence after idx=1275; given the question's structure, "into your Telegram" in the question is at t~=522.0s (right before "to make a PR demo")
  - "PR demo" — idx=1288, t=523.38s
  - "Yes no or hell" — idx=1290, t=524.95s (Yes/No/Hell No chips trigger)
  - "drop your verdict" — idx=1295, t=526.17s (final spoken)
  - Last word `verdict.` — idx=1297, t=527.01s

Plan note: Plan reserves t=535-540 for held-still terminal hold. Actual narration ends at 527.01s, so the held-still window naturally is 527→540 (13s, vs plan's 5s). This is actually BETTER for thumbnail-grade frame purpose — longer freeze = stronger thumbnail.

Retention picks:
  1. `gsap-typewriter` — at t=519.01s — purpose: the on-screen `#cta-question` element types out "Would you let an AI agent log into your Telegram to make a PR demo?" paced to the spoken question (520.25 → 524s). The question text PERSISTS through the held-still final frame — source: GSAP effects (`gsap-typewriter`)
  2. `gsap-stagger-grid` — at t=524.95s, 525.34s, 525.78s — purpose: 3 verdict chips (Yes / No / Hell No) enter aligned to "Yes," / "no," / "hell no." spoken words — source: GSAP effects (`gsap-stagger-grid`)
  3. `marker-circle` — at t=519.5s — purpose: hand-drawn ellipse around the entire debate question OR around "Telegram" specifically (the spicy word) — source: marker primitives (`marker-circle`)
  4. `audio-reactive-glow` — at t=510-525s only — purpose: SUBTLE treble-band glow on the persistent subscribe pill in the corner; CUTS at t=525s for the held-still freeze — source: audio-reactive (`audio-reactive-glow`)
  5. Final-frame freeze — at t=527s onward — purpose: ALL animation finishes by t=527s. From t=527 to t=540, the composition is COMPLETELY STATIC (no scale yoyos, no glow pulses, no marker sweeps — per plan §13 thumbnail-grade frame check). All 5 thumbnail-grade elements visible: dominant topic ("100 AGENTS. ONE DEV." 160px crab-red), visual anchor (small claw-mark + ghost tweet), brand chrome (OpenClaw + channel mark), outcome receipt ("3 OSS tools + Codex + deepsec = the fleet"), debate question (the `#cta-question` element persists)

Captions: `caption-fade-slide` — cuts at t=525s; the final 13s are caption-free (held-still frame).

Visual-pacing audit:
  - Gaps: 510→511.5→513.6→519→520.3→524.95→527→540 (last is intentional freeze; rule explicitly relaxed for thumbnail-grade hold)
  - Longest gap inside active period: 513.6→519 (5.4s — marginal VIOLATION). Add sub-beat at t=516s: "polarizing" word emphasis (scale-pulse on "polarizing" inside the narration-overlay caption-fade-slide animation; or, since captions are running, a `pop` icon entrance on a Telegram silhouette adjacent to the question setup)
  - All other gaps ≤ 4s. ✓
  - Held-still 527→540: 13s freeze. RULE EXPLICITLY RELAXED per `shorts-thumbnail-frames.md` adapted-for-long-form spirit (per plan §13). NO motion pick during this window.

Step-by-step audit: 3 verdict chips at narration word anchors. Question typewriter at narration anchor. ✓ All `tl.set` hidden-until-reveal.

GSAP / motion notes:
  - `#cta-question` element types out over ~3.5s (Yes ease)
  - 3 verdict chips enter with `back.out(1.5)`, 0.35s each
  - Subscribe pill audio-reactive-glow uses treble band, subtle 3-5% scale + soft `textShadow`
  - ALL animations END by t=527s — no `repeat: -1`, no trailing easing
  - SFX cues: `cinematic-whoosh` at t=509.6 (carryover s12→s13), `pop` at t=519 (question entrance, vol 0.13), `pop` per verdict chip (3 cues at 524.95 / 525.34 / 525.78, track 4 sequential vol 0.13), NO SFX 527→540 (silence reinforces freeze)

---

## Picks Cross-Reference (validate against menu)

| Pick name | Source file in retention-components-hyperframes.md | Confirmed valid? |
|---|---|---|
| `marker-highlight` | §1 Marker Highlights | ✓ |
| `marker-circle` | §1 Marker Highlights | ✓ |
| `caption-fade-slide` | §2 Caption Patterns | ✓ |
| `audio-reactive-glow` | §3 Audio-Reactive | ✓ |
| `blur-crossfade` | §4 Scene Transitions | ✓ |
| `gsap-typewriter` | §5 GSAP Effects | ✓ |
| `gsap-counter-tween` | §5 GSAP Effects | ✓ |
| `gsap-stagger-grid` | §5 GSAP Effects | ✓ |
| `gsap-path-draw` | §5 GSAP Effects | ✓ |
| `sub-composition` | §6 Composition Structure | ✓ |
| `hero-slam` | §7 Retention Pattern Library | ✓ (pattern) |
| `stat-pill-row` | §7 Retention Pattern Library | ✓ (pattern) |
| `timeline-cards` | §7 Retention Pattern Library | ✓ (pattern) |
| `narrated-stat-reveal` | §7 Retention Pattern Library | ✓ (pattern) |
| `cta-url-slam` | §7 Retention Pattern Library | ✓ (pattern) |

Shared/lib additions referenced (per `shared/lib/MANIFEST.md`):
| Pick | Path | Type |
|---|---|---|
| `magnet-snap-letters` (s01 slam 3) | `shared/lib/components/magnet-snap-letters/` | component |
| `hero-slam-shake.js` (s01 slams 1+2) | `shared/lib/effects/hero-slam-shake.js` | effect |
| `stat-pill-pop.js` analog (per-card pop) | `shared/lib/effects/stat-pill-pop.js` | effect |
| `spring-pop` (chips/cards) | `shared/lib/components/` (analog via GSAP `back.out(1.7)`) | inline pattern |
| `hostinger-midroll` (s04, s08) | `shared/lib/blocks/hostinger-midroll/block.html` | block (copy-from) |

Registry additions referenced (catalog at `.claude/rules/registry-blocks-catalog.md`):
**None.** This composition uses only project-local primitives + shared/lib items. No `npx hyperframes add <name>` invocations required for Phase 4. (The plan explicitly chose NOT to use any registry html-in-canvas blocks for this 9-min explainer — render cost too high, palette balance issues with crab-red.)

## SFX Cues — Summary (per `.claude/rules/audio-design.md`)

All cues sourced from `shared/audio/MANIFEST.md`. Per-cue volume ≤ 0.25 (the rule cap); `sonic-logo` at 0.60 is the documented exception. Track assignments below avoid overlap per the alignment rule.

| Cue | Where (scene + word anchor) | data-start | duration | track | volume |
|---|---|---|---|---|---|
| sonic-logo | s01 cold open | 0.0 | 1.52 | 3 | 0.60 |
| impact-slam | s01 slam 1 "One developer" | 0.04 | 0.63 | 4 | 0.20 |
| scale-slam | s01 slam 2 "A hundred" | 1.00 | 0.73 | 4 | 0.20 |
| impact-slam | s01 slam 3 "Zero" | 5.17 | 0.63 | 4 | 0.20 |
| screen-shake | s01 slam 3 (LAYERED) | 5.17 | 0.52 | 5 | 0.15 |
| spring-pop | s01 tweet card | 14.5 | 0.52 | 4 | 0.15 |
| cinematic-whoosh | s01→s02 crossfade | 24.6 | 0.84 | 3 | 0.15 |
| spring-pop | s02 attribution chip | 41.0 | 0.52 | 4 | 0.15 |
| cinematic-whoosh | s02→s03 crossfade | 54.6 | 0.84 | 3 | 0.15 |
| pop × 10 | s03 each card | per anchor (65.18, 68.60, 73.44, 77.70, 81.59, 85.78, 89.65, 91.81, 95.38, 98.97) | 0.52 | 4 | 0.13 |
| cinematic-whoosh | s03→s04 crossfade | 89.6 | 0.84 | 3 | 0.15 |
| cinematic-whoosh | s04→s05 crossfade | 109.6 | 0.84 | 3 | 0.15 |
| pop × 4 | s05 each lane | 125.53, 127.28, 130.36, 134.82 | 0.52 | 4 | 0.13 |
| scale-slam | s05 big number lock-in | 145.0 | 0.73 | 4 | 0.20 |
| impact-slam | s05 0.1% reveal | 151.18 | 0.63 | 4 | 0.20 |
| cinematic-whoosh | s05→s06 crossfade | 169.6 | 0.84 | 3 | 0.15 |
| pop | s06 typewriter start | 173.12 | 0.52 | 4 | 0.13 |
| pop × 7 | s06 backend paths | distributed 205.87-211.86 | 0.52 | 4 | 0.13 |
| pop × 3 | s06 OS frames | 216.44-222.79 | 0.52 | 4 | 0.13 |
| spring-pop | s06 phone-mockup | 228.45 | 0.52 | 4 | 0.15 |
| cinematic-whoosh | s06→s07 crossfade | 244.6 | 0.84 | 3 | 0.15 |
| pop × 5 | s07 semantic units | 269.77-277.36 | 0.52 | 4 | 0.13 |
| pop × 6 | s07 findings cards | 289.45-296.25 | 0.52 | 4 | 0.13 |
| cinematic-whoosh | s07→s08 crossfade | 299.6 | 0.84 | 3 | 0.15 |
| cinematic-whoosh | s08→s09 crossfade | 319.6 | 0.84 | 3 | 0.15 |
| pop × 5 | s09 fleet layers | 310.98-327.68 | 0.52 | 4 | 0.13 |
| cinematic-whoosh | s09→s10 crossfade | 354.6 | 0.84 | 3 | 0.15 |
| pop × 5 | s10 camp entrances | ~350.87, ~370, 386.75, 407.74, 421.22 | 0.52 | 4 | 0.13 |
| pop × ~16 | s10 sub-beat icon pulses | distributed across 105s | 0.52 | 5 | 0.13 |
| cinematic-whoosh | s10→s11 crossfade | 459.6 | 0.84 | 3 | 0.15 |
| impact-slam | s11 quote anchor | 465.28 | 0.63 | 4 | 0.20 |
| glitch-zap | s11 "It's latency" pivot | 483.75 | 0.52 | 4 | 0.12 |
| spring-pop | s11 URL chip | 488.22 | 0.52 | 4 | 0.15 |
| cinematic-whoosh | s11→s12 crossfade | 494.6 | 0.84 | 3 | 0.15 |
| pop × 3 | s12 icons | 490.97, 491.5, 492.47 | 0.52 | 4 | 0.13 |
| cinematic-whoosh | s12→s13 crossfade | 509.6 | 0.84 | 3 | 0.15 |
| pop | s13 question entrance | 519.0 | 0.52 | 4 | 0.13 |
| pop × 3 | s13 verdict chips | 524.95, 525.34, 525.78 | 0.52 | 4 | 0.13 |
| (silence) | s13 held-still freeze | 527-540 | — | — | — |

Per-cue concurrency check: max 2 cues concurrent at any moment (s01 slam 3 layers `impact-slam` track 4 + `screen-shake` track 5). All other cues are sequential. ✓

---

## Total picks summary

- **Markers (sweep / circle / scribble)**: 9 — s01×1 (highlight ZERO + 2nd at "freaking out" = 2), s02×2 (highlight "tokens" + tail), s05×1 (circle on stat), s06×1 (highlight "credentials"), s07×1 (highlight "semantic units"), s09×1 (highlight "three thin"), s10×2 (highlight "lean" + "cant parse"), s11×1 (highlight "latency"), s12×1 (highlight "cheapest"), s13×1 (circle on question). Re-tallying scenes (cap = 2/scene): all within cap. ≈11 total markers across composition.
- **Captions / text-reveals**: 1 `caption-fade-slide` pattern applied to 10 active scenes (excluding s04, s08 silent midrolls and s12 narrator-only) = 10 scenes captioned.
- **Audio-reactive**: 2 instances (s05 subtle glow on 0.1% stat; s13 subtle glow on subscribe pill, cuts at 525s). Both `audio-reactive-glow` only — no banned vocab.
- **Sub-comp blocks (registry)**: 0 — composition uses only project-local + shared/lib.
- **Sub-comp blocks (shared/lib)**: 1 unique block × 2 mounts — `hostinger-midroll` (s04, s08).
- **Shared/lib components referenced**: 3 — `magnet-snap-letters` (s01 pivot slam), `spring-pop` analog (s01, s02, s06, s11, s12), inline GSAP equivalents.
- **Shared/lib effects referenced**: 2 — `hero-slam-shake.js` (s01), `stat-pill-pop.js` analog (s03, s05, s07, s09, s10, s12).
- **Shader transitions**: 0 — composition uses pure CSS `blur-crossfade` at all 12 scene boundaries (calm news-explainer voice).
- **GSAP custom timelines**: 13 (one per scene sub-composition) + 1 root orchestration timeline = 14 paused timelines registered on `window.__timelines`.

**GSAP effects (`gsap-*`) total instances**:
- `gsap-stagger-grid`: 16 (s01 stack, s03 10-card grid, s05 lanes + safety chips, s06 OS frames, s07 units + findings + outputs, s09 layers, s10 buckets, s12 icons, s13 verdict chips)
- `gsap-typewriter`: 5 (s02 quote, s06 brew install, s07 sub-quote beats, s10 per-card sub-quotes ×5, s11 quote, s13 question)
- `gsap-counter-tween`: 4 (s01 847.5K views, s03 1→10 counter, s05 3,478 + 4, s11 70% pulse)
- `gsap-path-draw`: 2 (s06 architecture diagram, s09 right-bracket label)

## Anchors with no good pick (gaps for Phase 4 to author inline)

- **"847,000" or "847.5K" verbatim in s01**: not found in transcript (script may have said "847,000 viewers" but transcript likely shows separate tokens "847,000" — Phase 4 to ffprobe-grep). If not matchable, anchor the views chip to "this week" (idx=53 approx, t=~23s) instead. Inline-gsap-custom: `views-chip-tween-anchored-to-this-week-word`.
- **Camp 2 verbatim phrase "Camp two is the forward"**: NOT FOUND verbatim — transcript may use a paraphrase. Phase 4 to manually inspect words 870-900 in transcript and pick the closest anchor for camp 2's entrance (estimated ~t=370s based on context). Inline-gsap-custom: `camp-2-entrance-anchored-to-manual-word-lookup`.
- **"70%" verbatim (s11)**: not found as a single token; transcript may render it "70," "percent," etc. Phase 4 to ffprobe-grep transcript for `70` substring and lock the scale-pulse to its anchor. Inline-gsap-custom: `seventy-percent-scale-pulse-after-grep`.
- **"It's not cost" / "It's latency" s11**: matched without apostrophe (`Its not cost`, `Its latency` per transcript normalization). All transcript words preserve apostrophes in display form — Phase 4 to verify the exact rendered word for the marker anchor (likely shows as "It's" with apostrophe).
- **Second "tokens don't matter" in s13** (callback to s02 thesis): not matched in transcript (matched only the s02 instance). Phase 4 to search for the second occurrence near idx 1232-1240 and adjust the s13 thesis-callback marker anchor (currently floating).
- **Bucket sub-quotes (s10)**: the 5 typewriter sub-quotes per camp need exact phrase matches in transcript (camp 1 "extremely lean" ✓ found, camp 2 "18-36 months" ✓ found, camp 3 "Cerebras/Grok/Qwen" ✓ found, camp 4 "narrow my thinking" ✓ found, camp 5 "what am I looking at" — NOT VERIFIED; transcript shows "cant parse the stack" instead). Phase 4 to swap camp 5 sub-quote text to use the actual transcribed phrase, or accept the paraphrase if the on-screen text is creative-license per plan §10 (paraphrased only).

## Override Notes

Phase 4 (composition build) reads this file as authoritative. To override any pick, edit this file directly before invoking the build. Key reconciliation tasks Phase 4 MUST address:

1. **Plan-vs-narration drift**: Total narration is 527s; plan is 540s. The 13s difference is concentrated in the two Hostinger midroll windows (s04 + s08) where the sponsor-read narration is missing from the audio file. Phase 4 to inject sponsor-read narration OR accept narration shortfall and adjust scene `data_start` values to match actual narration anchors. Recommended: re-run TTS with sponsor reads added to scenes 4 and 8.

2. **Marker cap re-audit per scene**: As-listed, each scene stays at ≤2 markers. Phase 4 to re-confirm during HTML authoring; if visual feedback shows even 2 markers feels noisy in s10 (with 5 cards + sub-beats already), drop the s10 markers to 1.

3. **Audio-reactive subtlety**: §3 cap is 3-6% scale variation for text; Phase 4 to confirm `audio-reactive-glow` instances stay within cap and DO NOT use banned vocab (equalizers, spectrum analyzers, strobing).

4. **Final-frame held-still**: s13 freeze from t=527s onward is 13s (rather than plan's 5s) because narration ends earlier than plan. This is BETTER for thumbnail purposes. Phase 4 to verify the 5 mandatory thumbnail-grade elements are all visible at t=527s and persist unchanged to t=540s.

5. **Sub-composition wiring**: every sub-comp mount in `index.html` MUST satisfy the parent↔child `data-composition-id` match rule per `.claude/rules/sub-composition-wiring.md`. Phase 4 lint check.

6. **Composition duration extender**: last line of root `<script>` MUST be `tl.set({}, {}, 540);` per `.claude/rules/hyperframes-pitfalls.md` §1.

7. **Visual-pacing-5s audit per scene before lint**: Every scene below has sub-beats spec'd to keep all gaps ≤5s. Phase 4 must implement each sub-beat — not just the headline picks — or the rule fails.

8. **Step-by-step reveal `tl.set` pattern**: Every staggered list (s01 slams, s03 10 cards, s05 lanes + chips, s07 units + findings, s09 layers, s10 buckets, s12 icons, s13 chips) MUST use explicit `tl.set` hidden-until-reveal at t=0 followed by `tl.to` at the reveal anchor. NEVER `tl.from()` for these.
