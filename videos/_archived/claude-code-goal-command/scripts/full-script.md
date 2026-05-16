# Claude Code's New /goal Command

## Scene 1: Wait — there's a new slash command

Wait. There's a new slash command in Claude Code, and Haiku judges Sonnet now. It's called slash goal. And it just made typing "keep going" obsolete.

<!-- Receipt: https://code.claude.com/docs/en/goal -->
<!-- Receipt: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md -->

## Scene 2: How slash goal actually works

Because here's how it works. You state one completion condition. Claude does a turn. Then a small fast model, Haiku by default, checks the transcript and returns yes or no, with a short reason. No means keep working, with that reason as guidance. Yes auto-clears the goal and writes "achieved."

<!-- Receipt: https://code.claude.com/docs/en/goal -->

## Scene 3: What it looks like in your terminal

So here's what it looks like in your terminal. You type slash goal, then a condition, something like "all tests in test slash auth pass and the lint step is clean." Claude runs turn one. Two tests still fail. Haiku reads the transcript and returns: "no. Auth login still broken." That reason becomes turn two's directive. Claude fixes it. Haiku checks again. "Yes. Achieved." The goal clears itself. Wait. Haiku just told Sonnet to keep working. That's the loop.

<!-- Receipt: https://code.claude.com/docs/en/goal -->

## Scene 4: How it differs from a normal prompt

And here's why it's not just another prompt. A prompt asks once. Claude answers, control returns to you, and you re-prompt to continue. Slash goal keeps checking. Every turn, a fresh model, not the one doing the work, judges your condition against the conversation. If you've ever typed "keep going" eight times in a row, this replaces all eight.

<!-- Receipt: https://code.claude.com/docs/en/goal -->

## Scene 5: Try it now

So. Next time you're about to type "keep going" for the eighth time, type slash goal instead. State the finish line once. The docs are at claude dot com slash docs slash en slash goal. Shipped in version 2.1.139. Quick question. How many times in a row have you typed "keep going"? Drop your number in the comments. If you want to learn more about AI, check out the dynamous.ai community.

<!-- Receipt: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md -->
