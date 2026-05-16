---
name: diy-yt-creator
description: Use when the user wants to create a new YouTube video using one of the templates in this repo's templates/ folder. Spawns the project folder, drafts the script from a topic, generates TTS, fills the composition with real content sync'd to word-level timestamps, lints + inspects, and opens preview. Never auto-renders.
---

# diy-yt-creator

Zero-manual-step workflows for spawning fully-prepped HyperFrames videos from the templates in `templates/`.

## When to invoke

Trigger when the user says any of:

- "create / make / spawn a new short / video"
- "new short about X" / "new generic short about X" / "new standard short about X"
- "/diy-yt-creator:new-standard-short …"
- "new editorial short about X" / "deep-explainer short" / "single-accent short" / "warm editorial short" / "spec / standard / protocol overview short"
- "/diy-yt-creator:new-editorial-short …"
- "new anthropic short about X"
- "/diy-yt-creator:new-anthropic-short …"
- "new archon short about X"
- "/diy-yt-creator:new-archon-short …"
- "new google short about X" / "google brand short" / "gemini short" / "workspace short" / "android short" / "google ai short"
- "/diy-yt-creator:new-google-short …"
- "new openai short about X" / "openai brand short" / "chatgpt short" / "gpt short" / "gpt-5 short" / "sora short" / "dall·e short" / "codex short"
- "/diy-yt-creator:new-openai-short …"
- "new game-map short about X" / "game map short" / "tour short" / "hub and spoke short" / "six things short" / "X things short with camera transitions"
- "/diy-yt-creator:new-game-map-short …"
- "new long-form video about X" / "new long-form standard about X"
- "/diy-yt-creator:new-long-form-standard …"
- "new anthropic long-form about X" / "anthropic branded long-form" / "long-form about claude / anthropic blog post" / "article-response long-form about an anthropic.com / claude.com post"
- "/diy-yt-creator:new-long-form-anthropic …"
- "new dynamous long-form about X" / "dynamous slides about X" / "cole-style workshop about X" / "dynamous workshop video about X" / "deep-navy dynamous long-form" / "long-form about an ai-coding workshop topic"
- "/diy-yt-creator:new-long-form-dynamous-slides …"
- "new screencap dubbed video" / "new screen recording video" / "dub my screen recording" / "ai voice over my recording" / "i recorded a walkthrough and want an ai voice on it" / "long-form screencap dubbed about X" / "i don't want my real voice in the video"
- "/diy-yt-creator:new-long-form-screencap-dubbed …"
- "new claude code version update video" / "claude code release video"
- "/diy-yt-creator:claude-code-version v2.1.NN" — orchestration command for Claude Code releases
- "new claude code version short" / "claude code release short" / "short cut of claude code v2.1.NN"
- "new hostinger sponsored video" / "hostinger sponsored about X" / "hostinger × X sponsored ad" / "hostinger affiliate tutorial" / "1-click deploy tutorial" / "hostinger sponsorship video about X"
- "/diy-yt-creator:new-hostinger-sponsored …"
- Anything that asks to scaffold a video from a template in this repo
- "capture / screenshot <url> for video <slug>" → uses `capture-asset`
- "QA / check / verify the preview for <slug>" → uses `qa-composition`
- "review my video / video review / production review / audit video / is the video ready to publish" → uses the top-level `video-review` skill (5 parallel agents covering timing, render, layout, content, metadata)
- "use my voice" / "migrate to my voice" / "switch to cloned voice" / "regenerate narration with my voice" → uses `use-cloned-voice`

## Available commands

### Composition-build commands (template-specific HTML edit)

| Command | Template used | Use when |
|---|---|---|
| [new-standard-short.md](./new-standard-short.md) | `templates/shorts/standard/` | User wants a vertical YouTube Short (1080x1920, 30fps, ~24-180s) in the **brand-neutral standard** aesthetic. Default pick for any topic that isn't anchored to a specific brand. Numbered step cards (01/02/03) instead of dated timeline cards. |
| [new-editorial-short.md](./new-editorial-short.md) | `templates/shorts/editorial/` | User wants a vertical YouTube Short (1080x1920, 30fps, ~60-180s) in the **editorial-light single-accent** aesthetic — warm cream + Source Serif 4 italic + single terracotta accent. Best for deep-explainer overviews of a spec / standard / open protocol, essay-style "what is X and why" deep-dives, cross-tool comparisons, companion Shorts to long-form on the same topic. Same sub-composition architecture as `standard` (15 scene archetypes) but with editorial restraint (one lead accent per scene, no rainbow). |
| [new-anthropic-short.md](./new-anthropic-short.md) | `templates/shorts/anthropic/` | User wants a vertical YouTube Short (1080x1920, 30fps, ~24-60s) in the Anthropic dark-stage aesthetic |
| [new-archon-short.md](./new-archon-short.md) | `templates/shorts/archon/` | User wants a vertical YouTube Short (1080x1920, 30fps, ~24-60s) in the Archon dark-blue / cyan-magenta aesthetic |
| [new-google-short.md](./new-google-short.md) | `templates/shorts/google/` | User wants a vertical YouTube Short (1080x1920, 30fps, 70-130s) in the **Google brand cinematic-stage** aesthetic (canonical four-color rotation, Google logo, 5-dot SETUP→PUBLISH progress rail). Three theme variants (`cinematic` / `spotlight` / `editorial`) and four accent options (blue / red / yellow / green) match the source design's tweaks-panel knobs. **Dynamous promotion ON by default** — badge + module interstitial + 10% OFF bubble all enabled in `video.config.js`. |
| [new-openai-short.md](./new-openai-short.md) | `templates/shorts/openai/` | User wants a vertical YouTube Short (1080x1920, 30fps, 70-130s) in the **OpenAI monochrome-editorial** aesthetic (single ChatGPT-mint accent `#10A37F` on off-black `#0A0A0A`, ChatGPT spirograph top-center with OpenAI-wordmark swap option, 5-dot INTRO→CTA single-accent progress rail). Three theme variants (`quiet` / `cinematic` / `editorial`) and four accent options (mint / lavender for Sora / amber for DALL·E / coral for warnings). **Dynamous promotion ON by default** — badge + 10% OFF bubble + endcard enabled in `video.config.js`. Authored as a tight delta from new-google-short. |
| [new-game-map-short.md](./new-game-map-short.md) | `templates/shorts/game-map/` | User wants a vertical YouTube Short (1080x1920, 30fps, 30-60s) using the **camera-driven hub-and-spoke** structural pattern — a single GSAP camera pans + zooms across one giant world canvas with 7 sections (1 hub + 6 hex spokes) instead of phase-mutex crossfades. Reuses Anthropic-dark palette + typography. Best fit: "X things you missed", feature roundups, tour videos, list-format content where the journey metaphor carries the script. Final pull-back to map view with all nodes lit becomes the thumbnail-grade completion screen. |
| [new-long-form-standard.md](./new-long-form-standard.md) | `templates/long-form/standard/` | User wants a horizontal YouTube long-form (1920x1080, 30fps, 4-15 min) in the dark-navy + 4-accent baseline aesthetic |
| [new-long-form-anthropic.md](./new-long-form-anthropic.md) | `templates/long-form/anthropic/` | User wants a horizontal YouTube long-form (1920x1080, 30fps, 4-10 min) in the **Anthropic dark-stage** aesthetic — Claude orange leads, purple/blue/green rotate, warm off-white type on `#0B0F18`. Ships 12 scene archetypes including the **signature `scene-image-3d-reveal`** (perspective + rotateY entrance for blog screenshots / source figures), `scene-list-cards`, `scene-quote-card`, `scene-dynamous-midroll`, `scene-subscribe-banner`. Best for Anthropic / Claude article responses, "how it works" explainers, multi-figure deep dives that need 4–10 min to breathe. |
| [new-long-form-dynamous-slides.md](./new-long-form-dynamous-slides.md) | `templates/long-form/dynamous-slides/` | User wants a horizontal Dynamous-branded long-form (1920x1080, 30fps, 2-15 min) in the **classic Dynamous deep-navy + blue workshop deck** aesthetic — `#07090F` near-black + Dynamous Blue `#3B82F6` hero + Cyan `#0EA5E9` halo (NO PURPLE) + Montserrat 300/800 weight-contrast + JetBrains Mono mono-bar eyebrows. 8 scene archetypes: hook-wordmark (character-stagger hero + flame mark), headline-accent (Dynamous-Blue underline sweep), big-stat (counter ramp + gradient text), tension-pivot (300/800 weight-contrast headline), pillars-3 (step-by-step 3-card reveal), list-reveal (6-row enumerated + marker sweeps), quote-card (line-by-line + author chip), cta (logo lockup + debate question + comment/subscribe pills). Best for Dynamous workshops, Cole Medin episodes, AI-coding deep-dives, "scaling X" or "strategies for Y" workshop content. |
| [new-long-form-screencap-dubbed.md](./new-long-form-screencap-dubbed.md) | `templates/long-form/screencap-dubbed/` | User has an **existing screen recording with their own voice** and wants an **AI dub** over it — the user's voice is transcribed, lightly cleaned (filler + heteronym + tech-term audit), and TTS-regenerated so natural pacing is preserved while the published audio is AI-voice only. 3-scene flow: `title` → full-bleed `screencap` (muted `<video>`) → `cta` (debate question). **Recording-driven entry path** — uses [`phase0-ingest-recording`](../../commands/diy-yt-creator/phase0-ingest-recording.md), [`phase2-script-from-transcript`](../../commands/diy-yt-creator/phase2-script-from-transcript.md), and [`phase-sync-check`](../../commands/diy-yt-creator/phase-sync-check.md) instead of the topic-driven research+plan+script chain. Best for signup walkthroughs, app tours, settings demos, or any "real screen interaction + I don't want my voice published" case. |
| [new-claude-code-version-longform.md](./new-claude-code-version-longform.md) | `templates/long-form/claude-code-version/` | User wants a horizontal Claude Code release-update video (1920x1080, 30fps, 3-5 min) with VersionBranding overlay + terminal scene + stats opener. For full automation from a release tag, prefer the [/diy-yt-creator:claude-code-version](../../commands/diy-yt-creator/claude-code-version.md) slash command. |
| [new-claude-code-version-short.md](./new-claude-code-version-short.md) | `templates/shorts/claude-code-version/` | User wants a vertical Claude Code release-update Short (1080x1920, 30fps, ≤3 min — target 70-130s) with VersionBranding overlay + version slam + 3-pill stats opener + numbered highlight cards + `$ claude update` terminal CTA. **Reuses an existing long-form video's content brief if one already exists for the same release** (avoids duplicate WebFetch and keeps stats / highlights consistent across cuts). |
| [new-hostinger-sponsored.md](./new-hostinger-sponsored.md) | `templates/long-form/hostinger-sponsored/` | User wants a horizontal **Hostinger sponsorship tutorial** (1920x1080, 30fps, 53.5s) following Hostinger's brief cadence — hook → brand → why automate → why Hostinger → landing page → plan comparison → pricing/term → cart + coupon → setup steps → AI provider → channel selection → workflow demo → feature spotlight → CTA. Single-file composition (no sub-compositions), 14 inline scenes, one `cinematic-zoom` shader at the climax. Find/replace tokens for product name, affiliate URL, coupon code, plan prices, cart math, hero stat. Reusable across Hostinger creator deals (OpenClaw, Coolify, Plesk add-ons, etc.). **Tracking link + coupon code are mandatory mentions per Hostinger sponsorship policy.** |
| [capture-asset.md](./capture-asset.md) | n/a (uses `agent-browser`) | Per-video screenshot/asset from a public URL into `videos/<slug>/assets/` |
| [qa-composition.md](./qa-composition.md) | n/a (uses `agent-browser`) | Visually QA a running `hyperframes preview` — snapshot each phase, report issues |
| [use-cloned-voice.md](./use-cloned-voice.md) | n/a (uses `scripts/elevenlabs-tts.py`) | Migrate an existing video (or new video) from a stock voice to the user's ElevenLabs cloned voice: update `.env`, regenerate narration, rebuild `transcript.json`, re-wire all scene `data-start` values + SFX timing, re-render |

> **Adding a new template?** Follow the "Building New Templates" workflow in the project's [CLAUDE.md](../../../CLAUDE.md). Each new template MUST ship a matching playbook in this directory and a row in the table above.

### Pipeline commands (research + scriptwriting + retention)

These are first-class slash commands under `.claude/commands/diy-yt-creator/`. They produce the research, script, and retention artifacts that feed the composition-build step.

| Command | Use when |
|---|---|
| [/diy-yt-creator:full-auto](../../commands/diy-yt-creator/full-auto.md) | End-to-end pipeline from topic to retention-engineered script + per-scene retention strategy. Stops twice for human review (TTS, composition build). Use this by default. |
| [/diy-yt-creator:phase0-research](../../commands/diy-yt-creator/phase0-research.md) | Topic research only (vidiq + web search + 4 parallel agents → `videos/<slug>/research/content-brief.md`) |
| [/diy-yt-creator:phase1-plan](../../commands/diy-yt-creator/phase1-plan.md) | Composition plan (after Phase 0) — scenes, hook variants, retention component picks, `data-start`/`data-duration` budget |
| [/diy-yt-creator:phase2-script](../../commands/diy-yt-creator/phase2-script.md) | Draft narration script (after Phase 1) |
| [/diy-yt-creator:phase2-5-critique](../../commands/diy-yt-creator/phase2-5-critique.md) | Quality gate on script (after Phase 2) — hook score, story arc, banned phrases |
| [/diy-yt-creator:phase2a-tts-script](../../commands/diy-yt-creator/phase2a-tts-script.md) | TTS-optimize script + write flat `script.txt` (after Phase 2.5) |
| [/diy-yt-creator:phase2b-factcheck](../../commands/diy-yt-creator/phase2b-factcheck.md) | Fact-check claims via WebSearch (after Phase 2a) |
| [/diy-yt-creator:phase3-5-retention](../../commands/diy-yt-creator/phase3-5-retention.md) | Per-scene retention strategy from `transcript.json` (after `npx hyperframes transcribe` runs) |
| [/diy-yt-creator:brief-template](../../commands/diy-yt-creator/brief-template.md) | Reference for the structured-brief input format |
| [/diy-yt-creator:phase0-ingest-recording](../../commands/diy-yt-creator/phase0-ingest-recording.md) | **screencap-dubbed only**: Ingest an existing screen recording, extract Whisper-ready audio, transcribe with word-level timestamps. Replaces Phase 0 / Phase 1 for the [`new-long-form-screencap-dubbed`](./new-long-form-screencap-dubbed.md) playbook. |
| [/diy-yt-creator:phase2-script-from-transcript](../../commands/diy-yt-creator/phase2-script-from-transcript.md) | **screencap-dubbed only**: Convert the source transcript into a minimally-edited `script.txt` (strip fillers, fix flubs, heteronym + tech-term audit). Word-count delta capped at ±15% to preserve dub sync. |
| [/diy-yt-creator:phase-sync-check](../../commands/diy-yt-creator/phase-sync-check.md) | **screencap-dubbed only**: After TTS, compare source vs new transcript at sentence boundaries, report per-sentence drift, recommend speed-adjust (if uniform) or segment-warp (if variable). Run before composition wiring. |

## Pipeline vs direct invocation

- **Use `/diy-yt-creator:full-auto`** when the user gives you a topic and wants a researched, fact-checked, retention-engineered video. This is the default.
- **Use `/diy-yt-creator:new-standard-short`, `new-anthropic-short`, or `new-archon-short` directly** when the user already has a finished `script.txt` (or content brief) and just wants the composition built. Skips all research/critique/fact-check steps. Pick the playbook by aesthetic: **standard** brand-neutral dark-navy (default for any topic) vs **anthropic** dark-orange stage (Anthropic / Claude content) vs **archon** dark-blue / cyan-magenta (Archon workflow content).
- **Use individual phase commands** when debugging or re-running a single phase after fixes.

Both composition-build skills (`new-anthropic-short.md`, `new-archon-short.md`) read `videos/<slug>/scripts/full-script.md` and `videos/<slug>/plan.md` if they exist (Branch A in step 4) — so the pipeline output flows naturally into the build, regardless of template choice.

## Hard rules across every command

1. **Never auto-render.** Every workflow ends at `npx hyperframes preview videos/<slug>`. The user always triggers `npx hyperframes render` manually.
2. **Never fabricate facts.** Stats, dates, URLs, quotes must come from a source the user provides or that exists on the open web. If the topic has no source, ASK before drafting.
3. **Never modify the template itself.** Only edit the copy under `videos/<slug>/`.
4. **Never bundle multiple videos in one run.** One slug = one invocation.
5. **Always lint + inspect before reporting done.** Both must pass cleanly.
6. **Always invoke the `/hyperframes` skill** before editing any composition HTML — it has framework-specific rules (timeline registration, phase mutex, `data-*` semantics) that this skill assumes.
7. **Always run the font-var render-blocker check** after lint passes — per [`.claude/rules/hyperframes-pitfalls.md`](../../rules/hyperframes-pitfalls.md) §8. Lint + inspect both pass cleanly when scenes use `font-family: var(--sans|--mono)`, but render fails with `[Compiler] No deterministic font mapping for: var(--mono), var(--sans)`. Most templates inherit this latent bug. Mandatory grep + fix before declaring done:
   ```bash
   grep -rE "font-family:\s*var\(--(sans|mono)" videos/<slug>/ && echo BLOCKER || echo SAFE
   # If BLOCKER, apply sed fix from pitfalls §8 BEFORE preview/render.
   ```

Open the relevant command file for the full playbook.
