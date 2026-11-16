---
name: top5-rankings
description: >-
  Produce Top 5 tool rankings that earn their order: seven fixed weighted
  criteria, a research checklist per tool, hands-on and desk-research
  protocols, a mini claim ledger, and a score table the reader can check.
  Use for any ranked or "best X for Y" comparison post, and for any claim
  that one tool is better than another.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Top 5 Rankings & Hands-on Testing

## What this skill is

A method for producing ranked tool comparisons that earn their order:
explicit criteria, verified evidence per tool, a stated method, and an
honest hands-on vs desk-researched label. The reader can see why each
tool sits where it does — and what was never tested.

Who it is for: anyone writing "best X for Y" posts, tool roundups, or
comparison carousels who wants the ranking to survive a skeptical
reader checking the claims.

## When to use

- Any ranked or comparison post.
- Any "best X for Y" claim anywhere in a post.

## Rules (hard)

- **Never create a Top 5 by copying another creator, repeating
  affiliate rankings, or picking familiar brand names without checking
  them.**
- **Never fabricate a test.** If no test was run, the post is
  desk-researched and says so on the asset.
- **If five credible products cannot be verified, publish a smaller
  shortlist** ("3 tools worth testing") or retitle to "5 options to
  compare" — never invent a ranking or an entry.
- **Sponsorship/affiliates never determine ranking.** Disclose any
  relationship.
- **Add a "last checked" date** to every ranking, as a `[DATE]`
  placeholder filled in on the day you publish (see
  [Dates](#dates)). Never ship a stale date from an earlier draft.
- **Compare on the same task and, where practical, the same
  prompt/input.** Save test notes and example outputs when a test is
  run.

## Weighted ranking criteria (the author's method)

These weights are the author's fixed method for this skill, not a
researched fact — they are stated here so the reader can judge the
ranking, and they do not change between rankings.

| Criterion | Weight |
|---|---|
| Task performance (does it do the stated task well) | 30% |
| Ease of use (learning curve, setup friction) | 15% |
| Value / pricing (free tier generosity, paid step-up) | 15% |
| Features / workflow fit (integrations, fit to the task) | 15% |
| Reliability (uptime, consistency, support) | 10% |
| Privacy / rights / trust (data handling, commercial-use terms) | 10% |
| Availability / support (regions, plans, docs, help) | 5% |

Score each tool 0–10 per criterion, multiply by weight, total /100.
Publish the score table (or a readable summary of it) so the reader can
see why each tool sits where it does.

**Desk-research cap:** where evidence is thin (desk research only), the
task-performance score is capped at **7/10** and marked "desk estimate".
The cap exists because a ranking that never measured performance cannot
award full marks for it. Say so on the asset.

## Claim ledger (mini-ledger, inline — no external dependency)

Before scoring, build a claim ledger: one row per factual claim you
will publish. No claim reaches the post without a ledger row.

| # | Claim | Source (official page, help doc, or test note) | Date checked | Status |
|---|---|---|---|---|
| C1 | [e.g. "Tool X free plan gives 150 tokens/day"] | [official pricing page URL] | [DATE] | CONFIRMED / UNVERIFIED |
| C2 | … | … | … | … |

Status rules: CONFIRMED = read on the official page or measured in a
test you ran. UNVERIFIED = second-hand, outdated, or not yet checked —
do not publish it, or label it as unverified in the post. A template
ledger is in `references/template.md`.

## Required research per tool

- Official product name + verified official URL (domain checked, no
  lookalikes).
- Best-fit task and intended user — what it is best at, not that it is
  universally best.
- Current free tier, trial, pricing, credit limits, regional
  availability — currency + date checked.
- Key features + relevant integrations (no filler features).
- Limitations, output quality, learning curve, privacy/data handling,
  usage restrictions, known gaps.
- Hands-on tested vs desk-researched — labelled.
- Why it earned its position + which audience member should choose it.

## Hands-on test protocol (use when a test IS run)

1. **Fix one task and one input** (same prompt, same source material)
   for every tool.
2. **Run each tool once, same day**, save the raw output
   (screenshot/file) with timestamps.
3. **Score the outputs blind where possible** against the 7 criteria;
   note failures, hallucinations, and time taken.
4. **Record test notes**: date, tool version/model, exact prompt,
   input, output excerpt, score.
5. **Label the post "hands-on tested — [date]"** and link or show the
   evidence. A test that was not run is never described as one.

## Desk-research protocol (use when no test is run)

1. Build the claim ledger first (above).
2. Score from documented evidence only; mark task-performance scores as
   "desk estimate" and cap them at 7/10.
3. State on the asset: "Desk-researched — last checked [DATE]. No
   hands-on test yet."
4. Retitle honestly if the evidence cannot support a strict ranking:
   "5 options to compare" is acceptable; a fabricated #1–#5 is not.

## Dates

Every ranking carries a "last checked" date as a `[DATE]` placeholder in
drafts. Fill it with the actual check date on the day you publish, and
re-check every price and free-tier claim on that day — pricing changes
often, and a ranking with a stale date misleads the reader.

## Top 5 carousel card spec

Each card: consistent ranking badge (#1–#5) · tool name · "best for"
line · key benefit · limitation · access-link cue. Slide 1 = hook +
task + "last checked" date. Final slide = how to choose (which tool
for which reader) + one CTA. 7–10 slides, 1080×1350, slide 2 = second
hook.

## Template

Use `references/template.md` for every Top 5 build: claim ledger,
per-tool research sheet, score table, and card spec checklist.

## Worked example — 5 AI image generators for social post visuals

> TEMPLATE — replace the topic, tools, and scores with your own. The tools and prices below are public data used to show the format, not content to copy.

**Task (fixed for all five):** generate a 1080×1350 social post visual
with a readable headline. **Method:** desk-researched only — no hands-on
test was run. **Last checked:** 16 November 2026. Prices below were
verified against the vendors' pricing pages via search on that date;
re-check them before reuse, because pricing changes.

| Tool (official site) | Entry point verified 16 Nov 2026 |
|---|---|
| Midjourney (midjourney.com) | No free plan. Basic $10/month. |
| Adobe Firefly (adobe.com) | Free plan with limited generations. Standard $9.99/month (2,000 credits). |
| Ideogram (ideogram.ai) | Free plan (weekly credits; free images public). Plus $20/month, or $15/month billed annually. |
| Leonardo AI (leonardo.ai) | Free plan, 150 tokens/day. Essential $12/month. |
| ChatGPT — GPT Image (chatgpt.com) | Free with limits. Plus $20/month. |

**Score table (0–10 per criterion; task-performance scores are desk
estimates, capped at 7/10 per the desk-research rule):**

| Tool | Task perf. (30%) | Ease (15%) | Value (15%) | Features (15%) | Reliability (10%) | Privacy (10%) | Availability (5%) | Total /100 |
|---|---|---|---|---|---|---|---|---|
| #1 Adobe Firefly | 6 | 8 | 8 | 7 | 8 | 9 | 8 | **74** |
| #2 ChatGPT (GPT Image) | 7 | 9 | 6 | 7 | 8 | 6 | 8 | **72** |
| #3 Leonardo AI | 6 | 7 | 8 | 8 | 7 | 6 | 7 | **69** |
| #4 Ideogram | 7 | 7 | 7 | 6 | 7 | 6 | 7 | **68** |
| #5 Midjourney | 7 | 6 | 5 | 7 | 8 | 6 | 6 | **65** |

Worked total, Firefly: 6×0.30 + 8×0.15 + 8×0.15 + 7×0.15 + 8×0.10 +
9×0.10 + 8×0.05 = 1.80 + 1.20 + 1.20 + 1.05 + 0.80 + 0.90 + 0.40 =
7.35 → 74/100.

**Best-for lines (example):**

- #1 Adobe Firefly — best for commercial-safe brand work (licensed
  training data; strongest free-to-paid step-up in this set).
- #2 ChatGPT — best for text-in-image and chat-based edits.
- #3 Leonardo AI — best for high-volume creation and consistent
  characters (most generous free daily allowance here).
- #4 Ideogram — best for posters and images with accurate text.
- #5 Midjourney — best for artistic, polished-looking images; the only
  tool here with no free plan.

**What the asset would say:** "Desk-researched — last checked
16 November 2026. No hands-on test yet." Scores are illustrative
example scores for this worked example, not measured test results —
they show the method, and a real ranking must re-verify every price
and re-score from its own evidence.

## Troubleshooting

| Problem | Fix |
|---|---|
| Only 3–4 credible tools verify | Publish a smaller shortlist or retitle to "options to compare". Never pad the list. |
| A price changed since the last check | Re-check the official pricing page, update the ledger row date, and re-score Value before publishing. |
| Two tools tie | Break the tie on the highest-weighted criterion (task performance), and say so. If still tied, list them as tied — do not invent a gap. |
| A tool's free tier disappeared | Re-score Value and Availability from the new facts; if the tool no longer fits the task, drop it and say why. |
| Evidence is thin for one criterion | Score conservatively, mark it "desk estimate", and note the gap on the asset. |

## Known limits

- The weights are the author's method, not a researched fact. A
  different weighting would produce a different order — that is why the
  score table is published with the ranking.
- Desk-researched scores are estimates, not measurements. The 7/10
  task-performance cap exists for exactly this reason.
- Prices and free-tier limits change frequently. A ranking is only as
  current as its "last checked" date.
