# Recipe: dynamous-endcard

Last-5s contextual endcard for opted-in Shorts. Mirrors the midroll v3 Phase 6 CTA stack — mastery wordmark, "Join the Community" headline, **4-item community offerings list** (Agentic Coding Course, AI Second Brain (OpenClaw — you own it), AI Agent Master Course, Daily Events + Friday Workshops), "Link in Description ↓" gradient pill, red "10% OFF" badge, `https://dynamous.ai/?code=646a60` URL line — ending with a 0.5s fade-to-black for a clean cut.

> **OPT-IN.** Do not wire this block unless the author opted in to the Dynamous promotion at spawn time. See `videos/_template-wiring-snippet.md`.

> **5s window is reserved for YouTube's end-screen UI.** YouTube auto-renders a "Watch next" preview card in the bottom ~half of the frame during the last 4–5s of a Short. The Dynamous card is positioned in the UPPER half (top: 340px) so it sits above the YouTube overlay. Don't extend the duration past 5s — and don't move the card lower than top=340 — or the two will overlap.

## What it produces

```
   ┌───────────────────────────────────────────┐
   │       [ Dynamous AI Mastery wordmark ]    │   ← 480px wide, white-on-dark
   │                                           │
   │            Join the Community             │   ← 56px / 900 weight
   │                                           │
   │   ✓ Agentic Coding Course                 │   ← 4 community offerings,
   │   ✓ AI Second Brain (OpenClaw …)          │     30px / 700 weight,
   │   ✓ AI Agent Master Course                │     gradient check badge
   │   ✓ Daily Events + Friday Workshops       │     per item
   │                                           │
   │       ┌─────────────────────────────┐     │
   │       │  Link in Description    ↓   │     │   ← purple → pink → purple
   │       └─────────────────────────────┘     │     gradient pill, 32px
   │                                           │
   │            ┌──────────┐                   │
   │            │ 10% OFF  │                   │   ← red gradient badge
   │            └──────────┘                   │
   │                                           │
   │                dynamous.ai                │   ← muted slate, 26px
   │                                           │
   │  [ glass card on slate-900 surface ]      │
   └───────────────────────────────────────────┘
                       ↓
              fade-to-black at 4.5–5.0s
```

Three-phase animation:

1. **Card scale-in** (0–0.4s) — glass card pops from `scale 0.9 / opacity 0` with `back.out(1.2)` easing.
2. **Content stagger** (0.4–1.85s) — wordmark → headline → 4 offerings (each 0.08s after the previous) → CTA button → 10% OFF badge → URL, each with eased entry. Subtle gradient shimmer plays across the CTA button during the hold.
3. **Fade-to-black** (4.5–5.0s) — full-frame black overlay fades in for the clean cut at composition end.

## Required tokens

None. The block inlines all colors (midroll v3 palette) and the `Inter` font. Optional override: set `--bg` on the host to change the dark surface, but the locked default `#0f172a` is the intended brand surface.

## Wire into a host composition

1. **Copy the block** into the video's `compositions/` folder:

   ```bash
   cp shared/lib/blocks/dynamous-endcard/block.html \
      videos/<slug>/compositions/dynamous-endcard.html
   ```

2. **Copy the wordmark asset** (HyperFrames bundler rejects parent-of-project paths):

   ```bash
   cp shared/logos/dynamous-ai-mastery-white.svg \
      videos/<slug>/assets/dynamous-ai-mastery-white.svg
   # PowerShell: Copy-Item shared/logos/dynamous-ai-mastery-white.svg videos/<slug>/assets/dynamous-ai-mastery-white.svg
   ```

3. **Compute the start time** from the host video's total duration:

   ```
   start = totalDuration - 5
   ```

   (Round to one decimal — e.g. for a 77.0s video, start = 72.0; for a 12.0s video, start = 7.0.)

4. **Add the mount `<div>`** to `videos/<slug>/index.html`:

   ```html
   <div id="dynamous-endcard-mount"
        data-composition-id="dynamous-endcard"
        data-composition-src="compositions/dynamous-endcard.html"
        data-start="<start>"
        data-duration="5"
        data-track-index="10"
        data-width="1080"
        data-height="1920"></div>
   ```

   Pick a `data-track-index` that doesn't collide with the narration `<audio>` (track 2) or any SFX (tracks 3+). Track 10 is the recommended default.

5. **Add the host-side mount CSS** to `videos/<slug>/index.html`'s `<style>` block — the sub-composition needs absolute positioning + a high z-index so it overlays everything else (badge, top banner, phase content, noise overlay) during the last 5s:

   ```css
   #dynamous-endcard-mount {
     position: absolute;
     inset: 0;
     width: 1080px;
     height: 1920px;
     z-index: 100;
     pointer-events: none;
   }
   ```

6. **Fade out competing content during the endcard window.** The 5s before the host's total duration is when the endcard takes over. Add fade-outs for any phase content or persistent overlays that would still be on screen:

   ```js
   // Half a second before the endcard fires, fade out the trailing phase
   // and the persistent badge so the endcard owns the frame cleanly.
   tl.to("#phase<N>",       { opacity: 0, duration: 0.45, ease: "power2.in", overwrite: "auto" }, totalDuration - 5.5);
   tl.to("#dynamous-badge", { opacity: 0, duration: 0.45, ease: "power2.in", overwrite: "auto" }, totalDuration - 5.5);
   ```

5. **Lint to verify**:

   ```bash
   npx hyperframes lint videos/<slug>
   ```

## Slots to edit

The endcard ships brand-locked verbatim — there are no per-video slots. Every opted-in Short carries the **same** mastery wordmark, **same** "Join the Community" headline, **same** 4 community offerings, **same** "Link in Description ↓" CTA, **same** "10% OFF" badge, and **same** `dynamous.ai` URL. This is intentional: brand consistency across the channel is the load-bearing benefit.

If you genuinely need to vary the headline (e.g. for a special-occasion Short), edit `#dec-headline` directly in the per-video copy of `compositions/dynamous-endcard.html`. Do NOT touch the `.dec-offerings`, `.dec-discount` (`10% OFF`), or `.dec-button` (`Link in Description`) text — these are part of the locked CTA stack.

| Selector         | Purpose                                | Constraint                                         |
| ---------------- | -------------------------------------- | -------------------------------------------------- |
| `#dec-headline`  | Hero CTA headline                      | Default `Join the Community`. Keep ≤ 24 chars.     |
| `#dec-offerings` | 4-item community offerings list        | DO NOT EDIT. Locked at the 4 community offerings (Agentic Coding Course, AI Second Brain, AI Agent Master Course, Daily Events + Friday Workshops). |
| `#dec-button`    | Gradient action pill                   | DO NOT EDIT. Locked at `Link in Description ↓`.    |
| `#dec-discount`  | Red discount badge                     | DO NOT EDIT. Locked at `10% OFF`.                  |
| `#dec-url`       | Trailing full discount URL             | Locked default `https://dynamous.ai/?code=646a60`. Update only if Cole rotates the discount code (then update `dynamous-modules.json` `joinUrl` and re-sync per-video copies). |

## Don'ts

- **Don't put a coupon code on screen.** The 10% applies automatically when viewers click through the description link — the `10% OFF` badge is the visual reminder, the link is the actual mechanism. Adding a code field on the endcard would confuse viewers (no code to enter — just click the link).
- **Don't extend `data-duration` past 5.0s.** The fade-to-black is timed to land at exactly 5.0s; longer durations leave the black frame held, which disrupts the YouTube next-video autoplay handoff.
- **Don't shorten `data-duration` below 5.0s.** YouTube's end-screen overlay reserves the last 4–5s — going shorter means the Dynamous card cuts away while YouTube's UI is still showing, leaving viewers with just the YouTube card.
- **Don't lower the card's `top` below 340px or remove `transform: translateX(-50%)`.** The card is intentionally positioned in the upper half of the frame so it doesn't overlap with YouTube's "Watch next" preview that auto-renders in the bottom half during the end-screen window.
- **Don't change the fade-to-black timing.** The final 0.5s blackout is required for the clean cut — without it, the host video's last frame flashes back to the phase content for one frame at the boundary.
- **Don't reference the wordmark via `../../shared/logos/...`.** The bundler rejects parent-of-project paths. Always copy into `videos/<slug>/assets/` first; the block already uses `../assets/dynamous-ai-mastery-white.svg` (one level up from `compositions/`, i.e. into the host project's `assets/` folder).
- **Don't add SFX or stinger audio.** Per `.claude/rules/audio-design.md` rule "Shorts Have NO Background Music." The Remotion source ships silent — we mirror that.
- **Don't chain the endcard with `url-cta`.** Pick one outro per video. Stacking creates a 6+ second dead zone at the end where viewer drop-off is highest.

## Lint expectations

```bash
npx hyperframes lint videos/<slug>
```

Expect 0 errors after wiring. Inspect should show the card centered with no overflow:

```bash
npx hyperframes inspect videos/<slug>
```
