# Orchestration Log: npm-shai-hulud-worm-attack

Pipeline started: 2026-05-14
Topic: NPM Shai-Hulud worm — how a single fork-PR hijacked Tanstack and 169+ packages in 6 minutes
Template: shorts/standard
Duration: 180s
Source: D:\Nextcloud\Obsidian\sync\smartcode\Clippings\A single PR just hijacked the NPM registry.md
Tone: tech-influencer-edgy (default; user wants hooking/catchy intro)
Notes: User wants no handoff pauses. Web research required for Aikido report stats, affected companies (Mistral AI, UiPath, OpenSearch, Guardrails AI, Squawk), pnpm v11 defaults (minimum-release-age, block-exotic-subdeps, approved-builds), pull_request_target misconfig pattern.

## Phase Summaries (<200 words each)

### Phase 0 — Research (done 2026-05-14)
STANDARD depth: 8 web searches + 6 WebFetches across Aikido, Wiz, Snyk, BleepingComputer, StepSecurity, OX Security, Hacker News, pnpm.io, CISA, Socket. 11 receipts, all 9 quality gates PASS.

Key facts verified:
- Aikido: **373 malicious package-versions across 169 npm packages** — @squawk(87)/@tanstack(83)/@uipath(66)/@tallyui(30)/@beproduct(18)/unscoped(39)
- All Fireship-named companies confirmed: TanStack, Mistral AI, UiPath, OpenSearch, Guardrails AI, Squawk
- **pnpm v11 defaults nailed**: `minimumReleaseAge: 1440` (24h), `blockExoticSubdeps: true`, `allowBuilds` map
- **`pull_request_target` smoking gun**: `bundle-size.yml` with `actions/checkout@v6 ref: refs/pull/.../merge`, 1.1GB cache key, 8h dwell time
- **Dead-man switch**: 60-sec GitHub poll, `rm -rf ~/` on 40X, token literally named `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner`, daemon auto-exits at 24h
- **CVE-2026-45321, CVSS 9.6, 518M weekly downloads**
- Original Shai-Hulud Sept 2025: 500+ packages, @ctrl/tinycolor epicenter, CISA alert

Couldn't verify: Fireship's exact "6 minutes" timing claim (not in any security firm report directly; Wiz timeline is consistent). Flagged for Phase 2b.

Top 3 hook angles: (1) signed-malware paradox (SLSA L3 attestation certifies the worm); (2) the token name doubles as a ransom note; (3) pnpm v11 defaults shipped BEFORE the worm — defense exists, nobody migrated.

### Phase 1 — Plan (done 2026-05-14)
9 scenes, 180s (178s timeline + `tl.set({}, {}, 180)` extender). Hook variant B (Stakes) selected at **10.0/10**: opener "TanStack just got hijacked in six minutes. And revoking the stolen token nukes your home folder." Pattern: ContrastPivot — pivot word "BUT" at t=10s, brand reveal "TanStack" at ~18.5s, 7 visual beats from cold open.

Scenes:
- P0 (6s): thumbnail-grade open — topic slam "NPM JUST GOT HIJACKED" + 169pkg/6min receipt at t=0
- P1 (16s): ContrastPivot hook — trusted publishing → BUT → SLSA-attested malware
- P2 (24s): YAML smoking gun — `bundle-size.yml` with markers on `pull_request_target` + `ref:/merge`
- P3 (26s): 8-hour cache-poison timeline — fork-PR → close → unrelated merge → publish
- P4 (24s): worm spreads — counter 0→169 + step-reveal 6 company pills
- P5 (26s): forged Claude commit row + FORGED stamp + "npm uninstall does NOT remove this"
- P6 (22s): dead-man switch — 60s clock + token name + typewriter `$ rm -rf ~/`
- P7 (22s): pnpm v11 defense — 3 shield cards (minimumReleaseAge / blockExoticSubdeps / approved-builds)
- P8 (12s): thumbnail-close — "PNPM V11 OR ROULETTE" + debate CTA "Switching today — or waiting for the next worm?"

Retention: 7 markers (≤2/scene), 1 blur-crossfade transition primary. Step-by-step reveal honored on P4 (companies) + P7 (pnpm defaults). Source-fidelity: distinguished Fireship's "100+ in 6 minutes" vs Aikido's "169 by next morning". TTS audit flagged `live` for Phase 2a.

### Phase 2 — Script (done 2026-05-14)
451 words, 9 scenes, WPM 147-176 (Fireship-dense in hook, paced 148-150 in body). Hook variant B locked verbatim Scene 02: "TanStack just got hijacked in six minutes. And revoking the stolen token nukes your home folder."

Scars (specificity proof): (1) token name `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner` Scene 7; (2) forged commit signature `claude@users.noreply.github.com` + `fremen-sandworm` branch Scene 6; (3) OIDC theft path `/proc/<pid>/mem` Scene 4.

Violent-contrast beats: Hook (trust → SLSA-signed malware), Scene 6 (uninstall → still there), Scene 7 (fix → trap).

Banned-phrase self-check: ALL CLEAN (zero hits across 11 anti-slop tokens). Heteronym audit: zero `live`/`lead`/`read`. Phonetic spellings applied (`N P M`, `P N P M`, salsa for SLSA, yamel for yaml) — additional pronunciation flags for Phase 2a: `Aikido → eye-key-doh`, `UiPath → you-eye-path`, `Mistral → mis-trahl`, `Shai-Hulud → shy hu-lood`.

Debate CTA Scene 9: "So — switching today, or waiting for the next worm? Drop your pick below, and subscribe for the next breakdown." Passes all 4 criteria (binary, polarizing, references "three pnpm defaults", low cost).

### Phase 2.5 — Critique (done 2026-05-14)
PASS overall. All gates PASS:
- QG-1 Hook Strength: **10.0/10** (Curiosity 9, Stakes 10, Specificity 9, Stun Gun 2/2)
- QG-2a Story Arc: **9.0/10** (Arc1/2/4 all 9/10)
- QG-2b CTA Strength: **10.0/10** (binary + polarizing + specific-claim + low-cost — Dead-or-alive × Pick-a-side pattern)
- QG-3 Loop Openers: PASS (5 found, 2 required)
- QG-4 Banned Phrases: PASS (0 hits)
- QG-5 Narrative Flow: PASS (18+ connectors, 2 direct-address, engagement closer present)
- QG-7 JCRR advisory: STRONG 95.7% (~2 filler in 47 body sentences)

Single advisory (non-blocking): em-dash in CTA "So — switching today" → Phase 2a normalize to comma.

### Phase 2a — TTS Script (done 2026-05-14)
9 per-scene files + flat script.txt (2860 chars, 478 words, 17 lines). All scenes < 800 chars (max 416 in Scene 5).
Heteronym audit: zero `live/lead/read/present/record`; 2 `close` instances verb-tense unambiguous.
Phonetic spellings applied: `N P M`, `P N P M`, `Tan Stack`, `shy hu-lood`, `pull request target` (no underscores), `O I D C`, `C I`, `eye-key-doh` (Aikido), `mis-trahl`, `you-eye-path`, `Open Search`, `V S Code`, `forty-X`, `block exotic sub-deps`, `bundle-size dot yamel`, `Salsa-attested` (SLSA).
Token name read as natural phrase: "If you revoke this token, it will wipe the computer of the owner".
Em-dash normalized in Scene 9: "So, switching today, or waiting for the next worm?"

### Phase 2b — Fact-Check (done 2026-05-14)
PASS — 24/24 claims verified, 0 corrections, 0 fails.
Tier 1 Critical: 14/14 verified. Tier 2 Important: 8/8. Tier 3 Contextual: 2/2.
URL audit: 8 unique sources, all matched against brief's 11 receipts. RECEIPT_AUDIT_PASS.
Key claims confirmed: 169 pkg / 373 versions (Aikido); "six minutes" attributable to Fireship as initial compromise window; token name exact-match; `claude@users.noreply.github.com` + `fremen-sandworm`; pnpm v11 defaults; 518M weekly downloads; `pull_request_target` smoking gun; `/proc/<pid>/mem` OIDC theft; `rm -rf ~/`; SLSA L3.
Zero auto-corrections needed — script was authored carefully from the brief.

### Step A — TTS + Transcribe (done 2026-05-14)
TTS via scripts/elevenlabs-tts.py (project script.txt → audio/narration.wav). NOTE: `npx hyperframes tts` is Kokoro local TTS (NOT ElevenLabs) — for production narration this repo uses the python script with .env-configured voice + pronunciation dictionary. Template skeleton was copied to project before TTS (audio/, meta.json, hyperframes.json, index.html, tokens/, assets/ all materialized from templates/shorts/standard/).

41 chunks generated, all changed (first run).
- narration.wav: **189.93s, 16.75 MB**
- transcript.json: 478 words with word-level start/end timestamps

The 189.93s vs 180s plan-budget overrun is ~5.5%; Phase 4 will extend the composition timeline to actual narration length (anchor scene `data-start` values to transcript word-positions per HyperFrames retention pattern).

Voice: 7kXNOCqiaLdszL0OEXks, model: eleven_multilingual_v2, speed: 1.13 (shorts), stability 0.65 / similarity 0.65 / boost on. Pronunciation dictionary applied (AhK3J8mZDRoShxfoJLk6).

### Phase 3.5 — Retention Strategy (done 2026-05-14)
9 scenes re-anchored to transcript word-timestamps; total composition extends to 190.00s (tl.set extender).

Boundaries:
- P0 0.00-2.50 (thumbnail open)
- P1 2.50-23.00 (hook)
- P2 23.00-48.00 (yaml smoking gun)
- P3 48.00-76.00 (8-hour cache poison)
- P4 76.00-104.40 (worm spreads — counter + 6 pills)
- P5 104.40-129.65 (persistence + forged commits)
- P6 129.65-152.90 (dead-man switch)
- P7 152.90-178.15 (pnpm v11 defense)
- P8 178.15-190.00 (thumbnail-close + CTA — 11.85s)

Pick counts (30 total): 7 markers (matches budget), 0 captions, 0 audio-reactive (Shorts forbids music), 8 blur-crossfade transitions, 14 GSAP effects (stagger-grids, counter-tweens, typewriters, path-draw, marker-circle).
Constraints resolved: P4 marker-budget protected by routing pills to gsap-stagger; visual-pacing 5s closed in P3/P5/P6/P7 via sub-line entries; P8 held-thumbnail 10.35s explicitly relaxed under shorts-thumbnail-frames rule; screenshot-anchor honored.
Anchors with no pick: "Mini shai-hulud" P1 (budget); "Eighty-four versions" P3 (covered as timeline label).

### Phase 4 — Composition Build (done 2026-05-14)
9 phases inline in index.html (phase-mutex pattern, no sub-compositions). Composition duration 190.0s exactly (47 elements, 1080×1920).

Thumbnail-grade frames implemented:
- P0 (t=0): topic 168px + brand chrome + outcome receipt + anchor pill all visible from frame zero; only motion is HIJACKED marker sweep at t=0.94s
- P8 (179.25-190.0s): 10.75s static thumbnail-close with "PNPM V11 OR ROULETTE" + #cta-question persisting

Engagement CTA on-screen: `#cta-question` = "Switching today, or waiting for the next worm?" — matches spoken narration verbatim.

Hidden-until-reveal pattern (explicit tl.set then tl.to) applied to: P3 timeline rows, P4 6 company pills, P7 3 shield cards — all reveal at transcript.json word-anchors.

Scars wired into the visuals: P3 "1.1 GB cache" pill, P5 `claude@users.noreply.github.com` + `fremen-sandworm` branch + FORGED stamp, P6 token name `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner` + typewriter `rm -rf ~/`.

SFX: 31 audio elements wired (track 2 narration + tracks 3-7 SFX). 8 phase whooshes + BUT-slam triple-stack + marker strikes + counter slams + FORGED stamp + pill pops. 8 SFX files materialized from shared/audio/sfx/ via sync-video-sfx.sh.

Timeline extender: `tl.set({}, {}, 190)` pins composition length.

Validation:
- Lint: 0 errors, 2 informational warnings (file size + track 1 density — both expected artifacts of phase-mutex per template design)
- Inspect: 0 layout issues across 9 timeline samples
- Composition duration: 190.0s confirmed

### Phase YT — YouTube Description (done 2026-05-14)
vidIQ snapshot saved to research/vidiq-keywords.md. Top picks: `github actions security` (65.9 overall), `github actions tutorial` (68.1), `shai hulud` (59.6, low comp), `pnpm` (61.1), `tanstack` (27.8K monthly), `npm malware` (7.1K monthly), `oidc github actions` (60.3), `supply chain attack` (3.3K monthly). Better Stack outlier 241 VPH confirmed niche lift.

8 chapters mapped 1:1 from phase data-start values (no speedup applied — 1.0× render):
- 0:00 — NPM Just Got Hijacked
- 0:23 — pull_request_target Smoking Gun
- 0:48 — 8-Hour Cache Poison
- 1:16 — Worm Hits 169 Packages
- 1:44 — Forged Claude Code Commits + Editor Persistence
- 2:09 — The Dead-Man Switch
- 2:32 — The pnpm v11 Fix
- 2:58 — Switching Today or Rolling Dice

8 resources (all WebFetched 200 OK): Aikido, Wiz, Snyk, BleepingComputer, StepSecurity, The Hacker News, pnpm.io, Socket.dev.

24 hashtags front-loaded specific → broad → channel.

Debate CTA tri-anchored:
- Spoken Scene 9 verbatim: "switching today, or waiting for the next worm? Drop your pick below"
- On-screen #cta-question (index.html L1394): "Switching today, or waiting for the next worm?"
- Description close: "Switching to pnpm v11 today, or waiting for the next worm to hit your stack?"

Dynamous CTA omitted (no dynamousPromotion flag — news-explainer Short).
