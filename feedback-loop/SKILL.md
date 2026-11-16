---
name: feedback-loop
description: >-
  Turn every customer question, comment, objection, or refund into a classified, routed, fixed,
  and verified improvement: capture verbatim feedback, classify it into one of nine labels,
  find the root cause, fix at the smallest effective level, verify by re-testing the exact
  customer scenario, and log it. Use for any customer feedback about a digital product or
  its content.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Feedback Loop

## What this skill is

A seven-step loop that turns customer feedback into product improvement without letting
every request become a feature: capture, classify, root-cause, decide, fix, verify, log.
One fix per feedback item, at the smallest effective level, verified against the exact
scenario the customer described.

Who it is for: a solo creator or small team selling a digital product (guide, template,
course, or similar) who answers their own support mail and wants every message to either
improve the product or improve the listing — and to be able to prove which one it was.

## Prerequisites

- A support inbox you control (any email inbox, form, or DM channel — this skill does
  not assume a particular tool).
- Access to the product itself (the actual files the customer received) so you can
  reproduce their issue.
- Access to the sales listing / product page so you can check what was promised before
  blaming the product.
- A feedback log file (see "Output"). Create it at a path you choose and keep it in one
  place — it is internal, never customer-facing.
- Your refund terms written down before you need them (see "Refund terms" below).

## Inputs

For every feedback item, collect three things before you do anything else:

- The **verbatim feedback** — the customer's exact words, not a paraphrase.
- The **source** — email, comment, review, refund request, or DM — plus a link or
  message ID if you have one.
- The **date received**.

## The process

### 1. Capture

Record the verbatim feedback, source, and date. Do not paraphrase away the customer's
phrasing — the exact words are often the diagnosis.

### 2. Classify

Put the item into exactly one of the nine labels below. The first label is a hypothesis,
not a verdict: if new information changes the picture, re-classify and note the change.

| Label | Definition | Example (illustrative) |
|---|---|---|
| QUESTION | The customer asks how something works or what something means. No problem is reported and nothing is missing. | "Does the guide cover repotting after the first month?" |
| CONFUSION | The customer tried to use the product and got stuck, misunderstood a step, or could not find something that is actually there. | "I can't find the templates — where are they?" (templates exist, on page 6) |
| OBJECTION | The customer doubts the product's value, fit, or premise before or after buying, but is not asking for a refund. | "This looks useful, but I doubt it works for my niche." |
| BUG | Something in the product is broken: a dead link, a corrupt file, a wrong value, a step that cannot be completed as written. | "The download link on page 3 returns a 404." |
| MISSING CONTENT | The product works as written but a reasonable, promised piece is absent. | "The listing says 10 scripts — I count 7." |
| EXPECTATION GAP | The customer expected something the product never promised, because the listing, the content, or a post set the wrong expectation. The product is fine; the promise was wrong. | "I thought this would write the emails for me." (The listing promises templates, not done-for-you writing.) |
| FEATURE REQUEST | The customer asks for something new that the product never claimed to do. | "Could you add a version for agencies?" |
| POSITIVE SIGNAL | The customer reports a good outcome, a compliment, or a result. | "Used script 2 and got a reply the same day." |
| REFUND SIGNAL | The customer asks for a refund, hints at one, or says the product is not what they wanted in a way that points at a refund. | "This isn't what I expected — can I get my money back?" |

**Telling close labels apart:**

- **CONFUSION vs EXPECTATION GAP.** Ask: does the product already do what they want?
  If yes and they could not find or follow it, it is CONFUSION (fix the onboarding or
  the signposting). If no — they want something the product never promised — it is an
  EXPECTATION GAP (fix the listing or the content that set the expectation, not the
  product). The test is the product, not the customer's confidence: open the product
  and try their scenario yourself.
- **OBJECTION vs REFUND SIGNAL.** An OBJECTION argues about value or fit and leaves the
  door open ("convince me"). A REFUND SIGNAL asks for money back, or states the product
  is not what they wanted in a way that only a refund resolves. When in doubt, treat it
  as a REFUND SIGNAL — it gets same-day triage either way, and downgrading it later is
  cheap while missing it is not.

### 3. Identify root cause

Ask: is this the product, the listing copy, the onboarding, a missing file, or a wrong
expectation set by your content? **Check the listing BEFORE blaming the product.**
Open the sales page and the content that drove the purchase and read what was actually
promised. Then reproduce the customer's exact scenario against the actual product files.

### 4. Decide action

Exactly one action per item:

- **PRODUCT FIX** — change the product itself.
- **FAQ FIX** — add or correct an FAQ / help answer.
- **CONTENT IDEA** — the feedback is worth a post or a piece of content (an objection
  many people share, a confusion worth explaining publicly).
- **SALES PAGE FIX** — change what the listing promises.
- **ONBOARDING FIX** — change how the buyer is welcomed, guided, or pointed at the
  right file first.
- **NO ACTION** — record the reason (e.g. out of scope, one-off preference, already
  covered). NO ACTION items still get logged.

### 5. Fix at the smallest effective level

One fix per feedback item. Do not bundle unrelated changes into one edit — a bundled fix
cannot be verified item by item and cannot be rolled back cleanly.

### 6. Verify the fix

Re-test the exact customer scenario end to end, against the actual product files. For a
listing fix, re-read the whole listing against the product (a listing regression check:
name, price, description, download file, claims, refund info, and links all still
correct). Unresolved items stay OPEN in the log — never mark resolved on intent.

### 7. Log it

Every item gets a log entry, including NO ACTION items with the reason. See "Output".

## Finding feedback in your inbox (generic procedure)

This skill does not assume a particular inbox tool. Whatever you use, the procedure is:

1. Search the support inbox for the product name and for the customer's name or email.
2. Read the full thread, not just the latest message — the context usually sits two
   messages back.
3. Search for the same issue from other customers (same keywords, same error). One report
   is a fix; three reports with the same words is a listing problem.
4. If the feedback arrived as a comment or review, reply there only to acknowledge and
   point to the support channel — do not debug in public.

## Response templates and SLA

### Example response (adapt the brackets; this is an illustrative template, not a real reply)

> Hi [name] — thanks for flagging this, and sorry it tripped you up. I checked: [what you
> found — e.g. "the templates are on page 6, but the contents page doesn't point there,
> so it's easy to miss"]. I've [fixed it / added a pointer on page 2] and the updated
> file is in your download link now — no need to re-buy. If it still doesn't open, reply
> here and I'll send it directly. — [your name]

Rules for every reply: answer what they asked, state what you checked, state what you
changed (or why nothing changes), and give one concrete next step. Never promise what
the product does not contain. Never invent a fix you have not made.

### SLA guidance (set your own numbers; these are recommended starting points)

| Signal | Target |
|---|---|
| REFUND SIGNAL | Same-day triage — read it, classify it, and reply the same day. Do not let it sit overnight. |
| BUG | Acknowledge within 1 business day; fix or workaround within 3 business days. |
| CONFUSION / QUESTION | Reply within 1 business day. |
| OBJECTION / EXPECTATION GAP | Reply within 2 business days — these need a careful answer, not a fast one. |
| FEATURE REQUEST / POSITIVE SIGNAL | Acknowledge within 3 business days. |

If you cannot meet a target, say so in the reply with a real date — a missed silent
deadline is worse than a stated slow one.

## Refund terms

Write your refund terms down before your first sale and state them the same way
everywhere (listing, FAQ, and reply). This skill does not set your terms for you; the
recommended shape is **fix-first within a 30-day window**: if the product does not work
as described, you fix it first (or replace the file), and if the fix does not resolve it
within the window, you refund. Whatever your terms are, check them before replying to
any refund signal — never improvise refund policy in a reply.

## Quality rules

- Do not turn every customer request into a product feature. Most requests are
  information gaps, not product gaps.
- Expectation gaps are usually fixed in the listing or the content, not the product.
  Fix the promise, not just the thing.
- Refund signals get same-day triage — always.
- Positive signals feed testimonials ONLY with the customer's explicit permission.
  Never fabricate testimonials, reviews, or screenshots.
- Honesty rules apply: never promise what the product does not contain. Product claims
  stay within your product's claims source — the single file or page where you keep what
  the product actually contains and what the listing promises. If you do not have one,
  write it before your next sale: list every claim on the listing and check each one
  against the product files.

## Failure modes

- **Misclassification.** If new info changes the picture, re-classify. The first label
  is a hypothesis, not a verdict.
- **Fixing the product when the listing set the wrong expectation.** Always check the
  listing and the content that drove the purchase first.
- **Silent fixes with no log.** Every fix gets logged. An unlogged fix is a future
  regression nobody can trace.
- **Bundling fixes.** One fix per item. A bundle hides which change fixed which problem.

## Output — the feedback log

One entry per item. Fields: DATE, SOURCE, VERBATIM (short), CLASS, ROOT CAUSE, ACTION,
STATUS, VERIFIED. Keep the log in one file at a path you choose (for example
`feedback-log.md` in your product folder). A blank template and one filled example entry
are in `examples/feedback-log-template.md`.

Example entry (illustrative — written for this skill, not a real customer's words):

```
DATE: 2026-11-16 | SOURCE: email
VERBATIM: "I can't find the templates — where are they?"
CLASS: CONFUSION | ROOT CAUSE: onboarding — contents page does not point to page 6
ACTION: ONBOARDING FIX | STATUS: done
VERIFIED: yes — opened the updated file, followed the contents page, reached the templates in 2 clicks
```

## Escalation — stop and get a human decision

Do not attempt to resolve these three categories on your own. Escalate to the product
owner (or, for legal matters, to qualified advice):

- **Refund disputes** — anything beyond a straightforward fix-first refund under your
  stated terms.
- **Legal or compliance concerns** — advertising claims, tax, intellectual-property
  disputes, or anything that could be a regulatory issue.
- **Feedback suggesting the product is fundamentally misrepresented** — the listing
  promises something the product cannot do at all.

## Verification

- The fix is confirmed by re-testing the exact customer scenario end to end.
- Listing-copy fixes are confirmed by re-reading the whole listing against the product.
- Unresolved items stay OPEN in the log — never mark resolved on intent.

## Known limits

- This loop classifies and routes feedback; it does not decide your product strategy.
  A FEATURE REQUEST that ten customers make is still a strategy decision, not an
  automatic build.
- The nine labels cover the common cases. If an item genuinely fits two labels, pick
  the one that determines the fix, and note the second label in the log entry.
- The SLA targets and the fix-first refund shape are recommended starting points.
  Adapt them to your product and state the final versions on your listing.
