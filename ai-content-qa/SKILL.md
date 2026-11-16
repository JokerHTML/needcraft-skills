---
name: ai-content-qa
description: >-
  Run a fail-closed quality gate on AI-written social posts before they ship: score nine gates out of 100, catch eight automatic critical failures, and check rights, safety, disclosure, and platform-native structure with a printable checklist. Use when doing the final check on any AI-assisted post, or whenever a claim, link, price, prompt, or visual changes after the first draft.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Content QA & Rights/Safety

## What this skill is

A final quality gate for AI-assisted social posts. It fails closed: no post ships unless it passes the quality bar **and** every critical gate. Revise, re-check, or reject — never lower the bar to meet a calendar.

Who it is for: anyone publishing AI-assisted content who wants a repeatable check before a post goes live — a creator, a small team, or an agent drafting on their behalf.

## How to use this skill

1. Finish the draft first. QA runs on a complete post (copy + visual + links), never on an outline.
2. Score the nine gates, then check the eight critical failures. Any critical failure = revise or reject, whatever the score.
3. Run the pre-delivery checklist (also saved as `examples/quality-gate-checklist.md` — print it or copy it into your plan).
4. Record the score with per-gate points and the date. A post with no recorded score has not passed.
5. Re-run the gate whenever a claim, link, price, prompt, or visual changes after the first pass.

## The quality bar — read this first

**The bar is 92/100 AND every critical gate passed.** A post scoring below 92, or failing any critical gate, is revised until it passes or marked REJECTED with the reason. It is never shipped as passing.

**Honest note about the number:** 92/100 is a house threshold chosen by the author as a deliberately strict bar. It is not a proven predictor of reach, engagement, or sales, and no study is cited for it. Treat it as a discipline device — a post that clears 92 with zero critical failures has survived a hard check — not as a guarantee of performance.

## Rules (hard)

- **Independent verification:** the checker re-opens sources and links itself. It does not trust the drafter's notes.
- **One FAIL on the builder checklist or the visual checklist = revise, never ship.** Those checklists stay in force alongside this gate (summarised below).
- **Never represent a draft as tested, a recommendation as installed, or a scheduled post as published.** Label hands-on vs desk-researched honestly, on the post itself where the claim appears.
- **UNVERIFIED = do not publish the figure.** A claim with no source behind it does not appear as a stated fact; it is cut or labelled unverified.
- **No post ships with an unknown score.** "Probably fine" is a fail.

## Scored gates (100 points total)

| Gate | Points | What it scores |
|---|---|---|
| Accuracy / evidence | 20 | Every claim traces to a source; no unverified figure stated as fact |
| Practical usefulness | 15 | The reader can do something concrete after reading; not just inspiration |
| Prompt / workflow completeness | 15 | The full prompt or steps are present wherever a workflow is taught |
| Tool research / links | 10 | Every tool link opens to the official destination; prices and free tiers verified |
| Hook / storytelling | 10 | The opening earns attention and sets up the payoff (see the 4 S's below) |
| Originality | 10 | Own angle, own examples, own wording — not a rewrite of one source |
| Visual / audio | 10 | Visual supports the claim, text readable on mobile, no production defects |
| Platform-native structure | 5 | Written for this platform's format, not copy-pasted across platforms |
| SEO / accessibility | 5 | Search phrase placed, alt text / captions present |

Score each gate, total them, and record per-gate points. Deduct for: unverified wording, thin usefulness, an incomplete prompt block, untested claims presented as tested, a weak hook, derivative structure, visual defects, identical copy across platforms, missing SEO output or alt text.

## Automatic critical failures (any one = REVISE or REJECT, regardless of score)

1. Unverified factual claim, fabricated tool feature, fake ranking, fake test, or misleading "best" claim.
2. Broken, unsafe, unofficial, or wrong-destination tool link; unverified price or free-tier promise.
3. Missing exact prompt/steps when the content promises to teach a workflow.
4. Copied creator work, reused clips without meaningful original contribution, or unclear rights.
5. Misleading income, viral, or monetisation guarantee, or an inaccurate platform-policy claim.
6. Missing required AI disclosure or other platform disclosure where applicable.
7. Unreadable mobile text, deceptive thumbnail, fake product UI, or major production defect.
8. Identical mass-produced copy across platforms with no native adaptation.

## The 4 S's — the hook test

A hook passes when it satisfies all four. Define them the same way every time:

- **Subject:** the reader knows in the first line what this post is about. No mystery opener that hides the topic.
- **Stakes:** the reader knows why it matters to them — a problem, a cost, an opportunity — in concrete terms, not "this is important".
- **Speed:** the point lands fast. The first line carries the subject and the stakes; the reader does not have to read three lines to learn what the post offers.
- **Clarity:** the hook is unambiguous. One reading, one meaning. No clever wording that could be read two ways.

If any S fails, rewrite the hook. Do not patch it with a second line that explains the first.

## Builder checklist (summarised — the draft-quality gate)

The draft must pass all of these before it reaches the scored gates:

- **Claim ledger present:** every claim has a source URL, a date, and a confidence level; no UNVERIFIED figure is stated as fact.
- **Specificity floor:** at least 1 number + 1 named entity + 1 concrete detail per 100 words.
- **One CTA per platform version;** no triple-ask closer ("like, follow, comment, share, buy").
- **No AI-tell phrases** (stock openers, "delve", "in today's fast-paced world", "unlock the power of") and no emoji walls.
- **Em-dash discipline:** at most 1 em-dash per 100 words.
- **Native structure:** X ships as a native thread (first post no link, ends with a thread marker; link in the reply); Threads carries the link in the first reply only, plus a native topic tag.
- **Hashtags:** Instagram up to 5, LinkedIn 0–1, other platforms 1–3 where they genuinely help.
- **Hands-on vs desk-researched label present and true.**
- **"Last checked" date present** on every price, limit, or feature claim.

## Visual checklist (summarised — the visual gate)

- **Full text scan:** read every word on the visual against the brief, one by one. Any typo, wrong word, duplicated word, or cut-off text = regenerate before the post goes out.
- **Mobile readability:** all text legible at phone size; no tiny text, no text touching an edge.
- **No deception:** no fake product UI, no fake screenshot, no misleading before/after.
- **Card and image agree:** the image shows what the text says; it does not contradict it.
- **Alt text written** for every meaningful image; captions/subtitles for video.
- **AI disclosure checked** where the platform requires it.

## Character limits (last checked 16 November 2026)

Verify these in the platform's own composer or docs before publishing — platforms change them.

| Platform | Field | Limit |
|---|---|---|
| X | Post (standard account) | 280 characters, weighted (emoji and many non-Latin characters count as 2; every link counts as 23). X Premium allows up to 25,000 |
| Threads | Post | 500 characters |
| Instagram | Caption | 2,200 characters |
| Pinterest | Pin title | 100 characters |
| Pinterest | Pin description | 800 characters |
| LinkedIn | Post | 3,000 characters |
| Facebook | Post | Facebook publishes no post character limit — check the composer; do not quote a number |

Sources: X developer docs (counting characters), Threads API docs, Meta Instagram developer docs, Pinterest Help (pin specs), LinkedIn Help. Facebook's lack of a published limit is the finding — the widely quoted 63,206 figure comes from a 2011 announcement Meta has not repeated.

## Pre-delivery checklist (run in order)

- [ ] Claim ledger present; every claim has source URL + date + confidence; no UNVERIFIED figure stated as fact.
- [ ] Every tool link opened (or re-checked) and lands on the official destination.
- [ ] Prompt block complete (8 parts: title, copy-ready prompt, placeholders, tool/model, how to use, expected output, iteration prompt, limitations) wherever a workflow is taught.
- [ ] Hands-on vs desk-researched label present and true.
- [ ] "Last checked" date present.
- [ ] Hook passes the 4 S's (Subject / Stakes / Speed / Clarity); hook placed in the first line.
- [ ] One CTA per platform version; no triple-ask closer.
- [ ] Specificity floor: ≥1 number + ≥1 named entity + ≥1 concrete detail per 100 words.
- [ ] No AI-tell phrases; em-dash ≤1 per 100 words; no emoji walls.
- [ ] Character limits respected (table above); X native thread; Threads link in first reply only + native topic tag.
- [ ] Hashtags: IG ≤5, LinkedIn 0–1, others 1–3 where they help.
- [ ] Visual checklist passed; full text scan done; alt text / captions present.
- [ ] AI disclosure checked; no income/viral guarantee; no fake ranking or "best" claim.
- [ ] 92/100 score recorded with per-gate points and the date.

A printable copy of this checklist is in `examples/quality-gate-checklist.md`.

## Rights / safety checks

- Copyright, commercial-use terms, voice/likeness rights, stock licences, and AI asset restrictions checked before recommending production or monetisation workflows.
- No passwords, private client info, or confidential data in prompts, visuals, or docs.
- Sources: primary first (official product site, docs, pricing page, platform policy page); independent sources for comparison and context, never as the sole basis for a price or limit claim.
- If a fact changes after publishing, update where possible and add a correction note.

## Worked scored example (labelled example)

The post below is invented for this example only. It was not published and its claims are illustrative. It is scored gate-by-gate to show how the rubric is applied.

**Example post (Instagram caption, 148 words):**

> "I tested 3 free automation tools for one week. n8n's self-hosted Community Edition ran my daily digest 7 days in a row with zero failures. Zapier Free handled the same job in a two-step Zap, but I hit its 100-task monthly limit on day 5 because my feed polled every 15 minutes. Make's free plan covered the job with tasks to spare. Full comparison with the exact workflow in the carousel. Last checked 16 Nov 2026. Save this if you automate anything."

**Scores:**

| Gate | Points | Reason |
|---|---|---|
| Accuracy / evidence | 14/20 | Tool names and limits match official pages, but "7 days in a row with zero failures" is a test claim with no run log shown — deduct 6 |
| Practical usefulness | 12/15 | Concrete comparison and a carousel with the workflow; the reader can act on it |
| Prompt / workflow completeness | 10/15 | Workflow is in the carousel, but the post itself gives no prompt or steps — deduct 5 |
| Tool research / links | 8/10 | Limits match official pricing pages; no links in the caption itself — deduct 2 |
| Hook / storytelling | 8/10 | Subject and stakes land in line 1 ("I tested 3 free automation tools"); speed is good; clarity is good |
| Originality | 7/10 | Own test framing, but the three-tool comparison is a common format |
| Visual / audio | 8/10 | Carousel assumed readable; no visual defects noted in the example |
| Platform-native structure | 4/5 | Written as an Instagram caption with a save CTA; hashtags missing — deduct 1 |
| SEO / accessibility | 3/5 | Search phrase ("free automation tools") in line 1; alt text not mentioned — deduct 2 |
| **Total** | **74/100** | **FAIL — below 92** |

**Critical failures:** none of the eight trigger. But the score fails, so the verdict is REVISE: add the run log (or label the test claim as illustrative), put the prompt or steps in the carousel, add links and alt text, then re-score. A 74 that ships is a gate failure, not a judgement call.

## Troubleshooting

| Symptom | What it means | Fix |
|---|---|---|
| Score is 88–91 and you are tempted to ship | The bar is doing its job | Revise the weakest gate; never lower the bar to meet a calendar |
| A critical failure appears after the first pass | Something changed after drafting | Re-run the full gate; a changed claim, link, price, prompt, or visual always triggers a re-check |
| Two checkers score the same post 10+ points apart | A gate is being read differently | Score the disputed gate against its "what it scores" line only, with evidence quoted |
| The hook passes 3 of the 4 S's | The hook is not done | Rewrite it; a second explanatory line does not cure a failed S |
| The visual passes but the caption contradicts it | Card-and-image check failed | Change the image or rewrite the caption — never ship a contradiction |

## Known limits

- The 92/100 bar is a house threshold, not a proven predictor of performance. It measures how hard the post was checked, not how well it will perform.
- This skill checks a post's claims, structure, rights, and safety. It does not check whether the underlying advice is good business judgement — that needs a human who knows the audience.
- Character limits and platform rules change. The table above was last checked 16 November 2026; verify before publishing.
- The scored example is illustrative. Real scores need a real post, real sources, and a real visual.
