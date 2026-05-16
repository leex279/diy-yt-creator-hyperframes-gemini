# Hostinger × Sponsored — Tutorial Template (53.5s, 1920×1080)

A horizontal HyperFrames tutorial template designed around the **Hostinger sponsorship brief format** — hook → brand intro → feature pillars → landing page → plan comparison → pricing/term → cart + coupon → setup steps → AI provider → channel selection → workflow demo → feature spotlight → CTA. Single-file composition (no sub-compositions); 14 inline scenes; one shader transition at the climax.

Best fit: **Hostinger-branded creator deals** for products like OpenClaw, Coolify, Plesk add-ons, or anything Hostinger packages as a 1-click deploy. Reuses the brief's structure 1:1, so you can fill in the swap points without restructuring the script.

> **Not a long-form (~14min) tutorial.** This template is the **sponsored-ad cadence** Hostinger asks for — tight, every-second-counts, brief-aligned. For deeper teach-throughs, see `templates/long-form/standard/`.

| | |
|---|---|
| Canvas | 1920×1080 |
| Duration | 53.5s |
| Scenes | 14 inline (`#s1`…`#s14`) |
| Architecture | Single-file (no sub-compositions) |
| Shader transitions | 1 (`cinematic-zoom` at s7→s8) |
| Brand color | Hostinger purple `#673DE6` |
| Typography | Manrope (display) + JetBrains Mono (data) |

## Spawn a new video from this template

```bash
# Copy
cp -r templates/long-form/hostinger-sponsored videos/<slug>

# PowerShell
Copy-Item -Recurse templates/long-form/hostinger-sponsored videos/<slug>
```

Then edit `videos/<slug>/meta.json`:

```json
{
  "id": "<slug>",
  "name": "<Final video title — used in the studio file tree>"
}
```

## Swap points — find and replace before rendering

Open `videos/<slug>/index.html` and replace these tokens. They're the **only** values that change per sponsorship deal — everything else is template chrome.

| What | Current value | Lives in scene |
|---|---|---|
| Product name | `OpenClaw` (10+ occurrences) | s1 kicker, s2 product lockup, s5 CTA, s6 plan names, s8 cart line, s9 step copy, s12 chat speaker, s14 button |
| Affiliate URL | `hostinger.com/openclaw` | s5 browser bar, s14 link |
| Coupon code | `OPENCLAW20` | s8 cart pill, s14 coupon stamp |
| Managed price | `$5.99` | s6 plan card |
| VPS price | `$8.99` | s6 plan card |
| Cart subtotal | `$143.76` | s8 cart line, JS counter `s8t.v = 143.76` |
| Discount amount | `−$28.75` | s8 cart line, JS counter `s8d.v = 28.75` |
| Cart total | `$115.01` | s8 cart line, JS counter `s8t.v: 115.01` |
| Discount badge | `−20% OFF` | s14 stamp |
| Hero stat | `24/7` | s13 — generic, swap only if the angle changes |
| Workflow demo copy | Chat messages in s12 | Replace with the use-case you want to showcase |

**Recompute cart math:** if the discount % changes, update `subtotal`, `discount`, and `total` together — the JS counter math expects them to be consistent.

## Replace mockups with real screen recordings (optional)

The scenes that mock product UIs (s5 browser frame, s8 cart, s9 dashboard, s10 form, s12 phone chat) can be swapped for real screen captures:

1. Record the actual product flow → save to `videos/<slug>/assets/clips/<slot>.mp4`
2. In `index.html`, replace the mockup `<div>` with:
   ```html
   <video class="clip" data-start="<sceneStart>" data-duration="<sceneDur>"
          data-track-index="0" src="assets/clips/<slot>.mp4"
          muted playsinline style="width:100%; height:100%; object-fit:cover;"></video>
   ```
3. Add a lower-third with the scene's kicker + title overlay if the recording doesn't already show context.

## Preview, lint, render

```bash
# Lint
npx hyperframes lint videos/<slug>

# Preview in studio
npx hyperframes preview videos/<slug>

# Render to MP4 (default 1920×1080, 30fps)
npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4
```

## Scene map

| # | Scene | Start | Duration | Purpose |
|---|---|---|---|---|
| 1 | Hook | 0 | 3.0s | "Your AI. Your rules." — character-staggered headline |
| 2 | Brand lockup | 3.0s | 2.5s | Hostinger × {product} |
| 3 | Why automate | 5.5s | 4.0s | 3 numbered benefits of automation |
| 4 | Why Hostinger | 9.5s | 4.0s | 4 feature pills (1-click, AI credits, scraping, sovereign) |
| 5 | Landing page mock | 13.5s | 3.5s | Browser frame on `{affiliate URL}` with cursor + CTA |
| 6 | Plan comparison | 17.0s | 5.0s | Managed (`$5.99`) vs VPS (`$8.99`) side-by-side cards |
| 7 | Pricing / term | 22.0s | 3.5s | 1/12/24 mo toggle with SAVE 60% badge, animated price drop |
| 8 | Cart + coupon | 25.5s | 4.0s | Mock checkout with `{coupon}` applied, animated total |
| 9 | Setup steps | 29.5s | 5.0s | 4 numbered cards + progress bar fill |
| 10 | AI provider | 34.5s | 4.0s | Form mockup: Ready-to-use AI vs External API key |
| 11 | Channel select | 38.5s | 3.5s | WhatsApp / Telegram / Slack / Discord grid |
| 12 | Workflow demo | 42.0s | 4.0s | Phone-style chat: user → typing → bot reply with execution |
| 13 | Feature spotlight | 46.0s | 3.5s | Big "24/7" stat with breathing animation |
| 14 | CTA | 49.5s | 4.0s | `{affiliate URL}` + `{coupon}` + Deploy button |

Shader transition: **s7 → s8** at 25.25s, `cinematic-zoom` 0.5s — the moment the discount lands.

## Adding more shader transitions

The template ships with **one** shader at the climax (s7→s8). To add more, expand the `HyperShader.init` block at the bottom of `index.html`:

```js
window.HyperShader.init({
  bgColor: getComputedStyle(document.documentElement).getPropertyValue("--bg").trim() || "#0e0f19",
  scenes: ["s5", "s6", "s7", "s8"],  // make a consecutive anchor block
  timeline: tl,
  transitions: [
    { time: 16.75, shader: "whip-pan", duration: 0.5 },        // s5→s6
    { time: 21.75, shader: "light-leak", duration: 0.5 },      // s6→s7
    { time: 25.25, shader: "cinematic-zoom", duration: 0.5 },  // s7→s8 (existing)
  ],
});
```

Then change those scenes' inline style from `visibility:hidden` to `opacity:0`. See `claude-design-hyperframes.md` § Step 4 (in the uploads from the original template author) for the full rules.

## Design system

See [`DESIGN.md`](DESIGN.md) for the color tokens, typography scale, motion easing rules, and signature visual elements (mono kickers, accent lines, dotted grid, purple glow blobs, grain layer). Stay inside the palette — the Hostinger purple `#673DE6` does the heavy lifting; don't introduce a competing accent.

## Quality gates (the bare template MUST pass these before declaring it shipped)

```bash
npx hyperframes lint     templates/long-form/hostinger-sponsored
npx hyperframes validate templates/long-form/hostinger-sponsored
npx hyperframes inspect  templates/long-form/hostinger-sponsored
```

0 errors expected. Warnings are stylistic (`composition_file_too_large`, `timeline_track_too_dense`) and are inherent to a 14-scene single-file template — they don't block rendering. The current snapshot ships with 3 such warnings; if you change the file, run lint again and confirm the count doesn't grow.

```bash
# Spawn dry-run
cp -r templates/long-form/hostinger-sponsored /tmp/test-spawn
sed -i 's/REPLACE_WITH_VIDEO_SLUG/test-spawn/' /tmp/test-spawn/meta.json
sed -i 's/REPLACE_WITH_VIDEO_NAME/Test Spawn/' /tmp/test-spawn/meta.json
npx hyperframes lint /tmp/test-spawn  # must stay at the same warning count
rm -rf /tmp/test-spawn

# Bare draft render
npx hyperframes render templates/long-form/hostinger-sponsored --quality draft -o /tmp/hostinger-sponsored-smoke.mp4
```

## Provenance

This template is the canonical Hostinger sponsorship cadence — drafted in Claude Design from the Hostinger × OpenClaw brief, refined through several render passes, and adopted into the repo as `templates/long-form/hostinger-sponsored/`. The brand surface, motion system, and scene structure are locked; only the swap points change per sponsorship.

See [`DESIGN.md`](DESIGN.md) for the locked design system and `claude-design-hyperframes.md` (in the source uploads) for the authoring playbook the original template was built against.
