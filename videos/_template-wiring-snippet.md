# Dynamous Promotion — per-video wiring reference

Canonical reference for adding the Dynamous promotion system to an opted-in Short. Read this top-to-bottom before wiring. Every section is opt-in *within* an opted-in video — pick what fits the Short, skip what doesn't.

> **Strategy doc reference**: every choice below is sourced from `shorts_promotion_strategy.md.resolved` (user-supplied). The verbatim wording in the description / pinned-comment / `script.txt` sections is locked — improvising lands you in "salesy" territory and breaks the Friend Test.

---

## Step 0 — Decide if this Short gets the promotion

At spawn time, the diy-yt-creator skill (and the template README) asks:

> **"Add Dynamous promotion to this Short? (y/N — default no)"**

| Answer | Action                                                                                                                                            |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **N**  | Default. Skip this entire document. Spawn proceeds normally.                                                                                       |
| **Y**  | Continue to Step 1. Record the decision in `videos/<slug>/meta.json` as `"dynamousPromotion": true` for later audit.                                |

A "no" never gets retroactively flipped — existing videos are not touched. Each new video is its own decision.

---

## Step 1 — Persistent badge (every opted-in Short)

Adds the bottom-left Dynamous mark + `dynamous.ai` wordmark, idle at opacity 0.55, fades in once at `t=3.0s`.

1. **Copy the logo asset:**

   ```bash
   cp shared/logos/dynamous-logo.png videos/<slug>/assets/dynamous-logo.png
   ```

2. **Paste the three sections** from `shared/lib/components/dynamous-badge/component.html` into `videos/<slug>/index.html`:
   - HTML `<div id="dynamous-badge">…</div>` near the top of the root `<div>`.
   - The `<style>` block contents into your `<style>`.
   - The `<script>` block contents (the `addDynamousBadgeEntrance` function) into your existing GSAP `<script>`.

3. **Call the entrance from the root timeline:**

   ```js
   addDynamousBadgeEntrance(tl);
   ```

4. **Lint** to verify: `npx hyperframes lint videos/<slug>` — 0 errors expected.

See `shared/lib/components/dynamous-badge/README.md` for the full asset-copy + position rationale.

---

## Step 2 — Endcard (every opted-in Short)

Replaces the trailing **5.0s** of the Short with the canonical Dynamous CTA stack ending in a fade-to-black. The 5s window is sized to match YouTube's end-screen "Watch next" overlay — the Dynamous card sits in the UPPER half of the frame (top: 340px) and YouTube's auto-rendered next-video preview takes the bottom half.

1. **Copy the block:**

   ```bash
   cp shared/lib/blocks/dynamous-endcard/block.html \
      videos/<slug>/compositions/dynamous-endcard.html
   ```

2. **Copy the wordmark asset:**

   ```bash
   cp shared/logos/dynamous-ai-mastery-white.svg \
      videos/<slug>/assets/dynamous-ai-mastery-white.svg
   ```

3. **Compute** `start = totalDuration - 5` from the host timeline.

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

5. **Add the host-side mount CSS** (the sub-composition needs absolute positioning + high z-index so it overlays badge, top banner, phase content, and noise overlay during the last 5s):

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

6. **Fade out competing content 0.5s before the endcard fires** so the handoff is clean:

   ```js
   tl.to("#phase<N>",       { opacity: 0, duration: 0.45, ease: "power2.in", overwrite: "auto" }, totalDuration - 5.5);
   tl.to("#dynamous-badge", { opacity: 0, duration: 0.45, ease: "power2.in", overwrite: "auto" }, totalDuration - 5.5);
   ```

5. **Lint.** The endcard ships brand-locked verbatim — there are no per-video text slots. Headline, CTA pill, 10% OFF badge, URL line are all locked. See `shared/lib/blocks/dynamous-endcard/recipe.md` for details.

---

## Step 3 — Module interstitial (topic-matched Shorts only)

Optional 3.0s mid-video card naming the matching Dynamous AI Mastery module. **Only wire when the topic directly maps to a curriculum module.**

1. **Confirm a match** with the helper:

   ```bash
   node scripts/find-dynamous-module.js "<tag-1>" "<tag-2>" "<tag-3>"
   ```

   If the helper prints `NO_MATCH`, **skip this step entirely**.

2. **Copy the block:**

   ```bash
   cp shared/lib/blocks/dynamous-module-interstitial/block.html \
      videos/<slug>/compositions/dynamous-module-interstitial.html
   ```

3. **Pick a `data-start`** at a clean ≥ 1.0s narration breath. Avoid hero words.

4. **Add the mount `<div>`** with `data-layout-allow-overflow` (the card slides in/out across the right edge):

   ```html
   <div id="dynamous-mod-int-mount"
        data-composition-id="dynamous-module-interstitial"
        data-composition-src="compositions/dynamous-module-interstitial.html"
        data-start="<pause-start>"
        data-duration="3"
        data-track-index="3"
        data-width="1080"
        data-height="1920"
        data-layout-allow-overflow></div>
   ```

5. **Edit** the per-video copy (`videos/<slug>/compositions/dynamous-module-interstitial.html`) to fill in `#dmi-module-num`, `#dmi-module-title`, and (optionally) the `#dmi-dot` accent color from the matching module's `color` field in `dynamous-modules.json`.

6. **Lint + inspect.** See `shared/lib/blocks/dynamous-module-interstitial/recipe.md` for slot details.

---

## Step 4 — Discount bubble (tutorial / over-the-shoulder Shorts only)

Optional 3–4s pill that pops up *while the Dynamous platform is visibly on screen*. Logo + `Dynamous.ai` + red `10% OFF` badge + `in the link ↓`. **No coupon code field** — the discount is automatic via the description link.

1. **Confirm fit.** Wire ONLY if all of these are true:
   - Author opted in at spawn time.
   - The Short is a tutorial / over-the-shoulder format showing a screen recording of `dynamous.ai` (or the Circle community feed).
   - There's a calm scene window of 3.0–4.0s in that recording where the bubble can land.
   - That window starts at `t ≥ 3.0s` (no hook-time firing).

   If any of those is false, skip this step.

2. **Copy the logo asset** (already copied in Step 1 — re-run is a no-op):

   ```bash
   cp shared/logos/dynamous-logo.png videos/<slug>/assets/dynamous-logo.png
   ```

3. **Paste the three sections** from `shared/lib/components/dynamous-discount-bubble/component.html` into `videos/<slug>/index.html`. Replace `__SCENE_START__` and `__DURATION__` with your values.

4. **Call the entrance from the root timeline:**

   ```js
   addDynamousDiscountBubbleEntrance(tl, sceneStart, duration);
   ```

5. **Smoke-test note:** if the bubble's logo would be a second `<img>` pointing at `assets/dynamous-logo.png` (the badge already uses one), the linter raises `duplicate_media_discovery_risk`. Fix by switching the bubble's mark to a CSS `background-image` on `#ddb-mark`:

   ```css
   #ddb-mark {
     width: 32px; height: 32px; display: block;
     background-image: url('assets/dynamous-logo.png');
     background-size: contain;
     background-repeat: no-repeat;
     background-position: center;
   }
   ```

   …and change the HTML element to `<span id="ddb-mark" role="img" aria-label="Dynamous"></span>`. See `videos/_test-dynamous/index.html` for a working example.

6. **Tween-overlap note:** if the entrance uses `tl.from()` and the exit uses `tl.to()` on the same `opacity` property, the linter may emit `overlapping_gsap_tweens`. Fix by using `tl.fromTo({ opacity: 0 }, { opacity: 1, immediateRender: false })` for the entrance and `overwrite: "auto"` on the exit:

   ```js
   tl.fromTo("#dynamous-discount-bubble",
     { y: 16, opacity: 0 },
     { y: 0, opacity: 1, duration: 0.5, ease: "power2.out", immediateRender: false },
     sceneStart);
   tl.to("#dynamous-discount-bubble",
     { opacity: 0, duration: 0.4, ease: "power2.in", overwrite: "auto" },
     sceneStart + duration - 0.4);
   ```

See `shared/lib/components/dynamous-discount-bubble/README.md` for the full slot table and don'ts.

---

## Step 5 — `script.txt` outro line (every opted-in Short)

Append an outro line to the end of `videos/<slug>/script.txt` after your existing outro. The wording depends on **the channel author's relationship to Dynamous**.

### Default (channel author is OUTSIDE the Dynamous team)

Append this line VERBATIM:

> "A lot of you asked how I'm learning all this AI stuff — I use Dynamous. It's an awesome community. I actually reached out to them and got a 10% off code for you guys, it's in the pinned comment."

**Why verbatim?** This wording passes the strategy doc's Friend Test — a friend telling you about a discount they got, not a sales pitch. Improvising loses the frame.

**Note on "code"**: The line uses the word "code" even though the discount is automatic via the link, not a typed code. This is fine — a discounted link IS a "code" in the colloquial sense, and the friend-frame language is what carries the conversion. Don't rewrite it.

### Insider exception (channel author is ON the Dynamous team / works with the founder)

When the channel author is an insider — works on the team, builds projects with the founder, helps run workshops or content — the outsider line is **factually wrong**. Saying "I reached out to them" misrepresents the relationship and burns trust the moment a viewer recognises the author.

Use insider framing instead. The Friend Test still passes — an insider saying "join us" is *more* friend-framed than an outsider saying "I got a code", not less. Required ingredients:

- Acknowledge the team affiliation ("I'm on the Dynamous team" / "I build at Dynamous").
- Optionally name the founder by first name and 1–2 concrete projects you ship together (Archon is the highest-recognition; bolt.diy and local-ai-packaged are also valid).
- End with the same conversion CTA: "10% off code in the pinned comment if you want to join us."

Reference outro that shipped in `videos/claude-code-source-leak/script.txt`:

> "A lot of you asked how I learn this AI stuff. I'm on the Dynamous team. I work with Cole on workshops, his videos, and our open source projects. There's a 10% off code in the pinned comment if you want to join us."

What stays locked across BOTH variants:

- The pinned-comment first line (Step 6) — verbatim factual statement about the link.
- The description first line (Step 7) — same.
- The endcard CTA stack — brand-locked, no per-video text slots.
- Volume / SFX rules — no audio stinger on the outro line.

---

## Step 6 — Pinned comment (every opted-in Short)

**Pin within 5 minutes of upload.** Pinned-comment is the canonical conversion path; on-screen overlays are recall amplifiers, not the conversion mechanism.

First line of the pinned comment, VERBATIM (no `[YOURCODE]` placeholder — the discount is automatic via the link):

> "You can check out Dynamous AI here: https://dynamous.ai/?code=646a60. 10% off applies automatically when you join through this link! 👇"

The link `https://dynamous.ai/?code=646a60` is the canonical channel-wide Dynamous join link with the 10%-off code embedded — applies automatically when viewers click. If Cole rotates the code, update this file plus `shared/lib/components/dynamous-data/dynamous-modules.json` (`joinUrl` field) plus the endcard's `#dec-url` slot. Keep the `👇` — it points the eye to follow-up replies.

---

## Step 7 — Description first line (every opted-in Short)

Same template as the pinned comment:

> "You can check out Dynamous AI here: https://dynamous.ai/?code=646a60. 10% off applies automatically when you join through this link! 👇"

Same link. Same wording. The description first line is what shows above the fold on YouTube; the pinned comment is what shows under the video on mobile. Both need the same hook.

---

## Execution checklist (run before publishing)

Verbatim from strategy doc § 4 — every opted-in Short must pass these five checks before going live.

- [ ] **Value Test.** The video stands on its own — viewers get a useful insight even if they ignore the Dynamous promotion entirely. (If the video is *primarily* a Dynamous pitch, scrap and rebuild.)
- [ ] **Friend Test.** The verbal CTA in `script.txt` sounds like a friend telling you about a discount they got — not a sales pitch. Read it out loud. Cringe → rewrite.
- [ ] **Hook Test.** The first 3 seconds of the video do NOT mention Dynamous, do NOT show the badge, do NOT show any branding. The hook is *purely* the topic. (Verify: `addDynamousBadgeEntrance(tl)` fires at `t=3.0s`, not earlier.)
- [ ] **CTA softness.** The on-screen badge / endcard / discount bubble (where present) are *quiet* visual reminders — no flashing, no aggressive sizing, no audio stinger.
- [ ] **Frictionless purchase.** The pinned comment + description carry the discount link. No code to type. No "DM me for the code." One click from the comment to the discounted signup.

---

## Don'ts (universal — every opted-in Short)

- **Don't start the video with the brand name** or any Dynamous visual. Strategy doc rule: less than 3 seconds to stop the scroll.
- **Don't put a coupon code on screen.** Anywhere. The badge has no code, the endcard has no code, the discount bubble has no code field. The link does the work.
- **Don't add SFX or stinger audio** to any of the four artifacts. Per `audio-design.md` — Shorts are silent on the music track.
- **Don't change the locked CTA text.** "Join the Community", "Link in Description ↓", "10% OFF", "dynamous.ai" — all locked. Channel consistency is the load-bearing benefit.
- **Don't chain the Dynamous endcard with the existing `url-cta` block.** Pick one outro per video.
- **Don't retroactively wire opted-out videos.** A "no" at spawn time is permanent for that video.
