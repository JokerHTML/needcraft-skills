# AI Tool Research & Verification

Verify every AI tool claim from a primary source before it enters your copy, and keep a claim ledger so any price, free-tier limit, or feature traces to a URL, a date, and a confidence level.

## Install

Manual copy: copy this folder into `.claude/skills/` in your project, or into `~/.claude/skills/` to use it in every project. The folder name must stay `ai-tool-research` so the skill name matches the directory.

## Who it is for

Anyone writing Top 5 lists, tutorials, news, or comparisons about AI tools — a creator, a small team, or an agent drafting on their behalf.

## What it covers

- The six-step verification process and the HIGH / MEDIUM / UNVERIFIED confidence definitions
- A rule for deciding between conflicting sources (the page that charges the money wins; discrepancies named, never hidden)
- A claim ledger with three filled, verified example rows (n8n, Zapier, Perplexity — checked 16 November 2026)
- A worked example for handling unverified areas without inventing a figure
- A pre-draft verification checklist and a re-check cadence

## Usage

Invoke this skill before drafting any Top 5, tutorial, news, or comparison post, and whenever a price, limit, or feature is about to be written.

Quickstart:

1. Name each claim precisely.
2. Open the official page, record what it showed, assign confidence.
3. Write the supported wording — the exact sentence the source supports, nothing more.
4. Build the ledger: one row per claim in the copy.
5. Re-verify on posting day.

## Example

A filled claim ledger is in `examples/filled-claim-ledger.md`: three real, verified rows (two HIGH, one MEDIUM with the reason stated) plus an UNVERIFIED row showing how a gap is handled honestly.

## Repo layout

```text
ai-tool-research/
  SKILL.md            The skill: process, confidence levels, conflicting-source rule, ledger, checklist
  README.md           This file
  LICENSE             MIT licence
  examples/
    filled-claim-ledger.md
```

## License

MIT. See `LICENSE`. Copyright 2026 Muhammad Saad Ranjha.

## Disclaimer

This skill is independent and unaffiliated with n8n, Zapier, Perplexity, or any tool named in it. Example ledger figures were last checked 16 November 2026; re-check the official pricing page before quoting them.
