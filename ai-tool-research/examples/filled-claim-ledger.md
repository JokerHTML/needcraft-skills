# Worked example: a filled claim ledger

**Status: example.** Three real claims, verified 16 November 2026, with the confidence each one earned under the skill's definitions. Copy the table structure, replace every row with your own post's claims.

## The post

A comparison post naming three tools' free or entry prices. Every figure below appears in the post's copy, so every figure gets a ledger row.

## Ledger

| # | Claim | Source URL | Source date | Access date | Confidence | Exact supported wording |
|---|---|---|---|---|---|---|
| 1 | n8n Cloud Starter is €20/month billed annually, with 2,500 executions/month | https://n8n.io/pricing | n/a (live pricing page) | 16 Nov 2026 | HIGH | "n8n Cloud Starter is €20/month when billed annually and includes 2,500 executions a month (last checked 16 Nov 2026)." |
| 2 | Zapier Free is $0/month with 100 tasks/month and two-step Zaps | https://zapier.com/pricing | n/a (live pricing page) | 16 Nov 2026 | HIGH | "Zapier Free costs $0/month and includes 100 tasks a month with two-step Zaps (last checked 16 Nov 2026)." |
| 3 | Perplexity Pro is $20/month billed monthly, or $17/month billed annually ($200/year) | Perplexity pricing hub (perplexity.ai) — page did not load in the verification session; figures corroborated by multiple independent summaries of Perplexity's own pricing pages | n/a (live pricing page) | 16 Nov 2026 | MEDIUM | "Perplexity Pro is listed at $20/month on monthly billing, or $17/month when billed annually — $200 a year (last checked 16 Nov 2026; verify at checkout)." |

## Why the confidences differ

- **Rows 1–2 are HIGH:** the official pricing pages were read directly in the verification session (n8n.io/pricing and zapier.com/pricing, both crawled 16 Nov 2026). The figures above are what those pages showed.
- **Row 3 is MEDIUM:** the Perplexity pricing page could not be read directly, so the figures rest on multiple independent summaries of Perplexity's own pages, all agreeing on $20 monthly / $17 annual-equivalent / $200 a year. Under the skill's definitions that is MEDIUM. Re-open the official page before quoting it and upgrade the row to HIGH only after reading it yourself.

## An UNVERIFIED row (how to handle a gap)

| # | Claim | Source URL | Source date | Access date | Confidence | Exact supported wording |
|---|---|---|---|---|---|---|
| 4 | "Tool X's Pro plan costs $Y/month" | _(official pricing page URL — opened, price table did not render)_ | — | 16 Nov 2026 | UNVERIFIED | "Tool X's Pro price could not be confirmed — the official pricing page did not render on 16 Nov 2026. No price is stated." |

The figure does not appear in the post. The post says instead: "Tool X offers a paid Pro plan; the price is not stated here because it could not be verified."
