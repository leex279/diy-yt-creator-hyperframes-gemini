---
name: new-hostinger-sponsored
description: Spawn a new Hostinger sponsorship tutorial video (53.5s, 1920×1080) from the templates/long-form/hostinger-sponsored/ template. Follows Hostinger's brief cadence (hook → brand → plans → cart + coupon → setup → workflow → CTA). Single-file composition, 14 inline scenes, one cinematic-zoom shader at the climax. Use for any Hostinger creator deal (OpenClaw, Coolify, Plesk add-ons, etc.).
---

# new-hostinger-sponsored — Spawn a Hostinger sponsorship video

Hostinger sponsorships ship with a tight brief: 5 sections (Hook → Display purchase flow + coupon → Showcase install/deploy → Selling points → Strong closing CTA) and 1 mandatory disclosure (tracking link + coupon at top of description, `#sponsored` tag). This playbook spawns a 53.5s composition that maps 1:1 to that brief.

## Inputs the user must provide

1. **Product name** (e.g. `OpenClaw`, `Coolify`) — the SaaS / OSS app Hostinger is packaging.
2. **Affiliate / tracking URL** (e.g. `hostinger.com/openclaw`) — assigned by the Hostinger sponsorship contact.
3. **Coupon code** (e.g. `OPENCLAW20`) — assigned by the Hostinger sponsorship contact.
4. **Plan prices** — Managed (`$5.99`/mo etc.) and VPS (`$8.99`/mo etc.).
5. **Discount %** for the badge (e.g. `−20% OFF`).
6. **Cart math** — subtotal, discount amount, total (must be consistent with the discount %).
7. **Hero stat** (default: `24/7`) — what the closing emphasis should be. Generic enough to keep as-is for most deals.
8. **(Optional) Real screen recordings** to swap the mockup scenes (s5 browser, s8 cart, s9 setup, s10 form, s12 phone chat) — see "Replace mockups" below.

If any are missing, **ask** before drafting. Per the sponsorship policy: tracking link + coupon are MANDATORY.

## Output

`videos/<slug>/` containing:

```
videos/<slug>/
├── index.html             ← 14-scene tutorial composition (53.5s)
├── DESIGN.md              ← color/type/motion spec (locked)
├── README.md              ← spawn-doc adapted from template's README
├── preview.html           ← optional standalone preview wrapper
├── meta.json              ← { id: "<slug>", name: "<title>" }
├── hyperframes.json
├── sfx-cues.txt
├── assets/                ← screenshots, sfx, clips (operator drop-in)
├── audio/                 ← narration + bg-music (operator drop-in)
└── out/                   ← rendered MP4 (gitignored)
```

After this playbook completes, the user can:
- `npx hyperframes preview videos/<slug>` — open the studio
- `npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4` — render to MP4

## 12-step workflow

### 1. Pick the slug

Kebab-case. Format: `hostinger-<product>` (e.g. `hostinger-openclaw`, `hostinger-coolify`). Keep it short — it's the directory name AND `meta.json.id`.

### 2. Copy the template

```bash
cp -r templates/long-form/hostinger-sponsored videos/<slug>
```

PowerShell:

```powershell
Copy-Item -Recurse templates/long-form/hostinger-sponsored videos/<slug>
```

### 3. Update `meta.json`

Replace `REPLACE_WITH_VIDEO_SLUG` and `REPLACE_WITH_VIDEO_NAME`:

```json
{
  "id": "<slug>",
  "name": "<final YouTube title — e.g. 'Run Your Own AI Agent 24/7 for $6/mo — Hostinger OpenClaw Setup 2026'>"
}
```

### 4. Find/replace product-specific tokens in `index.html`

| Token | Pattern | Occurrences |
|---|---|---|
| Product name | `OpenClaw` | 10+ (s1 kicker, s2 product, s5 CTA, s6 plan names, s8 cart, s9 step copy, s12 chat speaker, s14 button) |
| Affiliate URL | `hostinger.com/openclaw` | 2 (s5 browser bar, s14 link) |
| Coupon code | `OPENCLAW20` | 3 (s8 cart pill + label, s14 stamp) |
| Managed price | `$5.99` | s6 plan card |
| VPS price | `$8.99` | s6 plan card |
| Cart subtotal | `$143.76` | s8 visual + JS `s8t.v = 143.76` initial value |
| Discount amount | `−$28.75` / `28.75` | s8 visual + JS `s8d.v` counter target |
| Cart total | `$115.01` | s8 visual + JS `s8t.v` counter target |
| Discount badge | `−20% OFF` / `−20%` | s14 stamp |

**Recompute cart math** if the discount % changes — subtotal × (1 − pct/100) = total, discount = subtotal − total. The JS counters expect consistent values; mismatched math is the most common visual bug.

Hero stat (`24/7` in s13) is intentionally generic — only swap if the sponsorship angle calls for a different framing (e.g. `60s` for a deploy-speed-driven cut).

### 5. Tighten the script

The script is encoded directly in the HTML (no separate `script.txt` for this template). Open `index.html` and tighten the copy per scene:

- **s1 Hook** — replace `"Your AI. Your rules."` if the angle is sharper (e.g. `"AI agents that never sleep."` for OpenClaw).
- **s2 Brand lockup** — usually stays `Hostinger × <Product>`.
- **s3 Why automate** — 3 benefit pillars; keep generic unless the product changes the answer.
- **s4 Why Hostinger** — 4 feature pills (1-click, AI credits, scraping, sovereign) — generic, keep.
- **s9 Setup steps** — 4 numbered cards. Tighten the step copy if the actual product flow differs from the OpenClaw flow.
- **s12 Workflow demo** — chat messages MUST reflect a real product use case. Replace placeholder bubbles with the actual workflow you'd showcase.
- **s14 CTA** — `Deploy <Product> →` + `<affiliate URL>` + `<coupon>` + `−<pct>% OFF` stamp.

### 6. (Optional) Replace mockups with real screen recordings

The mockup scenes that fake product UIs can be swapped for real captures:

| Scene | Mockup | Recording target |
|---|---|---|
| s5 | Browser frame on `hostinger.com/<product>` | Actual landing-page scroll |
| s8 | Cart with coupon applied | Real checkout with the live coupon |
| s9 | 4-step dashboard | Hostinger hPanel deploy flow |
| s10 | AI provider form | nexos.ai credit selector or external-key entry |
| s12 | Phone chat | Live Telegram/WhatsApp exchange with the deployed agent |

For each, drop the recording at `videos/<slug>/assets/clips/<scene>.mp4` and replace the mockup `<div>` block with:

```html
<video class="clip" data-start="<sceneStart>" data-duration="<sceneDur>"
       data-track-index="0" src="assets/clips/<scene>.mp4"
       muted playsinline style="width:100%; height:100%; object-fit:cover;"></video>
```

Keep the kicker + lower-third overlays around the `<video>` so the scene's structural context still reads.

### 7. (Optional) Add narration

The template ships without narration — the 53.5s pacing is built for fast-cut sponsored ads where the on-screen copy carries the message. If the deal calls for a voiceover:

```bash
npx hyperframes tts videos/<slug>
# Then wire one <audio> element inside #root at data-track-index="2", data-volume="1"
```

Without narration, the SFX cues in `sfx-cues.txt` (`cinematic-zoom`, `spring-pop`, `scale-slam`) carry the audio interest. Sync via:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

Then add `<audio>` elements at the appropriate `data-start` times per `.claude/rules/audio-design.md`.

### 8. Validate

```bash
npx hyperframes lint videos/<slug>      # must pass 0 errors; 3 stylistic warnings expected
npx hyperframes validate videos/<slug>  # WCAG contrast check
npx hyperframes inspect videos/<slug>   # layout overflow check
```

Expected lint warnings on the bare template (also present after operator edits):

- `composition_file_too_large` on `index.html` (~929 lines — single-file design)
- `timeline_track_too_dense` on track 0 (14 timed scenes)
- `overlapping_gsap_tweens` on `#s5-browser` between 13.65s and 14.35s (scale + transformOrigin)

If any new errors or warnings appear, fix before declaring done.

### 9. Preview

```bash
npx hyperframes preview videos/<slug>
```

Studio opens at `http://localhost:<port>`. Scrub every scene, verify:

- All swap tokens are replaced (no stray `OpenClaw` / `OPENCLAW20` / `hostinger.com/openclaw` if you spawned for a different product).
- Cart math in s8 lands at the right total via the JS counters.
- Shader transition at s7→s8 (25.25s) fires cleanly.
- Hero stat in s13 reads correctly.
- s14 CTA shows the right `affiliate URL` + `coupon` + `−<pct>% OFF`.

### 10. (Optional) QA pass with `qa-composition`

For a structured QA snapshot of every scene:

```
/diy-yt-creator:qa-composition videos/<slug>
```

This drives `agent-browser` against the live preview, snapshots each scene, and flags layout / contrast / overflow issues.

### 11. Draft YouTube description

Per the brief, the description MUST contain (at top of fold):

1. Affiliate / tracking link
2. Coupon code
3. Short CTA sentence
4. `#sponsored` tag

Create `videos/<slug>/youtube-description.md`:

```markdown
Run your own AI agent on Hostinger — 1-click deploy, $X/month, no Docker.

🤖 Get Hostinger <Product> here:
👉 <AFFILIATE_URL>
Use code <COUPON_CODE> for an exclusive discount!

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Chapters
0:00 Hook
0:03 Why <Product>
…

🔗 Links & Resources
- Hostinger <Product>: <AFFILIATE_URL>
- <Product> docs: <docs URL>

---
This video is sponsored by Hostinger. All opinions are my own.
Disclosure: Links above may be affiliate links.

#hostinger #<product> #aiagent #1clickdeploy #sponsored #diysmartcode
```

### 12. Hand off

End with:

```
✓ videos/<slug>/ ready.
  npx hyperframes preview videos/<slug>
  npx hyperframes render  videos/<slug> -o videos/<slug>/out/<slug>.mp4
```

Do NOT auto-render. The user triggers render manually.

## Quality bar checklist

- [ ] All product-specific tokens replaced (no `OpenClaw` / `OPENCLAW20` / `hostinger.com/openclaw` left over unless you spawned for OpenClaw)
- [ ] Cart math math-checks (subtotal × (1 − pct/100) ≈ total; discount = subtotal − total)
- [ ] Lint passes with the expected 3 stylistic warnings (no new errors or warnings)
- [ ] Inspect passes (no new overflow warnings)
- [ ] s14 CTA shows the affiliate link + coupon + discount % all on one frame
- [ ] s2 brand lockup says `Hostinger × <Product>` (not `<Product> × Hostinger`)
- [ ] `youtube-description.md` exists and has tracking link + coupon at top of fold
- [ ] s8 cart-counter math hits the displayed total at the end of its tween

## Don'ts

- **Don't change scene timing** unless the script genuinely runs longer. The 53.5s pacing is brief-aligned and ad-budget-aligned — each second is purchased screen time.
- **Don't add more shader transitions.** The template uses **one** at the climax by design (s7→s8). More than that turns the ad into a music-video and obscures the message. If you want to layer in more, see `templates/long-form/hostinger-sponsored/README.md` § "Adding more shader transitions" — but only do it for a deliberate creative beat, not as a default.
- **Don't drop the Dynamous CTA mid-roll into this template.** The 53.5s budget is too tight for a 31.5s midroll. If the user wants Dynamous integration, run a separate long-form using `templates/long-form/standard/` instead and add the `dynamous-midroll` block there.
- **Don't introduce a competing accent.** Hostinger purple `#673DE6` is the brand surface. The success-green `#00C896` is allowed for "applied coupon" and "live" indicators only. No other accent.
- **Don't render without verifying the cart math.** Mismatched subtotal/discount/total is the most common visual bug — it counter-animates to the wrong number and the viewer notices instantly.
- **Don't forget the `#sponsored` disclosure** in the YouTube description — failing this violates Hostinger's sponsorship policy AND YouTube's affiliate disclosure rules.
