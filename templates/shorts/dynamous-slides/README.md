# Dynamous-Slides Shorts Template

Vertical YouTube Short (1080×1920) port of `templates/long-form/dynamous-slides/`.

Deep-navy + Dynamous-Blue palette, Montserrat display + JetBrains Mono data, 300/800 weight-contrast signature. Same decorative stack as the long-form (ambient triple-radial breath, hairline grid, scattered Dynamous-icon shape backdrop, dual blue/cyan halo orbs, vignette, SVG film-grain), restaged for the vertical canvas.

## When to use

Companion Shorts for any long-form filmed in `templates/long-form/dynamous-slides/`. Default Dynamous-flavored vertical for community drops, daily-events recaps, workshop summaries, six-strategy explainers, anything where the long-form lived on the same deck.

## Aesthetic specifics

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#07090F` | Near-black with blue tint |
| `--accent` | `#3B82F6` | **Dynamous Blue** — hero color |
| `--accent-2` | `#60A5FA` | Dynamous Light — eyebrows, highlights |
| `--accent-3` | `#0EA5E9` | Dynamous Cyan — CTA glow |
| `--accent-dim` | `#1E40AF` | Deep halo |

Brand rules:

- Dynamous Blue is the hero. One or two focal elements per scene.
- **NO PURPLE.** Cyan or deep-halo for tertiary accents.
- Persistent `#bg-halo` (blue, top-right) and `#bg-halo-2` (cyan, bottom-left) do the brand atmosphere — per-scene glows stay subtle.

## Scene catalog

Default 80s composition. Operator retimes per video.

| # | File | Default window | Archetype |
|---|---|---|---|
| 1 | `scene-hook-wordmark.html` | 0–9s | Character-stagger wordmark + flame badge |
| 2 | `scene-headline-accent.html` | 9–19s | 300/800 weight contrast + blue accent sweep |
| 3 | `scene-big-stat.html` | 19–27s | Counter ramp + gradient text + receipt label |
| 4 | `scene-tension-pivot.html` | 27–35s | Strike-through pivot — light "NOT this" / 800 "THIS" |
| 5 | `scene-list-reveal.html` | 35–63s | 6 enumerated rows, step-by-step (~4.5s apart) |
| 6 | `scene-quote-card.html` | 63–70s | Line-by-line italic quote + author chip |
| 7 | `scene-cta.html` | 70–80s | Dynamous endcard — debate question + offerings + URL |

`flash: true` crossfade is enabled on two boundaries:
- big-stat → tension-pivot (hero pivot — the first emotional turn)
- quote-card → cta (CTA landing — settles instead of punches)

## Typography (vertical scale)

Per `.claude/rules/shorts-typography.md`, minimums respected:

| Role | Size | Notes |
|---|---|---|
| Hook wordmark | 180px | Hero slam, wraps to 2 lines as needed |
| Big stat number | 280px | Gradient-clipped |
| Big stat suffix | 160px | Solid Dynamous Light |
| Tension headline (bold) | 138px | The slam line |
| Tension headline (light) | 100px | The strike line |
| Headline-accent slam | 138px | 800 weight |
| Headline-accent light | 90px | 300 weight |
| List row label | 52px | Primary, 800 weight |
| List row descriptor | 32px | 400 weight |
| Quote body | 64px | 300 italic |
| CTA wordmark | 64px | Headline above debate |
| Debate question | 56px | The on-screen CTA |
| Offering label | 34px | Bold |
| Eyebrow (kicker) | 32–34px | Mono, uppercase |

## Spawning a new video

```bash
cp -r templates/shorts/dynamous-slides videos/<slug>
# Edit videos/<slug>/meta.json — set id + name
# Edit each compositions/scene-*.html — replace REPLACE: tokens with real copy
# Drop narration at videos/<slug>/audio/narration.wav (1-2min)
# Uncomment <audio id="narration"> + the 6 <audio id="sfx-whoosh-*"> blocks in index.html
# Sync SFX:
bash scripts/sync-video-sfx.sh videos/<slug>
# Lint:
npx hyperframes lint videos/<slug>
# Preview:
npx hyperframes preview videos/<slug>
```

## Voice (carry into copy)

The template ships with the Dynamous long-form voice expectations. When pairing with Cole-voice narration (per `brand-voices/cole-tone-of-voice.md`):

- **"Honestly"** and **"super"** show up. Use them.
- Direct address — say "you" often.
- Tell viewers what NOT to focus on.
- Numbers, not vague claims.
- One conviction per scene, max.
- "And here's the thing" / "But honestly" / "What NOT to focus on" are signature moves.

## Engagement CTA (MANDATORY)

The `#cta-question` element in `scene-cta.html` IS the on-screen engagement CTA. It MUST be replaced per video with a debate-sparking, polarizing, binary-answerable question that references a specific claim from the video. The same wording MUST appear:

- In the final 3-5s of the narration script (spoken)
- On the closing paragraph of `youtube-description.md`

See `.claude/rules/engagement-cta.md`.

## Final-frame thumbnail (MANDATORY)

The held CTA scene (last ~2-3s) IS the thumbnail-grade final frame per `.claude/rules/shorts-thumbnail-frames.md`. Required elements present in the bare template:

- ✓ Topic statement (the debate question, 56px)
- ✓ Visual anchor (Dynamous flame, 100×140px)
- ✓ Brand chrome (Dynamous wordmark + top-banner overlay)
- ✓ Outcome receipt (4 community offerings)
- ✓ CTA pill ("Link in Description ↓" + 10% OFF)

## Audio (operator wires per video)

- Narration: track 2, `data-volume="0.9"`
- Cinematic whoosh on every scene transition: track 3, `data-volume="0.11"`, `data-duration="1.5"`
- NO background music (per `.claude/rules/audio-design.md` Shorts hard rule)

SFX volume table is in `.claude/rules/audio-design.md`.

## What NOT to do

- Don't add purple anywhere. Cyan or deep-halo instead.
- Don't strip the flame mark from the CTA — it's the Dynamous brand seal.
- Don't reduce the wordmark below 160px on the hook scene — it loses scroll-stop power.
- Don't enable a flash transition on every boundary — two per video, max.
- Don't add background music.
- Don't ship without replacing every `REPLACE:` token in the scene HTML files.
