NPM supply chain attack just hit hard. The Shai-Hulud worm hijacked Tanstack in 6 minutes via one fork-PR, then jumped to 169 npm packages — Mistral AI, UiPath, OpenSearch, Guardrails AI, Squawk. Signed. SLSA-attested. Still malware. Here's exactly how — and how pnpm v11 already blocks it.

What's in this short:
- The `pull_request_target` smoking gun in Tanstack's `bundle-size.yml` — fork code ran with main-repo permissions
- The 1.1 GB poisoned GitHub Actions cache that sat ~8 hours until an unrelated merge weaponized it
- How one stolen OIDC token cascaded into 373 poisoned versions across 169 packages (518M weekly downloads)
- The dead-man switch: a daemon polls GitHub every 60 seconds and runs `rm -rf ~/` if you revoke the stolen token
- Why `npm uninstall` does NOT remove the worm — it writes itself into Claude Code hooks and VS Code tasks
- The three pnpm v11 defaults that block the entire chain: `minimumReleaseAge: 1440`, `blockExoticSubdeps: true`, `allowBuilds`

Chapters
0:00 NPM Just Got Hijacked — Shai-Hulud Worm Hits Tanstack (169 Packages, 6 Minutes)
0:21 The pull_request_target Smoking Gun — How One Fork-PR Owned Tanstack's CI
0:44 The GitHub Actions Cache Bomb (1.1 GB Poisoned pnpm Store)
1:12 How One Worm Hit 169 npm Packages — Mistral, UiPath, OpenSearch (518M Downloads)
1:38 NPM Uninstall Doesn't Work — Claude Code Hooks + VS Code Persistence
2:02 The Dead-Man Switch — Revoke the Token, Lose Your Home Folder
2:23 The pnpm v11 Fix — Three Defaults That Block the Entire Attack Chain
2:47 Switch to pnpm v11 Today, or Roll Dice on the Next Worm?

Resources (all URLs verified May 2026):
- Aikido Security primary report — Mini Shai-Hulud is Back, Tanstack Compromised: https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised
- Wiz technical writeup — Mini Shai-Hulud Strikes Again (60s poll, OIDC theft from /proc/pid/mem): https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised
- Snyk breakdown — Tanstack npm Packages Compromised (bundle-size.yml misconfig + 8h cache poison): https://snyk.io/blog/tanstack-npm-packages-compromised/
- BleepingComputer — Shai-Hulud Ships Signed Malicious Tanstack + Mistral npm Packages (editor persistence): https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/
- StepSecurity — Mini Shai-Hulud Self-Spreading Supply Chain Attack (forged Claude Code commits, Dune branch names): https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem
- The Hacker News — Mini Shai-Hulud Worm Compromises (CVE-2026-45321, dead-man token name): https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
- pnpm v11 release notes — minimumReleaseAge: 1440, blockExoticSubdeps: true defaults: https://pnpm.io/blog/releases/11.0
- Socket.dev — pnpm 11 Adds New Supply Chain Protection Defaults: https://socket.dev/blog/pnpm-11-adds-new-supply-chain-protection-defaults

Key Concepts:
- **`pull_request_target` (GitHub Actions)** — A workflow trigger that runs in the context of the base repository with WRITE permissions to secrets, even when triggered by a fork's PR. When combined with `actions/checkout` of the PR's merge ref (`refs/pull/$PR/merge`), fork-controlled code executes with main-repo credentials. This was the entry point in Tanstack's `bundle-size.yml`.
- **SLSA Level 3 attestation** — Cryptographic build provenance proving a package was produced by a trusted CI pipeline. The Mini Shai-Hulud worm is the first documented npm malware shipping with valid SLSA Level 3 provenance — the attestation is real, the malware is real. Trusted publishing is a permissions boundary, not a trust boundary.
- **Dead-man switch (`IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner`)** — A persistence-trap daemon that polls GitHub every 60 seconds for the stolen token's status. On any 40X auth error (i.e., revocation), it executes `rm -rf ~/` on the infected machine. The literal npm token name is the trap.
- **pnpm `minimumReleaseAge: 1440`** — pnpm v11 default that refuses to resolve any npm package version published less than 24 hours (1,440 minutes) ago. Cooling-off window for human detection. Single config change blocks the typical worm propagation window.
- **CI cache poisoning** — GitHub Actions caches persist across workflow runs and are keyed by content hash. Tanstack's pnpm cache (1.1 GB) sat poisoned for 8 hours after the attacker's fork-PR closed; the next unrelated merge restored it and ran the malware with real publish permissions.

Switching to pnpm v11 today, or waiting for the next worm to hit your stack? Drop your pick in the comments. The defense already shipped before this attack even happened — pnpm v11 had the three defaults on by default. Almost nobody migrated. So which side are you on: migrate this week, or roll dice on the next worm wave?

#NPM #SupplyChainAttack #ShaiHulud #Tanstack #PNPM #JavaScript #NodeJS #WebSecurity #DevSecOps #GitHubActions #OpenSourceSecurity #Malware #CyberSecurity #Programming #CodingNews #SmartCodeDIY #FromTheDevDesk #DevTools #SoftwareSupplyChain #PackageManager #OIDC #NPMMalware #ClaudeCode #VSCode
