# Content Brief — Claude Code v2.1.119 → v2.1.121

**Range release**: 3 versions, ~110 changes total. Shipped between the v2.1.118 cut and 2026-04-28.

## Version

`v2.1.119` → `v2.1.121` (range release covering all three).

## Stats (scene-stats-opener pills)

| Pill | Value | Label |
|---|---|---|
| 1 (cyan) | **27** | features |
| 2 (purple) | **56** | fixes |
| 3 (green) | **11** | improved |

## Hook angle (scene-hook)

The first cross-platform Claude Code release that drops the Git-for-Windows requirement, ships a headless code reviewer, and lets `/config` finally persist where you'd expect it. Three releases stacked end-to-end means a lot of one-line bullets — but a handful actually change how you use the CLI day-to-day.

## Highlights (scene-feature-cards, 3x2)

Top-6 from official changelog (user-confirmed):

| # | Title | Detail | Code/Hint | Version |
|---|---|---|---|---|
| 01 | Windows: no Git required | PowerShell is now the fallback when Git for Windows isn't installed. One less dependency on every Windows machine. | `pwsh` fallback | v2.1.120 |
| 02 | `claude ultrareview` headless | New CLI command runs `/ultrareview` non-interactively. Pipe findings to stdout from CI or scripts. | `$ claude ultrareview` | v2.1.120 |
| 03 | `/config` finally persists | Settings written via `/config` now save to `~/.claude/settings.json` with project / local / policy precedence. | `~/.claude/settings.json` | v2.1.119 |
| 04 | MCP `alwaysLoad` | New server config flag — tools from `alwaysLoad: true` servers skip the search-deferral and load immediately. | `alwaysLoad: true` | v2.1.121 |
| 05 | PostToolUse override | Hooks can now replace tool output for any tool via `hookSpecificOutput.updatedToolOutput` — previously MCP-only. | `updatedToolOutput` | v2.1.121 |
| 06 | Faster startup + LSP summaries | Recent Activity panel removed for faster cold start; LSP diagnostic summaries now expand on click. | `LSP` | v2.1.121 |

## Categories (per-version slice)

For optional category sub-scene with `feature-cards--stack` layout:

- **CI / headless workflows** — `claude ultrareview`, `--print` honors agent frontmatter, `--from-pr` accepts GitLab/Bitbucket/Enterprise URLs, `claude plugin prune`
- **Hooks / extensibility** — PostToolUse output replacement, hooks include `duration_ms`, `${CLAUDE_EFFORT}` in skills, `AI_AGENT` env var
- **Cross-platform** — Windows PowerShell fallback (no Git required), iTerm2 clipboard via `/terminal-setup`, X.509 Workload Identity for Vertex AI
- **Quality of life** — type-to-filter `/skills`, dialogs scroll on overflow, click wrapped URLs in fullscreen, persistent `/config`, slash command picker improvements

## Terminal scene pick (scene-terminal)

User-confirmed: **`$ claude ultrareview`**.

- Title bar: `~/project`
- Content: `$ claude ultrareview src/auth.ts`
- Headline above: "Headless code review, in one command."

## CTA (scene-cta)

- Inline terminal: `$ claude update` (default — pulls in everything covered)
- Debate question: "Is the headless `ultrareview` command going to replace your PR review workflow, or just supplement it?"

## WatchNext

**Skipped per user request.** No WatchNext scene insertion.

## Hero stats (scene-stat-pill-row, 2 huge color-rotated stats)

- **3 versions** — 110+ changes
- **27 features** — across CLI, hooks, MCP, IDE integrations

## Side-by-side (scene-side-by-side, A vs B contrast)

- **Before (v2.1.118)**: `/config` changes lost on restart · Windows machines blocked without Git · `/ultrareview` only worked interactively
- **After (v2.1.121)**: `/config` persists with proper precedence · PowerShell-only Windows works out of the box · `claude ultrareview` runs headless

---

## Sources

- `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` (v2.1.119, v2.1.120, v2.1.121 anchors)
- `https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.{119,120,121}` (curated Highlights section)
