# Screenshots

Operators replace these placeholder images per video.

## Expected files (referenced by sub-compositions)

| File | Used by | Aspect | Notes |
|---|---|---|---|
| `hero-shot.png` | `compositions/scene-image-hero.html` | 1920x1080 (full bleed) | Full-bleed photo backdrop with dark gradient overlay |
| `source-1.png`, `source-2.png`, `source-3.png` | `compositions/scene-source-cards.html` | 16:9 (e.g. 1280x720) | Photo for the source-card row; one per card |
| `next-video-thumbnail.png` | `compositions/scene-cta.html` | 16:9 | Optional next-video thumbnail in the closing CTA |

## Placeholder behaviour

The template ships without these files. The compositions reference them with
`<img>` tags — `npx hyperframes lint` will warn (not error) about the missing
sources until the operator drops real images. After replacement, re-run lint
to confirm cleanly.

## Asset guidelines

- Keep source dimensions ≤ 3840x2160 (HyperFrames performance budget — see
  `hyperframes-cli` skill `docs performance`).
- Prefer PNG for screenshots with sharp text, JPG for photos.
- For full-bleed hero images, include a touch of negative space top + bottom so
  the gradient overlay has room to land.
