#!/usr/bin/env node
/*
 * scripts/find-dynamous-module.js
 *
 * Picks the best-matching Dynamous AI Mastery module for given topic
 * tags by scoring keyword overlap. Prints "MODULE N — Title" or
 * "NO_MATCH" when nothing scores > 0.
 *
 * Usage:
 *   node scripts/find-dynamous-module.js "mcp" "tool"
 *   node scripts/find-dynamous-module.js "claude code" "subagent"
 *
 * Algorithm mirrors `findMatchingModule()` in
 * diy-yt-creator/src/shared/constants/dynamous.ts: lowercase the input
 * tags, score each module by counting how many of its keywords appear
 * as a substring of any input tag, return the highest-scored module.
 */

const fs = require("fs");
const path = require("path");

const DATA_PATH = path.join(
  __dirname,
  "..",
  "shared",
  "lib",
  "components",
  "dynamous-data",
  "dynamous-modules.json"
);

const tags = process.argv.slice(2).map((t) => t.toLowerCase());
if (tags.length === 0) {
  console.error("Usage: node scripts/find-dynamous-module.js <tag1> [tag2] ...");
  process.exit(2);
}

const data = JSON.parse(fs.readFileSync(DATA_PATH, "utf8"));

let best = { module: null, score: 0 };
for (const m of data.modules) {
  let score = 0;
  for (const kw of m.keywords) {
    const k = kw.toLowerCase();
    if (tags.some((t) => t.includes(k) || k.includes(t))) score++;
  }
  if (score > best.score) best = { module: m, score };
}

if (!best.module) {
  console.log("NO_MATCH");
  process.exit(0);
}

console.log(`MODULE ${best.module.id} — ${best.module.title}`);
