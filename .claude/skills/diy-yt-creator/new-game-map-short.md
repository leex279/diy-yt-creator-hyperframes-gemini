# new-game-map-short — Playbook

End-to-end pipeline that turns a **topic prompt** into a previewable HyperFrames Short using the `templates/shorts/game-map/` template — a **camera-driven hub-and-spoke** structure (1 hub + 6 hex spokes, GSAP camera pan/zoom replacing phase-mutex crossfades).

This playbook is a **delta-from [`new-anthropic-short.md`](./new-anthropic-short.md)** — the inputs, outputs, Dynamous decision, TTS, transcript, render, and Don'ts steps are identical. Read that playbook first; this file only covers what differs structurally.

> **For research + scriptwriting first**: see [`/diy-yt-creator:full-auto`](../../commands/diy-yt-creator/full-auto.md). That orchestrator runs phases 0-3.5 and writes the artifacts under `videos/<slug>/` that step 4 below picks up via Branch A. Use the pipeline by default; use this skill directly only when you already have a script.

## When to pick this template

The game-map template fits topics where the metaphor of a **tour / journey / "X things you missed"** carries the script. Strong fit:

- "Six things in [release X]"
- "Tour of [framework / product]"
- "The 6 features that ship today"
- "Five mistakes everyone makes" (use 5 spokes — see "Per-section count" below)
- "The map of [domain]: hub topic + spoke aspects"

Weak fit (use `templates/shorts/anthropic/` or `standard/` instead):

- Single-claim Shorts ("Claude Code got dumber" — one hero hook, no enumerable spokes)
- Postmortems with chronological evidence (timeline cards work better than spokes)
- Pure stat dumps ("3 bugs / 6 weeks" — stat-pill row is more direct than 6 separate sections)
- News announcements with a single source screenshot (the journey metaphor adds friction over a direct hero+receipt)

## Inputs

User provides ONE of:

- A **topic / prompt** with a list-friendly framing (e.g. _"Walk me through the 6 features that shipped in Claude Code 2.0"_) — agent drafts the full script across hub + 6 spokes
- A **title + 6 facts/highlights** (one per spoke) — agent uses the facts verbatim
- A **pre-written `script.txt`** with 7 narration blocks (hub + S1..S6) — agent skips drafting (jump to step 5)

If the user asks for a game-map but only has 4 distinct points, **propose dropping to a 4-spoke layout** before drafting. Padding 4 ideas across 6 spokes produces filler sections that break retention.

## Outputs

Same as `new-anthropic-short.md`:

- `script.txt` — narration script (organized as 7 blank-line-separated blocks: hub + S1..S6)
- `audio/narration.wav` — ElevenLabs TTS
- `transcript.json` — word-level timestamps
- `index.html` — composition with content filled in, camera moves retimed to spoken-word frames
- Preview studio open

The user runs render themselves: `npx hyperframes render videos/<slug> -o videos/<slug>/out/<slug>.mp4`.

---

## Steps — deltas from the Anthropic playbook

### 1. Confirm slug + title

Same as `new-anthropic-short.md` step 1. Slug examples specific to this template:

- "6 things shipping in Claude Code 2.0" → `claude-code-2-tour`
- "The 5 features I missed in Cursor" → `cursor-five-missed`
- "Walk through the GPT-5 capabilities" → `gpt5-capability-tour`

### 2. Copy the template

```bash
cp -r templates/shorts/game-map videos/<slug>
# PowerShell: Copy-Item -Recurse templates/shorts/game-map videos/<slug>
```

Verify the copy: `videos/<slug>/index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `audio/`, `assets/`, `tokens/`, `compositions/` should all exist.

### 3. Update meta.json

Same as `new-anthropic-short.md` step 3.

### 3.5. Dynamous decision

Same as `new-anthropic-short.md` step 3.5. Apply the wiring snippet to the game-map composition the same way — the badge and endcard are independent of camera state and can be wired without modification.

### 4. Draft the script — game-map structure

The narration MUST be 7 blocks separated by blank lines, in path order: HUB, S1, S2, S3, S4, S5, S6.

```
[hub block — the hero hook + one-line setup that frames the journey]

[S1 block — first point, plus a one-sentence receipt]

[S2 block — second point + receipt]

[S3 block — third point + receipt — this lands after the chapter break, treat it as the "but here's what nobody talks about" pivot]

[S4 block — fourth point + receipt]

[S5 block — fifth point + receipt]

[S6 block — sixth point + receipt — this is the loop-closing beat, mirror the hook]
```

**Per-block budget (default 38s short, ~90 narration words/min):**

| Block      | Word target | Time budget | What's on screen at this moment            |
| ---------- | ----------- | ----------- | ------------------------------------------ |
| HUB        | 9-13 words  | 4.5s        | Hero-slam + overline + accent pill         |
| S1, S2     | 8-11 words  | 4.0s each   | Overline + headline + body                 |
| S3 (pivot) | 9-13 words  | 4.0s        | (after chapter break) Same layout as spokes |
| S4, S5     | 8-11 words  | 4.0s each   | Overline + headline + body                 |
| S6         | 8-11 words  | 3.0s        | Loop-closer beat                           |

Total narration target: **~70-85 words across all 7 blocks**. The short's total duration is 38s, but ~6s is camera transit + establishing/completion holds with no narration; budget the words against the ~32s of "in-section" narration.

**Style rules** are the same as the Anthropic playbook step 4 (no semicolons, no em-dashes, digits not words for numbers, etc.). The Phase 2 / 2.5 / 2a / 2b commands work identically.

### 4.5 — 4.7. Source grounding, trust-signal screenshot, retention strategy

Same as `new-anthropic-short.md`. The trust-signal screenshot, if any, sits inside one of the spokes' content area (NOT in the HUB — the HUB is the hero hook). Pick a spoke whose narration matches the screenshot's claim.

### 5-7. TTS, transcript, compute timing anchors

Same as `new-anthropic-short.md` steps 5-7, with **one game-map-specific change**: instead of computing 4 phase boundaries, you compute **8 camera-move anchors**.

Read `transcript.json` and identify, in seconds:

```
hub_end   = end time of the last word of the HUB block
s1_end    = end time of the last word of the S1 block
... up through s6_end
total_duration = s6_end + 3.5  (1.5s pull-back + 2.0s completion hold)
```

Then compute the camera-tween `at` values:

```
t_dive       = 2.5
t_pan_s1     = hub_end - 0.2
t_pan_s2     = s1_end  - 0.2
t_chapter_s3 = s2_end  - 0.2
t_pan_s4     = s3_end  - 0.2
t_pan_s5     = s4_end  - 0.2
t_pan_s6     = s5_end  - 0.2
t_pullback   = s6_end  + 0.3      (small breath after S6 narration ends)
```

The chapter-break to S3 is 1.5s long (zoom-out + zoom-in), so the start of the S3 content fade-in is at `t_chapter_s3 + 0.6` (the camera reaches map view at +0.6, then dives into S3 over 0.9s arriving at +1.5).

### 8. Edit `videos/<slug>/index.html`

Always invoke the `/hyperframes` skill before this step.

The structure differs from the Anthropic template — there are 7 sections, not 4 phases, and the script tag has 8 camera tweens instead of 4 phase-crossfade blocks. Edit in this exact order:

1. **`<title>`** in `<head>` → the video title.
2. **`#root`** `data-duration` → `total_duration` (rounded to 0.1s).
3. **`#top-banner-logo`** `src` → swap to the right brand logo (copy from `shared/logos/` into `assets/` first; never reference paths outside the project dir).
4. **HUB content** (`#sec-hub`):
   - `.overline` → mono setup line (3-5 words)
   - `.hero-slam` → the slam word (160px max — keep it 6-10 chars)
   - `.accent-pill` → mono receipt (4-7 words)
   - `.node-num` `.node-label` → usually leave as `00` / `START`
5. **Spokes** (`#sec-1` through `#sec-6`):
   - `.overline` → 1-2 word category for that spoke
   - `.headline` → the section's main beat (one sentence, ≤ 10 words)
   - `.body` → optional 1-2 sentence receipt (omit if narration carries everything)
   - `.node-num` → `01-06` (do NOT change — these are structural)
   - `.node-label` → 1-word topic chip per spoke (e.g., `HOOK`, `STAT`, `PROOF`, `TWIST`, `CASE`, `CTA`)
6. **Map-overlay copy** (`#map-overlay`):
   - `.map-overline` → same theme as the HUB overline
   - `.map-headline` → the same hero phrase as the slam, broken into 2 lines (use `<br/>`)
   - `.map-sub` → "Tap → to start" by default; the script swaps it to the completion copy at t=35.8s via `tl.set('#map-overlay-sub', { innerText: ... })`. Update BOTH the HTML default AND the inner-text swap line.
7. **Final-frame CTA** (`#final-cta`):
   - `.cta-pill` text → "Follow for more →" by default. Match the channel's standard CTA wording.
8. **Camera-tween timestamps in the `<script>` block**: replace each `at` value (the last argument of `tl.to('#camera', ..., T)`) with the computed timing anchors from step 7.
9. **Per-section content micro-beats**: replace each section's `.overline`/`.headline`/`.body` entrance times with word-anchored values from the transcript (find the word in `transcript.json` where each beat should land).
10. **Badge ✓ check timestamps**: each `tl.to('#sec-N .node-check', ...)` happens late in that section's narration block (just before camera leaves). Compute as `<section_end> - 0.6` for each.
11. **Progress bar tween**: change `duration: 38` (in the `#progress-fill` fromTo) to the new `total_duration`.
12. **Audio element — narration**: insert just before `</div>` (the closing tag of `#root`), at the same indent level as the camera div. Use `data-start="0"` and `data-duration="<s6_end>"`. Track index 2.
13. **SFX cues — game-map default is camera-move whooshes** (per `templates/shorts/game-map/DESIGN.md` § Audio / SFX Cues). Wire all 8 cues:

```html
<audio id="sfx-dive-whoosh"   class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_dive>"        data-duration="0.84" data-track-index="3" data-volume="0.13"></audio>
<audio id="sfx-dive-impact"   class="clip" src="assets/sfx/impact-slam.mp3"
       data-start="<t_dive + 0.35>" data-duration="0.50" data-track-index="4" data-volume="0.15"></audio>

<audio id="sfx-pan-1"     class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_pan_s1>"      data-duration="0.50" data-track-index="3" data-volume="0.08"></audio>
<audio id="sfx-pan-2"     class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_pan_s2>"      data-duration="0.50" data-track-index="3" data-volume="0.08"></audio>

<audio id="sfx-chapter-1" class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_chapter_s3>"  data-duration="1.40" data-track-index="3" data-volume="0.13"></audio>

<audio id="sfx-pan-4"     class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_pan_s4>"      data-duration="0.50" data-track-index="3" data-volume="0.08"></audio>
<audio id="sfx-pan-5"     class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_pan_s5>"      data-duration="0.50" data-track-index="3" data-volume="0.08"></audio>
<audio id="sfx-pan-6"     class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_pan_s6>"      data-duration="0.50" data-track-index="3" data-volume="0.08"></audio>

<audio id="sfx-pullback"   class="clip" src="assets/sfx/cinematic-whoosh.mp3"
       data-start="<t_pullback>"        data-duration="1.40" data-track-index="3" data-volume="0.13"></audio>
<audio id="sfx-completion" class="clip" src="assets/sfx/scale-slam.mp3"
       data-start="<t_pullback + 1.3>"  data-duration="0.60" data-track-index="4" data-volume="0.13"></audio>
```

The default `index.html` ships these as a comment block at the bottom — uncomment and tune the `data-start` values per the computed anchors. The chapter-break whoosh (`sfx-chapter-1`) is 1.4s long because the camera move itself is 1.5s; both the whoosh and the impact land within the move's window.

**Whoosh-to-camera-move alignment rule (HARD):** every whoosh's `data-start` MUST equal the camera tween's `at` time. NOT `at - 0.4` (that's the Anthropic shape-reposition rule, which doesn't apply to this template — game-map doesn't reposition shapes). Drift > 0.15s is a defect.

### 9-12. Lint / inspect / validate / preview / YouTube description / done

Same as `new-anthropic-short.md`. The validation gates are unchanged:

```bash
npx hyperframes lint     videos/<slug>     # 0 errors, 1 warning (composition_file_too_large) is the accepted baseline
npx hyperframes validate videos/<slug>     # WCAG AA on all text
npx hyperframes inspect  videos/<slug>     # 0 layout overflow at active section
npx hyperframes preview  videos/<slug>     # opens studio
```

Then run [`new-anthropic-short.md`](./new-anthropic-short.md) §11.7 — **generate `videos/<slug>/youtube-description.md`** per [`.claude/rules/youtube-metadata.md`](../../rules/youtube-metadata.md). LEAN structure: vidIQ research → SEO hook (keyword-front-loaded) → Dynamous block → Resources: → Hostinger affiliate block in `----` separators (MANDATORY) → engagement question → hashtags → validate URLs. **Shorts skip Chapters entirely. NO Key Changes / Key Concepts bullet sections — explicitly cut.**

Ends at preview + description. **Never auto-render** (per the diy-yt-creator hard rule).

---

## Per-section count — when to deviate from the default 6 spokes

Default is hub + 6 spokes (hexagonal). To deviate:

- **5 spokes** (pentagonal): for "5 things" topics. Re-position S1-S5 at 90°, 162°, 234°, 306°, 18° (offset so the missing 6th doesn't leave a visible gap). Drop one camera move from the timeline (e.g., remove S5 → S6, end on S5 then pull back). Total duration ~32s.
- **4 spokes** (cardinal cross): for "4 things" topics. Position at N/E/S/W. 6 camera moves total. Total duration ~28s.
- **8 spokes** (octagon): for dense "8 things" Shorts. Add S7 + S8 with VIEWS entries + connection lines. ADD a second chapter break (after S5 say) so two zoom-outs space the rhythm. Total duration ~48-52s.

**Always re-author** the matching `VIEWS.sN` entries when adding/removing sections — see DESIGN.md for the formula. Also add `data-layout-allow-overflow="true"` to every new section.

Do NOT exceed 8 spokes — the map gets too crowded at scale 0.26 to read in the establishing shot.

## Quality bar checklist

Before declaring done:

- [ ] All 7 (or N+1) sections have non-placeholder content
- [ ] Camera transforms (`VIEWS.sN`) match each section's `top` / `left` (use the formula `tx = 540 - Lx`, `ty = 960 - Ly` at scale 1)
- [ ] Each camera move has a paired audio cue with `data-start` = camera-tween `at` (drift ≤ 0.05s for percussive cues, ≤ 0.15s for whooshes)
- [ ] Each section's content fade-in lands within 0.4s of the camera arriving (no dead air)
- [ ] Each section's badge ✓ lights up before the camera leaves (so the completion screen reads as "all visited")
- [ ] Final 1.5-2.0s holds the completion screen STILL (no drift, no pulses) per `shorts-thumbnail-frames.md`
- [ ] Map-overlay copy swap fires at t = pullback + 1.3 (so the completion copy is on screen when the camera lands at map view)
- [ ] `npx hyperframes lint` returns 0 errors (1 file-size warning is the accepted baseline)
- [ ] `npx hyperframes validate` returns no contrast errors
- [ ] `npx hyperframes inspect` returns 0 layout issues
- [ ] Preview confirms the duration display reads `0:00 / <total>` — NOT `0:00 / 0:00` (silent-bail symptom — see `.claude/rules/sub-composition-wiring.md`)

## Don'ts (template-specific)

1. **Don't change the camera ease.** `power2.inOut` for direct pans, `power2.in` → `power2.out` for chapter breaks. Other eases break the "physical lens" feel.
2. **Don't add per-section `tl.from(...filter: "blur"...)`** as a transition — this is a camera template, not a phase-mutex one. The camera is the transition.
3. **Don't omit the establishing shot.** Without the 0-2.5s map view, the viewer never sees the journey structure, and the template degrades to "weird floating sections that pan around for no reason".
4. **Don't omit the pull-back.** Without the final pull-back, the Short ends inside S6 — no thumbnail-grade frame, no loop closure.
5. **Don't author with > 8 spokes.** The establishing shot becomes unreadable.
6. **Don't forget to update both occurrences of map-overlay copy.** The HTML default is the establishing-shot copy; the `tl.set` swap in the script tag is the completion copy. Forgetting one leaves stale text on screen.
7. **Don't use `Math.random` / `Date.now`** in the script tag (HyperFrames determinism rule). The shape scatter in this template uses the seeded `seedHash` PRNG for the same reason.
