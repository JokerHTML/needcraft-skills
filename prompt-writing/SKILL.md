---
name: prompt-writing
description: >-
  Write copy-ready AI tutorial prompts in a fixed 8-part block — role,
  context, task, inputs, constraints, output structure, quality checks,
  placeholders, tool, steps, expected output, iteration prompt, and
  limitations — so a reader can run the workflow without guessing. Use when
  writing any tutorial post that teaches an AI task or promises "do X with
  AI", and whenever a post's hook makes a promise the prompt block must
  prove.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# AI Tutorial & Copy-Ready Prompt Writing

## What this skill is

A method for writing tutorial posts that teach an exact prompt — role,
context, task, inputs, constraints, output structure, quality checks —
so a reader can run the workflow without guessing. "Ask ChatGPT to do
this" is incomplete and never ships.

Who it is for: anyone writing AI tutorials, prompt posts, or workflow
explainers for social media, a blog, or a newsletter.

## When to use

- Any post that teaches an AI task, workflow, model, or use case.
- Any post whose hook promises "do X with AI" — the prompt block is the
  proof of the promise.

## Rules (hard)

- **Every tutorial carries the full 8-part prompt block** (below).
  Missing any part = fail the quality gate.
- **Never promise a prompt produces perfect, accurate, or guaranteed
  results.** Always include a verification step for research, factual,
  and high-impact tasks.
- **Placeholders must be explained AND filled once.** A prompt with
  unexplained `[brackets]` is incomplete.
- **Expected output is labelled as an example if not actually
  generated.** Never present an invented output as a real result.
- **Limitations are visible, not buried:** where the output may fail,
  hallucinate, need human review, or expose sensitive data.
- **Protect user data:** never tell readers to paste passwords, private
  client info, personal records, or confidential business data into a
  tool without checking its data controls first.
- **One CTA per post.** The prompt itself is the save-worthy asset; the
  CTA asks for one action only.

## The 8-part prompt block (non-negotiable)

1. **PROMPT TITLE** — name the result the reader will create.
2. **COPY-READY PROMPT** — the full prompt in a readable code/card
   block. Must contain: role · context · task · inputs · constraints ·
   output structure · quality checks.
3. **PLACEHOLDERS** — every `[insert your details]` field explained,
   plus one filled example.
4. **RECOMMENDED TOOL/MODEL** — tool and model/mode if it materially
   affects the result; re-check availability on the day you publish
   (model names, rollout state, and free-tier access change often —
   verify on the tool's official site or in the app before naming one).
5. **HOW TO USE** — numbered steps, including what files, URLs,
   screenshots, or context the user must provide.
6. **EXPECTED OUTPUT** — realistic example or excerpt, labelled as an
   example if not actually generated.
7. **ITERATION PROMPT** — a follow-up prompt to improve, verify, or
   refine the first result.
8. **LIMITATIONS** — where the output may fail, hallucinate, require
   human review, or expose sensitive data.

## Prompt-writing craft

- **Role first, task second, output format last.** The model needs to
  know who it is, what to do, and what "done" looks like — in that
  order.
- **Constraints beat adjectives.** "Under 120 words, 5 bullets, no
  jargon" beats "make it good".
- **Output structure is a contract:** headings, bullet counts, table
  columns, word limits — specified, not hoped for.
- **Quality checks inside the prompt:** "Flag any claim you cannot
  support from the sources I gave you" — build verification into the
  prompt, not just the post.
- **One prompt, one job.** If the workflow needs two jobs (research,
  then draft), write two prompts and number them.
- **Test the prompt once before publishing if possible;** if not tested,
  say so ("prompt drafted, not yet run — try it and tell us what it
  returned").

## Iteration prompts (keep a bank)

- Verify: "Check every factual claim in your answer against the sources
  I provided. List any claim you cannot support, and remove it."
- Tighten: "Cut this to half the length. Keep every number and every
  named tool. Remove filler."
- Reframe: "Rewrite this for [audience], at [reading level], keeping
  the same facts."
- Compare: "Give me 2 alternative versions: one shorter, one more
  detailed. Tell me which you recommend and why."

## Visual treatment

- Prompt shown as a readable code-style block or clean prompt card.
  Minimum readable size on mobile; no tiny text.
- On carousels, the prompt gets its own slide(s) — never shrunk to fit
  beside other content.
- On video, the prompt appears on screen long enough to read or
  screenshot, and is repeated in the caption/description.

## Template

Use `references/template.md` for every tutorial build. It is the blank
8-part scaffold with a fill-in checklist.

## Worked example — full 8-part prompt, end to end

Topic: write a short product description for a handmade candle for a new scent launch.

### 1. PROMPT TITLE

Product description for a handmade candle (new scent launch)

### 2. COPY-READY PROMPT

```text
You are a copywriter writing for a small candle maker. You are
launching a new scent, [scent name], and need one short product
description for the shop page. The candle is [product] with
[scent notes] and a [burn time] burn time. It costs [price].
Your reader is [audience]. The brand voice is [brand voice].

Write the description with this structure:
- Headline: under 8 words, names the scent, no "luxury", no "indulge".
- Opening: one sentence about what the room smells like when the
  candle is lit — not a generic greeting.
- Body: 2–3 short sentences. Name the one thing this candle does
  differently. Add one concrete detail (the wax, the wick, or how
  it was tested).
- Close: one clear, low-effort next step (a buy button cue or the
  burn time). No "let me know what you think".

Constraints: under 120 words total. Plain, direct language. No
exclamation marks. No "I hope you're doing well". No discount or
price cut offered.

Quality checks before you finish: read the description back and flag
any sentence that could apply to any candle — rewrite it to be
specific to this one. Confirm the description asks for exactly one
action.
```

### 3. PLACEHOLDERS — explained, plus one filled example

| Placeholder | What to put there | Filled example |
|---|---|---|
| `[scent name]` | The new scent | Cedar & Amber |
| `[product]` | The candle itself | handmade soy candle, 200 g |
| `[scent notes]` | What it smells like | cedar, amber, a little smoke |
| `[burn time]` | How long it burns | 45 hours |
| `[price]` | The shop price | $24 |
| `[audience]` | Who buys it | people buying a first candle for their home |
| `[brand voice]` | How the brand sounds | warm, plain, no hype |
| `[launch date]` | When it goes on sale | 12 December 2026 |

### 4. RECOMMENDED TOOL/MODEL

Any general-purpose chat AI with a free tier (ChatGPT, Claude, Gemini).
No model-specific feature is needed. Re-check the tool's official site
on the day you publish: model names and free-tier limits change.

### 5. HOW TO USE

1. Fill in every placeholder from the table above, using the maker's
   actual words where you have them.
2. Paste the full prompt into your chat AI of choice.
3. Read the draft against the quality checks in the prompt itself.
4. Publish the description on your shop page — do not paste the
   maker's private supplier details into a shared or public tool.

### 6. EXPECTED OUTPUT

Example (labelled as an example — written for illustration, not a
generated result):

> **Cedar & Amber — 200 g soy candle, 45-hour burn**
>
> Light it and the room smells like a cabin after rain — cedar
> first, then a low amber warmth. The wax is soy, the wick is
> cotton, and every batch is test-burned for a clean, even melt.
>
> Burns for 45 hours. $24.

### 7. ITERATION PROMPT

```text
Rewrite this description in two versions: one shorter (under 80
words) and one warmer in tone, keeping the same facts, the same
single next step, and no discount. Tell me which version you
recommend for a shop page, and why.
```

### 8. LIMITATIONS

- The model cannot know how the scent reads in a customer's home —
  the description sells the first sniff, it does not guarantee it.
- The "new detail" must be real: do not let the model invent a test
  result or a material claim. Check any detail it adds before
  publishing.
- Do not paste the maker's private supplier details or pricing
  history into the tool without checking its data controls first.
- Tone varies by model; read the draft aloud before publishing.

## Quality gate (before publishing any tutorial)

- [ ] All 8 parts present?
- [ ] Every placeholder explained AND filled once?
- [ ] Expected output labelled as example if not actually generated?
- [ ] Verification step present for any factual claim?
- [ ] Limitations visible, including data-privacy warning?
- [ ] Tool/model availability re-checked on the day of publishing?
- [ ] Prompt tested once, or marked "drafted, not yet run"?
- [ ] One CTA only?

## Troubleshooting

| Problem | Fix |
|---|---|
| The prompt returns generic text | Add constraints (word limit, structure, banned phrases) and a quality check that flags generic sentences. |
| Readers ask "what do I put in the brackets?" | A placeholder was explained but not filled — fill one example for every bracket. |
| The model invents facts in the output | Add "use only the sources I gave you; flag anything you cannot support" and a verification step in the post. |
| The named model no longer exists or is paywalled | Re-check the official site; name the current model or drop the model name and name the tool only. |
| The prompt is too long for one slide/frame | Split it across slides or put the full text in the caption/description and the title on screen. |

## Known limits

- A prompt is a starting point, not a guarantee. Model behaviour
  changes between versions; a prompt that worked in testing can drift.
  Say so in the post when a prompt is untested.
- This skill teaches prompt structure. It does not cover prompt
  injection, jailbreaks, or system-prompt design.
