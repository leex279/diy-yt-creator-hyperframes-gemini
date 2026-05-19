# TTS Pronunciation — Heteronym & Mispronunciation Audit

ElevenLabs `eleven_multilingual_v2` (the model this repo uses, per `.env`) reads English purely from spelling + sentence-context probability. It has no per-word semantic disambiguation, and **its pronunciation dictionaries on this model only support alias / string-substitution rules — phoneme rules require `eleven_flash_v2_5` or `eleven_turbo_v2`**, which we don't use.

That means heteronym disambiguation must happen at the **script level**. This file lists the words that consistently fail in our content and the synonym swaps that work. Every script written by Phase 2 / 2a / 2b MUST be checked against this list before TTS is generated.

## Hard rule

> **Before running `npx hyperframes tts` (or `python scripts/elevenlabs-tts.py`), grep the flat `videos/<slug>/script.txt` AND the per-scene `videos/<slug>/scripts/scene-NN-*.txt` files for every word in the "Heteronyms" table below. For each hit, decide whether the spelling will read correctly in context. If there is any ambiguity, swap to the synonym column.**

A 30-second grep saves a 7-minute regen + retime + re-render cycle.

## Heteronyms — words that flip pronunciation by meaning

Every row is a real-world failure mode we've observed or a known TTS-engine ambiguity.

| Word | Adjective / "active" sense | Verb / "alternate" sense | Default fix in this repo |
| ---- | --------------------------- | ------------------------- | ------------------------ |
| **live** | /laɪv/ — broadcast, available, in production | /lɪv/ — to reside | **Replace adjective sense** with `available` / `shipping` / `running` / `out today` / `streaming`. e.g. *"live today"* → *"available today"*; *"live on the Claude Platform"* → *"shipping on the Claude Platform"*. |
| **lead** | /liːd/ — leader, primary, "lead agent" | /lɛd/ — the metal | **Replace** with `primary` / `head` / `the lead-off agent` (verbose but unambiguous), OR rephrase to avoid the noun. *"a lead agent"* → *"a primary agent"* OR *"a coordinator agent"*. |
| **read** | /riːd/ — present tense | /rɛd/ — past tense | Use explicit time markers: *"will read"* / *"already read it"* (past usually works in context, but if it leads a sentence rewrite). |
| **close** | /kloʊs/ — near, *close to done* | /kloʊz/ — to shut, *close the loop* | Both senses appear in our content. Default: trust the engine — context usually wins. If ambiguous, replace adjective with `near` / `nearby`. |
| **wind** | /wɪnd/ — air | /waɪnd/ — to coil | Almost never appears in our content. If it does, rephrase. |
| **tear** | /tɪər/ — cry | /tɛər/ — rip | If used, prefer `rip` / `split` for the verb sense. |
| **bow** | /boʊ/ — ribbon, ship's front | /baʊ/ — bend down | Avoid; rephrase. |
| **minute** | /ˈmɪnɪt/ — unit of time | /maɪˈnjuːt/ — tiny | Replace adjective sense with `tiny` / `minuscule`. |
| **content** | /ˈkɒntɛnt/ — stuff, "the content of the page" | /kənˈtɛnt/ — satisfied | Default sense in our content (noun) usually reads correctly. |
| **object** | /ˈɒbdʒɛkt/ — thing, JSON object | /əbˈdʒɛkt/ — to protest | Tech context wins; usually fine. |
| **present** | /ˈprɛzənt/ — current, gift | /prɪˈzɛnt/ — to show | Default to `show` for the verb sense. |
| **record** | /ˈrɛkɔːrd/ — a recording, the record | /rɪˈkɔːrd/ — to record | If verb, use `capture` / `log` to disambiguate. |
| **convert** | /ˈkɒnvɜːrt/ — a convert (rare) | /kənˈvɜːrt/ — to convert | Verb is the default in tech content; usually fine. |
| **desert** | /ˈdɛzərt/ — arid place | /dɪˈzɜːrt/ — abandon | Avoid the verb sense; `abandon` / `bail on`. |

## Tech & brand pronunciation pitfalls

These are NOT heteronyms but consistent TTS failures on our content.

| Term | TTS often says | Should sound like | Fix |
| ---- | -------------- | ------------------ | ---- |
| `nginx` | en-jin-ks | engine-X | Spell as `engine-x` in TTS scripts |
| `kubectl` | kube-ECTL | cube-C-T-L | Spell as `cube-C T L` |
| `jq` | jq (silent) | jay-queue | Spell as `jay-queue` |
| `cgroups` | see-groups (varies) | see-groups | Spell as `see-groups` |
| `npm` | nuh-pem (varies) | N P M | Spell as `N P M` |
| `OAuth` | oh-auth | O-auth | Spell as `O auth` |
| `CRUD` | crud (one word) | C R U D | Usually fine in context; spell out only if isolated |
| `regex` | ree-jex | reh-jex | Spell as `reh-jex` only if engine fails (it usually doesn't) |
| `API` | ay-pee-eye | A P I | Spell as `A P I` |
| `CLI` | klee | C L I | Spell as `C L I` |
| `SSH` | esh | S S H | Spell as `S S H` |
| `IDE` | eye-dee | I D E | Spell as `I D E` |
| `CI/CD` | see-eye-stroke-see-dee | C I C D | Spell as `C I C D` |
| `OK` | oh-kay (sometimes oh-kuh) | okay | Spell as `okay` |
| `dynamous.ai` | dynamous-AY-EYE | dynamous-dot-AY-EYE | Spell as `dynamous dot AI` (already enforced by phase 2a) |
| `debug` | DEH-bug (rhymes with "dead-bug") | DEE-bug (long-e + bug) | Spell as `dee-bug` in TTS scripts. Confirmed consistent failure on `eleven_multilingual_v2` across multiple chunks (incl. `ast-grep-missing-layer` "debug logs"). Visual labels in the HTML can keep the normal spelling — only the spoken script needs the respell. |
| `CLAUDE.md` | C-L-A-U-D-E dot M D (if spelled as caps) | claude-dot-M-D | Spell as `Claude dot M D` in TTS scripts. NEVER spell out the letters of "Claude" — it's a brand word, pronounced as one syllable (/klɔːd/). The `.md` extension is fine to letter-spell. Visual labels in HTML keep the canonical `CLAUDE.md` spelling. Same pattern applies to other brand-word-plus-extension constructs (`README.md` → `readme dot M D`, `AGENTS.md` → `agents dot M D`). |

These are NOT exhaustive. Every new tech term encountered should be probe-tested with a single-chunk TTS before committing the whole script.

## What NOT to do

1. **Do NOT add a global `live → lyve` (or similar) alias to the ElevenLabs pronunciation dictionary.** It will mispronounce every future "they live in Tokyo" verb usage — a silent regression that's hard to detect.
2. **Do NOT use IPA `<phoneme>` SSML tags in script.txt.** The model strips them silently — and even if it didn't, `eleven_multilingual_v2` doesn't honor them.
3. **Do NOT trust 1.0× preview-listening to catch every issue.** ElevenLabs occasionally generates a clean pronunciation in one chunk and a wrong one in the next chunk on the same word. If a heteronym appears 3+ times in a script, every instance is a new roll of the dice. **Prevention via synonym swap is more reliable than detection via post-hoc listening.**

## Workflow integration

This rule is enforced at two points:

1. **Phase 2a (TTS script)** — before writing the per-scene `.txt` files and the flat `script.txt`, the agent grep-audits each scene against the heteronym table and applies the default fix where ambiguous.
2. **Phase 2b (fact-check)** — the fact-checker verifies the audit was performed by spot-checking 2-3 random heteronym candidates in the final `script.txt`.

If a heteronym is intentionally kept (e.g. a quote that uses "live" in the verb sense, where rewording would change meaning), document the decision inline in the per-scene `.txt` file as a comment header (the comment doesn't reach TTS — `elevenlabs-tts.py` strips `[SCENE: name]` style markers but a leading `<!-- … -->` is just whitespace from the engine's perspective and is fine).

## Adding a new heteronym to this list

When TTS mispronounces a word in a way that causes a regen cycle:

1. Add it to the table with: real adjective sense, real verb sense, the default fix that worked.
2. If the fix is genuinely irreplaceable in the script (loss of meaning / brand / quote integrity), document the exception under "Words to keep despite ambiguity" with the reasoning.
3. Commit the rule update IN THE SAME PR as the script fix so future agents pick up the lesson.

This list grows. The longer it grows, the fewer cycles we waste on a known issue.
