<!--
  AUTO-MAINTAINED — do not delete the table boundary HTML comments
  further down (the literal sentinel strings LIB-COLON-<KIND>-COLON-BEGIN
  and LIB-COLON-<KIND>-COLON-END inside HTML comments).

  scripts/sync-shared-lib.sh runs on every PostToolUse hook (see
  .claude/settings.json). Workflow:
    - Walks shared/lib/ for entries by kind
    - Adds new entries with a "_TBD_ (added by sync — please fill)" hint
    - Marks rows whose entry no longer exists with "[REMOVED]" prefix
    - Preserves your manual edits to existing rows (Description, Tags)
    - Writes the file only if something changed
-->

# shared/lib/ — Inventory

Single source of truth for what's in `shared/lib/` and what each entry does. Auto-synced by `scripts/sync-shared-lib.sh` on every Write / Edit / Bash via the PostToolUse hook.

**Conventions:**

- Paths are relative to `shared/lib/` (e.g. `blocks/stat-pill-row/`, not the full repo path).
- "Description" should explain WHAT the entry produces visually — not the file format.
- "Tags" are kebab-case, comma-separated, single-token each (`stats`, `numbers`, `dark-stage`).
- Leave description blank only as a last resort — future agents won't know what `stat-pill-row` is.
- See [README.md](./README.md) for how to consume each kind.

## Tokens

CSS variable sets (`:root { --bg: ...; --orange: ...; }`). Copy the `.css` file into `videos/<slug>/tokens/` and `<link>` it from `index.html`.

<!-- LIB:TOKENS:BEGIN -->
| File | Description | Tags |
|---|---|---|
| anthropic-dark.css | Anthropic dark-stage palette, spacing, and typography vars (`--bg`, `--orange`, `--purple`, etc.) | dark-stage, anthropic, palette, tokens |
| claude-code-dark.css | Claude Code release-Short palette (1080x1920): GitHub-dark `#0D1117` + Claude Code accent triad (cyan-blue / purple / green) + orange (warn + Subscribe pulse). Includes legacy `--orange/--purple/--blue/--green` aliases for shared/lib block compat. | dark-stage, claude-code, github-dark, short, palette, tokens, release |
| dynamous-modern.css | Dynamous midroll v3 modern-gradient palette (slate + purple + pink + cyan with red 10% OFF accent) | dark-stage, dynamous, palette, tokens, gradient |
| long-form-standard.css | Generic long-form (1920x1080) palette: dark navy + 4-accent rotation (blue/cyan/purple/green) + orange/yellow warn-stat | dark-stage, long-form, palette, tokens, navy |
| standard-short.css | Warm paper editorial standard short (1080x1920) palette: cream canvas + 5-accent rotation (terracotta/indigo/sage/sunset-gold/warm-rose) + serif/sans/mono triad. Brand-neutral baseline for vertical Shorts. | warm-paper, short, palette, tokens, editorial, baseline, light |
<!-- LIB:TOKENS:END -->

## Blocks

Standalone sub-compositions. Each block lives in its own directory with `block.html` (the composition) and `recipe.md` (wiring instructions). Copy `block.html` into `videos/<slug>/compositions/<name>.html`, then reference via `data-composition-src` in the host `index.html`.

<!-- LIB:BLOCKS:BEGIN -->
| Directory | Description | Dimensions | Tags |
|---|---|---|---|
| dynamous-endcard/ | Last-3s Dynamous CTA stack — wordmark + "Join the Community" + gradient pill + 10% OFF badge + URL, ends with fade-to-black | 1080x1920 | dynamous, cta, outro, endcard, vertical |
| dynamous-module-interstitial/ | Optional 3s mid-video card naming the matching Dynamous AI Mastery module (slide-in from right, hold, slide-out) | 1080x1920 | dynamous, module, interstitial, optional, vertical |
| stat-pill-row/ | Two color-rotated huge-number stat pills with mono labels | 1080x1920 | stats, numbers, vertical, dark-stage |
| timeline-cards/ | Three dated cards stacked vertically, accent rotation orange→purple→blue | 1080x1920 | timeline, dates, cards, vertical, dark-stage |
| url-cta/ | Closing CTA with green-glow URL pill + Subscribe pill | 1080x1920 | cta, url, outro, subscribe, vertical |
<!-- LIB:BLOCKS:END -->

## Components

Paste-in HTML+CSS+JS snippets. Each component lives in its own directory with `component.html` (the snippet) and an inline top-of-file comment naming where to merge each section into the host composition.

<!-- LIB:COMPONENTS:BEGIN -->
| Directory | Description | Tags |
|---|---|---|
| ambient-radial/ | Slow-breathing dual-radial wash (orange + purple) for background depth | background, ambient, decorative, breath |
| dynamous-badge/ | Persistent bottom-left Dynamous mark + dynamous.ai wordmark, opacity 0.55, fades in once at t=3.0s | brand, wordmark, dynamous, bottom-left, persistent |
| dynamous-discount-bubble/ | Opt-in 3-4s pill — logo + Dynamous.ai + red 10% OFF badge + "in the link ↓" (no coupon code field; discount is automatic via the description link) | dynamous, discount, opt-in, time-bounded, tutorial |
| progress-bar/ | Slim 6px linear progress bar at canvas bottom, accent-orange | progress, bottom-edge, accent |
| top-banner-wordmark/ | Persistent brand wordmark in the 60px top safe zone (uses local logo copy) | brand, wordmark, top-banner, persistent |
<!-- LIB:COMPONENTS:END -->

## Effects

Pure GSAP recipes — a single `.js` file with a top-of-file `// SOURCE:` and `// USAGE:` comment, exporting a function you paste into the host `<script>` and call against the timeline.

<!-- LIB:EFFECTS:BEGIN -->
| File | Description | Tags |
|---|---|---|
| hero-slam-shake.js | 4-tick ±5px inline shake for a slam word's impact frame (40ms ticks) | gsap, shake, percussive, slam |
| phase-crossfade.js | Blur+opacity scene-to-scene transition (1.1s span, configurable blur) | gsap, transition, crossfade, blur |
| stat-pill-pop.js | Single-element scale-pop entrance, back.out(1.6) from 0.85 | gsap, entrance, pop, scale |
<!-- LIB:EFFECTS:END -->

## Visual Styles

Named-style fragments — palette + typography + motion signature + suggested lib picks + anti-patterns. Read by the diy-yt-creator playbook (and humans authoring DESIGN.md) to pick lib entries that match a target aesthetic.

<!-- LIB:VISUAL-STYLES:BEGIN -->
| File | Description | Tags |
|---|---|---|
| anthropic-dark.md | Dark-stage Anthropic / Claude postmortem aesthetic (Inter 900 hero, Claude orange, back.out springs) | dark-stage, anthropic, premium, tech |
| claude-code-dark.md | GitHub-dark Claude Code release-update aesthetic for Shorts and long-form: `#0D1117` canvas + cyan-blue/purple/green triad + orange Subscribe pulse + VersionBranding overlay + `$ claude update` terminal CTA. | dark-stage, claude-code, github-dark, release, short, long-form, terminal |
| long-form-standard.md | Generic long-form (1920x1080) dark-navy stage with 4-accent rotation; canonical baseline for horizontal videos and the parent of future long-form variants | dark-stage, long-form, navy, documentary, baseline |
| standard-short.md | Warm paper editorial standard short (1080x1920): cream canvas, 5-accent rotation (terracotta/indigo/sage/sunset-gold/warm-rose), Playfair serif + Inter sans + JetBrains Mono. Sub-composition architecture with 9 scene archetypes. Canonical brand-neutral baseline for vertical Shorts. | warm-paper, short, editorial, baseline, light, sub-compositions |
<!-- LIB:VISUAL-STYLES:END -->
