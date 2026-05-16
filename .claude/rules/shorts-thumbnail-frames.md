# Shorts thumbnail frames — first AND last frame must be thumbnail-grade

Every vertical Short (`templates/shorts/<style>/`, every `videos/<slug>/` with a 1080×1920 canvas) MUST open on a **thumbnail-grade first frame** AND close on a **thumbnail-grade final frame** — held stills that, on their own with zero context, communicate the topic in under one second, stop the scroll, and make someone tap.

**Why both ends?**

- **First frame**: YouTube auto-picks the first frame as the entry thumbnail when no manual thumbnail is uploaded. A viewer scrolling the Shorts feed sees the video's first frame as the tile. A pain-hook or "WEEKS LATE." message at t=0 tells a new viewer nothing and CTR suffers.
- **Final frame**: Shorts loop. The final frame becomes the first frame on the next loop iteration, the still YouTube shows when the viewer pauses, the still that gets screenshotted and shared. A weak last frame (solo CTA, fade-to-black, brand wordmark on empty background) loses the loop and the share.

Both frames must satisfy the same 5-element checklist — the visual requirements are identical regardless of position.

---

## The 5 mandatory elements (applies to BOTH first AND last frame)

All five must be on screen at the same time in the thumbnail-grade frame:

1. **Topic statement** — the single most important phrase from the video, sized as the dominant element. Minimum 120px on canvas (recommended 140–200px). Not a question; a punchline. Examples: "CLAUDE CODE 2.0 IS HERE", "ARCHON BEATS CURSOR", "GEMINI 3 LEAKED".
2. **Visual anchor** — the hero icon, logo, version number, screenshot, or product mark that ties the topic to a recognizable thing. The viewer's eye must land on this within 200ms of pausing.
3. **Brand chrome** — the channel/brand wordmark or avatar, small but legible (≥ 40px logo height). This is what makes a screenshot trace back to the channel.
4. **Outcome / receipt** — one short line stating WHAT the viewer learns by watching (or learned, if they watched). Not a CTA. Examples: "5 features in 30 seconds", "the new default model", "what changed in 2.0". Min 36px, recommended 44–56px.
5. **Optional CTA pill** — "Watch the full video" / "Follow for more" — but the CTA NEVER occupies the dominant slot. The topic statement does.

---

## The first frame — thumbnail-grade opening

### Why the first frame is the thumbnail

YouTube's auto-thumbnail picker defaults to a frame near the start of the video when no manual thumbnail is uploaded. For Shorts, this is typically the very first rendered frame. A viewer scrolling the feed sees this frame as the tile image before tapping.

### The open-topic-then-pivot pattern (Anthropic template default)

Phase 1 is split into two visual beats within the same phase duration:

- **Beat 1a (0.0s → ~2.5s)**: The thumbnail-grade topic lockup is the dominant visible content from frame zero — no entrance animation delay, no fade-in. Elements: brand lockup (logo(s)), dominant topic slam (≥120px), outcome receipt line. Narration can play underneath — the topic frame is visible while the first sentence runs.
- **Beat 1b (~2.5s onward)**: The pain hook / hero slam content fades in as the topic lockup fades out. The original hook narrative (e.g., "WEEKS LATE.") takes the dominant slot from here.

This means:
- t=0.0s: paused frame → thumbnail-grade topic + brand (YouTube auto-thumbnail picks this)
- t=0.0–2.5s: narration plays while topic is dominant
- t=2.5s onward: topic transitions to a fade, pain/hook copy takes over

### First-frame timing

- **Topic lockup visible from t=0**: No entrance animation needed — the elements are at full opacity at composition start.
- **Static hold**: ≤ 2.5s before beat 1b starts. [`visual-pacing-5s.md`](./visual-pacing-5s.md) is explicitly relaxed for this opening beat — same rationale as the terminal hold.
- **Fade-out to beat 1b**: `tl.to("#p1-topic-lockup", { opacity: 0, duration: 0.5 }, 2.4)` is the template pattern.

### What the first frame must NOT be

- ❌ A pain hook or rhetorical question as the sole dominant content — the viewer has no context yet ("WEEKS LATE" with no topic anchor is meaningless as a thumbnail)
- ❌ An empty dark stage with only the overline — the top chrome alone does not carry the topic
- ❌ A fade-in with opacity 0 at t=0 — the very first rendered frame is black, which YouTube picks as the thumbnail

---

## The final frame — thumbnail-grade close

### Why the final frame is the thumbnail

Shorts loop. The final frame becomes the first frame on the next loop, the still YouTube shows when the viewer pauses, the still that gets screenshotted and shared, and frequently the still YouTube auto-picks as the thumbnail when one isn't manually uploaded.

### How to author it

Append a dedicated final phase (commonly `#phaseN-thumb` or `#phase-end`) AFTER the CTA / outro phase, OR enrich the existing CTA phase to satisfy all 5 requirements. Either pattern works; the rule is on the resulting frame, not the phase count.

```html
<!-- Phase: thumbnail hold (last 2.0s of the Short) -->
<div id="phase-thumb" class="clip phase"
     data-start="28.0" data-duration="2.0" data-track-index="9">

  <!-- Brand chrome (top-left) -->
  <img id="thumb-brand" class="clip" src="assets/dynamous-mark.svg"
       data-start="0" data-duration="2" data-track-index="1"
       style="position:absolute; top:60px; left:60px; height:48px;">

  <!-- Topic slam (dominant) -->
  <div id="thumb-topic" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:580px; left:60px; right:60px;
              font-size:160px; font-weight:900; line-height:0.95;
              letter-spacing:-0.03em; color:var(--accent);">
    CLAUDE CODE<br>2.0 IS HERE
  </div>

  <!-- Visual anchor (version chip / icon) -->
  <div id="thumb-version" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:1080px; left:60px;
              font-size:88px; font-weight:800;
              padding:18px 36px; border-radius:24px;
              background:var(--accent); color:#000;">
    v2.0.14
  </div>

  <!-- Outcome receipt -->
  <div id="thumb-outcome" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; top:1280px; left:60px; right:60px;
              font-size:52px; font-weight:600; color:var(--fg-dim);">
    5 things that changed
  </div>

  <!-- CTA (subordinate) -->
  <div id="thumb-cta" class="clip"
       data-start="0" data-duration="2" data-track-index="2"
       style="position:absolute; bottom:120px; left:60px;
              font-size:46px; font-weight:700;
              padding:20px 40px; border-radius:9999px;
              background:#fff; color:#000;">
    Follow for more →
  </div>
</div>
```

The phase must enter via the standard whoosh+shape-rearrange transition and then **freeze** — every entrance animation finishes by `data-start + 0.5s`, leaving ≥ 1.5s of completely static hold.

### Final-frame timing

- **Total final phase duration**: 2.0–2.5s recommended, 1.8s minimum.
- **Entrance animation budget**: ≤ 0.5s from phase start. After that, every element is at its final transform — no scale yoyos, no glow pulses, no shape drift.
- **Static hold**: ≥ 1.5s. This is the part that becomes the loop-pause thumbnail.

### What the final frame must NOT be

- ❌ A solo CTA pill ("Subscribe →") on an empty/dark background — the loop now opens with "Subscribe" instead of the topic
- ❌ Fade-to-black or fade-to-brand-color — dead air on pause/loop
- ❌ Brand wordmark/logo as the only large element — viewer learns nothing about the topic
- ❌ A trailing animation (counter still rolling, marker still sweeping). Every motion must finish ≥ 0.3s before the hold begins.
- ❌ The same frame as the hero slam from the intro — the end frame is the receipt; the intro is the question
- ❌ A full-bleed quote with no visual anchor — text-only thumbs underperform

---

## Interaction with other rules

- **[`visual-pacing-5s.md`](./visual-pacing-5s.md)**: Explicitly relaxed for BOTH the opening thumbnail hold (≤ 2.5s) AND the terminal thumbnail hold (≤ 2.5s). The relaxation applies ONLY to these two designated thumbnail-grade still windows. Anywhere else in the Short, the 5s rule still binds.
- **[`shorts-typography.md`](./shorts-typography.md)**: Sizes for the topic slam (≥120px), outcome (≥36px), CTA pill (≥44px), brand chrome (≥40px logo height) inherit from the typography minimums.
- **[`step-by-step-reveal.md`](./step-by-step-reveal.md)**: All thumbnail elements may enter together (within a 0.5s stagger). The thumbnail is a single composite, not an enumeration — quick stagger is correct here.

---

## Self-check before declaring a Short done

**First frame check** — pause the rendered MP4 at t=0 (or the very first frame) and ask:

1. **Topic test**: Could a stranger seeing ONLY this frame as a YouTube Shorts tile, with no audio, name the video's topic in one sentence?
2. **Thumbnail test**: Would this frame, shown as a static tile in the Shorts feed, make a viewer tap to watch?
3. **Brand test**: Does this frame visually connect to the channel — logo, wordmark, or recognizable brand color?
4. **No-context test**: If YouTube auto-picks this as the upload thumbnail, does the channel come across well?

**Final frame check** — pause the rendered MP4 on its very last frame and ask:

1. **Topic test**: Could a stranger paused on this frame, with no audio, no prior frames, name the video's topic in one sentence?
2. **Tap test**: Would this frame, shown as a tile in a YouTube Shorts feed, make a thumb-stopping viewer tap?
3. **Loop test**: When the Short loops and this frame becomes the opening frame for the next play, does it set up the topic — or does it confuse?
4. **Screenshot test**: If a viewer screenshots and shares this frame, does the share carry the channel + topic, or just a generic CTA?

If any answer is "no" for either frame, the composition is not done. Rework before render.

---

## Where this rule applies

- All vertical Shorts (`templates/shorts/<style>/`, every `videos/<slug>/` with 1080×1920 canvas).
- Includes derivatives — Anthropic, Archon, Dynamous, Google, news-explainer, claude-code-version, and any future shorts variants.

## Where this rule does NOT apply

- Long-form (`templates/long-form/<style>/`, 1920×1080). Long-form has YouTube end-screens and a manually uploaded thumbnail; the first and last frames play different roles.
- A Short that opens on a deliberate cold-open (black frame + narration) as a creative choice — but flag the deviation explicitly in the video's `notes.md` and ensure a manual thumbnail is uploaded to compensate for the non-thumbnail-grade first frame.
