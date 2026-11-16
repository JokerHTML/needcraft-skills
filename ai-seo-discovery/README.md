# SEO & Search Discovery

Find the exact words your audience already searches for and match each post to one searchable phrase plus its intent — with platform-native titles, captions, hashtags, and alt text, and without invented keyword volumes or guaranteed-ranking claims.

## Install

Manual copy: copy this folder into `.claude/skills/` in your project, or into `~/.claude/skills/` to use it in every project. The folder name must stay `ai-seo-discovery` so the skill name matches the directory.

## Who it is for

Creators and small teams publishing tutorials, comparisons, and how-to content who want their posts found by search, not just by the feed.

## What it covers

- The nine learning modules: keyword intent, platform-native search, YouTube, Instagram/Facebook, Pinterest, X/Threads, web/Google SEO, AI-search literacy, post-publish optimisation
- A seven-step process from audience problem to verified link
- A tie-break rule for conflicting phrase variants (intent → native evidence → specificity → shorter)
- A re-check cadence (publishing day, monthly, when a rule stops working)
- Verified character limits (last checked 16 November 2026) and the honest split between verified placement figures and house practice
- A complete worked example of a per-post SEO output block

## Usage

Invoke this skill before drafting any post, when choosing a tutorial angle or Top 5 topic, and when reviewing a post after it publishes.

Quickstart:

1. Write the question a beginner would type, in their own words.
2. Generate variants, check them natively, pick one primary phrase.
3. Write the per-post SEO output block and paste it into the plan before drafting.
4. Review at 24h / 72h / 7d and record what actually happened.

## Example

A complete worked example is in `examples/per-post-seo-output.md`: the full SEO block for an example carousel about growing tomatoes on a balcony, including the tie-break note and the review plan. The example is labelled as invented; it was not published and no volumes are claimed.

## Repo layout

```text
ai-seo-discovery/
  SKILL.md            The skill: modules, process, tie-break rule, worked example, references
  README.md           This file
  LICENSE             MIT licence
  examples/
    per-post-seo-output.md
```

## License

MIT. See `LICENSE`. Copyright 2026 Muhammad Saad Ranjha.

## Disclaimer

This skill is independent and unaffiliated with Google, Meta, Pinterest, or any platform named in it. It measures no keyword volume and promises no ranking. Character limits were last checked 16 November 2026; verify them before publishing.
