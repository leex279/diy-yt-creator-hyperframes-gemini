# Hostinger × OpenClaw — Tutorial Video Template

A HyperFrames video composition designed as a **template** for the OpenClaw deployment tutorial. Covers every element type the brief calls out — hook, brand intro, plan comparison, pricing toggle, cart + coupon, setup steps, AI provider config, channel selection, workflow demo, feature spotlight, and CTA.

Plain HTML + GSAP; rendered to MP4 by the `hyperframes` CLI.

- **Duration**: 53.5s @ 1920×1080
- **Scenes**: 14
- **Shader transitions**: 1 (hero deal reveal at scene 7 → 8)

## Requirements

- **Node.js 22+** — [nodejs.org](https://nodejs.org/)
- **FFmpeg** — `brew install ffmpeg` (macOS) or `sudo apt install ffmpeg` (Debian/Ubuntu) or [ffmpeg.org/download](https://ffmpeg.org/download.html) (Windows)

Verify: `npx hyperframes doctor`

## Preview

```bash
npx hyperframes preview
```

Opens HyperFrames Studio at `http://localhost:3002` with frame-accurate scrubbing.

## Refine with Claude Code

This template was drafted in Claude Design. To polish animations, timing, and pacing:

```bash
npx skills add heygen-com/hyperframes   # install HyperFrames skills (one-time)
npx hyperframes lint                     # verify structure (should pass with zero errors)
npx hyperframes preview                  # open the studio for live feedback
```

Then open in Claude Code and iterate:

- "Tighten scene 9 — the progress bar should fill faster"
- "Add a shader transition between the landing page (s5) and the plan comparison (s6)"
- "Swap the OPENCLAW20 coupon for the real code MYCODE2026 everywhere"
- "Slow scene 13 (the 24/7 stat) by 0.5s for more dwell time"

## Render

```bash
npx hyperframes render index.html -o output.mp4
```

1920×1080 / 30fps by default. Use `--fps 60` or `--resolution 3840x2160` to override.

## Scene map

| #   | Scene             | Start  | Duration | Purpose                                                     |
| --- | ----------------- | ------ | -------- | ----------------------------------------------------------- |
| 1   | Hook              | 0      | 3.0s     | "Your AI. Your rules." — character-staggered headline       |
| 2   | Brand lockup      | 3.0s   | 2.5s     | Hostinger × OpenClaw                                        |
| 3   | Why automate      | 5.5s   | 4.0s     | 3 numbered benefits of automation                           |
| 4   | Why Hostinger     | 9.5s   | 4.0s     | 4 feature pills (1-click, AI credits, scraping, sovereign)  |
| 5   | Landing page mock | 13.5s  | 3.5s     | Browser frame on hostinger.com/openclaw with cursor + CTA   |
| 6   | Plan comparison   | 17.0s  | 5.0s     | Managed ($5.99) vs VPS ($8.99) side-by-side cards           |
| 7   | Pricing / term    | 22.0s  | 3.5s     | 1/12/24 mo toggle with SAVE 60% badge, animated price drop  |
| 8   | Cart + coupon     | 25.5s  | 4.0s     | Mock checkout with OPENCLAW20 applied, animated total       |
| 9   | Setup steps       | 29.5s  | 5.0s     | 4 numbered cards + progress bar fill                        |
| 10  | AI provider       | 34.5s  | 4.0s     | Form mockup: Ready-to-use AI vs External API key            |
| 11  | Channel select    | 38.5s  | 3.5s     | WhatsApp / Telegram / Slack / Discord grid                  |
| 12  | Workflow demo     | 42.0s  | 4.0s     | Phone-style chat: user → typing → bot reply with execution  |
| 13  | Feature spotlight | 46.0s  | 3.5s     | Big "24/7" stat with breathing animation                    |
| 14  | CTA               | 49.5s  | 4.0s     | hostinger.com/openclaw URL + OPENCLAW20 coupon + Deploy btn |

## Placeholders to swap

Open `index.html` and replace these template values with real ones before rendering:

- **Affiliate URL** — `hostinger.com/openclaw` appears in scenes 5 and 14
- **Coupon code** — `OPENCLAW20` appears in scenes 8 and 14
- **Discount %** — `−20% OFF` badge in scene 14, savings in scene 8 cart
- **Plan prices** — `$5.99`, `$8.99` in scenes 6 and 7
- **Cart totals** — `$143.76` → `$115.01` math in scene 8 (recompute if discount changes)
- **Workflow demo copy** — chat messages in scene 12 (replace with your actual use case)

To replace the mockup UIs (browser frame, checkout, phone chat) with real screen recordings, swap the relevant scene `<div>` with a `<video muted playsinline>` element pointing to your captured MP4 — HyperFrames will composite it.

## Adding more shader transitions

The template uses **one** shader at the climax. To add more, expand the `HyperShader.init` block at the bottom of `index.html`:

```js
scenes: ["s5", "s6", "s7", "s8"],  // make consecutive anchor block
transitions: [
  { time: 16.75, shader: "whip-pan", duration: 0.5 },        // s5→s6
  { time: 21.75, shader: "light-leak", duration: 0.5 },       // s6→s7
  { time: 25.25, shader: "cinematic-zoom", duration: 0.5 },   // s7→s8 (existing)
],
```

Then change those scenes' inline style from `visibility:hidden` to `opacity:0`. See `claude-design-hyperframes.md` § Step 4 for the full rules.
