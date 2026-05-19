# Recipe: hostinger-midroll

A 20-second, 5-phase Hostinger affiliate midroll for **long-form (1920×1080)** videos. Drops in at a natural narration pause (typically halfway through the video). **Silent by default** — the host video's narrator speaks over it during the 20s window. Mirrors the visual structure of `shared/lib/blocks/dynamous-midroll/` (phase mutex with crossfades, glass cards, persistent brand + Werbung chrome, global fade-in / fade-out for host handoff).

> **OPT-IN per video.** Only wire this block in videos where you've opted in to the Hostinger affiliate promotion at spawn time. Brand-locked content (see "Slots" below) — every opted-in long-form video carries the identical 3 products, identical code, identical URL.

> **Long-form only.** Built for 1920×1080. The companion Shorts (1080×1920) variant for the same job is [`shared/lib/blocks/hostinger-banner-vertical/`](../hostinger-banner-vertical/recipe.md).

> **Affiliate-only, not sponsored.** The headline is `Try Hostinger`, never `Sponsored by Hostinger`. The **Werbung** badge is mandatory regardless (DE UWG treats affiliate links as commercial advertising). See `feedback_hostinger_affiliate_not_sponsored.md` memory.

## What it produces

```
   ┌──── 1920 × 1080 frame ──────────────────────────────────────┐
   │  [WERBUNG]                              [Hostinger logo]    │
   │                                                             │
   │   (persistent across all phases, bottom-right corner:       │
   │    [ 10% OFF | DIYSMARTCODE ] — green pill + purple pill )  │
   │                                                             │
   │  Phase 1 (0.0–3.0s)  Hostinger intro                        │
   │     TODAY'S PICK                                            │
   │     Try Hostinger    (220px purple gradient)                │
   │     ───────                                                 │
   │     Hosting that just works — 3 products, 1 purple roof.    │
   │                                                             │
   │  Phase 2 (3.0–7.0s)  Web Hosting                            │
   │     PRODUCT 01                                              │
   │     Web Hosting (96px)         ┌─ macOS frame ────────┐     │
   │     Up to 75% off              │ ● ● ● /web-hosting   │     │
   │     ✓ Free domain & migration  │ [web-hosting.png]    │     │
   │     ✓ WordPress or any CMS     │                      │     │
   │     ✓ Fully managed hosting    │                      │     │
   │     ✓ 24/7 customer support    └──────────────────────┘     │
   │                                                             │
   │  Phase 3 (7.0–11.5s)  VPS Hosting                           │
   │     PRODUCT 02 / VPS Hosting / Up to 70% off                │
   │     ✓ AMD EPYC processors                                   │
   │     ✓ NVMe SSD storage                                      │
   │     ✓ Free weekly backups          [vps-hosting.png]        │
   │     ✓ AI Web Terminal                                       │
   │                                                             │
   │  Phase 4 (11.5–16.0s)  AI Website Builder                   │
   │     PRODUCT 03 / AI Website Builder / Online in 60 seconds  │
   │     ✓ Chat with AI or pick a template                       │
   │     ✓ Free domain for one year     [ai-website-builder.png] │
   │     ✓ Up to 75% off                                         │
   │                                                             │
   │  Phase 5 (16.0–18.5s)  CTA                                  │
   │     EXTRA 10% OFF · STACKS WITH THE DEAL                    │
   │     [ CODE  DIYSMARTCODE ]                                  │
   │     [        10% OFF        ]                               │
   │      hostinger.com/DIYSMARTCODE                             │
   │     ↓ Link in description                                   │
   │                                                             │
   │  Outro (18.5–20.0s)  "Back to the video." → fade out        │
   └─────────────────────────────────────────────────────────────┘
                       ↓
              fade-to-transparent at 19.3–20.0s
                       ↓
                host video resumes
```

### Phase boundaries

| Phase | Visual time | Hand-off |
|---|---|---|
| 1 — Intro | 0.0 → 3.0s | white flash + crossfade |
| 2 — Web Hosting | 3.0 → 7.0s | crossfade |
| 3 — VPS Hosting | 7.0 → 11.5s | crossfade |
| 4 — AI Website Builder | 11.5 → 16.0s | white flash + crossfade |
| 5 — CTA | 16.0 → 18.5s | crossfade |
| Outro | 18.5 → 20.0s | full-root opacity fade |

## Required tokens

None. The block inlines the Hostinger palette (deep navy `#0e0f19` / `#15172a` + Hostinger purple `#673de6` / `#8b5cf6` / `#a78bfa` + success green `#00c896` + red `#dc2626` for Werbung) and the **Manrope** + **JetBrains Mono** fonts.

## Wire into a host long-form composition

### 1. Copy the block into the video's `compositions/` folder

```bash
cp shared/lib/blocks/hostinger-midroll/block.html \
   videos/<slug>/compositions/hostinger-midroll.html
```

PowerShell:
```powershell
Copy-Item shared/lib/blocks/hostinger-midroll/block.html `
  videos/<slug>/compositions/hostinger-midroll.html
```

### 2. Copy ALL static assets into the video's `assets/` folder

The bundler rejects parent-of-project paths, so every reference must resolve under `videos/<slug>/`. The block expects these exact paths:

```bash
# Hostinger horizontal white wordmark
cp shared/logos/hostinger-brand/Hostinger_Horizontal_White.svg \
   videos/<slug>/assets/hostinger-horizontal-white.svg

# Product screenshots — captured generically from hostinger.com
mkdir -p videos/<slug>/assets/hostinger-screens
cp shared/screenshots/hostinger/web-hosting.png \
   videos/<slug>/assets/hostinger-screens/web-hosting.png
cp shared/screenshots/hostinger/vps-hosting.png \
   videos/<slug>/assets/hostinger-screens/vps-hosting.png
cp shared/screenshots/hostinger/ai-website-builder.png \
   videos/<slug>/assets/hostinger-screens/ai-website-builder.png
```

PowerShell:
```powershell
Copy-Item shared/logos/hostinger-brand/Hostinger_Horizontal_White.svg `
  videos/<slug>/assets/hostinger-horizontal-white.svg
New-Item -Type Directory -Force videos/<slug>/assets/hostinger-screens | Out-Null
Copy-Item shared/screenshots/hostinger/web-hosting.png `
  videos/<slug>/assets/hostinger-screens/web-hosting.png
Copy-Item shared/screenshots/hostinger/vps-hosting.png `
  videos/<slug>/assets/hostinger-screens/vps-hosting.png
Copy-Item shared/screenshots/hostinger/ai-website-builder.png `
  videos/<slug>/assets/hostinger-screens/ai-website-builder.png
```

### 3. Pick the midroll start time

Place the block at a natural narration pause — typically halfway through the video. The midroll runs for exactly 20s; the host narrator covers it with a sponsor read ("Quick break — I've been running my own stuff on Hostinger…"). `<midrollStart>` is the absolute time (in seconds) where the block enters.

### 4. Add the mount `<div>` to `videos/<slug>/index.html`

```html
<div id="hostinger-midroll-mount"
     data-composition-id="hostinger-midroll"
     data-composition-src="compositions/hostinger-midroll.html"
     data-start="<midrollStart>"
     data-duration="20"
     data-track-index="20"
     data-width="1920"
     data-height="1080"></div>
```

Pick a `data-track-index` that doesn't collide with narration (track 2), bg-music (track 3), or per-cue SFX (tracks 4+). Track 20 is the recommended default for sub-comp mounts (one slot above the Hostinger banner's track 9, distinct from the Dynamous endcard's track 10).

### 5. Add the host-side mount CSS to `videos/<slug>/index.html`'s `<style>` block

The sub-composition needs absolute positioning + a high z-index so it overlays everything during the midroll window:

```css
#hostinger-midroll-mount {
  position: absolute;
  inset: 0;
  width: 1920px;
  height: 1080px;
  z-index: 50;
  pointer-events: none;
}
```

### 6. (Optional) Dip host audio during the midroll window

The midroll is silent — the host narrator covers it. If the host video has continuous bg-music, drop it down to 0.04 across the midroll window:

```html
<!-- Body bg-music split — segment that ends just before the midroll -->
<audio id="bg-music-body-pre"
       src="audio/bg-music-body.mp3"
       data-start="12"
       data-duration="<midrollStart - 12>"
       data-track-index="3"
       data-volume="0.07"></audio>

<!-- Quiet bed during the midroll (optional — pure silence also works) -->
<audio id="bg-music-midroll"
       src="audio/bg-music-body.mp3"
       data-start="<midrollStart>"
       data-duration="20"
       data-track-index="3"
       data-volume="0.04"></audio>

<!-- Body bg-music resumes after the midroll -->
<audio id="bg-music-body-post"
       src="audio/bg-music-body.mp3"
       data-start="<midrollStart + 20>"
       data-duration="..."
       data-track-index="3"
       data-volume="0.07"></audio>
```

Volume caps follow `.claude/rules/audio-design.md`.

### 7. Lint to verify

```bash
npx hyperframes lint videos/<slug>
```

Then preview to confirm visual sync:

```bash
npx hyperframes preview videos/<slug>
```

Scrub to `<midrollStart>` and watch the 20s window — every phase should crossfade cleanly, the white-flash transitions at P1→P2 and P4→P5 should pop without strobing, and the final root fade-out should hand back to the host video by `<midrollStart + 20>`.

## Slots to edit

The midroll ships **brand-locked**. Don't edit per-video:

| Selector | Content | Constraint |
|---|---|---|
| `#hm-intro-hero` | `Try Hostinger` | DO NOT change to "Sponsored by Hostinger" — relationship is affiliate-only, not sponsorship. |
| `#hm-intro-tagline` | Default tagline | Editable per-video if you want a more topical pitch. ≤ 90 chars to fit one line at 38px. |
| `.hm-phase-2 .hm-product-title` | `Web Hosting` | DO NOT EDIT. |
| `.hm-phase-3 .hm-product-title` | `VPS Hosting` | DO NOT EDIT. |
| `.hm-phase-4 .hm-product-title` | `AI Website Builder` | DO NOT EDIT. |
| `.hm-phase-*  .hm-features li`  | Product feature bullets | DO NOT EDIT without confirming the claims are still on the current hostinger.com product page. The features ship verbatim from the screenshots — they're sourced, not invented. |
| `.hm-product-hook` | "Fully managed · Free site migration" / "Full root access · AI-managed" / "Build with AI · No code needed" | DO NOT EDIT. These are EVERGREEN claims (no rotating discount %s) so the midroll ships in any video without re-checking Hostinger's current promo. |
| `.hm-cta-code` | `DIYSMARTCODE` | DO NOT EDIT. Locked affiliate slug. |
| `#hm-cta-url` | `hostinger.com/DIYSMARTCODE` | DO NOT EDIT. Locked affiliate redirect. |
| `.hm-cta-discount` | `10% OFF` | DO NOT EDIT. |
| `.hm-promo-discount` | `10% OFF` | DO NOT EDIT. Persistent bottom-right badge. |
| `.hm-promo-code` | `DIYSMARTCODE` | DO NOT EDIT. Persistent bottom-right badge. |
| `.hm-werbung` | `Werbung` | DO NOT REMOVE. DE ad-disclosure compliance. |

## Don'ts

- **Don't change phase boundaries piecemeal.** The crossfades are tuned so each transition is ~0.3s of overlap. Adjusting one without adjusting the others creates double-image flashes.
- **Don't shorten `data-duration` below 20s.** The final root fade-out starts at `DUR - 0.7` = 19.3s; shortening cuts the handoff mid-fade.
- **Don't extend `data-duration` past 20s.** The composition is silent + the outro lands at 20.0s; extending leaves a static "Back to the video." frame held visibly during what should be the host video resuming.
- **Don't add narration audio to this block.** It's silent by design — the host narrator covers it. If you genuinely need a pre-baked TTS variant (rare), fork the block as `hostinger-midroll-narrated` and wire the audio at the HOST level per `.claude/rules/audio-design.md` (sub-compositions don't host audio).
- **Don't write "Sponsored by Hostinger" anywhere.** The relationship is affiliate-only. Keep the `Try Hostinger` intro headline. The Werbung badge is the legal disclosure — it does NOT need a "Sponsored" headline to be valid.
- **Don't add rotating discount %s to the hook copy or features.** The block ships with evergreen claims so it survives Hostinger's promo rotations (which change every few weeks). The ONLY pricing claim in the entire midroll is the locked `10% OFF` from your own affiliate code — every other number in the block is a stable product feature (cores, "fully managed", etc.). Captured screenshots may show Hostinger's own rotating discount banners — that's fine, viewers parse those as Hostinger's marketing, not your claim.
- **Don't use this block in Shorts (1080×1920).** Its 720+1040px split layout doesn't fit a portrait canvas. Shorts use [`shared/lib/blocks/hostinger-banner-vertical/`](../hostinger-banner-vertical/recipe.md) instead.
- **Don't reference any path with `../../shared/...`.** The bundler rejects parent-of-project paths. Always copy first; the block uses `../assets/...` (one level up from `compositions/`, into `videos/<slug>/assets/`).
- **Don't pair this block with the long-form Hostinger banner** ([`shared/lib/components/hostinger-banner/`](../../components/hostinger-banner/)). Pick ONE Hostinger promo peak per video — the midroll is the deep version, the banner is the light overlay. Stacking creates an awkward double-disclosure with two `Werbung` badges and viewer fatigue.

## Lint expectations

```bash
npx hyperframes lint videos/<slug>
```

Expect 0 errors. Inspect:

```bash
npx hyperframes inspect videos/<slug>
```

The intro hero, product screenshots, and CTA card should all render within the 1920×1080 frame without overflow during their respective phase windows.

## Re-capturing product screenshots

When Hostinger's product hero pages change (new pricing, new layouts), re-capture:

```bash
# Using the agent-browser skill (see C:/Users/Leex279/.npm-global/agent-browser)
agent-browser open https://www.hostinger.com/web-hosting
agent-browser screenshot shared/screenshots/hostinger/web-hosting.png
agent-browser open https://www.hostinger.com/vps-hosting
agent-browser screenshot shared/screenshots/hostinger/vps-hosting.png
agent-browser open https://www.hostinger.com/website-builder
agent-browser screenshot shared/screenshots/hostinger/ai-website-builder.png
agent-browser close --all
```

Then re-copy into every opted-in video's `assets/hostinger-screens/` folder. Lint after to confirm the new PNGs aren't oversized (per `.claude/rules/hyperframes-pitfalls.md` — keep source images ≤ 2× canvas dimensions; the captures are 1264×625, well under the 3840×2160 long-form ceiling).

Also update the in-block product hooks (`hm-product-hook`) to match whatever discount % the new screenshots show.
