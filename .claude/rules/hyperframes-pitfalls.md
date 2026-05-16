# HyperFrames pitfalls — common mistakes the linter does NOT catch

Project-local cheat sheet covering pitfalls from the upstream
[**Common Mistakes**](https://hyperframes.mintlify.app/guides/common-mistakes) and
[**Troubleshooting**](https://hyperframes.mintlify.app/guides/troubleshooting)
guides that are NOT already enforced elsewhere in this repo (CLAUDE.md Key Rules,
`hyperframes` skill "Never do" list, or other `.claude/rules/*.md` files).

> **Upstream is the source of truth.** When in doubt, refresh via the doc index:
> `https://hyperframes.mintlify.app/llms.txt` and the two pages above. This file
> captures the items NOT yet duplicated elsewhere — read it alongside, not instead.

Already covered elsewhere (do NOT duplicate guidance here — point at the existing source):

| Pitfall | Where it lives |
|---|---|
| Animating video element dimensions → wrap in a div, animate the wrapper | `hyperframes` skill, "Never do" #5 |
| Calling `video.play()` / `audio.currentTime =` from scripts | `hyperframes` skill, "Never do" #6 |
| Missing `class="clip"` on timed elements | CLAUDE.md Key Rules #2 + `npx hyperframes lint` |
| `window.__timelines["X"]` key ≠ `data-composition-id` | CLAUDE.md Key Rules #3 + `.claude/rules/sub-composition-wiring.md` |

The pitfalls below are the ones our existing docs don't yet cover.

---

## 1. Composition duration shorter than the video / audio source

**Symptom:** The rendered MP4 cuts off after 7-10 seconds even though `narration.wav` is 4 minutes long. `npx hyperframes compositions` shows a duration far shorter than the audio file.

**Cause:** Composition duration is derived from the **GSAP timeline length**, not from `data-duration` on the audio/video element. If the last `tl.from()` / `tl.to()` ends at t=7.8s, the composition is 7.8s long — the media gets truncated.

**Fix — pin the timeline with a trailing `tl.set()`:**

```js
// Last GSAP tween in the timeline
tl.to("#cta", { opacity: 1, duration: 0.6 }, 7.2);

// THEN extend the timeline to the full media length (zero-duration tween, no element touched)
tl.set({}, {}, TOTAL_DURATION);
```

`tl.set({}, {}, T)` adds a no-op tween at time `T`, extending GSAP's perceived
timeline length without changing any visual state. Use it as the **last line**
of every long-form scene + root timeline.

**Self-check before render:**

```bash
npx hyperframes compositions videos/<slug>
```

If the printed duration is shorter than `audio/narration.wav`, the timeline is
underextended. Add the `tl.set({}, {}, TOTAL_DURATION)` line.

---

## 2. Oversized source images destroy preview FPS

**Symptom:** Preview stutters whenever a specific image is on screen. Render is slow. Render machine reports high memory.

**Cause:** Chrome decodes every `<img src>` into a raw RGBA bitmap before
compositing. Bitmap size is `width × height × 4` bytes — **independent of file
size on disk**. A 7000×5000 JPEG that's 2MB on disk becomes ~140 MB once decoded.
Displaying it in a 384×1080 region wastes memory and forces the compositor to
resample a huge texture every frame.

**Rule of thumb:** Source images should be at most **2× canvas dimensions**.

| Canvas | Max recommended source |
|---|---|
| Shorts (1080×1920) | 2160×3840 |
| Long-form (1920×1080) | 3840×2160 |
| Square (1080×1080) | 2160×2160 |

**Batch-resize before adding to a video:**

```bash
mkdir -p assets/resized
mogrify -path assets/resized -resize 3840x3840\> assets/*.jpg
# The trailing \> means "only shrink, never upscale"
```

Then reference `assets/resized/*.jpg` in `index.html`.

**Where this hits us hardest:** screenshots from 5K Macs, marketing renders,
mockups from Figma at 4× export. Always resize before committing to the video's
`assets/` folder.

---

## 3. Heavy `backdrop-filter` stacks tank specific scenes

**Symptom:** Preview is fine for most of the Short, then drops to 5-10fps for one
phase. The composition is otherwise fast.

**Cause:** `backdrop-filter: blur(N)` forces the compositor to sample pixels
behind the element, run a blur kernel, and composite the result. Stacked layers
multiply the cost. Each blur layer at radius >32px is expensive; at radius
>64px on a 1080×1920 region it dominates total frame cost.

**Bad — 8 stacked layers (16 blur passes per frame):**

```css
.pb-1 { backdrop-filter: blur(1px); }
.pb-2 { backdrop-filter: blur(2px); }
.pb-3 { backdrop-filter: blur(4px); }
.pb-4 { backdrop-filter: blur(8px); }
.pb-5 { backdrop-filter: blur(16px); }
.pb-6 { backdrop-filter: blur(32px); }
.pb-7 { backdrop-filter: blur(64px); }
.pb-8 { backdrop-filter: blur(128px); }
```

**Good — 2-3 tuned layers, visually similar, much cheaper:**

```css
.pb-1 { backdrop-filter: blur(4px); }
.pb-2 { backdrop-filter: blur(16px); }
.pb-3 { backdrop-filter: blur(48px); }
```

**Guidelines:**

- ≤ 2-3 stacked `backdrop-filter` layers per region
- Avoid radii > 64px over large areas — the biggest radii dominate cost
- For a **static** glass / blur effect: render it to PNG once and overlay as a
  regular `<img>` instead of computing blur every frame
- `filter: blur()` + `filter: drop-shadow()` on large elements have the same
  problem — apply the same cap

If you can't reproduce a preview stutter at scrub speed, render a draft MP4 —
the renderer captures frames serially and hides the cost, so the output looks
fine while the editor experience is broken.

---

## 4. HDR vs SDR output — auto-detect won't give you what you didn't ask for

**Symptom:** You wanted an HDR render, but the output looks like SDR or
`ffprobe` reports `color_transfer=bt709`.

**Cause:** HyperFrames only switches to HDR encoding when a source `<video>` or
`<img>` is tagged with BT.2020 / PQ / HLG color metadata. Common SDR-by-default
cases:

1. **All sources are SDR.** Verify with `ffprobe`:
   ```bash
   ffprobe -v error -show_streams source.mp4 | grep color_transfer
   # HDR markers: smpte2084 (PQ) or arib-std-b67 (HLG)
   # SDR markers: bt709, smpte170m, bt470bg
   ```
2. **Wrong output format.** HDR requires MP4 — `--format mov` and `--format
   webm` fall back to SDR.
3. **`--sdr` was passed.** Forces SDR regardless of source.

**Force HDR regardless of source:**

```bash
npx hyperframes render videos/<slug> --hdr -o out/<slug>.mp4
```

For this repo, **default is SDR** — our YouTube delivery is SDR-tone-mapped and
forcing HDR on SDR sources gains nothing. Only opt-in to `--hdr` when at least
one source clip is genuinely HDR-graded.

---

## 5. "Render looks different from preview" → use `--docker`

**Symptom:** The MP4 looks subtly different from the preview studio — fonts
reflow, colors shift, antialiasing differs.

**Cause:** Local renders use the host's fonts, Chromium version, and GPU
compositing. Different machine → different output.

**Fix — deterministic rendering:**

```bash
npx hyperframes render videos/<slug> --docker -o out/<slug>.mp4
```

`--docker` runs Chrome + FFmpeg inside a pinned container — byte-identical
across machines, byte-identical across CI runs.

**When to use:**

- **Local default**: skip `--docker` for fast iteration (Docker spin-up + slower
  SDR DOM capture path adds time).
- **Final delivery render**: use `--docker` so the MP4 you upload matches what
  you'd reproduce later.
- **Cross-machine bug reports**: always render with `--docker` so screenshots
  are reproducible.

Requires Docker daemon running. `doctor` reports it.

---

## 6. Render is slower than expected

**Symptom:** A 30-second Short takes 4+ minutes to render. A 7-minute long-form
takes 45 minutes.

**Probe before tuning:**

```bash
npx hyperframes benchmark videos/<slug>
```

`benchmark` renders with preset fps / quality / worker combinations and prints a
table — pick the fastest acceptable preset for your machine.

**Knobs that actually move the needle:**

| Flag | Effect |
|---|---|
| `--quality draft` | Fastest encode. Use while iterating. |
| `--workers <N>` (auto, 1-8) | Parallel Chrome workers. `auto` is usually right; benchmark to confirm. |
| `--gpu` (local only) | Hardware-accelerated encoding. Big wins for h264. |
| `--fps 24` | Use 24fps for cinematic look + 20% faster render than 30fps. 60fps **doubles** render time vs 30fps — only for high-motion content. |
| `--no-browser-gpu` | Compare to confirm GPU compositing is actually helping (rare). |

**Knobs that DON'T help and may hurt:**

- Bumping `--workers` above CPU core count (oversubscribes — slower).
- `--quality high` while iterating (only at final delivery).
- Adding `--docker` for speed (Docker is for determinism, NOT speed).

---

## 7. Preview stutter — diagnose before guessing

**Symptom:** Preview drops frames. Render is fine.

**Cause:** Per-frame paint cost > 16-33ms. Render hides this by capturing
serially; preview can't.

**Diagnose checklist (in order):**

1. **Is it scene-specific?** If yes — an element in THAT scene is expensive.
   Most often a `backdrop-filter` layer or an oversized image (see §2-3).
2. **Open Chrome DevTools → Performance tab.** Record 3-5s of playback. Look
   for long tasks labeled "Composite Layers" or "Paint" exceeding 30ms.
3. **Bisect.** Comment out half the elements in the slow scene. Does stutter
   stop? Bisect again. The element you remove last is the culprit.

**Temporary workaround while authoring:**

```bash
npx hyperframes render videos/<slug> --quality draft -o /tmp/preview.mp4
```

Watch the draft MP4 in a player — render is accurate regardless of per-frame
cost. Use this when preview stutters but you need to verify timing/layout.

---

## 8. `font-family: var(--sans|--mono)` — render-time compiler blocker

**Symptom:** `npx hyperframes render` (and sometimes `preview`) fails with:

```
[Compiler] No deterministic font mapping for: var(--mono), var(--sans)
  Mapped fonts: archivo black → archivo-black, arial black → montserrat, ...
                inter, jetbrains mono → jetbrains-mono, ...
  To fix, pick one:
    1. Use a mapped font name instead (see list above)
    2. Add a @font-face block in your HTML with a local or hosted font file
    3. Install the font locally on the render machine (Docker: add to Dockerfile)
    4. Add an alias to FONT_ALIASES in deterministicFonts.ts
```

**Cause:** The HyperFrames deterministic-font compiler needs to know each font
at compile time so it can embed the correct file in the render. It maps
**literal font names** (`inter`, `jetbrains mono`, `montserrat`, ...) to font
IDs — it does **NOT** follow CSS variable indirection (`var(--sans)`,
`var(--mono)`) because the value of a custom property is only known at
browser-paint time, after the compiler has already passed.

If your `tokens/<name>.css` defines a font alias like `--sans: 'Inter', ...`
and a scene CSS rule does `font-family: var(--sans)`, the compiler sees only
the unresolved `var()` token and errors out. This survives lint + inspect
because neither static-analyzes CSS variable resolution.

> **Heads up:** this pattern is **inherited from most of our templates today**.
> Eighty-nine template files contain `font-family: var(--sans|--mono)` lines
> (run `grep -rlE "font-family:\s*var\(--(sans|mono)" templates/` to enumerate).
> Every video forked from those templates ships with the same latent blocker
> until someone runs render and trips it. Until the templates themselves are
> fixed in a sweep, every new video MUST apply the post-build sed below before
> rendering.

### Fix — replace var() with literal font names

Across the **video's** `index.html` + every `compositions/*.html` file (NOT the
templates themselves — that's a separate cleanup PR):

```bash
# git-bash / msys / linux:
for f in videos/<slug>/index.html videos/<slug>/compositions/*.html; do
  sed -i \
    -e "s|font-family: *var(--sans)|font-family: 'Inter', system-ui, sans-serif|g" \
    -e "s|font-family: *var(--mono)|font-family: 'JetBrains Mono', ui-monospace, monospace|g" \
    "$f"
done
```

PowerShell equivalent:

```powershell
Get-ChildItem -Path videos\<slug>\index.html, videos\<slug>\compositions\*.html |
  ForEach-Object {
    (Get-Content $_.FullName -Raw) `
      -replace "font-family:\s*var\(--sans\)",  "font-family: 'Inter', system-ui, sans-serif" `
      -replace "font-family:\s*var\(--mono\)",  "font-family: 'JetBrains Mono', ui-monospace, monospace" |
      Set-Content -Path $_.FullName -Encoding utf8 -NoNewline
  }
```

Swap the literal font names (Inter / JetBrains Mono) for whatever the video's
tokens actually defined. The mapping table from the error message shows every
supported alias.

### Self-check before render (MANDATORY)

```bash
# After Phase 4 composition build, BEFORE `npx hyperframes render`:
grep -rE "font-family:\s*var\(--(sans|mono)" videos/<slug>/ && \
  echo "❌ font-family var() bindings still present — render will fail" || \
  echo "✓ no font-family var() bindings — safe to render"
```

If the grep finds any matches, run the sed fix above before invoking render.

### What NOT to do

- **Do NOT** patch `tokens/*.css` to inline literal fonts and leave the `var()`
  references in scenes — the var() is still unresolved at compile time.
- **Do NOT** add a Google Fonts `<link>` tag and assume that resolves the var.
  The compiler doesn't follow links — it still needs the literal name on
  `font-family`.
- **Do NOT** ignore the warning and `--force` the render. The output font will
  fall back to system defaults at the render machine, which means a different
  font per host (defeats determinism).

### Why we don't fix the templates in this rule

Patching 89 template files in scope of a single video's render unblock is
risky — every fork inherits the change AND every existing rendered video would
need a re-render to stay byte-identical (`--docker` parity). Schedule a
dedicated template-sweep PR that touches all 89 files in one go, verifies
draft-render on each modified template, and lands as one reviewable diff.

---

## Quick self-check checklist (before declaring a video done)

For every new or significantly-modified video:

- [ ] `npx hyperframes compositions videos/<slug>` — composition duration
      matches `audio/narration.wav` length (within 0.5s).
- [ ] Every image in `assets/` is ≤ 2× canvas dimensions on each axis.
- [ ] No CSS has > 3 stacked `backdrop-filter` layers, none with radius > 64px.
- [ ] `grep -rE "font-family:\s*var\(--(sans|mono)" videos/<slug>/` returns
      EMPTY (per pitfall §8 — if any matches, run the sed fix before render).
- [ ] Final delivery render uses `--docker` (long-form + Shorts both).
- [ ] If targeting HDR delivery, at least one source clip has
      `color_transfer=smpte2084` or `arib-std-b67`.

If any item fails, fix before render.

---

## When to update this rule

When the upstream
[Common Mistakes](https://hyperframes.mintlify.app/guides/common-mistakes) or
[Troubleshooting](https://hyperframes.mintlify.app/guides/troubleshooting) pages
add a new pitfall:

1. Cross-check whether it's already covered by CLAUDE.md, the `hyperframes`
   skill, or another `.claude/rules/*.md` file.
2. If covered: add a row to the "Already covered elsewhere" table above.
3. If not covered: add a new numbered section here, mirroring the existing ones
   (symptom → cause → fix → self-check).

Bump the link list at the top if the upstream URL path changes.
