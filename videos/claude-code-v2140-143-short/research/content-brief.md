# Content Brief — Claude Code v2.1.140 → v2.1.143 — Short

## Version Range
v2.1.140, v2.1.141, v2.1.142, v2.1.143  (four consecutive releases)

Slug: `claude-code-v2140-143-short`
Render target: 1080x1920 vertical, 30fps, ≤180s. Narration target ~78-85s; composition ~85s (5s Dynamous endcard at tail).

## Reused-from
**Fresh fetch** — no long-form video exists for this range (checked `videos/` + `videos/_archived/` 2026-05-16).

## Stats (Phase 1 — three pills)

Counts derived from `research/changelog-official.md` summary table:

- **Features:** `14`  (0 from v2.1.140 + 5 from v2.1.141 + 5 from v2.1.142 + 5 from v2.1.143 with light overlap dedup)
- **Fixes:** `80`  (~8 + ~23 + ~21 + ~34, rounded down conservatively)
- **Improvements:** `20`  (3 + 6 + 3 + 3, rounded up to absorb partial polish items)

These are the on-screen stat-pill values. They're verifiable in the linked changelog and round to easy-to-read numbers.

## Top 6 Highlights (Phase 2 — 6 cards across 2 sets)

Lead with universal-appeal wins, then pivot to power-user wins in Set B.

| # | Set | Title | Sub | Source | Why it matters |
|---|---|---|---|---|---|
| 01 | A | Ripgrep is the new grep | Faster code search by default | v2.1.142 | Built-in grep tool now uses ripgrep under the hood. Faster, more accurate, consistent across OSes. Universal dev win. |
| 02 | A | `claude agents` flag pack | --add-dir, --settings, --mcp-config | v2.1.142 | Subagent invocation now takes flags for working dir, settings file, MCP config, plugin dir, permission mode, model, and effort. Pin a subagent to exactly the tools and rules you want. |
| 03 | A | Plugin price tags land | Per-turn token cost shown | v2.1.143 | Plugin marketplace now displays per-turn and per-invocation token cost estimates. See the cost before you install. |
| 04 | B | Summarize up to here | Rewind menu compresses old turns | v2.1.141 | New rewind option compresses earlier context while preserving recent turns. Long sessions stop bleeding tokens. |
| 05 | B | Hooks get terminalSequence | Notifications without a TTY | v2.1.141 | Hook JSON output now supports terminal escape sequences. Emit notifications, window titles, even bells from hooks — no TTY required. |
| 06 | B | Sleep-resilient sessions | Clock jumps no longer break | v2.1.142+143 | Daemon detects clock jumps after macOS sleep/wake; background sessions preserve model and effort level on resume. No more silent model resets. |

## Hook Angle

Four Claude Code releases shipped in four days. The receipts: ripgrep is the new default search, `claude agents` finally gets a flag pack, and the plugin marketplace puts a price tag on every install.

## Caption Pill Text

(Not used in this template — Phase 1 ships `#p1-headline` instead. Leave headline as "The receipts.")

## Phase 1 (Stats opener with version header)

- Header overline: `Claude Code Update`
- Version slam (static, no animation): `v2.1.140 → v2.1.143`
- Headline: `The receipts.`
- Stat pills: `14 features` · `80 fixes` · `20 improved`

## Phase 2 (Highlight cards — 6 cards in 2 sets)

- **Set A (cards 01-03) — universal wins.** P2 = ~10s. Card 01 anchors at narration's first card cue ("First..."). Card 02 at "Second...". Card 03 at "Third...".
- **Set A → Set B crossfade** at P2_SET_B_AT (~the moment narration says "Fourth.").
- **Set B (cards 04-06) — power-user wins.** Card 04 at the crossfade. Card 05 at "Fifth...". Card 06 at "Sixth...".

## Phase 3 / Endcard

No `$ claude update` CTA — the Dynamous endcard owns the last 5s (template default).

**Debate question** (spoken + on-screen during last 3-5s of Phase 2):

> "Ripgrep, claude agents flags, or plugin price tags — which one wins? Drop a comment."

**Dynamous outro line** (spoken under endcard):

> "If you want to learn more about AI, check out the dynamous dot ai community."

## WatchNext

Skipped — no WatchNext for this Short.

## SFX cues (template-default for this variant)

Cinematic whooshes ONLY, at every phase/set transition. Per `.claude/rules/audio-design.md`:

- T1 (phase 1 → phase 2): `cinematic-whoosh` @ 0.11 volume, 1.5s duration, track 3
- P2_SET_B_AT (Set A → Set B crossfade): `cinematic-whoosh` @ 0.11, 1.5s, track 3
- T2 (phase 2 → endcard): `cinematic-whoosh` @ 0.11, 1.5s, track 3

No per-element impact-slams / spring-pops by default (audio-design rule for Anthropic-derived shorts).
