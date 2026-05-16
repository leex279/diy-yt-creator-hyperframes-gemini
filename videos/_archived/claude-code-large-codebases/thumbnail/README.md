# Thumbnails — claude-code-large-codebases

10 variants for "How Claude Code works in large codebases: Best practices and where to start" (Anthropic · Part 1 of Claude Code at scale series).

All headlines are fact-grounded to the source article. No fabrication.

| # | Angle | Headline | Cover anchor | Theme |
|---|---|---|---|---|
| 01 | Thesis-as-math | "Harness > Model." | article-header.png | dark |
| 02 | Pure number slam | "5 / 2 / 3." | fig1-harness.png | dark |
| 03 | Authority appeal | "Anthropic's own playbook." | article-header.png | cream |
| 04 | Contrarian vs RAG | "RAG is dead." | fig1-harness.png | dark |
| 05 | Model-worship pivot | "Stop blaming the model." | none (text only) | cream |
| 06 | Finger-point mistake | "Your CLAUDE.md is bloated." | fig3-getting-started-checklist.png | dark |
| 07 | Counter-intuitive order | "Don't build MCP first." | fig1-harness.png | cream |
| 08 | Emerging-role hook | "The agent manager era." | fig2-rollout-phases.png | cream |
| 09 | Imperative command | "Build the harness." | fig3-getting-started-checklist.png | dark |
| 10 | Binary tension | "Scale or stall." | article-header.png | dark |

**Theme breakdown:** 7 dark · 3 cream

## Files

- `_base.css` — shared 1280×720 design system (Anthropic dark-stage + cream variants)
- `variant-01.html` through `variant-10.html` — source HTML for each variant
- `variant-01.png` through `variant-10.png` — rendered at 1280×720
- `contact-sheet.html` — 2-column gallery of all 10 for quick picking
- `contact-sheet.png` — rendered gallery
- `render.cjs` — Puppeteer script to re-render all PNGs (`node videos/claude-code-large-codebases/thumbnail/render.cjs`)

## Usage

Upload the chosen `variant-NN.png` to YouTube Studio as the custom thumbnail.

To re-render after HTML edits:
```bash
node videos/claude-code-large-codebases/thumbnail/render.cjs
```
