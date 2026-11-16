# AI Agents & Workflow Automation

Build small, repeatable AI agents and automations a beginner can actually follow — with exact steps, exact prompts, honestly priced free tiers, and honest limits.

## Install

Manual copy: copy this folder into `.claude/skills/` in your project, or into `~/.claude/skills/` to use it in every project. The folder name must stay `ai-agents-automation` so the skill name matches the directory.

## Who it is for

Creators, freelancers, and small teams automating repetitive work on a $0 starting budget. No coding assumed.

## What it covers

- Choosing between n8n and Zapier for the job at hand
- A verified starting stack with prices last checked 16 November 2026 (n8n Cloud, Zapier Free, ChatGPT Free, Claude Free)
- Build anatomy: the seven parts every agent build documents
- The 8-part agent prompt block, filled in with an example
- n8n self-host setup (Docker and npm) with a first-workflow walkthrough
- Two worked builds: a daily research agent (n8n) and an inbox triage agent (Zapier)
- Error handling and cost guards, a security checklist, and troubleshooting

## Usage

Invoke this skill when automating a repetitive task, building a research or inbox-triage agent, or choosing between n8n, Zapier, and other automation tools.

Quickstart:

1. Pick your tool from the comparison table.
2. Follow the build anatomy for your agent.
3. Run the security checklist before anything goes live.
4. Label the build **tested** (you ran it end-to-end) or **build guide** (steps to follow, not yet run). Never present a build guide as a working run.

## Example

A complete worked build is in `examples/research-agent-build.md`: a daily research brief agent with the node-by-node setup, the filled 8-part prompt, an illustrative sample output, and a cost check.

## Honesty note

The two worked builds in this skill are build guides, not run reports — they have not been run end-to-end by the author. Prices and free-tier limits were last checked 16 November 2026 and change without notice; re-check the official pricing page on the day you publish. AI models hallucinate: every agent output that states a fact needs a source check before it is shared.

## Repo layout

```text
ai-agents-automation/
  SKILL.md            The skill: tool choice, build anatomy, prompt block, setup, builds, guards
  README.md           This file
  LICENSE             MIT licence
  examples/
    research-agent-build.md
```

## License

MIT. See `LICENSE`. Copyright 2026 Muhammad Saad Ranjha.

## Disclaimer

This skill is independent and unaffiliated with n8n, Zapier, OpenAI, or Anthropic. Prices and limits are stated as last checked on 16 November 2026 with links to the official pricing pages; verify them before relying on them.
