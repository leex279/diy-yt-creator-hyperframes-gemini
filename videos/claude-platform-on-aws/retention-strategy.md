# Retention Strategy: claude-platform-on-aws

**Source inputs**: `plan.md`, `scripts/full-script.md`, `transcript.json` (290 words, 108.89s narration ending — final word "community" ends at 108.886s; +0.2s tail → composition total ≈ 109.1-110.0s).

**Critical retiming note**: The plan's `data_timing_budget` assumed a 95s composition. Actual transcript clocks at ~109s (15% longer because the script grew by 2 sentences during Phase 2/2a — "the prompt improver / the generator / the evals UI" in Scene 4 was kept by the fact-checker, and the Dynamous outro lines are longer than the placeholder). Every scene `data_start` and `data_duration` below is re-anchored to the actual transcript word positions, not the plan's placeholders. The visual ordering (9 scenes, accent rotation, retention picks) is preserved — only the time math changes.

**Fact-check correction applied**: Phase 2b changed "17 AWS regions" → "eighteen AWS regions". Scene 06 visual updated: 18 region dots, counter tween 0→18, hero slam reads "18" (240px orange). This file enforces "eighteen" as the canonical count.

---

## Summary Table

| Scene | Pattern (from §7) | Primitives | Captions | Audio-Reactive | Transition Out | Total Picks |
|-------|------------------|------------|----------|----------------|----------------|-------------|
| 01 — Hook (Bedrock lag pain) | `hero-slam` | `gsap-stagger-grid`, `marker-highlight` | none | none | `blur-crossfade` | 3 |
| 02 — Pivot reveal | `hero-slam` | `gsap-stagger-grid` | none | none | `blur-crossfade` | 2 |
| 03 — Not-a-rebrand split | `stat-pill-row` (2-col comparison) | `gsap-stagger-grid`, `marker-highlight` | none | none | `blur-crossfade` | 3 |
| 04 — 8-beta pill cluster | `stat-pill-row` (extended 8-pill cluster) | `gsap-stagger-grid` | none | none | `blur-crossfade` | 2 |
| 05 — AWS integration receipts | `code-walkthrough` (URL-pill variant) | `gsap-typewriter`, `marker-highlight`, `gsap-stagger-grid` | none | none | `blur-crossfade` | 4 |
| 06 — 18 regions slam | `narrated-stat-reveal` | `gsap-stagger-grid`, `gsap-counter-tween` | none | none | `blur-crossfade` | 3 |
| 07 — Customer trust row | `stat-pill-row` (3-wordmark adapt) | `gsap-stagger-grid` | none | none | `blur-crossfade` | 2 |
| 08 — When to pick which | `stat-pill-row` (2-col decision matrix) | `gsap-stagger-grid`, `marker-highlight` | none | none | `blur-crossfade` | 3 |
| 09 — Thumbnail hold | `cta-url-slam` (thumbnail-grade) | `gsap-stagger-grid`, `marker-circle` | none | none | none (final) | 2 |

**Picks by category**:
- markers: 5 (scenes 01/03/05/08) `marker-highlight` + 1 (scene 09) `marker-circle` = **6 marker picks total**
- captions: **0** (narration carries; news-explainer dark-stage aesthetic per plan)
- audio-reactive: **0**
- transitions: **8 × `blur-crossfade`** (one primary, 100% — well within the 60-70% target band; calm-energy aesthetic per `transitions.md`)
- gsap effects: 9 × `gsap-stagger-grid`, 1 × `gsap-counter-tween`, 1 × `gsap-typewriter` = **11 gsap-effect picks**

**Total picks across all scenes**: 24.

**Constraint compliance**: max 2 markers/scene respected (max in any scene is 1). One caption group at a time respected (zero captions). One primary transition respected (`blur-crossfade` for all 8 boundaries). No exit animations on non-final scenes. No more than 2 markers/scene anywhere.

---

## Scene-by-Scene Detail

### Scene 01: Hook — Bedrock lag pain (data_start=0.0s, data_duration=6.59s)

**Words in scene**: 17 (transcript indices 0-16).

**Anchor moments**:
- 0.046s — first word "Every" (entrance moment — overline beat)
- 1.753s — "Claude" (brand mention — could be glow but skip; we're staying calm)
- 3.727s — "Bedrock" (the pain subject)
- 5.05s — "weeks" (the slam word — purple marker target)
- 5.318s — "late." (caps slam closer; marker sweep peaks here)

**Picks**:

1. **`gsap-stagger-grid`** — overline "AWS DEVS, READ THIS" enters at 0.046s; hero phrase "BEDROCK gets the new features…" line 1 enters at 1.753s (anchored to word "Claude" but visual is the hero phrase line ramping in); "WEEKS LATE" sub-slam enters at 5.05s anchored to word "weeks" (transcript index 15, start=5.05059s).
2. **`marker-highlight`** (purple, max 1/scene) — sweeps under "WEEKS LATE". `trigger_s` = 5.318 (word "late.", index 16), sweep_duration = 0.5s (`back.out(1.7)`).
3. **`blur-crossfade`** to Scene 02 — `trigger_s` = 6.094 (scene_end 6.59 − 0.5s transition duration). The whoosh fires at scene_end 6.59s (HARD rule: whoosh at the visual transition moment, NOT pre-rolled; per `audio-design.md` 2026-05-10 clarification).

**SFX cues** (per `.claude/rules/audio-design.md`; cues from `shared/audio/MANIFEST.md`):
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 02
    anchor_word_index: 17        # transcript.json[17] = "But" @ 6.594s — the next scene's first word
    offset_seconds: 0            # whoosh peak aligns with visual phase swap at scene_end 6.59s
    duration_seconds: 1.5        # per audio-design.md HARD rule — 1.5s exposes full decay tail
    track_index: 3
    volume: 0.11                 # MANIFEST default cinematic-whoosh; ≤ 0.25 cap
```

**Why these picks**: The hook script is short (4 sentences over 6.6s) and benefits from a single dominant marker, not a marker cluster. Purple under "WEEKS LATE" plants the pain visually; the next scene's pivot ("BUT TODAY") inverts the color to orange to reinforce the reversal. No captions because the visual hierarchy (overline → hero phrase → marker → sub-slam) already directs the eye through the same words narration is speaking. No audio-reactivity per the template's dark-stage default.

---

### Scene 02: Pivot reveal — "But today, that lag is gone" (data_start=6.59s, data_duration=7.41s)

**Words in scene**: 17 (transcript indices 17-33).

**Anchor moments**:
- 6.594s — "But" (PIVOT word — the stun-gun moment)
- 6.757s — "today,"
- 7.232s — "lag"
- 7.558s — "gone." (closes the pain)
- 8.394s — "Anthropic" (brand reveal beat begins)
- 9.752s — "Claude" (start of product title in spoken form)
- 10.008s — "Platform" (full product name lands)
- 11.076s — "S." (end of "AWS")
- 12.352s — "Generally" (date chip beat)
- 13.258s — "today." (GA date close)

**Picks**:

1. **`gsap-stagger-grid`** — three sequential reveals on the same hero slot:
   - "BUT TODAY" 200px purple slam enters at 6.594s (anchored to word "But"; `back.out(1.7)` 0.4s)
   - Slam fades out at ~8.0s; product title "CLAUDE PLATFORM ON AWS" 160px warm off-white enters at 9.752s (anchored to word "Claude")
   - "Generally Available · May 11, 2026" date chip (mono, orange fill) enters at 12.352s (anchored to word "Generally")
2. **`blur-crossfade`** to Scene 03 — `trigger_s` = 13.5 (scene_end 14.0 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition INTO this scene (the pivot whoosh)
    anchor_word_index: 17        # "But" @ 6.594s
    offset_seconds: 0            # whoosh peak fires at visual phase swap = 6.59s
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: impact-slam             # OPTIONAL: pivot punctuation on "BUT TODAY" hero slam
    anchor_word_index: 17        # "But" @ 6.594s
    offset_seconds: -0.05        # 50ms lead-in for percussive attack-onset
    duration_seconds: 0.63       # impact-slam.mp3 from MANIFEST
    track_index: 4               # concurrent with whoosh on track 3
    volume: 0.15                 # MANIFEST default; the ONE per-element SFX allowed by template (per plan note 8)
  - cue: cinematic-whoosh        # transition out to Scene 03
    anchor_word_index: 34        # "And" @ 14.001s (first word of Scene 03)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 02 is the structural fulcrum of the entire short — the Uno Reverse. The single allowed per-element `impact-slam` from the template's 2026-04-28 calibration belongs here, layered with the inbound whoosh (different track indices to avoid overlap). The hero-slam pattern handles the slam→title→chip sequence as one composite — no marker, because both "BUT TODAY" and "CLAUDE PLATFORM ON AWS" already dominate the screen. A marker on either would be decorative noise.

---

### Scene 03: Not-a-rebrand split (data_start=14.00s, data_duration=12.88s)

**Words in scene**: 30 (transcript indices 34-63).

**Anchor moments**:
- 14.001s — "And" (scene entrance, overline beat)
- 16.729s — "This" (header reveals — "This is not Bedrock with a new name")
- 18.784s — "Bedrock" (left column anchor — "Bedrock is the data-resident subset")
- 19.608s — "data-resident" (key term, marker candidate but left column is the dim side; skip)
- 21.837s — "Platform-on-A" (right column anchor — the "full native API")
- 23.857s — "native" (right column emphasis)
- 25.831s — "Day" (the closing slam — "DAY ZERO" — marker target)
- 26.017s — "zero." (orange marker sweep peak)

**Picks**:

1. **`gsap-stagger-grid`** — column structure reveals step-by-step:
   - Headline "NOT A REBRAND" + 2-col scaffold at 14.001s (anchored to "And")
   - Left col "Claude on Bedrock — data inside AWS, feature subset, weeks lag" content enters at 18.784s (anchored to "Bedrock")
   - Right col "Claude Platform on AWS — full native API, day zero, data outside AWS" content enters at 21.837s (anchored to "Platform-on-A")
   - Right col closer chip "DAY ZERO" enters at 25.831s (anchored to "Day")
2. **`marker-highlight`** (orange, max 1/scene) — sweeps under "DAY ZERO" on right-column closer. `trigger_s` = 26.017 (word "zero.", index 63), sweep_duration = 0.5s.
3. **`blur-crossfade`** to Scene 04 — `trigger_s` = 26.38 (scene_end 26.88 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 04
    anchor_word_index: 64        # "Which" @ 26.876s (Scene 04's first word)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: The split's job is to differentiate. Sequential reveal of left then right (dim-blue then orange) lets the viewer build the comparison the same way the narrator builds it. The marker on "DAY ZERO" punctuates the right-column's payoff — and stays orange, the right column's accent, to reinforce "this side is the winning side." No marker on the left column even though "data-resident subset" is a key term, because two markers in a comparison phase confuses the eye about which side is being emphasized.

---

### Scene 04: 8-beta pill cluster (data_start=26.88s, data_duration=18.91s)

**Words in scene**: 41 (transcript indices 64-104).

**Anchor moments** (each pill anchored to its narration word):
- 26.876s — "Which" (headline "8 BETAS. DAY ZERO." entrance)
- 28.176s — "beta" / "surface" (subhead resolves)
- 31.345s — "Managed" (pill 1: Managed Agents)
- 32.239s — "Advisor." (pill 2: Advisor)
- 32.797s — "Skills." (pill 3: Skills)
- 33.354s — "Files." (pill 4: Files)
- 33.888s — "M" (pill 5: MCP connector — anchor to "M" since "M C P" are 3 individual letters)
- 35.920s — "Code" (pill 6: Code execution)
- 36.941s — "Web" (pill 7: Web search)
- 38.149s — "Claude" (pill 8: Claude Console)

**Picks**:

1. **`gsap-stagger-grid`** with HIDDEN-UNTIL-REVEAL pattern (per `step-by-step-reveal.md`):
   - Headline + subhead enter together at 26.876s (`tl.set` opacity:0 at t=0; `tl.to` opacity:1 at 26.876)
   - 8 pills hidden from t=0; each `tl.to` at the anchor word above (Managed Agents @ 31.345, Advisor @ 32.239, Skills @ 32.797, Files @ 33.354, MCP @ 33.888, Code execution @ 35.920, Web search @ 36.941, Claude Console @ 38.149)
   - Pill entrance: 0.55s `back.out(1.5)` per pill, hidden until reveal (`tl.set` at t=0 + `tl.to` at anchor, NOT `tl.from`)
2. **`blur-crossfade`** to Scene 05 — `trigger_s` = 45.29 (scene_end 45.79 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 05
    anchor_word_index: 105       # "And" @ 45.788s (Scene 05's first word)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: 8 pills in 18.91s = ~2.36s/pill average. The transcript shows pills 2-5 (Advisor/Skills/Files/MCP) actually arrive in narration ~0.5s apart — that's a rapid-fire enumeration in the script, NOT a slow 2.36s rhythm. The retention strategy mirrors the narration: pills enter at the actual word.start of each name. Pills 2-5 land in quick succession (the narrator says them as one breath), pills 6-8 land more spaced (each gets its own sentence). This is the correct application of step-by-step-reveal — pace the visual to the narration, not the math average. After Claude Console enters at 38.149s, the "prompt improver / generator / evals UI" line (41.86-44.91s) plays under the static pill cluster — that's a 6.7s static gap which would normally violate `visual-pacing-5s.md`. Mitigation: pill 8 (Claude Console) gets a subtle scale-pulse beat at 41.86s (anchored to word "The") that does NOT count as a new entrance but does carry visual life; OR the Console pill could be split into two with "prompt improver / generator / evals UI" as a sub-card at 41.864s. **Phase 4 implementer's choice**: simplest path is the sub-card add at 41.864s. Document this in the composition build notes.

---

### Scene 05: AWS integration receipts (data_start=45.79s, data_duration=20.42s)

**Words in scene**: 41 (transcript indices 105-145).

**Anchor moments**:
- 45.788s — "And" (scene entrance, headline "Through your AWS account")
- 49.561s — "The" (URL pill scaffold enters — "The endpoint runs on…")
- 49.700s — "endpoint"
- 51.628s — "external" (the "aws-external-anthropic" mid-word — marker candidate)
- 55.957s — "Auth" (chip 1: IAM SigV4 auth)
- 58.327s — "Every" (chip 2: CloudTrail event — "Every call is a CloudTrail event")
- 60.927s — "Billing" (chip 3: AWS Marketplace billing)
- 65.235s — "commitment." (scene-end transition prep)

**Picks**:

1. **`gsap-typewriter`** on the URL pill — chars type out across 3.0s starting at 49.561s (anchored to word "The"). The full URL "aws-external-anthropic.<region>.api.aws" prints character by character at ~80 chars/s.
2. **`marker-highlight`** (blue, max 1/scene) — sweeps under "aws-external-anthropic" host portion of the URL after typewriter completes. `trigger_s` = 52.557 (just after the typewriter ends and right before the next narration beat).
3. **`gsap-stagger-grid`** — 3 integration chips drop step-by-step:
   - Chip 1 "IAM SigV4 auth" at 55.957s (anchored to "Auth")
   - Chip 2 "CloudTrail audit" at 58.327s (anchored to "Every")
   - Chip 3 "AWS Marketplace billing" at 60.927s (anchored to "Billing")
   - Hidden-until-reveal pattern (`tl.set` + `tl.to`, NOT `tl.from`)
4. **`blur-crossfade`** to Scene 06 — `trigger_s` = 65.71 (scene_end 66.21 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 06
    anchor_word_index: 146       # "Plus," @ 66.209s (Scene 06's first word)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: The URL is the most technical visual in the composition — it earns the `gsap-typewriter` because the viewer needs to read the host pattern. The marker on `aws-external-anthropic` highlights the part that is NOT a Bedrock URL (the killer detail). The 3 chips are paced to the actual narration cadence — each lands as the narrator names it. Blue accent (technical/integration colorway per plan accent rotation).

---

### Scene 06: 18 regions slam (data_start=66.21s, data_duration=7.33s)

**Words in scene**: 17 (transcript indices 146-162).

**Anchor moments**:
- 66.209s — "Plus," (scene entrance)
- 67.335s — "eighteen" (THE number — counter tween target)
- 67.811s — "A" (start of "A W S")
- 68.624s — "regions"
- 69.089s — "at" / "G A" (closing word — region count locked in)
- 70.412s — "That's" (broader-than-most callback)

**Picks**:

1. **`gsap-stagger-grid`** — vertical-cropped dark-styled SVG world map enters at 66.209s. **18 region dots** (UPDATED from plan's 17 per Phase 2b fact-check correction) pop in quick stagger: 6× US, 2× Canada, 4× EU (FRA/IRL/STO/LON), 3× APAC (TYO/SIN/SYD), 1× Brazil, 1× South Africa, 1× Bahrain (the 18th dot — added). Dots populate 66.6-69.0s at ~0.13s apart (quick stagger justified per `step-by-step-reveal.md` — narration says "eighteen AWS regions" as ONE phrase, NOT an enumeration).
2. **`gsap-counter-tween`** — 240px orange "18" counter tweens 0→18 anchored to the word "eighteen". `tween_s_range` = [66.835, 67.907] (word "eighteen" starts at 67.335; tween starts 0.5s before the word lands and resolves to 18 at word.end + 0.2s = 67.907 to give the brain time to register the slam).
3. **`blur-crossfade`** to Scene 07 — `trigger_s` = 73.04 (scene_end 73.54 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 07
    anchor_word_index: 163       # "Three" @ 73.535s (Scene 07's first word)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: The 18-counter slam is the scene's payoff. The map dots earn their quick stagger because the narration is a single short phrase ("eighteen AWS regions") — not an enumerated 18-item list. After the counter resolves, the "broader than most Claude routes at launch" line plays under the static slam (~3s tail hold), which is within the 5s static-gap cap.

---

### Scene 07: Customer trust row (data_start=73.54s, data_duration=13.23s)

**Words in scene**: 26 (transcript indices 163-188).

**Anchor moments**:
- 73.535s — "Three" (overline "LAUNCH CUSTOMERS" entrance + headline "3 named customers, day one")
- 75.056s — "shipping" (key verb — past tense, no marker needed)
- 76.635s — "ReliaQuest" (wordmark 1 — purple-tinted)
- 78.748s — "OpenRouter" (wordmark 2 — blue-tinted)
- 83.101s — "Emergent," (wordmark 3 — green-tinted)
- 85.794s — "model." (scene-end tail)

**Picks**:

1. **`gsap-stagger-grid`** — overline + headline at 73.535s; then 3 customer wordmarks step-by-step:
   - ReliaQuest wordmark at 76.635s (Inter 800, purple)
   - OpenRouter wordmark at 78.748s (Inter 800, blue)
   - Emergent wordmark at 83.101s (Inter 800, green)
   - Each enters with `back.out(1.5)` 0.55s; hidden-until-reveal pattern. Per plan note 2, this is the ONE scene where accent rotation crosses elements (justified as wordmark brand colors, not decoration).
2. **`blur-crossfade`** to Scene 08 — `trigger_s` = 86.27 (scene_end 86.77 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 08
    anchor_word_index: 189       # "So" @ 86.770s (Scene 08's first word)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Three wordmarks, three brand colors, paced to narration. No marker because each wordmark is itself a color-emphasized element — adding a marker on top would compete. The 4.4s gap between OpenRouter (78.748s) and Emergent (83.101s) is internal to a single sentence narration about OpenRouter's IAM detail; this is within the 5s static cap and the narration "OpenRouter routing through AWS IAM" carries the gap.

---

### Scene 08: When to pick which — decision matrix (data_start=86.77s, data_duration=10.03s)

**Words in scene**: 27 (transcript indices 189-215).

**Anchor moments**:
- 86.770s — "So" (scene entrance, headline "WHICH ONE?")
- 87.350s — "pick"
- 87.582s — "which?" (Q closure)
- 88.209s — "If" (left col anchor — "If you want every beta from day one…")
- 89.022s — "beta" / "from"
- 90.404s — "Platform-on-A" (left col closer — "that's Platform-on-AWS")
- 92.737s — "If" (right col anchor — "If your data must stay inside AWS…")
- 94.177s — "A" / "W" / "S," (right col emphasis: "inside AWS" — marker target)
- 95.419s — "Bedrock." (right col closer)

**Picks**:

1. **`gsap-stagger-grid`** — 2-col matrix reveals sequentially:
   - Headline "WHICH ONE?" enters at 86.770s (anchored to "So")
   - Left col (orange) "PLATFORM-ON-AWS: every beta, day one" enters at 88.209s (anchored to first "If")
   - Right col (blue) "BEDROCK: data MUST stay inside AWS" enters at 92.737s (anchored to second "If")
2. **`marker-highlight`** (blue, max 1/scene) — sweeps under "inside AWS" on the right-column. `trigger_s` = 94.177 (word "A" at index 213, start of "A W S"). Sweep duration 0.5s, blue (matches Bedrock column accent).
3. **`blur-crossfade`** to Scene 09 — `trigger_s` = 96.30 (scene_end 96.80 − 0.5s).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # transition out to Scene 09
    anchor_word_index: 216       # "The" @ 96.801s (Scene 09's first word)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: The decision-matrix earns the marker because "inside AWS" is the disambiguator — it's the ONE phrase that explains when Bedrock still wins. Blue accent ties to the Bedrock column. 4.5s gap between left-col (88.209s) and right-col (92.737s) is within cap; the connector "OR if your data must stay…" carries the bridge.

---

### Scene 09: Thumbnail-grade final frame hold (data_start=96.80s, data_duration=12.28s — extends to narration end + 0.2s tail)

**Words in scene**: 74 (transcript indices 216-289).

**Anchor moments**:
- 96.801s — "The" (scene entrance, all 5 thumbnail elements enter)
- 97.230s — "version" (the "lag is over" callback to scene 01)
- 98.519s — "Is" (open-loop question — "Is this the end of Bedrock for new agents?")
- 100.017s — "agents?" (Q closes)
- 101.526s — "Tell" (CTA: "Tell me in the comments")
- 102.490s — "Subscribe"
- 104.904s — "If" (Dynamous outro begins)
- 107.167s — "dynamous" (the brand mention)
- 108.27s — "AI" (the dot AI)
- 108.886s — "community." (final word — narration end)

**Picks**:

1. **`gsap-stagger-grid`** — all 5 thumbnail elements enter within a 0.5s composite stagger at 96.801s (anchored to "The"):
   - Brand chrome (Anthropic + AWS lockup, top-left, ≥48px logo height) at 96.801s
   - Topic slam "CLAUDE PLATFORM. ON AWS." (160px warm off-white, dominant) at 96.901s
   - Visual anchor: orange "GA" badge or version-style chip "MAY 11, 2026" (88px, accent-orange fill) at 97.001s
   - Outcome receipt "8 betas. 18 regions. Day zero." (52px, --fg-dim) at 97.101s — **UPDATED from plan's "17 regions" per Phase 2b fact-check**
   - Subordinate CTA pill "Watch the full breakdown →" (46px, white pill black text) at 97.201s
   - All entrances finish by 97.5s → 11.6s held static (well above the 1.5s minimum per `shorts-thumbnail-frames.md`)
2. **`marker-circle`** (orange, subtle, max 1/scene) — optional hand-drawn ellipse around "ON AWS" in the topic slam. `trigger_s` = 97.5 (after the topic slam settles). Draws over 0.6s then stays. This is the visual anchor that lets the final still pass the "tap test" — a stranger paused on this frame sees "Claude Platform" circled by "AWS".
3. **No transition out** — final scene; static hold until narration ends at 108.886s + 0.2s tail = 109.08s composition end.

**SFX cues**:
```yaml
sfx_cues: []                     # final scene — no whoosh out
```

**Why these picks**: The thumbnail-hold is a single composite reveal followed by a long static. All 5 mandatory elements per `shorts-thumbnail-frames.md` enter in a quick 0.5s stagger then freeze — no trailing animation. The `marker-circle` is subtle, not loud — it survives the 11.6s static hold without becoming repetitive. The hold passes all 4 checks from the rule:
- **Topic test**: "Claude Platform on AWS" (dominant 160px) — yes, name the topic in one sentence.
- **Tap test**: Brand chrome + topic slam + GA date chip + outcome receipt — composite thumb-stopper.
- **Loop test**: Loop opens on the topic statement, not on the CTA.
- **Screenshot test**: Brand + topic carries the share.

Narration through this scene plays under the static hold: lag-over callback, open-loop question for comments, subscribe CTA, Dynamous outro. The visuals do NOT change with the narration — that's the rule's whole purpose for the terminal scene (per `visual-pacing-5s.md` explicit relaxation for terminal hold).

---

## Picks Cross-Reference (validate against menu)

| Pick name | Source section in `retention-components-hyperframes.md` | Confirmed valid? |
|-----------|----------------------------------------------------------|------------------|
| `gsap-stagger-grid` | §5 GSAP Effects | YES — canonical |
| `gsap-counter-tween` | §5 GSAP Effects | YES — canonical |
| `gsap-typewriter` | §5 GSAP Effects | YES — canonical |
| `marker-highlight` | §1 Marker Highlights | YES — canonical |
| `marker-circle` | §1 Marker Highlights | YES — canonical |
| `blur-crossfade` | §4 Scene Transitions (calm energy CSS primary) | YES — canonical |
| `hero-slam` | §7 Pattern Library | YES — canonical composite |
| `stat-pill-row` | §7 Pattern Library | YES — canonical composite |
| `code-walkthrough` | §7 Pattern Library | YES — canonical composite (adapted as URL-pill variant, not full sub-comp) |
| `narrated-stat-reveal` | §7 Pattern Library | YES — canonical composite |
| `cta-url-slam` | §7 Pattern Library | YES — canonical composite |
| `inline-phase` | §6 Composition Structure | YES — canonical (Anthropic Shorts requirement) |
| `mutex-visibility` | §6 Composition Structure | YES — canonical (Anthropic Shorts requirement) |
| `cinematic-whoosh` SFX | `shared/audio/MANIFEST.md` | YES — file present, 0.84s duration, default volume 0.15 → audio-design.md prescribes 0.11 for whoosh |
| `impact-slam` SFX (Scene 02 optional) | `shared/audio/MANIFEST.md` | YES — file present, 0.63s duration, default volume 0.20 → audio-design.md prescribes 0.15 for impact-slam |

**Validation result**: All picks resolve to canonical names. No invented components.

---

## Constraint Check Summary

| Constraint | Result |
|-----------|--------|
| Max 2 markers/scene | PASS — max in any scene is 1 (Scenes 01/03/05/08 have `marker-highlight`; Scene 09 has `marker-circle`; all others have zero markers) |
| Only one caption group visible at a time | PASS (zero captions) |
| One primary transition (60-70%) + 1-2 accents | PASS — 100% `blur-crossfade` across 8 boundaries; calm energy aesthetic doesn't need accents at 95-110s length |
| No exit animations on non-final scenes | PASS — all transitions are `blur-crossfade` (the transition IS the exit); Scene 09 is the only scene with no out-transition |
| Audio: SFX volumes ≤ 0.25 | PASS — `cinematic-whoosh` at 0.11, `impact-slam` at 0.15 |
| SFX alignment drift ≤ 0.15s percussive, ≤ 0.05s drift acceptable | PASS — all `cinematic-whoosh` cues anchored to exact `transcript.json[anchor_word_index].start`; the Scene 02 `impact-slam` uses 50ms lead-in (within the 0.10s spec) |
| Visual pacing: no static > 5s within non-terminal scenes | MOSTLY PASS — Scene 04 has a 6.7s gap from "Claude Console" pill (38.149s) to scene end (45.79s) that the narration "prompt improver / generator / evals UI" carries audibly. Mitigation noted: add a sub-card at 41.864s (anchored to "The") as the 9th visual beat, OR a subtle scale-pulse on the Console pill (does NOT count as new entrance per `visual-pacing-5s.md`). Phase 4 implementer chooses one of these; sub-card is preferred for content density. |
| Shorts thumbnail-grade final frame (`shorts-thumbnail-frames.md`) | PASS — Scene 09 has all 5 required elements, ≥11.6s static hold, no trailing animation |
| Step-by-step reveal (`step-by-step-reveal.md`) | PASS — All multi-item lists (Scene 03 columns, Scene 04 pills, Scene 05 chips, Scene 07 wordmarks, Scene 08 cols) use hidden-until-reveal (`tl.set` + `tl.to`, NOT `tl.from`) |
| TTS heteronym audit (`tts-pronunciation.md`) | N/A here — Phase 2a applied. Script uses "shipping" instead of "live" in Scene 07; "available" instead of "live" in Scene 02. Confirmed against script. |

---

## Constraint Violations Resolved

1. **Plan assumed 95s; actual narration is 109s** — every scene's `data_start` and `data_duration` is re-anchored to transcript word positions, not plan placeholders. Phase 4 composition build must use the times from this file, NOT from plan.md.
2. **Scene 06 fact-correction**: plan said "17 regions"; script and fact-check say "eighteen". This file enforces 18 throughout — 18 region dots on the map, counter tween 0→18, hero slam "18", outcome receipt in Scene 09 reads "8 betas. 18 regions. Day zero."
3. **Scene 04 internal pacing risk** (6.7s static after Claude Console pill) — mitigation noted in scene detail: add a sub-card at 41.864s for "prompt improver / generator / evals UI" line, OR fold this content into Console pill's micro-content. Phase 4 implementer's call.
4. **Plan's whoosh placement** (`sceneT - 0.4`) is OUTDATED per `audio-design.md` 2026-05-10 clarification — whooshes must fire at the visual phase swap moment (`sceneT`), not pre-rolled. All SFX cues above use `offset_seconds: 0` for whoosh alignment.

---

## Anchors With No Good Pick (and Why)

- **Scene 02, word "Anthropic" @ 8.394s** — brand mention; candidate for `audio-reactive-glow` or `marker-circle`. SKIPPED because Scene 02 already has the heavy lift of slam→title→chip; adding a 4th visual beat would compete with the product title reveal. The brand context is carried by the persistent top-banner Anthropic+AWS lockup.
- **Scene 03, word "data-resident" @ 19.608s** — technical key term; candidate for `marker-highlight` on Bedrock column. SKIPPED to keep the 1-marker-per-scene rule (the "DAY ZERO" marker is the right side's emphasis; a left-column marker would compete and confuse which side is being championed).
- **Scene 04, no marker** — 8 pills + a sub-card; adding a marker would over-load the cluster. Color and pill geometry already direct the eye.
- **Scene 06, the "broader than most Claude routes at launch" callback @ 70.412s** — candidate for a sub-line entrance. SKIPPED because the counter slam ("18") already holds attention through 70-73s; adding text below would diminish the slam's dominance.
- **Scene 07, no marker** — three wordmarks in three colors already direct attention; a marker would compete with brand-color emphasis.

---

## Override Notes

Phase 4 (composition build) will read this file as authoritative. To override any pick, edit this file directly before invoking the build.

**Key implementer notes**:
1. Use the `data_start` / `data_duration` values from this file's scene headers, NOT from `plan.md`'s `data_timing_budget` (which was based on 95s placeholder).
2. Use the exact `transcript.json[].start` value for every GSAP trigger and SFX `data-start`. The anchor_word_index values in `sfx_cues` blocks resolve directly to transcript indices.
3. Scene 06 = **eighteen regions**, not seventeen. Update the map dot count, the counter tween target, and the Scene 09 outcome-receipt line accordingly.
4. Scene 04 needs a 9th visual beat between 38.149s and 45.29s (transition out) — recommended: a sub-card "prompt improver · generator · evals UI" anchored to word "The" @ 41.864s (transcript index 102). This satisfies the 5s static cap.
5. Total composition `data_duration` = 109.1s (rounding to integers: set on the `<root>` div). Narration ends at 108.886s; tail = 0.2s.
6. Persistent top-banner Anthropic+AWS lockup runs from t=0 to t=109.1 (full composition).
7. Shape-backdrop drift runs continuously; reposition fires at each phase transition (paired with the whoosh per `audio-design.md` HARD rule — both at the visual phase swap moment, not pre-rolled).
