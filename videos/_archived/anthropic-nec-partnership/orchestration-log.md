# Orchestration Log: anthropic-nec-partnership

Pipeline started: 2026-04-28 15:45
Topic: Anthropic × NEC partnership — Claude rolling out to ~30,000 NEC employees worldwide, NEC becomes Anthropic's first Japan-based global partner, jointly building Japan's largest AI-native engineering team via Claude Code, plus joint industry-specific solutions for finance, manufacturing, and local government.
Source URL: https://www.anthropic.com/news/anthropic-nec
Template: shorts/anthropic
Duration: 45s (default for shorts/anthropic)

Template selected: shorts/anthropic (suggested: shorts/anthropic; user confirmed)

## Phase Summaries (<200 words each)

### Phase 0 — Research (done 2026-04-28)

**Depth**: LIGHT (45s short). TOPIC_TYPE: ARTICLE_RESPONSE. Voice: `news-explainer`.

**Agents A–D**:
- **A (Core)**: Anthropic page confirmed — ~30K NEC Group seats; Claude/Opus 4.7/Claude Code/Cowork integrated; NEC BluStellar Scenario integration; Center of Excellence; Client Zero status; verticals = finance/manufacturing/local-gov/cybersecurity (SOC).
- **B (Competitive)**: Three-way Japan AI race — Microsoft $10B/5-partner, OpenAI×SoftBank $3B/yr JV, now Anthropic×NEC. First Japan-based global Anthropic partner. Japan faces 3.26M AI-worker shortfall by 2040.
- **C (Hooks)**: Strongest contrarian = "It's not the 30K, it's the 1899" (NEC founded 1899, now 127yo, ~105K total employees). Cult-hops vs Deloitte 470K, Cognizant 350K, Accenture 30K. Claude Code "most loved" 46% vs Cursor 19%, Copilot 9%.
- **D (Visual)**: 7 concepts — 1899→2026 morph, skyscraper-windows org rollout, Japan map pin, BluStellar plug-in, verticals 2×2 grid, 17.7M→29M Claude Code curve, competitor card-stack.

**vidiq**: USED. Top title score 91/100 ("Anthropic Just Took Over a 100,000-Person Japanese Giant"). Zero seed-volume keywords (breakout-fresh) — lean on title CTR.

**Quality gates**: 7 PASS / 0 WARN / 0 FAIL.

**Gaps**: NEC press release 403'd (Anthropic page covers same facts); "Japan's largest AI-native engineering team" is partner-framed (flag for Phase 2b); MS $10B Japan timeline 2026-2029 needs verification if quoted.

### Phase 1 — Plan (done 2026-04-28)

- **Scenes**: 5 (≤60s cap), avg 9s — Hook · Timeline-Shocker · First-Japan-Partner · 30K-Rollout · CTA-Who's-Next.
- **Hook variant locked**: variant_b (Stakes), score **10.0** — "Anthropic just out-flanked OpenAI in Japan — because a 127-year-old company gave Claude Code to 30,000 engineers." Beat variant_a (9.7) and variant_c (8.2); news-explainer profile demanded the `because` connector.
- **Pattern**: `ContrastPivot` (5 visual beats: Cold Open → Context → PIVOT → Stakes Reveal → Crossfade).
- **Total `data_duration`**: 45s (9 + 10 + 8 + 10 + 8).
- **Retention picks**: 7 markers (highlight/circle/scribble) · 2 caption fade-slide groups · 1 audio-reactive glow on the CTA pill · 4 blur-crossfade transitions.
- **Fact-check audit**: 11 sourced (4 in narration, 7 deprioritized for 45s budget) · 2 derived (Edison-era metaphor, 29% arithmetic) · 1 hedge-rephrased ("what they're calling Japan's largest AI-native engineering team") · 5 deprioritized (BluStellar, verticals, Client Zero, $3B OpenAI, $10B Microsoft) · 0 direct quotes generated. NEC press release 403 still flagged for Phase 2b retry.

### Phase 2 — Script (done 2026-04-28)

- **Words**: 123 across 5 scenes (45s @ ~164 wpm avg).
- **Scenes**: 5 (Hook · Edison-Era reveal · First Japan Partner · 30K Rollout · CTA).
- **Hook locked (Scene 1, first sentence)**: *"Anthropic just out-flanked OpenAI in Japan, because a 127-year-old company gave Claude Code to 30,000 engineers."* (em-dash → comma per news-explainer profile.)
- **Scar insert**: YES (Scene 3) — *"It's engineering depth, the kind enterprises pilot for years and never deploy."*
- **Banned-phrase self-check**: PASS — 0 hits across universal AI list + hype list; no em dashes in narration; no "we" as company; no "But here's the thing"; no "Most developers don't know."
- **News-explainer mandates**: 5 body connectors with 3 unique types (`and`×3, `so`×1, `to <verb>`×1, exceeds ≥3/≥2). Direct-address body line in Scene 4 ("If you build on Claude, this is your proof."). Scene 5 CTA carries all 3 components (rhetorical question + comments-ask + subscribe-ask).
- **WPM caveat**: Scenes 3 & 4 sit at 180 wpm (target 150-165) — Phase 2.5 will validate.

### Phase 2.5 — Critique (PASS — 9.7/10 hook, 8.3/10 arc, 2026-04-28)

- **QG-1 (Hook)**: PASS 9.7/10 — curiosity gap, `because` connector, named subject in line 1, "But the seat count isn't even the shocking part" stun-gun pivot.
- **QG-2a (Arc 1+2+4)**: PASS 8.3/10 — slight value-timing delay (~10s) but cohesion strong; both open loops resolved.
- **QG-2b (CTA solo)**: PASS 9.0/10 — all 3 components, under 15 words.
- **QG-3 (Loop openers)**: PASS — 2 found / 2 required (Scene 2 carry-pivot, Scene 4 "And here's what should worry OpenAI").
- **QG-4 (AI-phrasing)**: PASS — 0 banned phrases.
- **QG-5 (Narrative flow)**: PASS — connector density 6/10, direct-address line present, CTA all three.
- **Advisory for Phase 2a**: insert `[PAUSE]` before "1899", "127 YEARS", and "30,000" reveal beats.

### Phase 2a — TTS Script (done 2026-04-28)

- **Scenes**: 5 (hook · edison-era · first-japan-partner · rollout · cta).
- **Char counts (all <800)**: 236 / 204 / 159 / 213 / 110.
- **TTS skill used**: `text-to-speech` (not fallback).
- **Optimizations**: numbers→words ("eighteen ninety-nine", "thirty thousand", "one hundred twenty-seven-year-old"); `NTT Data` → "N T T Data"; kept `Claude`, `Claude Code`, `NEC`, `OpenAI`, `AI-native` natural per skill rules. 4 `<break time="0.5s" />` tags inserted at the Phase 2.5-flagged reveal beats.
- **Flat `script.txt`**: written (834 chars, 128 words, single paragraph, no scene headers / break tags / pause markers) — matches `claude-connectors-everyday-life/script.txt` format. Ready for `npx hyperframes tts`.

### Phase 2b — Fact Check (PASS — 7/7 claims verified, 2026-04-28)

- **Tiers**: 6 Tier-1 critical · 0 Tier-2 · 1 Tier-3 contextual.
- **Verdicts**: 6 VERIFIED · 1 CORRECTED · 0 STALE / UNVERIFIED / FAILED.
- **URL audit**: 4 of 5 LIVE (Anthropic, Wikipedia, TheFastMode, ITBrief). NEC press URL still 403'd; same content mirrored at ACN Newswire (verified live) — non-blocking.
- **Auto-corrections applied (1)**:
  - Scene 04: *"building what NEC calls Japan's largest AI-native engineering team"* → *"building what NEC calls one of Japan's largest AI-native engineering teams"* (matches Anthropic's verbatim "aims to build one of Japan's largest AI-native engineering teams"). Synced across scene-04 file, full-script.md, and flat script.txt.
- **Phase 1 flag resolved**: hedge phrasing already present, fix added missing "one of" + pluralized "team→teams".

### TTS handoff (manual, 2026-04-28)

- `npx hyperframes tts` → `audio/narration.wav` (56.7s, 11.7s longer than plan's 45s).
- `npx hyperframes transcribe` blocked: requires `whisper-cpp` binary, not installed.
- Fallback: `pip install openai-whisper`, ran `whisper --model small.en --output_format json --word_timestamps True`, converted output to flat `[{word, start, end}]` shape via Python one-liner. `transcript.json` = 133 words, 56.34s. Whisper transcribed "Claude" as "clawed/claw" — known Whisper artifact, ignored (retention picks key off canonical Phase 2a script).

### Phase 3.5 — Retention (done 2026-04-28)

- **Scenes**: 5 (re-paced 45s → 56.34s; +11.34s spread proportionally — composition build MUST use `retention-strategy.md` timings, not `plan.md`).
- **Picks by category**:
  - Markers: 6 (scribble ×1 · highlight ×3 · circle ×2).
  - Captions: 2 scenes (02 and 04, both `caption-fade-slide`).
  - Audio-reactive: 1 (`audio-reactive-glow` on Scene 5 subscribe pill, treble band).
  - Transitions: 4 `blur-crossfade` (every phase change; final scene has no exit).
  - GSAP effects: 9 invocations (`gsap-stagger-grid` ×5, `gsap-counter-tween` ×4, `gsap-path-draw` ×2).
  - SFX cues: 21 (all <0.25 cap; Scene 1 BUT-pivot stack uses tracks 4/5/6 for layered impact-slam + screen-shake + glitch-zap).
- **Violations resolved**: SFX track collision in Scene 1, Scene 4 caption split to skip the 30K slam, 11.34s pacing overrun.
- **Anchors with no good pick**: Scene 3 "engineering depth", Scene 5 "let me know in the comments", Scene 2 "Anthropic's" callback (covered by caption group).
