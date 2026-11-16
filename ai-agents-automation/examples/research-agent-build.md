# Worked build: daily research brief agent (n8n)

**Status: build guide (example).** The steps below are a complete build you can follow. The sample output is illustrative — it was written as an example, not produced by a run. Run the workflow yourself, then replace this note with your run date and result.

## The job

Every morning, produce a short brief on one topic: what changed, what the sources say, what to do next.

## Build (n8n)

1. **Schedule Trigger** — daily, 07:00.
2. **HTTP Request** — GET the source page or RSS feed for your topic. Example source: the n8n changelog, https://docs.n8n.io/release-notes/ (check the URL is current before use).
3. **AI Agent** — model of your choice; prompt below; input = text from step 2.
4. **IF node** — continue only when the output is non-empty and contains at least one source link.
5. **Gmail / Slack / Google Docs** — deliver the brief to one destination you actually read.

## The agent prompt (filled 8-part block)

1. **Title:** Daily research brief — n8n changelog.
2. **Copy-ready prompt:**

   ```text
   You are a research assistant. Context: I follow n8n product changes.
   Task: read the sources below and write a brief under 200 words with
   three sections: What changed, What the sources say, What to do next.
   Inputs: [paste the fetched changelog text].
   Constraints: use only claims present in the sources; name the source
   after each claim; if a claim has no source, write "unverified".
   Output structure: three headings, bullets under each, one source link
   per bullet. Quality checks: flag any claim you cannot support from the
   sources and remove it.
   ```

3. **Placeholders:** `[paste the fetched changelog text]` = the raw text from the HTTP Request node. No other placeholders.
4. **Recommended tool/model:** any chat model on your plan; verify the model name is current before publishing.
5. **How to use:** open the workflow, run it once manually, read the brief in your chosen destination.
6. **Expected output (example, not a real run):**

   ```text
   ## What changed
   - n8n released a new AI Agent node update. Source: n8n changelog.

   ## What the sources say
   - The update adds error handling for tool calls. Source: n8n changelog.

   ## What to do next
   - Read the changelog entry and test the new node in a copy of your workflow.
   ```

   The lines above are illustrative wording, not claims about any real release. Never present them as release notes.
7. **Iteration prompt:** "Check every factual claim in your answer against the sources I provided. List any claim you cannot support, and remove it."
8. **Limitations:** the model can hallucinate changelog entries; open every link before sharing the brief.

## Cost check (before you switch it on)

- n8n Cloud Starter allows 2,500 executions/month (last checked 16 Nov 2026). One run a day = ~30 executions/month. The AI step's cost depends on your model provider — set a budget cap there first.
- On Zapier Free (100 tasks/month), this build as a two-step Zap is not possible as written; the multi-step version needs a paid plan.

## Test run record

| Date | Input | Output | Result |
|---|---|---|---|
| _(fill in after your first run)_ | | | |

## No-code alternative (Zapier)

Schedule by Zapier → RSS by Zapier → AI by Zapier → Gmail. Free-plan note: two-step Zaps only, so split it into two Zaps with a storage step between them, or use a paid plan.
