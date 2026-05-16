# Anthropic Shorts Template — Cinematic V3

Vertical YouTube Short (1080×1920, 30fps) in the **Anthropic dark-stage** aesthetic, built for HyperFrames (HTML + GSAP). The full design system lives in [DESIGN.md](./DESIGN.md).

## What this template ships

A 34-second, 6-phase reference composition (`index.html`) demonstrating every reusable archetype:

| # | Phase | Component | Window |
|---|---|---|---|
| 1 | Hook | Topic lockup → RGB-split hero slam | 0-6s |
| 2 | Terminal | Claude-CLI session with typed prompt + streaming output + status tags | 6-11s |
| 3 | Benchmark | 4-bar animated chart with count-ups + industry-leader marker | 11-16s |
| 4 | Code diff | Before/after panels with line-stagger + syntax highlighting | 16-21s |
| 5 | Timeline | SVG connector line + traveling playhead + 3 dated cards | 21-27s |
| 6 | Quote + CTA | Tweet-style social proof card + typewriter URL pill + word-stagger CTA | 27-34s |

**Persistent atmosphere:** cinematic chrome (REC dot, timecode, viewfinder corners, letterbox, phase ticks), particle constellation field (30 dots + connecting lines), token-stream edges, anamorphic lens flare, light-leak transitions, CSS film grain, soft-light scanlines.

## Files

| File | Purpose |
|---|---|
| `index.html` | The V3 composition. Edit text, colors, durations here |
| `preview.html` | HyperFrames player wrapper for local preview |
| `Anthropic Shorts V2.html` | V2 snapshot (kept for reference) |
| `DESIGN.md` | Full design system — component library, motion rules, color tokens, anti-patterns |
| `assets/` | Logo + Anthropic shape backdrop |
| `hyperframes.json`, `meta.json`, `sfx-cues.txt` | HyperFrames CLI config |

## Spawn a new video

```bash
SLUG="my-new-short"
cp -r templates/shorts/anthropic videos/$SLUG
# edit videos/$SLUG/index.html — text, durations, accent colors
npx hyperframes lint videos/$SLUG
npx hyperframes preview videos/$SLUG
npx hyperframes render videos/$SLUG -o out/$SLUG.mp4
```

## Customizing

### Text content (operator-fill)
- `#p1-topic-slam` — main topic phrase
- `#p1-hero` — slam word
- `#p1-ga-receipt` — `RECEIPT · DATE · COUNT` line
- Terminal lines `#p2-l1..7` — command output (keep `prompt` + `out` + `term-tag` structure)
- Benchmark `#p3-row-1..4` — labels + `data-pct` values + matching pcts in the timeline `benchRows` array
- Code diff `#p4-d1..4` / `#p4-a1..4` — before/after lines + `#p4-filename`
- Timeline `#p5-card-1..3` — dates + titles + subs
- Quote card avatar / name / handle / text / engagement counts (`countUp()` targets)
- `#p6-url-text` content set in the JS `URL_TEXT` constant
- `#p6-cta-question` words

### Reordering / trimming
Each phase is self-contained: `#phaseN` div in HTML + a block in the script (`P_N = phase_start_offset`). To remove a phase, delete the div + the script block + the transition tweens that target it; renumber subsequent phases and update the `phase-ticks` markup.

### Per-phase accent
Color rotation lives in CSS class names — `.tl-card.orange`, `.bench-fill.purple`, etc. Swap classes to recolor a row/card. The rule: no two adjacent phases share the same dominant accent.

### Durations
Each phase has a `data-duration` window implicit in the timeline timestamps (`P2`, `P3`, etc). Change the `T1..T5` constants in the script to shift transitions; remember to bump `#root` `data-duration` to match the new total.

## Adding narration

1. Drop `audio/narration.wav`
2. Uncomment the `<audio id="narration">` block at the bottom of `index.html` (template comment shows the exact attrs)
3. Sync the timeline transition timestamps to spoken-word landmarks (use `npx hyperframes transcribe`)

## Adding SFX

Default is `cinematic-whoosh` on each phase boundary, fired by the `fireLightLeak()` timing — i.e. `data-start = T - 0.4`. Per-cue SFX (impact-slam, scale-slam, etc.) are opt-in for specific moments. See [DESIGN.md "Audio / SFX cues"](./DESIGN.md#audio--sfx-cues).

## Don'ts

See `DESIGN.md` "What NOT to Do". The big ones:
- No light canvas
- No more than one accent per phase
- No serif headlines (Inter only)
- No `<br>` in content text — use `max-width`
- No `position: absolute; top: Npx` on `.phase-content` — use padding
- No SVG `data:image/svg+xml` grain (taints html2canvas) — use the included CSS `#grain`
- Don't push cinematic chrome above 0.85 opacity — it should frame the content, not compete with it
