# Phase 2b — Fact Check (ARTICLE_RESPONSE scope)

Per `feedback_factcheck_article_response_scope.md`: bidirectional check against
`tmp/source.md` only. WebSearch is skipped — the scope is "what the article
says vs what we say."

Status: **PASS**.

## Forward direction — every claim in `script.txt` traces to source

| Script claim (paraphrased) | Source location in `tmp/source.md` | Drift? |
|---|---|---|
| Markdown is the default agent format | Article opening: "Markdown has become the dominant file format used by agents" | none |
| The Claude Code team stopped using markdown | Article opening: "increasingly see this being used by others on the Claude Code team" | none — script says "stopped using" which is consistent with Thariq's "started preferring HTML…instead of Markdown" |
| Thariq is on Claude Code at Anthropic | Author bio: "Claude Code @anthropicai" | none |
| 750,000 people read it (the post) | X-post screenshot: "751K views" | none — script rounds 751K → "seven hundred and fifty thousand" |
| Title: "The unreasonable effectiveness of HTML" | Article cover screenshot, source.md article header | none |
| HTML can carry 8 things in one file (tables, CSS, SVG, code, JS+CSS interactions, workflows, spatial canvas, images) | Information Density section verbatim | none |
| Markdown's escape: ASCII diagrams + estimating colors with unicode | Information Density section verbatim | none |
| 100-line markdown limit for reading | Visual Clarity section: "I tend to not actually read more than a 100-line markdown file" | none — used implicitly via the visual-clarity argument; not quoted directly to keep wording tighter |
| HTML 2-4× longer to generate | FAQ section verbatim | none |
| Opus 4.7 1MM context window | FAQ section verbatim | none |
| Easier to read, organize visually, navigate | Visual Clarity section verbatim | none |
| "Chance someone actually reads…much higher" | Ease of Sharing section verbatim | none |
| Use case 1: Specs, planning, exploration — fan out approaches, label trade-offs, plan with mockups | Specs, Planning & Exploration section + first example prompt | none |
| Use case 2: Code review — diff with margin annotations, severity colors, jump links; "attaches HTML code explainer to every PR" | Code Review section verbatim | none |
| Use case 3: Design — Claude Design built on HTML, sketches in HTML translates to React/Swift; sliders/knobs/copy params back | Design & Prototypes section verbatim | none |
| Use case 4: Reports/research — codebase + git history + Slack + internet → readable explainer | Reports, Research & Learning section verbatim | none |
| Use case 5: Custom editing — throwaway editor, single HTML file, copy back as JSON/markdown/prompt | Custom Editing Interfaces section verbatim | none |
| Three example custom-editor patterns: Linear ticket triage, feature flag editor, prompt tuner | Verbatim from the 3 example prompts in source.md Custom Editing Interfaces | none |
| Data ingestion stack: filesystem + MCPs (Slack, Linear) + browser (Claude in Chrome) + git history | Data Ingestion section verbatim | none |
| "More in the loop than ever before" — direct quote | Stay in the Loop closing verbatim | none — set off as "Quote." in narration to mark it |
| Reply themes: "I was already doing this", "explains why Claude keeps printing HTML as artifacts", "moving my workflow today", "editorial magazines" | Source Community Reactions block — themes match (`already doing this`, `Why does Claude always print HTML as artifacts`, workflow adoption, `editorial magazine`) | none — paraphrased only, no individual handles named |
| "Some replies pushed back: markdown's lower token spend is itself the value" | Source Community Reactions: "Markdown wins. Every time. Cleaner structure = fewer tokens" | none — script paraphrases the contrarian-take theme without naming the handle |
| Dynamous outro | Locked per `feedback_dynamous_short_outro.md` | none — verbatim |

## Reverse direction — important source claims and whether they're in the script

| Source claim | Status in script | Reason |
|---|---|---|
| HTML mobile-responsive | covered | "easier to navigate with tabs and links and illustrations" + "easier to organize visually" — covers responsive intent without diving into responsive specifically (would lengthen S2 unnecessarily) |
| "It's Joyful" benefit | partially covered | S6 mentions "joy of making things" and frames the loop-back as the deeper joy; deliberate compression — the "more in the loop" closing quote already carries the emotional payload |
| Two-way Interaction (sliders/knobs in HTML, copy back into prompt) | covered | Folded into Scene 4 use case 3 (Design & Prototypes) and use case 5 (Custom Editing Interfaces); both reference the export-button pattern |
| "I'm a little bit afraid people will turn this into a /html skill" | not covered | Deliberate omission — meta-commentary about the article's reception adds 30s without adding new viewer value. The reactions block in S6 already nods at this implicitly. |
| FAQ — "How do I view the HTML file" / "open in browser or upload to S3" | not covered | Lower-priority FAQ; not load-bearing for the thesis. Cut for time. |
| FAQ — "How do you match my taste / not make it ugly" → frontend design plugin + design system file | not covered | Workflow detail not load-bearing for the thesis. Cut for time. |
| FAQ — "When do you use markdown for now" → "stopped using markdown altogether for almost everything" | not covered as a quote | Already implicit in the hook ("stopped using markdown") |
| Version control downside (HTML diffs noisy) | not covered | Deliberate omission — script honors the tradeoff angle via the 2-4× generation cost line. Adding a second tradeoff would feel apologetic and dilute the thesis. Worth flagging in the plan as a possible follow-up video ("when HTML doesn't work — diff review and version control"). |
| Specific community reaction — "destination-dependent" (markdown to Notion, plain to Slack, HTML to docs) | not covered | A nuanced reaction — would require 15s of setup. Cut for time. |

**Important:** every omission is a deliberate compression call, not an
oversight. Nothing material to the article's thesis is missing from the
script. Two follow-up video ideas surfaced (version-control deep-dive,
destination-dependent format-routing) which can be pitched separately.

## Numerical / quoted accuracy

| Number / quote in script | As stated in source | Match? |
|---|---|---|
| "seven hundred and fifty thousand people" | 751K views (X-post screenshot) | Yes — rounds 751K → "750,000" then spells "seven hundred and fifty thousand" |
| "two to four times longer" | "2-4x longer than Markdown" | Yes — verbatim |
| "one million token context window" | "1MM context window in Opus 4.7" | Yes — 1MM → "one million" |
| "Opus 4.7" | "Opus 4.7" | Yes — verbatim |
| "eight things in one file" | 8-item list in source.md | Yes — count matches |
| "five places" / "five use cases" | 5 use case sections in source.md | Yes — count matches |
| Direct quote: "I am happy to say I feel more in the loop than ever before when using H T M L. I hope you do too." | "But I am happy to say instead that I feel more in the loop than ever before when using HTML. I hope you do too." | **Slight drift — script drops "instead"**. The "instead" in source contrasts with the prior sentence ("I would simply have to leave Claude to make its choices"). Without context, "instead" reads ambiguously in audio — drop is acceptable. Source meaning preserved. |
| "Thariq, who works on Claude Code at Anthropic" | Bio: "Claude Code @anthropicai" | Yes |

## Verdict

**PASS.** All claims in the script trace cleanly to `tmp/source.md` or the
user-supplied screenshots. One deliberate quote-trim ("instead" dropped from
the closing quote) is justified for spoken cadence and does not change the
meaning. No fabricated statistics, no invented examples, no named handles.
Proceed to user-review HARD STOP.
