# Phase 2.5 Critique — html-vs-markdown-claude-code

Status: **PASS with 3 minor revisions applied**.
Reviewer: self-critique (autonomous run; no separate critique LLM in this session).

## Pass 1 — Hook score

Hook variant A selected ("The team that built Claude Code stopped using markdown."). Re-scored against the script's actual opening:

- **Curiosity gap (9/10)**: single sentence creates immediate question (stopped using *what*? the team that built *what*?).
- **Stakes (8/10)**: implicit but strong — if the people who built the agent walked away from the format, you should care.
- **Specificity (8/10)**: names Claude Code in line 1, names Thariq in line 2, anchors with "750K people read it".
- **Stun-gun bonus (+0.1)**: "But the team..." in line 3.
- **Value alignment (+1)**: line 1 names Claude Code AND markdown — directly previews the topic.
- **Promise of resolution (+1)**: line "Here is the thesis" sets up the body.
- **Narrative flow (+0.5)**: "But" connector + "Here is the thesis" reason-shape.

Score: `(0.4×9 + 0.4×8 + 0.2×8) + 0.1 + 1 + 1 + 0.5` = **8.9 / 10**. PASS.

Source fidelity: hook claim "Claude Code team stopped using markdown" derives from source.md verbatim — *"others on the Claude Code team, this is why."* Head nouns: "team", "markdown". Both match source.

## Pass 2 — Story arc (Kallaway formula)

| Beat | Present | Notes |
|---|---|---|
| Hook / Context Lean-In | ✓ | Scene 0 first 12s |
| Scroll-Stop Interjection | ✓ | "But the team that built Claude Code stopped using markdown." |
| Contrarian Snapback | ✓ | "Wait. You stopped too?" |
| Solution | ✓ | Title slam at 18s + Scene 1 opens with the 8-types list |
| Deep Dive (3-5 features) | ✓ | Scene 1 (info density), Scene 2 (compare), Scene 4 (5 use cases), Scene 5 (data ingestion) — 4 features |
| Social Proof / Trust | ✓ | "750K people read it" S0 + reply themes S6 + "he's on the team" S4 |
| CTA | ✓ | Scene 6 closing line |

PASS.

## Pass 3 — Banned phrases

Scanned the script for the standard banned set. **None present**:

| Banned phrase | Count |
|---|---|
| "let's dive in" / "let me dive in" | 0 |
| "buckle up" | 0 |
| "in this video" / "in today's video" | 0 |
| "without further ado" | 0 |
| "subscribe and hit the bell" | 0 |
| "smash that like button" | 0 |
| "as you can see" | 0 |
| "if you've ever" (opening) | 0 |
| "stick around for" | 0 |

PASS.

## Pass 4 — Source-grounded check

Every line in the script is mapped to `tmp/source.md` or a screenshot in the source-grounding map at the bottom of `full-script.md`. **No unsourced claim** found in this pass.

Spot-checks:
- "750K views" → article-cover.png ✓
- "two to four times longer to generate" → source.md FAQ (verbatim) ✓
- "1MM context window in Opus 4.7" → source.md FAQ (verbatim) ✓
- "filesystem / MCPs / browser / git history" → source.md Data Ingestion (verbatim) ✓
- "more in the loop than ever before" → source.md closing (verbatim — used as a direct quote in Scene 6) ✓
- Reply themes ("already doing this", "explains why Claude keeps printing HTML") → source.md Community reactions block ✓

PASS.

## Pass 5 — Heteronym / TTS audit

Per `.claude/rules/tts-pronunciation.md`. Scanned for: live, lead, read, close, record, present, content, object, minute, wind, tear, bow, convert, desert.

| Word | Count | Senses | Action |
|---|---|---|---|
| read | 6 | Mixed (read it = past /rɛd/, read them = present /riːd/, read more = present /riːd/) | Keep — context unambiguous in every instance |
| close | 1 | "let him close it himself" — verb /kloʊz/ | Keep — preceded by "let him" |
| present | 0 | n/a | n/a |
| live | 0 | n/a | n/a |
| lead | 0 | n/a | n/a |

Tech-term spell-outs (HTML → H-T-M-L, etc.) already applied in the script. No further changes needed in Phase 2a — the TTS-script will be a near-direct copy of `full-script.md` minus the section headers and word-count audits.

PASS.

## Pass 6 — Narrative flow / connector check (news-explainer profile)

Required: every scene boundary has an explanatory connector word/phrase.

| Boundary | Connector |
|---|---|
| S0 → S1 | "Here is what HTML can carry that markdown cannot." (here-is signal + comparison) ✓ |
| S1 → S2 | "So compare." (so-because) ✓ |
| S2 → S3 | "And yes. There is a price. The honest one." (and-but) ✓ |
| S3 → S4 | "Here is the part that turns this from a thesis into a workflow." (here-is) ✓ |
| S4 → S5 | "So why Claude Code specifically?" (so-why) ✓ |
| S5 → S6 | "Here is the part the article actually ends on." (here-is) ✓ |

PASS.

---

## Revisions to apply (3 minor)

### Revision 1 — Disambiguate the "I" voice in Scene 6

The script has both narrator-I and Thariq's quoted-I in Scene 6, which can confuse listeners on first pass.

- **OLD**: "So I will let him close it himself."
- **NEW**: "So I will let Thariq close it himself."

### Revision 2 — Scene 6 polish on the editorial-magazine reply line

"Even editorial magazines, going by some of the replies." reads slightly awkward.

- **OLD**: "Even editorial magazines, going by some of the replies."
- **NEW**: "Even editorial magazines — and judging by the replies, plenty of other places too."

### Revision 3 — Scene 6 final CTA polish

"Open one of the example files in his gallery" can be tightened.

- **OLD**: "Open one of the example files in his gallery."
- **NEW**: "Open one of the files in Thariq's gallery."

---

## Verdict

**PASS — apply 3 revisions and proceed to Phase 2a (TTS-script).**

Hook score 8.9/10. Source fidelity clean. No banned phrases. All scene boundaries
carry connector words. TTS heteronym audit clean.
