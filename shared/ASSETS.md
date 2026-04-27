<!--
  AUTO-MAINTAINED — do not delete the table boundary HTML comments
  further down (the literal sentinel strings ASSETS-COLON-BEGIN and
  ASSETS-COLON-END inside HTML comments).

  scripts/sync-shared-assets.sh runs on every PostToolUse hook.
  Workflow:
    - Walks shared/ for non-md, non-dotfile assets
    - Appends new files between the markers with blank descriptions
    - Marks files removed from disk with [REMOVED] in the description
    - Preserves your edits to existing rows
-->

# shared/ — Asset Inventory

Single source of truth for what's in `shared/` and what each asset is for. Auto-synced by `scripts/sync-shared-assets.sh` on every Write / Edit / Bash via the PostToolUse hook.

**Conventions:**
- File paths are relative to `shared/` (so `logos/anthropic-logo-light.svg`, not the full repo path).
- "Use for" should describe the brand / product / context — not the file format.
- Light/dark variants: `*-light` for dark-stage videos (Anthropic shorts template), `*-dark` for light-stage videos.
- Leave description blank only as a last resort. Future-Claude will not know what `multica` is.

## Logos

<!-- ASSETS:BEGIN -->
| File | Category | Use for |
|---|---|---|
| logos/aider-logo.png | AI coding | Aider — terminal-based AI pair programmer |
| logos/aisi-logo.svg | AI safety | _TBD_ (UK AI Safety Institute? — please confirm) |
| logos/amd-logo.svg | Hardware | AMD — chipmaker (CPUs, GPUs) |
| logos/android-logo.svg | Platform | Android operating system |
| logos/anthropic-logo-dark.svg | AI lab | Anthropic wordmark — dark variant (use on light canvases) |
| logos/anthropic-logo-light.svg | AI lab | Anthropic wordmark — light variant (use on dark canvases — Anthropic shorts default) |
| logos/anthropic-logo.png | AI lab | Anthropic wordmark — PNG fallback |
| logos/apple-logo.png | Brand | Apple |
| logos/archon-logo.png | Project | _TBD_ (Archon — please confirm: user's own project? open-source tool?) |
| logos/asana-logo.png | Productivity | Asana — project / task management |
| logos/astro-logo.png | Web framework | Astro — static-site generator / web framework |
| logos/atlassian-logo.png | Brand | Atlassian — Jira / Confluence parent |
| logos/aws-logo.png | Cloud | Amazon Web Services |
| logos/block-logo.png | Fintech | Block — formerly Square (Cash App, Tidal, etc.) |
| logos/brilliant-logo.png | EdTech | Brilliant.org — interactive STEM learning |
| logos/canva-logo.png | Design | Canva — design / decks / social graphics |
| logos/chatgpt-logo.svg | AI product | ChatGPT (OpenAI consumer product) |
| logos/chrome-logo.svg | Browser | Google Chrome |
| logos/claude-code-logo-dark.svg | AI coding | Claude Code wordmark — dark variant |
| logos/claude-code-logo-light.svg | AI coding | Claude Code wordmark — light variant |
| logos/claude-icon.svg | AI product | Claude icon (square mark, not full wordmark) |
| logos/claude-logo-dark.svg | AI product | Claude wordmark — dark variant |
| logos/claude-logo-light.svg | AI product | Claude wordmark — light variant |
| logos/cline-logo.png | AI coding | Cline — autonomous AI coding agent (VS Code extension) |
| logos/cloudflare-logo-color.png | Cloud | Cloudflare — color/orange variant |
| logos/cloudflare-logo-white.png | Cloud | Cloudflare — white variant (for dark canvases) |
| logos/cloudflare-logo.png | Cloud | Cloudflare — default variant |
| logos/cursor-logo.png | AI coding | Cursor — AI-first IDE (VS Code fork) |
| logos/datadog-logo.png | Observability | Datadog — APM / monitoring / logs |
| logos/deepseek-logo.png | AI lab | DeepSeek — Chinese AI lab (DeepSeek-V3, R1) |
| logos/discord-logo.svg | Communication | Discord |
| logos/docker-logo-inverted.png | DevOps | Docker — inverted variant |
| logos/docker-logo.png | DevOps | Docker — default variant |
| logos/earendil-logo.png | Project | _TBD_ (Eärendil — please confirm) |
| logos/flask-logo.png | Web framework | Flask — Python web microframework |
| logos/gemini-logo.svg | AI product | Google Gemini |
| logos/gemma-logo.png | AI model | Google Gemma — open-weight model family |
| logos/gitea-logo.png | DevOps | Gitea — self-hosted git service |
| logos/gitea-logo.svg | DevOps | Gitea — vector |
| logos/github-logo.svg | DevOps | GitHub |
| logos/gitlab-logo.png | DevOps | GitLab |
| logos/gitlab-logo.svg | DevOps | GitLab — vector |
| logos/google-g-logo.png | Brand | Google "G" mark only |
| logos/google-logo.png | Brand | Google full wordmark |
| logos/groq-logo.png | Hardware / inference | Groq — LPU inference provider |
| logos/hostinger-logo.png | Hosting | Hostinger — web hosting |
| logos/huggingface-logo.png | AI infrastructure | Hugging Face — model hub |
| logos/jetbrains-logo.png | DevTools | JetBrains — IntelliJ / PyCharm / WebStorm parent |
| logos/jinja-logo.png | Templating | Jinja — Python templating engine |
| logos/kimi-logo.png | AI product | Kimi — Moonshot AI's chatbot |
| logos/llama-cpp-logo.png | AI infrastructure | llama.cpp — local LLM inference |
| logos/microsoft-logo.png | Brand | Microsoft |
| logos/midjourney-logo.png | AI product | Midjourney — AI image generation |
| logos/mistral-logo.png | AI lab | Mistral AI — French AI lab (Mistral, Mixtral) |
| logos/multica-logo.png | Project | _TBD_ (Multica — please confirm) |
| logos/multica-logo.svg | Project | _TBD_ (Multica — vector — please confirm) |
| logos/n8n-logo-fallback.png | Automation | n8n — workflow automation (fallback variant) |
| logos/n8n-logo.png | Automation | n8n — workflow automation |
| logos/netflix-logo.png | Brand | Netflix |
| logos/nvidia-logo.png | Hardware | Nvidia — GPUs / CUDA |
| logos/ollama-logo.png | AI infrastructure | Ollama — local LLM runner |
| logos/onyx-logo.png | Project | _TBD_ (Onyx — please confirm: Onyx enterprise search? Other?) |
| logos/openai-logo.png | AI lab | OpenAI |
| logos/openclaw-logo-text.svg | Project | _TBD_ (Openclaw — text variant — please confirm) |
| logos/openclaw-logo.png | Project | _TBD_ (Openclaw — please confirm) |
| logos/opencode-logo.png | AI coding | OpenCode — open-source AI coding agent |
| logos/qwen-logo.png | AI model | Qwen — Alibaba's open-weight model family |
| logos/remotion-logo.png | Video framework | Remotion — React-based programmatic video |
| logos/revolut-logo.png | Fintech | Revolut |
| logos/salesforce-logo.png | SaaS | Salesforce — CRM |
| logos/sentry-logo.png | Observability | Sentry — error tracking |
| logos/slack-logo.svg | Communication | Slack |
| logos/stripe-logo.png | Fintech | Stripe — payments |
| logos/telegram-logo.svg | Communication | Telegram |
| logos/ubuntu-logo-orange.svg | OS | Ubuntu — orange variant |
| logos/ubuntu-logo.png | OS | Ubuntu Linux |
| logos/unsloth-logo.png | AI infrastructure | Unsloth — fast LLM fine-tuning library |
| logos/vercel-logo.png | Hosting | Vercel — Next.js hosting / deployments |
| logos/vscode-logo.png | DevTools | Visual Studio Code |
| logos/whatsapp-logo.svg | Communication | WhatsApp |
| logos/windsurf-logo.png | AI coding | Windsurf — Codeium's AI-first IDE |
| logos/wordpress-logo.png | CMS | WordPress |
| logos/yc-logo.png | Brand | Y Combinator |
| logos/yc-logo.svg | Brand | Y Combinator — vector |
<!-- ASSETS:END -->

## Adding a new asset manually

1. Drop the file into the appropriate `shared/<category>/` folder.
2. Either:
   - Wait for the PostToolUse hook to fire on the next Claude action (it will append a row with blank description), OR
   - Run `bash scripts/sync-shared-assets.sh` directly to update right now.
3. Edit the row's "Use for" column with a real description.

## When the script flags a missing file

If a row has `[REMOVED]` in the description column, the file no longer exists in `shared/`. Either restore the file or delete the row.
