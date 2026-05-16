# Content Brief: Claude for Small Business

## Video Metadata

- **Slug**: `claude-for-small-business`
- **Template**: `templates/shorts/anthropic` (Anthropic dark-stage aesthetic — Anthropic-branded launch)
- **Duration**: 180s (2-3 min Short, 1080×1920 vertical)
- **Tone**: News-explainer, tech-savvy SMB operator audience; receipts-first, no fluff
- **Voice Profile**: `voice_profile: news-explainer` — Anthropic JUST launched this product (May 13, 2026). Maps to `.claude/references/brand-voice-news-explainer.md`.
- **Target Audience**: Small-business operators / founders / agency owners — the developer-adjacent audience that follows AI tooling. Secondary: solo entrepreneurs, accountants, ops managers at 15-50 person companies.
- **Key Angle**: "Anthropic just shipped Claude for Small Business — 15 workflows + 15 skills wired into QuickBooks, PayPal, HubSpot, Canva, DocuSign. Here's what it actually does, who it's for, and how it sizes up vs Copilot."
- **Topic Type**: `ARTICLE_RESPONSE` (primary source: anthropic.com/news/claude-for-small-business). Fact-check (Phase 2b) is source-only bidirectional per memory rule `feedback_factcheck_article_response_scope`.
- **Research Depth**: `STANDARD` (180s ≈ 60-180s bucket)

---

## Thesis

Claude for Small Business is not "ChatGPT with SMB branding" — it's a wedge product that bundles 15 pre-built agent workflows into the apps small businesses already pay for (QuickBooks, PayPal, HubSpot, Canva, DocuSign), and that bundle, not the model, is what makes it the first AI launch actually built for a 30-person company instead of a 30,000-person one.

---

## Receipts

1. https://www.anthropic.com/news/claude-for-small-business — May 13, 2026 — official launch announcement, the primary source for all product/workflow/customer/quote claims
2. https://www.youtube.com/watch?v=lserpKbUDjc — May 13, 2026 — official Anthropic demo video "Claude for Small Business: Planning Payroll with Confidence" — the demo we embed 0:06-0:35
3. https://www.axios.com/2026/05/13/anthropic-claude-small-business-smb — May 13, 2026 — Lina Ochman (Head of SMB at Anthropic) on-record quote about target customer
4. https://techcrunch.com/2026/05/13/anthropic-courts-a-new-kind-of-customer-small-business-owners/ — May 13, 2026 — competitive context vs OpenAI / ChatGPT Business; 36M US small business stat
5. https://trust.anthropic.com — referenced in the article for the "we don't train on your data by default on Team/Enterprise" claim
6. https://www.inc.com/ben-sherry/anthropics-newest-claude-feature-is-here-to-help-small-business-owners-with-their-pain-points/91343926 — May 13, 2026 — third-party press coverage, Inc. magazine
7. https://finance.yahoo.com/news/anthropic-debuts-claude-for-small-business-as-it-continues-its-enterprise-software-push-160500355.html — May 13, 2026 — Yahoo Finance, Anthropic enterprise revenue context

---

## Core Value Proposition

Claude for Small Business helps owners of 15-50 person companies automate payroll planning, month-end close, invoice chasing, lead triage, and marketing campaigns by toggling Claude into the tools they already use (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365) through 15 pre-built workflows and 15 reusable skills — no enterprise contract required.

---

## Target Audience

**Primary**: Owners and operators of US small-to-mid-market businesses (15-50 employees) running on QuickBooks + HubSpot + PayPal who have heard about ChatGPT but haven't found AI that fits THEIR stack.

**Secondary**: Solo entrepreneurs (Anthropic explicitly addresses them via the Solopreneurship Accelerator Program), agency owners, fractional CFOs/COOs, and the tech-savvy SMB operator who follows AI tooling.

**What they know**: They've tried ChatGPT and maybe Copilot. They know AI exists. They are stuck on "but how do I actually use it to close my books / chase invoices / plan payroll without dumping data into a generic chatbot?"

**What they care about**: Time savings on tedious clerical work, cash-flow visibility, not getting blindsided on payroll, data security (50% cited as their #1 hesitation per Anthropic's own survey), keeping their existing tool stack.

---

## Pain Points

1. **The Sunday-night payroll scramble**: Owner opens 5 tabs (bank, QuickBooks, PayPal, invoice list, payroll provider) every Friday to answer one question — "will I make payroll?" The companion video literally opens on this line. [VISUAL: HIGH — split-screen "before: 5 tabs" → "after: one Claude command"]
2. **Month-end close manually compiled in spreadsheets**: Reconcile bank/PayPal settlements against QuickBooks books, write a plain-English P&L, package it for the accountant. Currently a multi-day task. [VISUAL: HIGH — calendar with "3 days" → "30 minutes" counter]
3. **Invoices that slip through the cracks**: Overdue ARs go un-chased because no one has time to triage and write polite reminders. Skill name: "invoice chaser." [VISUAL: MEDIUM — pile of overdue invoices animating into a sorted queue]
4. **Generic AI tools don't touch your data stack**: ChatGPT can't see your QuickBooks. Copilot only sees Microsoft 365. Owners feel like the AI revolution is happening for big companies, not them. Lina Ochman quote nails this. [VISUAL: HIGH — generic chatbot icon with a closed lock over QuickBooks logo]
5. **Data security paralysis**: 50% of SMB owners cite data security as their #1 hesitation about AI (per Anthropic's own survey, referenced in the Axios piece). [VISUAL: MEDIUM — "50%" stat pill with shield icon]

---

## Key Features & Benefits

| Feature                          | Benefit (user-facing)                                              | Differentiator?           | Metric             | Visual Potential | Demo? |
| -------------------------------- | ------------------------------------------------------------------ | ------------------------- | ------------------ | ---------------- | ----- |
| 15 ready-to-run workflows        | Pre-built — no prompt engineering                                  | Yes vs ChatGPT/Copilot    | "15"               | HIGH             | Yes   |
| 15 reusable skills               | Repeatable tasks (invoice chaser, margin analyzer, etc.)           | Yes                       | "15"               | HIGH             | Yes   |
| QuickBooks integration           | Cash-flow forecasts, payroll plan, P&L                             | First-party connector     | Native             | HIGH             | Yes (companion video shows this) |
| PayPal integration               | Settlement reconciliation, transaction history pulled              | Yes                       | Native             | MED              | Yes   |
| HubSpot integration              | Lead triage, campaign attribution — "first CRM connector for Claude" per Angela DeFranco | Yes — first CRM connector | Native             | MED              | No    |
| Canva integration                | Auto-generate marketing assets inside the workflow                 | Yes                       | Native             | MED              | No    |
| DocuSign integration             | Contract sending/tracking/filing                                   | Yes                       | Native             | LOW              | No    |
| Approval-required execution      | "You approve the plan first, or let it run end-to-end"             | Yes — trust differentiator | UI flag           | MED              | No    |
| Existing permissions inherited   | Employee visibility mirrors underlying tool permissions            | Yes                       | Security           | LOW              | No    |
| No training on your data         | "Default" on Team and Enterprise plans                             | Tied with competitors     | Privacy default    | LOW              | No    |
| Plan Payroll workflow            | 5-minute payroll forecast vs Sunday-night spreadsheet scramble     | Yes — flagship demo       | "5 min" vs hours   | HIGH             | Yes (companion video) |
| AI Fluency for Small Business    | Free on-demand course taught by actual small business owners       | Yes                       | Free               | LOW              | No    |
| SMB Tour                         | Free half-day workshop, 100 leaders per stop, 10 cities Spring '26 | Yes — physical presence   | "10 cities"        | MED              | No    |

---

## Proof Points (Scene-Ready)

| Stat/Claim                                                | Formatted Value     | Comparison Baseline             | Source URL                                                    | Visual Format          | Shock Factor |
| --------------------------------------------------------- | ------------------- | ------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------ |
| Small businesses = 44% of US GDP                          | "44%"               | of US economy                   | https://www.anthropic.com/news/claude-for-small-business      | big stat pill          | 7/10         |
| 36 million US small businesses                            | "36M"               | total addressable               | https://techcrunch.com/2026/05/13/anthropic-courts-a-new-kind-of-customer-small-business-owners/ | counter roll      | 6/10         |
| 50% of SMB owners cite data security as #1 AI hesitation  | "50%"               | of surveyed owners              | https://www.anthropic.com/news/claude-for-small-business (Axios article cites it more clearly) | half-stat pill | 8/10         |
| 15 workflows + 15 skills shipped at launch                | "15 + 15"           | vs Copilot/ChatGPT generic chat | https://www.anthropic.com/news/claude-for-small-business      | dual-counter           | 9/10         |
| Anthropic revenue run rate $30B (up from $9B)             | "$30B"              | up from $9B prior year          | https://finance.yahoo.com/news/anthropic-debuts-claude-for-small-business-as-it-continues-its-enterprise-software-push-160500355.html | bar growth | 9/10         |
| 100 local small business leaders per SMB Tour stop        | "100/stop"          | free workshops                  | https://www.anthropic.com/news/claude-for-small-business      | map pin counter        | 5/10         |
| 10 US cities in Spring 2026 tour                          | "10 cities"         | physical SMB presence           | https://www.anthropic.com/news/claude-for-small-business      | US map dots            | 6/10         |
| "Plan payroll" turns a Sunday-night scramble into 5 minutes | "5 min"           | vs "Sunday night"               | https://www.youtube.com/watch?v=lserpKbUDjc (verbatim companion video closer) | before/after split | 9/10         |

---

## Visual Concepts

1. **The Five-Tab Scramble → One Command**: Open the Short on a frenetic split-screen showing 5 browser tabs (QuickBooks, PayPal, Gmail, bank, payroll provider) flickering open at once. Slam-cut to a single Claude prompt: `/plan-payroll`. The "before" is chaos; the "after" is one command. Mirrors the companion video's opening exactly. (Visual anchor for phase 1.)
2. **The 15+15 Receipt**: A two-row stat slab — top row counts up "15 workflows" with icons (📊 payroll, 📋 month-end, 💰 campaigns, etc.), bottom row counts up "15 skills" with icons (invoice chaser, margin analyzer, etc.). Lego-brick pattern: the bundle, not the model, is what's new.
3. **The Integration Constellation**: 7 partner logos (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365) orbiting a central Claude mark. On phase entrance, each logo connects to Claude with a glowing line, one at a time (step-by-step reveal per `.claude/rules/step-by-step-reveal.md`).
4. **The Companion Video Embed**: 0:06-0:35 of `lserpKbUDjc` plays in a phone-sized frame inside the composition, showing the actual Claude UI running `/plan-payroll`. Add a kinetic caption "what payroll planning actually looks like" with a marker sweep on the word "actually."
5. **The Lina Ochman Quote Card**: Full quote: "Not for the 15-person HVAC company or the 30-person landscaper or the 50-person real estate brokerage." Display as a quote card with the three business types popping in as discrete chips (HVAC, landscaper, brokerage) one at a time — three jabs to land the contrast against enterprise AI.
6. **The Customer Receipts Strip**: Three customer logos in a row — Purity Coffee, Simple Modern, MidCentral Energy — each with a 1-line outcome stat under them ("problems I didn't know I had", "constraints aren't constraints anymore", "tedious clerical work → value-add").
7. **The Daniela Amodei Cite**: Bottom-third lower-third quote: "Small businesses make up nearly half the American economy, but they've never had the resources of bigger companies. AI is the first technology that can finally close that gap." Attributed to "Daniela Amodei, Co-founder + President, Anthropic" with the Anthropic mark.
8. **The Final-Frame Thumbnail**: Per `.claude/rules/shorts-thumbnail-frames.md` — dominant slam text "CLAUDE FOR SMB" or "15 + 15 SHIPPED" at 160px+, Anthropic mark top-left, outcome receipt line "Sunday-night payroll → 5 min", debate-CTA question pill "Switching from Copilot?".

---

## Visual Metaphor Inventory

| Concept                          | Metaphor                                | How It Animates                                                                     | Source/Inspiration               |
| -------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------- |
| The Sunday-night payroll scramble | "5 tabs vs 1 command"                  | Browser-tab cluster flutters open frenetically, slam-cuts to single Claude prompt   | Companion video opening line     |
| Generic AI vs SMB-fit AI         | "One-size-fits-all sweater" → "tailored suit" | Loose generic ChatGPT box morphs into a fitted Claude block snapped into QB+HS+PP slots | Lina Ochman's "not for the 30-person landscaper" quote |
| 15 workflows + 15 skills         | "Lego bundle"                           | Stacked Lego bricks snap together to form a working machine                          | Engagement framework bricks pattern |
| Integration constellation        | "Orbit / spokes-of-a-wheel"             | Partner logos rotate around central Claude mark, each connects with a glowing edge   | Standard hub-and-spoke           |
| Approval-required execution      | "Trust gate"                            | A workflow plan visualized as a card; a viewer-controlled toggle gates execution     | Anthropic's stated trust model   |

---

## Demo Opportunity Inventory

| What to Demo                                          | Format                  | URL (if screenshot)                                       | Dark/Light | Wow Factor | Notes |
| ----------------------------------------------------- | ----------------------- | --------------------------------------------------------- | ---------- | ---------- | ----- |
| Claude `/plan-payroll` running inside Cowork          | Embedded YT clip 0:06-0:35 | https://www.youtube.com/watch?v=lserpKbUDjc           | dark       | 10/10      | This IS the demo — Anthropic's own video |
| Anthropic announcement page hero                      | Screenshot              | https://www.anthropic.com/news/claude-for-small-business | light      | 7/10       | Use as opening receipt anchor |
| Claude Cowork connectors panel                        | Screenshot or recreation | (from companion video frames)                            | dark       | 8/10       | "Connect the tools" beat |
| Cash flow forecast table output                       | Screenshot (companion video frame) | (from companion video frames)                  | dark       | 9/10       | The "payroll verdict" payoff frame |
| US map with 10 SMB Tour cities                        | Custom SVG               | N/A                                                       | dark       | 6/10       | Pin-drop animation |

---

## Before/After Transformations

| Before State                                         | After State                                  | Visual Treatment                                  |
| ---------------------------------------------------- | -------------------------------------------- | ------------------------------------------------- |
| 5 browser tabs (QB, PayPal, Gmail, bank, payroll)    | One Claude prompt `/plan-payroll`            | Split-screen → slam-cut                           |
| Sunday-night scramble (multi-hour)                   | 5-minute review with payroll verdict         | Calendar pages flipping → single clock face       |
| Generic ChatGPT (closed lock over QuickBooks)        | Claude with QuickBooks lit up                | Lock icon → key icon morph                        |
| Spreadsheet hand-built P&L                           | Plain-English P&L exported to Google Sheets  | Pixelated cells resolve into clean prose          |
| Anthropic = "enterprise/VC-backed/consumers" market  | Anthropic = also "15-person HVAC company"    | Pie chart redistributes / new wedge appears       |

---

## Architecture Diagram Opportunities

| System/Flow                       | Components                                                                 | Reveal Order                                          | Complexity |
| --------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------- | ---------- |
| Claude for SMB integration stack  | Claude Cowork hub → connectors panel → QB, PayPal, HubSpot, Canva, DocuSign | 1. Claude hub. 2. Connectors panel. 3. Each tool joins. | medium     |
| Plan-payroll workflow             | Slash command → clarifying Qs → data pull (QB+PayPal) → forecast → export | Sequential 5-step (mirrors companion video exactly)   | simple     |

---

## Competitive Landscape

| Alternative                                    | Key Difference                                       | Where Claude for SMB Wins                                  | Where Alternative Wins                                            |
| ---------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- |
| **Microsoft 365 Copilot**                      | Microsoft-stack-only; $30-43/user/month all-in       | Cross-stack (QB + PayPal + HubSpot, not just MS)            | Already deployed inside MS-shop SMBs                              |
| **Google Workspace + Gemini**                  | Gemini bundled free with Workspace seats             | Pre-built agentic workflows (15+15), not just chat sidebar | Free if you already pay Workspace                                 |
| **ChatGPT Business (OpenAI)**                  | Launched late 2023; generic chat-first                | First-party connectors to QB, HubSpot — Claude is built FOR the workflow, ChatGPT is a chatbot you bolt on | Massive head start in name recognition |
| **Intuit's own AI features in QuickBooks**     | Lives inside QB; doesn't see your CRM/marketing       | Multi-tool agent — finance + sales + marketing in one     | Already integrated, no extra subscription                         |
| **Vertical SaaS AI assistants** (e.g. HubSpot Breeze) | Single-tool                                       | Coordinates across tools — pulls QB cash + PayPal + HubSpot pipeline in one workflow | Deeper inside one tool                                       |

---

## Notable Adopters

| Company/Person                | How They Use It                                                              | Why It Matters for Video                                       |
| ----------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Purity Coffee**             | "Problem-solve for me, also showed me problems I didn't know I had"          | Cult-hop: small-batch coffee brand, recognizable consumer name |
| **Simple Modern**             | "Constraints aren't constraints anymore"                                     | Cult-hop: e-commerce brand many viewers will recognize          |
| **MidCentral Energy**         | "Freeing up tedious clerical work for value-add tasks"                       | Adds industry diversity (energy, not just retail)              |
| **Prospect Butcher Co.** (Brooklyn) | AI Fluency training partner                                                  | Local-brand authenticity beat                                  |
| **MAKS TIPM Rebuilders** (California) | AI Fluency training partner                                              | Blue-collar credibility — "this isn't just for tech bros"      |
| **Intuit (QuickBooks)** — Joe Preston, VP Product Mgmt | First-party connector partnership                                  | Distribution lever — QB has ~7M SMB users                      |
| **HubSpot** — Angela DeFranco, GM/VP Marketing Hub | "First CRM connector for Claude"                                       | Quote-card credibility                                         |
| **Canva** — Anwar Haneef, GM/Head of Ecosystem | Content creation inside the workflow                                       | Creative-stack legitimacy                                      |
| **PayPal** — Amy Bonitatibus, Chief Corporate Affairs | Settlement + invoicing partnership                                    | Money-rail trust signal                                        |
| **Workday Foundation + LISC** | Solopreneurship Accelerator funding                                          | Capital-backed legitimacy beat                                 |
| **Lina Ochman** (Anthropic Head of SMB) | "Not for the 15-person HVAC company..."                            | The strongest spoken anchor in the whole story                 |
| **Daniela Amodei** (Anthropic Co-founder + President) | "Half the American economy... finally close that gap"          | Top-of-house authority cite                                    |

---

## Market Context & Timing Signal

- **Market size**: 36 million US small businesses (TechCrunch), 44% of US GDP, ~half private-sector employment.
- **Growth**: Anthropic's revenue run rate climbed to $30B in 2026 (up from $9B in 2025) — they have the capital to ship this as a focused vertical product, not a side bet.
- **Why NOW**: Three converging forces. (1) OpenAI launched ChatGPT Business late 2023 — Anthropic was visibly behind on SMB. (2) Microsoft is bundling Copilot into higher-priced license tiers July 2026 — pricing pain creates switching window. (3) Anthropic's 50%-data-security-hesitation survey gave them the trust-positioning hook (approval-first, no-training-by-default, existing-permissions-inherited). The launch IS Anthropic's "we're not just enterprise, we're for the 30-person landscaper" repositioning.

---

## Messaging Hierarchy

### Must Include [Visual Treatment]

- **Anthropic shipped Claude for Small Business** [opening receipt — anthropic.com hero screenshot + date]
- **15 workflows + 15 skills** [dual counter stat slab]
- **Lives inside QB / PayPal / HubSpot / Canva / DocuSign / Google Workspace / MS365** [integration constellation reveal]
- **Plan-payroll demo (companion video 0:06-0:35)** [embedded video frame, this is THE proof]
- **Lina Ochman quote: "15-person HVAC, 30-person landscaper, 50-person brokerage"** [quote card with 3 chip-pops]
- **Sunday-night scramble → 5-minute review** [before/after split, the emotional payoff]
- **Approval-required + no-training-on-data default** [trust beat — fixes the #1 hesitation]
- **Final-frame thumbnail (per `.claude/rules/shorts-thumbnail-frames.md`)** [topic slam + brand + receipt + debate CTA]
- **Engagement CTA: debate question** [per `.claude/rules/engagement-cta.md` — see narrative arc step 7]

### Should Include

- **Daniela Amodei top-of-house cite** [Co-founder/President credibility, single lower-third]
- **3 customer testimonials (Purity / Simple Modern / MidCentral)** [3-logo strip with 1-line outcomes]
- **SMB Tour: 10 cities, 100 leaders/stop** [US map pin-drop]
- **AI Fluency course is FREE and on-demand** [pill chip]
- **vs Copilot ($30-43/user/mo all-in) vs Gemini (free w/ Workspace)** [3-column comparison]

### Could Include

- Solopreneurship Accelerator (Workday Foundation + LISC) — strong for solopreneur segment but tangential to the core story
- Anthropic $30B run rate context — strong receipt but moves attention off SMB
- Prospect Butcher Co. + MAKS TIPM (small-brand authenticity) — beautiful detail but cuts 1-2 seconds we may not have
- The 15 named skills (invoice chaser, margin analyzer, etc.) — overwhelming if all listed; show 3-4 max

### Omit

- Trust Center detailed compliance specifics (the article itself defers to trust.anthropic.com)
- Press coverage list (Axios, TechCrunch, Inc., Yahoo Finance) — these are receipts for fact-check, not on-screen content
- Nonprofit partner deep-dive (Accion, CRF, Pacific Community Ventures) — important for Anthropic's mission framing, not core to SMB-operator viewer's "should I switch?" question

---

## Hook Architecture

### Cult-Hopping References

| Brand/Person/Concept                      | Why It Works                                                       | Where to Use (Hook/Mid/CTA)   |
| ----------------------------------------- | ------------------------------------------------------------------ | ----------------------------- |
| **QuickBooks**                            | ~7M US SMB users — instant recognition                              | Hook + integration constellation |
| **PayPal**                                | Universal money rail; everyone knows the logo                       | Integration constellation     |
| **HubSpot**                               | CRM category leader; "first CRM connector for Claude" framing       | Mid (quote card)              |
| **Canva**                                 | Mainstream creative tool — bridge to non-technical viewers          | Integration constellation     |
| **DocuSign**                              | Contract/legal trust signal                                          | Integration constellation     |
| **ChatGPT / OpenAI**                      | Implicit comparison — "this isn't ChatGPT, it's Claude IN your tools" | Hook (the lock-icon contrast) |
| **Microsoft Copilot**                     | Direct price/lock-in comparison ($30-43/user/mo)                    | Mid (comparison row)          |
| **Sunday-night payroll dread**            | Universal SMB emotional anchor                                       | Hook (the scramble)           |
| **15-person HVAC / 30-person landscaper** | Lina Ochman's exact phrasing — tactile, blue-collar, real           | Mid (quote card)              |
| **Anthropic / Daniela Amodei**            | Source-of-truth authority cite                                       | Mid (top-of-house cite)       |

### Common Ground by Audience

- **Technical (developer-adjacent SMB operator)**: "AI tools that don't see my data stack are useless. Show me a connector for QuickBooks and I'll switch."
- **General (small-business owner)**: "I open 5 tabs every Friday to figure out if I can make payroll. I want that question answered, not another chatbot."
- **Decision Makers (founder / CEO / COO)**: "We pay for QB + HubSpot + Canva + Copilot already. Why doesn't AI actually orchestrate across them?"

### Contrarian Angles (Uno Reverse)

1. **"This isn't a new model — it's a new packaging"**: The headline is "Claude for Small Business" but the actual product is 15 pre-wired workflows + 15 reusable skills. The MODEL (Sonnet/Opus) is unchanged. The Lego brick is what's new — Anthropic finally admitted that SMBs don't want a model, they want a worker.
   - Evidence: https://www.anthropic.com/news/claude-for-small-business — workflows + skills are the entire announcement; model versioning isn't even mentioned.
2. **"Anthropic is late, and that's the play"**: OpenAI launched ChatGPT Business in late 2023. Anthropic took 2.5 years to ship for SMBs. Conventional wisdom says "first mover wins." Contrarian: Anthropic let OpenAI burn the generic chatbot path and shipped what SMBs actually buy — a workflow bundle that lives INSIDE QuickBooks, not a chat window that asks them to copy-paste their P&L.
   - Evidence: https://techcrunch.com/2026/05/13/anthropic-courts-a-new-kind-of-customer-small-business-owners/ — explicitly notes Anthropic is "a little behind" OpenAI. Reframe.
3. **"The SMB Tour is the real product"**: A free 10-city workshop tour for 100 leaders per stop is unusual go-to-market for a hyperscaler AI lab. Contrarian: this isn't marketing fluff — it's a physical anti-churn moat. Owners who attend an in-person workshop convert at 5-10x web rates AND become local evangelists. Anthropic is buying distribution that Copilot/ChatGPT cannot replicate at any price.
   - Evidence: https://www.anthropic.com/news/claude-for-small-business — 10 Spring cities, 100 leaders/stop = ~1,000 trained operators per quarter as a deliberate distribution lever.

### Mind-Blowing Stats

| Stat                                                              | Value         | Shock Factor (1-10) | Source URL                                                    |
| ----------------------------------------------------------------- | ------------- | ------------------- | ------------------------------------------------------------- |
| Small businesses = 44% of US GDP                                  | 44%           | 8/10                | https://www.anthropic.com/news/claude-for-small-business      |
| 36 million US small businesses (the addressable market)           | 36M           | 7/10                | https://techcrunch.com/2026/05/13/anthropic-courts-a-new-kind-of-customer-small-business-owners/ |
| 50% of SMB owners cite data security as #1 AI hesitation          | 50%           | 9/10                | https://www.anthropic.com/news/claude-for-small-business      |
| Anthropic revenue run rate $30B (up from $9B)                     | $30B          | 10/10               | https://finance.yahoo.com/news/anthropic-debuts-claude-for-small-business-as-it-continues-its-enterprise-software-push-160500355.html |
| 15 ready-to-run workflows + 15 skills at launch                   | 15 + 15       | 9/10                | https://www.anthropic.com/news/claude-for-small-business      |
| Sunday-night payroll scramble → 5-minute Claude review            | 5 min         | 9/10                | https://www.youtube.com/watch?v=lserpKbUDjc                   |
| 10 US cities in the Spring 2026 SMB Tour                          | 10            | 6/10                | https://www.anthropic.com/news/claude-for-small-business      |
| 100 small-business leaders trained per tour stop, free            | 100/stop free | 7/10                | https://www.anthropic.com/news/claude-for-small-business      |

### Preview Hook Teasers (for Scene 00 / opening 4 seconds)

1. **Bold stat / scroll-stop**: "44% of the US economy just got an AI worker."
2. **Mid-video reveal teaser**: "Anthropic shipped 15 workflows for SMBs — and one of them ends the Sunday-night payroll scramble in 5 minutes."
3. **Promise statement**: "In 60 seconds — what Claude for Small Business actually does, who it's for, and how it stacks up vs Copilot."

### Primary Open Loop Suggestion

- **Setup (Phase 1 / opening)**: "Every owner asks the same question the week before payday: will I make it?" (Lift verbatim from companion video opening — most universal SMB pain point in 12 words.)
- **Resolution (Phase 5+ / before CTA)**: Cut back to the payroll-verdict moment from the demo — "5 minutes. You go into payday knowing the number, not guessing at it."

---

## Suggested Narrative Arc (Kallaway Formula)

1. **Context Lean-In**: "Every owner asks the same question before payday: will I make it?" + the 5-tab scramble visual. (Universal SMB pain; works for anyone running a 15-50 person company.)
2. **Scroll-Stop**: "But Anthropic just shipped something that answers it in 5 minutes." (The "but" pivot.)
3. **Contrarian Snapback**: "And it's not a new model — it's 15 workflows wired directly into QuickBooks, PayPal, HubSpot." (Reframes "Claude for Small Business" as a packaging play, not a model play.)
4. **Solution**: Introduce Claude for Small Business + Claude Cowork. Show the `/plan-payroll` demo (embedded 0:06-0:35).
5. **Features (Benefit-Led)**: The 15+15 dual-counter. Integration constellation. Approval-required trust beat. Lina Ochman quote ("15-person HVAC, 30-person landscaper, 50-person brokerage").
6. **Trust**: 3-customer logo strip (Purity / Simple Modern / MidCentral) with 1-line outcomes. Daniela Amodei top-of-house cite. "We don't train on your data" + "approval-required" trust beat.
7. **CTA**: Debate-CTA question (per `engagement-cta.md`): "Switching from Copilot — or sticking?" OR "Claude or Copilot — which one's running your SMB by EOY?" (Polarizing, binary, references specific claim.) Plus spoken pointer to Dynamous per `feedback_dynamous_short_outro`.

---

## Suggested Scene Structure

180s total. 8 phases @ ~22s avg. Use Anthropic shorts template phase mutex.

| #  | Phase Name              | Duration Est. | Key Visual                                                              | Key Stat/Quote                                                       |
| -- | ----------------------- | ------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1  | Thumbnail-grade hook    | 6s            | Topic lockup + brand chrome (per `shorts-thumbnail-frames.md`)          | "Claude for SMB just shipped"                                        |
| 2  | The Sunday-night scramble | 22s         | 5 tabs flickering open → slam to `/plan-payroll` prompt                  | "Every owner asks: will I make payroll?"                             |
| 3  | The reveal: 15+15        | 24s           | Dual-counter (15 workflows / 15 skills) with named-skill chips reveal   | "15 workflows + 15 skills, pre-built"                                |
| 4  | Integration constellation | 22s          | 7 partner logos connecting to central Claude mark, one at a time        | "QB, PayPal, HubSpot, Canva, DocuSign, GW, MS365"                    |
| 5  | The companion demo      | 30s           | Embedded YT clip 0:06-0:35 (the `/plan-payroll` walkthrough)             | "Sunday-night scramble → 5-minute review"                            |
| 6  | The Lina Ochman quote   | 18s           | Quote card with 3 business-type chips (HVAC, landscaper, brokerage)     | "Not for the 15-person HVAC... 30-person landscaper..."              |
| 7  | Trust + customer proof  | 22s           | 3-logo customer strip + "we don't train on your data" + approval beat   | "Purity / Simple Modern / MidCentral — 50% cite security as #1 hesitation" |
| 8  | CTA + thumbnail-grade close | 16s        | Topic slam ("15 + 15 SHIPPED") + Dynamous pointer + debate question      | "Switching from Copilot — or sticking?"                              |

---

## Suggested Video Title Options

(All under 60 chars, all scored via vidiq.)

1. **"Claude vs Copilot for Small Business — who wins?"** (49 chars) — Direct comparison, polarizing. [vidiq score: 81/100 — HIGHEST]
2. **"Anthropic just launched Claude for Small Business"** (52 chars) — Stat-led news-explainer canonical. [vidiq score: 79/100]
3. **"Claude for Small Business is here. Worth it?"** (45 chars) — Question-driven, debate-friendly. [vidiq score: 74/100]
4. **"Anthropic dropped 15 AI workflows for small business"** (54 chars) — Specific number anchor. [vidiq score: 73/100]
5. **"15 AI workflows that run your small business"** (47 chars) — Outcome-led, generic. [vidiq score: 53/100 — LOWEST, avoid]

**Recommendation**: Lead with title #1 ("Claude vs Copilot for Small Business — who wins?"). Highest vidiq score (81), most aligned with the debate-CTA engagement frame, and explicitly references competitors which is what high-CTR SMB tooling searches look for. Title #2 as fallback for a purer news-explainer framing.

---

## SEO Keywords

| Keyword / Phrase            | Search Intent              | Volume Estimate |
| --------------------------- | -------------------------- | --------------- |
| claude for small business   | Direct topic discovery     | high (15,118/mo est)            |
| claude cowork tutorial      | How-to                     | high (465,479/mo est)           |
| how to use claude cowork    | How-to                     | high (272,392/mo est)           |
| claude skills               | Concept discovery          | high (1.3M/mo est)              |
| ai automation business      | Decision-maker             | medium (53,133/mo est)          |
| ai automation               | Broad category             | high (1M+/mo est)               |
| anthropic claude            | Brand search               | medium (118,195/mo est)         |
| claude cowork demo          | Demo-seekers               | medium (36,062/mo est)          |
| claude vs copilot           | Comparison shopper         | high (inferred)                 |
| small business ai tools     | Buying-stage               | high (inferred)                 |

---

## Keyword Research (vidiq)

### Keyword opportunities (vidiq overall score sorted)

| Keyword                        | Volume | Competition | Overall Score | Est Monthly Search | Recommended Use |
| ------------------------------ | ------ | ----------- | ------------- | ------------------ | --------------- |
| claude skills                  | 91     | 45          | 77            | 1,313,142          | Title alt + tag |
| claude ai                      | 97     | 55          | 77            | 3,306,287          | Tag             |
| ai automation                  | 90     | 45          | 76            | 1,018,276          | Description     |
| how to use claude cowork       | 81     | 37          | 74            | 272,392            | Description anchor |
| claude cowork tutorial         | 85     | 49          | 71            | 465,479            | Description anchor |
| how to use claude              | 84     | 49          | 71            | 417,344            | Tag             |
| ai                             | 100    | 71          | 72            | 6,786,255          | Tag (broad)     |
| claude                         | 100    | 71          | 72            | 7,917,804          | Tag (broad)     |
| **claude for small business**  | 62     | 35          | **64**        | **15,118**         | **Title — exact phrase** |

### Currently trending in this niche

_Not run — keyword research call was sufficient for STANDARD depth on a news-explainer; trending-videos would duplicate the competitor analysis from web search._

### Title scores (vidiq score)

| Title                                                         | Score   |
| ------------------------------------------------------------- | ------- |
| **Claude vs Copilot for Small Business — who wins?**          | **81**  |
| Anthropic just launched Claude for Small Business             | 79      |
| Claude for Small Business is here. Worth it?                  | 74      |
| Anthropic dropped 15 AI workflows for small business          | 73      |
| Claude just hit small business. Here's what changed.          | 53      |
| 15 AI workflows that run your small business                  | 53      |

---

## Technical Terms (TTS Pronunciation)

| Term                  | Pronunciation Note                                                                       |
| --------------------- | ---------------------------------------------------------------------------------------- |
| `Claude`              | Default — TTS reads "klode" correctly                                                    |
| `Cowork`              | Default — "co-work" reads correctly                                                       |
| `QuickBooks`          | Default — TTS reads correctly as one word                                                 |
| `HubSpot`             | Default — reads correctly                                                                 |
| `DocuSign`            | Default — reads correctly                                                                 |
| `PayPal`              | Default — reads correctly                                                                 |
| `Anthropic`           | Default — reads correctly                                                                 |
| `Daniela Amodei`      | Reads as "Daniela Ah-MO-day"; default usually fine, spot-check post-generation            |
| `Lina Ochman`         | Reads as "LEE-nah OCK-mun"; spot-check post-generation                                    |
| `SMB`                 | Spell as `S M B` in script to ensure letter-by-letter pronunciation, not "smub"           |
| `AR / AP` (accounts receivable/payable) | Spell as `A R` and `A P` for letter-by-letter pronunciation              |
| `P&L`                 | Spell as `P and L` (ampersand reads inconsistently)                                       |
| `CRM`                 | Spell as `C R M`                                                                          |
| `15` (when said as "fifteen", multiple times) | Default — TTS reads numerals correctly; varied phrasing recommended |
| `live` (avoid as adjective per `tts-pronunciation.md`) | Use `shipping` / `available` instead — e.g. NOT "Claude is live today" → "Claude is available today" |
| `lead` (verb sense)   | If used (e.g., "lead the workflow"), prefer `runs` / `drives` to avoid /lɛd/ vs /liːd/    |

---

## Viewer Objections to Preempt

1. **"This is just ChatGPT with a fresh coat of paint"** — Address by leading with the 15+15 workflow/skill bundle and the integration constellation. The model isn't the news; the workflow library and connectors are. (Phase 3 + Phase 4.)
2. **"I'm not giving my QuickBooks data to a chatbot"** — Address with the trust beat: approval-required execution, "your existing permissions hold", no-training-on-data default. (Phase 7.) Reference the 50%-data-security-hesitation stat to acknowledge the concern explicitly.
3. **"How is this different from Microsoft Copilot, which I'm already paying $30/seat for?"** — Address with the cross-stack angle in Phase 4 (constellation includes both Google Workspace AND Microsoft 365, plus 5 non-Microsoft tools). Copilot lives inside MS; Claude for SMB orchestrates ACROSS.
4. **"What does it cost?"** — Anthropic didn't publish pricing in the announcement. Flag this as a gap; don't fabricate. Mention "no extra charge beyond Claude licenses + your existing tool subscriptions" per the TechCrunch article. (Phase 8 / CTA can hint at this without specifying tiers.)
5. **"My business is 8 people, not 30 — is this for me?"** — The Solopreneurship Accelerator framing covers this. We won't have time for a deep dive but a brief mention in Phase 6 or 8 ("plus a free AI fluency course and a 10-city tour for solo founders too") addresses it.

---

## Competitor Video Analysis

| Video/Channel                 | Hook Used                                              | What They Miss                                                                |
| ----------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Anthropic official demo (`lserpKbUDjc`) | "Every owner asks the same question the week before payday" | Doesn't position vs Copilot/ChatGPT; doesn't quote Lina Ochman's anti-enterprise framing |
| (No major third-party explainer shorts on this topic exist at time of research — first-mover advantage on the explainer angle) | n/a | n/a |

---

## Quality Gate Results

| Gate  | Check                                | Result | Notes                                                                                      |
| ----- | ------------------------------------ | ------ | ------------------------------------------------------------------------------------------ |
| QG-0A | Proof points >= 5                    | PASS   | 8 scene-ready proof points, all sourced                                                    |
| QG-0B | Contrarian angles >= 3               | PASS   | 3 angles — "packaging not model" / "late on purpose" / "tour is the moat"                  |
| QG-0C | Visual metaphor >= 1                 | PASS   | 5 visual metaphors mapped                                                                  |
| QG-0D | Demo opportunity >= 1                | PASS   | The companion video IS the demo (Anthropic-published, sanctioned embed)                    |
| QG-0E | SEO keywords >= 3                    | PASS   | 10 keywords; vidiq enrichment ran                                                          |
| QG-0F | All proof-point stats sourced        | PASS   | Every stat has a source URL (Anthropic primary or third-party press)                       |
| QG-0G | Cult-hop refs >= 3                   | PASS   | 10 cult-hops — QB, PayPal, HubSpot, Canva, DocuSign, ChatGPT, Copilot, Lina, Daniela, Anthropic |
| QG-0H | Receipts >= 3 OR CONCEPT             | PASS   | 7 receipts, all linkable, all dated 2026-05-13                                             |
| QG-0I | Thesis present                       | PASS   | "Not ChatGPT with SMB branding — wedge product bundling 15 workflows into the apps SMBs already pay for" |

**ALL GATES PASS. Phase 1 may proceed.**

---

## Gaps / Needs User Input

- **Pricing**: Anthropic did NOT publish dollar-amount pricing. TechCrunch states "no extra charge beyond Claude licenses + existing partner tool subscriptions." Acceptable to mention this generically in the script; do NOT fabricate a per-seat price. If the user has access to the Claude.com/solutions/small-business page and it includes pricing tiers, we should pull and incorporate. Otherwise stay vague.
- **The remaining 8 (of 15) workflow names + 7 (of 15) skill names**: Anthropic only enumerated some by name. The script should not name workflows/skills that aren't in the article. If a user has a follow-up internal Anthropic doc that enumerates all 30, we can use it — otherwise stick to the named ones (invoice chaser, margin analyzer, month-end prepper, tax-season organizer, contract reviewer, lead triager, content strategist).
- **Customer logos**: Purity Coffee, Simple Modern, MidCentral Energy logos are visible on the announcement page but we'll need to source clean SVG/PNG versions for the 3-logo strip. Suggest pulling from each company's own press kit. None are in `shared/logos/` yet.
- **Lina Ochman headshot / Daniela Amodei headshot**: If we want to make the quote-cards faces-included, we'd need to source images. Quote cards work without headshots (and most shorts skip them) — defer this unless the user wants the polish.
- **Companion video embed clearance**: Anthropic's own demo video published on YouTube — embedding 0:06-0:35 in a fair-use commentary short is standard practice, but flag the decision so the user can override if they want to record their own demo instead.

---

## Sources

| Source                              | URL                                                                                                                                     | Used For                                          |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Anthropic launch announcement       | https://www.anthropic.com/news/claude-for-small-business                                                                                | Primary — product, features, customers, quotes    |
| Anthropic companion demo video      | https://www.youtube.com/watch?v=lserpKbUDjc                                                                                             | Primary demo (embed 0:06-0:35)                    |
| Axios coverage                      | https://www.axios.com/2026/05/13/anthropic-claude-small-business-smb                                                                    | Lina Ochman on-record quote, 50% security stat    |
| TechCrunch coverage                 | https://techcrunch.com/2026/05/13/anthropic-courts-a-new-kind-of-customer-small-business-owners/                                        | 36M SMBs stat, competitive context vs ChatGPT     |
| Yahoo Finance coverage              | https://finance.yahoo.com/news/anthropic-debuts-claude-for-small-business-as-it-continues-its-enterprise-software-push-160500355.html   | $30B Anthropic run-rate                           |
| Inc. magazine coverage              | https://www.inc.com/ben-sherry/anthropics-newest-claude-feature-is-here-to-help-small-business-owners-with-their-pain-points/91343926   | Third-party SMB-press validation                  |
| Compare-the-Cloud Copilot/Gemini pricing | https://www.comparethecloud.net/articles/google-gemini-workspace-vs-microsoft-365-copilot-uk-small-team-pricing                     | Copilot ~$30-43/seat all-in pricing reference     |
| Tech-Insider Copilot vs Gemini      | https://tech-insider.org/copilot-vs-gemini-2026/                                                                                        | Cross-vendor SMB AI pricing context                |
| Anthropic Trust Center              | https://trust.anthropic.com                                                                                                             | Trust beat reference                              |
| vidiq keyword research              | (MCP tool result — see Keyword Research section)                                                                                        | Title scoring + keyword opportunities             |
