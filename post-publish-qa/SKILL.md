---
name: post-publish-qa
description: >-
  Verify a social post after publishing it: duplicate guard, live re-read
  against the source caption, media and link checks, public-visibility
  check, and a lag re-read before any second delivery. Use after every
  publish or schedule, and whenever a publish result is uncertain, before
  retrying — a failed or stuck publish can still land later, and retrying
  blind creates duplicates.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Post-Publish QA

## What this skill is

A verification method for social posts, in three parts: check **before**
you publish (right account, no duplicate, latest caption, good media),
verify **after** you publish (live post re-read against the source
caption, media, links, visibility), and handle failures without creating
duplicates. It works with any publishing tool — a platform's own app or
scheduler, an API, or a third-party tool — because every check is done
against the live surface, never by trusting the tool's success message.

Who it is for: anyone who publishes or schedules social posts and wants
proof the post is live, correct, and not duplicated — instead of assuming
the publish call worked.

## Prerequisites

- One caption file per post, as the single source of truth. Fix text
  there, never by editing live text.
- Access to read the live account: the platform's app/website, an API
  read method, or a scheduling tool that shows recent posts. Any read
  method works; this skill names none, so it stays tool-independent.
- A way to view the post as a non-owner (see
  [Confirm public visibility](#confirm-public-visibility-through-a-non-owner-read)).

## Check before you publish

- Open the correct account first. Confirm the account name (and Page
  name, where the platform uses Pages) before you touch any publish or
  schedule control. Never publish from a duplicate or personal account
  when the post belongs to a brand account.
- Confirm the session is signed in as the correct account before you
  schedule. Stop and report a blocker when it is signed out.
- Read the recent posts on that exact account before you publish or
  schedule anything.
- Compare the slot caption and media against those recent posts and stop
  when you find the same caption or media already live.
- Read the caption file again at publish time and confirm it is the
  latest fixed version, not an earlier draft.
- Confirm the media file named in the batch matches the caption and
  opens without corruption.
- Write one pre-publish record for the slot (template in
  `examples/pre-publish-record.md`) naming the account checked and the
  duplicate-check result.

## Verify after you publish

- Open the live URL returned by the publish call. If no URL was
  returned, find the post in the account's recent posts list.
- Compare the live text with the caption file byte for byte. Fail the
  post on any hashtag or wording mismatch.
- Check that images load at full size and that video plays for the full
  source duration.
- Check that links appear only where the platform allows them. Never a
  raw link in a post body where the platform forbids it (for example, a
  raw URL in a Threads post body — the link belongs in the first reply).
- Check formatting for literal asterisks, broken unicode, and collapsed
  line breaks. Fail the post on any corruption.
- Confirm public visibility through a read that does not rely on the
  owner session (see below).
- Check recent posts again for an accidental duplicate. Treat a
  duplicate as a defect.
- Verify any product link, self-reply, or first comment on product posts:
  the exact product URL, in the correct place.
- Write one verification record per post (template in
  `examples/verification-record.md`) with date, platform, status, URL,
  and problem (or "none").

## Confirm public visibility through a non-owner read

An owner-session view can show a post that nobody else can see (draft,
scheduled-but-unpublished, restricted, or failed visibility). Confirm
visibility one of these ways, in order of preference:

1. **Logged-out view:** open the post's public URL in a private/incognito
   browser window while logged out. If the post loads with its full text
   and media, it is publicly visible.
2. **Second account:** open the post from a different account (a personal
   account, a colleague's) that does not follow the publishing account.
   If it loads, it is visible to non-followers.
3. **Ask a second person:** send the post URL to someone who does not
   manage the account and ask them to confirm it loads.
4. **Platform share preview:** use the platform's share/copy-link flow
   and open the copied link logged out (same as method 1).

If none of these is possible for a platform, record "visibility check
not possible — owner view only" in the verification record and treat the
post as unverified, not as confirmed live.

## Handle failures

- Stop the batch on any defect. Do not continue to the next slot until
  the defect is resolved or the owner explicitly waives it.
- Check the live surface first when a publish result is uncertain, and
  never retry a publish before that check.
- Treat a failed or stuck write as possibly delivered later, and re-check
  the live surface before you publish a replacement. A publish call that
  errors or times out can still land minutes later.
- Ask the owner for approval before you delete any live post. Never
  delete automatically.
- Stop after three genuine verification attempts when a live post cannot
  be reached, and report the blocker. A **genuine verification attempt**
  means: wait at least 60 seconds after the publish call, reload the
  recent-posts list (or re-open the post URL) from scratch — not a cached
  view — and check both the direct URL and the account's recent posts.
  Space attempts at least 5 minutes apart. Three attempts that all fail
  this way = report the blocker, do not keep retrying.

## Re-read after a lag before any second delivery

A "zero results" read is not proof of absence when an earlier run may
already have delivered the same post without reporting it.

- Treat a zero-guard result as unverified, not as proof of absence.
- For threaded replies: read the nested replies in the thread itself,
  not only the top-level recent-posts list, before you publish a reply.
- Wait for the threaded surface to settle and re-read the live thread a
  second time after a short delay (at least 2 minutes) when the first
  read shows no matching reply.
- Check the published log and any delivery record for the slot before
  you make a second delivery attempt.
- Stop and report the slot as unverified when the second read still
  cannot confirm absence, instead of publishing a second copy.
- Record both reads, with their times and results, in the pre-publish
  record for the slot.

## Alternatives for better results

- Schedule inside each platform's native scheduler and verify the slot
  in that platform's scheduled list, rather than trusting a schedule
  command's success message.
- Keep one caption file per slot as the single source of truth and fix
  it there rather than editing live text.
- Track each destination separately, so recovering one failure cannot
  duplicate a post that already succeeded on another destination.
- For image-first platforms, check recent pins/posts before you publish
  and verify the live pin/post after you publish, rather than trusting
  the publish result.

## Worked example — one full pass

**Slot:** a tutorial carousel for Instagram. Caption file:
`tutorial-carousel.txt`. Media: 5 slides, 1080x1350.

**Pre-publish (14:02).** Account checked: brand Instagram account
(display name confirmed). Recent posts read: last 10 posts, no matching
caption or media. Caption file re-read: latest version, 3 hashtags.
Media: all 5 slides open, correct order. Pre-publish record written:
duplicate check = clear.

**Publish (14:05).** Scheduled via the platform's native scheduler for
17:00. Slot confirmed in the platform's scheduled list.

**Verify after publish (17:04).** Post opened from the scheduled-list
link. Live text compared byte for byte with `tutorial-carousel.txt`:
match. All 5 slides load at full size. No raw link in the body (link
is in the first comment, as intended). No literal asterisks or broken
unicode. Public visibility: opened the post URL in a logged-out
private window — loads with full text and all slides. Recent posts
re-checked: one copy only. First comment verified: exact product URL
present. Verification record written: status PASS, problem none.

**What would have failed it:** if the live text had shown a hashtag
missing from the caption file, the record would read FAIL (text
mismatch), the batch would stop, and the fix would be made in the
caption file — never by editing the live post.

## Templates

- `examples/pre-publish-record.md` — blank template + one filled
  example (the carousel above).
- `examples/verification-record.md` — blank template + one filled
  example (the carousel above).

## Troubleshooting

| Problem | What to do |
|---|---|
| Publish call errors or times out | Do not retry. Read the live surface first (recent posts + direct URL). It may have landed. |
| Live text differs from the caption file | FAIL the post. Fix the caption file, then decide with the owner whether to edit or re-post. Never silently pass a mismatch. |
| Two copies live | Report both URLs to the owner and ask which to keep. Never delete without approval. |
| Post visible to owner but not logged-out | Visibility defect. Check the account's visibility/audience settings and the platform's status; report it, do not re-post. |
| Cannot reach the live post after 3 genuine attempts | Stop. Report the blocker with the three attempt times. Do not keep retrying. |
| A threaded reply may already exist | Re-read the nested thread after a 2-minute lag. If still unconfirmed, report as unverified — do not publish a second copy. |

## Known limits

- This skill verifies what is visible on the live surface. It cannot
  verify platform-internal states (shadow restrictions, reduced
  distribution) — those show up only in the platform's own insights or
  support channels.
- A logged-out visibility check is not possible on every platform (some
  require login to view any post). In that case the record must say so
  explicitly; the post is unverified, not confirmed.
