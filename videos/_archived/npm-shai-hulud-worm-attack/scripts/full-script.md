# NPM Just Got Hijacked — Six Minutes, 169 Packages, Signed Malware

## Scene 1: NPM Just Got Hijacked

NPM just got hijacked. Again.

<!-- Receipt: https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised -->

## Scene 2: The Trojan Horse Hook

TanStack just got hijacked in six minutes. And revoking the stolen token nukes your home folder. Trusted publishing was supposed to stop this. But the malware shipped signed. Salsa-attested. Still malware. Trusted publishing is not a trust boundary. It is a permissions boundary. Mini Shai-Hulud proved it.

<!-- Receipt: https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised -->
<!-- Receipt: https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/ -->

## Scene 3: The Smoking Gun

So how did one fork-PR own TanStack? Here's the smoking gun. A workflow file called bundle-size dot yamel ran on the pull-request-target trigger. That single line means fork code runs with main-repo permissions. Then it checked out the merge commit of the attacker's PR. Fork code. Real secrets. Same runner. The attacker closed the PR moments later. The damage was already cached.

<!-- Receipt: https://snyk.io/blog/tanstack-npm-packages-compromised/ -->

## Scene 4: The Eight-Hour Cache Bomb

And here is why closing the PR did nothing. Github Actions wrote a one-point-one gigabyte poisoned cache to disk. The cache poisons. The fork-PR opens, then closes. Hours later, an unrelated maintainer merges a real change. CI pulls the cache. The worm wakes up. It scrapes the OIDC token straight out of slash-proc slash-pid slash-mem. Eighty-four TanStack versions published before anyone refreshed npmjs dot com.

<!-- Receipt: https://snyk.io/blog/tanstack-npm-packages-compromised/ -->
<!-- Receipt: https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised -->

## Scene 5: How a TanStack Problem Became Everyone's Problem

And that is how a TanStack problem became everybody's problem. By the next morning, Aikido tracked three-hundred seventy-three poisoned versions across one-hundred sixty-nine packages. Five-hundred eighteen million weekly downloads. Mistral. UiPath. OpenSearch. Guardrails. Squawk. If you ship to N P M, your token was the next link in the chain. The worm did not pick targets. It picked maintainers.

<!-- Receipt: https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised -->
<!-- Receipt: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html -->

## Scene 6: NPM Uninstall Does Not Work

But the worm did not stop at publishing. Here is the twist. You run N P M uninstall. The package leaves. The malware stays. It writes itself into your Claude Code hooks and your V S Code tasks. Reopen your editor, it runs again. Then it signs forged commits as claude at users dot noreply dot github dot com. Branch names from a Dune wordlist. Your AI commits are not a trust signal anymore.

<!-- Receipt: https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/ -->
<!-- Receipt: https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem -->

## Scene 7: The Dead-Man Switch

And my favorite part. The dead-man switch. A daemon polls Github every sixty seconds. If your token throws a forty-X error, it runs r-m dash r-f tilde slash on your machine. The token name? IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner. That is the literal string. Revoke the token and you delete your home folder. The cleanup is the trap.

<!-- Receipt: https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised -->
<!-- Receipt: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html -->

## Scene 8: The pnpm v11 Defense

So how do you stop this? The fix already shipped. P N P M version eleven defaults block the chain. One: minimum release age of twenty-four hours, so new packages sit dormant. Two: blockExoticSubdeps refuses git and tarball deps. Three: approved-builds gates every install script behind your confirmation. Three defaults. Already shipped. Almost nobody migrated.

<!-- Receipt: https://pnpm.io/blog/releases/11.0 -->
<!-- Receipt: https://socket.dev/blog/pnpm-11-adds-new-supply-chain-protection-defaults -->

## Scene 9: Switch or Roll Dice

Three P N P M defaults blocked the entire chain. Almost nobody migrated. So — switching today, or waiting for the next worm? Drop your pick below, and subscribe for the next breakdown.
