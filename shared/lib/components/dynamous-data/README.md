# Component: dynamous-data

Canonical Dynamous AI Mastery curriculum + brand strings — the single source of truth used by all four Dynamous-promotion artifacts (badge, endcard, module interstitial, discount bubble).

## What this is

`dynamous-modules.json` — the verbatim 12-module curriculum (id, title, lessons, time, color, keywords) plus the `url`, `tagline`, `discountText`, `ctaHeadline`, and `ctaButton` brand strings.

**SOURCE**: `diy-yt-creator/src/shared/components/DynamousMidroll.tsx:134-147` (modules) + the Dynamous Circle product page (URL + tagline + discount).

The keywords array on each module is inferred from the title and is used by `scripts/find-dynamous-module.js` to score topic-match candidates. Do NOT alter module IDs, titles, or `lessons` / `time` fields without verifying against the live Dynamous platform.

## How to consume

Two patterns. Pick whichever fits the artifact:

### Pattern A — bake the picked module into HTML at authoring time (DEFAULT)

Most artifacts only need a single matching module name baked into the HTML. The author runs the helper before writing the recipe slot:

```bash
node scripts/find-dynamous-module.js "mcp" "tool"
# → "MODULE 10 — MCP Servers + Skills"
```

Then pastes that string into the endcard or interstitial slot in the host video. The runtime never reads the JSON file.

### Pattern B — copy the JSON into the video (rare)

If a video genuinely needs to look up modules at composition load (e.g. a custom interstitial that branches on a module ID), copy the JSON in:

```bash
cp shared/lib/components/dynamous-data/dynamous-modules.json videos/<slug>/assets/dynamous-modules.json
```

…and load it via a `fetch('assets/dynamous-modules.json')` from a `<script>` block. Note: the HyperFrames runtime is deterministic + synchronous; if you go this path, do the fetch BEFORE timeline construction and resolve before any `gsap.timeline()` call. Most videos should use Pattern A.

## Module-matching helper

A 30-line CLI helper lives at `scripts/find-dynamous-module.js`. It takes topic-tag arguments, lowercases them, scores each module by keyword overlap, and prints the best match (or `NO_MATCH` if nothing scores > 0):

```bash
node scripts/find-dynamous-module.js "claude code" "subagent" "delegation"
# → "MODULE 11 — Subagents"

node scripts/find-dynamous-module.js "totally unrelated topic"
# → "NO_MATCH"
```

The algorithm mirrors `findMatchingModule()` in `diy-yt-creator/src/shared/constants/dynamous.ts`.

## Don'ts

- **Don't run `find-dynamous-module.js` at composition render time.** The HyperFrames runtime is deterministic + synchronous — picking a module *during* render couples the rendered output to JSON content and makes diffs harder to review. Pick the module *before* writing the HTML slot, and bake the result as plain text.
- **Don't add or remove modules without confirming the live Dynamous platform.** This file is the canonical mirror; if the platform changes, update this file in a dedicated PR.
- **Don't translate or paraphrase module titles.** They are brand-owned strings — copy verbatim.
