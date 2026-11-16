# Human Gates

Track every action only a human can take — so it never ages silently.

## What it is

A human-in-the-loop tracker. Some steps can only be done by the person who owns the account or the decision: signing in, approving a session, tapping something on their phone, passing an identity check, or making a call only they can make. Each gate is logged once in a single gate log file, re-surfaced on a schedule (3 / 7 / 14 days by default, tunable), and closed only on verification.

## Who it is for

Anyone doing work on someone else's accounts, where some steps need the account owner — and solo operators tracking their own blocked steps across sessions.

## How to use

1. Pick one gate log file (`gates.md` in your project notes, for example) and write its path in your notes.
2. Before opening a gate, confirm the blocker is real: at least 3 genuine attempts first.
3. Log the gate the moment you ask, with exact steps and a timebox. Ask in chat first — the log is the record, never a replacement for the ask.
4. Read the log at the start of every session touching blocked work; re-surface at 3, 7, and 14 days; close only on confirmation or live verification.

## Example

A filled example gate entry (open and closed) is in `SKILL.md`, plus a copy-paste template for opening a gate. An example log file is in `examples/gates-example.md`.

## Install

This is a skill (a `SKILL.md` playbook), not software. Copy the `human-gates/` folder into your agent's skills directory and invoke it whenever work hits a human-only step, or follow it manually as a checklist.

## License

MIT — see `LICENSE` in the repository root, or treat this file set as MIT-licensed.

## Disclaimer

This skill tracks gates; it does not resolve them. A gate closes when the human acts or the need disappears. If the human never responds, the answer is the 14-day keep-or-drop decision — not louder asking.
