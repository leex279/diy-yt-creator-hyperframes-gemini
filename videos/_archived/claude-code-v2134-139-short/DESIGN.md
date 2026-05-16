# DESIGN — Claude Code Version Update Shorts (GitHub-Dark Stage)

Visual system for **vertical Claude Code release-update Shorts** (1080x1920, 30fps, 60-180s). Forked from [`templates/shorts/anthropic/DESIGN.md`](../anthropic/DESIGN.md). Inherits anthropic-dark's typography, motion, layout, audio, and "What NOT to Do" rules verbatim — variant deltas are limited to **palette + variant-specific surfaces (VersionBranding overlay, 3-pill stats opener, numbered highlight cards, terminal-window CTA)**.

## Style Prompt

A GitHub-dark stage tuned for Claude Code releases on vertical canvas. Off-white type sits on `#0D1117` (the GitHub dark surface). The accent triad is Claude Code's own palette: cyan-blue (`#58A6FF`) for primary / version reference, purple (`#A371F7`) for tertiary, green (`#3FB950`) for success / improved. Orange (`#F78166`) handles warnings and the Subscribe pulse — not the hero. A persistent VersionBranding overlay (Anthropic + Claude Code logos top-right at 0.7 opacity, repo URL + version string bottom-center) frames every phase as part of the Claude Code visual identity. The composition opens cold on the stats opener — there is no spoken version slam. The version sits as a static 130px reference above the stat pills, visible from frame 0 so viewers can read it but never narrated. The CTA is a macOS terminal block showing `$ claude update` — the canonical close for Claude Code release content.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts) — same as anthropic shorts
- Frame rate: **30fps** — same
- Duration target: **60-180s** (template demo is 24s; release-update Shorts target ~70-130s)
- Background: solid `#0D1117` GitHub-dark surface (was `#0B0F18` near-black with a touch of blue on anthropic). Radial highlights only — never full-screen linear gradients.

## Colors (variant override)

The accent triad is overridden in `tokens/claude-code-dark.css`. Surface, text, and spacing/type families inherit from anthropic shorts.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#0D1117` | GitHub-dark canvas (was `#0B0F18` in anthropic shorts) |
| Card surface | `--card` | `rgba(255,255,255,0.04)` | Dense card panels |
| Card surface (raised) | `--card-bright` | `rgba(255,255,255,0.08)` | Secondary surfaces |
| Border | `--border` | `rgba(255,255,255,0.10)` | Default border |
| Border (bright) | `--border-bright` | `rgba(255,255,255,0.18)` | Active / focused border |
| Primary text | `--text` | `#F1F3F4` | Headlines, body |
| Secondary text | `--text-secondary` | `#9AA0A6` | Captions, meta, fineprint (4.5:1 on bg) |
| Muted text | `--text-muted` | `#64748B` | Disabled / decorative |
| Accent — cyan-blue | `--accent-1` | `#58A6FF` | Primary lead, static version header (Phase 1), stat-pill 1 (features), highlight-card 1, terminal flag |
| Accent — purple | `--accent-3` | `#A371F7` | Stat-pill 2 (fixes), highlight-card 2 |
| Accent — green | `--accent-4` | `#3FB950` | Stat-pill 3 (improved), highlight-card 3, terminal `$` prompt |
| Warn / hero stat | `--accent-warn` | `#F78166` | Phase-1 overline, Phase-2 overline, Subscribe pulse glow |
| Pill bg | `--pill-bg` | `rgba(255,255,255,0.06)` | Caption pill, default chip fill |
| Pill border | `--pill-border` | `rgba(255,255,255,0.18)` | Caption pill stroke |

Legacy alias vars (`--orange`, `--purple`, `--blue`, `--green`, `--red`) are also declared in `tokens/claude-code-dark.css`. They map onto the Claude Code triad so any block / component pulled from `shared/lib/` (which references the legacy names) renders correctly without rewrite.

**Contrast verified (WCAG, body text on `#0D1117`):**

- Primary text (`#F1F3F4`) on bg: ~14:1 (AAA)
- Secondary text (`#9AA0A6`) on bg: 4.7:1 (AA normal)
- Cyan-blue `#58A6FF` on bg: 6.4:1 (AA normal — safe for 40px+ headings)
- Orange `#F78166` on bg: 5.4:1 (AA normal — safe for overlines and the subscribe pill at 38px)

**Accent rotation rule:** within one video, each phase pins one accent. Phase 1 (stats opener with version header): version header pins cyan-blue, then 3 stat pills rotate cyan/purple/green top-to-bottom. Phase 2 highlight cards rotate cyan/purple/green top-to-bottom. Phase 3 CTA uses cyan + green (terminal) and orange (Subscribe pulse). Orange is NEVER on a highlight card or a stat pill — that's the warn / brand pulse channel.

## Typography

Inherits anthropic shorts verbatim. `--sans` Inter (workhorse for hero, headline, body), `--mono` JetBrains Mono (overlines, version string, dates, code). Two families, no exceptions.

**Type scale (Shorts-tuned, variant overrides marked):**

| Role | Size | Notes |
|---|---|---|
| Static version header (Phase 1) | 130px | Cyan-blue with cyan glow; tabular-nums for `vN.M.PPP`. NOT animated as a slam — visible from frame 0, never narrated. |
| Headline (Phase 1) | 56px | One-line release-character line below the version (e.g. "MCP got a stability pass."), echoing on-screen but typically not the spoken hook |
| Stat number (Phase 1 pills) | 140px | -40px from anthropic's 180px because there are 3 pills horizontally instead of 2 — width-bounded |
| Stat label (Phase 1) | 38px | +8px from anthropic's 30px because the 3-pill layout has wider per-pill copy room than 2-pill |
| Highlight card title (Phase 2) | 38px | -2px from anthropic's 40px (tighter row gap on numbered cards) |
| Highlight card sub (Phase 2) | 26px | -2px from anthropic's 28px |
| Number badge (Phase 2) | 48px | mono 900, solid accent fill, near-black `color: var(--bg)` for AAA contrast — replaces anthropic's date chip |
| Terminal content (Phase 3) | 38px | mono; `$` prompt green, flag (`update`) cyan-blue |
| Subscribe pill (Phase 3) | 38px | sans 700; orange arrow at 48px |
| Section overline | 36px | mono 700, UPPERCASE, letter-spacing 6px — same as anthropic |
| VersionBranding URL | 22px | mono, secondary text, letter-spacing 1px — bottom-center for vertical canvas (long-form bottom-right) |

**Tabular numerals on stat numbers and the version header:** `font-variant-numeric: tabular-nums lining-nums` so digits don't jitter across springs.

## Layout

Inherits anthropic shorts verbatim. `--pad-top: 240px`, `--pad-x: 60px`, `--pad-bottom: 240px`. Phase content MUST use `width: 100%; height: 100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display: flex; flex-direction: column; box-sizing: border-box`.

**Phase mutex:** only one phase visible at any frame. Crossfades on whole phases, not individual elements.

## Motion Language

Inherits anthropic shorts verbatim. Same easing palette (`back.out(1.7)` slam, `back.out(1.6)` stat pop, `back.out(1.5)` card slide-in, `back.out(1.4)` terminal entrance, `power3.out` headline rise, `power2.out` body, `expo.out` URL slam, `power1.in` outgoing blur, `sine.inOut` ambient breath). Stagger 80-140ms body, 200-280ms cards, 500ms between adjacent stat pills.

**No inline shake on the version header.** The previous slam pattern (4 ticks ±5px on a 200px hero) was dropped — the version is now a static visual reference, not a narrated payload. Reserve percussive shakes for hero stat reveals if a future variant calls for them.

**Subscribe pulse** (Phase-3 CTA, variant-specific): `boxShadow` glow tween at `rgba(247, 129, 102, 0.40)`, `yoyo: true, repeat: 4`, 0.7s per half-cycle = ~3.5s span. Finite repeat — never `repeat: -1`.

## Variant-specific Surfaces

### VersionBranding overlay (`#version-branding`)

Persistent overlay rendered for full composition duration. Sits inside `#root` but outside any phase wrapper.

- **Container:** `position: absolute; inset: 0; opacity: 0.7; pointer-events: none; z-index: 9` (below the noise overlay at z-index 11, above all phases at z-index 1-4).
- **Logo stack** (`.vb-logos`): `position: absolute; top: 30px; right: 30px; display: flex; flex-direction: column; gap: 12px`. Two `<img>` elements, **200px** wide each (40px narrower than long-form's 240px to leave more room for the vertical canvas's tighter horizontal real estate): `assets/anthropic-logo-light.svg` then `assets/claude-code-logo-light.svg`.
- **Version string** (`.vb-version`, id `vb-version-string`): `position: absolute; bottom: 24px; left: 30px; right: 30px; text-align: center; font-family: var(--mono); font-size: 22px; color: var(--text-secondary); letter-spacing: 1px`. Bottom-**center** on the vertical canvas (long-form is bottom-right). Default content `github.com/anthropics/claude-code/releases  |  vX.Y.Z` — the slash command swaps the version string per release.
- **Animation:** root timeline does `tl.from("#version-branding", { opacity: 0, duration: 0.8, ease: "power2.out" }, 0.4)`. After the initial fade-in it stays visible for the rest of the composition.
- **Lint compliance:** the overlay does NOT have `class="clip"` (matches the rule for persistent visual chrome — `<audio>` and `<video>` never get `class="clip"`, and the same logic applies to non-clip wrappers).

**Brand-zone choice (per video):** ships with `#top-banner { display: none }` so VersionBranding is the single brand surface. Lint cleanly rejects two `<img>` elements with the same source/start/duration; when you re-enable the centered top-banner per video, source it from a different file (e.g. `assets/claude-logo-light.svg`) — never from `anthropic-logo-light.svg` (already in VersionBranding).

### 3-pill stats opener (Phase 2)

3-pill receipts row scaled for the vertical canvas. Used as the second phase of a Claude Code release Short — "27 features / 56 fixes / 11 improved" or similar.

- **Layout:** `display: flex; flex-direction: column; gap: 24px`. Each pill stretches to **920px** wide (vs anthropic's 460px each on a 2-pill horizontal row), 32px vertical padding × 40px horizontal padding, `border-radius: 28px`, `min-height: ~120px`.
- **Per-pill internal layout:** `flex-direction: row` so the huge stat-num sits on the LEFT (right-aligned, tabular-nums, min-width 220px) and the mono label sits on the RIGHT (left-aligned, flex: 1). This reads better than the long-form's column-stack on a vertical canvas because vertical real estate is precious.
- **Accent rotation:** pill 1 cyan-blue (`--accent-1`, "features"), pill 2 purple (`--accent-3`, "fixes"), pill 3 green (`--accent-4`, "improved"). Each pill has a colored gradient bg + matching border + matching `text-shadow` glow on the digit.
- **Stagger:** overline → headline → pill 1 → pill 2 → pill 3 at 0 / 0.3 / 0.9 / 1.4 / 1.9s relative to phase start.

### Numbered highlight cards (Phase 3)

Replaces anthropic's dated timeline cards with `01/02/03` number badges. Used to surface the top 3 highlights of the release without committing to specific dates (release-update content is single-event, not timeline).

- **Layout:** `display: flex; flex-direction: column; gap: 24px; width: 940px` — same as anthropic.
- **Per-card layout:** `flex-direction: row; gap: 26px; padding: 26px 32px; border-radius: 20px` — same as anthropic.
- **Number badge** (`.hl-num`): solid accent fill (cyan / purple / green rotation), `width: 96px; height: 96px; border-radius: 18px; font-family: var(--mono); font-weight: 900; font-size: 48px; color: var(--bg)`. Replaces anthropic's `min-width: 160px` date chip — the square badge reads as "step 1 / 2 / 3" rather than "Mar 4 / 26 / Apr 16".
- **Card body** (`.hl-body`): title `font-family: var(--sans); font-weight: 800; font-size: 38px`; sub `font-family: var(--mono); font-weight: 600; font-size: 26px` in the matching accent color.
- **Stagger:** overline → card 1 → card 2 → card 3 at 0 / 0.5 / 0.95 / 1.4s relative to phase start (same as anthropic).

### Terminal-window CTA (Phase 4)

Replaces anthropic's URL pill with a macOS-chrome terminal block showing `$ claude update`. CSS duplicated from [`templates/long-form/claude-code-version/compositions/scene-cta.html`](../../long-form/claude-code-version/compositions/scene-cta.html) (single-use; no shared CSS file). Sized for the vertical canvas: 920px wide vs long-form's 1100px, 38px content font-size vs long-form's 28px.

- **Frame:** `width: 920px; border-radius: 20px; overflow: hidden; background: rgba(28, 33, 40, 0.95); box-shadow: 0 25px 60px rgba(0, 0, 0, 0.55), 0 0 0 1.5px rgba(88, 166, 255, 0.4)`.
- **Title bar:** `height: 48px; background: #21262D`; three traffic-light dots (14px circles, `#FF5F56` / `#FFBD2E` / `#27C93F`); centered title in `var(--sans)` 20px secondary.
- **Content:** padding `36px 44px`; `font-family: var(--mono); font-size: 38px; line-height: 1.5`. The `$` prompt is `var(--accent-4)` green; the `update` flag is `var(--accent-1)` cyan-blue; positional args (none here) would be `var(--text-secondary)`.
- **Entrance:** `tl.from("#p3-terminal", { y: 24, scale: 0.96, opacity: 0, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, P4 + 0.5)`.

### Subscribe pulse (Phase 4)

Inherits anthropic's Subscribe pill but tunes the glow to Claude Code orange:

```js
tl.to("#p3-subscribe", {
  boxShadow: "0 0 0 6px rgba(247, 129, 102, 0.40)",
  duration: 0.7, ease: "sine.inOut", yoyo: true, repeat: 4
}, P4 + 1.8);
```

`yoyo: true, repeat: 4` is 5 total tweens (≈3.5s span). **Never `repeat: -1`** — deterministic timeline rule.

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Default `sfx-cues.txt` ships with: `impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop` — same as the long-form claude-code-version variant. Volume caps are post-2026-04-28:

| Cue | Use on | `data-volume` |
|---|---|---|
| `scale-slam` | Phase-1 stat-pill entrance (typically pill 1 only) | 0.15 |
| `cinematic-whoosh` | Phase / scene change (transitions T1, T2) | 0.11 |
| `spring-pop` | Highlight card or terminal entrance | 0.11 |
| `pop` | Subscribe pill / number badge entrance | 0.10 |
| `impact-slam` | Reserved — no longer used in the default phase mix | 0.15 |
| `screen-shake` | Reserved — the spoken slam was removed; keep available for future hero stat reveals | 0.11 |
| `glitch-zap` | "BUT…" pivot, regression callout | 0.09 |

Hard cap **0.25** per single per-cue SFX (sonic-logo at 0.45 is the only documented exception). Density target ~2 SFX placements per 10 seconds of narration; cap 2.5 / 10s. **No background music on Shorts** — narration + SFX only.

## What NOT to Do

Inherits anthropic shorts' 8 rules verbatim. Variant-specific additions:

9. **Do NOT reference the same source img twice in `index.html` with the same start/duration.** Lint emits `duplicate_media_discovery_risk`. Specifically: when re-enabling the centered top-banner per video, source it from a file that is NOT already used in VersionBranding (`assets/anthropic-logo-light.svg` is taken).
10. **Do NOT auto-generate `#vb-version-string` text.** The slash command sets it once per release based on the changelog tag — string is a literal, not a render-time placeholder pattern.
11. **Do NOT add `class="clip"` to `#version-branding` or its children.** The overlay is persistent visual chrome; the clip class is reserved for timed media (audio/video).
12. **Do NOT use orange (`--accent-warn`) on highlight cards or stat pills.** Orange is the warn / Subscribe-pulse channel only. Cyan / purple / green rotate through the cards and pills.
13. **Do NOT use `repeat: -1` on the Subscribe pulse.** The existing `yoyo: true, repeat: 4` is the deterministic finite pattern.
