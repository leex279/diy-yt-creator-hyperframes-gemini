# Orchestration Log: claude-code-goal-command

Pipeline started: 2026-05-12
Topic: Claude Code's new /goal slash command
Source: https://code.claude.com/docs/en/goal
Template: shorts/anthropic
Duration: ~120s
Tone: curious / excited (discovery vibe — command is brand new)

Mandatory inclusions:
- Simulate a Claude Code terminal running /goal with real example output (sourced from docs)
- Cover what /goal does, when to use it, how it differs from a normal prompt
- "Try it now" CTA at the end

Template selected: shorts/anthropic (user explicitly specified in brief — no prompt needed)

## Phase Summaries (<200 words each)

### Phase 0 — Research (done 2026-05-12)

Docs fetch: SUCCESS. Page `https://code.claude.com/docs/en/goal` saved verbatim to `tmp/source.md`. `/goal` is a session-scoped slash command that sets a completion condition; a small fast model (default Haiku) evaluates after every turn and returns yes/no + reason. "No" feeds back as next-turn guidance; "yes" auto-clears and writes "achieved" to transcript. Built on a session-scoped prompt-based Stop hook. Status view, `/goal clear` + 5 aliases, `--resume`/`--continue` restore, non-interactive via `claude -p`, 4,000-char condition limit, requires accepted trust dialog.

Real terminal examples extracted (verbatim from docs):
- Interactive: `/goal all tests in test/auth pass and the lint step is clean`
- Non-interactive: `claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"`
- Active indicator: `◎ /goal active`

Agent findings:
- A (Core): 23 fact-extracted claims; 10 features mapped; receipt-gated to docs
- B (Competitive): /goal vs /loop vs Stop hook framing strongest
- C (Hook): "Haiku now judges Sonnet" contrarian thesis; "stop typing 'keep going'" pain hook
- D (Visual): Two-model split (Sonnet writes / Haiku judges) hero; `◎ /goal active · 14m 32s` lockup candidate

Cross-refs: CHANGELOG v2.1.139 confirms "Works in interactive, -p, and Remote Control".

Gaps: No real screen recordings available → synthesize terminal frames in HTML/GSAP (not screenshots). No adopter case studies (feature is days old). Codex Goal Mode parallel exists but recommend skipping.

### Phase 1 — Plan (done 2026-05-12)

5 scenes, 120s total:
- S01 Hero / Discovery (0-12s)
- S02 What /goal does (12-32s)
- S03 Terminal Simulation (32-65s) — ANCHOR scene, 33s
- S04 How it differs from a normal prompt (65-90s)
- S05 Endcard / try-it-now CTA (90-120s)

Hook variant: `variant_a` counterintuitive, score 8.6 — "Wait. There's a new slash command in Claude Code — and Haiku judges Sonnet now." Pattern: TerminalHacker (5 visual beats — thumbnail-grade first frame at t=0, "Wait." slam at 2.5s, typewriter hook 3.6-7.5s, Haiku/Sonnet pills 8-10s, whoosh exit at 11s).

S03 terminal: data_start=32, data_duration=33 — 6-beat sequence (typewriter command, ◎ active indicator, turn-1 output, Haiku verdict-no bubble, turn-2 output, Haiku verdict-yes + "achieved" transcript line + thought-narration kicker at 60s).

Retention picks: 5 markers (3 highlight + 2 circle, max 1/scene), 2 caption-fade-slide scenes, 0 audio-reactive, 4× blur-crossfade transitions (single-primary discipline).

Fact-check audit: 17 claims — 14 sourced verbatim, 3 omitted (Could-Include — 4000-char limit, eval cost, 1-goal-per-session) for budget. 0 fabricated. Heteronyms `live`/`lead` planned absent.

Phase 3.5 follow-up flagged: S04 needs mid-beat at ~70s + tail-hold mid-beat at ~85s for ≤5s pacing.

### Phase 2 — Script (done 2026-05-12)

Total: 259 words (target 240-290). Per-scene: S01 25w / S02 50w / S03 78w (anchor) / S04 59w / S05 47w.

Scene 01 opens with the locked hook (variant_a, score 8.6): "Wait. There's a new slash command in Claude Code — and Haiku judges Sonnet now."

Scar insert in S03 (concrete failure + verdict-as-guidance): "Two tests still fail. Haiku reads the transcript and returns: 'no — auth login still broken.' That reason becomes turn two's directive."

Receipts: 5 inline source-receipt comments. Specifics: verbatim docs command paraphrased ("all tests in test slash auth pass and the lint step is clean"), version 2.1.139, "Haiku by default", "yes or no with a short reason", auto-clear + "achieved".

Banned phrase self-check: PASS. Heteronym audit: PASS — "live" never appears; "lead" never appears as noun. Tech terms spelled phonetically.

Tone: curious/discovery throughout. "judges"/"checks" used 4× for Haiku's role. Sonnet↔Haiku writer/judge split in hook + S03 kicker. CTA = try-it-now (no follow/subscribe ask; Dynamous endcard handles brand outro).

### Phase 2.5 — Critique (done 2026-05-12)

Scores: QG-1 hook 8.1/10 PASS, QG-2a arc 7.7/10 PASS, QG-3 loop openers 2/2 PASS, QG-7 JCRR 95.7% STRONG.

Three failures handled:
1. **QG-4 (em dashes, real)**: 11 narration em dashes auto-fixed inline (replaced with commas or sentence breaks). Lines 5/12/18/24/30. Brand voice §B.2 #5 compliance restored.
2. **QG-2b (CTA standalone, overridden)**: critique demanded rhetorical-question + comments-ask + subscribe-ask. Conflicts with user brief ("try it now CTA at end") + locked memory `feedback_dynamous_short_outro` (Anthropic-shorts use SHORT Dynamous pointer only, endcard carries the rest visually). Override documented; script unchanged on this gate.
3. **QG-5c (engagement closer, overridden)**: same root as QG-2b. Override.

Heteronym audit passed (no `live`, no `lead` as noun). Banned phrases: 0. Final closer remains: "type slash goal instead. State the finish line once. The docs are at..." + locked Dynamous pointer line.

### Phase 2a — TTS Script (done 2026-05-12)

5 per-scene files (150/295/463/347/317 chars — all under 800 cap) + flat script.txt at 274 words / 1576 chars.

Version-string spelling: "version two point one point one three nine" (precedent from videos/claude-code-v2126/script-tts.txt + new-claude-code-version-short.md). Other TTS adjustments: `dynamous.ai` → `dynamous dot ai` in S5.

Per-scene + flat-file word count match (274/274). No heteronym re-introductions during optimization.

### Phase 2b — Fact-Check (done 2026-05-12, 10/10 claims verified)

PASS. T1=7, T2=3, T3=0. All 10 VERIFIED, 0 corrected/stale/unverified/failed.

URL audit:
- https://code.claude.com/docs/en/goal → 200, page matches tmp/source.md verbatim
- CHANGELOG raw → 200, top entry confirmed v2.1.139: "Added `/goal` command: set a completion condition and Claude keeps working across turns until it's met. Works in interactive, `-p`, and Remote Control."

Auto-applied corrections: 0. script.txt left untouched.

Receipt audit: 6 inline source-receipt comments cross-referenced cleanly with brief's Receipts section.

Heteronym recheck: clean (zero matches for live/lead/read/close/etc. across all scene files + flat script.txt).

Bidirectional check vs source.md: zero contradictions. Intentional coverage omissions (4000-char limit, 5 aliases, ◎ active indicator, resume behavior, disableAllHooks) are scoping choices for the 120s budget, not factual issues.

Report at videos/claude-code-goal-command/scripts/fact-check-report.md.

### TTS — ElevenLabs (done 2026-05-12)

`python scripts/elevenlabs-tts.py videos/claude-code-goal-command --shorts` succeeded.
- narration.wav: 103.42s, 9.12MB (under 120s budget — 16.6s headroom for thumbnail holds)
- transcript.json: 274 words with word-level start/end timestamps (first "Wait." at 0.046s, last "community." at 103.18s)
- 20 chunks generated, voice_id=7kXNOCqiaLdszL0OEXks, speed=1.13 (shorts)
- pronunciation_dictionary=AhK3J8mZDRoShxfoJLk6 used

No separate `npx hyperframes transcribe` needed — elevenlabs-tts.py emits transcript.json directly via the API alignment data.

### Phase 3.5 — Retention Strategy (done 2026-05-12)

5 scenes anchored to real transcript times (narration ends at 103.18s, not plan budget 120s).

Picks: 6 markers (4 highlight + 2 circle), 2 caption-fade-slide (S02/S04), 0 audio-reactive (news-explainer tone), 4× blur-crossfade transitions (single-primary), 4× gsap-typewriter (S01 hook + S03 command/turn-1/turn-2), 5× gsap-stagger-grid, 4× scale-pulse mid-beats.

S03 terminal sim picks (no obscuring components): gsap-typewriter ×3, ◎ active indicator scale-slam + orange glow, verdict-no glitch-zap, verdict-yes scale-slam, 2 marker-highlight sweeps on yes-achieved verdict + "achieved" transcript line, deterministic CSS cursor blink, thought-narration content-morph at 59.10s, indicator scale-pulse mid-beat at 47.50s.

First-frame lockup (t=0 → 2.4s held): ◎ glyph 160px + Anthropic/Claude Code lockup + "NEW IN v2.1.139" chip + outcome "Set the finish line once". All visible from frame zero via tl.set().

Last-frame lockup (95.80s → 103.18s, ~7.4s held): ◎ 160px + "Try /goal" 140px + finish-line outcome + URL chip with marker-circle + Anthropic/Claude Code brand chrome. Doubles as auto-thumbnail/loop-pause.

Constraint violations resolved: S02 markers downgraded 3→2 (Yes-highlight→scale-pulse). S03 markers downgraded 3→2. S03 + S04 5s pacing gaps filled with scale-pulse mid-beats.

SFX cues: 26 instances anchored to transcript word indices, all ≤0.25 vol (sonic-logo 0.60 exception). No SFX during Dynamous outro.

### Phase 4 — Composition Build (done 2026-05-12)

5 phases (mutex z-stack) built into videos/claude-code-goal-command/index.html (706 lines, 57KB):

| Scene | data_start | data_duration |
|---|---|---|
| S01 Hero/Discovery | 0 | 9.86 |
| S02 4-step loop | 9.86 | 18.70 (→28.56) |
| S03 Terminal Simulation | 28.56 | 31.86 (→60.42) |
| S04 Differs matrix | 60.42 | 22.43 (→82.85) |
| S05 Endcard/Thumbnail hold | 82.85 | 25.65 (→108.5) |

Root `data-duration="108.5"` (narration 103.18s + 5.3s frozen thumbnail hold).

Terminal sim (S03): full-bleed dark panel #0A0E16, JetBrains Mono 30px. Traffic-light chrome + `claude — goal` title. Orange `claude >` prompt typewriter types verbatim docs example `/goal all tests in test/auth pass and the lint step is clean` (31.80→37.80s). `◎ /goal active · 00:01` indicator with scale-slam + glow (38.40s). Turn-1 output red 2-failed (40.20s), verdict-no muted-red bubble `Haiku · no · "auth/login_test.js still failing"` with glitch-zap (44.70s). Indicator scale-pulse mid-beat (47.50s). Turn-2 all-green + OK (50.70s), verdict-yes green bubble `Haiku · yes · achieved.` with scale-slam (52.75s). Green marker sweep behind "achieved." (54.15s). Transcript line `[goal achieved · 2 turns · auto-cleared]` (55.48s). Kicker `// Haiku just told Sonnet to keep working. That's the loop.` (59.10s).

First-frame lockup at t=0 via CSS default opacity (no tl.from): Anthropic + Claude Code lockup, ◎ glyph 160px + "/goal active" label, NEW IN v2.1.139 pill, outcome line. Held to 2.4s.

Last-frame thumbnail (96.4 → 108.5s, 12s+ static): ◎ 180px + "Try /goal." 140px headline + "State the finish line once." + claude.com/docs/en/goal URL chip with marker-circle + SHIPPED IN v2.1.139 pill + persistent Anthropic chrome.

Retention components installed: gsap-stagger-grid ×5, gsap-typewriter ×4, marker-highlight ×4, marker-circle ×3, scale-pulse mid-beats ×4, opacity fade ×1. Transitions: 4× blur-crossfade (single-primary).

SFX: 29 audio elements wired (vs 26 target — +3 for layered cold-open + S5 entrance pops). 8 unique cues (sonic-logo, impact-slam, screen-shake, spring-pop×14, cinematic-whoosh×4, pop×4, scale-slam×3, glitch-zap). All audio-design compliant.

Lint: 0 errors, 2 informational warnings (intentional duplicate brand img + 706-line advisory).
Inspect: 0 layout issues across 9 timeline samples.

Preview running at http://localhost:3013.


















