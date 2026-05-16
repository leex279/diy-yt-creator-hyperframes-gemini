# Content Brief — Claude Code v2.1.134 → v2.1.139 — Short

## Version Range
v2.1.136, v2.1.137, v2.1.138, v2.1.139  (v2.1.134 + v2.1.135 absent from upstream changelog)

Slug: `claude-code-v2134-139-short`
Render target: 1080x1920 vertical, 30fps, ≤180s. Narration runtime ~108.6s; composition 109s (5s Dynamous endcard at the tail).

## Reused-from
Fresh fetch — no long-form video exists for this range.

## Stats (Phase 1 — three pills)

Counts derived from `research/changelog-official.md`:

- **Features:** `9`  (7 from v2.1.139 + 2 from v2.1.136 — `Added …` bullets)
- **Fixes:** `73`  (~31 from v2.1.139, ~40 from v2.1.136, 1 from v2.1.137, plus v2.1.138's "internal fixes" counted as 1)
- **Improvements:** `14`  (10 silent-improvement bullets from v2.1.139 + 4 from v2.1.136 — `Improved …`, `Changed …`, behavior updates)

## Top 9 Highlights (Phase 2 — numbered cards, 3 sets)

User-confirmed top 3 lead (cards 01-03). Cards 04-06 are the second-strongest from v2.1.139 + v2.1.136 (technical / power-user). Cards 07-09 are broad-appeal items I left out of the 6-card cut at the user's request — added on expand pass.

| # | Title | Sub | Source | Why it matters |
|---|---|---|---|---|
| 01 | Agent view ships | `claude agents` · all sessions | v2.1.139 | First-ever multi-session dashboard. Run `claude agents` and see every session's state (running / blocked / done) in one list. |
| 02 | `/goal` runs across turns | set a condition, walk away | v2.1.139 | Set a completion condition; Claude keeps working with live elapsed / turns / tokens until it's met. |
| 03 | `hard_deny` lands | `autoMode.hard_deny` rule | v2.1.136 | Unconditional block rules — the classifier cannot override them. Hard safety lever for auto mode. |
| 04 | Transcript by keyboard | `?` `{` `}` `v` shortcuts | v2.1.139 | `?` shows shortcuts, `{`/`}` jumps between user prompts, `v` toggles the panel. Reviewing long sessions is finally pleasant. |
| 05 | Plugin price tags | `claude plugin details` | v2.1.139 | Shows a plugin's component inventory AND projected per-session token cost — see the price tag before installing. |
| 06 | MCP OAuth tokens stay | no more daily re-auth | v2.1.136 | Concurrent refreshes across multiple MCP servers no longer drop tokens. Multi-server setups stop forcing a daily re-auth. |
| 07 | Smarter context trimming | user intent kept on compaction | v2.1.139 | Compaction prompt now asks the model to preserve sensitive user instructions — long sessions stop losing intent on trim. |
| 08 | Auth deadlock fixed | claude auth login no longer hangs | v2.1.139 | The deadlock that blocked `claude auth login` / `logout` / `status` on expired credentials is patched. |
| 09 | `/mcp` hot reload | `.mcp.json` edits, no restart | v2.1.139 | `/mcp` Reconnect now picks up `.mcp.json` edits without a CLI restart. Server config iteration speeds up. |

## Hook Angle

Six Claude Code releases — and the receipts: agent view ships, `/goal` works across turns, and `hard_deny` finally lets you say "no, never" in auto mode.

## Caption Pill Text

"Six releases · the receipts"

## Phase 1 (Stats opener with version header)

- Header overline: `Claude Code Update`
- Version slam (static, no animation): `v2.1.134 → v2.1.139`
- Headline: "The receipts."
- Stat pills: `9 features` · `73 fixes` · `14 improved`

## Phase 2 (Highlight cards)

Three sets of 3 cards each.
- Set A (cards 01-03) — headline releases. P2 = 9.4s.
- Set B (cards 04-06) — power-user technical. P2_SET_B_AT = 42.5s.
- Set C (cards 07-09) — broad-appeal QoL fixes. P2_SET_C_AT = 69.05s (tight 0.35s crossfade).

## Phase 3 (Dynamous outro)

No `$ claude update` CTA — the Dynamous endcard owns the last 5 seconds. Spoken outro is the locked line from `_template-wiring-snippet.md` step 5:

> "If you want to learn more about AI, check out the dynamous dot ai community."

Debate question goes immediately before the Dynamous line:

> "Which patch matters most — agent view, slash goal, or hard deny? Drop a comment."

## WatchNext

Skipped — no WatchNext for this short.
