# Code templates — per-style closing-phase HTML

Drop-in `#phase-thumb` blocks for each of the 11 styles. Every template:

- Honors `.claude/rules/shorts-thumbnail-frames.md` (5-element baseline)
- Uses `class="clip"` + `data-start` / `data-duration` / `data-track-index` on every timed element (per the framework rule)
- Enters within ≤0.5s, then freezes for ≥1.5s static hold
- Assumes `1080×1920` canvas with the standard `--bg`, `--accent`, `--fg`, `--fg-dim` token system from the template's `tokens/<name>.css`
- Replace `<TOPIC>`, `<OUTCOME>`, `<BRAND-LOGO-PATH>`, `<ANCHOR>` placeholders with real content

Each template is followed by GSAP timeline lines that go inside the existing root timeline. The phase enters via the standard whoosh + shape-rearrange transition (template-specific, see your video's existing transitions).

> **Tip.** Copy the template, paste it AFTER the CTA / outro phase in `videos/<slug>/index.html`, replace placeholders, then run `npx hyperframes lint videos/<slug>` and verify in `npx hyperframes preview`.

---

## #1 — Neo-minimalism

```html
<!-- Phase: thumbnail hold (neo-minimalism) — last 2.0s of the Short -->
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#fff;">

  <!-- Brand chrome (top-left, tiny) -->
  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; top:60px; left:60px; height:48px; opacity:0.9;">

  <!-- Single subject — version chip / icon / wordmark — center -->
  <div id="thumb-subject" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
              font-size:200px; font-weight:900; line-height:0.9;
              letter-spacing:-0.04em; color:#000;">
    <ANCHOR>
  </div>

  <!-- Topic statement — small, below subject -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:1380px; left:60px; right:60px;
              font-size:56px; font-weight:600; color:#000;
              text-align:center;">
    <TOPIC>
  </div>

  <!-- Outcome receipt — tiny, bottom -->
  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:120px; left:60px; right:60px;
              font-size:38px; font-weight:500; color:#666; text-align:center;">
    <OUTCOME>
  </div>
</div>
```

**GSAP entrance (paste into root timeline):**

```js
const PT = 28.0; // phase-thumb start
tl.set("#thumb-subject", { scale: 0.92, opacity: 0 }, PT);
tl.set("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 16, opacity: 0 }, PT);
tl.to("#thumb-subject", { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.4)" }, PT);
tl.to("#thumb-brand", { y: 0, opacity: 0.9, duration: 0.3 }, PT);
tl.to("#thumb-topic", { y: 0, opacity: 1, duration: 0.35 }, PT + 0.1);
tl.to("#thumb-outcome", { y: 0, opacity: 1, duration: 0.35 }, PT + 0.2);
// hold from PT+0.5 to PT+2.0 — no further tweens
```

---

## #2 — Surround

```html
<!-- Phase: thumbnail hold (surround) -->
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:var(--bg);">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; top:60px; left:60px; height:48px;">

  <!-- Topic strip on top -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:200px; left:60px; right:60px;
              font-size:88px; font-weight:900; color:var(--fg);
              text-align:center; letter-spacing:-0.02em;">
    <TOPIC>
  </div>

  <!-- Center hero -->
  <div id="thumb-center" class="clip"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
              width:360px; height:360px; border-radius:50%;
              background:var(--accent); display:flex; align-items:center;
              justify-content:center; font-size:160px; font-weight:900; color:#000;">
    <ANCHOR>
  </div>

  <!-- 6 orbiting items around the center (replace each with real product/icon) -->
  <div class="orbit-item clip" id="thumb-o1" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:32%; left:18%; width:140px; height:140px;
              background:#222; border-radius:24px; display:flex; align-items:center;
              justify-content:center; font-size:32px; font-weight:700; color:#fff;">A</div>
  <div class="orbit-item clip" id="thumb-o2" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:32%; right:18%; width:140px; height:140px;
              background:#222; border-radius:24px; display:flex; align-items:center;
              justify-content:center; font-size:32px; font-weight:700; color:#fff;">B</div>
  <div class="orbit-item clip" id="thumb-o3" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:50%; left:8%; transform:translateY(-50%); width:140px; height:140px;
              background:#222; border-radius:24px; display:flex; align-items:center;
              justify-content:center; font-size:32px; font-weight:700; color:#fff;">C</div>
  <div class="orbit-item clip" id="thumb-o4" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:50%; right:8%; transform:translateY(-50%); width:140px; height:140px;
              background:#222; border-radius:24px; display:flex; align-items:center;
              justify-content:center; font-size:32px; font-weight:700; color:#fff;">D</div>
  <div class="orbit-item clip" id="thumb-o5" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:32%; left:18%; width:140px; height:140px;
              background:#222; border-radius:24px; display:flex; align-items:center;
              justify-content:center; font-size:32px; font-weight:700; color:#fff;">E</div>
  <div class="orbit-item clip" id="thumb-o6" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:32%; right:18%; width:140px; height:140px;
              background:#222; border-radius:24px; display:flex; align-items:center;
              justify-content:center; font-size:32px; font-weight:700; color:#fff;">F</div>

  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:120px; left:60px; right:60px;
              font-size:48px; font-weight:600; color:var(--fg-dim); text-align:center;">
    <OUTCOME>
  </div>
</div>
```

**GSAP entrance:**

```js
const PT = 28.0;
tl.set("#thumb-center", { scale: 0.7, opacity: 0 }, PT);
tl.set(".orbit-item", { scale: 0.6, opacity: 0 }, PT);
tl.set("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 16, opacity: 0 }, PT);
tl.to("#thumb-center", { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.4)" }, PT);
tl.to(".orbit-item", { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.4)", stagger: 0.04 }, PT + 0.1);
tl.to("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 0, opacity: 1, duration: 0.3, stagger: 0.05 }, PT + 0.15);
```

---

## #3 — Tier-rank rainbow

```html
<!-- Phase: thumbnail hold (tier-rank) -->
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#0a0a0a;">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; top:60px; left:60px; height:48px;">

  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:160px; left:60px; right:60px;
              font-size:96px; font-weight:900; color:#fff;
              text-align:center; letter-spacing:-0.02em; line-height:1;">
    <TOPIC>
  </div>

  <!-- 5 ranked rows; replace label + number per item; colors are the gradient -->
  <div class="rank-row clip" id="thumb-r1" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:520px; left:60px; right:60px; height:160px;
              background:#ff3b30; border-radius:24px; display:flex; align-items:center;
              padding:0 40px; gap:32px;">
    <div style="font-size:84px; font-weight:900; color:#fff;">1</div>
    <div style="font-size:56px; font-weight:700; color:#fff;">Item one</div>
  </div>
  <div class="rank-row clip" id="thumb-r2" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:700px; left:60px; right:60px; height:160px;
              background:#ff9500; border-radius:24px; display:flex; align-items:center;
              padding:0 40px; gap:32px;">
    <div style="font-size:84px; font-weight:900; color:#fff;">2</div>
    <div style="font-size:56px; font-weight:700; color:#fff;">Item two</div>
  </div>
  <div class="rank-row clip" id="thumb-r3" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:880px; left:60px; right:60px; height:160px;
              background:#ffcc00; border-radius:24px; display:flex; align-items:center;
              padding:0 40px; gap:32px;">
    <div style="font-size:84px; font-weight:900; color:#000;">3</div>
    <div style="font-size:56px; font-weight:700; color:#000;">Item three</div>
  </div>
  <div class="rank-row clip" id="thumb-r4" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:1060px; left:60px; right:60px; height:160px;
              background:#34c759; border-radius:24px; display:flex; align-items:center;
              padding:0 40px; gap:32px;">
    <div style="font-size:84px; font-weight:900; color:#fff;">4</div>
    <div style="font-size:56px; font-weight:700; color:#fff;">Item four</div>
  </div>
  <div class="rank-row clip" id="thumb-r5" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:1240px; left:60px; right:60px; height:160px;
              background:#007aff; border-radius:24px; display:flex; align-items:center;
              padding:0 40px; gap:32px;">
    <div style="font-size:84px; font-weight:900; color:#fff;">5</div>
    <div style="font-size:56px; font-weight:700; color:#fff;">Item five</div>
  </div>

  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:120px; left:60px; right:60px;
              font-size:44px; font-weight:600; color:#999; text-align:center;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** stagger the 5 rows entering left-to-right within 0.5s.

```js
const PT = 28.0;
tl.set(".rank-row", { x: -40, opacity: 0 }, PT);
tl.set("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 16, opacity: 0 }, PT);
tl.to(".rank-row", { x: 0, opacity: 1, duration: 0.4, ease: "back.out(1.2)", stagger: 0.06 }, PT);
tl.to("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 0, opacity: 1, duration: 0.3, stagger: 0.05 }, PT + 0.1);
```

---

## #4 — Whiteboard

This style needs an actual whiteboard texture asset. Drop the asset into `videos/<slug>/assets/whiteboard-bg.jpg` (≥ 1080×1920, real photo of a whiteboard with subtle marker streaks).

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#f4f3ee;">

  <img class="clip" src="assets/whiteboard-bg.jpg"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0.95;">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:60px; left:60px; height:48px;">

  <!-- Hand-drawn-feel diagram (use SVG with rough strokes, OR an Excalidraw export as PNG) -->
  <img class="clip" src="assets/whiteboard-diagram.png"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; top:380px; left:60px; right:60px; width:auto; max-height:1100px; object-fit:contain;">

  <!-- Topic — handwritten font OR clean overlay; here clean overlay -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="4"
       style="position:absolute; top:200px; left:60px; right:60px;
              font-size:88px; font-weight:800; color:#222; text-align:center;">
    <TOPIC>
  </div>

  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="4"
       style="position:absolute; bottom:120px; left:60px; right:60px;
              font-size:44px; font-weight:600; color:#444; text-align:center;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** the diagram appears as if being drawn, but for the thumbnail-hold we keep it simple — fade in within 0.4s.

```js
const PT = 28.0;
tl.set("#phase-thumb img, #phase-thumb > div", { opacity: 0 }, PT);
tl.to("#phase-thumb img, #phase-thumb > div", { opacity: 1, duration: 0.4, stagger: 0.04 }, PT);
```

---

## #5 — Familiar interface (fake tweet)

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#000;">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; bottom:80px; left:60px; height:48px;">

  <!-- Fake tweet card — match X/Twitter spacing precisely -->
  <div id="thumb-tweet" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
              width:920px; background:#16181c; border-radius:24px;
              padding:36px 40px; box-shadow:0 0 0 1px #2f3336;">

    <!-- Author row -->
    <div style="display:flex; align-items:center; gap:16px; margin-bottom:24px;">
      <div style="width:84px; height:84px; border-radius:50%; background:#3a3a3a;"></div>
      <div>
        <div style="display:flex; align-items:center; gap:8px;">
          <div style="font-size:36px; font-weight:800; color:#e7e9ea;">Display Name</div>
          <!-- Verified check -->
          <svg width="32" height="32" viewBox="0 0 24 24" fill="#1d9bf0">
            <path d="M22.5 12.5c0-1.58-.875-2.95-2.148-3.6.154-.435.238-.905.238-1.4 0-2.21-1.71-3.998-3.818-3.998-.47 0-.92.084-1.336.25C14.818 2.415 13.51 1.5 12 1.5s-2.816.917-3.437 2.25c-.415-.165-.866-.25-1.336-.25-2.11 0-3.818 1.79-3.818 4 0 .494.083.964.237 1.4-1.272.65-2.147 2.018-2.147 3.6 0 1.495.782 2.798 1.942 3.486-.02.17-.032.34-.032.514 0 2.21 1.708 4 3.818 4 .47 0 .92-.086 1.335-.25.62 1.334 1.926 2.25 3.437 2.25 1.512 0 2.818-.916 3.437-2.25.415.163.865.248 1.336.248 2.11 0 3.818-1.79 3.818-4 0-.174-.012-.344-.033-.513 1.158-.687 1.943-1.99 1.943-3.484zm-6.616-3.334l-4.334 6.5c-.145.217-.382.354-.643.366-.014.01-.025.01-.04.01-.243 0-.473-.107-.633-.293l-2-2.332c-.245-.282-.232-.71.052-.952.282-.244.72-.235.952.052l1.453 1.55 4.27-6.418c.193-.286.617-.343.893-.146.288.21.347.604.157.892z"/>
          </svg>
        </div>
        <div style="font-size:28px; color:#71767b;">@handle</div>
      </div>
    </div>

    <!-- Tweet body — IS the topic statement -->
    <div style="font-size:60px; font-weight:600; color:#e7e9ea; line-height:1.2; letter-spacing:-0.01em;">
      <TOPIC>
    </div>
  </div>

  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:80px; right:60px;
              font-size:44px; font-weight:600; color:#71767b;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** the card scales in like a notification.

```js
const PT = 28.0;
tl.set("#thumb-tweet", { scale: 0.9, opacity: 0 }, PT);
tl.set("#thumb-brand, #thumb-outcome", { y: 16, opacity: 0 }, PT);
tl.to("#thumb-tweet", { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(1.5)" }, PT);
tl.to("#thumb-brand, #thumb-outcome", { y: 0, opacity: 1, duration: 0.3 }, PT + 0.1);
```

---

## #6 — Cinematic text

This style requires a cinematic photo asset. Drop into `videos/<slug>/assets/cinematic-bg.jpg` (≥ 1080×1920, dark scene with strong directional lighting).

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0;">

  <img class="clip" src="assets/cinematic-bg.jpg"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;">

  <!-- Subtle gradient overlay for type readability -->
  <div class="clip" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; inset:0;
              background:linear-gradient(180deg, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.5) 100%);"></div>

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; top:60px; left:60px; height:48px; filter:brightness(2);">

  <!-- 3-word topic, embedded into scene — bottom-third placement; yellow on dark canon -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; bottom:380px; left:60px; right:60px;
              font-size:200px; font-weight:900; color:#ffd60a;
              line-height:0.9; letter-spacing:-0.04em;
              text-shadow: 0 0 60px rgba(0,0,0,0.4);">
    <TOPIC>
  </div>

  <!-- Outcome — small italic below the topic -->
  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; bottom:300px; left:60px;
              font-size:42px; font-weight:500; font-style:italic; color:#fff; opacity:0.85;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** type fades up subtly, no scale yoyo.

```js
const PT = 28.0;
tl.set("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 30, opacity: 0 }, PT);
tl.to("#thumb-topic", { y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }, PT);
tl.to("#thumb-outcome", { y: 0, opacity: 0.85, duration: 0.4 }, PT + 0.1);
tl.to("#thumb-brand", { y: 0, opacity: 1, duration: 0.3 }, PT + 0.05);
```

---

## #7 — Warped faces

This style needs a warped portrait asset (triple-expose, mirror-split, glitch displacement, or double-expose). Drop into `videos/<slug>/assets/warped-portrait.png`.

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#0a0a0a;">

  <img class="clip" src="assets/warped-portrait.png"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; filter:saturate(0.7) contrast(1.1);">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:60px; left:60px; height:48px; filter:brightness(2);">

  <!-- Topic minimal or absent. If present, off-center, small. -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:280px; left:60px; right:60px;
              font-size:88px; font-weight:900; color:#e8e6e1;
              text-align:left; letter-spacing:-0.02em; line-height:0.95;">
    <TOPIC>
  </div>

  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:120px; left:60px;
              font-size:36px; font-weight:500; color:#888;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** crossfade in, no scale or movement (the warp itself is the spectacle).

```js
const PT = 28.0;
tl.set("#phase-thumb img, #phase-thumb > div", { opacity: 0 }, PT);
tl.to("#phase-thumb img:first-of-type", { opacity: 1, duration: 0.5 }, PT);
tl.to("#thumb-brand, #thumb-topic, #thumb-outcome", { opacity: 1, duration: 0.3, stagger: 0.05 }, PT + 0.1);
```

---

## #8 — Maximalist

This style needs a multi-item collection rendered as one large image (12-30 items grid-arranged). Easiest: photograph the items on a flat surface, OR compose in Figma and export as PNG.

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#1a1a1a;">

  <img class="clip" src="assets/collection.png"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; top:280px; left:0; right:0; width:100%; height:auto; object-fit:contain;">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:60px; left:60px; height:48px;">

  <!-- Topic on top strip -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:140px; left:60px; right:60px;
              font-size:96px; font-weight:900; color:#fff; text-align:center;
              letter-spacing:-0.02em;">
    <TOPIC>
  </div>

  <!-- Outcome on bottom strip -->
  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:80px; left:60px; right:60px;
              font-size:48px; font-weight:600; color:#aaa; text-align:center;">
    <OUTCOME>
  </div>

  <!-- Optional: small host face in corner -->
  <!-- <img class="clip" src="assets/host-corner.png" data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; bottom:200px; right:80px; width:200px; height:200px; border-radius:50%;"> -->
</div>
```

**GSAP:** collection scales in, type follows.

```js
const PT = 28.0;
tl.set("#phase-thumb img:first-of-type", { scale: 0.92, opacity: 0 }, PT);
tl.set("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 16, opacity: 0 }, PT);
tl.to("#phase-thumb img:first-of-type", { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(1.3)" }, PT);
tl.to("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 0, opacity: 1, duration: 0.3, stagger: 0.05 }, PT + 0.1);
```

---

## #9 — Encyclopedia grid

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#fff;">

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; top:60px; left:60px; height:48px;">

  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:200px; left:60px; right:60px;
              font-size:88px; font-weight:900; color:#0a0a0a; text-align:center;
              letter-spacing:-0.02em;">
    <TOPIC>
  </div>

  <!-- 3×3 icon grid -->
  <div class="clip" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:480px; left:60px; right:60px;
              display:grid; grid-template-columns:repeat(3, 1fr); gap:36px;">

    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#ff6b6b; display:flex; align-items:center; justify-content:center; font-size:80px;">🧠</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 1</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#4ecdc4; display:flex; align-items:center; justify-content:center; font-size:80px;">⚙️</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 2</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#ffe66d; display:flex; align-items:center; justify-content:center; font-size:80px;">🔧</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 3</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#a8dadc; display:flex; align-items:center; justify-content:center; font-size:80px;">📦</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 4</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#f1faee; border:4px solid #0a0a0a; display:flex; align-items:center; justify-content:center; font-size:80px;">📊</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 5</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#e63946; display:flex; align-items:center; justify-content:center; font-size:80px;">🎯</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 6</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#1d3557; display:flex; align-items:center; justify-content:center; font-size:80px;">🔥</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 7</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#457b9d; display:flex; align-items:center; justify-content:center; font-size:80px;">⭐</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 8</div>
    </div>
    <div class="grid-cell" style="text-align:center;">
      <div style="width:200px; height:200px; margin:0 auto; border-radius:50%; background:#2a9d8f; display:flex; align-items:center; justify-content:center; font-size:80px;">💡</div>
      <div style="font-size:36px; font-weight:700; color:#0a0a0a; margin-top:16px;">Label 9</div>
    </div>
  </div>

  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:80px; left:60px; right:60px;
              font-size:44px; font-weight:600; color:#666; text-align:center;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** all cells fade in with quick stagger.

```js
const PT = 28.0;
tl.set(".grid-cell", { y: 20, opacity: 0 }, PT);
tl.set("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 16, opacity: 0 }, PT);
tl.to(".grid-cell", { y: 0, opacity: 1, duration: 0.35, ease: "power2.out", stagger: 0.03 }, PT);
tl.to("#thumb-topic, #thumb-outcome, #thumb-brand", { y: 0, opacity: 1, duration: 0.3 }, PT);
```

---

## #10 — Candid fake

This style needs an engineered photo asset: `videos/<slug>/assets/candid.jpg` — composed image that *could* have been captured (host + product + setting in a believable but unreproducible moment).

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0;">

  <img class="clip" src="assets/candid.jpg"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;">

  <!-- Tiny corner watermark, NO topic overlay, NO arrows, NO red circles -->
  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:60px; right:60px; height:40px; opacity:0.8; filter:brightness(2);">

  <!-- Optional graphic decoration (floating UI / glow) — skip if frame is strong enough on its own -->
  <!-- <div class="clip" id="thumb-glow" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:600px; left:50%; transform:translateX(-50%);
              width:400px; height:400px; border-radius:50%; background:radial-gradient(rgba(255,200,0,0.6), transparent);"></div> -->
</div>
```

**GSAP:** simple crossfade — the photo IS the moment.

```js
const PT = 28.0;
tl.set("#phase-thumb img", { opacity: 0 }, PT);
tl.to("#phase-thumb img:first-of-type", { opacity: 1, duration: 0.5 }, PT);
tl.to("#thumb-brand", { opacity: 0.8, duration: 0.3 }, PT + 0.2);
```

> ⚠️ Per the skill's hard rules, document in the video description if this still is engineered/AI-assisted, not real footage.

---

## #11 — Anti-thumbnail (quiet)

Needs a serious, well-lit portrait asset: `videos/<slug>/assets/host-serious.jpg` (host face, direct camera contact, single dramatic key light, dark background).

```html
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9"
     style="position:absolute; inset:0; background:#0d0d10;">

  <img class="clip" src="assets/host-serious.jpg"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;">

  <!-- Subtle vignette to push focus to face center -->
  <div class="clip" data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; inset:0;
              background:radial-gradient(ellipse at center, transparent 35%, rgba(0,0,0,0.7) 100%);"></div>

  <img id="thumb-brand" class="clip" src="<BRAND-LOGO-PATH>"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; top:60px; left:60px; height:42px; filter:brightness(2); opacity:0.7;">

  <!-- Off-round time constraint — the entire text content -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; bottom:280px; left:60px; right:60px;
              font-size:200px; font-weight:900; color:#fff;
              text-align:center; letter-spacing:-0.04em; line-height:0.9;">
    47 seconds.
  </div>

  <!-- Outcome — a single 3-4 word line below -->
  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="3"
       style="position:absolute; bottom:180px; left:60px; right:60px;
              font-size:48px; font-weight:500; color:#bbb;
              text-align:center; letter-spacing:0.02em;">
    <OUTCOME>
  </div>
</div>
```

**GSAP:** quiet fade-in. NO scale, NO bounce.

```js
const PT = 28.0;
tl.set("#phase-thumb img, #phase-thumb > div", { opacity: 0 }, PT);
tl.to("#phase-thumb img:first-of-type", { opacity: 1, duration: 0.5 }, PT);
tl.to("#thumb-topic", { opacity: 1, duration: 0.45 }, PT + 0.1);
tl.to("#thumb-outcome, #thumb-brand", { opacity: 1, duration: 0.4, stagger: 0.05 }, PT + 0.2);
```

---

## Universal post-author checklist

After pasting any template:

1. Replace `<TOPIC>`, `<OUTCOME>`, `<BRAND-LOGO-PATH>`, `<ANCHOR>` with real content
2. Adjust `data-start` to match your video's actual outro timing
3. Confirm `data-track-index` is HIGHER than any other concurrent phase (so the thumb-phase paints on top)
4. Drop required asset files into `videos/<slug>/assets/` (per template)
5. Run `npx hyperframes lint videos/<slug>` — fix all errors
6. Run `npx hyperframes inspect videos/<slug>` — fix any overflow
7. Open in `npx hyperframes preview videos/<slug>` and scrub to the last frame
8. Run [`audit-checklist.md`](audit-checklist.md) Layer 1 + Layer 2 for the chosen style
9. Document the picked style in `videos/<slug>/notes.md`
