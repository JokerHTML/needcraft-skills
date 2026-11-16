# YouTube Channel Operator

Run a YouTube channel end to end as a disciplined 10-stage pipeline: research, strategy, script, thumbnail, SEO, production, review, publish, learn, engage.

## What it is

The operating manual for one channel: every script carries an evidence desk for its factual claims, every upload passes hard review gates (human approval, AI disclosure, rights confirmed), every experiment needs approval at start and at adopt, and every lesson comes from your own channel's history — baselines from your own data, minimum evidence before any recommendation, nothing auto-applies.

## Who it is for

Creators and small teams running one YouTube channel (Shorts, long-form, or both) who want every video to pass the same checks.

## How to use

1. Write your one-sentence audience definition and build your source catalog (`SKILL.md` has the template).
2. Follow the 10-stage pipeline for each video. Do not skip Stage 7 (review) or Stage 8 (the 8-field read-back).
3. Run the weekly review from Stage 9 and keep recommendations pending until a human approves them.
4. Read `video-script-retention` before Stage 3 and `trend-intelligence` before Stage 1.

## Example

`examples/sample-seo-package.md` — a complete sample script record with claims, a full SEO package, and a worked score (title 26/30, description 34/40, tags 26/30, total 86/100).

## Install

This is a skill (a `SKILL.md` playbook), not software. Copy the `youtube-operator/` folder into your agent's skills directory and invoke it for channel work, or follow it manually as an operating manual. API use needs your own Google Cloud project with the YouTube Data API v3 and YouTube Analytics API enabled; keep credentials private.

## License

MIT — see `LICENSE` in the repository root, or treat this file set as MIT-licensed.

## Disclaimer

The performance formulas, quality bands, and alert thresholds are a starting system from one pipeline's mechanics, not YouTube-published truth. Validate them against your own channel's data. Publish windows are yours to test — this skill prescribes no "best time to post".
