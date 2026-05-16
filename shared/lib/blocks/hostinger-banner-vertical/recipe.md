# Recipe: hostinger-banner-vertical

7-second mid-video Hostinger sponsorship card for Shorts (1080×1920). Glass card centered in the upper half of the frame — Hostinger wordmark, "Try Hostinger" headline, three stacked product pills (Web Hosting, VPS Hosting, AI Website Builder), green "10% OFF" badge, purple gradient CODE pill (`DIYSMARTCODE`), and `hostinger.com/DIYSMARTCODE` URL line. Carries a "Werbung" badge for German ad-law compliance.

> **OPT-IN.** Do not wire this block unless the author opted in to the Hostinger promotion at spawn time. Each video either has a Hostinger sponsorship slot or it does not; the block lives only in opted-in Shorts.

> **NOT an endcard.** The Dynamous endcard owns the final 5s of every Short (`shared/lib/blocks/dynamous-endcard/`). This block is a **mid-video** banner — wire it during a phase where the narrator mentions the sponsor, NOT in the closing 5s.

## What it produces

```
   ┌───────────────────────────────────────────┐
   │            [ Werbung ]                    │   ← German ad-law badge, top-right
   │     [ Hostinger horizontal wordmark ]     │   ← 540px wide, white-on-glass
   │                                           │
   │         Try Hostinger            │   ← 60px / 800 weight
   │                                           │
   │   ●  Web Hosting                          │   ← stacked product pills,
   │   ●  VPS Hosting                          │     each in its own glass row,
   │   ●  AI Website Builder                   │     accent-tinted dot
   │                                           │
   │            ┌──────────────┐               │
   │            │   10% OFF    │               │   ← green gradient badge,
   │            └──────────────┘               │     subtle shimmer hold
   │                                           │
   │       ┌────────────────────────┐          │
   │       │       USE CODE         │          │   ← purple gradient pill,
   │       │     DIYSMARTCODE       │          │     JetBrains Mono, click-anchor
   │       └────────────────────────┘          │
   │                                           │
   │     hostinger.com/DIYSMARTCODE            │   ← muted slate URL line, mono
   │                                           │
   │  [ glass card, transparent backdrop ]     │
   └───────────────────────────────────────────┘
                       ↓
              scale-out fade at 6.5–7.0s
```

Four-phase animation:

1. **Card scale-in** (0–0.5s) — glass card pops from `scale 0.88 / opacity 0` with `back.out(1.3)` easing; Werbung badge fades in alongside.
2. **Content stagger** (0.40–1.85s) — wordmark → headline → 3 product rows (each 0.10s after the previous) → 10% OFF badge → DIYSMARTCODE code pill → URL line, each with eased entry.
3. **Hold + idle pulses** (2.0–6.5s) — green shimmer sweeps across the 10% OFF badge, accent dots breathe in staggered sympathy, discount badge has a subtle scale yoyo.
4. **Card scale-out** (6.5–7.0s) — glass card scales to 0.92 + fades out, leaving the underlying composition to continue.

## Required tokens

None. The block inlines the Hostinger purple palette + Manrope + JetBrains Mono fonts. Optional override: set `--bg` on the `[data-composition-id="hostinger-banner-vertical"]` selector to give the card a backdrop fill (default is `transparent` so the underlying phase shows through during the entry / exit animation).

## Wire into a host composition

1. **Copy the block** into the video's `compositions/` folder:

   ```bash
   cp shared/lib/blocks/hostinger-banner-vertical/block.html \
      videos/<slug>/compositions/hostinger-banner.html
   ```

   PowerShell:
   ```powershell
   Copy-Item shared/lib/blocks/hostinger-banner-vertical/block.html `
             videos/<slug>/compositions/hostinger-banner.html
   ```

2. **Copy the Hostinger wordmark asset** (HyperFrames bundler rejects parent-of-project paths):

   ```bash
   cp shared/logos/hostinger-brand/Hostinger_Horizontal_White.svg \
      videos/<slug>/assets/hostinger-horizontal-white.svg
   ```

   PowerShell:
   ```powershell
   Copy-Item shared/logos/hostinger-brand/Hostinger_Horizontal_White.svg `
             videos/<slug>/assets/hostinger-horizontal-white.svg
   ```

3. **Pick the start time.** This is a mid-video block — it should land where the narrator names the sponsor. Read the transcript and locate the word `Hostinger` (or `sponsor`, depending on the cold-open phrasing). Use that word's `start` value as the banner's `data-start`.

   ```js
   const transcript = JSON.parse(fs.readFileSync(`videos/${slug}/audio/transcript.json`));
   const hostWord = transcript.words.find(w => w.text.toLowerCase() === 'hostinger');
   const sponsorStart = hostWord.start; // seconds
   ```

   If the script has multiple `Hostinger` mentions, pick the FIRST one (the introduction beat) — subsequent mentions reinforce, the first one anchors the visual.

4. **Add the mount `<div>`** to `videos/<slug>/index.html`:

   ```html
   <div id="hostinger-banner-mount"
        data-composition-id="hostinger-banner-vertical"
        data-composition-src="compositions/hostinger-banner.html"
        data-start="<sponsorStart>"
        data-duration="7"
        data-track-index="9"
        data-width="1080"
        data-height="1920"></div>
   ```

   Pick a `data-track-index` that doesn't collide with narration (track 2) or SFX (tracks 3+). Track 9 is the recommended default for a mid-video sponsor (one below the Dynamous endcard's track 10).

5. **Add the host-side mount CSS** to `videos/<slug>/index.html`'s `<style>` block — the sub-composition needs absolute positioning + a high z-index so it overlays everything else (phase content, badge, noise overlay) during the 7s sponsor beat:

   ```css
   #hostinger-banner-mount {
     position: absolute;
     inset: 0;
     width: 1080px;
     height: 1920px;
     z-index: 90;     /* below endcard (100), above phase content */
     pointer-events: none;
   }
   ```

6. **Fade out competing content during the sponsor window.** The 7s the banner is on screen is a hard takeover — anything underneath fights the banner for attention. Wrap the active phase with an opacity dip:

   ```js
   // Fade the underlying phase down to 30% opacity during the sponsor window
   // so the Hostinger card owns the visual hierarchy. Restore after.
   tl.to("#phase<N>", { opacity: 0.30, duration: 0.45, ease: "power2.in" }, sponsorStart - 0.20);
   tl.to("#phase<N>", { opacity: 1.00, duration: 0.45, ease: "power2.out" }, sponsorStart + 7.00);
   ```

   (If the sponsor beat sits between two distinct phases — i.e. its window is silent on the underlying timeline anyway — skip this step.)

7. **Lint to verify**:

   ```bash
   npx hyperframes lint videos/<slug>
   ```

## Slots to edit

The banner ships brand-locked. Every opted-in Short carries the **same** Hostinger wordmark, **same** 3 product pills, **same** "10% OFF" badge, **same** `DIYSMARTCODE` code, **same** `hostinger.com/DIYSMARTCODE` URL. This is intentional: brand and offer consistency is the load-bearing benefit, and the affiliate URL is a single locked redirect.

If you genuinely need to vary anything (e.g. a special-occasion Hostinger campaign with a different code), edit the per-video copy of `compositions/hostinger-banner.html` directly. Do NOT touch the `Werbung` badge — it is German ad-law compliance.

| Selector         | Purpose                                | Constraint                                              |
| ---------------- | -------------------------------------- | ------------------------------------------------------- |
| `.hbv-headline`  | Sponsorship headline                   | Default `Try Hostinger`. Keep ≤ 26 chars.      |
| `.hbv-products`  | 3-item product list                    | DO NOT EDIT. Locked at Web Hosting / VPS / AI Builder.  |
| `.hbv-discount`  | Green discount badge                   | DO NOT EDIT. Locked at `10% OFF`.                       |
| `.hbv-url-code`  | Coupon code pill                       | DO NOT EDIT. Locked at `DIYSMARTCODE`.                  |
| `.hbv-url`       | URL line                               | DO NOT EDIT. Locked at `hostinger.com/DIYSMARTCODE`.    |
| `.hbv-werbung`   | German ad-disclosure badge             | DO NOT REMOVE.                                          |

## Don'ts

- **Don't wire this into the closing 5s of a Short.** The Dynamous endcard (`shared/lib/blocks/dynamous-endcard/`) is locked to that window. Stacking the two creates a 12s sponsor zone at the end where viewer drop-off is highest — also two `Werbung` badges, which looks broken.
- **Don't extend `data-duration` past 7.0s.** The scale-out is timed to land at exactly 7.0s; longer durations leave the card frozen at scale 0.92, which reads as a paused video.
- **Don't shorten `data-duration` below 6.5s.** The scale-out animation starts at 6.5s — going shorter cuts the exit mid-flight.
- **Don't change the `Werbung` badge text, color, or position.** German ad disclosure law requires the term `Werbung` (Anzeige is also legal but `Werbung` is what the Dynamous endcard uses — we keep the convention consistent across all sponsorship surfaces).
- **Don't reference the wordmark via `../../shared/logos/...`.** The bundler rejects parent-of-project paths. Always copy into `videos/<slug>/assets/` first; the block already uses `../assets/hostinger-horizontal-white.svg` (one level up from `compositions/`, i.e. into the host project's `assets/` folder).
- **Don't add SFX or stinger audio.** Per `.claude/rules/audio-design.md` rule "Shorts Have NO Background Music." A subtle whoosh on banner-in is acceptable IF the host is already using `cinematic-whoosh` for phase transitions — match its `data-volume="0.11"` and `data-duration="1.5"`.
- **Don't change the affiliate URL or code.** `hostinger.com/DIYSMARTCODE` is the locked affiliate redirect; `DIYSMARTCODE` is both the slug AND the 10% off coupon. Changing either breaks attribution.
- **Don't run two sponsor banners in the same video.** If a Short is also running a non-Hostinger sponsor (rare), pick one — stacking sponsors in a 30-60s Short tanks both.

## Lint expectations

```bash
npx hyperframes lint videos/<slug>
```

Expect 0 errors after wiring. Inspect should show the card centered with no overflow:

```bash
npx hyperframes inspect videos/<slug>
```
