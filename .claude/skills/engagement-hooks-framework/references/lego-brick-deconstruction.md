# Lego-Brick Deconstruction

> "There are seven Lego brick categories that matter. All you have to do is figure out what videos and creators are winning in your category. Explode their best videos into those seven pieces. Hold as many constant as you think are world class and improve on the ones that aren't. Restack into your own new Lego formation and post." — Kallaway

The Lego-Brick framework eliminates "creative gut feel". Instead of designing a video from scratch, deconstruct 3-5 outliers, isolate which bricks are world-class in each, then restack the best bricks into your own formation. **Volume negates luck. Iteration on identified bricks negates volume.**

## The seven bricks

| # | Brick | What it covers | How to score 1-10 |
|---|---|---|---|
| 1 | **Topic** | The broad subject matter (e.g., "AI productivity", "YouTube SEO", "Anthropic deal") | How well does it map to a high-performing topic in the niche? Does Sandcastles / vidIQ data confirm topic outliers? |
| 2 | **Angle** | The unique, non-obvious perspective ON the topic | How counterintuitive is it? How specific? Could it have been generated from the title alone? |
| 3 | **Hook Structure** | First 3 seconds — visual, text, spoken | Does it stop the scroll? Triple-Threat aligned? Violent Contrast applied? |
| 4 | **Story Structure** | Narrative flow — case study, listicle, breakdown, comparison | Does it match the topic's natural shape? Or is it forcing a viral format? |
| 5 | **Visual Format** | Screen layout — split-screen, POV, cinematic, talking head, faceless typography | Does the layout reinforce the topic, or is it generic? |
| 6 | **Key Visuals** | Specific assets — A-roll, B-roll, AI-generated, screenshots, charts | Are they earning the screen time? Or are they decoration? |
| 7 | **Audio** | Soundscape, music, SFX, pacing triggers | Does it carry energy at the right moments? Or is it ambient padding? |

## When to run a deconstruction

| Situation | Run a deconstruction? |
|---|---|
| Starting a new video on a topic you've never made before | **Yes** — find 3-5 outliers in the niche before Phase 1 plan |
| Following a successful 5x outlier of your own | **Yes** — deconstruct your OWN outlier to identify which 3 bricks carried the win |
| Standard feature-update video (e.g., Claude Code v2.1.NN) | Skip — the playbook is already proven, just apply the carry-forward rules |
| Short on a topic identical to one shipped recently | Skip — use the prior video's bricks as the baseline |
| New aesthetic / template variant | **Yes** — find 3-5 outliers in the new aesthetic to validate the visual + audio bricks |

## Workflow

### Step 1 — Identify the outliers

Use Sandcastles, vidIQ, or manual search. Filter for:
- Outlier score ≥ 5x channel average
- Same niche / target audience as the planned video
- Posted in the last 3 months (to capture current platform behavior)
- 5 videos minimum for statistical signal

If only 1-2 candidates exist, the niche is too narrow OR you're in a brand-new format. In that case, deconstruct the 1-2 you have and supplement with general engagement patterns from `winning-patterns.md`.

### Step 2 — Fill the deconstruction template per video

For each outlier, fill this YAML:

```yaml
# Outlier Deconstruction
url: https://youtube.com/watch?v=XXX
channel: <name>
title: <title as displayed>
posted: YYYY-MM-DD
metrics:
  views: <number>
  outlier_score: <e.g., 7.3x>
  engagement_rate: <%>
  comments: <number>
  retention_curve_3s: <% if known>
  retention_curve_30s: <% if known>

bricks:
  topic:
    score: 1-10
    notes: <one sentence on why this score>
  angle:
    score: 1-10
    notes: <the contrarian / unique frame>
  hook_structure:
    score: 1-10
    notes: <pattern A/B/C/D/E from triple-threat-hook.md>
    visual: <what shows in first 3s>
    text: <on-screen text first 3s>
    spoken: <verbatim first sentence(s)>
  story_structure:
    score: 1-10
    notes: <narrative arc — setup-tension-payoff per scene? listicle? case study?>
  visual_format:
    score: 1-10
    notes: <layout — talking head, screen recording, faceless typography, kinetic type>
  key_visuals:
    score: 1-10
    notes: <the 3-5 assets that did the heavy lifting>
  audio:
    score: 1-10
    notes: <music genre, SFX use, pacing triggers — beat-aligned cuts? swell on reveals?>

carry_forward_candidates:
  - <brick name + specific element to lift>
  - <brick name + specific element to lift>

what_NOT_to_copy:
  - <element that worked for them but won't work for us — usually because of voice, brand, or audience mismatch>
```

Save each deconstruction to `videos/<slug>/research/deconstruction-<channel>-<short-id>.md`.

### Step 3 — Aggregate — find the world-class bricks

Across all 5 deconstructions, count which bricks scored 8+ in 3 or more videos. Those are the **world-class bricks for this niche right now**. Hold them constant.

Bricks that scored ≤5 in most outliers, OR varied widely (some 10, some 3), are the **iteration zone**. That's where you experiment.

Example aggregation (5 videos):

| Brick | Avg score | Spread | Verdict |
|---|---|---|---|
| Topic | 9.2 | 8-10 | World-class — niche has clear topic winners |
| Angle | 6.4 | 4-9 | Iterate — angle is what separates the top from the middle |
| Hook | 8.6 | 7-10 | World-class — strong hook patterns dominate |
| Story | 5.8 | 3-8 | Iterate — no consensus structure |
| Visual | 7.0 | 5-9 | Mostly settled — minor experimentation OK |
| Key visuals | 6.2 | 4-8 | Iterate |
| Audio | 8.0 | 7-9 | World-class — current music + SFX patterns work |

→ Hold: Topic, Hook, Visual, Audio. Iterate: Angle, Story, Key Visuals.

### Step 4 — Restack into your video's plan

The Phase 1 plan inherits from the aggregation:

- **World-class bricks** → mirror the dominant pattern. Don't reinvent.
- **Iteration bricks** → pick a specific iteration target ("we're going to try a contrarian-rank story instead of a feature-listicle, holding everything else constant").

Limit experiments to **1-2 iteration bricks per video**. Any more and you can't attribute results.

### Step 5 — Post-ship — measure and update

After ship, log the actual performance:

```yaml
shipped_video: videos/<slug>
shipped_metrics:
  views_at_30d: <number>
  retention_3s: <%>
  retention_30s: <%>
  outlier_score: <e.g., 2.1x>

bricks_carried_forward:
  - <name>: <result — outperformed / par / underperformed>

iteration_targets:
  - angle: <what was tried, what happened>
  - story: <what was tried, what happened>

verdict:
  - <which iterations to keep>
  - <which to revert>
```

Save to `videos/<slug>/research/post-ship-review.md`. The next deconstruction starts from this output.

## Carry-Forward Rule (10x batch system)

From the Master Blueprint and Kallaway's 10x batch process:

| Outlier score | Carry forward |
|---|---|
| < 5x (no winner) | Re-run from scratch — the bricks didn't compose. Look for an obvious miss in hook or substance. |
| 5x to 10x | Take that exact topic + format. **3 of your next 10 videos** should follow it (with the angle iterated). |
| ≥ 10x | Take exact topic + exact format + exact angle. Replicate aggressively across the next batch. |

**Never replicate 100% of a winner across all 10 next videos** — viewer fatigue kicks in. 3 of 10 is the sweet spot.

## What this skill replaces / augments in the existing pipeline

- **Replaces**: nothing. The existing `phase0-research.md` doesn't have a structured outlier-deconstruction step.
- **Augments**: `phase1-plan.md` Step "Outlier analysis" can call this skill in deconstruct mode when the brief has ≥ 3 reference video URLs.
- **New artifact**: `videos/<slug>/research/deconstruction-*.md` and `videos/<slug>/research/aggregation.md`.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Deconstructing only 1-2 outliers | No statistical signal — one outlier may be a fluke (right-place, right-time) |
| Scoring bricks holistically (single 1-10 for "the video") | Loses the deconstruction's purpose — you want per-brick clarity, not overall vibes |
| Lifting all 7 bricks from one video | That's cloning, not iterating. The brain rejects 1:1 clones. |
| Iterating ≥ 3 bricks at once | Can't attribute the result — you don't know which iteration moved the needle |
| Skipping post-ship measurement | The framework decays into theater without the feedback loop |
