# Feature: Port Remotion `audio-design.md` SFX System to HyperFrames

## Summary

Port the SFX/audio-design rule set from the old Remotion `diy-yt-creator` project into this HyperFrames repo. The Remotion version was framework-coupled (`<Audio volume={0.15} />` inside `<Sequence>`, frame-based timing, `interpolate()` volume curves). HyperFrames is HTML-native: each SFX is a separate `<audio>` element with `data-start`/`data-duration`/`data-track-index`/`data-volume`. The mechanism is already documented in `templates/shorts/anthropic/README.md` and `DESIGN.md`, but **zero SFX files exist** and **no pipeline step generates or wires them**. This plan fills that gap with: (1) a canonical `audio-design.md` rule file adapted for HyperFrames syntax, (2) a `shared/audio/sfx/` library of generated cues, (3) a Python generator script that batch-creates SFX via ElevenLabs, (4) a sync hook that copies SFX into a video on demand, and (5) updates to the `/diy-yt-creator` pipeline so SFX placement becomes a concrete step (not a deferred human-judgment note).

## User Story

As a HyperFrames video creator using the `/diy-yt-creator` pipeline
I want SFX cues with volume-balanced presets and a simple way to wire them into compositions
So that my Shorts have the same percussive, retention-focused audio polish as the old Remotion videos — without me hand-tuning volumes, hand-picking files, or re-discovering frame-alignment rules every video.

## Problem Statement

1. The old Remotion repo had a battle-tested `audio-design.md` rule file with research-backed volume caps, an SFX volume table, beat-alignment guidance, and a "frame-aligned to visual triggers" audit rule. This knowledge is **not in this repo** — the `DESIGN.md` cue table here is a thin subset and `phase1-plan.md`'s "5C: SFX placement" only describes intent (`"impact-slam + screen-shake + glitch-zap"`) without resolving to files or volumes.
2. **No SFX `.wav`/`.mp3` files exist anywhere in the repo.** `templates/shorts/anthropic/audio/` contains only `.gitkeep`. No `videos/*/assets/sfx/` folders exist. The `sound-effects` skill exists but has never been called.
3. The `/diy-yt-creator:full-auto` orchestrator explicitly skips SFX (`full-auto.md:521-523` defers it as "creative work that benefits from human-in-the-loop judgment"). So the planned blueprint never lands as elements in `index.html`.
4. The Remotion-specific guidance (frame-based math, `interpolate()` volume curves, `<Sequence from={...}>`, beat alignment with `alignToDownbeat()`, `wordToFrame()` formulas, sonic logo `<Audio>` at frame 0) **does not translate verbatim** to HyperFrames. Copy-pasting `audio-design.md` would mislead future agents.

## Solution Statement

Three layers, in dependency order:

1. **Canonical rules file** — author `.claude/rules/audio-design.md` adapted for HyperFrames syntax (seconds-native, `<audio data-volume="...">`, `data-track-index` collision rules, no JS volume curves). Carry over: volume caps + dB cheatsheet, per-cue volume table, "no BG music on Shorts", "SFX must be aligned to visual triggers" audit rule (rewritten in seconds), the multi-segment background music pattern (long-form only, deferred).
2. **Shared SFX library** — create `shared/audio/sfx/` with a canonical set of `.mp3` files matching the cue names already documented in `DESIGN.md` (`impact-slam`, `scale-slam`, `screen-shake`, `cinematic-whoosh`, `spring-pop`, `pop`, `glitch-zap`, `sonic-logo` + a few transition variants). Generated via a Python batch script (`scripts/generate-sfx-library.py`) that calls ElevenLabs. Files are committed (so future agents don't burn API credits regenerating them).
3. **Per-video sync + pipeline integration** — a `scripts/sync-video-sfx.sh` (mirroring the existing `scripts/sync-shared-*.sh` pattern) that copies the cues a video declares from `shared/audio/sfx/` into `videos/<slug>/assets/sfx/`. Update `phase1-plan.md` and `new-anthropic-short.md` so SFX placement becomes concrete: planning resolves cue names, composition build inserts `<audio>` elements + runs the sync. Update `full-auto.md` to no longer treat SFX as a deferred handoff.

## Metadata

| Field            | Value                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| Type             | NEW_CAPABILITY (audio asset library + rules file) + ENHANCEMENT (pipeline phases, template README)                 |
| Complexity       | MEDIUM — no new framework code; coordinates existing skills + assets; main risk is matching naming/path conventions |
| Systems Affected | `.claude/rules/`, `shared/audio/`, `scripts/`, `templates/shorts/anthropic/`, `.claude/commands/diy-yt-creator/`, `.claude/skills/diy-yt-creator/`, `shared/lib/visual-styles/anthropic-dark.md` |
| Dependencies     | ElevenLabs SDK (`elevenlabs` Python pkg, already used by `scripts/elevenlabs-tts.py`), `python-dotenv` (already used), `ELEVENLABS_API_KEY` in `.env` (already required) |
| Estimated Tasks  | 11                                                                                                                 |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                              BEFORE STATE                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────┐    ║
║  │ phase1-plan│───►│ phase2a-tts  │───►│ phase3-5     │───►│ comp-build │    ║
║  │ "SFX intent│    │ narration    │    │ retention    │    │ index.html │    ║
║  │  layered.."│    │ only         │    │ visual only  │    │  ❌  no SFX│    ║
║  └────────────┘    └──────────────┘    └──────────────┘    └────────────┘    ║
║                                                                    │          ║
║                                                                    ▼          ║
║                                              ┌────────────────────────┐      ║
║                                              │ videos/<slug>/         │      ║
║                                              │  audio/narration.wav   │      ║
║                                              │  ❌ no assets/sfx/     │      ║
║                                              │  ❌ no SFX <audio> tags│      ║
║                                              └────────────────────────┘      ║
║                                                                               ║
║  USER_FLOW:  "I'd love SFX too" → user reads DESIGN.md cue table              ║
║              → user has to find/generate every sound themselves               ║
║              → user has to manually compute data-start from transcript.json   ║
║              → user has to remember volume caps every time                    ║
║                                                                               ║
║  PAIN_POINT: SFX is documented as a pattern but unimplemented end-to-end.     ║
║              Every video starts from zero on audio polish.                    ║
║                                                                               ║
║  DATA_FLOW:  plan.md (intent) → ✗ nothing → composition (no SFX)              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                               AFTER STATE                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────┐    ║
║  │ phase1-plan│───►│ phase2a-tts  │───►│ phase3-5     │───►│ comp-build │    ║
║  │ resolves   │    │ narration    │    │ retention    │    │ + SFX wire │    ║
║  │ cue→file   │    │ + transcript │    │ + SFX        │    │ + sync hook│    ║
║  │ + seconds  │    │              │    │ alignment    │    │            │    ║
║  └────────────┘    └──────────────┘    └──────────────┘    └────────────┘    ║
║                                                  │                  │         ║
║                                                  ▼                  ▼         ║
║                              ┌────────────────────────┐  ┌──────────────────┐║
║                              │ retention-strategy.md  │  │  shared/audio/   │║
║                              │  + sfx_cues:           │  │   sfx/*.mp3      │║
║                              │    - cue: impact-slam  │  │   (canonical)    │║
║                              │      anchor_word: idx  │  └────────┬─────────┘║
║                              │      start_seconds:.. │           │           ║
║                              │      track_index: 3    │  scripts/sync-video-sfx.sh
║                              │      volume: 0.20      │           │           ║
║                              └────────────────────────┘           ▼           ║
║                                                          ┌──────────────────┐║
║                                                          │ videos/<slug>/   │║
║                                                          │  assets/sfx/     │║
║                                                          │   *.mp3 (copied) │║
║                                                          │  index.html with │║
║                                                          │   ✓ <audio …>×N  │║
║                                                          └──────────────────┘║
║                                                                               ║
║  USER_FLOW:  /diy-yt-creator:full-auto → SFX cues land in retention-strategy  ║
║              → composition build runs sync-video-sfx.sh + writes <audio>      ║
║              → lint passes, preview plays narration + balanced SFX            ║
║                                                                               ║
║  VALUE_ADD:  Zero hand-tuning of volumes (presets enforce caps)               ║
║              Zero hand-picking of files (cue names resolve via library)       ║
║              No more "SFX placement is human work" — it's a pipeline step     ║
║              audio-design.md rule file rejects accidental volume regressions  ║
║                                                                               ║
║  DATA_FLOW:  plan.md → retention-strategy.md (cues+seconds+vol)               ║
║              → sync-video-sfx.sh (copies files)                               ║
║              → new-anthropic-short.md (writes <audio> elements)               ║
║              → lint validates volume cap + track-index uniqueness             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                                                        | Before                          | After                                                        | User Impact                                          |
| --------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| `.claude/rules/audio-design.md`                                 | Does not exist                  | Single source of truth for SFX volumes + Shorts-no-music     | Future agents can't drift on volume caps             |
| `shared/audio/sfx/`                                             | Does not exist                  | 8–10 canonical `.mp3` cues, committed                        | Zero-cost reuse across all videos                    |
| `scripts/generate-sfx-library.py`                               | Does not exist                  | Batch ElevenLabs generator, idempotent (skips existing)      | One-time setup; later additions are one-line edits   |
| `scripts/sync-video-sfx.sh`                                     | Does not exist                  | Copies declared cues from `shared/audio/sfx/` to a video     | Per-video assets stay self-contained (lint-safe path)|
| `templates/shorts/anthropic/index.html`                         | Comment placeholder for SFX     | Live commented-out SFX block ready to uncomment              | New videos start with a working pattern              |
| `templates/shorts/anthropic/README.md`                          | "Adding SFX" doc only           | + reference to `sync-video-sfx.sh` and `audio-design.md`     | Discovery path is one search away                    |
| `.claude/commands/diy-yt-creator/phase3-5-retention.md`         | Visual cues only                | + SFX cue table per scene with seconds + track + volume      | Plan output now includes resolvable SFX rows         |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`          | Step 8 (HTML) doesn't write SFX | Step 8 reads `retention-strategy.md sfx_cues`, writes `<audio>` elements + runs `sync-video-sfx.sh` | SFX is wired automatically                       |
| `.claude/commands/diy-yt-creator/full-auto.md` line 521-523     | "SFX placement = human work"    | "SFX wiring is automated; review preview"                    | Pipeline truly ends with a finished composition      |

---

## Mandatory Reading

**Implementation agent MUST read these files before starting:**

| Priority | File                                                                                                                                              | Lines     | Why Read This                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\rules\audio-design.md`                                                                  | all       | Source rules to port. Every section maps to either a kept-section, an adapted section, or a dropped section.        |
| P0       | `templates/shorts/anthropic/DESIGN.md`                                                                                                            | 110-125   | Existing cue table — the new rule file must subsume and extend this without contradicting volumes.                  |
| P0       | `templates/shorts/anthropic/README.md`                                                                                                            | 105-118   | Canonical SFX `<audio>` element template — pattern to MIRROR exactly                                                |
| P0       | `videos/anthropic-amazon-compute/index.html`                                                                                                      | 906-912   | Working reference for narration `<audio>` with `class="clip"` — same pattern extends to SFX                         |
| P1       | `.claude/skills/sound-effects/SKILL.md`                                                                                                           | all       | ElevenLabs `text_to_sound_effects.convert()` API — exact parameters for the generator script                        |
| P1       | `scripts/elevenlabs-tts.py`                                                                                                                       | all       | Reference impl for `.env`-loading + ElevenLabs calls + writing audio files. The new generator MIRRORS this style.   |
| P1       | `shared/lib/README.md`                                                                                                                            | 1-60      | Hard rule: `<audio src>` cannot reference `shared/` at runtime. Audio files must be copy-from. Confirms architecture.|
| P1       | `scripts/sync-shared-lib.sh`                                                                                                                      | all       | Reference impl pattern for shared→video sync hooks. The new `sync-video-sfx.sh` MIRRORS its style.                  |
| P1       | `.claude/commands/diy-yt-creator/phase1-plan.md`                                                                                                  | 338-363   | Section 5C "SFX placement" — needs to be tightened from intent-only to cue-name-resolvable                          |
| P1       | `.claude/commands/diy-yt-creator/phase3-5-retention.md`                                                                                           | all       | Per-scene retention strategy — where SFX cues with concrete seconds + track + volume must land                      |
| P1       | `.claude/skills/diy-yt-creator/new-anthropic-short.md`                                                                                            | 240-258   | Step 8/9 (HTML edit + lint) — where SFX `<audio>` elements get inserted                                             |
| P2       | `.claude/commands/diy-yt-creator/full-auto.md`                                                                                                    | 490-525   | Composition build handoff — the "SFX placement is human work" note that needs to be updated                         |
| P2       | `shared/lib/visual-styles/anthropic-dark.md`                                                                                                      | 85-100    | Duplicate cue table that must stay in sync with DESIGN.md after this work                                           |
| P2       | `videos/anthropic-amazon-compute/transcript.json`                                                                                                 | first 30 lines | Format of word-level timestamps used to anchor SFX `data-start` values                                         |

**External Documentation:** None required. ElevenLabs API surface is fully captured in `.claude/skills/sound-effects/SKILL.md`. No new libraries.

---

## Patterns to Mirror

**NARRATION_AUDIO_ELEMENT** — extends to SFX with same shape:

```html
<!-- SOURCE: videos/anthropic-amazon-compute/index.html:906-912 -->
<!-- COPY THIS PATTERN (change id, src, data-start/duration/track-index/volume): -->
<audio id="narration"
       class="clip"
       src="audio/narration.wav"
       data-start="0"
       data-duration="52.78"
       data-track-index="2"
       data-volume="1"></audio>
```

**SFX_AUDIO_ELEMENT** — the template form:

```html
<!-- SOURCE: templates/shorts/anthropic/README.md:109-115 -->
<!-- COPY THIS PATTERN: -->
<audio id="sfx-slam"
       src="assets/sfx/scale-slam.mp3"
       data-start="1.55"
       data-duration="0.9"
       data-track-index="3"
       data-volume="0.20"></audio>
```

**ELEVENLABS_PYTHON_SCRIPT** — the script style for `generate-sfx-library.py`:

```python
# SOURCE: scripts/elevenlabs-tts.py:1-50
# COPY THIS PATTERN (env loading, argparse, dotenv, output dir mkdir):
"""<one-line docstring of purpose>

Usage:
  python scripts/<name>.py <args>
"""
from __future__ import annotations
import argparse, os, sys
from pathlib import Path
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(...)
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    load_dotenv(repo_root / ".env", override=True)
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not set", file=sys.stderr)
        return 2
    client = ElevenLabs(api_key=api_key)
    # ... call client.text_to_sound_effects.convert(...)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

**SHARED_SYNC_HOOK** — pattern for `sync-video-sfx.sh`:

```bash
# SOURCE: scripts/sync-shared-lib.sh (read first 30 lines for full pattern)
# COPY THIS PATTERN (bash strict mode, repo-root resolution, idempotent copy):
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
# ... rest follows shared-lib pattern
```

**RULES_FILE_FRONTMATTER** — frontmatter format from the source:

```markdown
<!-- SOURCE: C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\rules\audio-design.md:1-6 -->
<!-- COPY THIS PATTERN (paths globs at top, descriptive H1): -->
---
paths:
  - "**/index.html"
  - "**/*.py"
---

# Audio Design Rules
```

**TASK_COMMAND_FRONTMATTER** — for `phase*-*.md` files (already exists in repo, no change needed):

```markdown
<!-- SOURCE: .claude/commands/diy-yt-creator/phase1-plan.md:1-10 -->
<!-- DO NOT CHANGE the frontmatter style; only edit body content -->
```

---

## Files to Change

| File                                                                          | Action | Justification                                                                                                |
| ----------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| `.claude/rules/audio-design.md`                                               | CREATE | Canonical SFX/audio rules for HyperFrames (adapted port of Remotion source)                                  |
| `shared/audio/`                                                               | CREATE | New top-level shared audio dir (mirrors `shared/logos/` and `shared/lib/`)                                   |
| `shared/audio/sfx/*.mp3`                                                      | CREATE | 8–10 canonical SFX files generated once and committed                                                        |
| `shared/audio/README.md`                                                      | CREATE | Catalog + consumption rules (must be copied, not referenced)                                                 |
| `shared/audio/MANIFEST.md`                                                    | CREATE | One-line-per-file registry (cue name, file, default volume, recommended use)                                 |
| `scripts/generate-sfx-library.py`                                             | CREATE | Batch ElevenLabs generator: reads cue specs, writes to `shared/audio/sfx/`, idempotent (skips existing)      |
| `scripts/sync-video-sfx.sh`                                                   | CREATE | Copies declared cues from `shared/audio/sfx/` into `videos/<slug>/assets/sfx/`                               |
| `templates/shorts/anthropic/index.html`                                       | UPDATE | Replace SFX comment placeholder with commented-out live SFX block + sonic-logo block                         |
| `templates/shorts/anthropic/README.md`                                        | UPDATE | "Adding SFX" section: reference `sync-video-sfx.sh` and `.claude/rules/audio-design.md`                      |
| `templates/shorts/anthropic/DESIGN.md`                                        | UPDATE | Cue table: cross-link to `audio-design.md`; ensure values match (no contradiction)                           |
| `shared/lib/visual-styles/anthropic-dark.md`                                  | UPDATE | Cross-link to `audio-design.md`; ensure cue table matches DESIGN.md                                          |
| `.claude/commands/diy-yt-creator/phase1-plan.md`                              | UPDATE | Section 5C: tighten "SFX placement" — output cue **names** that resolve to library files, not freeform prose |
| `.claude/commands/diy-yt-creator/phase3-5-retention.md`                       | UPDATE | Add per-scene `sfx_cues` block to retention-strategy.md output (cue, anchor_word_index, start_seconds, track_index, volume) |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                        | UPDATE | Step 8: add SFX wiring substep (read `sfx_cues`, run sync, insert `<audio>` elements). Step 9: add SFX-specific lint expectations.|
| `.claude/commands/diy-yt-creator/full-auto.md`                                | UPDATE | Lines 521-523: remove "SFX placement is human work" framing — pipeline now wires SFX                         |
| `CLAUDE.md`                                                                   | UPDATE | Add `shared/audio/` to project-structure tree (between `shared/logos/` and `shared/lib/`)                    |

---

## NOT Building (Scope Limits)

Explicit exclusions to keep this PR shippable:

- **Long-form multi-segment background music.** The Remotion `audio-design.md` has an extensive multi-segment BG music section (`bg-music-hook.mp3` / `body.mp3` / `cta.mp3` with BPM-driven volume curves). HyperFrames currently only ships Shorts (1080×1920) which by rule have **no BG music**. Document the long-form pattern as TBD in `audio-design.md` for when long-form templates land — but build no script and no template scaffolding for it now.
- **Sonic-logo at frame 0 as a hard-mandatory rule.** The Remotion repo enforced sonic-logo on every composition. Generate one canonical `sonic-logo.mp3` in the library and document the pattern in the rule file, but don't make the linter or template enforce it on every video. Optional, opt-in.
- **Beat alignment / `alignToDownbeat()` utility.** Remotion's beat-snapping was for cinematic hook trailers with measured BPM tracks. Out of scope until long-form arrives. Document as TBD.
- **`extract-audio-data.py` integration.** That script exists in this repo (`.agents/skills/gsap/scripts/`) for audio-reactive *visuals*, not SFX scheduling. SFX uses `transcript.json` word timestamps — no extra extraction needed.
- **Custom HyperFrames lint rules for SFX volume caps.** Tempting, but linter is third-party (`@hyperframes/cli`). Enforce caps in `audio-design.md` + at composition-build agent prompt level. A future plan can add a wrapping script.
- **Replacing the existing `sound-effects` skill.** The skill is a thin ElevenLabs wrapper used ad-hoc. The new generator script consumes the same API directly; the skill remains for one-off interactive use.
- **Backfilling SFX into existing videos** (`videos/claude-connectors-everyday-life/`, `videos/anthropic-amazon-compute/`). Out of scope. The new pipeline applies to videos created from this point forward; existing videos can be re-edited manually if the user chooses.

---

## Step-by-Step Tasks

Execute in dependency order. Each task is atomic and independently verifiable.

### Task 1: CREATE `.claude/rules/audio-design.md`

- **ACTION**: Author the canonical HyperFrames audio rules file by adapting `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\rules\audio-design.md`.
- **STRUCTURE** (in this order):
  1. Frontmatter `paths: [ "**/index.html", "**/*.py" ]` (mirrors source)
  2. **Volume Levels** — keep the dB-anchored table; rename `volume={1.0}` → `data-volume="1.0"` etc.
  3. **SFX Volume Caps (MANDATORY)** — keep verbatim including the dB cheatsheet; rewrite "0.25 hard cap" rationale.
  4. **SFX Volume Table per cue** — match `templates/shorts/anthropic/DESIGN.md:114-123` exactly. Include the file basename column (e.g., `impact-slam.mp3`) for unambiguous resolution.
  5. **Sonic Logo** — adapted: `<audio id="sonic-logo" src="assets/sfx/sonic-logo.mp3" data-start="0" data-duration="1.5" data-track-index="3" data-volume="0.6">`. Note: optional, not enforced.
  6. **Shorts Have NO Background Music (HARD RULE)** — keep verbatim, but rewrite the React/Sequence example as: "do not add any `<audio src=…bg-music…>` element to a Short composition."
  7. **SFX Must Be Aligned to Their Visual Triggers (Audit After Composition Build)** — rewrite for seconds: alignment is `transcript.json[word_index].start + offset`. Drift > 0.15s (~5 frames at 30fps) is a bug. Drop frame-formula references.
  8. **Volume control mechanics** — explicit: `data-volume` is the only mechanism; the framework reads it; do NOT call `element.volume = …` from JS; do NOT animate volume via GSAP.
  9. **Track-index assignment rule** — narration on 2; SFX start at 3 and increment per concurrent cue; same-track clips cannot overlap (lint will catch).
  10. **Multi-segment BG music — TBD for long-form** — short paragraph noting it exists in legacy Remotion and will be ported when long-form templates land.
  11. **Beat alignment — TBD** — same: parking lot.
- **DROP from source**: `<Audio>`, `<Sequence>`, `interpolate()`, `staticFile()`, `wordToFrame()`, `alignToDownbeat()`, `python scripts/generate-sonic-logo.py` references.
- **CROSS-LINK**: at top, link `templates/shorts/anthropic/DESIGN.md` cue table; at bottom, link `shared/audio/MANIFEST.md`, `scripts/generate-sfx-library.py`, `scripts/sync-video-sfx.sh`.
- **MIRROR**: source frontmatter style (P0 reading)
- **GOTCHA**: Volume table must NOT contradict `templates/shorts/anthropic/DESIGN.md:114-123`. If a value differs (the source has `cinematic-whoosh: 0.15` and DESIGN.md says `0.15` ✓; source has `glitch-zap: 0.12` and DESIGN.md says `0.12` ✓; both match), prefer the existing repo value and note the alignment.
- **VALIDATE**: `npx hyperframes lint videos/anthropic-amazon-compute` still passes (rules file is doc-only; lint should not regress). Also: `grep -E "\\<Audio|<Sequence|interpolate\\(|staticFile" .claude/rules/audio-design.md` returns nothing (verifies no Remotion-specific syntax leaked).

### Task 2: CREATE `shared/audio/README.md`

- **ACTION**: Document the directory and consumption rules.
- **CONTENT** (mirror `shared/lib/README.md` style):
  - One-paragraph purpose: "Canonical SFX library for HyperFrames videos. Like `shared/lib/`, this is **copy-from**, not reference-from — the bundler rejects paths outside a video's project dir for `<audio src>`."
  - **How to use**: 1. Pick cue from `MANIFEST.md`. 2. Add to your video's plan/retention-strategy as `sfx_cues:`. 3. Run `bash scripts/sync-video-sfx.sh videos/<slug>` to copy declared cues. 4. Wire `<audio>` elements per `.claude/rules/audio-design.md`.
  - **Don'ts**: do not `<audio src="../../shared/audio/sfx/foo.mp3">` — will 404 in preview, render empty. (Cite `shared/lib/README.md:7-13` constraint.)
- **MIRROR**: `shared/lib/README.md:1-80` structure.
- **VALIDATE**: file exists, contains the words "copy-from" and "404".

### Task 3: CREATE `shared/audio/MANIFEST.md`

- **ACTION**: One-line-per-file registry.
- **STRUCTURE**: Markdown table with columns: `cue_name | file | duration_s | default_volume | recommended_use`
- **CONTENT** (8–10 entries matching `templates/shorts/anthropic/DESIGN.md:114-123`):
  ```markdown
  | Cue                | File                       | Duration | Default Volume | Recommended Use                                |
  |--------------------|----------------------------|----------|----------------|------------------------------------------------|
  | impact-slam        | impact-slam.mp3            | ~0.6s    | 0.20           | Hero word reveal; pivot moment                  |
  | scale-slam         | scale-slam.mp3             | ~0.7s    | 0.20           | Stat-pill entrance; big number reveal           |
  | screen-shake       | screen-shake.mp3           | ~0.5s    | 0.15           | Hero word inline shake; layer with impact-slam  |
  | cinematic-whoosh   | cinematic-whoosh.mp3       | ~0.8s    | 0.15           | Phase / scene change                            |
  | spring-pop         | spring-pop.mp3             | ~0.4s    | 0.15           | Card or chip entrance                           |
  | pop                | pop.mp3                    | ~0.25s   | 0.13           | Small chip / list item                          |
  | glitch-zap         | glitch-zap.mp3             | ~0.5s    | 0.12           | "BUT…" pivot; regression callout                |
  | strike-cross       | strike-cross.mp3           | ~0.6s    | 0.15           | Strikethrough moment                            |
  | sonic-logo         | sonic-logo.mp3             | ~1.5s    | 0.60           | Brand stinger at frame 0 (optional)             |
  ```
  Duration column is approximate — to be filled in precisely after Task 5 generates files (use `ffprobe` or read WAV headers; commit the real values).
- **VALIDATE**: file parses as Markdown table with 9 rows.

### Task 4: CREATE `scripts/generate-sfx-library.py`

- **ACTION**: Batch ElevenLabs generator, idempotent (skips files already on disk unless `--force`).
- **STRUCTURE** (mirror `scripts/elevenlabs-tts.py:1-67`):
  - Module docstring: `"""Generate canonical SFX library for shared/audio/sfx/ via ElevenLabs."""`
  - Imports: `argparse, os, sys, pathlib, dotenv, elevenlabs.ElevenLabs`
  - Define a Python list of cue specs at module top:
    ```python
    CUES = [
      {"name": "impact-slam",     "prompt": "Deep cinematic bass impact slam, single hit, no reverb tail, dry punchy",     "duration_seconds": 0.6, "prompt_influence": 0.7},
      {"name": "scale-slam",      "prompt": "Heavy metallic scale slam, weighty single drop, very short tail",              "duration_seconds": 0.7, "prompt_influence": 0.7},
      {"name": "screen-shake",    "prompt": "Subtle low-frequency rumble, half a second, no rise no decay, suitable to layer", "duration_seconds": 0.5, "prompt_influence": 0.6},
      {"name": "cinematic-whoosh","prompt": "Quick cinematic whoosh, transition sweep, mid-range, no reverb",                "duration_seconds": 0.8, "prompt_influence": 0.6},
      {"name": "spring-pop",      "prompt": "Light bouncy spring pop, UI element entrance, snappy",                          "duration_seconds": 0.4, "prompt_influence": 0.7},
      {"name": "pop",             "prompt": "Soft round pop, small UI tap",                                                  "duration_seconds": 0.25,"prompt_influence": 0.7},
      {"name": "glitch-zap",      "prompt": "Digital glitch zap, electric sputter, retro tech, half a second",               "duration_seconds": 0.5, "prompt_influence": 0.7},
      {"name": "strike-cross",    "prompt": "Quick brush strikethrough sound, pen scratch crossing out text",                "duration_seconds": 0.6, "prompt_influence": 0.7},
      {"name": "sonic-logo",      "prompt": "Brief warm orchestral brand stinger, ascending two-note motif, ends clean",     "duration_seconds": 1.5, "prompt_influence": 0.5},
    ]
    ```
  - Argparse: `--force` (regenerate existing), `--only <name>` (single cue), `--out-dir` (default `shared/audio/sfx`).
  - Output: `mp3_44100_128` format. Iterate cues, skip if file exists and not `--force`, otherwise call `client.text_to_sound_effects.convert(text=..., duration_seconds=..., prompt_influence=...)` and stream to file.
  - Print one line per cue: `[sfx] generated impact-slam.mp3 (0.6s, NN bytes)` or `[sfx] skipped impact-slam.mp3 (exists)`.
  - Exit 2 on missing API key, 0 on success, 1 on any per-cue failure but continue.
- **MIRROR**: `scripts/elevenlabs-tts.py:1-67` (env loading, argparse, error patterns)
- **IMPORTS**: `from elevenlabs import ElevenLabs` (already in deps via `elevenlabs-tts.py`)
- **GOTCHA**: ElevenLabs rate-limits. Add a `time.sleep(1)` between requests. Do NOT raise on a single cue failure — log and continue so a partial run is useful.
- **VALIDATE**:
  - `python scripts/generate-sfx-library.py --help` prints usage with `--force`, `--only`, `--out-dir`.
  - Dry-run test: `python -c "import ast; ast.parse(open('scripts/generate-sfx-library.py').read())"` parses cleanly.
  - With `ELEVENLABS_API_KEY` unset: prints "ERROR: ELEVENLABS_API_KEY not set", exits 2.

### Task 5: RUN `scripts/generate-sfx-library.py` and commit results

- **ACTION**: Generate all 9 cues to `shared/audio/sfx/`. Verify durations by inspection. Update `shared/audio/MANIFEST.md` with real durations.
- **PRECONDITION**: User has `ELEVENLABS_API_KEY` in `.env` (already required by `elevenlabs-tts.py`).
- **PROCEDURE**:
  1. `python scripts/generate-sfx-library.py`
  2. For each generated file, listen via system audio player and verify it matches the cue (manual QA).
  3. If a cue is wrong (e.g., reverb tail too long, wrong character), regenerate with adjusted prompt: edit `CUES` in the script, run `python scripts/generate-sfx-library.py --force --only <name>`.
  4. Run `ffprobe -v error -show_entries format=duration -of default=nokey=1:noprint_wrappers=1 shared/audio/sfx/<file>.mp3` for each file, write real duration into `MANIFEST.md`.
- **GOTCHA**: This task burns API credits. If `ELEVENLABS_API_KEY` is not present, defer this task and document the user must run it themselves.
- **VALIDATE**: 9 `.mp3` files exist in `shared/audio/sfx/`. `du -sh shared/audio/sfx/` shows >100KB total. `MANIFEST.md` durations are no longer "approx".

### Task 6: CREATE `scripts/sync-video-sfx.sh`

- **ACTION**: Per-video sync hook. Reads either a CLI list or a manifest file from the video, copies cues from `shared/audio/sfx/` into `videos/<slug>/assets/sfx/`.
- **STRUCTURE** (mirror `scripts/sync-shared-lib.sh`):
  - Bash strict mode, repo-root resolution.
  - Usage: `sync-video-sfx.sh <project_dir> [cue1 cue2 ...]`. If no cues given, read from `<project_dir>/sfx-cues.txt` (one cue name per line).
  - For each cue: validate `shared/audio/sfx/<cue>.mp3` exists; `mkdir -p <project_dir>/assets/sfx`; `cp -n` (no-clobber) or `cp` if `--force`.
  - Print one line per cue: `[sfx-sync] copied impact-slam.mp3 → videos/<slug>/assets/sfx/`.
  - Exit nonzero if any requested cue is not in the library (with helpful message listing available cues).
- **MIRROR**: `scripts/sync-shared-lib.sh` (strict mode header, repo-root pattern)
- **IMPORTS**: bash builtins only.
- **GOTCHA**: Windows path separators — use forward slashes; the existing sync scripts already work on Git Bash on Windows (per CLAUDE.md). Don't introduce `realpath` if the existing scripts don't (verify first).
- **VALIDATE**:
  - `bash scripts/sync-video-sfx.sh --help` (or running with no args) prints usage.
  - Dry-run on existing video: `bash scripts/sync-video-sfx.sh videos/anthropic-amazon-compute impact-slam` should copy `shared/audio/sfx/impact-slam.mp3` → `videos/anthropic-amazon-compute/assets/sfx/impact-slam.mp3`. Verify file appears, then delete it (cleanup; we don't backfill that video per scope limits).

### Task 7: UPDATE `templates/shorts/anthropic/index.html`

- **ACTION**: Replace the SFX-placeholder comment block at lines 518-523 with a richer commented-out block: a sonic-logo `<audio>` and 2 SFX `<audio>` examples (commented), plus the `<audio id="narration">` template (already partly there as a comment per `tts.md`).
- **CONTENT** (insert after the closing `</div>` of `#root` content but before `</div>` of `#root` itself, where audio currently lives in `videos/anthropic-amazon-compute/index.html:906`):
  ```html
  <!-- ═══════════════════════════════════════════════════════
       NARRATION + SFX
       Rules: .claude/rules/audio-design.md
       Cue catalog: shared/audio/MANIFEST.md
       Sync into this project: bash scripts/sync-video-sfx.sh videos/<slug>
       ═══════════════════════════════════════════════════════ -->

  <!--
  <audio id="narration"
         class="clip"
         src="audio/narration.wav"
         data-start="0"
         data-duration="0"
         data-track-index="2"
         data-volume="1"></audio>

  <audio id="sfx-impact"
         class="clip"
         src="assets/sfx/impact-slam.mp3"
         data-start="1.55"
         data-duration="0.6"
         data-track-index="3"
         data-volume="0.20"></audio>

  <audio id="sfx-whoosh"
         class="clip"
         src="assets/sfx/cinematic-whoosh.mp3"
         data-start="3.2"
         data-duration="0.8"
         data-track-index="4"
         data-volume="0.15"></audio>
  -->
  ```
- **MIRROR**: `videos/anthropic-amazon-compute/index.html:906-912` for the live narration shape; `templates/shorts/anthropic/README.md:109-115` for SFX shape.
- **GOTCHA**: Keep elements commented out — uncommenting them in the template would cause `audio_src_not_found` lint errors because the files don't exist in the template dir. Live elements only get uncommented in real videos after `sync-video-sfx.sh` runs.
- **VALIDATE**: `npx hyperframes lint templates/shorts/anthropic` passes with 0 errors (matching pre-change baseline). Use `--verbose` to see warnings; `duplicate_media_discovery_risk` should NOT appear (the literal `<audio …>` is inside an HTML comment, but the linter has been seen to mistakenly flag commented-out tags — if it does, restructure the comment per CLAUDE.md "Linting" section guidance).

### Task 8: UPDATE `templates/shorts/anthropic/README.md`

- **ACTION**: Extend the "Adding SFX" section (currently lines 105-118).
- **CHANGES**:
  - After line 118 (the "Place under the `<audio id="narration">` block..." sentence), add:
    ```markdown
    ### Sourcing the actual SFX files

    The cues above are names — the audio files live in `shared/audio/sfx/`. To copy
    them into your video's `assets/sfx/` (required because HyperFrames rejects paths
    outside the project dir at runtime), run:

    ```bash
    bash scripts/sync-video-sfx.sh videos/<slug> impact-slam scale-slam spring-pop
    ```

    Or list the cues you want in `videos/<slug>/sfx-cues.txt` (one per line) and run
    without arguments. Volume caps and the full per-cue table are in
    `.claude/rules/audio-design.md`.
    ```
- **MIRROR**: existing README style (concise, code blocks, cross-links).
- **VALIDATE**: file is valid Markdown; new section appears; existing "Adding narration" section is unchanged.

### Task 9: UPDATE `.claude/commands/diy-yt-creator/phase1-plan.md` Section 5C

- **ACTION**: Tighten "5C: SFX placement" so the planning output uses **resolvable cue names** from `shared/audio/MANIFEST.md`, not free prose.
- **CURRENT** (lines 338-350): table with intent like `"LAYERED: impact-slam + screen-shake + glitch-zap"` — readable but not directly consumable.
- **NEW**: same table, but add a structured YAML output requirement at the bottom:
  ```yaml
  sfx_cues:                          # consumable by phase3-5-retention.md
    - beat: "PIVOT"
      cues: [impact-slam, screen-shake, glitch-zap]   # MUST come from shared/audio/MANIFEST.md
    - beat: "Brand reveal"
      cues: [scale-slam]
    - beat: "Feature card entrance"
      cues: [spring-pop]
  ```
- **CONSTRAINT**: Add a sentence: "Every cue name MUST appear in `shared/audio/MANIFEST.md`. If a needed cue is missing, stop and propose an addition to the library — do not invent a filename."
- **CROSS-LINK**: link to `.claude/rules/audio-design.md` (volume caps + same-track rule).
- **VALIDATE**: file diff shows only Section 5C changed; the other sections (5A, 5B, 5D, 5E) untouched.

### Task 10: UPDATE `.claude/commands/diy-yt-creator/phase3-5-retention.md`

- **ACTION**: Add a per-scene `sfx_cues` block to the retention-strategy.md output schema. This is where intent (Phase 1) becomes concrete (cue + seconds + track + volume) using `transcript.json` as the timing source.
- **CHANGES**:
  - Find the section that defines the retention-strategy.md output structure (per-scene block).
  - Add a sub-section after the visual retention components, e.g.:
    ```yaml
    sfx_cues:                       # per scene
      - cue: impact-slam            # name from shared/audio/MANIFEST.md
        anchor_word_index: 12       # transcript.json[12].start is the beat anchor
        offset_seconds: -0.05       # SFX fires 0.05s BEFORE the spoken word (lead-in)
        duration_seconds: 0.6       # from MANIFEST.md
        track_index: 3              # unique per concurrent SFX (3, 4, 5...)
        volume: 0.20                # from MANIFEST.md default unless overridden
    ```
  - Add explicit instruction: "Resolve `data-start = transcript.json[anchor_word_index].start + offset_seconds`. Verify start ≥ 0 and start + duration ≤ narration duration. Verify track_index uniqueness for any cues whose [start, start+duration) overlap."
  - Add reference: "See `.claude/rules/audio-design.md` for volume caps and the alignment audit rule (drift > 0.15s is a bug)."
- **MIRROR**: existing per-scene block style in the same file.
- **VALIDATE**: file diff is additive only (no existing visual-component logic removed); the new `sfx_cues` schema is unambiguous (cue, anchor_word_index, offset_seconds, duration_seconds, track_index, volume — six fields, all required except `offset_seconds` which defaults to 0).

### Task 11: UPDATE `.claude/skills/diy-yt-creator/new-anthropic-short.md` Step 8 + Step 9

- **ACTION**: Make SFX wiring an explicit substep of the composition build.
- **CHANGES**:
  - In Step 8 (HTML edit), add a new sub-step after the visual-component wiring:
    > **8.7 Wire SFX from `retention-strategy.md`**
    > 1. Read the `sfx_cues` blocks from each scene of `videos/<slug>/retention-strategy.md`.
    > 2. Build a deduplicated cue list: `cues = unique(all sfx_cues[].cue)`.
    > 3. Run: `bash scripts/sync-video-sfx.sh videos/<slug> ${cues[@]}` — this copies files into `videos/<slug>/assets/sfx/`.
    > 4. For each `sfx_cues` entry across all scenes, insert an `<audio>` element below the `<audio id="narration">` block:
    >    ```html
    >    <audio id="sfx-<cue>-<index>"
    >           class="clip"
    >           src="assets/sfx/<cue>.mp3"
    >           data-start="<computed_start>"
    >           data-duration="<duration_seconds>"
    >           data-track-index="<track_index>"
    >           data-volume="<volume>"></audio>
    >    ```
    > 5. Verify all `data-volume` values ≤ 0.25 (per `.claude/rules/audio-design.md`). Sonic-logo only may exceed this.
  - In Step 9 (Lint table at lines 252-256), add a new error row:
    ```markdown
    | `audio_src_not_found` (sfx) | Cue file missing from `assets/sfx/` | Run `bash scripts/sync-video-sfx.sh videos/<slug> <missing-cue>` |
    | `overlapping_gsap_tweens` (sfx) | Two SFX on same `data-track-index` overlap in time | Bump second SFX to next track index |
    ```
- **MIRROR**: existing step-8/step-9 prose style and table format.
- **VALIDATE**: file diff is additive; running `/diy-yt-creator:new-anthropic-short` on a sample video would now write SFX elements (manual verification on a fresh test video, post-merge).

### Task 12: UPDATE `.claude/commands/diy-yt-creator/full-auto.md` lines 521-523

- **ACTION**: Remove the "SFX placement is human work" framing — the pipeline now does it.
- **CURRENT** (lines 521-523):
  > Why we pause here: composition build is creative work (logo selection, accent
  > rotation, phase timing, **SFX placement**) that benefits from human-in-the-loop
  > judgment. Auto-building would produce a generic output.
- **NEW**:
  > Why we pause here: composition build is creative work (logo selection, accent
  > rotation, phase timing) that benefits from human-in-the-loop judgment. Auto-building
  > would produce a generic output. SFX wiring **is** automated — `new-anthropic-short`
  > reads `retention-strategy.md sfx_cues`, runs `sync-video-sfx.sh`, and inserts the
  > `<audio>` elements per `.claude/rules/audio-design.md`.
- **VALIDATE**: file diff shows only this paragraph changed; no other handoff messaging touched.

### Task 13: UPDATE `templates/shorts/anthropic/DESIGN.md` and `shared/lib/visual-styles/anthropic-dark.md`

- **ACTION**: Cross-link both cue tables to `.claude/rules/audio-design.md` as the canonical source. Verify the volume values match.
- **CHANGES (DESIGN.md, line 110-125 area)**: Above the cue table, add: "Canonical rules: `.claude/rules/audio-design.md`. Cue files live in `shared/audio/sfx/` (sync via `scripts/sync-video-sfx.sh`)."
- **CHANGES (anthropic-dark.md, line 85-100 area)**: Same one-line cross-link above the cue table.
- **VERIFY**: Each row's volume in the existing cue tables matches `.claude/rules/audio-design.md` (Task 1) and `shared/audio/MANIFEST.md` (Task 3). If a value differs, the source of truth is `audio-design.md`; update DESIGN.md and anthropic-dark.md to match.
- **VALIDATE**: `diff <(grep -E '^\| `?[a-z-]+`?' templates/shorts/anthropic/DESIGN.md | sort) <(grep -E '^\| [a-z-]+' shared/audio/MANIFEST.md | sort)` shows matching cue names (volumes will differ in formatting; verify by eye).

### Task 14: UPDATE `CLAUDE.md` project-structure tree

- **ACTION**: Add `shared/audio/` to the directory tree at lines 54-77.
- **CHANGE**: Insert between `shared/logos/` line and `shared/lib/` line:
  ```
  │   ├── audio/                                   ← shared SFX library — copy-from
  ```
- **VALIDATE**: tree still parses visually; no other lines moved.

---

## Testing Strategy

### Validation Commands per Task

| Task | Validation                                                                                                     |
| ---- | -------------------------------------------------------------------------------------------------------------- |
| 1    | `npx hyperframes lint videos/anthropic-amazon-compute` exit 0; grep confirms no Remotion syntax in rule file  |
| 2    | File exists; contains "copy-from" and "404"                                                                    |
| 3    | Markdown table parses; 9 rows                                                                                  |
| 4    | `python -c "import ast; ast.parse(open('scripts/generate-sfx-library.py').read())"` succeeds; `--help` works   |
| 5    | 9 `.mp3` files in `shared/audio/sfx/`; total size > 100 KB; manual playback QA                                 |
| 6    | `bash scripts/sync-video-sfx.sh` smoke-test copies a file then cleans up                                       |
| 7    | `npx hyperframes lint templates/shorts/anthropic` exit 0                                                       |
| 8    | Markdown valid; cross-links resolve                                                                            |
| 9-13 | File diffs are scoped; rules-doc cross-links exist                                                             |
| 14   | `cat CLAUDE.md` shows `shared/audio/` in tree                                                                  |

### End-to-End Validation (Manual)

After all tasks complete, run a smoke pass on a fresh test video:

1. Spawn a new test video: `cp -r templates/shorts/anthropic videos/sfx-smoke-test`
2. Update meta.json
3. Drop a placeholder `audio/narration.wav` (any short WAV will do — generate a 5-second silence with `ffmpeg -f lavfi -i anullsrc -t 5 videos/sfx-smoke-test/audio/narration.wav`)
4. Manually edit `index.html` to uncomment the narration block, set `data-duration="5"`
5. Run: `bash scripts/sync-video-sfx.sh videos/sfx-smoke-test impact-slam spring-pop`
6. Manually wire two SFX `<audio>` elements at `data-start="1"` track 3 and `data-start="2"` track 4.
7. `npx hyperframes lint videos/sfx-smoke-test` — must exit 0.
8. `npx hyperframes preview videos/sfx-smoke-test` — open in browser, listen, verify both SFX fire at the right times and volume sounds balanced (impact-slam ≈ -12 dB below narration; spring-pop quieter).
9. Delete `videos/sfx-smoke-test/` after smoke passes.

### Edge Cases Checklist

- [ ] Cue name in plan but not in `shared/audio/MANIFEST.md` → sync script errors with helpful message + library listing
- [ ] Two SFX on same `data-track-index` with overlapping time windows → lint catches `overlapping_gsap_tweens`
- [ ] `data-volume="0.5"` (above 0.25 cap) → caught at composition-build time by agent reading `audio-design.md`; no automated linter check (out of scope)
- [ ] `data-start` < 0 or > narration duration → caught at composition-build time by agent verification step (Task 10 instruction "Verify start ≥ 0...")
- [ ] Missing `class="clip"` on SFX `<audio>` → may cause framework not to gate visibility; the live narration in `videos/anthropic-amazon-compute/index.html:907` has it; the one in `videos/claude-connectors-everyday-life/index.html:510` doesn't, and both currently work — but `audio-design.md` should require it for SFX consistency.
- [ ] `ELEVENLABS_API_KEY` unset when running generate script → script exits 2 with clear message
- [ ] Generation produces an SFX with too long a reverb tail → `--force --only <name>` regenerates after prompt tuning
- [ ] User runs `sync-video-sfx.sh` twice → second run is no-op (cp `-n`) unless `--force`

---

## Validation Commands

### Level 1: STATIC_ANALYSIS

```bash
# Python syntax check on the new generator script
python -c "import ast; ast.parse(open('scripts/generate-sfx-library.py').read())"

# Bash syntax check on the new sync script
bash -n scripts/sync-video-sfx.sh

# Rules file does not contain Remotion-specific syntax (per Task 1 constraint)
grep -E "<Audio|<Sequence|interpolate\\(|staticFile|wordToFrame|alignToDownbeat" .claude/rules/audio-design.md && echo "FAIL: Remotion syntax leaked" || echo "PASS"
```

**EXPECT**: Python parses; bash parses; grep returns nothing → "PASS"

### Level 2: LINT_BASELINE_NO_REGRESSION

```bash
npx hyperframes lint videos/anthropic-amazon-compute
npx hyperframes lint videos/claude-connectors-everyday-life
npx hyperframes lint templates/shorts/anthropic
```

**EXPECT**: exit 0 for all three, matching pre-change baseline. Warnings allowed; errors not.

### Level 3: GENERATOR_DRY_RUN

```bash
# With API key absent: clean error, exit 2
ELEVENLABS_API_KEY="" python scripts/generate-sfx-library.py
echo "exit: $?"
# Expected: "ERROR: ELEVENLABS_API_KEY not set" + exit 2

# With API key present: generates 9 files, idempotent on second run
python scripts/generate-sfx-library.py
ls shared/audio/sfx/*.mp3 | wc -l   # should be 9
python scripts/generate-sfx-library.py   # second run, all skipped
```

**EXPECT**: First failure path exits 2; happy path generates 9 files; idempotent re-run skips all.

### Level 4: SYNC_HOOK_SMOKE

```bash
# Should copy two named cues into a real video, then back out cleanly
mkdir -p /tmp/sfx-test-target/assets
bash scripts/sync-video-sfx.sh /tmp/sfx-test-target impact-slam spring-pop
ls /tmp/sfx-test-target/assets/sfx/   # impact-slam.mp3 spring-pop.mp3
rm -rf /tmp/sfx-test-target
```

**EXPECT**: Two MP3s copied; no errors.

### Level 5: END_TO_END_PIPELINE_DRY_RUN (manual)

See "End-to-End Validation" above. Run on a throwaway video.

### Level 6: DOC_CONSISTENCY_AUDIT

```bash
# Cue names must match across MANIFEST.md, audio-design.md, DESIGN.md
grep -oE 'impact-slam|scale-slam|screen-shake|cinematic-whoosh|spring-pop|^\| pop|glitch-zap|strike-cross|sonic-logo' \
  shared/audio/MANIFEST.md .claude/rules/audio-design.md templates/shorts/anthropic/DESIGN.md \
  | sort | uniq -c
```

**EXPECT**: each cue name appears at least once in each of the three docs.

---

## Acceptance Criteria

- [ ] `.claude/rules/audio-design.md` exists with HyperFrames-specific syntax only (no `<Audio>`, `<Sequence>`, `interpolate()`, etc.)
- [ ] `shared/audio/sfx/` contains the 9 canonical cue files
- [ ] `shared/audio/MANIFEST.md` and `README.md` exist and cross-link
- [ ] `scripts/generate-sfx-library.py` runs idempotently and exits 2 on missing API key
- [ ] `scripts/sync-video-sfx.sh` copies declared cues into a video's `assets/sfx/`
- [ ] Template `index.html` has commented-out SFX block; lint still 0 errors
- [ ] Template `README.md` documents the sync hook + rules link
- [ ] `phase1-plan.md` 5C produces a structured `sfx_cues:` YAML output with names from MANIFEST
- [ ] `phase3-5-retention.md` adds per-scene `sfx_cues` schema with seconds/track/volume
- [ ] `new-anthropic-short.md` Step 8 wires `<audio>` elements; Step 9 documents new lint failure modes
- [ ] `full-auto.md` no longer claims SFX placement is human work
- [ ] `CLAUDE.md` project tree includes `shared/audio/`
- [ ] All 6 validation levels pass
- [ ] Smoke test on a throwaway video plays narration + 2 SFX in correct positions, balanced volumes

---

## Completion Checklist

- [ ] Tasks 1-14 completed in dependency order
- [ ] Level 1 static analysis: clean
- [ ] Level 2 lint baseline: no regression on existing videos
- [ ] Level 3 generator dry-run: idempotent, fails clean without API key
- [ ] Level 4 sync hook smoke: copies cleanly
- [ ] Level 5 end-to-end smoke: a throwaway video previews with SFX
- [ ] Level 6 doc consistency: all 9 cue names present in 3 docs
- [ ] No `<Audio>`/`<Sequence>`/`interpolate()` references in any new file
- [ ] Volume table values match across `.claude/rules/audio-design.md`, `shared/audio/MANIFEST.md`, `templates/shorts/anthropic/DESIGN.md`, `shared/lib/visual-styles/anthropic-dark.md`

---

## Risks and Mitigations

| Risk                                                                                                    | Likelihood | Impact | Mitigation                                                                                                                            |
| ------------------------------------------------------------------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| ElevenLabs SFX generation produces files that don't match the cue intent (wrong character / reverb)     | MEDIUM     | MEDIUM | Manual QA in Task 5; `--force --only` allows targeted regeneration with adjusted prompt; document prompt tuning in MANIFEST.md         |
| `<audio>` inside an HTML comment triggers `duplicate_media_discovery_risk` warning in lint              | MEDIUM     | LOW    | Per CLAUDE.md, this is a known false-positive pattern. If it fires, restructure the comment (split across lines so `<audio` is not on a single comment line) |
| HyperFrames render pipeline does not capture `<audio data-volume>` correctly with many concurrent tracks | LOW        | HIGH   | Test render output (one short MP4) as part of end-to-end validation. If broken, reduce to fewer concurrent tracks per scene; file an issue upstream |
| Volume values drift between `audio-design.md`, `MANIFEST.md`, and `DESIGN.md` over time                 | MEDIUM     | LOW    | Level 6 doc consistency audit codifies the cross-check; Task 13 establishes `audio-design.md` as source of truth                       |
| Fractional `data-start` precision: HyperFrames may snap to frame boundaries internally                  | LOW        | LOW    | The framework is documented as seconds-native (`hyperframes/SKILL.md`). Drift in playback < 33ms (1 frame at 30fps) is below human audio threshold for non-percussive cues. Audit rule "drift > 0.15s is a bug" tolerates this |
| User runs out of ElevenLabs API quota during Task 5                                                     | LOW        | LOW    | Generator is idempotent — restart picks up where it left off. 9 cues × ~$0.01 each ≈ negligible cost                                  |
| Existing two videos (`anthropic-amazon-compute`, `claude-connectors-everyday-life`) lack SFX            | N/A        | N/A    | Out of scope (per "NOT Building"). User can manually backfill if desired.                                                              |
| Long-form template lands later and re-uses different naming conventions                                 | LOW        | LOW    | `audio-design.md` has TBD sections for multi-segment BG music + beat alignment; future plan extends rather than replaces               |

---

## Notes

**Why a rules file at `.claude/rules/audio-design.md` and not just an extension of `DESIGN.md`?**

The Remotion source had a `paths`-globbed rule file that auto-loaded into the agent context whenever `Composition.tsx` or `*.py` files were edited. This repo's `.claude/` directory has `commands/`, `references/`, and `skills/` but no `rules/` yet (per Bash discovery). The rule file is a clean addition that preserves the original's auto-loading semantics for HTML compositions, and centralizes guidance that would otherwise be duplicated across `DESIGN.md`, `anthropic-dark.md`, and pipeline-phase docs. `DESIGN.md` is template-specific (anthropic-dark); the rules file is repo-wide.

**Why MP3 instead of WAV?**

The existing `.gitignore` and asset patterns in this repo (and the template README's `assets/sfx/scale-slam.wav` example) suggest WAV is acceptable. But ElevenLabs sound-effects API defaults to `mp3_44100_128`. Using MP3 keeps generated artifacts ~5× smaller for git, and HyperFrames `<audio>` accepts both. We pick MP3. (Narration stays WAV because `elevenlabs-tts.py` writes WAV and downstream tooling depends on that.)

**Why commit the SFX files instead of `.gitignore`-ing them?**

Reproducibility. New contributors should not need an ElevenLabs API key to render existing videos or develop on the pipeline. 9 small MP3s ~< 500 KB total is well within reasonable repo size. The generator script exists for adding new cues, not for everyday use.

**Future plan hooks (out of scope here, but worth noting):**

1. A long-form template will need: multi-segment BG music section in `audio-design.md` (currently TBD), a `generate-bg-music.py` script (mirrors `generate-sfx-library.py` but uses ElevenLabs Music API), and a beat-alignment utility. Defer until long-form template work begins.
2. A `validate-audio-mix.sh` linter wrapper could parse a video's `<audio>` elements and verify volume caps, track-index uniqueness, and start/duration bounds — codifying the audit rule. Defer until manual auditing reveals enough drift to justify it.
3. A sonic-logo enforcement option (e.g., `hyperframes lint --strict-audio`) could ensure every composition starts with a sonic-logo. Defer.

**Confidence Score: 8.5 / 10** for one-pass implementation success.
- (+) HyperFrames mechanism is fully understood and documented in-repo (`templates/shorts/anthropic/README.md:105-118` is the exact pattern)
- (+) ElevenLabs API surface is in-skill (`sound-effects/SKILL.md`) and the Python pattern is mirrored from `elevenlabs-tts.py`
- (+) No new framework code, no React→HTML translation tricks needed
- (+) Existing `shared/lib/` "copy-from" architecture is the same model `shared/audio/` follows
- (-) Task 5 (file generation) requires API access and manual QA — can't be fully automated in CI
- (-) Render-pipeline audio capture for many concurrent tracks is documented as a "needs verification" gap from the analyst (Question 6) — only end-to-end smoke testing surfaces issues
- (-) The `duplicate_media_discovery_risk` lint false-positive on commented-out `<audio>` tags is a known footgun the implementer must catch on first lint run
