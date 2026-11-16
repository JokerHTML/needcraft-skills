---
name: human-gates
description: >-
  Track every action only a human can take — a login, a session approval, a phone-side action, a platform identity check, or a decision only the human can make — so it never ages silently. Each gate is logged once in a gate log file, re-surfaced on a schedule, and closed only on verification. Use whenever your work hits a step that only the human can do, at the start of any session that touches blocked work, and when deciding whether an old gate stays open or gets dropped.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Human Gates

## What this skill is

A human-in-the-loop tracker. Some steps can only be done by the human who owns the account or the decision: signing in, approving a session, tapping something on their phone, passing an identity check, or making a call only they can make. This skill makes sure those steps get asked once, logged once, re-surfaced on a schedule, and closed only when verified — so a gate asked on Monday is not silently forgotten by Friday.

Who it is for: anyone (human or agent) doing work on someone else's accounts, where some steps need the account owner. Also useful for a solo operator tracking their own blocked steps across sessions.

## Prerequisites

- **One gate log file, chosen by you.** A plain text or Markdown file in a place every session and every scheduled run can read — for example `gates.md` in your project notes, or a section of your main notes file. The whole skill runs on this one file. Pick it once, write its path at the top of your notes, and never move it.
- A way to remind yourself: a calendar reminder, a scheduled check, or a session-start habit (see "Setup" below). The skill does not depend on any particular reminder tool.

## When to use

- The moment your work hits a step only the human can do.
- At the start of any session or run that touches blocked work — read the log first.
- When a gate has waited 3, 7, or 14 days (see "Re-surface the gate").
- When the blocked work can proceed partly — stage everything around the gate.

## Setup

1. Create the gate log file. Put this header at the top:

```markdown
# Human gates

One line per gate. Never rewrite history, never merge two gates into one line.
Columns: opened date | gate (one line) | exact steps for the human | asked dates | status (OPEN/CLOSED/DROPPED) | resolution + how verified
```

2. Make reading the log a habit: read it at the start of every session and every scheduled run that touches the blocked area, and set a recurring reminder (daily or weekly, your choice) to review open gates. The reminder tool is yours — a calendar event, a cron job, a scheduled agent run, or a sticky note. The skill needs the review to happen; it does not care what triggers it.
3. Tell the human, once, where the log lives and that open gates will be re-surfaced — so the reminders are expected, not a surprise.

## The blocker protocol (summary)

Before opening a gate, confirm the blocker is real. The rule:

1. **Try at least 3 genuine attempts** before declaring a blocker — across sessions when the failure looks transient. A flaky session is not a gate. A genuine attempt means waiting for the page or tool to fully load, reloading once, and checking the actual state (not assuming from an error message).
2. **Then escalate to the human** with the exact ask, exact steps, and a timebox. The ask goes in chat first; the log entry is the record, never a replacement for the ask.
3. **Never work around the gate silently.** Do not find a different route that bypasses a login, an approval, or an identity check the human is supposed to do. If a workaround exists and is legitimate, say so explicitly and let the human decide.
4. **Stage everything around the gate.** While it waits, do all the work that does not need it, so resolving the gate later needs no rework. Say plainly what is staged, what is blocked, and what resolving the gate unblocks.

## Open a gate

- Log the gate in the gate log file the moment you ask the human, before you move on. Record the date, the gate in one line, the exact steps for them, and the status OPEN.
- Report the ask in chat first, with exact steps and a timebox. The log is the queue; it never replaces the ask.
- Keep one line per gate and append every asked date. Never rewrite history or merge two different gates into one line.

### Example gate entry

```markdown
- 2026-10-06 | Social profile link needs updating from the phone app (app-only setting) | 1. Open the app on your phone. 2. Go to Edit profile. 3. Set the website field to the new page URL. 4. Tell me when it is done so I can verify it live. | Asked: 2026-10-06, 2026-10-09 | OPEN
```

## Re-surface the gate

- Read the log at the start of every session and every run that touches the blocked area. Check which gates are still open and how long they have waited.
- **After 3 days open:** re-surface the gate with one chat line carrying the exact ask again. Mention the days waited so the human sees the age.
- **After 7 days open:** collect every stale gate into one short list, newest first, and post it at most once per day. Stop attaching gate asks to unrelated conversations.
- **After 14 days open:** bring the gate to chat for a keep-or-drop decision. A dropped gate leaves the log with a one-line reason and its asked history intact.

The 3 / 7 / 14-day cadence is a tunable default, not a fixed rule. It assumes a human who checks chat roughly daily and work that can wait a few days. Tighten it (1 / 3 / 7) if the gate blocks a launch or a deadline; loosen it (7 / 14 / 30) if the human checks in weekly and nothing is time-critical. Whatever cadence you choose, write it in the log header and stick to it — the point is that re-surfacing is scheduled, not improvised.

## Close the gate

- Close a gate when the human confirms the action, when the action verifies live, or when the need disappears. Record the resolution date and how you verified it.
- Never close on assumption or because the run moved on. An unverified gate stays OPEN.
- A dropped gate (after the 14-day keep-or-drop decision) leaves the log with a one-line reason and its asked history intact.

### Example closed entry

```markdown
- 2026-10-06 | Social profile link needs updating from the phone app (app-only setting) | 1. Open the app on your phone. 2. Go to Edit profile. 3. Set the website field to the new page URL. 4. Tell me when it is done so I can verify it live. | Asked: 2026-10-06, 2026-10-09 | CLOSED 2026-10-10 — human confirmed; verified live on the profile page
```

## Copy-paste template

Use this to open a gate in chat and in the log:

```markdown
GATE — [one-line gate]
Needed from you:
1. [exact step]
2. [exact step]
3. [exact step]
Time needed: [minutes]
Blocks: [what is staged and waiting on this]
If this waits: [what happens if it stays open]
Asked: [date]
```

## Failure modes

- **A gate asked once and never re-surfaced.** Mitigate: the 3 / 7 / 14-day re-surface schedule, and the session-start log read.
- **A gate closed on assumption.** Mitigate: close only on confirmation or live verification, with the verification method recorded.
- **Two gates merged into one line.** Mitigate: one line per gate; a new ask is a new line, even if it looks similar.
- **A workaround applied silently.** Mitigate: the blocker protocol — no bypass without the human's explicit decision.
- **The log lives in two places.** Mitigate: one log file, chosen once, named in your notes. If you ever move it, leave a pointer at the old location.

## Known limits

- This skill tracks gates; it does not resolve them. A gate closes when the human acts or the need disappears — no tracking system changes that.
- The cadence defaults are a starting point. A human who checks chat weekly needs a different schedule than one who checks hourly; tune it and write the tuned version in the log header.
- If the human never responds, the skill's answer is the 14-day keep-or-drop decision — not louder or more frequent asking.
