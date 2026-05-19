# ast-grep-missing-layer — thumbnail variants

15 distinct YouTube thumbnail concepts for the video **ast-grep — the search tool AI agents are missing** (`videos/ast-grep-missing-layer/`).

All variants:
- 1280×720 PNG, sRGB
- VSCode-dark palette: `#0d1117` deep bg, `#1e1e1e` editor, accent yellow `#dcdcaa`, ok `#4ec9b0`, red `#f48771` / `#ff4d4d`
- Brand chrome: `smartcode.diy` text-pill, bottom-right
- Source-grounded numbers only: 22 → 12 files, ~50% tokens, 122% / 30% / 26% / 19% false-hit rates, $0.47 token cost

## Contact sheet

See `_contact-sheet.png` — 3 columns × 5 rows of all variants, labeled.

## Variants

| # | File | Angle | Headline (verbatim) |
|---|---|---|---|
| 01 | `v01-your-agent-is-lying.png` | Hot-take / shock — Anthropic-flavored opener mirrors existing `thumbnail.html` | YOUR AGENT IS **LYING** TO YOU. |
| 02 | `v02-grep-is-dead.png` | Verdict / dead-or-alive | **grep** IS DEAD. → ast-grep |
| 03 | `v03-stop-using-grep.png` | Directive / stop-doing-X with red banner | STOP USING GREP → GIVE YOUR AGENT **ast-grep** |
| 04 | `v04-half-the-tokens.png` | Number-led — payoff up front | CUT YOUR AGENT'S TOKENS **IN HALF.** |
| 05 | `v05-ais-blind-spot.png` | Blind-spot — all 3 agents X'd | **AI'S** BLIND SPOT. |
| 06 | `v06-one-line-claude-md.png` | CLAUDE.md hook with actual config snippet | **ONE LINE.** CLAUDE.md |
| 07 | `v07-claude-burns-tokens.png` | Agent-victim with fire gradient | CLAUDE CODE **BURNS** TOKENS. |
| 08 | `v08-grep-vs-ast-grep.png` | Tool-vs-tool — split-screen comparison | grep VS ast-grep |
| 09 | `v09-122-percent-waste.png` | Big-number lead — 122% as hero | **122%** OVER-COUNTED. |
| 10 | `v10-tool-claude-missed.png` | Discovery / what's missing — Claude tool stack | THE TOOL CLAUDE **MISSED.** |
| 11 | `v11-logo-led.png` | Logo-led — giant ast-grep arrow + daily hammer punch | THE DAILY HAMMER. → ast-grep |
| 12 | `v12-token-counter-split.png` | Before/after — token counters RED vs GREEN | grep vs **ast-grep** (token counters) |
| 13 | `v13-all-3-agents.png` | Insider — all 3 agents need it | ALL **3 AGENTS** NEED ast-grep. |
| 14 | `v14-refactors-cost-2x.png` | Dev-pain with math receipt | **WHY** YOUR REFACTORS COST 2x MORE. |
| 15 | `v15-the-missing-layer.png` | Stack-led — Read/Glob/Grep/+ast-grep | YOUR AGENT'S **MISSING LAYER.** |

## How they were rendered

`_render-all.py` (Playwright + Pillow) renders every `v[0-9][0-9]-*.html` to its matching PNG at exactly 1280×720, then composes the 3×5 contact sheet. Each HTML imports `_common.css` for shared tokens.

To re-render after editing any variant:

```bash
cd videos/ast-grep-missing-layer/thumbnails
python _render-all.py
```

## Self-check — applied to every variant

Per `.claude/rules/shorts-thumbnail-frames.md`:

1. **Topic test** — every thumbnail names ast-grep AND signals the search/agent problem. ✓
2. **Tap test** — every variant leads with a polarizing or curiosity hook (lying, dead, 122%, burns, missing). ✓
3. **Brand test** — `smartcode.diy` pill bottom-right on every frame, accent-color. ✓
4. **No-context test** — none reduce to a brand-only or CTA-only frame; every one carries the topic + a receipt. ✓

## Notes

- v11 (`logo-led`) is the only frame where the ast-grep arrow logo dominates — useful for channel discovery if a viewer already knows the logo.
- v06 (`one-line-claude-md`) is the most "tutorial-feeling" — best paired with a how-to-style title.
- v09 (`122-percent-waste`) leads with the strongest single number and may CTR best in the feed.
- v01, v07, v14 carry the most aggressive contrarian framing.
- v04, v12 lead with the savings payoff (best for retention-quote viewers).

Pick the winner; the rest can be A/B'd or repurposed for community-tab posts.
