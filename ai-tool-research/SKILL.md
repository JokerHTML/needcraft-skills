---
name: ai-tool-research
description: >-
  Verify every AI tool claim from a primary source before it enters your copy, and keep a claim ledger so any price, free-tier limit, or feature traces to a URL, a date, and a confidence level. Use before drafting any Top 5, tutorial, news, or comparison post, and whenever a price, limit, or feature is about to be written.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# AI Tool Research & Verification

## What this skill is

A method for verifying every tool claim from a primary source before it enters your copy, and keeping a claim ledger so any claim can be traced to a URL, a date, and a confidence level. It exists because AI tool prices, free tiers, and features change constantly — and because a wrong price in a post is a wrong price in public.

Who it is for: anyone writing Top 5 lists, tutorials, news, or comparisons about AI tools — a creator, a small team, or an agent drafting on their behalf.

## How to use this skill

1. Name each claim precisely before you research it (see Process).
2. Open the official page, record what it actually showed, and assign confidence.
3. Write the supported wording — the exact sentence the source supports, nothing more.
4. Build the claim ledger: one row per claim that appears in copy, on-screen text, or a visual.
5. Re-verify on posting day. Prices and limits change without notice.

## Rules (hard)

- **Primary sources first:** official product site, changelog, docs, pricing page, platform policy page. Independent sources are context, never the sole basis for a price or limit claim.
- **Never fabricate a test, output, speed result, or personal experience.** Label every assessment "hands-on tested" or "desk-researched" — and until a real test run exists, everything is desk-researched by definition.
- **UNVERIFIED = do not publish the figure.** Use only the ledger's "supported wording" for that row.
- **Never quote a figure from a page that did not render.** If the price table did not load, record the render failure, not a guess.
- **No rumours, leaks, or social-only claims as facts.** No benchmark screenshots as facts without corroboration.
- **Regional availability, currency, and date checked** for every price and free-tier claim. Prices are US list unless stated otherwise; n8n Cloud lists prices in euros (verified on its pricing page 16 Nov 2026 — the page shows a local-currency equivalent for your region).
- **Last-checked date on every asset.** Every price or limit claim carries its check date.

## Process

1. **Name the claim precisely** (e.g. "Perplexity Pro is $20/month billed monthly, $17/month billed annually" — not "Perplexity is cheap").
2. **Open the official page** (pricing / help / changelog). Record URL, source date, access date, and what the page actually showed.
3. **Assign confidence:**
   - **HIGH** = read directly from the official page this session.
   - **MEDIUM** = official-domain text via a search snippet, or the page loaded but the figure did not render, or the claim is corroborated by multiple independent summaries of the official page but you did not read the official page yourself.
   - **UNVERIFIED** = not confirmed from the official page (third-party consensus only).
4. **Write the supported wording** — the exact sentence the source supports, nothing more.
5. **Check the competing alternative** (at least one) so the claim is comparative, not isolated.
6. **Re-verify on posting day** for every price and limit; log any change and correct the copy before it ships.

## Conflicting sources — how to decide

Sources disagree often: a pricing page shows one number, a help article another, a review a third. Decide in this order:

1. **The official page that charges the money wins.** The pricing or checkout page outranks a help article, which outranks a blog post, which outranks a review.
2. **Newer wins, when both are official.** A changelog or pricing page dated this month outranks a help article from last year. Record both dates in the ledger.
3. **The more specific figure wins.** A figure that names its billing period ("$17/month billed annually") outranks a bare figure ("$17/month").
4. **When two official pages disagree, say so.** Write the supported wording with the discrepancy named — e.g. "Perplexity's pricing hub lists Pro at $20/month; its Pro page shows $17/month billed annually ($200/year). Check at checkout." Never silently pick one and hide the other.
5. **When nothing official can be found, the claim is UNVERIFIED** and does not appear as a stated figure. A third-party consensus is not a source.

## Claim ledger (per post — required)

One row per claim that appears in copy, on-screen text, or a visual. UNVERIFIED rows: the claim must NOT appear in the post as a stated figure; use the supported wording instead.

| # | Claim | Source URL | Source date | Access date | Confidence | Exact supported wording |
|---|---|---|---|---|---|---|
| 1 | n8n Cloud Starter is €20/month billed annually, with 2,500 executions/month | https://n8n.io/pricing | n/a (live pricing page) | 16 Nov 2026 | HIGH | "n8n Cloud Starter is €20/month when billed annually and includes 2,500 executions a month (last checked 16 Nov 2026)." |
| 2 | Zapier Free is $0/month with 100 tasks/month and two-step Zaps | https://zapier.com/pricing | n/a (live pricing page) | 16 Nov 2026 | HIGH | "Zapier Free costs $0/month and includes 100 tasks a month with two-step Zaps (last checked 16 Nov 2026)." |
| 3 | Perplexity Pro is $20/month billed monthly, or $17/month billed annually ($200/year) | Perplexity pricing hub (perplexity.ai) — page did not load in the verification session; figures corroborated by multiple independent summaries of Perplexity's own pricing pages | n/a (live pricing page) | 16 Nov 2026 | MEDIUM | "Perplexity Pro is listed at $20/month on monthly billing, or $17/month when billed annually — $200 a year (last checked 16 Nov 2026; verify at checkout)." |

**Why row 3 is MEDIUM, not HIGH:** the Perplexity pricing page could not be read directly in the verification session (the page did not load), so the figures are corroborated by multiple independent summaries of Perplexity's own pricing pages, all agreeing on $20 monthly / $17 annual-equivalent / $200 a year. Under this skill's own definitions that is MEDIUM. Re-open the official page before quoting it and upgrade the row to HIGH only after reading it yourself.

**Corrections:** if a fact changes after publishing, update where possible and add a correction note.

A standalone copy of this ledger is in `examples/filled-claim-ledger.md`.

## Handling unverified areas (worked example)

Every research pass leaves gaps. Do not point at an external research pack the reader cannot see. Instead, write the gap into the ledger as an UNVERIFIED row with a concrete next step, like this:

| # | Claim | Source URL | Source date | Access date | Confidence | Exact supported wording |
|---|---|---|---|---|---|---|
| 4 | "Tool X's Pro plan costs $Y/month" | _(official pricing page URL — opened, price table did not render)_ | — | 16 Nov 2026 | UNVERIFIED | "Tool X's Pro price could not be confirmed — the official pricing page did not render on 16 Nov 2026. No price is stated." |

Then do one of these, in order:

1. **Try the page again** in a different browser or at a later time — render failures are often transient. Record each attempt.
2. **Try the vendor's help centre or changelog** for the same figure. If it appears there, the row becomes MEDIUM with the help URL as the source.
3. **Try the vendor's checkout or signup flow** up to (not including) payment — the price shown there is official.
4. **If all three fail, cut the figure.** Write around it: "Tool X offers a paid Pro plan; the price is not stated here because it could not be verified." A missing price is honest. A guessed price is a lie.

Typical unverified areas in AI-tool research: consumer plan prices that change by region, free-tier usage caps that are not published as numbers, daily credit allowances, per-clip generation costs, and notebook/source limits. Treat every one of them as UNVERIFIED until an official page states the number.

## Verification checklist (before a post leaves draft)

- [ ] Every price/limit has a ledger row with an official URL.
- [ ] No UNVERIFIED figure appears as a stated price, limit, or count.
- [ ] Official domain verified (no lookalike links).
- [ ] Hands-on vs desk-researched label present and true.
- [ ] "Last checked" date present.
- [ ] Sponsorship/affiliate status disclosed if any (none assumed — state it explicitly).
- [ ] Conflicting sources resolved by the rule above, with discrepancies named in the copy where they exist.

## Re-check cadence

- **On posting day:** re-open every official page in the ledger and correct the copy if anything changed. Free-tier limits change without notice — this is the most important re-check in the skill.
- **Monthly:** re-check the standing figures you quote most often (the three example rows above are a good start) and update the "last checked" date.
- **When a reader reports a wrong figure:** treat it as a bug. Re-check the official page the same day, correct the post, and add a correction note. Do not argue from memory.
- **When a page stops rendering:** record the failure and the date; do not carry the old figure forward as if it were re-verified.

## Known limits

- This skill verifies claims against published sources. It cannot verify a claim the vendor does not publish — usage caps, unpublished limits, and regional prices that only appear at checkout are UNVERIFIED by definition until you see them yourself.
- Prices are stated as last checked on 16 November 2026. AI tool pricing changes frequently; a figure quoted without a date is a stale figure.
- A HIGH-confidence row means "read from the official page on the stated date". It does not mean the price will be the same tomorrow.
- The example ledger rows are real, verified claims — but they are examples, not a standing price list. Re-check them before reuse.
