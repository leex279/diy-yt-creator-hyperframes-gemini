# Claude Code Dark — GitHub-Dark Stage

**Mood:** GitHub-native, release-update precision | **Best for:** Claude Code release-update Shorts and long-form videos, dev-tool changelog posts, terminal-driven product updates.

A GitHub-dark stage tuned for Claude Code releases. Off-white type sits on `#0D1117` (the GitHub dark surface). The accent triad is Claude Code's own palette: cyan-blue for primary / version slam, purple for tertiary, green for success / improved. Orange handles warnings and Subscribe-pulse glow — never the hero. Scenes are framed by a persistent **VersionBranding** overlay (Anthropic + Claude Code logos top-right at 0.7 opacity, repo URL + version string at the bottom). The canonical CTA is a macOS terminal block showing `$ claude update` — instantly readable as the post-release update command for any Claude Code viewer.

## Tokens

[`shared/lib/tokens/claude-code-dark.css`](../tokens/claude-code-dark.css)

Defines: `--bg`, `--card`, `--card-bright`, `--border`, `--border-bright`, `--text`, `--text-secondary`, `--text-muted`, `--text-dim`, `--accent-1`, `--accent-3`, `--accent-4`, `--accent-warn`, `--accent-stat`, `--orange`, `--purple`, `--blue`, `--green`, `--red`, `--pill-bg`, `--pill-border`, `--pad-top`, `--pad-x`, `--pad-bottom`, `--mono`, `--sans`.

The legacy `--orange` / `--purple` / `--blue` / `--green` aliases map onto the Claude Code triad so blocks/components pulled from the lib (which reference the legacy names) render correctly without rewrite.

## Palette roles

| Role         | Token            | When to use                                                                  |
| ------------ | ---------------- | ---------------------------------------------------------------------------- |
| Background   | `--bg`           | Canvas (`#0D1117`) + number-badge text color (near-black for AAA contrast).  |
| Card surface | `--card`         | Default card panel fill (transparent white over canvas).                     |
| Body         | `--text`         | Headlines, body — off-white `#F1F3F4`.                                       |
| Caption      | `--text-secondary` | Secondary lines, VersionBranding URL string, terminal title.               |
| Primary      | `--accent-1`     | Cyan-blue — version slam, stat-pill 1 (features), highlight-card 1, terminal flag (`update`). |
| Tertiary     | `--accent-3`     | Purple — stat-pill 2 (fixes), highlight-card 2.                              |
| Success      | `--accent-4`     | Green — stat-pill 3 (improved), highlight-card 3, terminal `$` prompt.       |
| Warn / pulse | `--accent-warn`  | Orange — Phase-1 / Phase-2 overlines, Subscribe pill bg + glow pulse, regression callouts. |

**Accent rotation rule:** within one video, each phase pins one accent. Phase 1 leads cyan; Phase 2 stat pills rotate cyan → purple → green left-to-right (or top-to-bottom on vertical canvas); Phase 3 highlight cards rotate cyan → purple → green; Phase 4 CTA uses cyan + green (terminal) and orange (Subscribe pulse). Orange is NEVER on a highlight card or stat pill — that's the warn / brand-pulse channel only.

## Typography

| Role             | Family                                | Weight | Treatment                                                |
| ---------------- | ------------------------------------- | ------ | -------------------------------------------------------- |
| Hero / version slam | `--sans` (Inter)                   | 900    | `letter-spacing: -4px`, cyan glow, `tabular-nums`        |
| Headline         | `--sans` (Inter)                      | 800    | `letter-spacing: -1px`, line-height 1.05                 |
| Body             | `--sans` (Inter)                      | 500-700 | line-height 1.3-1.4                                     |
| Section overline | `--mono` (JetBrains Mono)             | 700    | UPPERCASE, `letter-spacing: 6px`, accent color           |
| Number badge     | `--mono` (JetBrains Mono)             | 900    | `letter-spacing: 1px`, tabular-nums, solid accent fill   |
| Stat number      | `--sans` (Inter)                      | 900    | `tabular-nums`, `letter-spacing: -4px`                   |
| URL / code / version | `--mono` (JetBrains Mono)         | 600-700 | `letter-spacing: 1-2px`                                 |
| Terminal content | `--mono` (JetBrains Mono)             | 400    | `line-height: 1.5`; `$` green, flag cyan-blue, args secondary |

**Type scale (Shorts-tuned):** Version slam 200px · Headline 56px · Pre-line 64px · Stat number 140px · Number badge 48px · Highlight title 38px · Terminal 38px · Overline 36px · Caption 30px · Sub 26px · VersionBranding URL 22px.

## Motion Signature

| Easing           | Use for                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| `back.out(1.7)`  | Phase-1 version slam entrance (the signature spring)                   |
| `back.out(1.6)`  | Stat-pill pop entrances                                                |
| `back.out(1.5)`  | Highlight-card slide-ins with overshoot                                |
| `back.out(1.4)`  | Terminal-window scale + opacity reveal                                 |
| `power3.out`     | Headlines and primary text rises                                       |
| `power2.out`     | Body / chip / pill text entrances + outgoing scene blur                |
| `expo.out`       | High-impact one-element reveals                                        |
| `power1.in`      | Outgoing scene blur+fade                                               |
| `sine.inOut`     | Ambient breath + Subscribe pulse glow                                  |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Stagger:** 80-140ms on body lists; 200-280ms between adjacent highlight cards; 500ms between adjacent stat pills (3-pill row).

**Inline shake** on the impact frame of the version slam (4 ticks, ±5px, 40ms each). One shake per phase max.

**Subscribe pulse**: `boxShadow` glow tween at `rgba(247, 129, 102, 0.40)`, `yoyo: true, repeat: 4`, 0.7s per half-cycle. Finite repeat — never `repeat: -1`.

## Suggested Lib Picks

| Block / Component / Effect                                                | Use for                                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [`tokens/claude-code-dark.css`](../tokens/claude-code-dark.css)           | Always link first — every other entry depends on these tokens     |
| [`components/ambient-radial`](../components/ambient-radial/)              | Background depth — cyan-blue + purple + green breath              |
| [`components/progress-bar`](../components/progress-bar/)                  | Bottom-edge time progress (accent-1 cyan-blue)                    |
| [`effects/phase-crossfade.js`](../effects/phase-crossfade.js)             | Phase / scene transitions (blur + opacity, 1.1s span)             |
| [`effects/hero-slam-shake.js`](../effects/hero-slam-shake.js)             | Impact-frame shake on the version slam                            |
| [`effects/stat-pill-pop.js`](../effects/stat-pill-pop.js)                 | Stat-pill scale-pop entrance                                      |

**Variant-specific picks not yet in the lib:**

- VersionBranding overlay (top-right Anthropic + Claude Code logos + bottom URL line) — currently inlined in [`templates/shorts/claude-code-version/index.html`](../../../templates/shorts/claude-code-version/index.html) and [`templates/long-form/claude-code-version/index.html`](../../../templates/long-form/claude-code-version/index.html). Consider extracting to `shared/lib/components/version-branding/` if a third release-update variant lands.
- Macos terminal-window block (`$ claude update`) — currently inlined in the Phase-4 CTA of [`templates/shorts/claude-code-version/index.html`](../../../templates/shorts/claude-code-version/index.html) and as `compositions/scene-cta.html` + `compositions/scene-terminal.html` in the long-form variant.

## Surface detail formulas

- **Stat pill (3-row, vertical canvas):** `width: 920px; padding: 32px 40px; border-radius: 28px; background: linear-gradient(135deg, <accent>33, <accent>0d); border: 2px solid <accent>73; box-shadow: 0 14px 36px <accent>33`. Stat number (140px) right-aligned with min-width 220px; label left-aligned, flex: 1.
- **Highlight card (numbered):** `padding: 26px 32px; border-radius: 20px; background: linear-gradient(135deg, <accent>29, <accent>0d); border: 2px solid <accent>73; box-shadow: 0 10px 30px <accent>33`. 96×96 number badge with solid accent fill, `color: var(--bg)` for AAA.
- **Number badge:** mono 900, 48px, letter-spacing 1px, `border-radius: 18px`, solid accent fill, `color: var(--bg)` for high contrast.
- **Terminal window (vertical canvas):** `width: 920px; border-radius: 20px; background: rgba(28, 33, 40, 0.95); box-shadow: 0 25px 60px rgba(0,0,0,0.55), 0 0 0 1.5px rgba(88,166,255,0.4)`. 48px title bar with `#FF5F56`/`#FFBD2E`/`#27C93F` traffic lights and centered title in secondary text.
- **Subscribe pill:** `padding: 18px 36px; border-radius: 999px; background: linear-gradient(135deg, rgba(247,129,102,0.18), rgba(247,129,102,0.05)); border: 1.5px solid rgba(247,129,102,0.55)`. Orange arrow at 48px, sans 900.
- **VersionBranding overlay:** `position: absolute; inset: 0; opacity: 0.7; z-index: 9; pointer-events: none`. Logo stack 200px wide × 2 stacked top-right; URL line bottom-center mono 22px secondary.
- **Ambient:** dual radial wash (cyan-blue + purple) on the canvas, 30s sine yoyo. Scoped to never compete with phase content.

## Audio / SFX

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Volume caps post-2026-04-28 — see the cue table there.

Default `sfx-cues.txt` for this aesthetic: `impact-slam` (version slam), `scale-slam` (stat pills), `cinematic-whoosh` (phase transitions), `spring-pop` (highlight cards), `pop` (number badges).

**No background music on Shorts.** Narration + SFX only.

## What NOT to Do

1. No light canvas. This style is GitHub-dark (`#0D1117`) only.
2. No more than one accent per phase — pick cyan OR purple OR green for that phase's chrome.
3. No serif headlines — Inter only.
4. No flashing strobes / glitches longer than 6 frames.
5. No `<br>` in content text — use `max-width` for natural wrapping.
6. No background music on Shorts — narration + SFX only.
7. No `position: absolute; top: Npx` on `.phase-content` — use padding for content positioning.
8. No accent below 40px — cyan/purple/green don't carry contrast for body text. Reserve them for hero, headline, badges, borders, single accent words.
9. No same-source img twice with same start/duration — `anthropic-logo-light.svg` is taken by VersionBranding.
10. No auto-generated `#vb-version-string` text at render time — set once per release.
11. No `class="clip"` on `#version-branding` or its children.
12. No orange (`--accent-warn`) on highlight cards or stat pills — orange is the warn / Subscribe-pulse channel only.
13. No `repeat: -1` on the Subscribe pulse — finite `yoyo: true, repeat: 4` only.
