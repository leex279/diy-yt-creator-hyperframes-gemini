---
status: pending
created: 2026-04-27
input_type: free-form
type: NEW_CAPABILITY
complexity: MEDIUM
---

# Feature: Integrate `agent-browser` Skill into diy-yt-creator-hyperframes

## Summary

Bring the `agent-browser` skill from the sister project (`C:\Users\Leex279\Documents\GitHub\diy-yt-creator`) into this HyperFrames video repo so that Claude can drive a real Chromium browser to (a) capture per-video screenshots/logos for use as visual assets, (b) QA rendered HyperFrames previews end-to-end, and (c) ground script-writing in real, current website content. The skill itself is a thin wrapper around the globally installed `agent-browser` CLI (v0.15.0, already on disk) — install is essentially a file copy plus permissions. The novel work is a thin **HyperFrames-aware adapter** (a new sub-playbook under `diy-yt-creator`) that knows the per-video asset convention (`videos/<slug>/assets/`), the brand-light/dark contrast rule, and how to QA the live preview server.

## User Story

As a video creator using this repo
I want Claude to be able to navigate, screenshot, and analyze real websites on my behalf
So that videos cite real visuals and stats (no fabrication), per-app screenshots in phase 3 cards stop falling back to mono-text, and I can ask Claude to QA the rendered composition by actually looking at it instead of just reading the HTML.

## Problem Statement

Today the `diy-yt-creator` skill cannot:

1. **Capture visual assets autonomously.** When the `new-anthropic-short.md` playbook needs an app's UI screenshot for a phase 3 timeline card, it can only fall back to logos in `shared/logos/` or styled mono-text — there is no path to navigate to the app's website and snapshot it. (`new-anthropic-short.md:267-274`)
2. **Ground the script in real source URLs.** Step 4 says "If facts would be fabricated, stop and ask the user for a source URL before proceeding" (`new-anthropic-short.md:13`) — but even when a URL is supplied, the agent has no way to *read* it. It can `WebFetch` static HTML, but JS-heavy sites render blank.
3. **QA the rendered composition.** The quality bar (`new-anthropic-short.md:241-249`) is "lint passes + inspect passes + audio wired." There's no verification that the composition *looks right* in the browser — Claude can't see the preview studio output.
4. **Compare against the source URL.** When building a website-driven video (`website-to-hyperframes`), there's no way to diff the composition against the real site for visual fidelity QA.

The sister project (`diy-yt-creator`, Remotion-based) solved this with `agent-browser` + a Python wrapper (`screenshot_capture_lib.py`) + a `/capture-screenshot` slash command — but those are tied to Remotion's `public/images/<composition>/` convention, not HyperFrames' `videos/<slug>/assets/`.

## Solution Statement

Copy the `agent-browser` skill verbatim from the sister project (it's framework-agnostic — just CLI bindings and references), mirror it into both `.claude/skills/` and `.agents/skills/` per existing repo convention, grant `Bash(agent-browser:*)` permission, then add a small set of HyperFrames-aware sub-playbooks under the existing `diy-yt-creator` skill that translate the generic skill into concrete per-video workflows. Wire those sub-playbooks into the `new-anthropic-short.md` playbook as **optional steps** (4.5 = capture assets, 11.5 = QA preview) — gated on whether the topic actually needs them, so simple text-only shorts skip the browser entirely.

Phase the work so that the minimal install (Phase A) is independently usable — the skill works on its own for ad-hoc browser tasks. Phases B and C layer on the HyperFrames-specific value.

## Metadata

| Field            | Value                                                                  |
| ---------------- | ---------------------------------------------------------------------- |
| Type             | NEW_CAPABILITY                                                         |
| Complexity       | MEDIUM                                                                 |
| Systems Affected | `.claude/skills/`, `.agents/skills/`, `.claude/settings.local.json`, `CLAUDE.md`, `diy-yt-creator` skill |
| Dependencies     | `agent-browser` CLI v0.15.0 (already installed globally), Playwright (bundled in CLI), Chromium (bundled) |
| Estimated Tasks  | 14 tasks across 3 phases (A: 6, B: 4, C: 4)                            |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║   USER: "Make a short about Anthropic's new MCP connectors"                    ║
║                                                                                ║
║   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                    ║
║   │  diy-yt-     │ ─► │  Draft       │ ─► │  Phase 3 card│                    ║
║   │  creator     │    │  script.txt  │    │  for "Slack" │                    ║
║   └──────────────┘    └──────────────┘    └──────┬───────┘                    ║
║                                                   │                            ║
║                                                   ▼                            ║
║                                          ┌──────────────┐                      ║
║                                          │ ls shared/   │                      ║
║                                          │ logos|grep   │                      ║
║                                          │ slack        │                      ║
║                                          └──────┬───────┘                      ║
║                                                   │                            ║
║                                                   ▼                            ║
║                                          ┌──────────────┐                      ║
║                                          │ Found logo?  │                      ║
║                                          │ → use it     │                      ║
║                                          │ Not found?   │                      ║
║                                          │ → mono-text  │                      ║
║                                          │   fallback   │                      ║
║                                          └──────────────┘                      ║
║                                                                                ║
║   USER_FLOW: Topic → script → (logo lookup) → mono-text fallback if missing    ║
║   PAIN_POINTS:                                                                 ║
║     1. No browser → can't fact-check claims against the source URL             ║
║     2. No screenshot → can't show app UI in cards (only the logo)              ║
║     3. No QA → can't verify the composition looks right                        ║
║     4. Mono-text fallback for any logo not in shared/logos/ (84 max)           ║
║   DATA_FLOW: topic → text-only → HTML composition (no visual grounding)        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║   USER: "Make a short about Anthropic's new MCP connectors"                    ║
║                                                                                ║
║   ┌──────────────┐    ┌──────────────┐                                         ║
║   │  diy-yt-     │ ─► │  Draft       │                                         ║
║   │  creator     │    │  script.txt  │                                         ║
║   └──────────────┘    └──────┬───────┘                                         ║
║                              │                                                 ║
║                              ▼                                                 ║
║                     ┌──────────────────┐                                       ║
║                     │ NEW: Optional    │ ◄── Triggered when script cites a     ║
║                     │ capture-asset    │     URL or names an app whose         ║
║                     │ sub-playbook     │     screenshot/logo isn't in shared/  ║
║                     └────┬─────────────┘                                       ║
║                          │ uses                                                ║
║                          ▼                                                     ║
║                     ┌──────────────────┐                                       ║
║                     │ agent-browser    │  open <url> + screenshot → PNG        ║
║                     │  (skill)         │  Output: videos/<slug>/assets/       ║
║                     └────┬─────────────┘                                       ║
║                          │                                                     ║
║                          ▼                                                     ║
║                     ┌──────────────────┐                                       ║
║                     │  Phase 3 card    │  <img src="assets/slack-ui.png">      ║
║                     │  for "Slack"     │  (real screenshot, not mono-text)     ║
║                     └────┬─────────────┘                                       ║
║                          │                                                     ║
║                          ▼                                                     ║
║                     ┌──────────────────┐                                       ║
║                     │ lint + inspect   │                                       ║
║                     └────┬─────────────┘                                       ║
║                          │                                                     ║
║                          ▼                                                     ║
║                     ┌──────────────────┐                                       ║
║                     │ NEW: Optional    │ ◄── agent-browser opens preview URL,  ║
║                     │ qa-composition   │     snapshots each phase, reports     ║
║                     │ sub-playbook     │     overflow / contrast / layout      ║
║                     └────┬─────────────┘                                       ║
║                          │                                                     ║
║                          ▼                                                     ║
║                     ┌──────────────────┐                                       ║
║                     │  Report to user  │  Preview URL + QA notes               ║
║                     └──────────────────┘                                       ║
║                                                                                ║
║   USER_FLOW: Topic → script → (auto-capture missing visuals) → composition →  ║
║              (auto-QA preview) → report                                        ║
║   VALUE_ADD:                                                                   ║
║     1. Real visual grounding for any app, not limited to 84 shared logos       ║
║     2. Source URL fact-checking via agent-browser snapshot/get-text            ║
║     3. Visual QA — Claude actually sees the rendered preview                   ║
║     4. agent-browser available for ANY ad-hoc browser task in this repo        ║
║   DATA_FLOW: topic → web-grounded text + per-video PNGs → composition          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                                              | Before                                    | After                                                                                | User Impact                                                                                              |
| ----------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Any task needing browser                              | No skill — Claude can't navigate JS sites | `/agent-browser` skill auto-loads when user says "open / screenshot / scrape / fill" | Ad-hoc browser tasks now work without leaving the chat                                                   |
| `diy-yt-creator/new-anthropic-short.md` step 4        | "ask user for source URL"                 | "ask user for source URL → optionally agent-browser open + get text"                 | Script drafting is grounded in real page content (not a `WebFetch` of static HTML which fails on JS SPAs) |
| `diy-yt-creator/new-anthropic-short.md` step 8 (cards) | `ls shared/logos | grep <app>` only       | Logo check first, then optional `agent-browser screenshot <app-url>` if no logo      | Phase 3 cards show real UIs for any app, not just the 84 in `shared/logos/`                              |
| `diy-yt-creator/new-anthropic-short.md` step 11 (preview) | "preview opens in browser, done"          | Preview opens **and** QA sub-playbook can be triggered to snapshot each phase        | Optional automated visual QA before user manually inspects                                               |
| `videos/<slug>/assets/`                                | Documented but empty                      | Populated with per-video PNGs, named `<app-or-page>.png`                              | Asset folder fulfills its documented purpose                                                             |
| `.claude/settings.local.json`                          | `{}` (no permissions)                     | Adds `Bash(agent-browser:*)` and `Bash(npx agent-browser:*)`                          | No permission prompts every time                                                                         |

---

## Mandatory Reading

**Before starting any task, the implementer MUST read these files completely.**

| Priority | File                                                                                                | Lines | Why Read This                                                                                              |
| -------- | --------------------------------------------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------- |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\skills\agent-browser\SKILL.md`            | all   | The skill file to copy. Contains frontmatter (name, description, allowed-tools), command reference, gotchas |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\CLAUDE.md`                            | all   | Project conventions — skills table, commands list, key rules. New skill must be added here.                |
| P0       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\.claude\skills\diy-yt-creator\SKILL.md` | all   | Router — new sub-playbooks must be registered in its commands table                                        |
| P1       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\.claude\skills\diy-yt-creator\new-anthropic-short.md` | all   | Playbook to extend. Insertion points: step 4 (script grounding), step 8 (phase 3 cards), step 11 (preview QA) |
| P1       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\.claude\settings.json`                | all   | Existing hooks. The PostToolUse `Bash` hook fires on every `agent-browser` call — verify the sync script tolerates it |
| P1       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\.claude\settings.local.json`          | all   | `{}` empty — needs the permissions block added                                                              |
| P1       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\shared\README.md`                     | all   | Asset organization rules — explicitly forbids per-video screenshots in `shared/`. Confirms the per-video `assets/` convention |
| P2       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\skills\agent-browser\references\commands.md` | all   | Full command surface for agent-browser. The QA sub-playbook will use `snapshot -i`, `get text`, `screenshot --full`, `diff`. |
| P2       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\commands\capture-screenshot.md`           | all   | Sister project's higher-level wrapper around agent-browser. **Do NOT copy as-is** — its paths are Remotion-tied. Use it as a *reference* for cookie-dismissal patterns and obstacle-removal JS, then adapt to HyperFrames paths. |
| P2       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\skills\agent-browser\templates\capture-workflow.sh` | all   | Bash template showing the canonical capture sequence (open → wait networkidle → screenshot --full)         |
| P2       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\videos\claude-connectors-everyday-life\index.html` | scan for `<img>` and `assets/` | Reference example. Currently only references `../../shared/logos/anthropic-logo-light.svg` (line ~416). New videos can also use `assets/<name>.png` |
| P2       | `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\scripts\sync-shared-assets.sh`         | all   | Existing PostToolUse hook script. Confirms it doesn't crash when called from a Bash that just ran `agent-browser` |

**No external documentation** — `agent-browser` is a single CLI binary with all docs bundled in the skill files we're copying. The repo `vercel-labs/agent-browser` on GitHub is the upstream source (referenced in `update-from-source.sh`), but no live HTTP fetch is needed at install time.

---

## Patterns to Mirror

### NAMING_CONVENTION (skill files)

```yaml
# SOURCE: C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\.claude\skills\diy-yt-creator\SKILL.md:1-4
# COPY THIS PATTERN for any new skill SKILL.md frontmatter:
---
name: <kebab-case-skill-name>
description: Use when <triggering condition>. Include explicit trigger phrases the user might say.
---
```

### SKILL_FRONTMATTER_WITH_ALLOWED_TOOLS

```yaml
# SOURCE: C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\skills\agent-browser\SKILL.md:1-5
# COPY THIS PATTERN — agent-browser SKILL.md needs the allowed-tools line:
---
name: agent-browser
description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction.
allowed-tools: Bash(npx agent-browser:*), Bash(agent-browser:*)
---
```

### SKILL_ROUTER_TABLE

```markdown
<!-- SOURCE: .claude/skills/diy-yt-creator/SKILL.md:21-25 -->
<!-- COPY THIS PATTERN to add new sub-playbook rows: -->
## Available commands

| Command | Template used | Use when |
|---|---|---|
| [new-anthropic-short.md](./new-anthropic-short.md) | `templates/shorts/anthropic/` | User wants a vertical YouTube Short ... |
| [capture-asset.md](./capture-asset.md) | n/a (uses `agent-browser`) | User needs a per-video screenshot/logo from a URL into `videos/<slug>/assets/` |
| [qa-composition.md](./qa-composition.md) | n/a (uses `agent-browser`) | After `hyperframes preview` is running, agent should snapshot each phase to verify visually |
```

### CLAUDE_MD_SKILLS_TABLE_ENTRY

```markdown
<!-- SOURCE: CLAUDE.md:7-13 -->
<!-- ADD A ROW: -->
| **agent-browser**          | `/agent-browser`          | Driving a real Chromium browser — open URL, snapshot DOM/refs, click, fill, screenshot, scrape, QA. Use directly OR as a building block inside other skills. |
```

### SETTINGS_PERMISSIONS_BLOCK

```jsonc
// SOURCE: C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\settings.local.json (the working pattern in the sister project)
// COPY THIS SHAPE into our currently-empty .claude/settings.local.json:
{
  "permissions": {
    "allow": [
      "Bash(agent-browser:*)",
      "Bash(npx agent-browser:*)",
      "WebFetch(domain:agent-browser.dev)"
    ]
  }
}
```

> If the file already has other keys later, merge — do NOT overwrite siblings.

### CAPTURE_SEQUENCE (canonical)

```bash
# SOURCE: C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\skills\agent-browser\templates\capture-workflow.sh
# COPY THIS PATTERN inside capture-asset.md:
agent-browser open "$URL" \
  && agent-browser wait --load networkidle \
  && agent-browser eval "document.querySelectorAll('[id*=cookie], [class*=cookie], [id*=consent]').forEach(e => e.remove())" \
  && agent-browser screenshot --full "$OUTPUT_PNG"
```

### PLAYBOOK_STEP_STRUCTURE

```markdown
<!-- SOURCE: .claude/skills/diy-yt-creator/new-anthropic-short.md:31-49 -->
<!-- COPY THIS HEADING / CODE-BLOCK / VERIFICATION STYLE for new steps: -->
### N. Short verb-first title

Brief one-sentence what.

```bash
the actual command
```

PowerShell: `Powershell-equivalent`

Verify: `cmd to confirm` should `expected output`.
```

### DON'TS_LIST (extension)

```markdown
<!-- SOURCE: .claude/skills/diy-yt-creator/new-anthropic-short.md:280-291 -->
<!-- ADD ENTRIES MATCHING EXISTING TONE — terse, imperative: -->
- Never `agent-browser` against `localhost` or internal IPs without an explicit user request — only public URLs by default.
- Never store captured PNGs in `shared/` — they belong in `videos/<slug>/assets/` per `shared/README.md:43`.
- Never run `agent-browser` against the same URL more than once per video without a force flag — repeated captures are wasteful and may rate-limit.
```

---

## Files to Change

| File                                                                                | Action | Phase | Justification                                                                                                                          |
| ----------------------------------------------------------------------------------- | ------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `.claude/skills/agent-browser/SKILL.md`                                             | CREATE | A     | Copy from sister project — primary skill file                                                                                          |
| `.claude/skills/agent-browser/references/authentication.md`                         | CREATE | A     | Copy from sister project — login/2FA workflows                                                                                         |
| `.claude/skills/agent-browser/references/commands.md`                               | CREATE | A     | Copy from sister project — full command reference                                                                                      |
| `.claude/skills/agent-browser/references/profiling.md`                              | CREATE | A     | Copy from sister project — Chrome DevTools profiling                                                                                   |
| `.claude/skills/agent-browser/references/proxy-support.md`                          | CREATE | A     | Copy from sister project — proxy config                                                                                                |
| `.claude/skills/agent-browser/references/session-management.md`                     | CREATE | A     | Copy from sister project — sessions and state                                                                                          |
| `.claude/skills/agent-browser/references/snapshot-refs.md`                          | CREATE | A     | Copy from sister project — `@eN` ref lifecycle                                                                                         |
| `.claude/skills/agent-browser/references/video-recording.md`                        | CREATE | A     | Copy from sister project — WebM recording (useful for HyperFrames preview QA)                                                          |
| `.claude/skills/agent-browser/templates/authenticated-session.sh`                   | CREATE | A     | Copy from sister project — login + state reuse template                                                                                |
| `.claude/skills/agent-browser/templates/capture-workflow.sh`                        | CREATE | A     | Copy from sister project — full page capture template                                                                                  |
| `.claude/skills/agent-browser/templates/form-automation.sh`                         | CREATE | A     | Copy from sister project — form filling template                                                                                       |
| `.claude/skills/agent-browser/update-from-source.sh`                                | CREATE | A     | Copy from sister project (`.claude/commands/agent-browser/update-from-source.sh`) — pulls future updates from `vercel-labs/agent-browser` |
| `.agents/skills/agent-browser/**`                                                   | CREATE | A     | Mirror everything in `.claude/skills/agent-browser/` — repo convention (10 existing skills are mirrored in both locations)              |
| `.claude/settings.local.json`                                                       | UPDATE | A     | Add `permissions.allow` block with `Bash(agent-browser:*)`, `Bash(npx agent-browser:*)`, `WebFetch(domain:agent-browser.dev)`           |
| `CLAUDE.md`                                                                         | UPDATE | A     | Add `agent-browser` row to the skills table (line 7-13). One row, terse.                                                                |
| `.claude/skills/diy-yt-creator/capture-asset.md`                                    | CREATE | B     | New sub-playbook: take URL → save to `videos/<slug>/assets/<name>.png` with cookie-dismissal, viewport sizing, dark-mode hint, validation |
| `.claude/skills/diy-yt-creator/qa-composition.md`                                   | CREATE | B     | New sub-playbook: open `hyperframes preview` URL, snapshot each phase by jumping to its `data-start`, save under `videos/<slug>/qa/`, report findings |
| `.claude/skills/diy-yt-creator/SKILL.md`                                            | UPDATE | B     | Add two new rows to commands table at line 21-25 + extend "When to invoke" trigger list                                                |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                              | UPDATE | C     | Insert step 4.5 (optional source-URL capture for script grounding), step 8.5 (optional per-app screenshot for phase 3 cards), step 11.5 (optional QA sweep). All three are *optional* — playbook still works without browser. |

> **`scripts/sync-shared-assets.sh`** — verify (do NOT modify) that the PostToolUse hook in `.claude/settings.json:4-15` (which runs on every Bash) doesn't break when the Bash is `agent-browser screenshot ...`. Expectation: it just rescans `shared/` and finds nothing new (because new PNGs go to `videos/<slug>/assets/`, not `shared/`). If it errors, the fix is to scope its trigger differently — but that's a follow-up, not part of this plan.

---

## NOT Building (Scope Limits)

Explicit exclusions to prevent scope creep:

- **No Python wrapper port.** The sister project has `screenshot_capture_lib.py` and `capture-screenshots.py` that drive a JSON manifest. Tempting to port, but the manifest format (`src/<Name>/images/screenshots.json`) is Remotion-shaped. HyperFrames doesn't need batch capture — videos in this repo are smaller-scope (1 video = 1-3 captures max). Defer until we have a video that genuinely needs ≥5 captures.
- **No `/capture-screenshot` slash command.** The sister project has one (`.claude/commands/capture-screenshot.md`) with hard-coded Remotion paths. Replicating it as a HyperFrames slash command duplicates what `capture-asset.md` (sub-playbook under `diy-yt-creator`) already does. If a top-level slash command is wanted later, add it then.
- **No `browser-screencast` skill.** The sister project has a parallel CDP-based screencast skill that produces WebM + manifest for video sync. Different mechanism, different use case (recording user flows for embedding). Out of scope — propose separately if a video needs it.
- **No replacement of `npx hyperframes capture`.** The `website-to-hyperframes` skill uses `npx hyperframes capture` (built into the HyperFrames CLI). It produces structured extraction (tokens, animations, lottie manifests) that `agent-browser` doesn't. Keep both; document the choice in `capture-asset.md` as: "use `npx hyperframes capture` for full-site extraction, use `agent-browser` for spot screenshots and QA."
- **No iOS simulator support.** `agent-browser -p ios` requires Appium + Xcode + macOS. This is Windows. The skill files reference iOS support but we won't enable or test that path.
- **No `agent-browser.json` project config.** The sister project doesn't ship one either. Settings via env vars or CLI flags as needed.
- **No automatic invocation hooks.** Don't add a SessionStart or PostToolUse hook that pre-warms the browser daemon. The daemon starts on first command, fast enough.
- **No modification to existing videos.** `videos/claude-connectors-everyday-life/` stays as is. Pattern applies to *new* videos only.
- **No automated `agent-browser` calls during `npx hyperframes lint/inspect/preview`.** These are existing CLI commands, untouched.

---

## Step-by-Step Tasks

Execute in order. Tasks within a phase can be done in any sequence; phases are dependency-ordered.

### Phase A — Install the skill (independently usable)

#### Task A1: COPY agent-browser skill files into `.claude/skills/agent-browser/`

- **ACTION**: COPY 12 files from `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\skills\agent-browser\` into `C:\Users\Leex279\Documents\GitHub\diy-yt-creator-hyperframes\.claude\skills\agent-browser\` preserving directory layout.
- **IMPLEMENT**: `cp -r ../diy-yt-creator/.claude/skills/agent-browser .claude/skills/` (or PowerShell `Copy-Item -Recurse`). Files to land: `SKILL.md`, `references/{authentication,commands,profiling,proxy-support,session-management,snapshot-refs,video-recording}.md`, `templates/{authenticated-session,capture-workflow,form-automation}.sh`. The skills-copy in the sister project does NOT include `update-from-source.sh` — pull that from the commands-copy: `cp ../diy-yt-creator/.claude/commands/agent-browser/update-from-source.sh .claude/skills/agent-browser/`.
- **MIRROR**: existing skills in `.claude/skills/{music,sound-effects,text-to-speech,...}` — same shape (SKILL.md + optional references/ + optional templates/).
- **GOTCHA**: The skills copy is the more complete version (has `references/profiling.md` + auth-vault content). Do NOT copy from `.claude/commands/agent-browser/` instead — that version is older.
- **VALIDATE**: `ls .claude/skills/agent-browser/` lists `SKILL.md`, `references/`, `templates/`, `update-from-source.sh`. `head -5 .claude/skills/agent-browser/SKILL.md` shows the frontmatter ending with `allowed-tools: Bash(npx agent-browser:*), Bash(agent-browser:*)`.

#### Task A2: MIRROR into `.agents/skills/agent-browser/`

- **ACTION**: COPY the same 12 files into `.agents/skills/agent-browser/`.
- **IMPLEMENT**: `cp -r .claude/skills/agent-browser .agents/skills/`.
- **MIRROR**: every other skill is mirrored across both locations — confirmed by `ls .claude/skills/ && ls .agents/skills/` showing identical 9 directories (10 in `.claude/skills/` because `diy-yt-creator` is `.claude/skills/`-only — that asymmetry is pre-existing and intentional).
- **GOTCHA**: don't symlink — sub-agents and other harnesses may not follow symlinks. Plain copy.
- **VALIDATE**: `diff -r .claude/skills/agent-browser .agents/skills/agent-browser` produces no output.

#### Task A3: UPDATE `.claude/settings.local.json` with permissions

- **ACTION**: Replace the empty `{}` with a permissions block that pre-allows `agent-browser` invocations.
- **IMPLEMENT**: Use Edit tool. Replace file contents with:
  ```json
  {
    "permissions": {
      "allow": [
        "Bash(agent-browser:*)",
        "Bash(npx agent-browser:*)",
        "WebFetch(domain:agent-browser.dev)"
      ]
    }
  }
  ```
- **MIRROR**: `C:\Users\Leex279\Documents\GitHub\diy-yt-creator\.claude\settings.local.json` lines 168-170 — same shape, just the relevant subset.
- **GOTCHA**: This is a local settings file — git status currently shows it as untracked. That's fine; it stays untracked (per gitignore convention for `.local.json`). Don't add it to git.
- **VALIDATE**: `cat .claude/settings.local.json | python -m json.tool` parses without error. Open Claude Code, run `agent-browser --version` via Bash — no permission prompt.

#### Task A4: VERIFY agent-browser CLI is installed

- **ACTION**: Confirm the CLI binary is on PATH at the expected version.
- **IMPLEMENT**: `which agent-browser && agent-browser --version`.
- **EXPECT**: `/c/Users/Leex279/.npm-global/agent-browser` and `agent-browser 0.15.0` (already verified at planning time — re-check before proceeding in case the user upgrades or reinstalls).
- **GOTCHA**: If missing, reinstall: `npm install -g agent-browser` (or `pnpm add -g agent-browser` per the global PNPM rule in `~/.claude/CLAUDE.md`). The skill SKILL.md frontmatter allows both `agent-browser:*` and `npx agent-browser:*` — `npx` works as a fallback when global install is missing.
- **VALIDATE**: Both commands return success.

#### Task A5: SMOKE-TEST the skill end-to-end

- **ACTION**: Run a non-destructive capture against a stable URL to prove the skill loads, the daemon starts, the screenshot writes.
- **IMPLEMENT**:
  ```bash
  cd /tmp && agent-browser open https://example.com \
    && agent-browser wait --load networkidle \
    && agent-browser screenshot /tmp/agent-browser-smoke.png \
    && ls -lh /tmp/agent-browser-smoke.png
  ```
- **EXPECT**: PNG file ≥10KB at the expected path. No permission prompts (Task A3 should have eliminated them). No errors about missing Chromium.
- **GOTCHA**: First run downloads Chromium if not yet cached — may take 30-60s. Second run is fast (<5s).
- **VALIDATE**: File exists, opens correctly in any image viewer.

#### Task A6: UPDATE `CLAUDE.md` skills table with the new entry

- **ACTION**: Add one row to the table at lines 7-13 of `CLAUDE.md`.
- **IMPLEMENT**: Use Edit tool. Insert after the `gsap` row:
  ```markdown
  | **agent-browser**          | `/agent-browser`          | Real Chromium browser — open URL, snapshot DOM, click, fill, screenshot, scrape, QA. Use directly or as a building block inside other skills. |
  ```
- **MIRROR**: existing rows at `CLAUDE.md:9-13` — preserve column alignment with surrounding rows (or use any consistent style; markdown tables don't require pixel-perfect alignment, but keep it readable).
- **VALIDATE**: `grep -n "agent-browser" CLAUDE.md` returns the new line. The skills table renders with one extra row.

**Phase A acceptance**: After A1-A6, the user can type `/agent-browser` (or any phrase that triggers the SKILL description) and Claude will load the skill, drive the browser, and complete tasks like "open https://github.com/anthropic/claude-code and screenshot the README." No HyperFrames-specific awareness yet — that's Phase B.

---

### Phase B — HyperFrames-aware adapter sub-playbooks

#### Task B1: CREATE `.claude/skills/diy-yt-creator/capture-asset.md`

- **ACTION**: Author a new sub-playbook for the `diy-yt-creator` skill that wraps `agent-browser` for the per-video screenshot use case.
- **IMPLEMENT**: New markdown file with this structure (full content — no placeholders):

  ```markdown
  # capture-asset — Sub-playbook

  Capture a per-video visual asset (app UI screenshot, page hero, logo from a brand site)
  and save it to `videos/<slug>/assets/<name>.png` ready to reference from `index.html`.

  Wraps the `agent-browser` skill with HyperFrames conventions: per-video isolation,
  cookie-banner dismissal, dark-mode hinting (the Anthropic template is dark-stage, so
  we prefer the site's dark theme when available), validation, and reproducibility.

  ## Inputs

  - **slug**: the video folder name (must already exist under `videos/<slug>/`)
  - **url**: the source URL (must be publicly accessible; no localhost without explicit user OK)
  - **name**: kebab-case filename (no extension), e.g. `slack-channel-ui`. PNG is appended.
  - **mode** (optional): `full` (full-page, default), `viewport` (1080x1920 fold only), `element` (requires `selector`)
  - **scheme** (optional): `dark` (default for the Anthropic template), `light`
  - **selector** (optional): CSS selector if `mode=element`, or to scroll-to before capturing

  ## Steps

  ### 1. Verify the target

  - `ls videos/<slug>/index.html` exists. If not, stop — capture-asset only runs against existing video projects.
  - `mkdir -p videos/<slug>/assets`.
  - If `videos/<slug>/assets/<name>.png` already exists and the user did NOT pass `--force`, ask before overwriting.

  ### 2. Capture

  Use the `/agent-browser` skill. Canonical chained call:

  ```bash
  agent-browser open "<url>" \
    && agent-browser wait --load networkidle \
    && agent-browser eval "document.querySelectorAll('[id*=cookie i], [class*=cookie i], [id*=consent i], [class*=consent i], [class*=banner i][class*=cookie i], [aria-label*=cookie i]').forEach(e => e.remove()); document.documentElement.style.setProperty('color-scheme', '<scheme>');" \
    && agent-browser screenshot --full "videos/<slug>/assets/<name>.png"
  ```

  For `mode=viewport`: drop `--full` and prepend `agent-browser viewport 1080 1920`.
  For `mode=element` + selector: replace the screenshot line with `agent-browser screenshot @<ref>` after `agent-browser snapshot -i` and identifying the matching ref.

  ### 3. Validate

  ```bash
  ls -lh videos/<slug>/assets/<name>.png
  ```

  - File must exist and be ≥10KB. <10KB usually means a blank page or a redirect to an interstitial.
  - If too small, retry once with `agent-browser wait --load networkidle && agent-browser wait 2000 && agent-browser screenshot --full ...` (extra 2s for animations).
  - If still too small, stop and ask the user — the page may require auth or have anti-bot protection.

  ### 4. Report

  One line: `Captured <name>.png (<size>KB) from <url> → videos/<slug>/assets/<name>.png`.
  Then suggest the `<img>` tag for the user to splice into `index.html`:

  ```html
  <img src="assets/<name>.png" alt="<descriptive alt>" />
  ```

  ## Don'ts

  - Never store captures in `shared/` (per `shared/README.md:43`).
  - Never capture localhost / 127.0.0.1 / internal IPs without explicit user approval.
  - Never re-capture a URL within the same video without `--force` (waste + rate limit risk).
  - Never use `agent-browser screenshot` without prior `wait --load networkidle` — you'll capture the loading skeleton.
  - Never modify the captured PNG (no resize, no compression) — `npx hyperframes inspect` works on raw output and the framework handles scaling.
  ```

- **MIRROR**: structure of `.claude/skills/diy-yt-creator/new-anthropic-short.md` — same heading hierarchy (`# title — Subtype`, `## Inputs`, `## Steps` numbered with `### N. Verb`, `## Don'ts`).
- **GOTCHA**: The cookie-dismissal `eval` uses CSS attribute-selector case-insensitive matching (`[id*=cookie i]`). Verify your `agent-browser eval` supports this (modern Chromium does). If not, use `[id*="cookie"], [id*="Cookie"], [id*="COOKIE"]` triple form.
- **VALIDATE**: File exists, is well-formed markdown, frontmatter not needed (sub-playbooks under a skill don't need frontmatter — only the skill router has it).

#### Task B2: CREATE `.claude/skills/diy-yt-creator/qa-composition.md`

- **ACTION**: Author a sub-playbook that opens the running `hyperframes preview` server, jumps to each phase's `data-start` time, screenshots, and reports findings.
- **IMPLEMENT**: New markdown file with this structure:

  ```markdown
  # qa-composition — Sub-playbook

  After `npx hyperframes preview videos/<slug>` is running (it prints a URL like
  `http://localhost:3002/api/projects/<slug>/preview`), use `agent-browser` to
  visually QA the rendered composition by jumping to each phase's start time and
  snapshotting the rendered output.

  Complements `npx hyperframes lint` and `npx hyperframes inspect` (which check
  HTML/layout statically); this skill checks the *rendered visual output*.

  ## Inputs

  - **slug**: the video folder name
  - **preview_url**: the URL printed by `hyperframes preview` (defaults to `http://localhost:3002/api/projects/<slug>/preview`)

  ## Steps

  ### 1. Verify preview is running

  ```bash
  curl -fsS -o /dev/null "<preview_url>" && echo OK
  ```

  If not 200, ask the user to run `npx hyperframes preview videos/<slug>` first.

  ### 2. Read phase boundaries from index.html

  Parse `videos/<slug>/index.html` for elements with `data-start` and `data-duration`.
  Build a list `[{phase: "intro", start_s: 0, duration_s: 4}, ...]`. The exact selector
  depends on the template — for the Anthropic shorts template, look for top-level
  `data-track-index="0"` clips at known IDs (`#intro`, `#phase-2`, `#phase-3`, `#outro`).

  ### 3. Capture each phase

  Create `videos/<slug>/qa/` if it doesn't exist. For each phase:

  ```bash
  agent-browser open "<preview_url>?t=<start_s>" \
    && agent-browser wait 500 \
    && agent-browser viewport 1080 1920 \
    && agent-browser screenshot "videos/<slug>/qa/phase-<name>-t<start_s>.png"
  ```

  > Check that the preview server supports `?t=<seconds>` query for time-jump. If it
  > doesn't, fall back to `agent-browser eval "window.__timelines && Object.values(window.__timelines).forEach(tl => tl.seek(<start_s>))"` after open + wait.

  ### 4. Analyze

  For each captured PNG, run `agent-browser` against the file (or just inspect via
  Read tool — PNGs render in the chat). Specifically check:

  - Text not clipped or overflowing the safe area
  - Logos rendered (no broken-image icons)
  - Phase 3 cards have all expected elements
  - Top banner present
  - No leftover template placeholders ("DUMBER?", template stat numbers)

  ### 5. Report

  Bullet list per phase: `phase-N: [PASS|FAIL: reason]`. If any FAIL, link the PNG
  path so the user can see the issue. Recommend specific edits (e.g. "phase-3 stat pill
  3 overflows by ~12px on the right — reduce font-size from 64px → 56px").

  ## Don'ts

  - Never claim PASS without actually viewing the PNG (it must be Read into the chat or
    described from `agent-browser get text` output).
  - Never modify `index.html` from this sub-playbook — qa-composition is read-only,
    suggestions only. Edits go through the user or back to `new-anthropic-short` step 8.
  - Never capture against the rendered MP4 (`videos/<slug>/out/short.mp4`) — that's a
    different artifact; qa-composition is for the live preview only.
  - Never delete `videos/<slug>/qa/` automatically — keep snapshots for reference.
  ```

- **MIRROR**: same shape as `capture-asset.md`; tone matches existing `new-anthropic-short.md` don'ts list.
- **GOTCHA**: Whether `?t=<seconds>` works is a hyperframes preview server detail — not certain. The fallback (`agent-browser eval` + `window.__timelines.seek()`) is documented in the project's `CLAUDE.md:99-103` (timelines are exposed on `window.__timelines`). Use the fallback by default and let the user discover/document the preview-URL trick separately.
- **VALIDATE**: File exists, structure mirrors capture-asset.md.

#### Task B3: UPDATE `.claude/skills/diy-yt-creator/SKILL.md` to register the two new sub-playbooks

- **ACTION**: Add two rows to the commands table at lines 21-25 and extend the "When to invoke" trigger list at lines 12-17.
- **IMPLEMENT**: Use Edit tool. Two edits:

  Edit 1 — extend trigger list. Current `SKILL.md:12-17`:
  ```
  - "create / make / spawn a new short / video"
  - "new anthropic short about X"
  - "/diy-yt-creator:new-anthropic-short …"
  - Anything that asks to scaffold a video from a template in this repo
  ```

  Add lines:
  ```
  - "capture / screenshot <url> for video <slug>" (uses `capture-asset`)
  - "QA / check / verify the preview for <slug>" (uses `qa-composition`)
  ```

  Edit 2 — extend commands table. Current `SKILL.md:21-25`:
  ```markdown
  | Command | Template used | Use when |
  |---|---|---|
  | [new-anthropic-short.md](./new-anthropic-short.md) | `templates/shorts/anthropic/` | User wants a vertical YouTube Short ... |
  ```

  Add rows:
  ```markdown
  | [capture-asset.md](./capture-asset.md) | n/a (uses `agent-browser`) | Per-video screenshot/asset from a public URL into `videos/<slug>/assets/` |
  | [qa-composition.md](./qa-composition.md) | n/a (uses `agent-browser`) | Visually QA a running `hyperframes preview` — snapshot each phase, report issues |
  ```

- **MIRROR**: existing row formatting in `SKILL.md:23`.
- **VALIDATE**: `grep -n "capture-asset\|qa-composition" .claude/skills/diy-yt-creator/SKILL.md` returns 4 matches (2 trigger lines + 2 table rows).

#### Task B4: SMOKE-TEST capture-asset against the existing video

- **ACTION**: Use `capture-asset` to grab a logo/screenshot for `videos/claude-connectors-everyday-life/` without modifying its `index.html` — pure smoke test.
- **IMPLEMENT**: User invokes `/diy-yt-creator capture-asset claude-connectors-everyday-life https://www.anthropic.com/news/connectors anthropic-news-page`. Resulting file: `videos/claude-connectors-everyday-life/assets/anthropic-news-page.png`.
- **EXPECT**: PNG exists, ≥50KB (typical for a real page).
- **GOTCHA**: `videos/claude-connectors-everyday-life/index.html` shows as modified in `git status` already — DO NOT edit it as part of this smoke test. The smoke test produces a new file in `assets/`, nothing else.
- **VALIDATE**: `ls -lh videos/claude-connectors-everyday-life/assets/anthropic-news-page.png`. After verification, optionally `git status` should show the new file as untracked. Delete with `rm` after the smoke test if the user doesn't want it kept.

**Phase B acceptance**: After B1-B4, `diy-yt-creator` knows three commands (new-anthropic-short, capture-asset, qa-composition) and the latter two work end-to-end against any public URL or running preview server.

---

### Phase C — Wire optional steps into `new-anthropic-short.md`

#### Task C1: ADD optional step 4.5 to `new-anthropic-short.md` — script grounding

- **ACTION**: Insert a new step between the existing step 4 (draft script) and step 5 (TTS) that *optionally* uses `agent-browser` to read the source URL.
- **IMPLEMENT**: Use Edit tool. After step 4's body, before step 5:

  ```markdown
  ### 4.5. (Optional) Ground the script in real source content

  Skip if: the topic is text-only opinion / commentary, OR the user already provided
  full key facts verbatim, OR the source is reachable via plain `WebFetch` (static
  HTML, e.g. a release-notes Markdown page on GitHub).

  Use when: the source is a JS-rendered page (SPA, dashboard, blog with dynamic
  content), or you need to verify a specific stat / quote / version number against
  the current state of the page (anti-fabrication rule).

  Sub-playbook: `/diy-yt-creator capture-asset` won't help — that's for visuals. For
  text grounding, invoke `/agent-browser` directly:

  ```bash
  agent-browser open "<source_url>" \
    && agent-browser wait --load networkidle \
    && agent-browser get text body
  ```

  Read the output. Cross-check every stat / date / quote in your draft `script.txt`
  against this text. If a fact in the script can't be found in the page text,
  remove it or ask the user. NEVER preserve a fabricated fact just because the
  draft was already written.
  ```

- **MIRROR**: heading style matches existing steps (`### N. Verb-first title`); the "Skip if" / "Use when" pattern is novel but reads well in this playbook's voice — confirm with user if unsure.
- **GOTCHA**: Step numbering. Existing steps are `### 1.` through `### 12.`. Inserting `### 4.5` keeps later steps numbered as-is (no renumbering). If the user prefers no decimal steps, alternatives are: (a) renumber all subsequent (high churn), (b) call it `### 4a.` (less common in repo). Pick `### 4.5.` — minimal blast radius.
- **VALIDATE**: `grep -n "^### " .claude/skills/diy-yt-creator/new-anthropic-short.md` shows the new heading inserted between existing 4 and 5.

#### Task C2: ADD step 8.5 reference to capture-asset for phase 3 cards

- **ACTION**: Insert a note after step 8.6 (phase 3 card editing) referencing `capture-asset` for missing logos.
- **IMPLEMENT**: Use Edit tool. Find the section discussing phase 3 timeline cards (around `new-anthropic-short.md:267-274`, the "Workflow inside step 8" block) and add a bullet to the existing fallback ladder:

  Current bullet 3:
  ```
  3. If a logo does NOT exist, do NOT fabricate one. Either:
     - Ask the user for the logo file (preferred), OR
     - Fall back to the styled mono-text app name (current default in the template), OR
     - Pick a different app already in `shared/logos/` IF the script-content allows substitution without losing factual accuracy.
  ```

  Add as the first sub-option:
  ```
  3. If a logo does NOT exist, do NOT fabricate one. Either:
     - Run `/diy-yt-creator capture-asset <slug> <app_homepage_url> <app>-screenshot` to grab a UI screenshot (lands in `videos/<slug>/assets/<app>-screenshot.png`). Reference as `<img src="assets/<app>-screenshot.png" alt="<App>">`. Use sparingly — screenshots are heavier than logos and may distract from the card composition. OR
     - Ask the user for the logo file (preferred for brand consistency), OR
     - Fall back to the styled mono-text app name (current default in the template), OR
     - Pick a different app already in `shared/logos/` IF the script-content allows substitution without losing factual accuracy.
  ```

- **MIRROR**: bullet structure preserved; tone matches the surrounding "Either / OR" ladder.
- **GOTCHA**: Position the new sub-option *first* so the agent considers it before the user-ask fallback. The user-ask fallback should still exist — capture-asset can fail (auth-walled apps, anti-bot).
- **VALIDATE**: The Workflow block reads cleanly with the new option.

#### Task C3: ADD optional step 11.5 to `new-anthropic-short.md` — preview QA

- **ACTION**: Insert a new step between step 11 (preview) and step 12 (report) that *optionally* runs the qa-composition sub-playbook.
- **IMPLEMENT**: Use Edit tool. After step 11's body, before step 12:

  ```markdown
  ### 11.5. (Optional) QA the rendered preview visually

  Skip if: lint and inspect both passed cleanly AND the user wants a fast turnaround.

  Use when: the composition involves new content patterns (custom animations, novel
  card layouts, atypical font sizes), OR the user explicitly asks "verify the preview".

  Sub-playbook: `/diy-yt-creator qa-composition <slug>`. It will use `agent-browser`
  to snapshot each phase from the running preview server and report any visual issues
  (overflow, missing assets, broken image icons, leftover template placeholders).

  Do NOT block on this step — it's advisory. Report findings in step 12.
  ```

- **MIRROR**: same `Skip if / Use when` structure introduced in step 4.5.
- **GOTCHA**: This step assumes the preview server (`hyperframes preview`) is still running from step 11. If the user closed it, qa-composition will fail at its step 1 — that's expected behavior (the sub-playbook handles it gracefully).
- **VALIDATE**: `grep -n "^### " .claude/skills/diy-yt-creator/new-anthropic-short.md` shows new headings 4.5, 11.5 inserted correctly.

#### Task C4: ADD agent-browser don'ts to the playbook's Don'ts section

- **ACTION**: Append three new bullets to the existing Don'ts list at `new-anthropic-short.md:280-291`.
- **IMPLEMENT**: Use Edit tool. After the last existing don't:

  ```markdown
  - Never run `agent-browser` against `localhost` or internal IPs without explicit user approval — only public URLs by default.
  - Never store captured PNGs in `shared/` — they belong in `videos/<slug>/assets/` per `shared/README.md:43`.
  - Never re-run `capture-asset` against the same URL for the same video without `--force` — wasteful and may rate-limit.
  ```

- **MIRROR**: existing terse imperative tone (existing entries: "Never auto-render. Never fabricate stats. ...").
- **VALIDATE**: `tail -20 .claude/skills/diy-yt-creator/new-anthropic-short.md` shows the three new bullets at the bottom of the Don'ts list.

**Phase C acceptance**: The `new-anthropic-short.md` playbook now offers three optional integration points (4.5 script grounding, 8 phase-3 card screenshot fallback, 11.5 preview QA) without breaking the existing happy-path flow. Simple text-only shorts skip all three and behave identically to today.

---

## Testing Strategy

### Smoke tests (manual, after each phase)

| Test                                                    | Phase | Steps                                                                                                              | Expected                                                            |
| ------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Skill loads                                             | A     | Type "/agent-browser" or "open https://example.com and screenshot it" in a fresh Claude Code session                | Skill description appears in available-skills list; SKILL.md auto-loads |
| Permissions wired                                       | A     | Run `agent-browser --version` via Bash                                                                             | No permission prompt; outputs `agent-browser 0.15.0`                  |
| Daemon starts                                           | A     | Run the canonical capture chain in Task A5                                                                         | PNG ≥10KB at the expected path within ~10s                          |
| Sub-playbook discoverable                               | B     | After `/diy-yt-creator`, the SKILL.md commands table shows three rows                                              | Three rows: new-anthropic-short, capture-asset, qa-composition       |
| capture-asset writes to the right place                 | B     | Task B4 smoke test                                                                                                 | PNG lands at `videos/claude-connectors-everyday-life/assets/<name>.png` |
| qa-composition fails gracefully when preview is offline | B     | Run `/diy-yt-creator qa-composition <slug>` without preview server running                                         | Sub-playbook stops at step 1 with the documented message; no crash    |
| Existing `new-anthropic-short` flow unaffected          | C     | Run a full `new-anthropic-short` invocation on a topic that doesn't need browser (e.g. opinion-style commentary)   | Behaves identically to pre-Phase-C — no new prompts or steps shown    |
| Optional step 4.5 triggers correctly                    | C     | Run `new-anthropic-short` on a topic that requires JS-rendered source (e.g. a SPA dashboard URL)                  | Step 4.5 fires; `agent-browser get text` output is read and cross-checked |

### Edge Cases Checklist

- [ ] First-ever `agent-browser` invocation downloads Chromium (~30-60s) — communicate this to user, don't appear hung
- [ ] Page that requires login (e.g. private GitHub repo URL) — capture-asset detects the small file size and stops with a clear "auth required, please supply credentials or pick a public URL" message
- [ ] Page with anti-bot (Cloudflare challenge, hCaptcha) — same path: small file or non-200 → stop, ask user
- [ ] Page that takes >25s to load — `agent-browser wait --load networkidle` will time out at the default 25s. Document `AGENT_BROWSER_DEFAULT_TIMEOUT=60000` env var override in `capture-asset.md` troubleshooting (do NOT add to plan as a code change — just a documented escape hatch)
- [ ] User runs `capture-asset` against a slug that doesn't exist — sub-playbook stops at step 1 with a clear message
- [ ] User accidentally runs against a localhost URL — sub-playbook step 1 catches and asks for confirmation
- [ ] Concurrent `agent-browser` invocations — daemon serializes; works but slow. Don't parallelize captures from sub-agents
- [ ] PostToolUse hook (`sync-shared-assets.sh`) fires on every `agent-browser` Bash — verify it doesn't crash or spam logs (it shouldn't, since `agent-browser` writes to `videos/<slug>/assets/`, not `shared/`)
- [ ] `videos/<slug>/qa/` folder accumulates over many QA runs — qa-composition leaves them by design (history). Document in playbook that user can `rm -rf videos/<slug>/qa/` whenever they want.
- [ ] Cookie-dismissal `eval` doesn't catch a particular site's banner — the screenshot will include the banner. Capture is still useful; the user can crop in post or supply a manual `--scroll-to <selector>`.

---

## Validation Commands

This repo doesn't have a `package.json` for tests at root, and the skills are markdown — there's no compile/lint step. Validation is mostly **structural** (files exist, frontmatter parses) and **behavioral** (smoke-test invocations work).

### Level 1: STRUCTURAL_VALIDATION

```bash
# Skill files present
ls .claude/skills/agent-browser/SKILL.md \
   .claude/skills/agent-browser/references/commands.md \
   .claude/skills/agent-browser/templates/capture-workflow.sh \
   .claude/skills/agent-browser/update-from-source.sh \
   .agents/skills/agent-browser/SKILL.md

# Frontmatter parses (yaml block at top of SKILL.md)
head -5 .claude/skills/agent-browser/SKILL.md | grep -q "allowed-tools:"

# Permissions JSON valid
python -m json.tool < .claude/settings.local.json > /dev/null

# Mirror is identical
diff -r .claude/skills/agent-browser .agents/skills/agent-browser
```

**EXPECT**: All commands exit 0. `diff -r` produces no output.

### Level 2: HYPERFRAMES_LINT_UNCHANGED

```bash
# Existing video lints clean (no regression)
npx hyperframes lint videos/claude-connectors-everyday-life
```

**EXPECT**: Same lint output as before this plan was implemented (this plan touches no `.html` compositions in `videos/`).

### Level 3: AGENT_BROWSER_FUNCTIONAL

```bash
# Smoke from Task A5
agent-browser open https://example.com \
  && agent-browser wait --load networkidle \
  && agent-browser screenshot /tmp/agent-browser-smoke.png \
  && test $(stat -c%s /tmp/agent-browser-smoke.png) -gt 10000 \
  && echo OK
```

**EXPECT**: Outputs `OK`. PNG ≥10KB.

### Level 4: SUB_PLAYBOOK_FUNCTIONAL (Phase B only)

```bash
# Smoke from Task B4 — capture against the existing video
# (run inside Claude Code via the /diy-yt-creator capture-asset invocation;
#  the underlying bash chain ends with this validation)
test -s videos/claude-connectors-everyday-life/assets/anthropic-news-page.png \
  && test $(stat -c%s videos/claude-connectors-everyday-life/assets/anthropic-news-page.png) -gt 50000 \
  && echo OK
```

**EXPECT**: Outputs `OK`.

### Level 5: PLAYBOOK_INTEGRATION (Phase C only)

Manual: walk through `new-anthropic-short` against a live topic that genuinely needs browser grounding (e.g. "make a short about <a recent JS-SPA blog post URL>"). Confirm step 4.5 fires, step 8 considers screenshots for unknown apps, step 11.5 offers QA.

### Level 6: NO_REGRESSION (final)

Manual: run `new-anthropic-short` against a topic that does NOT need browser (e.g. "make a short about why the lint rule X is good"). Confirm the playbook completes identically to today — no new prompts, no extra steps shown, same outputs.

---

## Acceptance Criteria

- [ ] `/agent-browser` skill is invokable directly with no permission prompts
- [ ] `agent-browser` CLI calls succeed and produce expected output files
- [ ] `.claude/skills/agent-browser/` and `.agents/skills/agent-browser/` are byte-identical
- [ ] `CLAUDE.md` skills table includes the new entry
- [ ] `/diy-yt-creator` shows three commands (new-anthropic-short, capture-asset, qa-composition)
- [ ] `capture-asset` smoke-test produces a real PNG in `videos/<slug>/assets/`
- [ ] `qa-composition` produces phase snapshots when preview is running
- [ ] `new-anthropic-short` against a no-browser-needed topic behaves identically to today (no regression)
- [ ] `new-anthropic-short` against a browser-needed topic fires step 4.5 and/or step 8 screenshot path
- [ ] No edits to `videos/claude-connectors-everyday-life/index.html`, no edits to `templates/`
- [ ] `npx hyperframes lint videos/claude-connectors-everyday-life` produces same output as before
- [ ] All `Don'ts` are documented in `capture-asset.md`, `qa-composition.md`, and the extended `new-anthropic-short.md` Don'ts list

---

## Completion Checklist

- [ ] **Phase A** — Tasks A1-A6 complete; smoke test passes
- [ ] **Phase B** — Tasks B1-B4 complete; capture-asset smoke test passes
- [ ] **Phase C** — Tasks C1-C4 complete; playbook regression test passes
- [ ] Level 1 structural validation passes
- [ ] Level 2 lint regression passes
- [ ] Level 3 agent-browser functional smoke passes
- [ ] Level 4 sub-playbook functional smoke passes (Phase B)
- [ ] Level 5 playbook integration manual walk-through passes (Phase C)
- [ ] Level 6 no-regression manual walk-through passes (Phase C)
- [ ] All acceptance criteria met

---

## Risks and Mitigations

| Risk                                                                         | Likelihood | Impact | Mitigation                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------- | ---------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent-browser` v0.15.0 → future-version breaking change in CLI surface       | LOW        | MED    | `update-from-source.sh` lets us re-pull skill files from upstream `vercel-labs/agent-browser`. Pin the binary version with `npm install -g agent-browser@0.15.0` if drift becomes a problem.                       |
| PostToolUse hook (`sync-shared-assets.sh`) crashes on `agent-browser` Bash    | LOW        | LOW    | Hook scans `shared/`; agent-browser writes to `videos/<slug>/assets/`. No interaction. Verify in Phase A smoke test (Task A5 explicitly runs a Bash and confirms no error from the hook).                          |
| Cookie-dismissal `eval` misses some sites' GDPR banners                       | MED        | LOW    | Documented as known limitation in `capture-asset.md`. User can re-capture with a custom `--scroll-to` after manual dismissal, or supply pre-capture JS via env var. Out-of-scope: a registry of per-site selectors. |
| Anti-bot protection (Cloudflare challenge) blocks captures                    | MED        | LOW    | capture-asset's <10KB validation catches the failure. Sub-playbook reports clearly. Out-of-scope: proxy/residential-IP support (skill supports proxies — documented in `references/proxy-support.md` — but we don't preconfigure). |
| Sister project's `agent-browser` skill files are ahead of vercel-labs source  | LOW        | LOW    | The sister project's `update-from-source.sh` indicates files are auto-synced from upstream. If the sister project has local edits, we'll inherit them. Diff before copying if user is concerned.                  |
| User runs Phase B/C without Phase A                                           | LOW        | HIGH   | Phases are dependency-ordered in this plan and the task list is explicit. Phase B and C reference `agent-browser` skill which doesn't exist if Phase A skipped — sub-playbooks will fail at step 1 with clear error. |
| `videos/<slug>/qa/` folder grows large over many QA runs                      | MED        | LOW    | Documented in qa-composition.md that user can clean up. Add to `.gitignore` if needed (out of scope; not part of this plan).                                                                                       |
| `.claude/settings.local.json` gets accidentally committed                     | LOW        | MED    | The file is named `.local.json` per Claude Code convention — these are typically gitignored. Verify `.gitignore` excludes it before merging. If not, add the line.                                                 |
| Step 4.5 / 8 / 11.5 confuse agents into ALWAYS using browser even for simple topics | MED   | LOW    | Both new optional steps have explicit `Skip if:` clauses. Keep wording strong on "skip when not needed" — the playbook's existing don't-fabricate rule is the natural trigger; if no fabrication risk, no browser. |

---

## Notes

### Why a sub-playbook under `diy-yt-creator` instead of a top-level skill?

Considered: a new top-level skill `hf-capture` (peer of `agent-browser`, mirroring the sister project's `/capture-screenshot` slash command). Rejected because:

1. The wrapper logic is HyperFrames-pipeline-specific (`videos/<slug>/assets/` convention, dark-stage scheme default, integration with phase 3 card editing). Belongs near the pipeline, not as a sibling.
2. Sub-playbooks under `diy-yt-creator` already have precedent (`new-anthropic-short.md`).
3. A top-level slash command can be added later trivially if usage patterns warrant — it would just call this sub-playbook.

### Why mirror to `.agents/skills/`?

Existing convention. 9 of 10 skills are mirrored; only `diy-yt-creator` is `.claude/skills/`-only (likely because it's project-specific and only the Claude Code harness reads it). `agent-browser` is generic — mirror for parity with the other generic skills (`hyperframes`, `gsap`, `music`, etc).

### Why not replace `npx hyperframes capture` with `agent-browser`?

`hyperframes capture` produces structured extraction (design tokens, lottie manifests, animation manifests, shader configs) by introspecting the page beyond visual capture. `agent-browser screenshot` is just the screenshot — no structural extraction. Different tool, different job. They coexist:

- **`hyperframes capture`**: Use when starting `website-to-hyperframes` pipeline — full URL-to-video.
- **`agent-browser`**: Use for spot screenshots, ad-hoc QA, anything outside the website-to-hyperframes pipeline.

Document this distinction in `capture-asset.md` and consider adding a one-liner in `website-to-hyperframes` SKILL.md that points at `agent-browser` for QA — but that's a follow-up, not part of this plan.

### Future considerations (out of scope)

- **Cron-scheduled re-capture**: For videos based on dashboards or live data, re-running capture on a schedule and re-rendering. Use the `schedule` skill if the user wants this.
- **Diff-based asset refresh**: `agent-browser diff url <old> <new>` could detect when a captured asset has gone stale (page redesign). Worth a small follow-up plan if the asset library grows.
- **MCP wrapper for `agent-browser`**: Currently CLI-only. Wrapping in an MCP server would let other Claude harnesses (web app, Cursor) use it without shell access. Not needed for this repo (Claude Code has Bash).
- **Browser pool / parallel captures**: Daemon serializes by design. If a video needs 10+ captures, parallelism via multiple `AGENT_BROWSER_SESSION` names would help. Defer until needed.
- **Playwright codegen integration**: For complex flows (multi-step forms, auth), `agent-browser`'s `record` command produces WebM that could feed `browser-screencast`-style replay. Out of scope.

### Why phased?

Phase A is independently valuable (skill works for ad-hoc tasks). Phase B is independently valuable (sub-playbooks work for any video). Phase C touches the existing `new-anthropic-short.md` and is the only phase that risks regression — it's last so the user can verify A and B cleanly first, and roll back C alone if it causes issues.

### Confidence Score: 8/10 for one-pass implementation success

- **+** All file copy operations are mechanical (sister project files exist, paths verified)
- **+** Skill SKILL.md content is fully specified — no creative writing required for Phase A
- **+** Phase B/C sub-playbook content is specified inline in this plan — implementer can copy-paste structure
- **+** Validation commands are concrete (file existence + smoke tests)
- **+** No external dependencies to install (agent-browser CLI v0.15.0 verified present)
- **−** The cookie-dismissal `eval` may need site-specific tweaks in practice (rated MEDIUM risk)
- **−** Phase C's optional-step triggers ("Skip if / Use when") are advisory — agent judgment is required at runtime; cannot be statically tested
- **−** Mirror sync (`.claude/skills/` ↔ `.agents/skills/`) is currently manual — no enforcement; future drift possible
