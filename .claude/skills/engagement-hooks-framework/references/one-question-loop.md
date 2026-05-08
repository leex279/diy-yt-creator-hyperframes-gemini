# One-Question-Loop — sentence-to-sentence pull

The viewer's brain is a question machine. Every sentence either raises a new question (pulling them forward) or doesn't (giving them an exit). High-retention narration is engineered so **every sentence answers the question raised by the previous one — and raises a new one**.

> "Step 1 (Context): Google just dropped Gemini 3. (Viewer thinks: What can it do?) — Step 2 (The How): It uses a new logic model to solve complex math in seconds. (Viewer thinks: Is it expensive?) — Step 3 (Implications): It's free for the first 100 users here." — Faceless Creator's Master Blueprint

## The mechanic

```
Sentence 1  →  raises Q1
Sentence 2  →  answers Q1, raises Q2
Sentence 3  →  answers Q2, raises Q3
Sentence 4  →  answers Q3, raises Q4
...
```

Each sentence has TWO jobs. If it only answers, the loop closes and the viewer has permission to leave. If it only raises, it feels like a teaser hose with no payoff.

## Why this matters more than "Boxer's Rhythm" or "Jagged Edge"

Existing references in this repo (`faceless-tech-scriptwriting-playbook.md` §4) emphasize **rhythmic variation** (Gary Provost, Boxer's Rhythm). That's true and useful — but rhythm controls *how it sounds*, not *whether the viewer stays*. The One-Question-Loop controls *whether the viewer stays*.

Rhythm without question-loop = a beautifully cadenced narration that lets the viewer drift off because nothing pulls them forward.

Question-loop without rhythm = monotone but high-retention (the viewer keeps watching despite the monotony).

The goal is both. But if you can only get one, get the loop first.

## How to author

### Step 1 — Map the question chain BEFORE writing prose

For each scene, write the question chain on its own line. 5-8 questions for a 30s scene. Example for a 30s "skills system" scene:

```
Q1: What's a skill?
Q2: How is that different from CLAUDE.md?
Q3: When does it auto-load?
Q4: Can I make my own?
Q5: What does the file look like?
Q6: How do I install one?
Q7: Where does Claude find them?
```

This is the spine. The narration is just the answer-and-raise wrap around each question.

### Step 2 — Convert the chain to prose

For each question, write a sentence that:
- **Answers the previous question** (concrete, specific)
- **Raises the next question** (the last clause should be the seed of Q+1)

Example:

```
Q1: What's a skill?
S1: A skill is a packaged piece of context that auto-loads when Claude detects you need it.
                                                                ^^^^^^^^^^^^^^^^^^^^^^
                                                         (raises Q2: how detect?)

Q2: How does it detect?
S2: It scans your message for triggers — keywords, file types, intent — and loads the matching skill before generating a response.
                                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                                                  (raises Q3: what does the matching feel like?)

Q3: How is that different from CLAUDE.md?
S3: CLAUDE.md is always in context. Skills are conditional — only loaded when relevant — so you can have hundreds without bloating context.
                                                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                                                       (raises Q4: hundreds? where do they live?)
```

The technique: **end each sentence on the seed of the next question**. Not a new claim. Not a new fact. The clause that triggers the brain to ask the next question.

### Step 3 — Verify the chain

Read the script with a colleague (or aloud to yourself, eyes closed). After each sentence, pause. Does a question form in your head naturally? If yes, the next sentence has a job. If no, the loop is broken — rewrite that sentence.

This IS the **Eyes-Closed Test** mentioned in the Master Blueprint:

> "Listen to your script with your eyes closed. If the pacing feels slow or the clarity drops, your Absorption Rate is failing. Clarity is the only KPI that matters in a script."

The Eyes-Closed Test detects two failure modes:
1. **Loop break** — a sentence doesn't raise the next question, the brain coasts.
2. **Clarity drop** — a sentence answers a question the viewer didn't ask. The chain is misaligned.

## Common loop-break patterns

| Failure | Symptom | Fix |
|---|---|---|
| Listing without questions | "Skills auto-load. Skills are scoped. Skills can be shared." | Convert to question-driven: "Skills auto-load — but only when relevant. How does Claude know what's relevant?" |
| Stacking facts without progression | "GPT-4 has 1.7T parameters. It runs on H100 GPUs. It costs $30/M tokens." | Lead with the question that connects them: "GPT-4 needs 1.7 trillion parameters. That's why it runs on H100 GPUs and costs thirty dollars per million tokens." |
| Premature payoff | All info dumped in sentence 2; sentences 3-8 add no question | Cut at sentence 2 or restructure to delay the full payoff across 4 sentences |
| Tangent without return | Sentence 4 raises Q4, but sentences 5-7 answer a different question | Either return to Q4 by sentence 6, or restructure the chain |

## The "Two-Dopamine-Hits-in-60s" rule

Question chains aren't enough by themselves. The Master Blueprint requires **two tactical, useful nuggets within the first 60 seconds**. These are the dopamine hits that prevent churn during the early absorption window.

A "nugget" is:
- A specific tactical takeaway (not a vague principle)
- Immediately actionable or immediately memorable
- Self-contained (the viewer can extract it as a tweet)

Examples:
- "Add `claude-code-version: latest` to your CLAUDE.md and the skills system stays current automatically." (specific, actionable)
- "Tags only matter for spelling-disambiguation now — Apple/apple, kid the goat / Kid the goat." (specific, memorable)
- "A 5x outlier video should get cloned 3 times in your next batch of 10. That's the carry-forward rule." (specific, actionable)

Place hit #1 around 15-20s and hit #2 around 40-50s. Each hit closes a question loop with a payoff strong enough to feel like value-already-delivered. Then immediately raise the next question.

## Compatibility with brand-voice profiles

The One-Question-Loop pattern is profile-agnostic — it works for tutorial, news-explainer, and comparison voices.

| Profile | Loop adaptation |
|---|---|
| **Tutorial** | Each step is one Q-A pair. "First, install. (How?) Run `brew install foo`. (Then?) Add the API key. (Where?) In `.env`." |
| **News-explainer** | Each connector (`because`, `why`, `to <verb>`) is the explicit question form. "Why? Because Claude's growth is exploding." |
| **Comparison** | Each tradeoff opens a question. "Cursor wins on speed. (At what cost?) Privacy — every keystroke ships to their servers." |

The connectors required by `brand-voice-news-explainer.md` (≥3 in body, ≥2 unique types) ARE question markers. A connector-rich script naturally satisfies the loop pattern. If your news-explainer script has 5 connectors and still feels listy, you're probably stating connectors without raising questions — fix by ending each connector-clause on a question seed.

## Self-check

Before declaring a script done:

1. **Question-chain map exists.** A 5-8 line outline of the questions, written before the prose.
2. **Eyes-Closed Test passes.** Read aloud, eyes closed. After each sentence, a question forms naturally.
3. **No 3+ consecutive answer-only sentences.** A loop break of 3 sentences = 3 seconds of viewer drift = ~1.5% of a 200s video.
4. **Two dopamine hits land before 60s.** Mark them in the script with `(NUGGET 1)` and `(NUGGET 2)` annotations during authoring; remove before saving.
5. **The final sentence of each scene seeds the next scene's first question.** Cross-scene loops are how 30s shorts feel like 60s of value.
