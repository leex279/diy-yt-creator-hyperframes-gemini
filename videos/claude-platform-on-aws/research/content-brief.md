# Content Brief: Claude Platform on AWS

## Video Metadata

- **Slug**: `claude-platform-on-aws`
- **Template**: shorts/anthropic
- **Duration**: 90-120s (vertical YouTube Short, 1080×1920)
- **Tone**: Confident, technical, "look at what just shipped" news-explainer with developer authority
- **Voice Profile**: `voice_profile: news-explainer` — picked in Step 0E (URL is a vendor blog post / product announcement; topic mentions "now generally available"). Phase 2 will read `.claude/references/brand-voice-news-explainer.md`.
- **Target Audience**: Primary — developers and platform engineers building AI agents on AWS who use IAM/CloudTrail every day. Secondary — engineering managers and architecture decision-makers evaluating Claude on Bedrock vs other enterprise routes.
- **Key Angle**: For the first time, the FULL native Claude Platform (every beta, every console feature, every new model on day one) ships through your AWS account — not just the Bedrock subset. This is a structurally different product than "Claude on Bedrock," and it lands the same day as features go live on Anthropic's own API.
- **Topic Type**: PRODUCT_TOOL (announcement of a new managed service)
- **Research Depth**: STANDARD (90-120s short, 5 sources, 3 alternatives, 3 angles)

---

## Thesis

**Claude Platform on AWS is not a rebrand of Claude on Bedrock — it's Anthropic's API operating outside the AWS data boundary, billed through AWS, and the only way enterprise teams get Claude Managed Agents, Skills, Advisor, and every future beta from day zero without leaving their IAM perimeter.**

This is falsifiable: if the new service were just a Bedrock alias, the feature matrix would match; it doesn't (Managed Agents, Advisor, Files, Skills, MCP connector, Code execution, Console — all ship on Platform-on-AWS today; Bedrock is still the data-resident subset).

---

## Receipts

1. https://claude.com/blog/claude-platform-on-aws — May 11, 2026 — Anthropic's announcement post, GA notice, full feature list, customer quotes (ReliaQuest, OpenRouter, Emergent), model availability (Opus 4.7, Sonnet 4.6, Haiku 4.5).
2. https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ — May 11, 2026 — AWS technical post: IAM SigV4 auth, regional endpoint format `https://aws-external-anthropic.<REGION>.api.aws`, 17 AWS regions listed, AWS Marketplace billing, CloudTrail logging.
3. https://aws.amazon.com/about-aws/whats-new/2026/05/claude-platform-aws/ — May 11, 2026 — GA "What's New" announcement, confirms general availability.
4. https://aws.amazon.com/claude-platform/ — May 2026 — Official AWS landing page for the service.
5. https://claude.com/blog/new-in-claude-managed-agents — May 6, 2026 — Companion drop: Managed Agents dreaming + outcomes + multiagent orchestration; provides upstream feature context for why "full Platform on AWS" matters now.
6. https://www.anthropic.com/news/anthropic-amazon-compute — Anthropic + Amazon 5GW capacity expansion: up to 5 gigawatts AWS Trainium2/Trainium3 capacity, $100B over ten years, Project Rainier (~half a million Trainium2 chips).
7. https://aws.amazon.com/bedrock/agentcore/ — Amazon Bedrock AgentCore GA (October 13, 2025) — VPC, PrivateLink, CloudFormation, session isolation; the agent-deployment substrate teams already know.
8. https://dev.classmethod.jp/en/articles/claude-platform-on-aws-bedrock-differences/ — Third-party differences analysis between Claude Platform on AWS and Claude on Bedrock (data boundary, feature parity, billing).

---

## Core Value Proposition

Claude Platform on AWS helps AWS-centric developers get full native Claude API access (every beta, every console feature, day-one new models) by routing requests through AWS IAM, CloudTrail, and Marketplace billing — without leaving their existing AWS operating model.

---

## Target Audience

**Primary**: Developers and platform engineers at AWS-committed companies who want Claude's newest agent features (Managed Agents, Skills, Advisor, MCP connector) the day they ship — but can't sign a separate Anthropic contract or rotate to a new credential system.

**Secondary**: Architecture decision-makers evaluating "Bedrock vs native Anthropic vs Vertex Claude" and the AI-platform team running enterprise governance on top of AWS Organizations.

**What they know**: AWS IAM, CloudTrail, Marketplace billing, Bedrock's model catalog, what "private offer" means. Probably already shipping a Claude-powered agent through Bedrock today. Knows Claude Code, Sonnet 4.6, has heard of Managed Agents.

**What they care about**: Day-one access to new betas (most painful gap with Bedrock historically). Existing IAM + audit posture. Commitment retirement against AWS spend. NOT wanting to manage two billing relationships. Knowing when to pick Platform-on-AWS vs Bedrock (data residency).

---

## Pain Points

1. **Bedrock feature lag**: Claude features ship on the native API first, then trickle to Bedrock weeks or months later. Teams committed to AWS billing have been getting a stale Claude. [VISUAL: HIGH — split-screen timeline of native-vs-Bedrock release dates]
2. **Two-contract overhead**: Wanting native Claude features but already locked into AWS spend means a second invoice, a second SSO config, a second audit trail. Procurement says no. [VISUAL: HIGH — diagram of dual-credential / dual-invoice friction]
3. **No console = no fast iteration**: Bedrock has no equivalent of Anthropic's prompt improver / generator / evals; teams iterate in chat windows or build their own tooling. [VISUAL: MEDIUM — screenshot of Claude Console missing from Bedrock workflow]
4. **Managed Agents fragmentation**: New agent capabilities (dreaming, outcomes, multiagent orchestration, Skills, Advisor) all live on the native API. Bedrock-only teams can't ship them without a second integration. [VISUAL: HIGH — pill row showing locked features]
5. **Commitment-retirement anxiety**: Spending money on Claude outside AWS means it doesn't count toward your AWS commitment / EDP. Finance hates it. [VISUAL: MEDIUM — counter graphic showing dollars NOT retiring]

---

## Key Features & Benefits

| Feature | Benefit (user-facing) | Differentiator? | Metric | Visual Potential | Demo? |
|---------|----------------------|-----------------|--------|-----------------|-------|
| Same-day feature parity with native Claude API | New betas land on AWS the day they ship on api.anthropic.com | Yes — vs Bedrock weeks-of-lag | "Same day" | HIGH | Yes — timeline graphic |
| Claude Managed Agents (beta) | Build + deploy agents at scale through one API | Yes — was Anthropic-direct only | beta GA today | HIGH | Yes — agent flow diagram |
| Advisor strategy (beta) | Boost agent intelligence by consulting an advisor model | Yes | beta | MEDIUM | Yes — split-brain visual |
| AWS IAM + SigV4 auth | Use existing AWS credentials and IAM policies | Yes — Bedrock has it too, but native Anthropic API does not | "AWS Signature v4" | MEDIUM | Yes — code snippet |
| CloudTrail audit logging | Every Claude API call is a CloudTrail event | Yes — vs separate Anthropic audit | "Management + data events" | MEDIUM | Yes — log line |
| AWS Marketplace billing | Single AWS invoice, retires against commitments | Yes — first time for native Claude API | "consumption-based" | HIGH | Yes — invoice mockup |
| Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 | All current Claude models | No — also on Bedrock and native | model IDs | HIGH | Yes — model row |
| Web search + web fetch tools | Augment Claude with current web data | No (on native too) | beta | LOW | No |
| Code execution (Python) | Run Python and visualize data within an API call | Partial — Bedrock subset | beta | MEDIUM | Yes — code render |
| Files API (beta) | Upload + reference documents across conversations | Yes — Bedrock lacks | beta | MEDIUM | No |
| Skills (beta) | Teach Claude best practices via versioned artifacts | Yes — native-only previously | beta | MEDIUM | Yes — skill name pill |
| MCP connector (beta) | Connect to any remote MCP server, no client code | Yes — first on AWS | beta | MEDIUM | No |
| Prompt caching | Cut input cost up to 90% on repeated context | No — also Bedrock | "up to 90%" | HIGH | Yes — counter |
| Citations | Ground responses in source docs | No | beta | LOW | No |
| Batch processing | 50% discount, async, high-volume | No — also Bedrock | "50% off" | MEDIUM | Yes — discount pill |
| Claude Console access | Prompt improver, generator, evals UI | Yes — never on AWS before | new | HIGH | Yes — console screenshot |
| 17 AWS regions at launch | Coverage in US, Canada, EU, APAC, SA | Yes — broad day-one | "17 regions" | HIGH | Yes — region map |

---

## Proof Points (Scene-Ready)

| Stat/Claim | Formatted Value | Comparison Baseline | Source URL | Visual Format | Shock Factor |
|-----------|----------------|-------------------|-----------|--------------|-------------|
| Full Claude Platform features ship same-day on AWS | "Day-zero parity" | vs Bedrock weeks-of-lag | https://claude.com/blog/claude-platform-on-aws | timeline | 8/10 |
| Available in 17 AWS regions at GA | "17 regions" | vs typical "1-2 regions" launches | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ | world map | 7/10 |
| Models: Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 | "3 models" | full lineup | https://claude.com/blog/claude-platform-on-aws | model-pill row | 6/10 |
| Anthropic-Amazon compute deal: up to 5GW, $100B over 10 years | "5 GW / $100B" | hyperscaler-scale infra | https://www.anthropic.com/news/anthropic-amazon-compute | counter slam | 9/10 |
| Project Rainier: nearly 500,000 Trainium2 chips | "~500K Trainium2" | one of the world's largest AI clusters | https://www.anthropic.com/news/anthropic-amazon-compute | chip-grid | 9/10 |
| Authentication via AWS Signature Version 4 (IAM) | "IAM SigV4" | no extra credential system | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ | code snippet | 6/10 |
| Endpoint: `https://aws-external-anthropic.<REGION>.api.aws` | endpoint string | familiar AWS DNS shape | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ | mono URL pill | 5/10 |
| ReliaQuest (cybersecurity), OpenRouter, Emergent named as launch customers | "3 customers named" | beta testers public | https://claude.com/blog/claude-platform-on-aws | logo row | 7/10 |
| Pricing parity: Sonnet 4.6 $3/$15 per million tokens — same on Bedrock and native | "$3 in / $15 out" | parity, no AWS premium beyond regional 10% | https://benchlm.ai/blog/posts/claude-api-pricing | price-pill | 6/10 |

---

## Visual Concepts

1. **The "two paths" split**: Vertical canvas with a left column labeled "Claude on Bedrock" (data inside AWS) and a right column labeled "Claude Platform on AWS" (full Platform features). Items drop into each column step-by-step revealing the gap. Anthropic dark stage, accent color highlights the new path on the right.
2. **Feature parity timeline**: A horizontal timeline (rotated into vertical-friendly columns) of recent Claude features (Skills, Managed Agents, Dreaming, MCP connector). Two dots per feature: "ships on native" vs "ships on AWS Platform." On Platform-on-AWS, both dots align — the dramatic visual is that the AWS-side dots used to be weeks later and now sit on the same vertical line.
3. **17 region map slam**: Vertical-cropped world map with the 17 AWS regions popping in as accent dots, then collapsing into a "17" counter. The shock factor is "more regions than most Claude routes."
4. **Endpoint reveal**: A mono-font URL string typed out character-by-character: `https://aws-external-anthropic.us-east-1.api.aws/v1/messages`. The familiar `.api.aws` suffix anchors "yes this is your AWS." Underline-marker sweep on `aws-external-anthropic`.
5. **Feature pill cluster**: 6-8 pill row of beta names — Managed Agents · Advisor · Skills · Files · MCP · Code execution · Web search · Console. Pills enter step-by-step (5s apart) and lock into place. The "all of them, today" beat.
6. **Final-frame thumbnail**: Dominant slam "CLAUDE PLATFORM. ON AWS." 160-180px, white-on-dark. Below: feature-count receipt ("8 betas. 17 regions. Day zero."). Anthropic mark top-left. Subordinate CTA "Watch the full breakdown".

---

## Visual Metaphor Inventory

| Concept | Metaphor | How It Animates | Source/Inspiration |
|---------|----------|----------------|-------------------|
| "Full Platform vs Bedrock subset" | Two doors — one shows partial features, one swings wide to full set | Doors swing in sequence; full-Platform door swings further | Comparison pattern |
| "Day-zero parity" | Two clocks ticking in sync (was: lagged) | Clocks slide into perfect alignment | Sync-up motion |
| "Existing AWS perimeter" | A fence/walled garden where Claude now drops INSIDE | Claude logo translates from outside to inside the IAM perimeter outline | Perimeter security visual |
| "Commitment retirement" | A drain/funnel where Claude spend pours into the AWS commitment bar | Bar fills as Claude spend pours down | Plumbing metaphor |

---

## Demo Opportunity Inventory

| What to Demo | Format | URL (if screenshot) | Dark/Light | Wow Factor | Notes |
|-------------|--------|---------------------|------------|-----------|-------|
| Anthropic blog post hero | screenshot | https://claude.com/blog/claude-platform-on-aws | dark | 7 | Authority anchor — proves the news is real |
| AWS announcement page | screenshot | https://aws.amazon.com/claude-platform/ | dark | 6 | Second authority anchor (AWS side) |
| Endpoint URL string | mono code reveal | N/A | dark | 6 | Type-on animation of the endpoint URL |
| IAM SigV4 auth snippet | code | N/A | dark | 5 | 4-line Python or curl showing IAM auth header |
| 17 regions map | diagram | N/A | dark | 8 | Vertical-cropped world map with dot pops |
| Model row (Opus 4.7 / Sonnet 4.6 / Haiku 4.5) | pill row | N/A | dark | 6 | Three model pills entering with version numbers |
| Customer logos (ReliaQuest / OpenRouter / Emergent) | logo row | N/A | dark | 7 | Social proof in 1 second |
| Feature pill cluster | pill row | N/A | dark | 7 | 8 betas, step-by-step reveal |

---

## Before/After Transformations

| Before State | After State | Visual Treatment |
|-------------|------------|-----------------|
| Bedrock = subset of features, weeks-of-lag | Platform-on-AWS = full feature set, day-zero | Split-screen feature columns |
| Two contracts (AWS + Anthropic) | One AWS invoice, retires against commitment | Invoice morph |
| Anthropic console missing from AWS path | Console accessible via AWS auth | Console screenshot fades in over AWS shell |

---

## Architecture Diagram Opportunities

| System/Flow | Components | Reveal Order | Complexity |
|------------|-----------|-------------|-----------|
| Request path | Developer → IAM SigV4 → `aws-external-anthropic.<region>.api.aws` → Anthropic (outside AWS boundary) → response → CloudTrail event | Sequential left-to-right | simple |
| Service comparison | Native Claude API (outside AWS) · Claude Platform on AWS (auth/billing/audit through AWS, processing outside) · Claude on Bedrock (auth/billing/audit/processing inside AWS) | Three-row table | medium |

---

## Competitive Landscape

| Alternative | Key Difference | Where Topic Wins | Where Alternative Wins |
|------------|---------------|-----------------|---------------------|
| Claude on Amazon Bedrock | Data processed inside AWS boundary; feature subset; weeks of lag on betas | Day-zero feature parity, full Console, Managed Agents | Strict data residency / "data stays inside AWS" mandates |
| Native Anthropic API (api.anthropic.com) | No AWS integration; own billing | Existing AWS IAM + Marketplace + commitment retirement | Non-AWS shops, simpler for solo devs |
| Claude on Google Vertex AI | Anthropic via Google Cloud partnership | If you're on AWS, you stay on AWS | Google Cloud-native shops |
| Azure OpenAI (GPT family) | Different model family, Microsoft ecosystem | Best Claude experience on AWS | Microsoft-first orgs, Office integrations |
| OpenAI on AWS Bedrock (April 28, 2026) | OpenAI models also now on Bedrock | Claude-specific features (Skills, Managed Agents) | If you want GPT alongside Claude on one platform |

---

## Notable Adopters

| Company/Person | How They Use It | Why It Matters for Video |
|---------------|----------------|------------------------|
| ReliaQuest | Cybersecurity + engineering workflows; Claude Code engineers as key users | Security-sensitive shop endorses the IAM/AWS integration story |
| OpenRouter | Routes Claude through AWS IAM credentials alongside other AWS services | Validates "uses same AWS IAM as our other services" claim — meta-credible since OpenRouter resells AI |
| Emergent | Day-one access to new model capabilities, "one team across both companies" | Validates "full feature parity, day-one access" claim with a named quote |
| Project Rainier | ~500K Trainium2 chips powering Claude | Background credibility — the deal funding this isn't theoretical |

---

## Market Context & Timing Signal

- **Market size**: Amazon Bedrock AgentCore is GA (October 13, 2025); Amazon Bedrock catalog now spans Claude, Llama, Mistral, Cohere, and (as of April 28, 2026) OpenAI. Enterprise AI platform market is consolidating around AWS/Azure/GCP.
- **Growth**: Anthropic + AWS committed up to 5GW Trainium2/3 capacity; $100B over 10 years; ~500K Trainium2 chips in Project Rainier; Amazon's latest $5B Anthropic investment with up to $20B more on milestones.
- **Why NOW**: (a) Bedrock historically lagged the native API on new features — a real pain point developers complained about for years; (b) Managed Agents (with dreaming + outcomes + multiagent orchestration) shipped Anthropic-direct on May 6, 2026, and the AWS GA route landed exactly 5 days later, signaling Anthropic wants enterprise adopters on Managed Agents NOW; (c) AgentCore GA in October 2025 set up the enterprise-agent substrate AWS customers were waiting for; (d) OpenAI dropping on Bedrock April 28, 2026 raised the competitive heat — Anthropic needs full feature surface on AWS to keep enterprise mindshare.

---

## Messaging Hierarchy

### Must Include [Visual Treatment]
- Claude Platform on AWS is generally available TODAY (May 11, 2026) [headline slam]
- This is NOT a Bedrock rebrand — full native API, every beta included [two-column split]
- IAM SigV4 + CloudTrail + AWS Marketplace billing [code snippet + invoice mockup]
- Day-zero feature parity with the native Claude API [timeline sync visual]
- Available in 17 AWS regions at launch [region map slam]
- All three models — Opus 4.7, Sonnet 4.6, Haiku 4.5 [model pill row]
- Three named customers — ReliaQuest, OpenRouter, Emergent [logo row]

### Should Include
- Feature roster pills — Managed Agents, Advisor, Skills, Files, MCP, Code execution, Console
- Comparison to Claude on Bedrock (when to pick which)
- The endpoint URL pattern (`aws-external-anthropic.<region>.api.aws`)

### Could Include
- Anthropic + AWS infrastructure backstory (5GW, Project Rainier, $100B)
- Pricing parity note (Sonnet $3/$15 same as native)
- Private-offer note for existing Bedrock customers

### Omit
- Detailed AgentCore explanation (separate topic, would bloat the Short)
- AgentCore vs Managed Agents debate (advanced; save for long-form)
- Cross-cloud Vertex comparison (off-thesis for this audience)
- Exhaustive region list naming each region (use a map, not 17 names)

---

## Hook Architecture

### Cult-Hopping References

| Brand/Person/Concept | Why It Works | Where to Use (Hook/Mid/CTA) |
|---------------------|-------------|---------------------------|
| AWS IAM | Every AWS developer's daily reality; instant credibility anchor | Hook + Mid |
| CloudTrail | Recognized AWS security primitive; cult-anchors "production-ready" | Mid |
| Claude Code | Anthropic's own coding agent; ReliaQuest quote calls them out by name | Mid |
| Project Rainier | Half a million Trainium chips — concrete number that anchors the partnership | Mid |
| ReliaQuest | Cybersecurity name; security-conscious validation | Mid |
| OpenRouter | Familiar AI-routing brand; meta-credible | Mid |
| Bedrock | Every AWS-AI dev has heard of it; comparison anchor | Hook |

### Common Ground by Audience

- **Technical**: "You shipped a Claude agent through Bedrock 3 months ago and you've been waiting for Managed Agents ever since." (Shared waiting-for-features pain.)
- **General**: "You know how some apps get the new feature first, and then later other apps get a watered-down version?" (Day-zero feature parity metaphor.)
- **Decision Makers**: "One AWS invoice, retired against your existing commitment — no second contract." (Procurement-friendly outcome.)

### Contrarian Angles (Uno Reverse)

1. **It's not just Bedrock with a new name**. Most developers will read "Claude on AWS" and assume "oh, like Bedrock." They're wrong — Bedrock is the data-resident subset; Platform-on-AWS is the full native API with AWS auth and billing wrapped around it. Different product, different feature surface.
   - Evidence: https://claude.com/blog/claude-platform-on-aws — "first-of-its-kind offering for Anthropic, providing all native Claude API features from day one." Bedrock historically does not.

2. **Anthropic is moving compute infrastructure to AWS but moving the data boundary out of AWS**. The same announcement that proves Anthropic's deepest infrastructure commitment to AWS (5GW Trainium, Project Rainier) also explicitly says data is processed OUTSIDE the AWS boundary on Platform-on-AWS. Two opposite directions in one product.
   - Evidence: AWS technical blog explicitly states "Claude Platform on AWS is operated by Anthropic, and the underlying requests and data are processed outside the AWS security boundary." Plus the Anthropic compute announcement re: 5GW.

3. **The thing that matters most isn't the new features — it's that the version-lag is gone**. Developers don't celebrate Managed Agents-on-AWS-today; they celebrate that the NEXT thing Anthropic ships will be on AWS the same day. The lag was the real product gap.
   - Evidence: Anthropic post: "all new features and betas shipping the same day they go live on the native Claude API."

### Mind-Blowing Stats

| Stat | Value | Shock Factor (1-10) | Source URL |
|------|-------|-------------------|-----------|
| Day-zero feature parity (new betas land on AWS same day as native) | "Day 0" | 8/10 | https://claude.com/blog/claude-platform-on-aws |
| 17 AWS regions at launch | "17 regions" | 7/10 | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ |
| ~500,000 Trainium2 chips in Project Rainier | "~500K chips" | 9/10 | https://www.anthropic.com/news/anthropic-amazon-compute |
| $100 billion over 10 years committed to AWS | "$100B / 10yr" | 9/10 | https://www.anthropic.com/news/anthropic-amazon-compute |
| Up to 5 GW of new compute capacity | "5 GW" | 8/10 | https://www.anthropic.com/news/anthropic-amazon-compute |
| 8 betas shipping on AWS day-one (Managed Agents, Advisor, Skills, Files, MCP, Code execution, Web search, Console) | "8 betas" | 7/10 | https://claude.com/blog/claude-platform-on-aws |

### Preview Hook Teasers (for Scene 00)

1. **"Anthropic just put the FULL Claude API on AWS — not the Bedrock subset, the actual thing."** (scroll-stop opener — stakes-clear in 6 words)
2. **"Same day. Same features. 17 regions."** (teaser — references the parity reveal)
3. **"Here's what changed for every AWS team shipping with Claude."** (promise statement)

### Primary Open Loop Suggestion

- **Setup** (early): "If you're on AWS and you've been waiting for Managed Agents, Skills, and the Claude Console — what just changed?"
- **Resolution** (late): Reveal that all 8 betas are on AWS today, with day-zero parity going forward, via IAM and CloudTrail.

---

## Suggested Narrative Arc (Kallaway Formula)

1. **Context Lean-In**: "Every AWS dev shipping with Claude knows this pain: Bedrock gets the new features WEEKS later."
2. **Scroll-Stop**: "But today, that lag is gone."
3. **Contrarian Snapback**: "Anthropic didn't move Claude TO Bedrock — they shipped the entire native Claude Platform THROUGH your AWS account. Different product."
4. **Solution**: "Claude Platform on AWS — generally available now."
5. **Features (Benefit-Led)**: Managed Agents, Advisor, Skills, Files, MCP, Code execution, Console — via IAM and CloudTrail, retiring against your AWS commitment.
6. **Trust**: Three named customers (ReliaQuest, OpenRouter, Emergent). 17 regions. Project Rainier infrastructure (~500K Trainium2 chips, 5GW).
7. **CTA**: "Visit the Claude Platform on AWS page. Full breakdown linked below."

---

## Suggested Scene Structure

| # | Scene Name | Duration Est. | Key Visual | Key Stat/Quote |
|---|-----------|--------------|-----------|---------------|
| 1 | Hook — "Bedrock has been lagging" | 8s | Bedrock pain split-screen | "Weeks of lag" |
| 2 | Scroll-stop reveal — "Claude Platform on AWS" | 6s | Title slam + Anthropic + AWS marks | "GA today" |
| 3 | Not-a-rebrand split | 10s | Two-column feature comparison | "Full native API" |
| 4 | Feature pills cluster | 18s | 6-8 pills entering step-by-step | "Managed Agents · Advisor · Skills · Files · MCP · Code · Web · Console" |
| 5 | AWS integration story | 14s | IAM SigV4 snippet + CloudTrail + Marketplace | "Endpoint: aws-external-anthropic.<region>.api.aws" |
| 6 | 17 regions slam | 8s | World map dot pops → "17" counter | "17 regions at GA" |
| 7 | Customer trust row | 10s | ReliaQuest / OpenRouter / Emergent logos | "3 launch customers" |
| 8 | When to pick which | 10s | Decision matrix Platform-on-AWS vs Bedrock | "Data outside vs inside AWS boundary" |
| 9 | Thumbnail / CTA hold | 8s | Topic slam + outcome receipt + brand | "CLAUDE PLATFORM. ON AWS." |

Total: ~92s — fits 90-120s target.

---

## Suggested Video Title Options

1. **"Anthropic just put the full Claude API on AWS"** — direct news framing; vidiq score **81/100**. Lead candidate.
2. **"Forget Bedrock. The Claude Platform is on AWS now"** — contrarian framing against Bedrock; vidiq score **68/100**.
3. **"Claude on AWS just changed enterprise AI"** — stakes-led / broad framing; vidiq score **53/100**.
4. **"AWS just got the WHOLE Claude Platform"** — stat-led emphasis on completeness; not scored (suggest).
5. **"The version-lag on Claude + AWS is over"** — pain-resolution framing; not scored (suggest).

---

## SEO Keywords

| Keyword / Phrase | Search Intent | Volume Estimate |
|-----------------|--------------|----------------|
| Claude on AWS | navigational | low (calibrated 0 — new term) |
| Claude Platform on AWS | navigational (brand new) | low (0 today, expected ramp) |
| AWS Bedrock Claude | comparison | medium (5K/mo) |
| Anthropic AWS | news/partnership | low-medium (4.3K/mo) |
| Amazon Bedrock Claude | product | medium (9.3K/mo) |
| Claude Managed Agents | feature | high (303K/mo) |
| Claude Opus 4.7 | model | high (576K/mo) |
| Trainium | infrastructure | medium (43.7K/mo) |
| Enterprise AI | category | medium (12K/mo) |

---

## Keyword Research (vidiq)

**Used.**

### Keyword opportunities

| Keyword | Volume | Competition | Overall score | Recommended use |
|---------|--------|-------------|---------------|-----------------|
| `claude managed agents` | 81.8 | 42.3 | 72.2 | High-volume + medium-comp — use in title/description |
| `aws bedrock claude` | 55.3 | 24.6 | 63.3 | Use in description and tags — strong overall score |
| `amazon bedrock claude` | 59.2 | 33.0 | 62.3 | Description + tags |
| `anthropic aws` | 54.2 | 45.1 | 54.5 | Description |
| `claude platform on aws` | 0 | 11.7 | 35.3 | Reserved brand term — use in title and description for first-mover SEO |
| `trainium` | 69.3 | 59.0 | 58.0 | Mention only if Project Rainier referenced |
| `claude code` | 100 | 61.1 | 75.6 | High-volume halo — mention in description |

### Currently trending in this niche (Shorts, query: "Claude AWS Bedrock")

No directly relevant trending Shorts surfaced (top results were Minecraft Bedrock Edition content and Russian-language Claude tips). This signals an open lane: Claude-on-AWS as a topic has very low Shorts competition right now. Move fast.

### Title scores

| Candidate title | vidiq score |
|-----------------|-------------|
| "Anthropic just put the full Claude API on AWS" | **81/100** |
| "Forget Bedrock. The Claude Platform is on AWS now" | 68/100 |
| "Claude on AWS just changed enterprise AI" | 53/100 |

Recommendation: lead with the **81/100** title.

---

## Technical Terms (TTS Pronunciation)

| Term | Pronunciation Note |
|------|-------------------|
| AWS | Spell as `A W S` |
| IAM | Spell as `I A M` |
| SigV4 | Read as `Sig V four` |
| API | Spell as `A P I` |
| MCP | Spell as `M C P` |
| Bedrock | OK as-is |
| AgentCore | OK as-is |
| Anthropic | OK as-is |
| Opus 4.7 | Read as `Opus four point seven` |
| Sonnet 4.6 | Read as `Sonnet four point six` |
| Haiku 4.5 | Read as `Haiku four point five` |
| Trainium2 | Read as `Trainium two` |
| Trainium3 | Read as `Trainium three` |
| CloudTrail | OK as-is |
| Marketplace | OK as-is |
| ReliaQuest | Read as `Rely-ah-Quest` if engine flubs it |
| OpenRouter | OK as-is |
| GA | Read as `generally available` (avoid `gah`) |
| 5GW | Read as `five gigawatts` (avoid `five gee double-u`) |
| GovCloud | OK as-is |

Heteronym audit (per `.claude/rules/tts-pronunciation.md`):
- **"live"** likely appears in script ("live today", "go live") — replace with `available today` / `shipping today` per the rule. Flag for Phase 2a.
- **"lead"** — if "lead agent" appears (in Managed Agents context), swap to `primary agent` or `coordinator agent`.

---

## Viewer Objections to Preempt

1. **"Isn't this just Bedrock with a new name?"** — Address head-on in Scene 3: feature parity matrix proves it's not. Bedrock = subset, data-resident. Platform-on-AWS = full native API, data outside AWS boundary, every beta.
2. **"But my data has to stay inside AWS for compliance"** — Acknowledge in Scene 8: that's exactly when you stay on Bedrock. Platform-on-AWS is for teams without strict residency mandates. Both are supported.
3. **"What about pricing — is this more expensive?"** — Brief mention: pricing parity with native API (Sonnet $3/$15 per million tokens). AWS Marketplace billing, retires against commitment.
4. **"Why now? Why didn't they do this earlier?"** — Timing signal: Managed Agents matured (May 6, 2026); OpenAI dropped on Bedrock April 28, 2026; AgentCore GA October 13, 2025 made the substrate ready.
5. **"Is this just for big enterprises?"** — No — any AWS account with credentials can use it; AWS Marketplace handles billing on consumption.

---

## Competitor Video Analysis

No directly competing Shorts on "Claude Platform on AWS" surfaced in vidiq trending search at time of brief (query returned Minecraft Bedrock Edition and unrelated Claude tips content). This is an open lane — first credible Short on the topic wins discovery. The Anthropic + AWS official channels will publish announcement posts but typically not snappy 90s Shorts.

---

## Quality Gate Results

| Gate | Check | Result | Notes |
|------|-------|--------|-------|
| QG-0A | Proof points >= 5 | **PASS** | 9 proof points with source URLs |
| QG-0B | Contrarian angles >= 3 | **PASS** | 3 contrarian angles with evidence URLs |
| QG-0C | Visual metaphor >= 1 | **PASS** | 4 metaphors catalogued |
| QG-0D | Demo opportunity >= 1 | **PASS** | 8 demo opportunities |
| QG-0E | SEO keywords >= 3 | **PASS** | 9 keywords with intent + volume |
| QG-0F | All stats sourced | **PASS** | Every proof point has a source URL |
| QG-0G | Cult-hop refs >= 3 | **PASS** | 7 cult-hops (IAM, CloudTrail, Claude Code, Project Rainier, ReliaQuest, OpenRouter, Bedrock) |
| QG-0H | Receipts >= 3 OR CONCEPT | **PASS** | 8 receipts (well above 3) — BLOCKING gate satisfied |
| QG-0I | Thesis present | **PASS** | One falsifiable sentence in Thesis section |

All gates pass. Pipeline cleared for Phase 1.

---

## Gaps / Needs User Input

- **Customer logo files**: ReliaQuest, OpenRouter, and Emergent logos may not be in `shared/logos/`. Phase 1 plan should call this out — if missing, either fetch via the agent-browser/screenshot route or stylize as text wordmarks.
- **17-region map asset**: No existing dark-styled world map in `shared/lib/`. Will need a simple custom SVG or use a built block — check `registry-blocks-catalog.md` for any candidates (no direct world-map block exists; recommend an inline SVG with dot pops).
- **Pricing note positioning**: The brief mentions Sonnet 4.6 = $3/$15. Decide in Phase 1 whether to include or omit — competing for screen time with 8 betas may push it to "Could Include" only.
- **Decision matrix in Scene 8**: Platform-on-AWS vs Bedrock — confirm the criteria language is right ("data outside vs inside AWS boundary") since this is the single most important "when to pick which" axis per the Anthropic post.

---

## Sources

| Source | URL | Used For |
|--------|-----|---------|
| Anthropic — Introducing the Claude Platform on AWS | https://claude.com/blog/claude-platform-on-aws | Primary source; features list; customer quotes; model availability |
| AWS Machine Learning Blog — Introducing Claude Platform on AWS | https://aws.amazon.com/blogs/machine-learning/introducing-claude-platform-on-aws-anthropics-native-platform-through-your-aws-account/ | Technical details: IAM SigV4, endpoint URL, 17 regions, Marketplace, CloudTrail |
| AWS What's New — Claude Platform on AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/claude-platform-aws/ | GA confirmation |
| AWS Product Page — Claude Platform | https://aws.amazon.com/claude-platform/ | Product landing reference |
| Anthropic — New in Claude Managed Agents | https://claude.com/blog/new-in-claude-managed-agents | Dreaming, outcomes, multiagent orchestration context |
| Anthropic — Amazon Compute Partnership | https://www.anthropic.com/news/anthropic-amazon-compute | 5GW, $100B over 10 years, Project Rainier (~500K Trainium2 chips) |
| AWS — Amazon Bedrock AgentCore | https://aws.amazon.com/bedrock/agentcore/ | AgentCore GA (October 13, 2025) substrate context |
| ClassMethod DevelopersIO — Claude Platform vs Bedrock | https://dev.classmethod.jp/en/articles/claude-platform-on-aws-bedrock-differences/ | Differences analysis |
| BenchLM — Claude API Pricing | https://benchlm.ai/blog/posts/claude-api-pricing | Pricing reference: Opus 4.7 $5/$25, Sonnet 4.6 $3/$15, Haiku 4.5 $1/$5 |
| AboutAmazon — Amazon expands Anthropic collaboration | https://www.aboutamazon.com/news/aws/amazon-invests-additional-4-billion-anthropic-ai | Investment history context |
| TechnoSports — Anthropic Launches Claude Platform on AWS | https://technosports.co.in/anthropic-claude-platform-on-aws/ | Independent press confirmation |
| The New Stack — Anthropic Managed Agents Dreaming | https://thenewstack.io/anthropic-managed-agents-dreaming-outcomes/ | Managed Agents press context |

---

_Brief written 2026-05-12. Phase 0 done._
