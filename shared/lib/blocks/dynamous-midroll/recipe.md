# Recipe: dynamous-midroll

A 31.5-second, 6-phase Dynamous AI Mastery promotional break for **long-form (1920x1080)** videos. Drops in at a natural script pause (typically halfway through the video), plays its own narration + transition SFX, and hands back to the host. Mirrors the legacy Remotion `DynamousMidrollV2.tsx` visually and structurally — same script, same phase order, same brand surface.

> **OPT-IN per video.** Only wire this block when the author has opted in to the Dynamous promotion at spawn time. The block is brand-locked content (see "Slots" below) — every opted-in long-form video carries the identical script, identical course lists, identical CTA. Brand consistency is the load-bearing benefit.

> **Long-form only.** Built for 1920×1080. There is **no Shorts variant** — Shorts already have `dynamous-endcard` (1080×1920) for the same job.

## What it produces

```
   ┌──── 1920 × 1080 frame ──────────────────────────────────────┐
   │  [WERBUNG]                          [Logo Dynamous AI Mastery]
   │                                                             │
   │  ╔═══════════════════════════════════════════════════════╗  │
   │  ║                                                       ║  │
   │  ║   Phase 1 (0.0–9.4s)  Community                       ║  │
   │  ║   1,000+  Builders   Three Full Courses               ║  │
   │  ║   ● Daily Hangouts                                    ║  │
   │  ║   ● Debug Together         [LIVE]                     ║  │
   │  ║   ● Weekly Workshops       [FEATURED]                 ║  │
   │  ║                                                       ║  │
   │  ║   Phase 2 (9.4–16.0s)  Agentic Coding                 ║  │
   │  ║   AGENTIC CODING COURSE / Master AI Coding / 18 mods  ║  │
   │  ║   →  scrolling list of 18 modules                     ║  │
   │  ║                                                       ║  │
   │  ║   Phase 3 (16.0–21.4s)  Agent Mastery                 ║  │
   │  ║   AI AGENT MASTERY / Build AI Agents / n8n + Python   ║  │
   │  ║   →  5 highlight cards (icons + text)                 ║  │
   │  ║                                                       ║  │
   │  ║   Phase 4 (21.4–27.3s)  Second Brain Bootcamp         ║  │
   │  ║   SECOND BRAIN BOOTCAMP / Your Personal AI / 8 mods   ║  │
   │  ║   →  scrolling list of 8 lessons                      ║  │
   │  ║                                                       ║  │
   │  ║   Phase 5 (27.3–30.2s)  CTA                           ║  │
   │  ║   [Cole portrait]   Join the Community                ║  │
   │  ║                     [Link in Description ↓]           ║  │
   │  ║                     [10% OFF]   dynamous.ai           ║  │
   │  ║                                                       ║  │
   │  ║   Outro (30.2–31.5s)  "Back to the video."            ║  │
   │  ╚═══════════════════════════════════════════════════════╝  │
   └─────────────────────────────────────────────────────────────┘
                       ↓
              fade-to-transparent at 30.8–31.5s
                       ↓
                host video resumes
```

Phase boundaries are anchored to word-end timestamps in `dynamous-midroll-v2-sync.json` (with a 0.3s audio-offset for the transition-in SFX):

| Phase | Visual time | Audio anchor (1.0x) |
|---|---|---|
| 1 — Community | 0.0 → 9.4s | "courses." ends 9.137s |
| 2 — Agentic Coding | 9.4 → 16.0s | "repeatable." ends 15.708s |
| 3 — Agent Mastery | 16.0 → 21.4s | "Python." ends 21.142s |
| 4 — Second Brain | 21.4 → 27.3s | "scratch." ends 27.016s |
| 5 — CTA | 27.3 → 30.2s | "off." ends 29.861s |
| Outro | 30.2 → 31.5s | "video." ends 30.975s |

## Required tokens

None. The block inlines the midroll v3 palette (slate `#0f172a` + purple `#a855f7` + pink `#ec4899` + cyan `#06b6d4` + red `#dc2626`) and the Inter font.

## Wire into a host long-form composition

### 1. Copy the block into the video's `compositions/` folder

```bash
cp shared/lib/blocks/dynamous-midroll/block.html \
   videos/<slug>/compositions/dynamous-midroll.html
```

PowerShell:
```powershell
Copy-Item shared/lib/blocks/dynamous-midroll/block.html `
  videos/<slug>/compositions/dynamous-midroll.html
```

### 2. Copy ALL static assets into the video's `assets/` folder

The bundler rejects parent-of-project paths, so every reference must resolve under `videos/<slug>/`. The block expects these exact filenames in `assets/`:

```bash
# Brand mark
cp ../diy-yt-creator/public/assets/dynamous-logo.png \
   videos/<slug>/assets/dynamous-logo.png

# Cole portrait + community screenshots
cp ../diy-yt-creator/public/images/dynamous/cole-medin.webp \
   videos/<slug>/assets/dynamous-cole-medin.webp
cp ../diy-yt-creator/public/images/dynamous/events.png \
   videos/<slug>/assets/dynamous-events.png
cp ../diy-yt-creator/public/images/dynamous/feed.png \
   videos/<slug>/assets/dynamous-feed.png
cp ../diy-yt-creator/public/images/dynamous/social-proof/community-01.png \
   videos/<slug>/assets/dynamous-community-01.png
cp ../diy-yt-creator/public/images/dynamous/social-proof/workshop-01.png \
   videos/<slug>/assets/dynamous-workshop-01.png
```

PowerShell equivalents use `Copy-Item` with the same source/destination pairs.

### 3. Copy audio files into the video's `audio/` folder

```bash
cp ../diy-yt-creator/public/audio/shared/dynamous-midroll-v2.mp3 \
   videos/<slug>/audio/dynamous-midroll-v2.mp3
cp ../diy-yt-creator/public/audio/shared/midroll-transition-in.mp3 \
   videos/<slug>/audio/midroll-transition-in.mp3
cp ../diy-yt-creator/public/audio/shared/midroll-transition-out.mp3 \
   videos/<slug>/audio/midroll-transition-out.mp3
```

### 4. Pick the midroll start time

Place the block at a natural pause in the host script — typically halfway through the video. The narration pauses for ~31.5s, then resumes. `<midrollStart>` is the absolute time (in seconds) where the block enters.

### 5. Add the mount `<div>` to `videos/<slug>/index.html`

```html
<div id="dynamous-midroll-mount"
     data-composition-id="dynamous-midroll"
     data-composition-src="compositions/dynamous-midroll.html"
     data-start="<midrollStart>"
     data-duration="31.5"
     data-track-index="20"
     data-width="1920"
     data-height="1080"></div>
```

Pick a `data-track-index` that doesn't collide with narration (track 2), bg-music (track 3), or per-cue SFX (tracks 4+). Track 20 is the recommended default for sub-comp mounts.

### 6. Add the host-side mount CSS to `videos/<slug>/index.html`'s `<style>` block

The sub-composition needs absolute positioning + a high z-index so it overlays everything during the midroll window:

```css
#dynamous-midroll-mount {
  position: absolute;
  inset: 0;
  width: 1920px;
  height: 1080px;
  z-index: 50;
  pointer-events: none;
}
```

### 7. Wire the THREE host-level `<audio>` elements

Sub-compositions don't carry audio — `<audio>` lives at the host. Add these three elements to `index.html` (replace `<midrollStart>` with the same number from step 4):

```html
<!-- Midroll transition-in SFX — fires at midroll start -->
<audio id="midroll-sfx-in"
       src="audio/midroll-transition-in.mp3"
       data-start="<midrollStart>"
       data-duration="1.5"
       data-track-index="4"
       data-volume="0.20"></audio>

<!-- Midroll narration — starts 0.3s after midroll start (audio-offset) -->
<audio id="midroll-narration"
       src="audio/dynamous-midroll-v2.mp3"
       data-start="<midrollStart + 0.3>"
       data-duration="31.0"
       data-track-index="2"
       data-volume="1.0"></audio>

<!-- Midroll transition-out SFX — fires near the end of the outro -->
<audio id="midroll-sfx-out"
       src="audio/midroll-transition-out.mp3"
       data-start="<midrollStart + 30.5>"
       data-duration="1.5"
       data-track-index="4"
       data-volume="0.15"></audio>
```

> **Volumes are capped per `.claude/rules/audio-design.md`.** Narration sits at 1.0; the transition SFX sit at 0.20 / 0.15 (well under the 0.25 SFX cap). The Remotion source ran transitions at `0.5` / `0.4` — those exceeded the cap; we lower them here.

> **Track-index `2` is the host narration track.** During the midroll window (30s+) the host's main narration MUST NOT overlap. If your host narration runs continuously, gate it: split the host narration into pre-midroll and post-midroll segments and make the gap exactly cover `<midrollStart> .. <midrollStart + 31>`.

### 8. Pause / fade the host's bg-music during the midroll window

The midroll narration is dense. Drop bg-music down to ~0.04 across the midroll window (or split the bg-music segments around the gap):

```html
<!-- Example: a body bg-music segment that ends just before the midroll -->
<audio id="bg-music-body-pre"
       src="audio/bg-music-body.mp3"
       data-start="12"
       data-duration="<midrollStart - 12>"
       data-track-index="3"
       data-volume="0.07"></audio>

<!-- (no bg-music during the 31.5s midroll) -->

<!-- Body bg-music resumes after the midroll -->
<audio id="bg-music-body-post"
       src="audio/bg-music-body.mp3"
       data-start="<midrollStart + 31.5>"
       data-duration="..."
       data-track-index="3"
       data-volume="0.07"></audio>
```

### 9. Lint to verify

```bash
npx hyperframes lint videos/<slug>
```

Then preview to confirm sync:

```bash
npx hyperframes preview videos/<slug>
```

Scrub to `<midrollStart>` and watch the 31.5s window — every phase boundary should land within ~50ms of its anchor word.

## Slots to edit

The midroll ships **brand-locked verbatim**. There are no per-video slots. Every opted-in long-form video carries the same:

- **Narration audio** (`dynamous-midroll-v2.mp3`) — 30.98s, 69 words.
- **Stat number** (`1,000+`) — counted up over 1.2s starting at "thousand" word anchor.
- **Event cards** (Daily Hangouts / Debug Together LIVE / Weekly Workshops FEATURED).
- **Course names** (Agentic Coding / AI Agent Mastery / Second Brain Bootcamp).
- **Module lists** (18 agentic / 8 second-brain) — locked content from the Dynamous curriculum.
- **CTA stack** (Join the Community / Link in Description ↓ / 10% OFF / dynamous.ai).
- **Outro** ("Back to the video.").

If Cole rotates the discount code, update **only**:
- `[data-composition-id="dynamous-midroll"] #dm-cta-discount` text in `compositions/dynamous-midroll.html` if the percentage changes.
- The `<audio>` source if a new narration is recorded — and if so, regenerate `dynamous-midroll-v2-sync.json` and update the phase-end constants in the block's `<script>` (P1_END..P5_END) to match the new word ends.

## Don'ts

- **Don't change phase boundaries piecemeal.** They're anchored to specific word ends in the sync JSON. If you adjust one, recheck all six.
- **Don't use this block in Shorts (1080×1920).** Its layout and copy are designed for horizontal long-form. Shorts already have `dynamous-endcard` for the same purpose.
- **Don't run the SFX above 0.25.** The legacy Remotion source had `0.5` / `0.4` — those are illegal under `audio-design.md`. The block ships with corrected `0.20` / `0.15` defaults; do not raise.
- **Don't shorten `data-duration` below 31.5s.** The narration runs to 30.98s + the outro fade lands at 31.5s. Shorter and the audio gets cut off.
- **Don't extend `data-duration` past 31.5s.** The outro fade-to-transparent ends at 31.5s; extending leaves a silent dead frame the host doesn't expect.
- **Don't reference any path with `../../shared/...`.** The bundler rejects parent-of-project paths. Always copy first; the block uses `../assets/...` (one level up from `compositions/`, into `videos/<slug>/assets/`).
- **Don't add this block to `templates/long-form/standard/`.** Templates ship clean; the midroll is wired at video-spawn time when the author opts in.
- **Don't pair this block with a second long-form CTA** (e.g. an end-of-video subscribe banner reusing the CTA pill). Pick one promotion peak — viewer drop-off is highest when CTAs cluster.

## Lint expectations

```bash
npx hyperframes lint videos/<slug>
```

Expect 0 errors. Inspect:

```bash
npx hyperframes inspect videos/<slug>
```

The Cole portrait, scrolling lists, and CTA card should all render within the 1920×1080 frame without overflow during their respective phase windows.
