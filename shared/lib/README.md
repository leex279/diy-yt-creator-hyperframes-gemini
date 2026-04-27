# shared/lib/

Generic, reusable HyperFrames building blocks — cards, effects, animations, palettes, named visual styles. Authored once here, **copied into a video at authoring time**, never referenced at runtime.

## Why copy, not reference?

HyperFrames' bundler and preview server actively reject filesystem paths that escape a project's directory (`isSafePath` / `safePath` in `@hyperframes/core`). A `data-composition-src="../../shared/lib/blocks/foo.html"` will:

- pass `npx hyperframes lint` silently (no rule checks the path)
- 404 in `npx hyperframes preview` (the studio server's `<base href>` is scoped to the project)
- render an empty `<div>` in `npx hyperframes render` (the bundler logs `[Bundler] Composition file not found:` and continues)

So **never** point any runtime attribute (`data-composition-src`, `<img src>`, `<audio src>`, `<video src>`, `<link href>`, `<script src>`) at `../../shared/lib/...`. Copy the file into `videos/<slug>/` first, then reference the local copy.

## Kinds

| Kind             | Path                                          | What it is                                                      | How to consume                                                                                                |
| ---------------- | --------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `tokens/`        | `shared/lib/tokens/<name>.css`                | `:root` CSS variable sets (palette + spacing + typography vars) | Copy into `videos/<slug>/tokens/<name>.css`, link via `<link rel="stylesheet" href="tokens/<name>.css">`.    |
| `blocks/`        | `shared/lib/blocks/<name>/block.html`         | Standalone sub-composition (own `<template>`, GSAP timeline)   | Copy `block.html` to `videos/<slug>/compositions/<name>.html`. Wire via `data-composition-src` in host HTML. |
| `components/`    | `shared/lib/components/<name>/component.html` | Paste-in HTML+CSS+JS snippet (no own dimensions or timeline)   | Read the file; merge its HTML into the host's composition `<div>`, CSS into the host `<style>`, JS into host `<script>`. |
| `effects/`       | `shared/lib/effects/<name>.js`                | Pure GSAP recipe — a function you call against a timeline       | Read the file; paste the function body into the host `<script>` and call it from the timeline.               |
| `visual-styles/` | `shared/lib/visual-styles/<name>.md`          | Named-style fragment (palette + typography + motion + lib picks) | Read in the diy-yt-creator playbook to pick lib entries that match a style. Reference from `videos/<slug>/DESIGN.md`. |

## Discovery

Read [`MANIFEST.md`](./MANIFEST.md). It's auto-maintained by `scripts/sync-shared-lib.sh` (wired into the `.claude/settings.json` PostToolUse + SessionStart hooks). Run manually any time:

```bash
bash scripts/sync-shared-lib.sh
```

Each entry's row in `MANIFEST.md` carries a one-line description, tags, and the path you copy from.

## Adding a new entry

1. **Pick the kind** (tokens / blocks / components / effects / visual-styles).
2. **Create the directory or file** following the naming convention below.
3. **Add a top-of-file comment** naming the source if you extracted from a template (e.g. `<!-- SOURCE: templates/shorts/anthropic/index.html:203-241 -->`).
4. **For blocks and components**, add a sibling `recipe.md` explaining wiring, slots, dependencies, and any gotchas.
5. The next agent tool-use triggers `sync-shared-lib.sh`, which appends the entry to `MANIFEST.md` with a `_TBD_` description for you to fill in.

## Naming conventions

- Directories and files: `kebab-case`.
- Block / component IDs: match the directory name (e.g. `blocks/stat-pill-row/` → `data-composition-id="stat-pill-row"`).
- Effect filenames: `<verb>-<noun>.js` (`hero-slam-shake.js`, `phase-crossfade.js`).
- Visual-style filenames: `<descriptor>.md` (`anthropic-dark.md`, `swiss-pulse.md`).
- Token filenames: same descriptor as the matching visual-style (`anthropic-dark.css` ↔ `anthropic-dark.md`).

## Don'ts

- Don't reference `shared/lib/` from `data-composition-src`, `<img src>`, `<audio src>`, `<video src>`, `<link href>`, or `<script src>` at runtime. Copy the file in.
- Don't edit `MANIFEST.md` directly between the sentinel comments — `sync-shared-lib.sh` will overwrite. Edit row metadata (description, tags) anywhere outside or use the script's preservation behavior.
- Don't put project-specific content here — `shared/lib/` is for generic ingredients. If something is unique to one aesthetic and unlikely to be reused, it belongs in a template's `index.html` or a video's local files.
- Don't introduce non-deterministic logic (`Math.random()`, `Date.now()`, network fetches, `setTimeout` in timeline construction) — HyperFrames is deterministic and the hyperframes skill enforces this.
- Don't use `repeat: -1` in any tween — calculate finite repeat counts from composition duration.
