# Feature: Multi-Video Preview Dashboard

## Summary

Add two repo-level helper scripts (`scripts/preview-all.sh`, `scripts/preview-stop.sh`) and one generated dashboard (`scripts/preview-dashboard.html`) so the user can boot a `hyperframes preview` server for every project under `videos/` on consecutive ports and watch them all simultaneously in one browser page — a responsive grid of iframes pointing at the per-project deep-link route the studio already exposes.

**Mixed orientations (shorts + long-form):** the repo houses both `templates/shorts/` (1080×1920, 9:16) and `templates/long-form/` (1920×1080, 16:9) projects. Per-video dimensions are read from `npx hyperframes info --json <dir>` (returns `{width, height, resolution: "portrait"|"landscape"}`) and recorded in the manifest so each tile renders at its own correct aspect ratio. The dashboard grid auto-fits a mix of portrait and landscape tiles in the same view.

## User Story

As a video creator working on multiple HyperFrames shorts in parallel
I want a single command that starts a preview server per video and opens one dashboard with live tiles for all of them
So that I can quickly switch focus and visually compare changes across videos without manually `npx hyperframes preview videos/<slug>` and `localhost:300X` per project.

## Problem Statement

Today, previewing N videos requires N terminals running `npx hyperframes preview videos/<slug>` (auto-allocating port 3002, 3003, …) and N browser tabs to compare them. There is no aggregated view; iterating across videos in parallel is slow and context-switch-heavy. The user explicitly stated: "currently i need to preview each video on its own with hyperframes preview. I need a way to watch quickly multiple videos when creating/working on them in parallel."

## Solution Statement

Lean entirely on what the `hyperframes` CLI already provides — multi-server orchestration is built in (`--port`, `--list`, `--kill-all`, `--force-new`). Add a thin bash wrapper that:

1. Discovers every `videos/<slug>/` project (each has `meta.json` + `index.html`).
2. Reuses any matching server already in `npx hyperframes preview --list`; starts the rest on consecutive free ports starting at 3002.
3. Captures per-video dimensions via `npx hyperframes info --json <dir>` so portrait shorts and landscape long-form videos each render at their correct aspect ratio.
4. Writes a manifest (`scripts/.preview-servers.json`, gitignored) including `{slug, port, dir, name, width, height, orientation}` per server.
5. Generates a self-contained `scripts/preview-dashboard.html` with the manifest inlined and embeds each composition via the studio's existing deep-link route `http://localhost:<port>/api/projects/<slug>/preview` (returns the raw composition HTML — already exercised by `scripts/measure-logo.cjs:14`).
6. Opens the dashboard in the default browser.

A second script (`preview-stop.sh`) just calls `npx hyperframes preview --kill-all` for one-line teardown.

## Metadata

| Field            | Value                                                                |
| ---------------- | -------------------------------------------------------------------- |
| Type             | NEW_CAPABILITY                                                       |
| Complexity       | LOW                                                                  |
| Systems Affected | `scripts/`, `.gitignore`, `README.md` (a one-line usage section)     |
| Dependencies     | hyperframes CLI v0.4.31 (already in repo); `bash` + `git` (existing) |
| Estimated Tasks  | 6                                                                    |

---

## UX Design

### Before State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║ BEFORE                                                                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Terminal A                Terminal B                Terminal C              ║
║   ┌────────────────┐        ┌────────────────┐        ┌────────────────┐      ║
║   │ npx hyperframes│        │ npx hyperframes│        │ npx hyperframes│      ║
║   │ preview vid/A  │        │ preview vid/B  │        │ preview vid/C  │      ║
║   │ → :3002        │        │ → :3003        │        │ → :3004        │      ║
║   └───────┬────────┘        └───────┬────────┘        └───────┬────────┘      ║
║           ▼                         ▼                         ▼               ║
║   Browser tab 1             Browser tab 2             Browser tab 3           ║
║   localhost:3002            localhost:3003            localhost:3004          ║
║                                                                               ║
║   USER_FLOW: spawn N terminals, alt-tab N browser tabs, mentally diff scenes  ║
║   PAIN_POINT: linear-time per-video boot, no aggregated view, easy to lose    ║
║              track of which tab is which slug                                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║ AFTER                                                                         ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   Single terminal                                                             ║
║   ┌────────────────────────────────────────────────────────────────────┐      ║
║   │ ./scripts/preview-all.sh                                           │      ║
║   │ → discovers videos/{A,B,C}                                         │      ║
║   │ → reuses existing servers (matched by dir from --list)             │      ║
║   │ → starts missing ones on next free ports (3002,3003,3004)          │      ║
║   │ → writes scripts/.preview-servers.json                             │      ║
║   │ → opens scripts/preview-dashboard.html                             │      ║
║   └─────────────────────────┬──────────────────────────────────────────┘      ║
║                             ▼                                                 ║
║   Browser: scripts/preview-dashboard.html (file://)                           ║
║   ┌────────────────────────────────────────────────────────────────────┐      ║
║   │ HyperFrames — Multi-Preview                          [reload all]  │      ║
║   │ ┌──────────┐ ┌──────────┐ ┌─────────────────────┐                  │      ║
║   │ │ slug-A   │ │ slug-B   │ │ slug-C (long-form)  │ ← per-tile        │      ║
║   │ │ :3002 ↗  │ │ :3003 ↗  │ │ :3004 ↗             │   aspect-ratio    │      ║
║   │ │┌────────┐│ │┌────────┐│ │┌───────────────────┐│   from manifest   │      ║
║   │ ││iframe  ││ ││iframe  ││ ││iframe  16:9       ││ ← landscape tile  │      ║
║   │ ││ 9:16   ││ ││ 9:16   ││ ││ spans 2 grid cols ││   spans 2 cols    │      ║
║   │ ││ short  ││ ││ short  ││ │└───────────────────┘│                   │      ║
║   │ │└────────┘│ │└────────┘│ └─────────────────────┘                  │      ║
║   │ └──────────┘ └──────────┘                                           │      ║
║   └────────────────────────────────────────────────────────────────────┘      ║
║                                                                               ║
║   USER_FLOW: one command, one browser page, all videos visible at once,      ║
║              click a tile's ↗ to open full studio for deep edits              ║
║   VALUE_ADD: parallel visual diff; zero terminal/tab management overhead     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                                    | Before                            | After                                         | User Impact                                    |
| ------------------------------------------- | --------------------------------- | --------------------------------------------- | ---------------------------------------------- |
| Repo root                                   | N terminals running `preview`     | `./scripts/preview-all.sh` → 1 terminal       | Single command, idempotent reuse               |
| Browser                                     | N tabs                            | 1 dashboard page with N iframe tiles          | Side-by-side compare, no tab juggling          |
| Per-tile open-in-studio                     | n/a                               | `↗` link → `localhost:<port>` (full studio)   | Drill down for editing, dashboard for overview |
| Teardown                                    | Ctrl-C × N or close N terminals   | `./scripts/preview-stop.sh`                   | One-liner kill                                 |

---

## Mandatory Reading

**Implementation agent MUST read these before starting:**

| Priority | File                              | Lines | Why Read This                                                                                            |
| -------- | --------------------------------- | ----- | -------------------------------------------------------------------------------------------------------- |
| P0       | `scripts/sync-shared-assets.sh`   | 1-50  | Pattern to MIRROR: shebang, `set -euo pipefail`, repo-root via `git rev-parse`, idempotent early-exits   |
| P0       | `scripts/measure-logo.cjs`        | 12-16 | Confirms the deep-link URL: `http://localhost:<port>/api/projects/<slug>/preview` is the raw composition |
| P1       | `CLAUDE.md`                       | 49-72 | Project structure: every `videos/<slug>/` has `meta.json` + `index.html`                                 |
| P1       | `videos/claude-connectors-everyday-life/meta.json` | 1-5  | Confirms slug = directory name = `meta.json.id`                                                          |
| P2       | `.gitignore`                      | all   | Add `.preview-servers.json` and `preview-dashboard.html` (regenerated artefacts)                         |

**External API surface (already verified live, no docs needed):**

| Endpoint                                       | Verified result                                                                                          |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `GET /api/projects`                            | `{"projects":[{"id","dir","title"}]}` — JSON, one entry per server's project                             |
| `GET /api/projects/<slug>/preview`             | `200 OK`, `text/html` — raw composition (embeddable in iframe)                                           |
| `GET /api/projects/<slug>/preview/` (trailing) | `404` — must NOT trail-slash                                                                             |
| `npx hyperframes preview --list`               | Plain text: `Port <n>  <slug>  <abs-path>` per server                                                    |
| `npx hyperframes preview --port=<n> <dir>`     | Starts server on requested port (background-friendly with `&`)                                           |
| `npx hyperframes preview --kill-all`           | Stops every tracked server                                                                               |
| `npx hyperframes info --json <dir>`            | `{"name","resolution":"portrait"\|"landscape","width","height","duration",...}` — per-video dimensions  |

---

## Patterns to Mirror

**SCRIPT_HEADER + REPO_ROOT_DETECT:**

```bash
# SOURCE: scripts/sync-shared-assets.sh:1-25
# COPY THIS PATTERN:
#!/usr/bin/env bash
# preview-all.sh — Boot a hyperframes preview server per videos/<slug>/ and
# open a single dashboard page that embeds them all.

set -euo pipefail

if REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  :
else
  REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi
```

**CHANGE-DETECTION + EARLY EXIT (mirror this idempotency style):**

```bash
# SOURCE: scripts/sync-shared-assets.sh:31-33
# COPY THIS PATTERN:
[ -d "$REPO_ROOT/videos" ] || { echo "no videos/ directory; nothing to preview" >&2; exit 0; }
```

**DEEP-LINK URL FORMAT (already in use, copy verbatim):**

```js
// SOURCE: scripts/measure-logo.cjs:13-15
// COPY THIS PATTERN — note: NO trailing slash:
const url =
  process.argv[2] ||
  "http://localhost:3002/api/projects/claude-connectors-everyday-life/preview";
```

**META.JSON SHAPE (slug source of truth):**

```json
// SOURCE: videos/claude-connectors-everyday-life/meta.json:1-5
// READ id FROM HERE (falls back to directory name if missing):
{
  "id": "claude-connectors-everyday-life",
  "name": "Claude Connectors for Everyday Life",
  "createdAt": "2026-04-26T19:37:22.701Z"
}
```

---

## Files to Change

| File                                  | Action | Justification                                                                              |
| ------------------------------------- | ------ | ------------------------------------------------------------------------------------------ |
| `scripts/preview-all.sh`              | CREATE | Orchestrator: discover, boot/reuse servers, write manifest, generate dashboard, open it    |
| `scripts/preview-stop.sh`             | CREATE | One-line teardown wrapper (`npx hyperframes preview --kill-all`)                           |
| `scripts/preview-dashboard.template.html` | CREATE | Static HTML template (committed); the orchestrator copies it to `preview-dashboard.html` and inlines the manifest as `<script id="manifest" type="application/json">…</script>` |
| `.gitignore`                          | UPDATE | Ignore `scripts/.preview-servers.json` and `scripts/preview-dashboard.html` (generated)    |
| `README.md`                           | UPDATE | Add a 5-line "Preview all videos at once" section under existing Commands                  |
| `CLAUDE.md`                           | UPDATE | Add one row to the Commands table referencing `./scripts/preview-all.sh`                   |

---

## NOT Building (Scope Limits)

- **No new npm package, no node deps.** Pure bash + already-installed `hyperframes` + plain HTML/JS. The single existing `.cjs` script (`measure-logo.cjs`) imports puppeteer from a global path — we're NOT following that pattern; we have no need for headless browser automation here.
- **No live process supervision (PM2/concurrently).** The CLI already tracks servers via `--list` and survives the parent shell exit (per the user's global CLAUDE.md note about `bun run dev`-style detached children). We rely on that, not a process manager.
- **No WebSocket bridge / no shared-state server.** The dashboard is a static `file://` HTML; iframes hit the per-port preview servers directly.
- **No auto-rebuild of the dashboard when a new video is added.** User re-runs `preview-all.sh`. (A file-watcher is a future enhancement.)
- **No mobile/responsive polish beyond a CSS grid with `auto-fit, minmax(280px, 1fr)`.** This is a desktop dev tool.
- **Not a HyperFrames CLI patch.** All changes live in this repo's `scripts/`, no upstream fork.
- **No port-conflict resolution beyond "skip ports already in LISTEN".** If 3002 is taken by something other than a hyperframes server, we walk to 3003, 3004, … up to 3020 then fail loud.

---

## Step-by-Step Tasks

Execute in order. Each task is independently verifiable.

### Task 1: Verify the studio's deep-link URL is iframe-embeddable (no X-Frame-Options / CSP frame-ancestors)

- **ACTION**: Run a one-shot probe before writing code. The whole plan hinges on iframes loading.
- **VALIDATE**:
  ```bash
  curl -sI http://localhost:3002/api/projects/claude-connectors-everyday-life/preview \
    | grep -iE 'x-frame-options|content-security-policy|frame-ancestors' \
    && echo "POTENTIAL BLOCKER: framing restricted" \
    || echo "ok: no framing restrictions advertised"
  ```
- **EXPECT**: Either no matches (ok) OR `frame-ancestors *`/`'self'`-permissive value. If the server sets `X-Frame-Options: DENY/SAMEORIGIN`, abort the plan and switch to **fallback approach** (see Risks section: serve dashboard from one of the preview servers' origins, or run a tiny static file server on the same host, or use `<object>`/`<embed>` instead of iframes).
- **GOTCHA**: This MUST be done first. If iframes are blocked, every other task is wasted work.

### Task 2: CREATE `scripts/preview-all.sh`

- **ACTION**: New executable bash script.
- **IMPLEMENT** (in this order inside the script):
  1. Header + `set -euo pipefail` + `REPO_ROOT` detection — mirror `scripts/sync-shared-assets.sh:1-25` exactly.
  2. Define `VIDEOS_DIR="$REPO_ROOT/videos"`, `MANIFEST="$REPO_ROOT/scripts/.preview-servers.json"`, `DASHBOARD="$REPO_ROOT/scripts/preview-dashboard.html"`, `TEMPLATE="$REPO_ROOT/scripts/preview-dashboard.template.html"`, `START_PORT=3002`.
  3. Early exit: `[ -d "$VIDEOS_DIR" ] || { echo "no videos/ — nothing to preview" >&2; exit 0; }`.
  4. Discover slugs: `mapfile -t SLUGS < <(find "$VIDEOS_DIR" -mindepth 2 -maxdepth 2 -name index.html -printf '%h\n' | sed "s|$VIDEOS_DIR/||" | LC_ALL=C sort)` — robust against directories that aren't real projects (no `index.html` ⇒ skipped). Use a portable `find` flag set; if `-printf` is missing on macOS, fall back to a `while read; basename` loop. (Git Bash on Windows has `-printf`.)
  5. Read existing servers: capture stdout of `npx hyperframes preview --list 2>&1` and parse lines matching `^[[:space:]]*Port[[:space:]]+([0-9]+)[[:space:]]+([^[:space:]]+)[[:space:]]+(.*)$` into three parallel arrays: `EX_PORTS`, `EX_SLUGS`, `EX_DIRS`.
  6. For each discovered slug:
     - Compute its absolute project dir.
     - If a row in the existing list has a matching `dir`, REUSE that port — skip booting.
     - Else: walk port allocator `next_port` (starts at `START_PORT`, increments past any port already in `EX_PORTS` and any port currently in LISTEN state — check via `(echo > /dev/tcp/127.0.0.1/$port) 2>/dev/null` test in a subshell). Cap at `START_PORT + 19`; abort with a clear message on overflow.
     - Boot in background: `npx hyperframes preview --port="$next_port" "$VIDEOS_DIR/$slug" >/dev/null 2>&1 &` then `disown` (so the script can exit cleanly).
     - Record the assigned port for this slug.
  7. **Wait for boot**: for every newly started server, poll `curl -sf "http://localhost:$port/api/projects" >/dev/null` with a 200ms sleep, max 30 tries (~6s). Fail loud on any that never come up.
  8. Build the manifest JSON to `$MANIFEST`. Use `printf` directly — no `jq` requirement (slugs are alphanumeric/dash; safe). For each server, also capture dimensions: `npx hyperframes info --json "$VIDEOS_DIR/$slug"` → extract `width`, `height`, `resolution` (which is `"portrait"` | `"landscape"` | `"square"`). Shape:
     ```json
     {
       "generatedAt": "2026-04-27T...",
       "servers": [
         {
           "slug": "claude-connectors-everyday-life",
           "port": 3002,
           "dir": "/abs/path",
           "name": "Claude Connectors for Everyday Life",
           "width": 1080,
           "height": 1920,
           "orientation": "portrait"
         }
       ]
     }
     ```
     Pull `name` from `videos/<slug>/meta.json` via `grep -o '"name"[^,}]*' | sed ...` (avoid the `jq` dependency); fall back to slug if missing or unparseable. Same approach for `width` / `height` / `resolution` from `info --json` output. If `info --json` fails for a project (malformed composition, lint errors), fall back to `width=1080, height=1920, orientation="portrait"` and log a warning — don't abort the whole run.
  9. **Generate the dashboard**: copy `$TEMPLATE` to `$DASHBOARD`, then replace the line `<!-- MANIFEST_INLINE -->` with `<script id="manifest" type="application/json">…manifest JSON…</script>` using `awk` (sed struggles with multi-line JSON; awk replaces the line with file contents cleanly). Document this contract in a comment at the top of the template file.
  10. Print a summary table to stdout (`Slug  Port  Status  URL`).
  11. **Open the dashboard**: pick one of `xdg-open`, `open`, `start` based on `$OSTYPE` / Windows detection; on Git Bash use `start "" "$DASHBOARD"`. Skip if `--no-open` flag is passed.
- **MIRROR**: `scripts/sync-shared-assets.sh:1-100` for header / repo-root / idempotency style.
- **FLAGS** to support: `--no-open` (skip browser launch), `--only=slug1,slug2` (subset), `--port=NNNN` (override start port). Keep parsing minimal — a simple `case` over `$@`.
- **GOTCHAS**:
  - `chmod +x scripts/preview-all.sh` after creation. Test: `ls -l scripts/preview-all.sh` shows `x` bits.
  - `npx hyperframes preview --list` text format isn't documented as stable; pin the regex strictly and fail loud (with the offending line) if zero rows parse but the command exited 0 — that's the canary for "CLI changed format".
  - Background `&` plus `disown` is critical on Git Bash so the script doesn't keep child stdin open and block on exit.
  - The TCP probe `(echo > /dev/tcp/127.0.0.1/$port)` only works in bash (not sh, not POSIX). Already required.
  - `find -printf` works on Git Bash and Linux but NOT on stock macOS BSD-find. If supporting macOS matters, switch to `find ... -exec sh -c 'echo "${1#$VIDEOS_DIR/}"' _ {} \;`. Per current CLAUDE.md the user is Windows-only — leave the Linux-friendly form and add a comment.
- **VALIDATE**:
  ```bash
  bash -n scripts/preview-all.sh                    # syntax check
  shellcheck scripts/preview-all.sh || true         # lint (best-effort; not in CI)
  ./scripts/preview-all.sh --no-open                # smoke run; should print summary, write manifest
  test -f scripts/.preview-servers.json
  test -f scripts/preview-dashboard.html
  npx hyperframes preview --list                    # should show one server per video
  ```

### Task 3: CREATE `scripts/preview-dashboard.template.html`

- **ACTION**: New static file (committed). Self-contained: inline CSS, inline JS, no external CDN.
- **IMPLEMENT**:
  - `<!doctype html>`, `<meta charset>`, `<meta viewport>` (standard).
  - `<title>HyperFrames — Multi-Preview</title>`.
  - Header strip: project name on left, button row on right (`Reload all`, `Mute all` toggle, `Open studio for selected`, `Stop all` (links to `./preview-stop.sh` instructions in a `<details>`).
  - A **placeholder line** `<!-- MANIFEST_INLINE -->` exactly as written; orchestrator replaces this with the inlined `<script id="manifest" type="application/json">…</script>` block. Keep the marker on its own line.
  - Body JS:
    1. Read `JSON.parse(document.getElementById('manifest').textContent)`.
    2. For each `server`, append a `<article class="tile">` containing:
       - Title row: slug + `name` + `:port` + an `<a target="_blank" href="http://localhost:<port>/">↗ studio</a>`.
       - An `<iframe loading="lazy" src="http://localhost:<port>/api/projects/<slug>/preview" sandbox="allow-scripts allow-same-origin allow-popups" allow="autoplay; fullscreen">`.
       - Per-tile button: `Reload` (sets `iframe.src = iframe.src` to force reload).
    3. Implement `Mute all` by `iframe.contentWindow.postMessage` is overkill — simpler: loop iframes and write `iframe.contentDocument?.querySelectorAll('audio,video').forEach(m => m.muted = !m.muted)` inside a try (cross-origin file:// vs localhost — see Risks). Fallback: hide audio elements via injecting CSS into same-origin iframes only. If cross-origin blocks DOM access, surface a clear "open from one of the localhost preview servers instead" message in the UI.
  - CSS layout: a single grid auto-fits **both** portrait shorts (9:16) and landscape long-form (16:9) tiles. Strategy: per-tile `aspect-ratio` is set inline from manifest data (`style="aspect-ratio: ${width}/${height}"`), and the grid uses `grid-auto-flow: dense` so a wide landscape tile + a narrow portrait tile pack neighbours instead of leaving gaps. Concretely:
    ```css
    :root { --tile-min: 280px; }
    main { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(var(--tile-min), 1fr)); grid-auto-flow: dense; }
    .tile { display: flex; flex-direction: column; }
    .tile.landscape { grid-column: span 2; }    /* landscape tiles take two grid columns */
    .tile iframe { width: 100%; aspect-ratio: var(--ar); border: 0; background: #000; }
    ```
    The orchestrator emits `<article class="tile ${orientation}" style="--ar: ${width}/${height}">` per server. On narrow viewports, the `auto-fit` collapses to one column and the `span 2` becomes a no-op (it caps at the available track count), so the layout still works on a half-screen window.
  - Dark-stage palette (matches the `templates/shorts/anthropic` aesthetic): `body { background: #0b0b0d; color: #e8e8ea; font: 13px/1.4 ui-sans-serif, system-ui; }`.
- **MIRROR**: No prior dashboard exists. Style after the Anthropic Shorts template's dark surface (`templates/shorts/anthropic/DESIGN.md`) so it visually fits the project.
- **GOTCHAS**:
  - `sandbox` without `allow-same-origin` blocks the composition's own JS (timelines, audio sync) — both flags required.
  - When opened via `file://`, `iframe.contentDocument` access to `http://localhost:*` content is **cross-origin and blocked**. The "Mute all" feature must degrade gracefully — wrap in try/catch and surface a tooltip "cross-origin: per-tile mute only" if it fails.
  - Per-tile `aspect-ratio` from manifest dims keeps the visible region correct for both 9:16 and 16:9 compositions, but the composition's internal CSS sets a fixed pixel viewport (e.g. `1080×1920` per `videos/claude-connectors-everyday-life/index.html:14-15`). Let the iframe scrollbar handle overflow for v1; if it looks bad in Task 3 visual check, add a `transform: scale(...)` derived from `iframe.clientWidth / manifestEntry.width` (computed in JS after layout). Decide after viewing both a portrait and landscape tile in the same grid.
  - For mixed-orientation grids: a single landscape tile (16:9) is roughly 3.5× wider per pixel of height than a portrait tile (9:16). Without `grid-column: span 2` on landscapes, a row of mixed tiles produces ugly empty space. The `dense` auto-flow + span-2 rule above handles this — verify with at least one of each format present.
- **VALIDATE**:
  ```bash
  # After Task 2 has run preview-all.sh once:
  start "" "scripts/preview-dashboard.html"   # opens in default browser
  # Manual:
  #  - All tiles render the live composition
  #  - Per-tile Reload restarts the timeline
  #  - The ↗ studio link opens localhost:<port> in a new tab
  ```

### Task 4: CREATE `scripts/preview-stop.sh`

- **ACTION**: 5-line wrapper.
- **IMPLEMENT**:
  ```bash
  #!/usr/bin/env bash
  set -euo pipefail
  npx hyperframes preview --kill-all
  rm -f "$(git rev-parse --show-toplevel)/scripts/.preview-servers.json" \
        "$(git rev-parse --show-toplevel)/scripts/preview-dashboard.html"
  ```
- **VALIDATE**:
  ```bash
  ./scripts/preview-stop.sh
  npx hyperframes preview --list   # → "0 servers running."
  ```

### Task 5: UPDATE `.gitignore`

- **ACTION**: Append two lines.
- **IMPLEMENT**:
  ```
  # Multi-video preview dashboard — generated by scripts/preview-all.sh
  scripts/.preview-servers.json
  scripts/preview-dashboard.html
  ```
- **MIRROR**: existing `.gitignore` style (one comment per group, no trailing blanks).
- **VALIDATE**: `git status --short scripts/` after a `preview-all.sh` run shows nothing.

### Task 6: UPDATE `README.md` and `CLAUDE.md`

- **ACTION**: Add a single short section to each.
- **README.md** — add under existing Commands section:
  ```markdown
  ### Preview all videos at once

  ```bash
  ./scripts/preview-all.sh           # boot one server per videos/<slug>/, open dashboard
  ./scripts/preview-all.sh --no-open # boot only; print URL
  ./scripts/preview-stop.sh          # kill all preview servers
  ```

  Idempotent — reuses servers already running for a project. Generated dashboard is gitignored.
  ```
- **CLAUDE.md** — append one row to the Commands code block:
  ```bash
  ./scripts/preview-all.sh                        # boot all videos, open multi-tile dashboard
  ```
- **VALIDATE**: `npx hyperframes lint` is unaffected (markdown only, no compositions touched). Visually inspect both files render correctly.

---

## Testing Strategy

This is a developer-tooling shell script, not a runtime feature. No unit-test framework exists in this repo (`package.json` has none). Testing is manual + smoke.

### Smoke Tests (run in order)

| Step | Command                                                      | Expected                                                                                  |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| 1    | `npx hyperframes preview --kill-all`                         | "0 servers running."                                                                      |
| 2    | `./scripts/preview-all.sh --no-open`                         | Boots N servers (N = `videos/*/index.html` count); prints summary; writes manifest        |
| 3    | `npx hyperframes preview --list`                             | Shows N rows, each with a port and the matching slug                                      |
| 4    | `cat scripts/.preview-servers.json | head -20`               | Valid JSON, one entry per video                                                            |
| 5    | `start "" scripts/preview-dashboard.html` (or `xdg-open`)    | Browser opens; all tiles render live compositions                                          |
| 6    | `./scripts/preview-all.sh --no-open` (re-run)                | No new servers booted (idempotent reuse); manifest regenerated with same ports             |
| 7    | Add a new project: `cp -r templates/shorts/anthropic videos/test-x` | Re-running `preview-all.sh` boots ONE more server on the next free port                   |
| 8    | `./scripts/preview-stop.sh`                                  | All servers stopped; manifest + dashboard removed                                          |

### Edge Cases Checklist

- [ ] **No `videos/` directory** → script exits 0 with a clean message, no error.
- [ ] **Empty `videos/`** → script exits 0; "no projects found" message.
- [ ] **`videos/<slug>/` with no `index.html`** → silently skipped (matches the `find -name index.html` filter).
- [ ] **Already-running server for a project** → reused, port unchanged.
- [ ] **Port 3002 already in use by something else** → walk to next free port, log the skip.
- [ ] **Port range exhausted (3002–3020 all busy)** → fail loud with the offending state.
- [ ] **`meta.json` missing or malformed** → fall back to slug for `name`; do not crash.
- [ ] **`hyperframes info --json` fails for a project** → fall back to `1080×1920 portrait`; emit a warning row in the orchestrator summary; tile still renders.
- [ ] **Mixed-orientation grid (1× short + 1× long-form)** → `grid-auto-flow: dense` + `.tile.landscape { grid-column: span 2 }` packs neighbours; visually verify before merging.
- [ ] **Square format (`resolution: "square"`)** → fall through to `aspect-ratio: 1/1`; treat as portrait for grid placement (no span-2).
- [ ] **Slugs with spaces** → not supported; document and fail loud (HyperFrames slugs are kebab-case by convention).
- [ ] **Server fails to boot within 6s** → fail the script with the slug + port + last 20 lines of stderr.
- [ ] **`X-Frame-Options` set on preview HTML** → caught in Task 1; plan must pivot.
- [ ] **Cross-origin blocks "Mute all"** → graceful degradation, tooltip explains; per-tile reload still works.

---

## Validation Commands

### Level 1: STATIC_ANALYSIS

```bash
bash -n scripts/preview-all.sh
bash -n scripts/preview-stop.sh
shellcheck scripts/preview-all.sh scripts/preview-stop.sh   # best-effort; install via choco/scoop if missing
```

**EXPECT**: Exit 0, no warnings beyond style.

### Level 2: SMOKE

```bash
./scripts/preview-stop.sh                # clean slate
./scripts/preview-all.sh --no-open       # boot
npx hyperframes preview --list           # verify count == videos/*/index.html count
test -f scripts/.preview-servers.json
test -f scripts/preview-dashboard.html
```

### Level 3: BROWSER

```bash
start "" scripts/preview-dashboard.html  # Git Bash on Windows
# Manual:
#  - All tiles load
#  - Per-tile reload works
#  - ↗ studio link opens full studio
#  - Cross-origin DOM access for "Mute all" either works (same-origin path) or degrades cleanly
```

### Level 4: IDEMPOTENCY

```bash
./scripts/preview-all.sh --no-open       # 1st run
PORTS_BEFORE=$(npx hyperframes preview --list)
./scripts/preview-all.sh --no-open       # 2nd run
PORTS_AFTER=$(npx hyperframes preview --list)
diff <(echo "$PORTS_BEFORE") <(echo "$PORTS_AFTER")   # → empty
```

### Level 5: HYPERFRAMES INTEGRITY

```bash
npx hyperframes lint videos/claude-connectors-everyday-life
```

**EXPECT**: Exit 0; no compositions modified, lint must remain clean.

---

## Acceptance Criteria

- [ ] `./scripts/preview-all.sh` boots exactly one server per `videos/*/index.html` (or reuses existing matches).
- [ ] Dashboard at `scripts/preview-dashboard.html` opens in default browser and renders all videos in a responsive grid.
- [ ] Per-tile `↗ studio` link opens the full studio at `http://localhost:<port>/`.
- [ ] Re-running `preview-all.sh` is a no-op for already-running matched servers.
- [ ] `./scripts/preview-stop.sh` kills all servers and removes generated artefacts.
- [ ] `.gitignore` excludes generated files; `git status` clean after a run.
- [ ] No HyperFrames compositions modified; `npx hyperframes lint` still passes for every video.
- [ ] Documented in `README.md` and `CLAUDE.md`.

---

## Completion Checklist

- [ ] Task 1 probe confirms iframe-embeddable preview URL (or pivot triggered)
- [ ] `scripts/preview-all.sh` created, executable, passes `bash -n`
- [ ] `scripts/preview-dashboard.template.html` created, self-contained
- [ ] `scripts/preview-stop.sh` created, executable
- [ ] `.gitignore` updated
- [ ] `README.md` + `CLAUDE.md` updated with usage
- [ ] All 5 validation levels pass
- [ ] Idempotent re-run verified
- [ ] Stop script tested

---

## Risks and Mitigations

| Risk                                                                                            | Likelihood | Impact | Mitigation                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Studio sets `X-Frame-Options` or restrictive CSP `frame-ancestors` and iframes don't load        | LOW        | HIGH   | **Task 1 probes this first.** Fallback: serve the dashboard from one of the existing preview servers (drop the file into `videos/<slug>/` and load via `http://localhost:<port>/dashboard.html`) so origins match — every iframe is then same-origin to its own server only, but that's enough for embedding (CSP is checked against the framing page's origin, not the iframe's). |
| Mixed orientations (shorts 9:16 + long-form 16:9) produce an awkward grid with gaps             | MED        | LOW    | Per-tile `aspect-ratio` from `info --json` + `grid-auto-flow: dense` + `.tile.landscape { grid-column: span 2 }`. Verified during Task 3 with at least one of each format present.                                  |
| `preview --list` text format changes in a future hyperframes release                            | LOW        | MED    | Strict regex with explicit error if zero rows parse on non-empty output. Pin `hyperframes` version in a future task by adding `"hyperframes": "0.4.31"` to a (currently-absent) `package.json`'s `devDependencies`. |
| Multiple compositions auto-playing audio simultaneously is jarring                              | HIGH       | LOW    | Tiles default to `<iframe>` without `autoplay` — most compositions wait for studio play; if any auto-start, surface "Mute all" button (graceful degradation under cross-origin).                                    |
| Memory/CPU: 5+ vertical compositions × audio + GSAP timelines = heavy                           | MED        | MED    | Use `loading="lazy"` on iframes; document recommended max 6 tiles in README; future enhancement: pause-when-not-visible via IntersectionObserver.                                                                    |
| Slug includes characters illegal in URLs (unlikely — convention is kebab-case)                  | VERY LOW   | LOW    | Fail loud in the orchestrator with a clear message; document slug rules in README.                                                                                                                                   |
| Port collisions if user runs other dev servers on 3002+                                         | MED        | LOW    | TCP probe walks past busy ports up to 3020; cap + abort with a clear message.                                                                                                                                        |
| Background `&`/`disown` doesn't fully detach on some Git Bash configs (script hangs)            | LOW        | LOW    | Add `nohup` belt-and-braces + `>/dev/null 2>&1`. Document the fallback `--no-bg` flag if needed (not part of v1).                                                                                                    |

---

## Notes

**Why this is a 100-line bash script and not a Node tool:** the orchestration is genuinely thin — discover, boot, generate, open. The hyperframes CLI does all the heavy lifting (server lifecycle, port tracking via `--list`, the deep-link route). A Node implementation would add a `package.json`, a build/lint pipeline, and four orders of magnitude more LOC for the same outcome.

**Why a generated dashboard, not a long-running dashboard server:** there's nothing dynamic to host — the manifest is static within a session, iframes load directly from preview servers. A `file://` HTML keeps the surface area at zero (no port to allocate, no process to supervise, no leaked handle to clean up). The trade-off is the cross-origin "Mute all" caveat; addressed via graceful degradation.

**Future enhancements (intentionally out of scope):**
- File-watcher that re-runs `preview-all.sh` automatically when `videos/<new-slug>/` appears.
- Per-tile timeline scrubber overlay synced across tiles.
- Side-by-side A/B mode (mount the same composition twice with different DESIGN.md tweaks).
- A small Express/Bun static server for hosting the dashboard same-origin to localhost so DOM access across tiles works.
- An `npx hyperframes preview --list --json` upstream PR — the cleanest fix for the regex-parsing fragility above.

**Confidence the agent can implement in one pass:** HIGH. The hyperframes CLI surface is verified live in this session, the deep-link URL is already in production use (`scripts/measure-logo.cjs:14`), the bash-script style is established (`scripts/sync-shared-assets.sh`), and the only true unknown — iframe embeddability — is gated behind Task 1 with a documented pivot.
