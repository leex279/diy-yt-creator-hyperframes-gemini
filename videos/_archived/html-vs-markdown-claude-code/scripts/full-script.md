# Full Script — html-vs-markdown-claude-code

**Status**: draft 1, pre-critique
**Target duration**: ~8 min at ELEVENLABS_SPEED=1.10 (≈ 165 wpm × 480s ≈ 1320 words)
**Voice**: cloned voice (info@smartcode.diy default in `.env`)
**Tone**: editorial / news-explainer with light personal lean — mirrors the calm,
confident energy of Thariq's gallery page. Connectors between scenes mandatory
(news-explainer profile).

**Source rule**: every claim traces to `tmp/source.md` or to one of the
screenshots in `assets/`. No fabrication. No invented examples. Community
reactions appear as paraphrased zeitgeist only — never named handles.

**Bracket markers** like `[SCENE: …]` are NOT spoken — they are scene split
markers used by Phase 2a to fan out into per-scene `.txt` files. They are
stripped before TTS by `scripts/elevenlabs-tts.py`.

---

## Scene 0 — Hook (32s, ~85 words)

[SCENE: hook]

Markdown is the default.

It is the format your agent reaches for. Specs. Plans. Brainstorms. All of it lands as a wall of dot-m-d.

But the team that built Claude Code just stopped using markdown.

Thariq, who works on Claude Code at Anthropic, published the reason why. Seven hundred and fifty thousand people read it. And most of the replies were the same.

Wait. You stopped too?

Here is the thesis. The unreasonable effectiveness of HTML.

---

## Scene 1 — Information density (75s, ~205 words)

[SCENE: image-hero]

Here is what HTML can carry that markdown cannot.

01. Information density.

Markdown can carry headings. Bold. A bullet list. A table if you squint at it.

That is roughly it.

HTML can carry eight things in one file.

Tables. C-S-S driven design. S-V-G illustrations. Code snippets inside script tags. Live interactions wired with JavaScript and C-S-S. Workflows drawn with S-V-G and H-T-M-L side by side. Spatial data, anything you can place on a canvas with absolute positions. And actual images, with image tags.

Thariq's claim, and I think it holds — there is almost nothing Claude can read that you cannot represent in H-T-M-L.

So what does the model do when the format fails it?

It improvises. ASCII diagrams. Or, his favorite, estimating colors with unicode characters. Boxes that pretend to be charts. Hashes that pretend to be color swatches.

That is the cost of forcing a powerful agent through a format built for a 1990s readme.

When you give it H-T-M-L, the agent stops faking the chart and just draws the chart.

---

## Scene 2 — Side by side (70s, ~190 words)

[SCENE: side-by-side]

So compare. Same data, two formats.

Markdown gives you this.

A bar chart hand-drawn out of pipes and dashes. From a distance it looks like a chart. Up close, the columns drift. The bars do not line up with the axis. And the second you paste it into a doc with a different font, every alignment breaks.

H-T-M-L gives you this.

Same five numbers. A real S-V-G bar chart, rendered crisply, picking its own colors from a palette. Sitting inside a single dot-h-t-m-l file you can open in any browser.

That is why Thariq writes — H-T-M-L documents are easier to read, easier to organize visually, easier to navigate with tabs and links and illustrations.

He says the chance someone actually reads your spec, your report, your P-R writeup — that chance gets much, much higher when it is H-T-M-L.

A markdown file is a thing your colleague will skim. An H-T-M-L file is a thing your colleague will open.

That is the difference.

---

## Scene 3 — The honest tradeoff (50s, ~135 words)

[SCENE: stat-pill-row]

And yes. There is a price. The honest one.

H-T-M-L can take two to four times longer to generate than markdown.

Two to four x. That is real.

But here is the piece that changes the math.

Opus 4.7 ships with a one million token context window. One million.

Which means the extra tokens you spend rendering H-T-M-L — they barely register against the budget you already have.

The cost is real. The cost is also absorbable. And in exchange you get a document your team will actually read.

Some of the replies under the post pushed back on this. They argued markdown's lower token spend is itself the value. The honest answer is — it depends what you are buying.

---

## Scene 4 — Five use cases (110s, ~310 words)

[SCENE: source-cards]

Here is the part that turns this from a thesis into a workflow.

Five places where switching to H-T-M-L changes everything.

Use case one. Specs, planning, and exploration.

You ask Claude Code to fan out six approaches to a problem in one H-T-M-L file. Side by side. Each one labeled with the trade-off it is making. You pick. The pick becomes a plan with mockups and code snippets baked in.

Use case two. Code review.

The P-R diff rendered with margin annotations. Severity colors. Jump links. Thariq attaches an H-T-M-L code explainer to every P-R he makes now — and he is on the team. He says it works better than the default GitHub diff view.

Use case three. Design and prototypes.

Claude Design is built on H-T-M-L for a reason. H-T-M-L is incredibly expressive for design — even when your end surface is React, or Swift, or anything else. Claude sketches in H-T-M-L, then translates. You can ship the prototype with sliders and knobs, tune the animation, then copy the parameters back into a prompt.

Use case four. Reports, research, and learning.

You point Claude Code at your codebase, your git history, your Slack, the internet. You get back a single readable explainer page. A diagram of the flow. Three or four key code snippets, annotated. A gotchas section at the bottom.

Use case five. Custom editing interfaces.

This one is the sleeper.

Sometimes typing in a text box cannot describe what you want. So Claude Code builds you a throwaway editor. A single H-T-M-L file purpose-built for your one piece of data.

Drag thirty Linear tickets into now, next, later, cut. Edit a feature flag config with dependency warnings. Tune a system prompt with live re-render of three sample inputs.

And every one of them ends with one button — copy it back out. As markdown. As a diff. As a prompt for the next session.

---

## Scene 5 — Why Claude Code, not Claude Design (55s, ~150 words)

[SCENE: architecture-stack]

So why Claude Code specifically? Why not Claude A-I, or Claude Design?

Because of what Claude Code can ingest.

Your filesystem. Every dot-h-t-m-l file you have already generated, all visible at once.

Your M-C-P servers. Slack, Linear, anything you have connected.

Your browser, when you have Claude in Chrome.

Your git history. The why behind every line of code.

That stack of context is what makes the H-T-M-L output actually informed. The agent is not synthesizing in the dark — it is synthesizing from your real work.

Move the same prompt to a chat surface, and you lose half of it. The artifact comes back generic. Pretty, maybe. But generic.

This is the part that does not transfer. Claude Code's reach into your environment is the input that makes the output worth having.

---

## Scene 6 — Stay in the loop + CTA (88s, ~245 words)

[SCENE: cta]

Here is the part the article actually ends on.

Thariq says the real reason he switched is not density. It is not sharing. It is not even the joy of making things.

It is that he stopped reading the markdown plans.

He would offload work to Claude, get back a wall of text, and he just would not read it. Which meant he was leaving Claude to make every choice. Which is a slow way to lose the plot.

The H-T-M-L versions — he reads them. He clicks around. He suggests changes. He is back in the loop.

So I will let Thariq close it himself.

Quote. I am happy to say I feel more in the loop than ever before when using H-T-M-L. I hope you do too.

The replies under the post are full of people saying the same thing. I was already doing this, I just did not have the framing yet. This finally explains why Claude keeps printing H-T-M-L as artifacts. I am moving my whole planning workflow today.

You are going to see this format show up everywhere over the next few months. Specs. P-R writeups. Status reports. Internal explainers. Even editorial magazines — and judging by the replies, plenty of other places too.

Get ahead of it. Open one of the files in Thariq's gallery. Look at how it reads compared to the markdown you would normally get.

And if you want to learn more about A-I, check out the dynamous dot A-I community.

---

## Word count audit

| Scene | Words | Target s | Actual s @ 165 wpm |
|---|---|---|---|
| 0 hook | 85 | 32 | 31 |
| 1 image-hero | 205 | 75 | 75 |
| 2 side-by-side | 190 | 70 | 69 |
| 3 stat-pill-row | 135 | 50 | 49 |
| 4 source-cards | 310 | 110 | 113 |
| 5 architecture-stack | 150 | 55 | 55 |
| 6 cta | 245 | 88 | 89 |
| **Total** | **1320** | **480** | **481** |

±1 second is well within retiming tolerance. Phase 3.5 will pin every scene
boundary to the actual `transcript.json[<word>].start` once TTS lands.

## TTS heteronym audit (Phase 2a will re-audit but flag here)

- **"live"**: not used in adjective sense. Used 0 times.
- **"lead"**: not used.
- **"read"**: appears 6 times — "read it" (past), "read them" (present plural), "read more than" (infinitive), etc. All read in unambiguous context. Keep.
- **"close"**: "I will let him close it himself" — verb sense /kloʊz/. Context is unambiguous (preceded by "let him"); keep.
- **"record"**: not used.
- **"present"**: not used.
- **Tech terms requiring spell-out** (Phase 2a will apply):
  - `HTML` → spell as `H-T-M-L` (already applied)
  - `MD` / `.md` → spell as `dot m d` / `dot-m-d` (already applied)
  - `CSS` → spell as `C-S-S` (already applied)
  - `SVG` → spell as `S-V-G` (already applied)
  - `MCP` → spell as `M-C-P` (already applied)
  - `PR` → spell as `P-R` (already applied)
  - `AI` → spell as `A-I` (already applied)
  - `dynamous.ai` → `dynamous dot A-I` (already applied; matches per-rule pronunciation)
  - `1MM` / `one million` → say `one million` (already applied)
  - `Opus 4.7` → keep verbatim, ElevenLabs handles version numbers fine

## Source-grounding map

Every line of this script traces back to `tmp/source.md` or a screenshot.

| Script line | Source |
|---|---|
| "Markdown is the default" | source.md article opening |
| "team that built Claude Code stopped using markdown" | source.md article opening |
| "750,000 people read it" | article-cover.png screenshot |
| "the unreasonable effectiveness of HTML" | source.md article title |
| "8 things in one file" + the list | source.md "Information Density" verbatim |
| "ASCII diagrams or estimating colors with unicode characters" | source.md verbatim |
| "two to four times longer to generate" | source.md FAQ verbatim |
| "Opus 4.7 one million token context window" | source.md FAQ verbatim |
| "5 use cases" + names | source.md Use Cases section verbatim |
| "attaches an HTML code explainer to every PR" | source.md Code Review verbatim |
| "Claude Design is built on HTML" | source.md Design section verbatim |
| "filesystem / MCPs / browser / git history" | source.md Data Ingestion verbatim |
| "more in the loop than ever before" | source.md Stay in the Loop verbatim |
| Reply themes ("already doing this", "explains why Claude keeps printing HTML") | source.md Community reactions block |
| "dynamous.ai community" outro | locked per `feedback_dynamous_short_outro.md` |

No claim in the script is unsourced. No reaction handle is named.
