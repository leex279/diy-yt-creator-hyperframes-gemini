---
description: "Phase 0 — Research a topic deeply: gather facts, features, stats, and messaging for video content"
argument-hint: <topic | URL | concept | brief.md>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebSearch, WebFetch
---

<objective>
Execute Phase 0 of the HyperFrames video pipeline.
Perform deep research on "$ARGUMENTS" to produce a comprehensive, **video-content-aware** content brief that will feed Phase 1 (composition planning) and Phase 2 (script writing).

This phase uses **parallel research agents** to gather information 3-4× faster than sequential research, then synthesizes findings with quality gates.

**Goal**: Understand the topic thoroughly — features, benefits, differentiators, audience pain points, compelling angles, AND how each piece of information translates to a compelling HyperFrames composition.

**Output**: `videos/<slug>/research/content-brief.md`
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

If invoked as part of the orchestrator, parameters arrive in context. **DO NOT ask questions** — use the provided values or infer sensible defaults:

- **Topic type**: Infer from URL/description (product if it has features, concept if it's technology)
- **Target viewer**: Default to "developers and technical audience" unless specified
- **Key angle**: Determine from research — find the most compelling differentiator
- **Duration**: Use to determine research depth (15-30s = LIGHT, 45-90s = STANDARD, 3min+ = DEEP)

Proceed autonomously through all waves.
</autonomous-mode>

<process>

### Step 0 — Slug & Phase Gate

Derive `<slug>` (kebab-case, 3-6 words, no stopwords) from `$ARGUMENTS`:
- "Claude Code Skills launch" → `claude-code-skills-launch`
- A URL → use the page title or product name, then kebab-case it
- A `*.md` brief file → read the `**Slug**:` field if present, else derive from `**Topic**:`

Read `videos/<slug>/phase-status.md` if it exists.
- **Prerequisites**: None — Phase 0 can always run.
- **Re-run check**: If row `0 - Research` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

If `videos/<slug>/` does not exist, create it (`mkdir -p videos/<slug>/research`).

---

## WAVE 0 — Parse & Pre-Fetch (Lead, synchronous)

### Step 0A: Identify Input Type

Determine what `$ARGUMENTS` refers to and classify it:

| Input Pattern                                                            | Classification     | Pre-Fetch Action                                                |
| ------------------------------------------------------------------------ | ------------------ | --------------------------------------------------------------- |
| YouTube URL (`youtube.com/watch`, `youtu.be/`, `youtube.com/playlist`, `youtube.com/@handle`) | `YOUTUBE_SOURCE`   | Fetch transcript via `youtube-transcript` skill (see Step 0C.5) |
| URL (http/https, non-YouTube)                                            | infer from page    | Fetch URL content for all agents                                |
| Product/tool name                                                        | `PRODUCT_TOOL`     | Search for official site                                        |
| Abstract concept                                                         | `CONCEPT`          | No pre-fetch, agents search                                     |
| Article/video response                                                   | `ARTICLE_RESPONSE` | Fetch article URL                                               |
| "X vs Y" or comparison                                                   | `COMPARISON`       | Search both subjects                                            |
| Brief template (contains `**Topic**:`)                                   | `STRUCTURED_BRIEF` | Parse fields, fetch links (YouTube links route through 0C.5)    |

Store as `TOPIC_TYPE` for agent prompts.

`YOUTUBE_SOURCE` behaves like `ARTICLE_RESPONSE` for fact-check scope (the transcript is the source of truth) — see the memory rule "Fact-check ARTICLE_RESPONSE against the source only." When phase 2b runs, point it at `videos/<slug>/research/source-transcript.json` as the canonical source.

### Step 0B: Determine Research Depth

Based on target duration (from context, brief, or default):

| Duration  | Depth      | Agent A scope | Agent B competitors | Agent C angles |
| --------- | ---------- | ------------- | ------------------- | -------------- |
| < 60s     | `LIGHT`    | 3 key sources | 2 alternatives      | 2 angles       |
| 60-180s   | `STANDARD` | 5 key sources | 3 alternatives      | 3 angles       |
| 3-8min    | `DEEP`     | 8+ sources    | 5 alternatives      | 3+ angles      |

Default to `STANDARD` if duration is unknown.

### Step 0C: Pre-Fetch Primary URL (if applicable)

If a URL was provided AND `TOPIC_TYPE` is **not** `YOUTUBE_SOURCE`, fetch the page content now via `WebFetch`. Include this content in ALL agent prompts so they share the same primary source without redundant fetches.

For `YOUTUBE_SOURCE`, skip `WebFetch` entirely — the YouTube watch page has no usable text content. Use Step 0C.5 instead.

### Step 0C.5: Pre-Fetch YouTube Transcript (YOUTUBE_SOURCE only)

When `TOPIC_TYPE == YOUTUBE_SOURCE`, fetch the transcript via the installed `youtube-transcript` skill before spawning Wave 1 agents. The skill is a stdlib-only Python script at `~/.claude/skills/youtube-transcript/scripts/youtube_transcript.py` and reads `TRANSCRIPT_API_KEY` from the project `.env`.

Pick the right subcommand based on the URL pattern:

| URL pattern                          | Subcommand                              |
| ------------------------------------ | --------------------------------------- |
| `youtube.com/watch?v=...` or `youtu.be/...` | `video <url>`                    |
| `youtube.com/playlist?list=...`      | `playlist <url>`                        |
| `youtube.com/@handle` or `/channel/UC...` | `channel <handle> --count 5` (default 5; raise to 10-15 if the topic is "latest from this channel") |

Run from the repo root, writing both JSON (with timestamps, for downstream phases) and a plain-text copy (for agent prompts):

```bash
mkdir -p videos/<slug>/research

# JSON with word-level timestamps + metadata — canonical source for fact-check
python ~/.claude/skills/youtube-transcript/scripts/youtube_transcript.py \
  video "<URL>" --metadata --format json \
  -o videos/<slug>/research/source-transcript.json

# Plain-text copy — pasted into Wave 1 agent prompts
python ~/.claude/skills/youtube-transcript/scripts/youtube_transcript.py \
  video "<URL>" --metadata --format text --no-timestamps \
  -o videos/<slug>/research/source-transcript.txt
```

PowerShell variant (Windows): replace `~` with `$env:USERPROFILE` and the line continuations with backticks. The script itself works identically.

**Failure handling**:
- Exit code 1 with "Invalid API key" → STOP and tell the user to set `TRANSCRIPT_API_KEY` in `.env` (get a key at https://transcriptapi.com).
- Exit code 1 with "No credits remaining" → STOP and tell the user to top up.
- Exit code 1 with "Not found (404)" → the video may be private, region-locked, or have no captions. STOP and ask the user for an alternative source URL.
- Any other failure → fall back to `WebFetch` on the watch page (will yield only metadata) and warn in the brief that no transcript was available.

After the fetch succeeds, read `source-transcript.txt` and include the full text inline in **every** Wave 1 agent prompt (under a `PRE-FETCHED YOUTUBE TRANSCRIPT` heading) so all four agents work from the same source without redundant API calls. Also include the video title + channel from the metadata header so agents can attribute claims correctly.

### Step 0D: Interactive Scoping (standalone execution only)

**Interactive mode** — Ask the user one question at a time:
1. **What is this?** Product, open-source tool, concept, or service?
2. **Target viewer**: Who should care? (developers, managers, marketers, general tech)
3. **Key angle**: What's the ONE thing viewers should remember?

**Autonomous mode** (from `full-auto`) — Use context or defaults; do not ask.

### Step 0E: Pick Voice Profile

Set `voice_profile` for this video. The field flows into `content-brief.md` and Phase 2 reads it to pick the right `brand-voice-*.md` rules.

Heuristic — match the topic against the strongest signal first; defaults are conservative:

| Topic signal                                                                                            | Default profile                                                  |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Topic mentions "I tried", "I built", "tutorial", "guide", "how to use", "walkthrough", "let's build"   | `tutorial`                                                       |
| Topic mentions "just shipped", "just launched", "just announced", "deal", "acquired", "raised", "vs"    | `news-explainer`                                                 |
| URL is a GitHub release, vendor blog post, or news article                                              | `news-explainer`                                                 |
| URL is a tool's homepage with no announcement context                                                   | `tutorial` (offer; ask in interactive mode)                      |
| Topic frames Tool A vs Tool B / benchmark / comparison                                                  | `comparison` (currently uses `news-explainer` rules)              |
| None of the above                                                                                       | ASK in interactive mode; default `news-explainer` in autonomous   |

**Default**: when nothing matches and you can't ask (autonomous mode), pick `news-explainer` — it's the dominant format on this channel and the dispatcher (`brand-voice.md`) treats missing values as `news-explainer` anyway.

Store the picked value as `voice_profile` for inclusion in the content brief metadata.

---

## WAVE 1 — Parallel Research (4 agents, concurrent)

Spawn ALL FOUR agents simultaneously using the Task tool. Each agent gets a self-contained prompt with topic, classification, depth, and any pre-fetched content.

**IMPORTANT**: Use `subagent_type: "general-purpose"` for all 4 agents. Spawn all 4 in a SINGLE message to maximize parallelism. Do NOT specify a `model` parameter — let it inherit from the parent agent (this project runs on Opus by default).

---

### Agent A — Core Topic Researcher

**Focus**: Deep understanding of WHAT the topic IS — features, mechanism, docs, proof points.

```
You are a research analyst preparing material for a YouTube explainer video.

TOPIC: {topic description}
TOPIC TYPE: {TOPIC_TYPE}
RESEARCH DEPTH: {LIGHT|STANDARD|DEEP}
{PRE-FETCHED CONTENT if available}

Your job: Research the CORE TOPIC deeply. Understand what it is, how it works, and why it matters.

Research these areas (adapt based on topic type):

FOR PRODUCT_TOOL:
- Official documentation / landing page
- GitHub README (if open source) — stars, contributors, release cadence
- Feature list / changelog / recent updates
- Pricing / tiers / free vs paid
- Integration ecosystem
- Security model / compliance
- Technical architecture (how it works under the hood)

FOR CONCEPT:
- How it works (technical mechanism)
- Why it matters (business/developer value)
- Current state of adoption
- Key players / implementations
- Common misconceptions
- Historical context (when did this emerge?)

FOR ARTICLE_RESPONSE:
- Deep analysis of the source article
- Author background and credibility
- Key claims and their evidence
- Counter-arguments in the discourse

FOR ALL TOPICS:
- Pain points this solves (3-5 relatable scenarios framed as "You've been there...")
- Quantifiable claims with sources (benchmarks, adoption stats, cost savings)
- Technical terms that might need TTS pronunciation notes

OUTPUT FORMAT (use these exact headers):

## Value Proposition
<One sentence: "X helps Y achieve Z by doing W">

## Target Audience
<Primary, secondary, what they know, what they care about>

## Pain Points
1. <Pain point with relatable scenario> [VISUAL POTENTIAL: HIGH/MEDIUM/LOW]
2. ...
(minimum 3, target 5)

## Features & Benefits
| Feature | Benefit (user-facing) | Differentiator? | Metric | Demo Possible? |
|---------|----------------------|-----------------|--------|---------------|
| ... | ... | Yes/No | ... | Yes/No |

## Proof Points
| Stat/Claim | Value | Comparison Baseline | Source URL | Visual Format |
|-----------|-------|-------------------|-----------|--------------|
| ... | ... | ... | ... | bar chart / counter / comparison |
(minimum 5 proof points with source URLs)

## Technical Terms (TTS Pronunciation)
| Term | Pronunciation Note |
|------|-------------------|
| ... | ... |

## Raw Research Notes
<Links, quotes, data points gathered — include everything even if not used above>
```

---

### Agent B — Competitive & Market Analyst

**Focus**: Position the topic against alternatives and the broader market.

```
You are a competitive intelligence analyst preparing material for a YouTube explainer video.

TOPIC: {topic description}
TOPIC TYPE: {TOPIC_TYPE}
RESEARCH DEPTH: {LIGHT|STANDARD|DEEP}
{PRE-FETCHED CONTENT if available}

Your job: Map the competitive landscape and market context. Help the video creator position this topic against alternatives and explain WHY NOW.

Research these areas:
- Direct competitors / alternatives ({2-5 based on depth})
- Key differentiators (what THIS does that others don't)
- Notable adopters / case studies (companies, people — these become "cult-hop" references)
- Market trends and timing signal ("why NOW?" — what changed recently?)
- Industry size / growth stats
- SEO keywords people search for related to this topic (for YouTube title/description optimization)

OUTPUT FORMAT (use these exact headers):

## Competitive Landscape
| Alternative | Key Difference | Where Topic Wins | Where Alternative Wins |
|------------|---------------|-----------------|---------------------|
| ... | ... | ... | ... |

## Notable Adopters
| Company/Person | How They Use It | Why It Matters for Video |
|---------------|----------------|------------------------|
| ... | ... | cult-hop reference / social proof / etc. |

## Market Context
- Market size: ...
- Growth trajectory: ...
- Key trend driving adoption: ...

## Timing Signal (Why NOW?)
<2-3 sentences on what changed recently that makes this topic timely>

## SEO Keywords
| Keyword / Phrase | Search Intent | Monthly Volume Estimate |
|-----------------|--------------|----------------------|
| ... | ... | high/medium/low |
(minimum 5 keywords)

## Raw Research Notes
<Links, quotes, data points>
```

---

### Agent C — Hook Architecture Researcher

**Focus**: Find raw materials for maximum-retention hooks.

```
You are a YouTube hook specialist and audience researcher preparing material for an explainer video.

TOPIC: {topic description}
TOPIC TYPE: {TOPIC_TYPE}
RESEARCH DEPTH: {LIGHT|STANDARD|DEEP}
{PRE-FETCHED CONTENT if available}

Your job: Find the raw materials that will make this video IMPOSSIBLE TO SCROLL PAST. Research hook elements, contrarian angles, and audience psychology.

The video uses the Kallaway Formula:
1. Context Lean-In — mind-blowing fact or shared pain point (first 4 seconds)
2. Scroll-Stop Interjection — "But/However/Yet" as a stun gun
3. Contrarian Snapback — "Uno Reverse" that snaps viewers onto unexpected path

Research these areas:

CULT-HOPPING OPPORTUNITIES (minimum 5):
- Established brands, celebrities, or cultural references that can anchor the topic
- Well-known companies/people that use this or something similar
- Familiar concepts that serve as analogies (cross-domain borrowing is powerful)
- "Known layers" that can wrap the unknown idea
- For each: WHERE in the video it should appear (hook, mid-video, CTA)

CONTRARIAN ANGLES (minimum 3):
- What's counterintuitive about this topic?
- What common belief can be challenged with evidence?
- What seems obvious but is actually wrong?
- For each: what EVIDENCE supports the contrarian claim? (no unsupported hot takes)

MIND-BLOWING STATS (minimum 5 candidates):
- Surprising metrics or benchmarks WITH source URLs
- Counterintuitive data points
- Comparison statistics that shock (e.g., "X is bigger than Y" where Y is unexpected)
- Rate each: SHOCK FACTOR 1-10 (how likely to cause a scroll-stop)

COMPETITOR VIDEO ANALYSIS:
- Search YouTube for existing videos on this topic
- What hooks do they use? What angles do they take?
- What do they MISS that we can cover?
- What do YouTube comments say? (viewer objections to preempt)

COMMON GROUND BY AUDIENCE:
- Technical audience: What shared professional pain point resonates?
- General audience: What everyday metaphor explains the concept?
- Decision makers: What business outcome matters most?

OUTPUT FORMAT (use these exact headers):

## Cult-Hopping References
| Brand/Person/Concept | Why It Works | Where to Use (Hook/Mid/CTA) |
|---------------------|-------------|---------------------------|
| ... | ... | ... |

## Contrarian Angles (Uno Reverse)
1. **<Angle title>**: <Description>
   - Evidence: <source URL or data point>
2. ...
(minimum 3)

## Mind-Blowing Stats
| Stat | Value | Shock Factor (1-10) | Source URL |
|------|-------|-------------------|-----------|
| ... | ... | ... | ... |
(minimum 5 candidates)

## Common Ground by Audience
- **Technical**: <shared pain point>
- **General**: <everyday metaphor>
- **Decision Makers**: <business outcome>

## Competitor Video Analysis
| Video/Channel | Hook Used | Angle | What They Miss |
|--------------|-----------|-------|---------------|
| ... | ... | ... | ... |

## Viewer Objections to Preempt
1. <Objection viewers will have> — <How to address it in the script>
2. ...

## Primary Open Loop Suggestion
- **Setup** (Scene 01-02): <The question or tension to raise early>
- **Resolution** (Scene 06-08): <Where and how to resolve it>

## Preview Hook Teasers (3 lines for Scene 00)
1. <Bold stat or claim — the scroll-stop opener>
2. <Teaser referencing a mid-video reveal>
3. <Promise statement — "In this video...">

## Raw Research Notes
<Links, quotes, data points>
```

---

### Agent D — Video Production Researcher

**Focus**: Research specifically for VIDEO content — how to SHOW, not just tell. This agent is what makes the workflow **video-content-aware**.

```
You are a video production researcher and visual storyteller preparing material for a HyperFrames (HTML + GSAP) composition.

TOPIC: {topic description}
TOPIC TYPE: {TOPIC_TYPE}
RESEARCH DEPTH: {LIGHT|STANDARD|DEEP}
{PRE-FETCHED CONTENT if available}

Your job: For every key concept in this topic, answer: "How do we SHOW this, not just tell it?" Research visual metaphors, demo opportunities, and scene-ready data that will make this video visually compelling.

The composition will be authored as plain HTML + GSAP timelines. You don't need to know the rendering details — just identify what's worth SHOWING and why.

Research these areas:

VISUAL METAPHORS:
- What real-world or cross-domain metaphors explain abstract concepts?
  (e.g., Swiss Cheese Model for layered safety, J-curve for adoption dip, Roulette Wheel for token prediction)
- What spatial metaphors work? (pipelines, funnels, layers, networks, timelines)
- For each metaphor: what concept does it explain, and how would it animate?

DEMO OPPORTUNITIES:
- Can we SHOW the tool/concept working? (screenshots, code snippets, terminal output)
- Are there before/after transformations that work as split-screen scenes?
- Are there live demos, GIFs, or videos from the creators we could reference?
- What would a "wow moment" demo look like?

SCREENSHOT OPPORTUNITIES:
- Which web pages should we capture as real screenshots? (product homepages, GitHub repos, docs pages, dashboards, blog posts)
- For each: exact URL, which section/area to capture, dark or light mode preference
- Note any pages likely to have auth walls, anti-bot protections, or heavy dynamic loading
- Prioritize pages where the REAL UI is more compelling than a recreation

SCENE-READY DATA POINTS:
- Statistics formatted for animation (number + unit + comparison baseline)
- Data suitable for bar charts, counters, or comparison tables
- Percentages, growth rates, time savings — anything that can be a visual number reveal

ARCHITECTURE / DIAGRAM OPPORTUNITIES:
- Does the topic have a system architecture that can be progressively revealed?
- Are there flowcharts, pipelines, or decision trees?
- What components connect to what? (for box-and-arrow diagrams)

EXISTING VISUAL TREATMENTS:
- How have conference talks visualized this concept?
- What infographics exist?
- What do other YouTube videos show on screen for this topic?

OUTPUT FORMAT (use these exact headers):

## Visual Metaphor Inventory
| Concept | Metaphor | How It Animates | Source/Inspiration |
|---------|----------|----------------|-------------------|
| ... | ... | ... | ... |
(minimum 3 metaphors)

## Demo Opportunities
| What to Demo | Format (screenshot/code/terminal/diagram) | URL (if screenshot) | Dark/Light | Wow Factor (1-10) | Notes |
|-------------|------------------------------------------|---------------------|------------|-------------------|-------|
| ... | ... | https://... or N/A | dark/light/N/A | ... | ... |

## Scene-Ready Data Points
| Data Point | Animated Value | Comparison Baseline | Visual Format |
|-----------|---------------|-------------------|--------------|
| ... | ... | ... | bar chart / counter / side-by-side / etc. |

## Before/After Transformations
| Before State | After State | Visual Treatment |
|-------------|------------|-----------------|
| ... | ... | split-screen / morph / timeline / etc. |

## Architecture Diagram Opportunities
| System/Flow | Components | Progressive Reveal Order | Complexity |
|------------|-----------|------------------------|-----------|
| ... | ... | ... | simple/medium/complex |

## Visual Concepts (Detailed Descriptions)
1. **<Visual name>**: <Detailed description of the visual, how it would look on screen, colors, motion, timing>
2. ...
(these feed directly into Phase 1 scene planning)

## Suggested Scene Structure
| # | Scene Name | Duration Estimate | Key Visual | Key Stat/Quote |
|---|-----------|------------------|-----------|---------------|
| 00 | Preview Hook | 5-10s | ... | ... |
| 01 | Hook | 15-25s | ... | ... |
| ... | ... | ... | ... | ... |

## Hero Visual Recommendation
<The ONE visual that should be the thumbnail / most memorable moment of the video. Describe it in detail.>

## Raw Research Notes
<Links, visual references, screenshots found>
```

---

## WAVE 1.5 — Optional vidiq Enrichment

Probe the available tool list for any tools whose name starts with `mcp__claude_ai_vidiq__`. If present, run these in parallel after Wave 1 completes (do not block Wave 1 on this):

- `mcp__claude_ai_vidiq__vidiq_keyword_research` — query for the topic; pull keyword volume + competition scores
- `mcp__claude_ai_vidiq__vidiq_trending_videos` — for the inferred category, pull current breakout videos
- `mcp__claude_ai_vidiq__vidiq_score_title` — score 2-3 candidate titles drafted from Wave 1 hook research

If vidiq tools are NOT available (the env doesn't expose them, or they error on auth), skip silently — this is enrichment, not a gate. Do NOT fail Phase 0 on vidiq problems.

Fold any results into the synthesized brief under a new section `## Keyword Research (vidiq)` with subsections:
- "Keyword opportunities" (table: keyword | volume | competition score | recommended use)
- "Currently trending in this niche" (top 3 videos with hook + view count)
- "Title scores" (the candidate titles + their vidiq score)

If vidiq was not used, write this section as `## Keyword Research (vidiq)` followed by a single line: `_Skipped — vidiq MCP tools not available in this session._`

---

## WAVE 2 — Synthesis + Quality Gates (Lead, synchronous)

After ALL four agents return (and vidiq enrichment completes or is skipped), synthesize findings into the final content brief.

### Step 2A: Merge & Deduplicate

Review all 4 agent outputs and:
1. **Deduplicate** — remove redundant findings that appear in multiple agents' output
2. **Cross-reference stats** — if Agent C found a stat and Agent A found the same stat with a different value, investigate which source is more authoritative
3. **Resolve conflicts** — if agents disagree on positioning or audience, use Agent A's primary research as the authority

### Step 2B: Tag Visual Potential

For EVERY proof point, feature, and pain point, assign a visual potential tag:
- **HIGH** — Agent D identified a specific visual treatment (metaphor, diagram, demo)
- **MEDIUM** — Concept is visual but no specific treatment identified yet
- **LOW** — Abstract concept, best as text-on-screen with narration

### Step 2C: Build Messaging Hierarchy

Construct the Must/Should/Could/Omit hierarchy using TWO criteria:
1. **Message importance** — how essential to understanding the topic?
2. **Visual showability** — can we SHOW this compellingly? (from Agent D's assessment)

Items that are both important AND visually showable go to "Must Include." Items that are important but hard to visualize may still be "Must Include" but flagged as needing creative treatment.

### Step 2D: Construct Narrative Arc

Build the Kallaway Formula narrative arc using:
- Agent C's hook materials (contrarian angles, mind-blowing stats, cult-hop references)
- Agent A's feature hierarchy
- Agent D's scene structure suggestion
- Agent B's timing signal for "why NOW?"

### Step 2E: Generate Suggested Video Titles

Based on research findings, generate 3-5 video title options:
- At least one stat-led title
- At least one contrarian/provocative title
- At least one "how-to" / solution-oriented title
- All under 60 characters for YouTube display
- If vidiq title scoring ran, include the score next to each candidate

### Step 2F: Run Quality Gates

| Gate  | Check                       | Threshold                  | Action on Fail                                                  |
| ----- | --------------------------- | -------------------------- | --------------------------------------------------------------- |
| QG-0A | Proof points found          | >= 5 with source URLs      | **FAIL** — list specific gaps in "Gaps / Needs User Input"      |
| QG-0B | Contrarian angles found     | >= 3 with evidence         | **FAIL** — report gap, suggest more research                    |
| QG-0C | Visual metaphor suggested   | >= 1                       | **WARN** — suggest using a generic spatial metaphor             |
| QG-0D | Demo opportunity identified | >= 1                       | **WARN** — flag that the video may lack demo moments            |
| QG-0E | SEO keywords found          | >= 3                       | **WARN** — suggest manual keyword research                      |
| QG-0F | All proof points sourced    | URLs present for each      | **FAIL** — mark unsourced claims with ⚠️ in proof points table  |
| QG-0G | Cult-hop references found   | >= 3                       | **WARN** — suggest expanding references                         |
| QG-0H | Receipts (anti-slop gate)   | >= 3 named, linkable items OR `topic_type == CONCEPT` | **FAIL — BLOCKS PIPELINE** — see Step 2H below |
| QG-0I | Thesis present              | One falsifiable sentence in brief | **FAIL** — derive one in Step 2H if missing                |

**FAIL** = report specific gap in "Gaps / Needs User Input" section. In autonomous mode, proceed but flag prominently.
**FAIL — BLOCKS PIPELINE** = QG-0H specifically blocks Phase 1 from running until the receipt gate is satisfied. This is the anti-slop gate — it prevents the model from inventing "studies show 73%..." stats during script generation.
**WARN** = advisory note in the brief, does not block.

### Step 2H: Receipt Gate + Thesis (anti-slop pre-script gate)

This is the gate that prevents AI slop downstream. The model cannot invent "studies show 73%..." or "experts agree..." in Phase 2 if Phase 0 has already collected ≥3 verifiable, linkable receipts AND committed to a falsifiable thesis.

#### Step 2H.1 — Collect Receipts

Build a `## Receipts` block for the content brief. A receipt is:

- A URL (resolvable, not behind auth)
- A version or date (so future drift is detectable)
- A one-line summary of what the receipt verifies

Sources for receipts (in priority order):
1. URLs already in `Links:` from the structured brief
2. URLs Agent A pulled from official docs / changelogs / release notes
3. URLs Agent B found for competitive landscape and adoption signals
4. URLs from the Proof Points table (must already have source URLs per QG-0F)
5. Specific GitHub commits, PRs, issues, or discussion threads (named developer reactions)
6. Quoted statements with named author + venue + date

What does NOT count as a receipt:
- A general claim ("AI tools are improving") with no URL
- A blog post that itself relies on uncited sources
- A WebSearch result snippet without a real underlying URL
- "Many developers find..." or "Experts agree..." style summaries

Target: ≥ 3 receipts. If the brief had `Links:` items, those count. If Agent A pulled changelog/release URLs, those count. If you ran out of receipts after walking the priority list, the topic likely lacks public verifiable evidence — flag it in Step 2H.3 and the user decides.

#### Step 2H.2 — Derive Thesis (if not in brief)

If the structured brief had `**Thesis**:`, use it verbatim — do not rewrite.

If the brief had no Thesis OR the input was a free-form topic string, derive one from research now. The thesis MUST be:

- ONE sentence
- Falsifiable — could be wrong if the facts were different
- Argumentative — not descriptive

| Bad (descriptive) | Good (falsifiable thesis) |
|---|---|
| "Claude Code is changing how developers work." | "Claude Code's plan-first agent mode prevents the codebase damage that direct-edit agents cause — but only if the developer reads the plan before approving." |
| "Skills are markdown files that bundle prompts." | "Skills are not 'another extension system' — they're the first install mechanism that lets ChatGPT-grade prompt engineering ship as version-controlled artifacts in the repo." |
| "The Anthropic-AWS deal is huge." | "The Anthropic-AWS $100B deal is a hedge against Nvidia, not against capacity — Anthropic locked in non-Nvidia silicon before Nvidia's next-gen launch made the price spike permanent." |

In autonomous mode, derive without asking. In interactive mode, present the derived thesis to the user for confirmation before writing the brief.

Store the thesis in the content brief metadata (alongside `voice_profile`).

#### Step 2H.3 — Apply the Gate

```
PASS condition (Phase 1 may proceed):
  receipts_count >= 3
  OR
  topic_type == "CONCEPT" AND user has acknowledged the override

FAIL condition (Phase 1 BLOCKED):
  receipts_count < 3 AND topic_type != "CONCEPT"
```

CONCEPT override behavior:
- For abstract topics (e.g., "What is RAG?", "What is a vector database?") that genuinely have no specific linkable artifacts to point at, the gate accepts `topic_type: CONCEPT`
- BUT the brief MUST still include a Thesis (per QG-0I), even for CONCEPT topics — concepts can still have falsifiable angles
- The brief's Receipts section gets the line: `_Receipt gate waived — topic_type: CONCEPT. Script may not invent stats; Phase 2.5 Pass 5 enforces the authority-without-evidence ban regardless._`

On FAIL (interactive mode):
1. STOP synthesis — do not write the brief yet
2. Tell the user: "Phase 0 found N receipts. Need ≥3 to ship. Either (a) provide additional URLs, (b) confirm `topic_type: CONCEPT` if this is a genuine abstract topic, or (c) abandon the topic — Phase 1 is blocked otherwise."
3. Wait for user input before proceeding to Step 2G

On FAIL (autonomous mode):
1. Write the brief with whatever receipts were found
2. Append a top-level `## ⚠️ RECEIPT GATE FAILED` section listing the count + missing-receipts gap
3. Set `0 - Research` row in `phase-status.md` to `blocked (receipt gate: N/3) <YYYY-MM-DD>`
4. Phase 1 will refuse to start with this status

The downstream effect is non-negotiable. The script-generation pipeline is built around the assumption that the brief contains real, linkable evidence. Skipping the gate guarantees slop at Phase 2.

### Step 2G: Write Content Brief

Assemble the enriched content brief and write to `videos/<slug>/research/content-brief.md`.

</process>

<output>
**Save to**: `videos/<slug>/research/content-brief.md`

The content brief uses this enriched template (ALL sections are mandatory unless marked OPTIONAL):

```markdown
# Content Brief: <Topic>

## Video Metadata
- **Slug**: `<kebab-case>`
- **Template**: <shorts/anthropic | long-form/* — currently only shorts/anthropic>
- **Duration**: <target duration>
- **Tone**: <tone>
- **Voice Profile**: `voice_profile: <tutorial | news-explainer | comparison>` — picked in Step 0E (see Voice Profile heuristic). Determines which `brand-voice-*.md` file Phase 2 reads. Default: `news-explainer`.
- **Target Audience**: <primary and secondary>
- **Key Angle**: <the ONE thing viewers should remember>
- **Topic Type**: <PRODUCT_TOOL | CONCEPT | ARTICLE_RESPONSE | COMPARISON | YOUTUBE_SOURCE>
- **Research Depth**: <LIGHT | STANDARD | DEEP>

---

## Thesis
<ONE falsifiable sentence — a claim that could be wrong. Forces the script to argue, not describe. See Step 2H.2 for examples. Required for both regular and CONCEPT topics.>

---

## Receipts
<≥ 3 named, linkable items — OR a single line `_Receipt gate waived — topic_type: CONCEPT._` if the override was applied. See Step 2H for the gate logic.>

1. <URL> — <version or date> — <what this verifies>
2. <URL> — <version or date> — <what this verifies>
3. <URL> — <version or date> — <what this verifies>

---

## Core Value Proposition
<One sentence: "X helps Y achieve Z by doing W">

---

## Target Audience
**Primary**: <who, what they know, what they care about>
**Secondary**: <who else might watch>
**What they know**: <baseline knowledge level>
**What they care about**: <motivations>

---

## Pain Points
1. **<Pain point title>**: <relatable scenario> [VISUAL: HIGH/MEDIUM/LOW]
2. ...
(minimum 3, target 5)

---

## Key Features & Benefits
| Feature | Benefit (user-facing) | Differentiator? | Metric | Visual Potential | Demo? |
|---------|----------------------|-----------------|--------|-----------------|-------|
| ... | ... | Yes/No | ... | HIGH/MED/LOW | Yes/No |

---

## Proof Points (Scene-Ready)
| Stat/Claim | Formatted Value | Comparison Baseline | Source URL | Visual Format | Shock Factor |
|-----------|----------------|-------------------|-----------|--------------|-------------|
| ... | "21% more tasks" | vs pre-AI baseline | https://... | bar chart | 7/10 |
(minimum 5, all must have source URLs — unsourced claims marked with ⚠️)

---

## Visual Concepts
1. **<Visual name>**: <Detailed description — what it looks like, how it animates, colors, timing>
2. ...
(from Agent D — these feed directly into Phase 1 scene planning)

---

## Visual Metaphor Inventory
| Concept | Metaphor | How It Animates | Source/Inspiration |
|---------|----------|----------------|-------------------|
| ... | ... | ... | ... |

---

## Demo Opportunity Inventory
| What to Demo | Format | URL (if screenshot) | Dark/Light | Wow Factor | Notes |
|-------------|--------|---------------------|------------|-----------|-------|
| ... | screenshot/code/terminal/diagram | https://... or N/A | dark/light/N/A | 1-10 | ... |

---

## Before/After Transformations (OPTIONAL)
| Before State | After State | Visual Treatment |
|-------------|------------|-----------------|
| ... | ... | split-screen / morph / timeline |

---

## Architecture Diagram Opportunities (OPTIONAL)
| System/Flow | Components | Reveal Order | Complexity |
|------------|-----------|-------------|-----------|
| ... | ... | ... | simple/medium/complex |

---

## Competitive Landscape
| Alternative | Key Difference | Where Topic Wins | Where Alternative Wins |
|------------|---------------|-----------------|---------------------|
| ... | ... | ... | ... |

---

## Notable Adopters
| Company/Person | How They Use It | Why It Matters for Video |
|---------------|----------------|------------------------|
| ... | ... | cult-hop / social proof / credibility |

---

## Market Context & Timing Signal
- **Market size**: ...
- **Growth**: ...
- **Why NOW**: <what changed recently>

---

## Messaging Hierarchy
### Must Include [Visual Treatment]
- <item> [<visual approach from Agent D>]
- ...

### Should Include
- ...

### Could Include
- ...

### Omit
- ...

---

## Hook Architecture

### Cult-Hopping References
| Brand/Person/Concept | Why It Works | Where to Use (Hook/Mid/CTA) |
|---------------------|-------------|---------------------------|
| ... | ... | ... |
(minimum 3)

### Common Ground by Audience
- **Technical**: <shared pain point>
- **General**: <everyday metaphor>
- **Decision Makers**: <business outcome>

### Contrarian Angles (Uno Reverse)
1. **<Angle>**: <description>
   - Evidence: <source URL or data>
2. ...
(minimum 3)

### Mind-Blowing Stats
| Stat | Value | Shock Factor (1-10) | Source URL |
|------|-------|-------------------|-----------|
| ... | ... | ... | ... |
(minimum 5 candidates)

### Preview Hook Teasers (for Scene 00)
1. <Bold stat or claim — the scroll-stop opener>
2. <Teaser referencing a mid-video reveal>
3. <Promise statement — "In this video...">

### Primary Open Loop Suggestion
- **Setup** (early): <question or tension to raise>
- **Resolution** (late): <where and how to resolve it>

---

## Suggested Narrative Arc (Kallaway Formula)
1. **Context Lean-In**: <mind-blowing fact or pain point>
2. **Scroll-Stop**: <"But..." interjection>
3. **Contrarian Snapback**: <unexpected path>
4. **Solution**: <introduce the topic/product — benefit-first>
5. **Features (Benefit-Led)**: <which 3-5 features deserve scenes>
6. **Trust**: <proof point that closes the credibility gap>
7. **CTA**: <what the viewer should do next>

---

## Suggested Scene Structure
| # | Scene Name | Duration Est. | Key Visual | Key Stat/Quote |
|---|-----------|--------------|-----------|---------------|
| 00 | Preview Hook | 5-10s | ... | ... |
| 01 | Hook | 15-25s | ... | ... |
| ... | ... | ... | ... | ... |
(from Agent D, refined in synthesis)

---

## Suggested Video Title Options
1. **"<title>"** — <rationale> [vidiq score: N/100 if available]
2. ...
(3-5 options, all under 60 characters)

---

## SEO Keywords
| Keyword / Phrase | Search Intent | Volume Estimate |
|-----------------|--------------|----------------|
| ... | ... | high/medium/low |

---

## Keyword Research (vidiq)
<vidiq enrichment results, OR a single line "_Skipped — vidiq MCP tools not available in this session._" if not run>

---

## Technical Terms (TTS Pronunciation)
| Term | Pronunciation Note |
|------|-------------------|
| ... | Write as single word / needs spacing / phonetic guide |

---

## Viewer Objections to Preempt
1. **<Objection>**: <How to address in script>
2. ...

---

## Competitor Video Analysis (OPTIONAL)
| Video/Channel | Hook Used | What They Miss |
|--------------|-----------|---------------|
| ... | ... | ... |

---

## Quality Gate Results
| Gate | Check | Result | Notes |
|------|-------|--------|-------|
| QG-0A | Proof points >= 5 | PASS/FAIL | ... |
| QG-0B | Contrarian angles >= 3 | PASS/FAIL | ... |
| QG-0C | Visual metaphor >= 1 | PASS/WARN | ... |
| QG-0D | Demo opportunity >= 1 | PASS/WARN | ... |
| QG-0E | SEO keywords >= 3 | PASS/WARN | ... |
| QG-0F | All stats sourced | PASS/FAIL | ... |
| QG-0G | Cult-hop refs >= 3 | PASS/WARN | ... |
| QG-0H | Receipts >= 3 OR CONCEPT | PASS/FAIL | <BLOCKING — receipt gate. Override: topic_type=CONCEPT> |
| QG-0I | Thesis present | PASS/FAIL | <one falsifiable sentence required> |

---

## Gaps / Needs User Input
- <Specific gap or decision needed>
- ...
(Quality gate failures are listed here automatically)

---

## Sources
| Source | URL | Used For |
|--------|-----|---------|
| ... | ... | ... |
(all URLs from all agents, deduplicated, with "Used For" column)
```

**Report to user**:
1. Summary of what was found (3-5 bullet points)
2. Recommended video angle
3. Quality gate results (pass/fail/warn counts)
4. Suggested scene count based on content density
5. Whether vidiq enrichment ran
6. Any gaps in research that need user input
7. Next step: Run `/diy-yt-creator:phase1-plan <slug>` to plan the composition

### Update Phase Status

Update (or create) `videos/<slug>/phase-status.md`. If it does not exist, create it with this template:

    # Phase Status: <slug>

    | Phase | Status | Completed |
    |-------|--------|-----------|
    | 0 - Research | pending | |
    | 1 - Plan | pending | |
    | 2 - Script | pending | |
    | 2.5 - Critique | pending | |
    | 2a - TTS Script | pending | |
    | 2b - Fact Check | pending | |
    | 3.5 - Retention | pending | |

    **Status vocabulary**: `pending` | `in-progress` | `done` | `done <details>` | `blocked (<reason>)`

Then set the `0 - Research` row to `done <YYYY-MM-DD>` (today's date).

**Note**: This pipeline ends at Phase 3.5. After 3.5, hand off to `/diy-yt-creator:new-anthropic-short <slug>` (or another template skill) to build the HTML composition. Phase 3 (audio generation) and Phase 4-5 (composition build + render) are handled by `npx hyperframes tts`, the composition skill, and `npx hyperframes render` respectively — they are not pipeline phases here.
</output>
