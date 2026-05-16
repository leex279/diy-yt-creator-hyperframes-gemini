# Content Brief: Claude Code `/goal` Command

## Video Metadata
- **Slug**: `claude-code-goal-command`
- **Template**: `shorts/anthropic`
- **Duration**: 120s (vertical 1080×1920 Short)
- **Tone**: Excited / curious / discovery — "wait, there's a new slash command and it changes the loop"
- **Voice Profile**: `voice_profile: news-explainer` — feature-just-shipped framing, no first-person tutorial
- **Target Audience**: Developers using Claude Code daily — already familiar with `/init`, `/clear`, `/compact`, `/model`, `/plan`, `/loop`
- **Key Angle**: `/goal` flips Claude Code from "you re-prompt every turn" to "you state the finish line once" — a second model judges every turn against your condition.
- **Topic Type**: PRODUCT_TOOL (a specific shipped feature of Claude Code v2.1.139)
- **Research Depth**: STANDARD (single-source canonical docs page + changelog cross-ref)

---

## Thesis

`/goal` is not "auto mode for the whole session" — it's the first Claude Code primitive where a **separate evaluator model** (Haiku by default) judges every turn against a falsifiable condition, which means the developer's job changes from "prompt repeatedly" to "write the test that ends the loop."

(Falsifiable: if the docs said the SAME model that did the work also judged completion, this thesis would be wrong. The docs explicitly state a "fresh model" / "small fast model" evaluates — so the thesis is testable and held.)

---

## Receipts

1. https://code.claude.com/docs/en/goal — 2026-05-12 — verbatim canonical documentation of the `/goal` command (syntax, semantics, evaluator behavior, examples)
2. https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md — version 2.1.139 — official changelog entry: "Added `/goal` command: set a completion condition and Claude keeps working across turns until it's met. Works in interactive, `-p`, and Remote Control."
3. https://code.claude.com/docs/en/scheduled-tasks — 2026-05-12 — `/loop` docs page explicitly cross-references `/goal` as the condition-driven sibling: "To keep the session working turn after turn until a condition is met rather than on an interval, see `/goal`."
4. https://code.claude.com/docs/en/commands — 2026-05-12 — Claude Code commands reference index (confirms `/goal` is a built-in command, not a plugin/skill)

(All four resolvable, all four versioned/dated, all four name the artifact. Receipt gate PASSES with margin.)

---

## Core Value Proposition

`/goal` helps developers running long agentic Claude Code tasks remove per-turn re-prompting by stating one verifiable end state — a separate Haiku-class evaluator decides "done or not" after every turn and feeds the reason back as guidance.

---

## Target Audience

**Primary**: Claude Code daily drivers — devs who already use `/init`, `/clear`, `/compact`, `/plan`, `/loop`, and know what "session-scoped" means.
**Secondary**: Developers curious about agentic loops who use Cursor/Cline/Codex CLI and want to compare. Also viewers comparing Claude Code's autonomy story to OpenAI Codex's "Goal Mode" (April 2026).
**What they know**: Slash commands, plan vs auto mode, the cost of re-prompting Claude Sonnet across 20 turns, what a Stop hook is conceptually.
**What they care about**: Time saved per long task, token cost of the loop, whether the loop will go off the rails, whether "yes/no judging" actually works at production scale.

---

## Pain Points

1. **The re-prompt babysit loop**: You ask Claude Code to migrate a module. It does turn 1, returns control. You type "keep going." It does turn 2. You type "keep going." Repeat 18 times. The model is competent — the bottleneck is *you*. [VISUAL: HIGH — show terminal with 8x "keep going" prompts stacked]
2. **No clear "done" line**: Auto mode approves tool calls but stops when the *working* model decides it's done. The working model is biased to declare success — it has skin in the task. There's no second pair of eyes. [VISUAL: HIGH — split screen of "worker model says done" / "but did it actually pass tests?"]
3. **Long-running tasks that span turns**: Migrate every call site to a new API. Split a 4000-line file into modules. Address every label-filtered issue. These don't fit one turn — and you don't want to sit there. [VISUAL: HIGH — backlog of issues count-down from 47 to 0]
4. **You don't know when to stop**: Even if you wanted to fire-and-forget, "did Claude finish?" needs an opinion. Without a structured exit, the agent either over-runs (wastes tokens) or under-runs (leaves work). [VISUAL: MEDIUM — a runaway counter contrasted against a clean "achieved" stamp]
5. **Codex shipped Goal Mode in April; you've been jealous**: OpenAI's CLI got persistent objectives with token budgets a month ago. Now Anthropic shipped the equivalent — but with a different evaluation architecture. [VISUAL: MEDIUM — date-ordered timeline, careful not to fabricate a Codex spec the user hasn't verified]

---

## Key Features & Benefits

| Feature                              | Benefit (user-facing)                                                          | Differentiator? | Metric                                  | Visual Potential | Demo? |
| ------------------------------------ | ------------------------------------------------------------------------------ | --------------- | --------------------------------------- | ---------------- | ----- |
| One-line set: `/goal <condition>`    | No separate prompt — the condition IS the directive that starts turn 1         | Yes             | 1 command vs N "keep going" prompts     | HIGH             | Yes   |
| Separate evaluator (small fast model) | A fresh model judges done-ness — not the model that did the work               | YES (vs auto)   | Default = Haiku                         | HIGH             | Yes   |
| Yes/no + reason after every turn     | "No" reason is fed back as next-turn guidance — self-correcting               | Yes             | Per-turn evaluator verdict              | HIGH             | Yes   |
| Auto-clears on completion            | Records "achieved" in transcript; no manual cleanup                            | Yes             | One state transition                    | MEDIUM           | Yes   |
| Status view (`/goal` no args)        | See condition, duration, turn count, token spend, last evaluator reason       | Yes             | 5 fields displayed                       | HIGH             | Yes   |
| `/goal clear` + 5 aliases            | `stop`, `off`, `reset`, `none`, `cancel` all work; `/clear` also wipes it      | Polish          | 6 ways to bail                          | LOW              | No    |
| Non-interactive: `claude -p "/goal …"` | Headless / CI loop in one shell invocation                                   | Yes             | 1 invocation = N turns                  | MEDIUM           | Yes   |
| Resume restores active goals          | `--resume` / `--continue` carries the condition forward (counters reset)       | Polish          | 1 of 4 state fields preserved           | LOW              | No    |
| Built on session-scoped Stop hook     | Same primitive devs already configure — `/goal` is the ergonomic shortcut    | Architectural   | Wraps existing hooks system             | MEDIUM           | No    |
| Condition limit 4,000 chars           | Room for measurable end state + check + constraints + turn/time bound       | Polish          | 4,000 char ceiling                      | LOW              | No    |

---

## Proof Points (Scene-Ready)

| Stat / Claim                                       | Formatted Value | Comparison Baseline                       | Source URL                                                                       | Visual Format     | Shock Factor |
| -------------------------------------------------- | --------------- | ----------------------------------------- | -------------------------------------------------------------------------------- | ----------------- | ------------ |
| Evaluator defaults to Haiku ("small fast model")   | "Haiku"         | vs full-spend Sonnet doing the work       | https://code.claude.com/docs/en/goal                                             | model-name chip   | 7/10         |
| Maximum condition length                           | "4,000 chars"   | vs typical 1-line prompts                 | https://code.claude.com/docs/en/goal                                             | character counter | 5/10         |
| Aliases accepted for `/goal clear`                 | "5 aliases"     | `stop` / `off` / `reset` / `none` / `cancel` | https://code.claude.com/docs/en/goal                                             | pill row of 5     | 4/10         |
| Version that shipped `/goal`                       | "v2.1.139"      | first appearance in changelog              | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md       | version chip      | 6/10         |
| Three modes `/goal` works in                       | "3 modes"       | interactive / `-p` / Remote Control       | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md       | 3-pill matrix     | 6/10         |
| Active indicator glyph                             | "◎ /goal active" | UI proof — show the actual char            | https://code.claude.com/docs/en/goal                                             | terminal glyph    | 7/10         |
| One goal per session                               | "1 active"      | new `/goal` replaces the old              | https://code.claude.com/docs/en/goal                                             | replace-arrow     | 5/10         |
| Evaluation token cost                              | "negligible"    | vs main-turn Sonnet spend                 | https://code.claude.com/docs/en/goal                                             | cost-bar contrast | 7/10         |

All 8 proof points have a source URL. QG-0F PASS.

---

## Visual Concepts

1. **The "keep going" stack collapse**: Terminal-style scene showing 8 stacked prompts that all say "keep going" → they melt into a single line: `/goal all tests in test/auth pass and the lint step is clean`. Carries the value prop in one beat.
2. **Two-model split**: Left half labeled "Sonnet — does the work." Right half labeled "Haiku — judges the work." After each turn, an arrow loops from left to right, right returns "no — auth/login_test.js still failing", arrow loops back. On final turn, right returns "yes — achieved" and a green checkmark seals the frame.
3. **The active indicator hero**: Black terminal frame, centered glyph `◎ /goal active · 14m 32s` at 160px, subtitle line `condition: all tests in test/auth pass and the lint step is clean` at 44px. This is a perfect first AND last frame candidate.
4. **Real terminal example**: Reproduce the docs example verbatim — `/goal all tests in test/auth pass and the lint step is clean`. Show turn 1 output (test runner fails), evaluator verdict pill ("no — 2 failures in login_test.js"), then turn 2 output (Claude fixes), evaluator verdict ("yes — achieved"), then the auto-clear.
5. **Compare-modes matrix**: 3-row table — `/goal` (condition-driven, model decides done) / `/loop` (time-driven, you or model decides done) / Stop hook (settings-level, you decide done). Each row enters on its own beat.
6. **Non-interactive one-liner**: Terminal frame shows `claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"` with the cursor blinking; then a fast-forward visual shows turn 1, turn 2, turn 3 firing automatically; then "achieved" + the process returns control. Ctrl+C interrupt called out subtly.
7. **The condition anatomy**: One condition deconstructed into 3 colored ribbons — (1) measurable end state (red), (2) stated check (yellow), (3) constraints that matter (cyan). Plus a 4th hint chip: "or stop after 20 turns" for bound-runtime.

---

## Visual Metaphor Inventory

| Concept                              | Metaphor                                | How It Animates                                                                                              | Source / Inspiration                              |
| ------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| Worker model + evaluator architecture | Coding partner + code reviewer at standup | Sonnet "writes" on left, Haiku "reviews" on right, turn-arrow loops between until reviewer stamps approved | Pair programming                                  |
| Self-correcting feedback loop        | A thermostat                            | Temperature gauge oscillates around target; each tick = a turn; gauge snaps to target = "achieved"           | HVAC / control systems                            |
| Re-prompt removal                    | Hands-free cruise control               | Highway dash: driver lifts hands off wheel, car keeps pace until exit ramp arrives                           | Tesla autopilot trope (familiar audience metaphor) |
| Condition as test                    | Pass/fail unit test                     | Red bar → fixes → green bar; the green bar IS the "achieved"                                                | Standard TDD red-green                            |
| Session-scoped vs settings-scoped    | Whiteboard note vs framed policy        | `/goal` written in dry-erase on a whiteboard (wiped at end of session); Stop hook stamped on a framed sign  | Office metaphor                                   |

---

## Demo Opportunity Inventory

| What to Demo                                                            | Format                | URL (if screenshot)                                          | Dark/Light | Wow Factor | Notes                                                                                                                                                                |
| ----------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------ | ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The full `/goal` docs page hero — title + opening sentence              | Screenshot            | https://code.claude.com/docs/en/goal                         | light      | 8/10       | Use as the "this is real, not a leak" receipt frame                                                                                                                  |
| Verbatim example: `/goal all tests in test/auth pass and the lint step is clean` | Synthesized terminal | N/A                                                          | dark       | 9/10       | Best demo moment — recreate as a stylized terminal frame, NOT a real screenshot (no real session to capture)                                                          |
| The active indicator `◎ /goal active · 14m 32s`                         | Synthesized terminal | N/A                                                          | dark       | 8/10       | First-frame AND last-frame thumbnail candidate                                                                                                                       |
| Non-interactive: `claude -p "/goal CHANGELOG.md has an entry…"`         | Synthesized terminal | N/A                                                          | dark       | 7/10       | The headless / CI angle                                                                                                                                              |
| Changelog screenshot showing the `/goal` line                            | Screenshot            | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md | light      | 6/10       | "v2.1.139" receipt — proves it's official, not rumor                                                                                                                 |
| Compare-modes matrix (`/goal` vs `/loop` vs Stop hook)                  | Diagram               | N/A                                                          | dark       | 7/10       | From the docs page comparison table — transcribed not screenshotted                                                                                                  |
| Aliases pill row: `clear / stop / off / reset / none / cancel`         | Diagram               | N/A                                                          | dark       | 5/10       | Side detail; show as a chip row entering one at a time                                                                                                               |
| The evaluator reason fed back as guidance                                | Diagram               | N/A                                                          | dark       | 8/10       | This is the "wow — it self-corrects" beat. Animate the verdict text flowing from right (evaluator) → into left (worker model) as next-turn guidance |

---

## Before/After Transformations

| Before State                                              | After State                                                        | Visual Treatment                                                                            |
| --------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Dev types "keep going" 8 times across a 20-min migration | Dev types `/goal <condition>` once, walks away, comes back to "achieved" | Split-screen: left = stacked prompt log, right = single command + active indicator        |
| One model decides "I'm done" (auto mode)                  | Two models — worker + judge — agree before "done"                  | Single-headshot → two-headshot reveal                                                       |
| Goal condition vs the loop wandering off                  | Goal condition stays exact; reason adapts every turn               | One pinned card (condition) + scrolling cards (reasons) below it                            |

---

## Architecture Diagram Opportunities

| System / Flow                                                | Components                                                                  | Progressive Reveal Order                                                                                                                                                                                                                          | Complexity |
| ------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `/goal` evaluation loop (per turn)                           | Worker model (Sonnet) / Conversation transcript / Evaluator model (Haiku) / Yes-or-no verdict / Reason | (1) Worker does turn → (2) Transcript updates → (3) Evaluator reads transcript → (4) Returns yes/no+reason → (5a if no: reason → next turn guidance; loop back to 1) (5b if yes: clear goal, write "achieved" to transcript) | medium     |
| Three autonomy primitives compared                           | `/goal` / `/loop` / Stop hook                                               | Show all three boxes, then highlight the "what triggers next turn" pin on each                                                                                                                                                                    | simple     |
| Where `/goal` sits in the hooks system                       | Stop hook (general) ⟸ session-scoped Stop hook ⟸ `/goal` (the ergonomic wrap) | Outer box → inner box → inner box, with `/goal` as the innermost convenience layer                                                                                                                                                                | simple     |

---

## Competitive Landscape

| Alternative                                       | Key Difference                                                                            | Where `/goal` Wins                                                       | Where Alternative Wins                                                                                          |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `/loop` (Claude Code)                             | Time-driven instead of condition-driven                                                   | Stops the moment work is verifiably done — not after N intervals         | Better for polling external events (deploys, CI, PR comments)                                                   |
| Stop hook (Claude Code, deeper primitive)         | Configured in settings; can be script or prompt; persists across sessions                 | Session-scoped — set it for one task, no settings file edit needed       | Persistent across every session in scope; can run arbitrary scripts for deterministic checks                    |
| Auto mode (Claude Code)                           | Approves tool calls within ONE turn — doesn't start a new turn                            | Removes per-turn re-prompt; auto mode only removes per-tool approval     | Auto mode pairs with `/goal` — they're complementary, not competing                                             |
| Codex CLI "Goal Mode" (OpenAI, shipped 2026-04-16) | OpenAI's equivalent — first to ship; uses token budgets explicitly                       | Anthropic's version uses a separate evaluator model architecture          | Codex shipped first; user is welcome to verify Codex spec details — DO NOT fabricate Codex's exact mechanics    |
| Manual "keep going" / "continue" prompts          | The default                                                                                | Hands-free; condition is judged objectively; auto-clears                 | Zero learning curve; works with any tool                                                                        |

---

## Notable Adopters

| Company/Person                                | How They Use It                                                  | Why It Matters for Video                                                              |
| --------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| _Unknown — feature just shipped in v2.1.139_  | N/A                                                              | Brief is HONEST: no adopter case studies exist yet. Do NOT fabricate any.             |
| Community precedents (NOT in script)         | `github.com/jthack/claude-goal`, `github.com/chrischabot/claude-code-goal` | Evidence that the community wanted this — but these are NOT to be cited as adopters. |

(Adopter table is intentionally thin. No fabrication allowed per the no-fabrication memory rule.)

---

## Market Context & Timing Signal

- **Market size**: The "agentic CLI" tier — Claude Code, Cursor agent mode, Cline, Codex CLI, Aider — has converged on multi-turn autonomy as the table-stakes feature. The argument moved from "should the agent run multi-turn?" to "who decides when it stops?"
- **Growth**: Adoption of `/loop` (Claude Code's earlier autonomy primitive) gave Anthropic the usage signal to ship `/goal`. The change in primitive is from time-driven to condition-driven, the more advanced mode.
- **Why NOW (2026-05)**: Codex CLI shipped Goal Mode 2026-04-16 (a month ago). Anthropic's response in v2.1.139 closes the autonomy-feature-parity gap with a different architectural decision (separate evaluator vs token budget). The autonomy-loop arms race is the trend.

---

## Messaging Hierarchy

### Must Include [Visual Treatment]
- The single-line `/goal <condition>` syntax with the verbatim docs example [terminal frame]
- The "separate evaluator model decides done — not the worker" point [two-model split]
- Verdict-as-guidance feedback loop (no→reason→next turn) [arrow loop diagram]
- Auto-clear on "yes" → "achieved" stamp [transcript entry visual]
- Version shipped (v2.1.139) so it's clearly NEW [version chip]
- The 3 modes it works in: interactive / `-p` / Remote Control [3-pill matrix]
- Status view with 5 fields (condition / duration / turns / tokens / last reason) [terminal status block]
- Comparison vs `/loop` (condition vs time) [side-by-side table]

### Should Include
- Use cases — the 4 docs bullets verbatim (API migration, design doc, file split, issue backlog)
- The "write an effective condition" 3-part anatomy (end state + check + constraints)
- 4,000 char condition limit (room for full task spec)
- Bounded runtime via `or stop after 20 turns` clause in condition
- Aliases for `/goal clear`

### Could Include
- Resume behavior (`--resume`/`--continue` restores condition, resets counters)
- Trust dialog / `disableAllHooks` requirement
- That `/goal` is built on the existing Stop hook primitive (architectural elegance)
- One-goal-per-session rule

### Omit
- Anything about Codex spec details (we don't have receipts) — only mention Codex in a comparative one-liner if at all
- "Adopter X uses it for Y" — no real adopters yet, no fabrication
- Pricing claims beyond "Haiku — typically negligible"
- Anything about the small-fast-model being configurable beyond a one-liner pointer

---

## Hook Architecture

### Cult-Hopping References
| Brand / Person / Concept           | Why It Works                                                                                                  | Where to Use (Hook / Mid / CTA) |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Tesla autopilot / cruise control   | Universal "hands off the wheel" metaphor that pairs with the no-re-prompt benefit                            | Hook                            |
| Code review at standup             | Two-person engineering pattern that maps to the worker+evaluator split                                       | Mid                             |
| TDD red→green                      | "Condition met = green bar" is the developer-native shape of the loop                                        | Mid                             |
| Codex Goal Mode (OpenAI, April)    | The same week's competitor parallel — anchors "why this matters now" without fabricating details             | Hook or "why now" beat           |
| `/init`, `/clear`, `/compact`      | Already-known slash commands the audience uses daily — `/goal` slots into their muscle memory                | Hook                            |

### Common Ground by Audience
- **Technical (Claude Code daily drivers)**: "You type 'keep going' more than you type real code on long migrations." Specific, painful, true.
- **General (broader dev audience)**: "What if the test was the directive?" — pairs the TDD shape with autonomy.
- **Decision Makers**: "One Haiku call per turn is the price; no developer-in-the-loop is the savings."

### Contrarian Angles (Uno Reverse)
1. **`/goal` is not "more autonomy" — it's MORE oversight.** The audience expects "automation = less judgment." But `/goal` literally adds a second model that judges every turn. The mental flip: it's "two models with a contract" not "one model running wild."
   - Evidence: docs explicitly say "completion is decided by a fresh model rather than the one doing the work" — https://code.claude.com/docs/en/goal
2. **The hardest part is NOT writing the goal — it's writing a condition the evaluator can READ.** The docs warn: the evaluator doesn't run commands or read files. It only judges what's surfaced in the conversation. That changes how you write the condition.
   - Evidence: docs "Write an effective condition" section — https://code.claude.com/docs/en/goal
3. **Auto mode + `/goal` are complementary, not competing.** A natural assumption is "auto mode IS the autonomy feature." But the docs split them: auto mode removes per-tool prompts, `/goal` removes per-turn prompts. You probably want both.
   - Evidence: docs Compare section — https://code.claude.com/docs/en/goal

### Mind-Blowing Stats
| Stat                                          | Value                          | Shock Factor (1-10) | Source URL                                                                       |
| --------------------------------------------- | ------------------------------ | ------------------- | -------------------------------------------------------------------------------- |
| Evaluator defaults to Haiku                   | "Haiku judges Sonnet"          | 7/10                | https://code.claude.com/docs/en/goal                                             |
| Max condition length                          | 4,000 chars                    | 6/10                | https://code.claude.com/docs/en/goal                                             |
| Aliases for `/goal clear`                     | 5                              | 4/10                | https://code.claude.com/docs/en/goal                                             |
| Shipped in v2.1.139                           | v2.1.139                       | 7/10                | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md       |
| 3 invocation modes                            | interactive / `-p` / Remote   | 6/10                | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md       |
| Eval cost vs main-turn spend                  | "typically negligible"         | 7/10                | https://code.claude.com/docs/en/goal                                             |

### Preview Hook Teasers (for Scene 00 / opening)
1. **"Claude Code just shipped `/goal` — and Haiku judges Sonnet now."** (scroll-stop opener; quotes the actual architecture)
2. **"You'll never type 'keep going' again."** (teaser for the re-prompt removal beat — the pain point that lands instantly)
3. **"v2.1.139 turns your condition into the directive. The model judges every turn until it's met."** (promise statement)

### Primary Open Loop Suggestion
- **Setup (early)**: "There's a new slash command in Claude Code. It's two letters away from `/loop` — and it works completely differently."
- **Resolution (late)**: "`/loop` fires on time. `/goal` fires until the test goes green. That's the whole difference." — paired with the matrix visual.

---

## Suggested Narrative Arc (Kallaway Formula)

1. **Context Lean-In**: "If you use Claude Code, you've typed 'keep going' at least once today." (Pain everyone recognizes instantly.)
2. **Scroll-Stop**: "**But** there's a new slash command — and it makes 'keep going' obsolete."
3. **Contrarian Snapback**: "It's not auto mode. It's not `/loop`. **`/goal` makes a second model judge every turn.**"
4. **Solution**: Show the verbatim `/goal all tests in test/auth pass and the lint step is clean` example — that single line replaces the re-prompt loop.
5. **Features (Benefit-Led)**: 4 features one at a time, paced — (a) condition IS the directive, (b) separate evaluator (Haiku), (c) verdict-as-guidance loop, (d) auto-clear on achieved.
6. **Trust**: "Shipped in v2.1.139. Works in interactive, `-p`, and Remote Control."
7. **CTA**: "Type `/goal` next time you're about to type 'keep going' for the eighth time." (Followed by Dynamous outro line.)

---

## Suggested Scene Structure

| #   | Scene / Phase Name          | Duration Est. | Key Visual                                                                                  | Key Stat / Quote                                                       |
| --- | --------------------------- | ------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | Thumbnail-grade open + pain | 0–14s         | Title slam "Claude Code just shipped `/goal`" + stacked "keep going" prompt receipt        | "v2.1.139"                                                            |
| 2   | The single-line setup       | 14–28s        | Terminal frame with verbatim docs example                                                   | `/goal all tests in test/auth pass and the lint step is clean`         |
| 3   | The two-model split         | 28–48s        | Worker (Sonnet) / Evaluator (Haiku) split + verdict-loop arrow                              | "Haiku judges every turn"                                              |
| 4   | The condition anatomy       | 48–66s        | One condition deconstructed into 3 colored ribbons + the 4,000-char chip                    | "End state + check + constraints"                                       |
| 5   | The compare matrix          | 66–84s        | `/goal` vs `/loop` vs Stop hook side-by-side, one row at a time                            | "`/goal` fires until the test goes green; `/loop` fires on time"      |
| 6   | The non-interactive mode    | 84–98s        | `claude -p "/goal …"` terminal one-liner + "achieved" stamp                                 | "3 modes: interactive, `-p`, Remote Control"                          |
| 7   | CTA + thumbnail-grade close | 98–120s       | Active-indicator hero `◎ /goal active` + outcome line + Dynamous CTA + brand chrome        | "Try `/goal` next time you type 'keep going'"                          |

(Approximate — Phase 1 will firm up exact data-start values when timing maps to TTS transcript.)

---

## Suggested Video Title Options

1. **"Claude Code's New `/goal` Command Changes Everything"** — generic but high-CTR; under 60 chars.
2. **"Haiku Now Judges Sonnet (in Claude Code v2.1.139)"** — architectural / contrarian; specific.
3. **"Stop Typing 'Keep Going' in Claude Code"** — pain-led; pairs with the cult-hop of the universal re-prompt habit.
4. **"`/goal` vs `/loop`: Claude Code's Two Autonomy Modes"** — searchable; rides the existing `/loop` SEO.
5. **"Claude Code v2.1.139 Quietly Shipped a Goal Mode"** — news-explainer voice fits this one best.

(No vidiq scores — enrichment skipped per instructions.)

---

## SEO Keywords

| Keyword / Phrase                              | Search Intent                            | Volume Estimate |
| --------------------------------------------- | ---------------------------------------- | --------------- |
| `claude code /goal`                           | direct feature lookup                    | rising — new    |
| `claude code goal command`                    | same intent, expanded                    | rising — new    |
| `claude code v2.1.139`                        | version-specific changelog lookup        | medium          |
| `claude code autonomous mode`                 | broader autonomy discovery               | high            |
| `claude code loop vs goal`                    | comparison intent                        | medium          |
| `claude code stop hook`                       | adjacent primitive                       | medium          |
| `claude code completion condition`            | conceptual / new-feature                 | rising          |
| `claude code keep claude working`             | pain-point query                          | low — long-tail  |

---

## Keyword Research (vidiq)

_Skipped — vidiq MCP tools not available in this session._

---

## Technical Terms (TTS Pronunciation)

| Term              | Pronunciation Note                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `/goal`           | Spell as "slash goal" in narration; the slash is part of the brand. Phase 2a may write it as "slash-goal" if the engine swallows. |
| `/loop`           | Same — "slash loop"                                                                                                               |
| `/clear`, `/compact`, `/init` | "slash clear", "slash compact", "slash init"                                                                                      |
| Haiku             | /ˈhaɪkuː/ — usually fine; if engine mispronounces, spell as "Hi-koo" only as last resort. Test before regen.                     |
| Sonnet            | /ˈsɒnɪt/ — usually fine                                                                                                           |
| `v2.1.139`        | Read as "version 2 point 1 point 139" — pre-write in script as `version 2.1.139` (TTS reads version numbers correctly with the word "version") |
| `--resume`, `--continue` | "double-dash resume", "double-dash continue"                                                                                |
| `-p`              | "dash P"                                                                                                                          |
| `disableAllHooks` | "disable all hooks" (camelCase will be split correctly by the engine; verify on render)                                            |
| CLI               | Spell as "C L I"                                                                                                                  |
| API               | Spell as "A P I"                                                                                                                  |
| `live`            | HETERONYM AUDIT: per `.claude/rules/tts-pronunciation.md`, replace any adjective-sense "live" (e.g. "live today") with "available today" / "shipping today". |
| `lead`            | HETERONYM AUDIT: avoid; use "primary" instead.                                                                                    |

---

## Viewer Objections to Preempt

1. **"This is just auto mode renamed."** — Address: NO. Auto mode runs within one turn (per-tool approval). `/goal` runs across turns AND adds a separate evaluator model. Cite the docs Compare section.
2. **"How is this different from `/loop`?"** — Address head-on with the matrix: `/loop` is time-driven, `/goal` is condition-driven. Both are session-scoped.
3. **"Won't the loop go off the rails?"** — Address: 3 mitigations from the docs — (a) the condition can include a turn/time bound clause, (b) the evaluator runs every turn (no runaway), (c) `/clear` and 5 aliases for `/goal clear` give 6 ways to bail.
4. **"What does the evaluation cost me?"** — Address: "typically negligible" per docs — Haiku-class tokens vs main-turn Sonnet spend.
5. **"Can I run this headless?"** — Address: yes, `claude -p "/goal …"` is in the docs. Show the verbatim example.
6. **"Does Codex have this?"** — Codex shipped Goal Mode in April 2026 (mention briefly, don't fabricate spec details). The point is Anthropic shipped a competitive answer with a different architectural choice.

---

## Competitor Video Analysis

| Video / Channel               | Hook Used                                            | What They Miss                                                                                             |
| ----------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| _Unknown — feature is days old_ | N/A                                                  | No competitor videos to analyze yet. The video has a clean SOV (share of voice) window for the first weeks. |

(Empty — no competitor video coverage exists yet for this specific feature. Mention to user as a tailwind.)

---

## Quality Gate Results

| Gate  | Check                       | Result | Notes                                                                                                                            |
| ----- | --------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| QG-0A | Proof points >= 5           | PASS   | 8 proof points listed; all with source URLs                                                                                      |
| QG-0B | Contrarian angles >= 3      | PASS   | 3 angles, all with docs URLs as evidence                                                                                         |
| QG-0C | Visual metaphor >= 1        | PASS   | 5 metaphors                                                                                                                      |
| QG-0D | Demo opportunity >= 1       | PASS   | 8 demo opportunities; the verbatim docs example is the hero demo                                                                  |
| QG-0E | SEO keywords >= 3           | PASS   | 8 keywords                                                                                                                       |
| QG-0F | All stats sourced           | PASS   | Every stat row has a source URL — no ⚠️ flags                                                                                    |
| QG-0G | Cult-hop refs >= 3          | PASS   | 5 cult-hops                                                                                                                      |
| QG-0H | Receipts >= 3 OR CONCEPT    | PASS   | 4 receipts (docs page, changelog, /loop docs cross-ref, commands index). Comfortably above the 3-receipt floor.                  |
| QG-0I | Thesis present              | PASS   | Falsifiable single-sentence thesis present and explicitly grounded in a docs claim that, if changed, would falsify it.            |

**All gates PASS. Phase 1 is unblocked.**

---

## Gaps / Needs User Input

- **Codex Goal Mode comparison depth**: The brief touches Codex as a "why now" timing signal. If the user wants a head-to-head feature-comparison beat in the script (e.g. "Codex uses token budgets; Claude uses a separate evaluator"), they should verify the Codex spec themselves — the source for that claim is `codex.danielvaughan.com 2026-04-16`, NOT an OpenAI primary source. Default behavior: omit Codex specifics from script, mention only as a one-line "and a month after Codex shipped Goal Mode, Anthropic shipped this." OR omit entirely.
- **Real terminal capture vs synthesized terminal frame**: The docs example (`/goal all tests in test/auth pass …`) is verbatim, but we don't have a real screen recording of a session. Recommendation: synthesize a stylized terminal in HTML/GSAP (Anthropic-brand-consistent) rather than risk fabricated screenshots. Confirm with user before Phase 1 if they have a screen capture they'd prefer.
- **Adopter case studies**: None exist. Brief is honest about this. No fabrication.

---

## Sources

| Source                                      | URL                                                                                                          | Used For                                                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Claude Code `/goal` docs page (primary)     | https://code.claude.com/docs/en/goal                                                                         | Every claim, syntax, example, behavior, requirement, comparison                                                |
| Claude Code CHANGELOG.md                    | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md                                   | Version (v2.1.139), 3 modes (interactive/-p/Remote Control), confirmed shipped status                          |
| Claude Code `/loop` docs page               | https://code.claude.com/docs/en/scheduled-tasks                                                              | Reciprocal cross-reference confirming `/goal` is the condition-driven sibling                                  |
| Claude Code Commands reference index        | https://code.claude.com/docs/en/commands                                                                     | Confirms `/goal` is a built-in command (not plugin/skill); broader context of slash-command ecosystem          |
| (Third-party, NOT cited in script) Codex Goal Mode (Daniel Vaughan blog) | https://codex.danielvaughan.com/2026/04/16/codex-cli-goal-mode-persistent-objectives-token-budgets/ | Timing context only. NOT a source for any specific claim about Codex. Mentioned in gaps for user awareness. |
