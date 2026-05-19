# Next steps — `scaling-ai-coding-complex-codebases-short`

## Status

- ✅ Template `templates/shorts/dynamous-slides/` shipped (0 errors, 0 layout issues, 70 text elements pass WCAG AA)
- ✅ Video composition built and lint-clean (0 errors, 0 layout issues, 66 text elements pass WCAG AA)
- ✅ Cole-voice narration generated via ElevenLabs (`.env.cole`, `pcm_24000` Creator-tier): 66.73s, 191 words
- ✅ Composition retimed to transcript word-anchors — every scene starts on its narration anchor word
- ✅ Narration `<audio>` + 6 whoosh SFX wired and synced
- ✅ Werbung disclosure badge on CTA scene (UWG §5a compliance)
- ✅ Engagement CTA in 3 mandatory locations (script.txt, `#cta-question`, youtube-description.md)
- ✅ `youtube-description.md` written per canonical structure

## Anchor map (transcript-driven)

| Scene | Anchor word | Start (s) | Duration (s) |
|---|---|---|---|
| `scene-hook-wordmark` | "Vibe" | 0.00 | 6.40 |
| `scene-headline-accent` | "Cole" | 6.40 | 8.45 |
| `scene-big-stat` | "Ninety" | 14.85 | 6.56 |
| `scene-tension-pivot` | "File" | 21.41 | 6.02 |
| `scene-list-reveal` | "Six strategies" | 27.43 | 23.28 |
| `scene-quote-card` | "most precious" | 50.71 | 5.99 |
| `scene-cta` | "So" | 56.70 | 11.30 |

List-reveal row entrances (scene-relative):

| Row | Anchor word | Scene-rel (s) |
|---|---|---|
| r1 — Vertical slices | "vertical" | 2.07 |
| r2 — Brownfield day one | "brownfield" | 5.77 |
| r3 — Three-tier context | "Three" | 9.31 |
| r4 — Focused priming | "focused" | 13.60 |
| r5 — Parallel worktrees | "parallel" | 16.78 |
| r6 — Coupling over lines | "size" | 20.54 |

Total composition: 68s (narration 66.73s + 1.27s held-frame CTA tail).

## Remaining

1. **Scrub preview** — verify scene boundaries land cleanly on narration:
   ```bash
   npx hyperframes preview videos/scaling-ai-coding-complex-codebases-short
   ```

2. **Render** (only after preview looks good):
   ```bash
   npx hyperframes render videos/scaling-ai-coding-complex-codebases-short -o out/scaling-ai-coding-complex-codebases-short.mp4
   ```
   Output lands at `videos/<slug>/out/<slug>.mp4` per memory rule.

3. **(Optional) Speedup pass** — if 68s feels too slow for the Shorts audience, apply ffmpeg per `.claude/rules/video-speedup.md`. Update youtube-description.md chapters automatically (memory rule — but Shorts have no chapters, so it's a no-op).
