# Install — NeedCraft Skills MEGA Bundle

## Option A — from GitHub (once the repo is public)

```bash
# Whole bundle — installs all 18 skills
npx skills add JokerHTML/needcraft-skills

# One skill only
npx skills add JokerHTML/needcraft-skills --skill top5-rankings
```

The `skills` CLI detects your agent (Claude Code, Codex, Cursor, and others) and installs into its skills directory. Verify with the agent: ask it to list its skills — all 18 names should appear.

> These two commands need the public repo. Until it is published, use Option B.

## Option B — from a local copy (works TODAY)

Clone or download this repo, then install with the `skills` CLI (verified 16 Nov 2026 — installs all 18, images included):

```bash
# Whole bundle, non-interactive (Claude Code, global scope)
npx skills add /path/to/needcraft-skills --skill ai-agents-automation ai-content-qa ai-seo-discovery ai-tool-research carousel-thumbnail-design color-grading fb-ig-scheduling feedback-loop human-gates human-reply motion-graphics platform-policy-disclosure post-publish-qa prompt-writing top5-rankings trend-intelligence video-script-retention youtube-operator -g -y --agent claude-code

# One skill only
npx skills add /path/to/needcraft-skills --skill top5-rankings -g -y --agent claude-code
```

Without `--skill ...` the CLI shows an interactive multi-select of all 18 skills — pick what you want. Omit `--agent claude-code` to let it detect your agent, or replace with `cursor`, `codex`, etc.

Or copy the folders by hand (same result — every skill is self-contained):

```bash
# Claude Code — whole bundle (user scope)
cp -r needcraft-skills/* ~/.claude/skills/

# Claude Code — one skill (user scope)
cp -r needcraft-skills/top5-rankings ~/.claude/skills/

# Claude Code — project scope (this project only)
cp -r needcraft-skills/top5-rankings .claude/skills/

# Codex — whole bundle
cp -r needcraft-skills/* ~/.codex/skills/

# Codex — one skill
cp -r needcraft-skills/top5-rankings ~/.codex/skills/
```

For any other agent, copy the skill folder into that agent's skills directory — every skill is self-contained (`SKILL.md` + `README.md` + `examples/` + `LICENSE`), so a plain copy is a complete install.

## Verify the install

1. Restart the agent (or start a new session) so it picks up the new skills.
2. Ask it: "What skills do you have for ranking AI tools?" — it should answer from `top5-rankings`.
3. Spot-check one skill: open `~/.claude/skills/top5-rankings/SKILL.md` and confirm the frontmatter `name: top5-rankings` is present.

## Uninstall

Delete the skill folder from the agent's skills directory, e.g. `rm -rf ~/.claude/skills/top5-rankings`. Nothing else is installed — no binaries, no background services.
