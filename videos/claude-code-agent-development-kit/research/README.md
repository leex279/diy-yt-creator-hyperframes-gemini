# The Agent Development Kit — Working Space

8–10 min long-form on Claude Code's 5-layer architecture (CLAUDE.md / Skills / Hooks / Subagents / Plugins).

## Files

| File | Purpose |
|---|---|
| [`Instagram.md`](Instagram.md) | Source clipping — Brij Kishore Pandey post (Apr 25 2026) that framed the "5-layer agent architecture" angle |
| [`source.md`](source.md) | Researched facts on each layer, comparison table, the 4 common confusions, every claim citation-ready |
| [`BRIEF.md`](BRIEF.md) | Production brief — thesis, 8-scene outline, visual library picks, receipts, hook variants, SEO starter, /diy-yt-creator handoff |
| [`diagrams/01-5-layer-stack.excalidraw`](diagrams/01-5-layer-stack.excalidraw) | The architecture overview — 5 layers + MCP sidebar, shape-is-meaning per layer |
| [`diagrams/02-request-lifecycle.excalidraw`](diagrams/02-request-lifecycle.excalidraw) | Where each layer fires during a single request (CLAUDE.md band → main thread with hook events → skill activation → subagent fork → MCP wire → plugin wrapper) |
| [`diagrams/03-decision-tree.excalidraw`](diagrams/03-decision-tree.excalidraw) | "Which layer do I need?" — 5 yes/no questions cascading to L1 / MCP / L3 / L4 / L2 + plugin distribution band |

## How to use

1. Open `source.md` for the facts. Every claim cites `code.claude.com/docs`.
2. Open `BRIEF.md` for the production plan. The 8-scene outline maps cleanly to `templates/long-form/standard/` archetypes.
3. Open the three `.excalidraw` files in Excalidraw (or VS Code Excalidraw extension). Diagram 1 = architecture hero, used in scenes 1–2 and 8. Diagram 2 = scene 8 (lifecycle). Diagram 3 = scene 7 (decision tree).
4. Spawn the video project with the handoff command in BRIEF.md §13. The diy-yt-creator phases will pick up the brief and start writing the script.

## Status

- ✅ Research complete (source.md)
- ✅ Diagrams 1, 2, 3 drafted
- ✅ Brief drafted
- ⏳ Awaiting Phase 1 (composition plan) → spawn `videos/claude-code-agent-development-kit/` from `templates/long-form/standard`
