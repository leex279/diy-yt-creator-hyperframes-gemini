# diy-yt-creator-hyperframes

A multi-video [HyperFrames](https://hyperframes.heygen.com) workspace. Each video is a self-contained HTML + GSAP composition under `videos/`. New videos are spawned by copying a template from `templates/`.

## Layout

```
.
├── videos/                                 # one self-contained HyperFrames project per video
│   └── claude-connectors-everyday-life/    # the first video (60s anthropic dark-stage short)
├── templates/                              # copyable starter projects
│   ├── shorts/
│   │   └── anthropic/                      # 1080x1920 dark-stage (Inter + JetBrains Mono)
│   └── long-form/                          # 1920x1080 — no templates yet
├── shared/                                 # repo-level assets shared across all videos
│   └── logos/                              # 84 brand wordmarks (Anthropic, Claude, OpenAI, …)
├── CLAUDE.md                               # AI agent guidance (skills, commands, structure)
├── AGENTS.md                               # general agent setup notes
└── skills-lock.json                        # HyperFrames skill versions
```

## Quick start — preview an existing video

```bash
npx hyperframes preview videos/claude-connectors-everyday-life
```

Open the studio URL it prints. Hot-reload on save.

## Quick start — render an existing video

```bash
npx hyperframes render videos/claude-connectors-everyday-life \
  -o videos/claude-connectors-everyday-life/out/short.mp4
```

`out/` is gitignored.

## Spawn a new video

```bash
# Pick a kebab-case slug
SLUG="my-new-short"

# Copy the template you want
cp -r templates/shorts/anthropic videos/$SLUG

# Update meta + design
$EDITOR videos/$SLUG/meta.json
$EDITOR videos/$SLUG/DESIGN.md
$EDITOR videos/$SLUG/index.html

# Validate
npx hyperframes lint videos/$SLUG
npx hyperframes inspect videos/$SLUG

# Iterate
npx hyperframes preview videos/$SLUG

# Ship
npx hyperframes render videos/$SLUG -o videos/$SLUG/out/short.mp4
```

PowerShell equivalent for the copy: `Copy-Item -Recurse templates/shorts/anthropic videos/$SLUG`.

## Templates

| Template | Format | Resolution | Aesthetic |
|---|---|---|---|
| `templates/shorts/anthropic/` | YouTube Shorts | 1080x1920, 30fps | Dark stage, Inter + JetBrains Mono, Claude orange + 4-accent rotation. Lifted from the `AnthropicPostmortemShort` Remotion source. |
| `templates/long-form/` | Long-form | 1920x1080 | _none yet_ |

Each template ships with its own `README.md` (spawn instructions) and `DESIGN.md` (full design system spec).

## Add a new template

1. Pick the format folder: `templates/shorts/` for vertical, `templates/long-form/` for horizontal.
2. Create a sub-folder named after the aesthetic (e.g. `templates/shorts/swiss-pulse/`).
3. Mirror the structure of `templates/shorts/anthropic/`: `index.html`, `meta.json`, `hyperframes.json`, `DESIGN.md`, `README.md`, `audio/`, `assets/`, `compositions/`.
4. Run `/hyperframes` (skill) before authoring the composition.
5. `npx hyperframes lint templates/<format>/<style>` must pass clean.

## Documentation

- [`CLAUDE.md`](./CLAUDE.md) — agent guidance, skills, commands, key rules
- [`AGENTS.md`](./AGENTS.md) — general agent setup
- HyperFrames CLI: `npx hyperframes docs <topic>` (topics: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`)
- Full HyperFrames docs index: <https://hyperframes.heygen.com/llms.txt>
