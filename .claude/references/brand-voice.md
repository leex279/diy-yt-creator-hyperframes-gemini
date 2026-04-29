# Brand Voice — Profile Dispatcher

**Status:** v2.0 — 2026-04-28
**Lives in:** `.claude/references/brand-voice.md`
**Dispatches to:** profile-specific files based on the `voice_profile` field in `videos/<slug>/research/content-brief.md`.

---

## How to use

Read `videos/<slug>/research/content-brief.md` and find the `voice_profile` field. Then read the matching profile file:

| voice_profile     | File to read                                                | Use when                                                                            |
| ----------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `tutorial`        | `.claude/references/brand-voice-tutorial.md`                | Thomas is the practitioner — hands-on developer content, terminal demos, workflows  |
| `news-explainer`  | `.claude/references/brand-voice-news-explainer.md`          | Reporting on third-party news — announcements, deals, releases, industry shifts     |
| `comparison`      | (deferred — fall back to `news-explainer` for now)          | Tool A vs Tool B — currently uses news-explainer rules                              |

If `voice_profile` is missing, default to `news-explainer` (most shorts in this channel are news-explainer; tutorial is opt-in).

---

## What's universal across all profiles

Both profile files share a **Universal Bans** section — the generic-AI banned word list (`delve`, `leverage`, `paradigm`, `seamless`, etc.) and the hype phrases banned for this channel (`changed everything`, `mind-blowing`, `smash that like button`, etc.). Profile-specific lists ADD to these; they do not replace them.

The Universal Bans live in BOTH profile files (intentional duplication so each file is self-contained). If a banned phrase needs to be added or removed, update both profile files.

---

## Profile precedence

Where the active profile's rules and the generic playbook (`.claude/references/faceless-tech-scriptwriting-playbook.md`) conflict, the active profile wins. Where two profiles disagree on a rule, the brief's `voice_profile` field decides which one applies.

---

## See also

- `.claude/references/script-library.md` — annotated gold-standard scripts. Phase 2 reads this BEFORE the profile file.
- `.claude/references/faceless-tech-scriptwriting-playbook.md` — generic scriptwriting playbook (broader patterns).
- `.claude/references/story-locks.md` — universal story-lock taxonomy (term branding, embedded truths, loop openers, etc.).
