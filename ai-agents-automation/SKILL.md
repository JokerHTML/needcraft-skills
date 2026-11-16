---
name: ai-agents-automation
description: >-
  Build repeatable AI agents and no-code automations with n8n and Zapier: pick the right tool, write the full agent prompt, set up self-hosted n8n, and ship a tested workflow with error handling, cost guards, and a security checklist. Use when automating a repetitive task, building a research or inbox-triage agent, or choosing between n8n, Zapier, and other automation tools.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# AI Agents & Workflow Automation

## What this skill is

A method for building small, repeatable AI agents and automations a beginner can actually follow — with exact steps, exact prompts, honestly priced free tiers, and honest limits. It covers two tools in depth (n8n and Zapier), two agent archetypes with worked builds, and the guards that keep a workflow from silently spending money or leaking data.

Who it is for: a creator, freelancer, or small team automating repetitive work on a $0 starting budget. It assumes no coding. Where code appears, it is a copy-paste command or a short settings value, explained in place.

## How to use this skill

1. Start with **Choosing a tool** and pick n8n or Zapier for the job at hand.
2. Follow **Build anatomy** for every agent: problem, tool map, build steps, prompt, test run, limits, no-code alternative.
3. If you self-host n8n, follow **n8n self-host setup** exactly, then run the **Research agent** build.
4. Before any build goes live, run the **Security checklist** and the **Error handling + cost guards** section.
5. Label every build honestly: **tested** (you ran it end-to-end and recorded the result) or **build guide** (steps to follow — not yet run end-to-end). Never present a build guide as a working run.

## Rules (hard)

- **Free-first, honestly priced.** n8n Community Edition is free *software* that you self-host — the server and the upkeep cost real money and time; say so. Zapier Free is $0/month with real limits. Never present a paid-only path as free.
- **Every build carries the full prompt block** (see "The 8-part agent prompt" below) for the agent's AI step. A build without its prompt is incomplete.
- **Never tell readers to paste passwords, private client info, or confidential data into a tool without checking its data controls first.**
- **No fabricated run.** A workflow shown as "working" must have been run, or be labelled as a build guide.
- **One call to action per post or tutorial.** The workflow is the value; the CTA asks for one action only.
- **Re-check prices and limits on the day you publish.** Free tiers change without notice. Every price in this skill carries a "last checked" date.

## Choosing a tool

Pick by the job, not by hype.

| Need | Pick | Why |
|---|---|---|
| Free, unlimited runs, you can run a small server | n8n Community Edition (self-hosted) | No per-run fee; you pay only for the server |
| Free, zero setup, simple two-app automation | Zapier Free | Works in minutes; no server to maintain |
| Multi-step logic, branches, AI steps, webhooks | n8n Cloud or Zapier Professional | Free tiers cap steps and runs (see below) |
| A workflow that must run while you sleep, unattended | Either, on a paid plan or a self-hosted server | Free Zapier polls every 15 minutes; a laptop that sleeps stops a local n8n |

**n8n bills per execution** — one execution is one full run of a workflow, however many steps it has. **Zapier bills per task** — one task is one successful action step; triggers do not count as tasks.

## Verified starting stack (last checked 16 November 2026)

Re-check every figure on the official pricing page before quoting it. Prices change; the links below are the source of truth.

- **n8n Community Edition** — free, self-hosted, unlimited executions. You pay for your own server. Source: https://n8n.io/pricing (Community Edition section) and https://docs.n8n.io
- **n8n Cloud Starter** — €20/month billed annually, 2,500 executions/month. Pro — €50/month billed annually, 10,000 executions/month. Prices are listed in euros; the page shows your local currency equivalent. Source: https://n8n.io/pricing (read directly 16 Nov 2026)
- **Zapier Free** — $0/month, 100 tasks/month, two-step Zaps (one trigger, one action), unlimited Zaps, 15-minute polling. Professional from $19.99/month billed annually (750 tasks). New accounts start with a 14-day Professional trial. Source: https://zapier.com/pricing (read directly 16 Nov 2026)
- **ChatGPT Free** — $0. OpenAI's pricing page lists "unlimited text chats" for the free plan, subject to abuse guardrails. Uploads, image creation, voice, and deep research are limited on Free. Plus is $20/month. Source: https://chatgpt.com/pricing
- **Claude Free** — $0. Limited usage that resets every 5 hours and weekly; Anthropic publishes no fixed message count. Pro is $20/month, or $17/month billed annually ($200 up front), and gives at least 5x Free's usage per 5-hour session. Source: https://claude.com/pricing

What "unlimited" never means: no free plan is unlimited in every dimension. Say which dimension is unlimited (text chats, executions, Zaps) and which is capped (uploads, images, tasks, executions per month).

## Build anatomy (every agent build)

Every agent build documents these seven parts, in order:

1. **Problem + trigger** — what starts the workflow, and what problem it solves. One sentence each.
2. **Tool map** — the nodes/steps as a simple diagram or list (trigger → step → step → output). Draw it yourself; never use a fake screenshot.
3. **Step-by-step build** — numbered, with exact settings: trigger type, model, prompt, output destination.
4. **The agent prompt** — the full 8-part block (below).
5. **Test run** — what input you gave, what output came back, labelled **tested** (with date) or **example** (illustrative, not run).
6. **Limits + failure modes** — rate limits, task caps, self-hosting upkeep, hallucination risk.
7. **No-code alternative** — the Zapier path where the lead build is n8n, and vice versa.

## The 8-part agent prompt

Every agent's AI step carries all eight parts. Missing any part = the build is incomplete.

1. **PROMPT TITLE** — name the result the reader will create.
2. **COPY-READY PROMPT** — the full prompt in a readable code block. It must contain: role, context, task, inputs, constraints, output structure, quality checks.
3. **PLACEHOLDERS** — every `[insert your details]` field explained, plus one filled example.
4. **RECOMMENDED TOOL/MODEL** — tool and model/mode, but only where it materially affects the result; verify the model is actually available on the reader's plan.
5. **HOW TO USE** — numbered steps, including what files, URLs, screenshots, or context the user must provide.
6. **EXPECTED OUTPUT** — a realistic example or excerpt, labelled as an example if not actually generated.
7. **ITERATION PROMPT** — a follow-up prompt to improve, verify, or refine the first result.
8. **LIMITATIONS** — where the output may fail, hallucinate, require human review, or expose sensitive data.

Craft rules: role first, task second, output format last. Constraints beat adjectives ("under 120 words, 5 bullets, no jargon" beats "make it good"). Output structure is a contract: headings, bullet counts, table columns, word limits — specified, not hoped for. Build verification into the prompt itself ("Flag any claim you cannot support from the sources I gave you"). One prompt, one job: if the workflow needs two jobs (research, then draft), write two prompts and number them.

## n8n self-host setup guide

This is a setup guide, not a run report: follow it, and record your own result. If a command fails, check the official docs at https://docs.n8n.io/hosting/ before changing anything.

**Prerequisites:** a computer or server that stays on, Docker installed (recommended path) or Node.js 20+ (npm path), and an account with the AI model you plan to use (ChatGPT, Claude, or another provider with an API key).

**Option A — Docker (recommended).** Run:

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Then open `http://localhost:5678` in your browser and create your owner account. The `-v n8n_data:/home/node/.n8n` volume is what keeps your workflows after a restart — without it, a container rebuild wipes them.

**Option B — npm.** Run:

```bash
npx n8n
```

Then open `http://localhost:5678`. This runs in your terminal session: closing the terminal stops n8n. Use a process manager (for example `pm2`) or a server if the workflow must run unattended.

**First-workflow walkthrough (do this before any real build):**

1. In n8n, click **Create Workflow**. Add a **Schedule Trigger** node, set it to run once a day at a time you choose.
2. Add an **AI Agent** node (or an **HTTP Request** node if you are not using AI yet). Connect the trigger to it.
3. Add a final node that writes somewhere you can read — **Google Sheets**, **Slack**, or **Email** (via SMTP or Gmail).
4. Click **Execute workflow** and read the output. If it ran, your install works. Save the workflow and toggle it **Active**.
5. Add your AI provider credential under **Credentials**: paste the API key into n8n's credential store only, never into a prompt, a node name, or a doc.

**Self-hosting costs to state honestly:** the software is free; the server is not. A small virtual server typically costs a few dollars a month, and you are responsible for updates, backups, and keeping it online. If that upkeep is not worth it, use n8n Cloud or Zapier instead.

## Worked build 1: research agent (n8n)

**Status: build guide** — steps to follow, not yet run end-to-end by the author. Run it, then record the date and the result.

**Problem:** every morning you need a short brief on one topic — what changed, what the sources say, what to do next — without opening ten tabs.
**Trigger:** Schedule Trigger, daily at 07:00.

**Node-by-node reference:**

| # | Node | Settings |
|---|---|---|
| 1 | Schedule Trigger | Cron or interval: daily, 07:00 |
| 2 | HTTP Request (or RSS Read) | GET your source: a news search, an RSS feed, or a docs page. Record the exact URL in the node |
| 3 | AI Agent (or Basic LLM Chain) | Model of your choice; prompt = the 8-part block below; input = the text from step 2 |
| 4 | IF / Filter | Only continue when the AI output is non-empty and contains a source link; otherwise stop and log |
| 5 | Google Docs / Email / Slack | Write the brief to one destination you actually read; include the source URLs |
| 6 | Error Trigger (separate workflow) | On failure, send yourself a message with the workflow name and the error text |

**The agent prompt (8-part block, filled):**

1. **Title:** Daily research brief.
2. **Copy-ready prompt:** "You are a research assistant. Context: I follow [topic]. Task: read the sources below and write a brief under 200 words with three sections: What changed, What the sources say, What to do next. Inputs: [paste the fetched text]. Constraints: use only claims present in the sources; name the source after each claim; if a claim has no source, write 'unverified'. Output structure: three headings, bullets under each, one source link per bullet. Quality checks: flag any claim you cannot support from the sources and remove it."
3. **Placeholders:** `[topic]` = the subject you track, e.g. "n8n pricing changes". Fill one example before publishing.
4. **Recommended tool/model:** any chat model on your plan; verify the model name is current before publishing.
5. **How to use:** paste the fetched source text into the prompt; run; read the brief.
6. **Expected output:** example brief (labelled example, not a real run) — see `examples/research-agent-build.md`.
7. **Iteration prompt:** "Check every factual claim in your answer against the sources I provided. List any claim you cannot support, and remove it."
8. **Limitations:** the model can hallucinate sources; every link must be opened and checked before the brief is shared.

**Test run:** run once with a real topic, record the input, the output, and the date. If the output invents a source, the build fails the test — fix the prompt (add the "unverified" rule) and re-run.

**Limits + failure modes:** Schedule Trigger runs only while n8n is up; a laptop that sleeps misses runs. AI steps cost API credit or count against plan limits. The model may summarise a page that failed to load — the Filter node in step 4 is what catches an empty fetch.

**No-code alternative (Zapier):** Schedule by Zapier (trigger) → RSS by Zapier or Webhooks (fetch) → AI by Zapier (summarise) → Gmail or Slack (deliver). Free-plan note: two-step Zaps only, so the fetch-and-summarise version needs Professional, or split it into two Zaps with a storage step between them.

## Worked build 2: inbox triage agent (Zapier)

**Status: build guide** — steps to follow, not yet run end-to-end by the author.

**Problem:** your inbox fills with newsletters, client mail, and notifications, and the urgent items hide. **Trigger:** Gmail "New Email" (or Outlook "New Email").

**Build:**

1. **Trigger:** new email arrives.
2. **AI step:** classify the email into one of four labels — `Urgent — reply today`, `Client — reply this week`, `Newsletter — read later`, `Noise — archive` — and write one line saying why. Prompt rule: "Classify using only the subject and body I give you. If you are unsure, choose the more urgent label and say so."
3. **Paths/Filter (paid plans):** route by label — urgent mail gets a Slack message or a starred label; newsletters get a "Read later" label; noise gets archived.
4. **Output:** a labelled inbox plus, once a day, a digest of the urgent items.

**Free-plan reality check:** the full version is multi-step, so it needs Zapier Professional or an n8n build. On Zapier Free, the honest version is a single two-step Zap: new email → AI classification written into a Google Sheet row. Say which version you are showing.

**Limits + failure modes:** AI classification is a judgement call, not a fact — spot-check it weekly for a month before trusting it. Never let an agent auto-reply to clients or auto-delete mail until the classifier has been right for at least 30 days. Keep a human review step for anything labelled urgent.

## Error handling + cost guards

- **Set an execution cap.** In n8n Cloud, know your monthly execution allowance (Starter: 2,500) and check usage weekly; in Zapier, watch the task counter on the dashboard. A runaway loop (a trigger firing every minute on a noisy feed) burns a month's allowance in a day.
- **Add an Error Trigger workflow in n8n** (or Zapier's error notifications) that messages you the workflow name and the error text. A silent failure is worse than a loud one.
- **Cap AI spend.** Set a usage limit or a monthly budget cap in your AI provider's dashboard before the first run, and check it after the first week.
- **Guard loops.** Any workflow that reads a feed and writes somewhere must remember what it already processed (a "last seen" value in a sheet, a database, or n8n's static data). Without that, every run reprocesses everything.
- **Rate-limit your triggers.** Poll a feed every 15–30 minutes at most on a free plan; every minute is almost never needed and costs executions/tasks.
- **Retry once, then stop.** Configure one retry with a short wait for transient errors (network blips). A workflow that retries forever is a billing incident.
- **Keep a run log.** One row per run: date, input, output, success/failure. When something breaks, the log is how you find out when it started.

## Security checklist

Run this before any build goes live, and again whenever you add a credential or a destination.

- [ ] API keys and passwords live only in the tool's credential store (n8n Credentials, Zapier Connections). Never in a prompt, a node name, a workflow title, a doc, or a screenshot.
- [ ] Each credential has the minimum permission the workflow needs (read-only where possible; no admin keys for a read-only job).
- [ ] No private client data, passwords, or personal records are pasted into an AI prompt unless you have checked that tool's data controls and retention policy.
- [ ] Webhook URLs are treated as secrets: anyone with the URL can trigger the workflow. Use authentication where the tool supports it.
- [ ] The workflow writes only to destinations you control, and you have checked what data leaves your account at each step.
- [ ] Old credentials are revoked when a workflow is retired, not left active.
- [ ] If the workflow touches other people's data (clients, subscribers), you have a lawful basis and a way to delete their data on request.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Workflow never runs on schedule | n8n is not running (terminal closed / server down) or the workflow is not Active | Start n8n, toggle the workflow Active, check the executions list |
| Zapier Zap stops after a few runs | Free-plan task limit (100/month) reached | Check the task counter; upgrade, or reduce polling frequency |
| AI step returns an empty or invented answer | The input fetch failed and the model filled the gap | Add the Filter node (step 4 in Build 1); check the fetched text first |
| "Credential not found" error | The credential was created in a different n8n account or environment | Re-create it in the same instance and re-link the node |
| Same items processed every run | No "last seen" memory | Store the last processed ID/timestamp and filter on it |
| Docker container loses workflows on restart | No volume mounted | Re-create with `-v n8n_data:/home/node/.n8n` and re-import your workflows |

## Known limits

- This skill is a build guide, not a run report. The two worked builds have not been run end-to-end by the author; run them and record your own result before presenting either as working.
- Prices and free-tier limits were last checked 16 November 2026 and change without notice. Always re-check the official pricing page on the day you publish.
- AI models hallucinate: every agent output that states a fact needs a human or automated source check before it is shared.
- n8n self-hosting trades money for maintenance. If you cannot keep a server updated and backed up, a managed plan is the honest recommendation.

## Re-check cadence

- **On publishing day:** re-open every pricing/limit page cited and correct the copy if anything changed.
- **Monthly:** re-check the verified starting stack and update the "last checked" date.
- **When a build breaks:** re-check the tool's docs/changelog first — a silent API or limit change is the most common cause.
