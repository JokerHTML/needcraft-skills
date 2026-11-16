# Facebook & Instagram Scheduling

Schedule Facebook and Instagram posts natively and verify them — without re-uploading blind.

## What it is

A scheduling route that uses Meta's own tools first (Meta Business Suite, then the in-app composer, then the account owner's device), verifies every slot in the scheduled-posts view or on the live profile, and never retries a failed publish before checking whether it already went through. Its core principle: **verify live state before retrying a failed write** — a publish that reports an error can still have executed, and re-uploading blind creates a duplicate.

## Who it is for

Anyone scheduling posts to a Facebook Page or an Instagram account who wants a checkable routine instead of guessing whether a post went out.

## How to use

1. Write the caption file for the slot (format in `SKILL.md`) — it is the single source of truth.
2. Run the pre-schedule account check.
3. Schedule via Meta Business Suite (primary route). If it fails in your environment, use the in-app composer; if that fails, the owner's device.
4. Verify the slot in Planner / Scheduled view. Report the time or link only after verification.

## Example

A filled caption file is in `examples/slot-2027-06-15-1900-facebook.md`.

## Install

This is a skill (a `SKILL.md` playbook), not software. Copy the `fb-ig-scheduling/` folder into your agent's skills directory and invoke it when scheduling, or follow it manually as a checklist.

## License

MIT — see `LICENSE` in the repository root, or treat this file set as MIT-licensed.

## Disclaimer

Steps and limits reflect Meta's help pages as read 28 October 2026, verified 16 November 2026. Meta changes the interface and the limits; re-check the help page when a step stops matching the screen. There is no standard command-line tool for publishing to Facebook or Instagram — this skill does not invent one.
