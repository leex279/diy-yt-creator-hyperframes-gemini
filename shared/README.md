# shared/

Repo-level assets shared across all videos and templates. Single source of truth — never copy these files into per-video `assets/` folders. Reference via relative path from the consumer:

| Consumer | Path to a logo |
|---|---|
| `videos/<slug>/index.html` | `../../shared/logos/<file>` |
| `templates/shorts/<style>/index.html` | `../../../shared/logos/<file>` |
| `templates/long-form/<style>/index.html` | `../../../shared/logos/<file>` |

HyperFrames lint accepts these cross-project relative paths — verified against `npx hyperframes lint`.

## Contents

### `logos/` — 84 brand wordmarks and icons

Real, production-quality logos (PNG and SVG). Use `*-light.svg` or `*-light.png` variants on dark backgrounds (the Anthropic-shorts template), and `*-dark` variants on light backgrounds (future light templates).

**Full alphabetized inventory with descriptions: [`ASSETS.md`](./ASSETS.md)** — auto-maintained by `scripts/sync-shared-assets.sh` (wired into the PostToolUse + SessionStart hooks). Run it manually any time with `bash scripts/sync-shared-assets.sh`.

**Common picks:**

| Family | Files |
|---|---|
| Anthropic / Claude | `anthropic-logo.png`, `anthropic-logo-light.svg`, `anthropic-logo-dark.svg`, `claude-logo-light.svg`, `claude-logo-dark.svg`, `claude-icon.svg`, `claude-code-logo-light.svg`, `claude-code-logo-dark.svg` |
| AI labs / models | `openai-logo.png`, `chatgpt-logo.svg`, `gemini-logo.svg`, `gemma-logo.png`, `mistral-logo.png`, `deepseek-logo.png`, `qwen-logo.png`, `kimi-logo.png`, `groq-logo.png`, `llama-cpp-logo.png`, `ollama-logo.png`, `huggingface-logo.png`, `unsloth-logo.png` |
| Dev tools / IDEs | `github-logo.svg`, `gitlab-logo.svg`, `gitea-logo.svg`, `vscode-logo.png`, `jetbrains-logo.png`, `cursor-logo.png`, `windsurf-logo.png`, `cline-logo.png`, `aider-logo.png`, `opencode-logo.png` |
| Cloud / infra | `aws-logo.png`, `cloudflare-logo.png`, `vercel-logo.png`, `docker-logo.png`, `nvidia-logo.png`, `amd-logo.png`, `datadog-logo.png`, `sentry-logo.png` |
| Productivity | `canva-logo.png`, `asana-logo.png`, `slack-logo.svg`, `discord-logo.svg`, `telegram-logo.svg`, `whatsapp-logo.svg` |
| Other | `apple-logo.png`, `google-logo.png`, `google-g-logo.png`, `microsoft-logo.png`, `chrome-logo.svg`, `android-logo.svg`, `ubuntu-logo.png`, `netflix-logo.png`, `salesforce-logo.png`, `stripe-logo.png`, `revolut-logo.png`, `wordpress-logo.png`, `n8n-logo.png`, `flask-logo.png`, `astro-logo.png`, `remotion-logo.png`, `block-logo.png`, `brilliant-logo.png`, `archon-logo.png`, `multica-logo.svg`, `openclaw-logo.png`, `earendil-logo.png`, `hostinger-logo.png`, `midjourney-logo.png`, `gitlab-logo.png`, `aisi-logo.svg`, `yc-logo.svg` |

Run `ls shared/logos | grep -i <brand>` to find a specific logo.

## Adding new logos

1. Drop the file into `shared/logos/`. Name it `<brand>-logo.<ext>` (kebab-case).
2. Prefer SVG for wordmarks (scales cleanly), PNG for complex marks.
3. If both light- and dark-stage variants are needed, ship both with `-light` / `-dark` suffixes.
4. Update this README's "Common picks" table if it's a major brand.

## Don'ts

- Don't copy logos into `videos/<slug>/assets/`. Reference from `shared/logos/` instead — single source of truth.
- Don't commit unlicensed logos. Brands must be either (a) used under their own brand-asset terms, or (b) used in a clearly editorial / commentary context covered by fair use.
- Don't replace a real logo with a styled-text fallback when the real one exists — see the `diy-yt-creator` skill's "Real logos" rule.
