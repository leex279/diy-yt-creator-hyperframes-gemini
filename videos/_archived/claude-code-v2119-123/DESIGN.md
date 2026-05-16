# DESIGN — Long-Form Claude Code Version Update Variant

Visual system for **horizontal Claude Code release-update videos** (1920x1080, 30fps, ~3-5 minutes). Forked from [`templates/long-form/standard/DESIGN.md`](../standard/DESIGN.md). Inherits standard's typography, motion, layout, audio, and "What NOT to Do" rules verbatim — variant deltas are limited to **palette + variant-specific surfaces (VersionBranding overlay, terminal-window scene, 3-pill stats opener, feature-cards layout modes)**.

## Style Prompt

A GitHub-dark stage tuned for Claude Code releases. Off-white type sits on `#0D1117` (the GitHub dark surface). The accent triad is Claude Code's own palette: cyan-blue (`#58A6FF`) for primary, purple (`#A371F7`) for tertiary, green (`#3FB950`) for success/improvements, orange (`#F78166`) for warnings and hero stats. Persistent VersionBranding overlay (Anthropic + Claude Code logos top-right at 0.7 opacity, repo URL + version string bottom-right) frames every scene as part of the Claude Code visual identity. Terminal-window scenes carry the macOS chrome (`#FF5F56`/`#FFBD2E`/`#27C93F` traffic lights) and JetBrains Mono content. Otherwise reads exactly like the standard long-form: premium engineering documentary, scene crossfades, ambient breath, finite deterministic motion.

## Canvas

- Resolution: **1920 x 1080** (horizontal, full HD) — same as standard
- Frame rate: **30fps** — same as standard
- Duration target: **3-5 minutes** (template demo is 120s)
- Background: solid `#0D1117` GitHub-dark surface. Radial highlights only.

## Colors (variant override)

The 6 accent vars are overridden in `tokens/long-form.css`. Surface, text, spacing, and type families inherit from standard.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#0D1117` | GitHub-dark canvas (was `#0B0F1A` in standard) |
| Card surface (default) | `--bg-card` | `rgba(255,255,255,0.04)` | inherited |
| Card surface (raised) | `--bg-surface` | `rgba(255,255,255,0.08)` | inherited |
| Border (default) | `--border` | `rgba(255,255,255,0.10)` | inherited |
| Border (bright) | `--border-bright` | `rgba(255,255,255,0.18)` | inherited |
| Primary text | `--text` | `#F1F3F4` | inherited |
| Secondary text | `--text-secondary` | `#9AA0A6` | inherited |
| Muted text | `--text-muted` | `#64748B` | inherited |
| Accent — cyan-blue | `--accent-1` | `#58A6FF` | Primary lead, stats-opener cyan pill, terminal flag, feature-card #1 |
| Accent — cyan | `--accent-2` | `#06B6D4` | Secondary, terminal overline, video-embed overline (kept from standard for color separation) |
| Accent — purple | `--accent-3` | `#A371F7` | Tertiary, stats-opener purple pill, feature-card #3, side-by-side B |
| Accent — green | `--accent-4` | `#3FB950` | Success, stats-opener green pill, terminal `$` prompt, feature-card #4 |
| Warn — orange | `--accent-warn` | `#F78166` | Hook overline, stat-pill #1, CTA subscribe pulse |
| Stat — orange | `--accent-stat` | `#F78166` | Hero stat slam digits — Claude Code uses one orange for both stats and warnings |

**Contrast verified (WCAG, body text on `#0D1117`):**

- Primary text (`--text`): ≥14:1 (AAA)
- Accent text on dark bg passes AA at ≥18.5px / 700 weight; below that, use brighter shades or `--text` instead
- All 57 text elements in the bare template pass `npx hyperframes validate` AA

**Note:** `--accent-stat` and `--accent-warn` resolve to the same hex. Acceptable per the variant's scope — Claude Code uses one orange. The two contexts (hero stat number vs warning callout) are visually distinct from layout/size, not color.

## Typography

Inherits standard verbatim. `--sans` Inter, `--mono` JetBrains Mono. Type scale unchanged.

## Layout

Inherits standard verbatim. `--pad-top: 80px`, `--pad-x: 100px`, `--pad-bottom: 80px`. `#scene-*-content` MUST use `width:100%; height:100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom)`.

**Scene mix differs from standard:**

| Slot | Standard | Variant |
|---|---|---|
| 1 | scene-hook | scene-hook (kept) |
| 2 | scene-image-hero | **scene-stats-opener** (new — 3 stat pills + version badge) |
| 3 | scene-side-by-side | scene-side-by-side (kept) |
| 4 | scene-stat-pill-row | scene-stat-pill-row (kept) |
| 5 | scene-source-cards | **scene-feature-cards** (new — 4-6 card grid, 2x2/3x2/stack layouts) |
| 6 | scene-video-embed | scene-video-embed (kept; commented hooks in `index.html` per release) |
| 7 | scene-architecture-stack | **scene-terminal** (new — macOS terminal chrome, command demo) |
| 8 | scene-cta | scene-cta (adapted — `$ claude update` terminal block replaces next-video card) |

## Motion Language

Inherits standard verbatim. `expo.out`, `back.out(1.4)`, `back.out(1.6)`, `power3.out`, `power2.out`, `power1.in`, `sine.inOut`. Stagger 80-180ms. No `repeat: -1`.

## Variant-specific Surfaces

### VersionBranding overlay (`#version-branding`)

Persistent overlay rendered for full composition duration. Sits inside `#root` but outside any scene wrapper.

- **Container:** `position: absolute; inset: 0; opacity: 0.7; pointer-events: none; z-index: 9` (same z-index as captions, below noise overlay).
- **Logo stack** (`.vb-logos`): `position: absolute; top: 30px; right: 30px; display: flex; flex-direction: column; gap: 12px`. Two `<img>` elements, 240px wide each: `assets/anthropic-logo-light.svg` then `assets/claude-code-logo-light.svg`.
- **Version string** (`.vb-version`, id `vb-version-string`): `position: absolute; bottom: 30px; right: 30px; font-family: var(--mono); font-size: 20px; color: var(--text-secondary); letter-spacing: 1px`. Default content `github.com/anthropics/claude-code/releases  |  vX.Y.Z` — the slash command swaps the version string per release.
- **Animation:** root timeline does `tl.from("#version-branding", { opacity: 0, duration: 0.8, ease: "power2.out" }, 0.4)`. After the initial fade-in it stays visible for the rest of the composition.
- **Lint compliance:** the overlay does NOT have `class="clip"` (matches the rule for persistent visual chrome — `<audio>` and `<video>` never get `class="clip"`, and the same logic applies to non-clip wrappers).

**Brand-zone choice (per video):** the variant ships with `#top-banner { display: none }` so VersionBranding is the single brand surface. Lint cleanly rejects two `<img>` elements with the same source/start/duration, so when you re-enable the centered top-banner per video, source it from a different file (e.g. `assets/claude-logo-light.svg`) — never from `anthropic-logo-light.svg` (already in VersionBranding).

### Terminal window (`compositions/scene-terminal.html`, also reused inline in `scene-cta.html`)

macOS chrome around a code block. Used both as a standalone scene (slot 7) and inline in the CTA scene to show the post-release update command.

- **Frame:** `width: 1400px` (700px in CTA's denser layout); `border-radius: 16px; overflow: hidden; background: rgba(28, 33, 40, 0.95); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.55), 0 0 0 1.5px rgba(88, 166, 255, 0.4)`.
- **Title bar:** `height: 40px` (36px in CTA); `background: #21262D`; three traffic-light dots (12px circles, `#FF5F56` red / `#FFBD2E` yellow / `#27C93F` green); centered title in `var(--sans)` 18px secondary.
- **Content:** padding `36px 44px` (28px 36px in CTA); `font-family: var(--mono); font-size: 32px` (28px in CTA); `line-height: 1.5`. The `$` prompt is `var(--accent-4)` green; flag/subcommand is `var(--accent-1)` cyan-blue; positional args are `var(--text-secondary)`.
- **Entrance:** `tl.from("#term-window", { scale: 0.92, opacity: 0, duration: 0.7, ease: "back.out(1.4)", immediateRender: false }, 0.4)`.

### Stats opener (`compositions/scene-stats-opener.html`)

3-pill receipts row scaled from standard's 2-pill stat-pill-row. Used as the second scene of a Claude Code release video — "5 features / 30 fixes / 7 improved" or similar.

- **Layout:** `display: flex; flex-direction: row; gap: 40px`. Each pill `width: 460px; padding: 56px 36px; border-radius: 28px`.
- **Accent rotation:** pill 1 cyan-blue (`--accent-1`), pill 2 purple (`--accent-3`), pill 3 green (`--accent-4`). Each pill has a colored gradient bg + matching border + matching `text-shadow` glow on the digit.
- **Version badge:** small `vbadge` element above the overline, `font-family: var(--mono); font-weight: 700; font-size: 26px; letter-spacing: 4px; color: var(--accent-1)`. Default content `vX.Y.Z` placeholder; slash command swaps per release.
- **Stagger:** vbadge → overline → headline → pill 1 → pill 2 → pill 3 at 0 / 0.2 / 0.45 / 0.9 / 1.4 / 1.9s.
- **Tabular nums:** `font-variant-numeric: tabular-nums lining-nums` on `.stat-num` ensures 3-digit values (e.g. "120 fixes") don't reflow.

### Feature cards (`compositions/scene-feature-cards.html`)

Configurable grid of 4-6 highlight cards. Replaces standard's `scene-source-cards.html` and `scene-architecture-stack.html` for release-update use cases.

- **Layout class on `.feature-cards` controls the grid:**
  - `.feature-cards--3x2` → 3 columns, default for highlights scenes
  - `.feature-cards--2x2` → 2 columns, default for category sub-scenes
  - `.feature-cards--stack` → 1 column, default for narrative/explanatory category scenes
- **Card shape:** `padding: 28px 28px 24px; border-radius: 18px; min-height: 200px; box-shadow: 0 18px 48px rgba(0, 0, 0, 0.45)`.
- **Card chrome:** number badge top-right (mono 32px accent rotated `--accent-1` → `--accent-2` → `--accent-3` → `--accent-4` → `--accent-warn` → `--accent-1`); title 28px Inter 700; detail 20px Inter 500 secondary; optional code-pill (mono 18px on `rgba(88, 166, 255, 0.12)` with cyan-blue border).
- **Stagger:** `back.out(1.4)`, 0.18s between cards.

### CTA — `$ claude update` block

`compositions/scene-cta.html` swaps standard's next-video thumbnail card for an inline terminal block. CSS is duplicated from `scene-terminal.html` (single-use; no shared CSS file). Subscribe pulse glow uses Claude Code orange (`rgba(247, 129, 102, 0.35)`) instead of standard's blue/orange. Pulse repeat is finite (`yoyo: true, repeat: 4`).

## Audio Bed (long-form-specific)

Inherits standard's 3-segment bg-music + narration + SFX cap rules verbatim. Canonical: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

**Per-cue volume table** is the post-2026-04-28 calibration:

| Cue | `data-volume` |
|---|---|
| `impact-slam` | `0.15` |
| `scale-slam` | `0.15` |
| `screen-shake` | `0.11` |
| `cinematic-whoosh` | `0.11` |
| `spring-pop` | `0.11` |
| `pop` | `0.10` |
| `glitch-zap` | `0.09` |
| `strike-cross` | `0.11` |
| `sonic-logo` | `0.45` |

The variant inherits standard's `sfx-cues.txt` (`impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop`). New cues require adding the source file to `shared/audio/sfx/` first per [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

## What NOT to Do

Inherits standard's 11 rules verbatim. Variant-specific additions:

12. **Do NOT reference the same source img twice in `index.html` with the same start/duration.** Lint emits `duplicate_media_discovery_risk`. Specifically: when re-enabling the centered top-banner per video, source it from a file that is NOT already used in VersionBranding (`assets/anthropic-logo-light.svg` is taken).
13. **Do NOT auto-generate the `#vb-version-string` text.** The slash command sets it once per release based on the changelog tag — string is a literal, not a placeholder pattern at render time.
14. **Do NOT add `class="clip"` to `#version-branding` or its children.** The overlay is persistent visual chrome; the clip class is reserved for timed media (audio/video).
