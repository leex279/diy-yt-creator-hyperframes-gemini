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
| dynamous-deep-navy.css | Classic Dynamous-brand long-form deep-navy palette: `#07090F` canvas + Dynamous Blue `#3B82F6` hero + Cyan `#0EA5E9` halo (NO PURPLE) + Montserrat / JetBrains Mono. Pairs with `templates/long-form/dynamous-slides/`. Distinct from `dynamous-modern.css` (which is the promo-artifact slate+purple+pink palette). | dark-stage, long-form, dynamous, palette, tokens, deep-navy, no-purple |
| dynamous-modern.css | Dynamous midroll v3 modern-gradient palette (slate + purple + pink + cyan with red 10% OFF accent) | dark-stage, dynamous, palette, tokens, gradient |
| editorial-short.css | _TBD_ (added by sync — please fill) |  |
| google-cinematic.css | Google Shorts cinematic-stage palette (1080x1920): `#06080F` deep-navy canvas with four-corner brand glows + canonical Google brand triad (`#4285F4` / `#EA4335` / `#FBBC05` / `#34A853`) + Plus Jakarta Sans + JetBrains Mono. Includes legacy `--orange/--purple/--blue/--green/--red/--yellow` aliases for shared/lib block compat. | dark-stage, google, brand, short, palette, tokens, cinematic |
| google-cinematic-long-form.css | Google brand cinematic palette adapted for long-form (1920x1080): `#0C0C0E` near-black canvas + four canonical Google brand hues (`#4285F4` / `#EA4335` / `#FBBC04` / `#34A853`) re-mapped onto `--accent-1..4` + Google Cloud cyan `#00BCD4` reserved for architecture-stack l5 and progress-bar gradient + Inter (matches V2 reference). Pairs with [`templates/long-form/google/`](../../../templates/long-form/google/). | dark-stage, long-form, google, brand, palette, tokens, cinematic |
| long-form-anthropic.css | Anthropic dark-stage palette adapted for long-form (1920x1080): `#0B0F18` near-black + warm off-white `#F5F1EB` + Claude orange `#E97458` lead + purple/blue/green rotation + red `#D14343` warnings. Same variable NAMES as `long-form-standard.css` for stable per-video overrides. Pairs with [`templates/long-form/anthropic/`](../../../templates/long-form/anthropic/). | dark-stage, long-form, anthropic, palette, tokens, premium |
| long-form-standard.css | Generic long-form (1920x1080) palette: dark navy + 4-accent rotation (blue/cyan/purple/green) + orange/yellow warn-stat | dark-stage, long-form, palette, tokens, navy |
| openai-mono.css | OpenAI Shorts monochrome-editorial palette (1080x1920): `#0A0A0A` off-black canvas with single mint `#10A37F` accent + auxiliary lavender/amber/coral tints + Inter + JetBrains Mono. Includes legacy `--orange/--purple/--blue/--green/--red/--yellow` and `--g-blue/red/yellow/green` aliases for shared/lib + Google-template block compat. | dark-stage, openai, brand, short, palette, tokens, monochrome, mint, editorial |
| standard-short.css | Warm paper editorial standard short (1080x1920) palette: cream canvas + 5-accent rotation (terracotta/indigo/sage/sunset-gold/warm-rose) + serif/sans/mono triad. Brand-neutral baseline for vertical Shorts. | warm-paper, short, palette, tokens, editorial, baseline, light |
<!-- LIB:TOKENS:END -->

## Blocks

Standalone sub-compositions. Each block lives in its own directory with `block.html` (the composition) and `recipe.md` (wiring instructions). Copy `block.html` into `videos/<slug>/compositions/<name>.html`, then reference via `data-composition-src` in the host `index.html`.

<!-- LIB:BLOCKS:BEGIN -->
| Directory | Description | Dimensions | Tags |
|---|---|---|---|
| cinema-title-slam/ | Hero word spring-slams with inline shake, hand-drawn SVG underline draws beneath, tagline fades up, ambient breath hold, full-block fade out (3-tier reveal, 6s) | 1080x1920 | hero, title, slam, vertical, dark-stage, premium |
| dynamous-endcard/ | Last-3s Dynamous CTA stack — wordmark + "Join the Community" + gradient pill + 10% OFF badge + URL, ends with fade-to-black | 1080x1920 | dynamous, cta, outro, endcard, vertical |
| dynamous-midroll/ | 31.5s 6-phase Dynamous AI Mastery promotional break — community / 3 courses (Agentic Coding / Agent Mastery / Second Brain) / CTA / outro. Ports legacy Remotion DynamousMidrollV2 to GSAP; ships its own narration audio + transition SFX, brand-locked content. | 1920x1080 | dynamous, midroll, cta, long-form, horizontal, brand-locked |
| dynamous-module-interstitial/ | Optional 3s mid-video card naming the matching Dynamous AI Mastery module (slide-in from right, hold, slide-out) | 1080x1920 | dynamous, module, interstitial, optional, vertical |
| hostinger-banner-vertical/ | 7s mid-video Hostinger sponsorship card — glass surface with Hostinger wordmark + "Try Hostinger" headline + 3 stacked product pills (Web Hosting / VPS / AI Website Builder) + green 10% OFF badge + DIYSMARTCODE code pill + hostinger.com/DIYSMARTCODE URL + Werbung badge for German ad-law compliance | 1080x1920 | hostinger, sponsor, banner, midroll, vertical, opt-in, werbung |
| hostinger-midroll/ | 20s 5-phase Hostinger AFFILIATE midroll break for long-form — intro hero "Try Hostinger" + 3 product showcases (Web Hosting / VPS / AI Website Builder) each with real hostinger.com screenshot + features list, glass CTA card with DIYSMARTCODE code pill + green 10% OFF badge + URL, "Back to the video." outro. Silent (host narrator covers), brand-locked content, Werbung badge for DE ad-law. Sibling of dynamous-midroll. | 1920x1080 | hostinger, midroll, affiliate, long-form, horizontal, brand-locked, werbung, silent |
| ranking-podium-rise/ | _TBD_ (added by sync — please fill) |  |  |
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
| bar-fill-pulse/ | _TBD_ (added by sync — please fill) |  |
| burst-rays/ | 12-ray tapered sun-burst radiating from origin — radial flash bloom + 30ms-staggered ray scale expand + chromatic aberration peak split (red/cyan), 0.9s | burst, rays, energy, accent, particle, hero |
| camera-flash-pop/ | _TBD_ (added by sync — please fill) |  |
| checkbox-tick/ | _TBD_ (added by sync — please fill) |  |
| cinematic-letterbox-reveal/ | Black bars descend from top + ascend from bottom (~0.5s), hold the letterbox, then retract; inner content clip-reveals from center outward during the hold | cinematic, letterbox, reveal, bars, framing, premium |
| circular-progress-wave/ | _TBD_ (added by sync — please fill) |  |
| confetti-burst/ | Physics-driven SVG confetti — 60 mulberry32-seeded ballistic particles from configurable origin, 4-accent palette, 1.6s gravity arc with fade-out tail | confetti, burst, celebration, particle, deterministic, accent |
| counter-blast/ | _TBD_ (added by sync — please fill) |  |
| dynamous-badge/ | Persistent bottom-left Dynamous mark + dynamous.ai wordmark, opacity 0.55, fades in once at t=3.0s | brand, wordmark, dynamous, bottom-left, persistent |
| dynamous-discount-bubble/ | Opt-in 3-4s pill — logo + Dynamous.ai + red 10% OFF badge + "in the link ↓" (no coupon code field; discount is automatic via the description link) | dynamous, discount, opt-in, time-bounded, tutorial |
| ember-rise/ | _TBD_ (added by sync — please fill) |  |
| film-strip-reveal/ | _TBD_ (added by sync — please fill) |  |
| glitch-text-reveal/ | _TBD_ (added by sync — please fill) |  |
| heartbeat-pulse/ | _TBD_ (added by sync — please fill) |  |
| highlight-marker-sweep/ | _TBD_ (added by sync — please fill) |  |
| hostinger-banner/ | Animated long-form (1920x1080) Hostinger sponsorship banner — Hostinger wordmark + headline + 3 product pills (Web Hosting / VPS / AI Website Builder) + green 10% OFF badge + hostinger.com/DIYSMARTCODE URL panel + Werbung badge for German ad-law compliance. ~8s lifetime, white card with Hostinger purple border. | cta, sponsor, hostinger, banner, long-form, horizontal, animated, werbung |
| kinetic-typography-stack/ | _TBD_ (added by sync — please fill) |  |
| lightning-strike/ | _TBD_ (added by sync — please fill) |  |
| liquid-reveal/ | _TBD_ (added by sync — please fill) |  |
| magnet-snap-letters/ | Per-character fly-in from seeded random offsets with back.out(2.5) spring + lock micro-shudder (tactile "magnetic" feel as letters lock to position) | letters, snap, magnetic, entrance, deterministic, tactile |
| notification-toast-stack/ | _TBD_ (added by sync — please fill) |  |
| portal-ring/ | _TBD_ (added by sync — please fill) |  |
| progress-bar/ | Slim 6px linear progress bar at canvas bottom, accent-orange | progress, bottom-edge, accent |
| rubber-band-snap/ | _TBD_ (added by sync — please fill) |  |
| shockwave-ring/ | _TBD_ (added by sync — please fill) |  |
| subscribe-banner/ | Animated long-form (1920x1080) YouTube subscribe banner — profile + channel name + red SUBSCRIBE pill with idle bell shake + mouse cursor click animation + ripple + bell burst. ~8s lifetime. | cta, subscribe, banner, long-form, horizontal, animated |
| support-banner/ | Animated long-form (1920x1080) "support the channel" banner — three pills (Join / Super Thanks / Buy Coffee) + profile + headline + BMC URL panel. ~8s lifetime, no mouse animation. | cta, support, banner, long-form, horizontal, donations |
| top-banner-wordmark/ | Persistent brand wordmark in the 60px top safe zone (uses local logo copy) | brand, wordmark, top-banner, persistent |
| typewriter-line/ | _TBD_ (added by sync — please fill) |  |
<!-- LIB:COMPONENTS:END -->

## Effects

Pure GSAP recipes — a single `.js` file with a top-of-file `// SOURCE:` and `// USAGE:` comment, exporting a function you paste into the host `<script>` and call against the timeline.

<!-- LIB:EFFECTS:BEGIN -->
| File | Description | Tags |
|---|---|---|
| hero-slam-shake.js | 4-tick ±5px inline shake for a slam word's impact frame (40ms ticks) | gsap, shake, percussive, slam |
| phase-crossfade.js | Blur+opacity scene-to-scene transition (1.1s span, configurable blur) | gsap, transition, crossfade, blur |
| shake-reject.js | _TBD_ (added by sync — please fill) |  |
| stat-pill-pop.js | Single-element scale-pop entrance, back.out(1.6) from 0.85 | gsap, entrance, pop, scale |
<!-- LIB:EFFECTS:END -->

## Visual Styles

Named-style fragments — palette + typography + motion signature + suggested lib picks + anti-patterns. Read by the diy-yt-creator playbook (and humans authoring DESIGN.md) to pick lib entries that match a target aesthetic.

<!-- LIB:VISUAL-STYLES:BEGIN -->
| File | Description | Tags |
|---|---|---|
| anthropic-dark.md | Dark-stage Anthropic / Claude postmortem aesthetic (Inter 900 hero, Claude orange, back.out springs) | dark-stage, anthropic, premium, tech |
| claude-code-dark.md | GitHub-dark Claude Code release-update aesthetic for Shorts and long-form: `#0D1117` canvas + cyan-blue/purple/green triad + orange Subscribe pulse + VersionBranding overlay + `$ claude update` terminal CTA. | dark-stage, claude-code, github-dark, release, short, long-form, terminal |
| dynamous-deep-navy.md | Classic Dynamous-brand long-form (1920x1080) deep-navy workshop stage: `#07090F` canvas + Dynamous Blue `#3B82F6` hero + Cyan `#0EA5E9` secondary halo (NO PURPLE) + Montserrat 300/800 weight-contrast + JetBrains Mono mono-bar eyebrows + persistent dual blue/cyan halo backdrop. Ships 8 scene archetypes (hook-wordmark, headline-accent, big-stat counter, tension-pivot, pillars-3, list-reveal, quote-card, cta). Best for Dynamous workshops, Cole Medin episodes, AI-coding deep-dives. | dark-stage, long-form, dynamous, workshop, deep-navy, montserrat, no-purple |
| editorial-short.md | _TBD_ (added by sync — please fill) |  |
| google-cinematic.md | Google brand cinematic-stage aesthetic for vertical Shorts (1080x1920): `#06080F` deep-navy with four-corner brand glows + Google brand triad (blue/red/yellow/green) + Plus Jakarta Sans 800 hero + JetBrains Mono eyebrow + 5-dot rotating progress rail + persistent Google wordmark + accent-tinted `@handle`. Optional `theme-light` shift surface on the closing phase. | dark-stage, google, brand, short, cinematic, four-color, tweaks-panel |
| google-cinematic-long-form.md | Google brand cinematic aesthetic adapted for horizontal long-form (1920x1080): `#0C0C0E` near-black canvas with four Google-color corner glows (blue NW / red NE / yellow SE / green SW) + canonical four-color rotation on `--accent-1..4` + Google wordmark top-right watermark (180×180, `top:-20, right:30` per V2 Remotion reference) + Google-blue → cyan progress bar + Inter (matches V2). Forked from `long-form-standard` with palette + logo swap; 8 scene archetypes (hook with yellow stat / red overline, image-hero, side-by-side blue+yellow, stat-pill red+yellow, source-cards blue/red/yellow, video-embed, architecture-stack blue/red/yellow/green/cyan, CTA red subscribe pulse). Best for Google Cloud Next / I/O recaps, Gemini / Gemma launches, Workspace AI, Android / Pixel, TPU / DeepMind walkthroughs. | dark-stage, long-form, google, brand, cinematic, four-color, premium |
| long-form-anthropic.md | Anthropic dark-stage adapted for long-form (1920x1080): `#0B0F18` near-black canvas + warm off-white `#F5F1EB` + Claude orange `#E97458` lead, purple/blue/green rotation. Ships 12 scene archetypes including the signature `scene-image-3d-reveal` (perspective + rotateY entrance for blog screenshots), `scene-list-cards` (2×2 step-by-step grid), `scene-quote-card` (180px orange quote-mark + marker-sweep), `scene-dynamous-midroll` (opt-out community plug), `scene-subscribe-banner` (mid-video pop-in). Best for Anthropic / Claude article responses and multi-figure deep dives. | dark-stage, long-form, anthropic, premium, tech, article-response, 3d-reveal |
| long-form-standard.md | Generic long-form (1920x1080) dark-navy stage with 4-accent rotation; canonical baseline for horizontal videos and the parent of future long-form variants | dark-stage, long-form, navy, documentary, baseline |
| openai-mono.md | OpenAI monochrome-editorial aesthetic for vertical Shorts (1080x1920): off-black `#0A0A0A` canvas with single ChatGPT-mint `#10A37F` accent + auxiliary lavender/amber/coral tints + Inter 800 hero + JetBrains Mono eyebrow + 5-dot single-accent progress rail + ChatGPT spirograph (or OpenAI wordmark swap) + sparse monochrome particle field. Optional `theme-light` warm off-white shift surface on the closing phase. | dark-stage, openai, brand, short, monochrome, mint, editorial, calm |
| standard-short.md | Warm paper editorial standard short (1080x1920): cream canvas, 5-accent rotation (terracotta/indigo/sage/sunset-gold/warm-rose), Playfair serif + Inter sans + JetBrains Mono. Sub-composition architecture with 9 scene archetypes. Canonical brand-neutral baseline for vertical Shorts. | warm-paper, short, editorial, baseline, light, sub-compositions |
<!-- LIB:VISUAL-STYLES:END -->
