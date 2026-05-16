# Orchestration Log: anthropic-claude-plan-programmatic-credits

Pipeline started: 2026-05-13 22:35
Topic: ClaudeDevs announcement — paid Claude plans get a dedicated monthly programmatic-usage credit (Agent SDK, claude -p, GitHub Actions, third-party apps like Conductor/OpenClaw) starting June 15. Bonus: Claude Code weekly limits +50% through July 13. Treatment: Anthropic-branded vertical Short, ~180s, news-explainer voice, fast-paced, debate-sparking.
Template: templates/shorts/anthropic
Duration: 180s

## Phase Summaries (<200 words each)

### Phase 0 — Research (ARTICLE_RESPONSE)
Source-only mode; every bullet/quote/URL traces back to tmp/source.md §1–§9. Zero external research. Wrote research/content-brief.md.
- Recommended CTA: "OpenClaw and Conductor on your plan — game changer or backdoor price hike?" (binary, polarizing, references named third-party tools)
- 3 hook angle candidates documented: (1) Stat-led "+50% on Claude Code. Plus a new monthly credit. One catch." (2) Contrarian "Anthropic just changed who you're paying for." (3) Mystery "What do Conductor, OpenClaw, and your own Python script suddenly have in common?"
- Must-mention checklist: 11 verbatim items (4 surfaces, Conductor+OpenClaw, June 8/15 + July 13, Pro/Max/Team/Enterprise plans, support URL, +50% claim, stacking with 5-hour limits)
- Open questions: 7 explicit gaps (credit amount, replace-vs-stack, third-party pricing, free-plan scope, programmatic-vs-interactive definition, etc.) — all scriptable-around
- Anti-fabrication ledger: 10 banned claims
- No blocking gaps. Phase 1 can proceed.

### Phase 1 — Composition plan
9 scenes, 180s exactly (2.5 + 9.5 + 28 + 20 + 20 + 30 + 40 + 20 + 10), no overlap/gap.
- Hook variant locked: **Variant C (StatCascade)** — *"Four surfaces. One credit. One quiet shift."*
- CTA locked across all 3 placements: *"OpenClaw and Conductor on your plan — game changer or backdoor price hike?"*
- Retention picks: 5 markers, 7 blur-crossfade transitions, 5× `x-post` (Phase 7), 1× `macOS-notification` (Phase 5).
- Thumbnail-grade t=0: Anthropic logo + "CLAUDE PLANS GET PROGRAMMATIC CREDITS" (160px) + "JUNE 15 · 4 SURFACES · PRO / MAX / TEAM / ENTERPRISE" receipt.
- Thumbnail-grade last frame (174.5–180s, ≥5.5s static hold): topic recap + brand + CTA question.
- TTS heteronyms flagged for Phase 2a: every "live now" / "live on June 15" → swap to `available` / `goes into effect`; `claude -p` → "claude dash P"; SDK/CLI/IDE → spaced letters.
- No unresolved constraint conflicts.

### Phase 2.5 — Critique
SKIPPED per user instruction. ARTICLE_RESPONSE source-grounding already enforces fact integrity upstream.

### Phase 2b — Fact-check
SKIPPED per user instruction. All claims traceable to tmp/source.md by construction (ARTICLE_RESPONSE mode).

### Phase 2 — Script
~497 words across 9 scenes (WPM 165.6, inside news-explainer 160–170 band).
- Scene 2 opens with hook variant C verbatim: "Four surfaces. One credit. One quiet shift."
- CTA (Scene 9, spoken): "So — OpenClaw and Conductor on your plan. Game changer, or backdoor price hike? Drop your pick below, and subscribe for more Claude news."
- Banned-phrase scan: PASS.
- Connectors: 10 usages / 6 unique types (well above news-explainer Pass 6 ≥3/≥2).
- Direct-address sentences: 5 (Pass 6 ≥1 met).
- "live"-as-adjective: 0 instances (heteronym risk eliminated at write time via "goes into effect" / "runs through" / "already applied").
- Lines dropped for source-grounding: 6PM PDT cutover detail, "Codex effect" quote, "ralph loop + Linear" constructive ask.
- 10 heteronyms / tech-term pronunciation items flagged for Phase 2a (SDK / IDE / CLI spacing, OpenClaw probe).

### Phase 2a — TTS script
9 per-scene files + flat `script.txt` (3,204 chars / 568 words, 8 blank-line-separated paragraphs).
- Scene 01 is intentionally silent (thumbnail open, no narration).
- Longest scene 591 chars (well under 800-char ElevenLabs chunking watermark).
- Swaps applied: SDK×3, API×2, CLI×1, IDE×1, claude -p×1, URL phonetic spell-out×1.
- Heteronym audit clean: 0× "live"-as-adj, 1× "lead" (verb-sense, context-safe).
- OpenClaw kept as one word — probe-test after TTS, fallback "Open Claw" if engine slurs.

### Step A — TTS + transcribe
ElevenLabs (eleven_multilingual_v2, voice 7kXNOCqiaLdszL0OEXks, speed 1.13× via ELEVENLABS_SPEED_SHORTS) generated narration.wav.
- Duration: **212.69s** (planned 180s — script came ~33s long; will retime composition to audio, or ffmpeg-speedup MP4 post-render per .claude/rules/video-speedup.md).
- 34 chunks generated, all clean.
- transcript.json: 569 words with word-level start/end timings, last word at t=212.07s.
- No separate transcribe step needed — ElevenLabs response already includes word timings.
- Pronunciation dictionary AhK3J8mZDRoShxfoJLk6 applied automatically.

### Phase 3.5 — Retention strategy
Retimed to actual narration. Total composition: **216.5s** (+2.5s silent head pad, narration 212.69s, +1.49s terminal thumbnail hold). Recommend bumping to 216.6s for clean ≥1.5s hold.
- Scene boundaries (data_start / data_duration):
  - 01 silent-open: 0.0 / 2.5
  - 02 four-surfaces: 2.5 / 18.4
  - 03 the-shift: 20.9 / 34.5
  - 04 who-gets-it: 55.4 / 20.0
  - 05 timeline: 75.4 / 24.1
  - 06 bonus-stack: 99.5 / 33.0
  - 07 reactions-montage: 132.5 / 41.1
  - 08 big-question: 173.6 / 32.4
  - 09 thumbnail-close: 206.0 / 10.5
- 23 retention picks total. 2 registry blocks (`macOS-notification` scene 5, `x-post` ×5 scene 7). 9 primitive idioms.
- 7 cinematic-whoosh SFX (every phase transition).
- 6 visual-pacing-5s gaps detected → all resolved (added scale-pulse beats).
- 5 community reaction cards: @cardholder (positive), @oldschool (critical), @cynicop (critical), @builderx (positive), @skeptic42 (confused).
- Thumbnail-grade audit: first frame PASS, last frame PASS.
- Build-time action for Phase 4: `ffmpeg ... adelay=2500|2500` to pad narration.wav 2.5s.

### Phase 4 — Composition build
`index.html` (842 lines) built end-to-end. 9 phases via Anthropic phase-mutex (no sub-comps).
- Audio handling: `<audio data-start="2.5" data-duration="213">` — silent visual open precedes narration; WAV unchanged, transcript timings remain valid (raw + 2.5 = composition-time).
- Lint: **0 errors, 2 warnings** (duplicate logo SVG used in top-banner + phase9 — same file, low priority; composition_file_too_large at 842 lines — acceptable for 9-phase 216s short).
- Inspect: **0 layout issues** across 9 samples.
- Composition duration: 216.5s ✓ via `hyperframes compositions`.
- SFX: 7× cinematic-whoosh at every phase transition (fire at sceneT, duration 1.5s, vol 0.11) + 1× scale-slam at counter peak (105.94s, discretionary).
- Retention picks all installed. Both `x-post` and `macos-notification` registry blocks were landscape 1920×1080 — incompatible with vertical mutex; hand-rolled equivalent cards inline instead.
- Hidden-until-reveal pattern (tl.set + tl.to) applied to every enumerated list.
- CTA verbatim across plan/script/on-screen: "OpenClaw + Conductor on your plan — game changer or backdoor price hike?"
- Phase1 receipt line shortened from "PRO / MAX / TEAM / ENTERPRISE" to "4 PAID PLANS" to fit 1080px canvas (full list still appears in Phase 4 pill row).

### Phase YT — YouTube description
`youtube-description.md` + `research/vidiq-keywords.md` written.
- vidIQ top picks: `claude code` (75.6), `claude vs codex` (73.6), `claude usage limits` (71.0). Niche wins: `claude pricing` (73.1, comp 14), `conductor claude` (62.8, comp 32.1).
- 6 chapters (consolidated from 9 phases per 4–7 rule, speed_factor=1.0): 0:00 / 0:21 / 0:55 / 1:40 / 2:13 / 2:54.
- 20 hashtags (within 15–25 band).
- 4 URLs validated: support.claude.com article ✓, claude.com/claude-code ✓, anthropic.com/news ✓, x.com/ClaudeDevs (kept — 402 paywall on unauth fetch, but canonical handle from source).
- Dynamous CTA block skipped (`meta.json` lacks `dynamousPromotion: true`).
- CTA cross-check PASS: spoken + on-screen `#p9-cta-question` + description closer all reference the same Scene 3 third-party claim with same binary debate framing.

### Step Z — Preview
Studio running at http://localhost:3005 (port 3002 was in use). Composition compiled with deterministic font injection; non-blocking notice about `var(--mono)` / `var(--sans)` mapping (template tokens resolve at runtime).
