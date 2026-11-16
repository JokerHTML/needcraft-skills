# Content QA & Rights/Safety

A fail-closed quality gate for AI-assisted social posts: score nine gates out of 100, catch eight automatic critical failures, and check rights, safety, disclosure, and platform-native structure before anything ships.

## Install

Manual copy: copy this folder into `.claude/skills/` in your project, or into `~/.claude/skills/` to use it in every project. The folder name must stay `ai-content-qa` so the skill name matches the directory.

## Who it is for

Anyone publishing AI-assisted content who wants a repeatable final check — a creator, a small team, or an agent drafting on their behalf.

## What it covers

- The 92/100 bar and what it honestly is (a strict house threshold, not a proven predictor of performance)
- Nine scored gates (100 points) and eight automatic critical failures
- The 4 S's hook test — Subject, Stakes, Speed, Clarity — defined, not assumed
- Summarised builder and visual checklists
- Verified character limits (last checked 16 November 2026), including the honest finding that Facebook publishes no post limit
- A printable pre-delivery checklist and a worked scored example

## Usage

Invoke this skill for the final check on any AI-assisted post, or whenever a claim, link, price, prompt, or visual changes after the first draft.

Quickstart:

1. Finish the draft (copy + visual + links).
2. Score the nine gates, then check the eight critical failures.
3. Run the pre-delivery checklist in `examples/quality-gate-checklist.md`.
4. Record the score with per-gate points and the date. No recorded score = not passed.

## Example

A worked scored example is in `SKILL.md`: an invented Instagram caption scored gate-by-gate at 74/100 — a FAIL, with the exact revisions that would be needed. The example is labelled as invented; it was not published and its claims are illustrative.

## Repo layout

```text
ai-content-qa/
  SKILL.md            The skill: gates, critical failures, checklists, limits, worked example
  README.md           This file
  LICENSE             MIT licence
  examples/
    quality-gate-checklist.md
```

## License

MIT. See `LICENSE`. Copyright 2026 Muhammad Saad Ranjha.

## Disclaimer

This skill is independent and unaffiliated with any platform named in it. Character limits were last checked 16 November 2026; verify them in the platform's own composer or docs before publishing.
