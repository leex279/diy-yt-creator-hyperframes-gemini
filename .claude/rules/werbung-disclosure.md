# Werbung disclosure — mandatory on every on-screen promotion (German law)

Every video shipped from this repo (Short OR long-form, every template, every aesthetic) MUST display a visible **"Werbung"** disclosure badge on every on-screen promotional element. This is a legal requirement under German advertising law — the channel operator is based in Germany and is bound by it for every published video, regardless of where the viewer is.

The rule is content-driven, not format-driven: **if a brand, product, course, community, hosting service, or any commercial partner is shown on screen — for any reason that involves a financial relationship (affiliate, sponsorship, paid placement, revenue share, partnership) — a "Werbung" badge must accompany it.**

---

## Applicable promotions (this list grows over time)

| Promo | Trigger | Badge placement |
|---|---|---|
| **Dynamous AI community** | Any endcard / midroll / module interstitial / discount bubble | Top-right corner of the Dynamous card (inside the card frame, riding with the CTA) |
| **Hostinger** | Banner block / midroll | Top-right corner of the Hostinger banner |
| Any future affiliate / sponsored brand | First on-screen mention per video | Top-right corner of the brand's card / banner |

If a video shows the brand wordmark, logo, URL, discount slug, or any combination thereof as part of a CTA flow → the Werbung badge is mandatory. A passing mention in the script with no on-screen brand element does NOT require it — but **the moment the brand appears visually, the badge MUST appear with it**.

---

## Hard requirements (all four must be satisfied)

1. **Visible from the moment the promo element enters** — the badge must fade in WITH the promo element (or before it), not after. A 0.1–0.4s lead-in is acceptable.
2. **Inside or directly adjacent to the promo element** — the badge rides with the card/banner. NEVER tuck it in a corner of the frame disconnected from the promo.
3. **Legible without zooming** — minimum 18px on Shorts canvas (1080×1920), 24px on long-form (1920×1080). White text on saturated red background. WCAG AA contrast (4.5:1 or better) — `#ffffff` on `#dc2626` satisfies this.
4. **Persistent for the full duration of the promo's on-screen visibility** — if the promo lingers 12s, the badge lingers 12s. Don't fade the badge before the promo exits.

---

## Canonical badge styling

Use this exact treatment on every new video. The studio + render path treats it as a normal `<span>`; nothing framework-specific is required.

```html
<!-- inside the promo card / banner element -->
<span class="dec-werbung"
      style="color:#ffffff; background:#dc2626;">Werbung</span>
```

```css
.dec-werbung {
  position: absolute;
  top: 20px;            /* or top: -16px if the badge should ride the card edge */
  right: 24px;
  background: #dc2626;
  color: #ffffff;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 26px;       /* Shorts; bump to 32px on long-form */
  font-weight: 800;
  padding: 8px 18px;
  border-radius: 8px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  opacity: 0;            /* GSAP fades it in with the card */
  z-index: 10;
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.30);
}
```

```js
// In the scene's GSAP timeline, fade the badge in BEFORE / WITH the card
tl.to('.dec-werbung',
  { opacity: 1, duration: 0.4, ease: "power2.out" },
  0.1);  // 0.1s lead-in is fine; any lag after the card is NOT.
```

The **inline `style="color:#ffffff; background:#dc2626;"` is mandatory** even when the class also sets them. HyperFrames' validator in WCAG-contrast mode may run a static-CSS scan that doesn't resolve scoped sub-composition `<style>` blocks; inline values guarantee the contrast check sees the correct colors.

> **Note on validator timing**: if the badge enters at scene-rel N seconds, the validator may sample mid-fade (opacity ≈ 0) and emit a contrast warning. That is a false positive of the WCAG sampler against animated opacity. If you see only ONE `Werbung` contrast warning and the rendered MP4 shows the badge clearly at the steady-state frame, it is safe to ship. Do not change the badge colors to chase that warning.

---

## Hostinger framing — affiliate, NOT sponsored

Per `feedback_hostinger_affiliate_not_sponsored` (locked 2026-05-12): the Hostinger banner headline is **"Try Hostinger"**, not **"Sponsored by Hostinger"**. The relationship is affiliate (10% off via `/DIYSMARTCODE` slug). The Werbung badge MUST still appear — German law treats affiliate links as Werbung — but the verbal framing in script and description stays affiliate-only.

---

## What does NOT need a Werbung badge

- **Anthropic / Claude / OpenAI / Google / Vercel** etc. when the video is purely *about* the product (covering a release, debate, news) and the channel earns nothing from the mention. Editorial coverage is NOT advertising.
- **Tool of the week / link in description** when the link is a plain URL with no affiliate slug, no commission, no sponsorship deal, and the channel earns zero from clicks. This is reference, not promotion.
- **Open-source projects** the channel uses but isn't commercially tied to.

The line is the **money relationship**. Editorial coverage = no Werbung. Anything where the channel makes money if the viewer clicks/joins/buys = Werbung mandatory.

---

## Self-check before declaring a video done

For every video:

1. Scrub through the MP4 (or studio preview) and identify every frame where a brand wordmark / URL / discount code is visible.
2. For each such frame: is the Werbung badge ALSO visible at that frame?
3. If any frame fails the check → either add the badge OR remove the brand element. No exceptions.

Phase YT (description) AND the final composition build BOTH need to pass this check.

---

## Why

German UWG (Gesetz gegen den unlauteren Wettbewerb) §5a Abs. 4 and §6 require unambiguous identification of commercial content. The Rundfunkstaatsvertrag (RStV) §58 and §7 Abs. 7 reinforce this for broadcast-equivalent platforms (YouTube qualifies). The relevant case law (LG Heilbronn 21 O 54/17 KfH; LG München 31 O 18002/22) confirms that affiliate links and influencer endorsements require visible disclosure. Failure → cease-and-desist letters, fines, and platform-level enforcement action.

For our purposes the practical rule is simpler: **if money flows back to the channel when a viewer engages with the on-screen brand, the badge must be there.**

---

## When to update this rule

When a new promotional partner is added to the channel's catalog, add a row to the "Applicable promotions" table above with the placement convention for that brand's card. When a new on-screen artifact for an existing partner is added (a new badge style, a new banner layout), update the canonical badge styling section if the geometry changes.

This rule grows with the channel's promotional inventory. Never shrink it.
