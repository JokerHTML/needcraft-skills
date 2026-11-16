---
name: fb-ig-scheduling
description: >-
  Schedule Facebook and Instagram posts natively and verify them, without re-uploading blind. Covers the Meta Business Suite route, the in-app composer route, a pre-schedule account check, and the verify-before-you-retry rule that stops duplicates when a publish fails or stalls. Use when scheduling any Facebook Page post or Instagram post, or when a scheduled post or publish reports an error and you need to decide whether to retry.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Facebook & Instagram Scheduling

## What this skill is

A scheduling route for Facebook and Instagram that uses Meta's own native tools first, verifies every slot in the scheduled-posts view or on the live profile, and never retries a failed publish before checking whether it already went through.

Its core principle — **verify live state before retrying a failed write** — is the whole skill in one line. A publish that reports an error, times out, or stalls can still have executed. Re-uploading blind creates a duplicate, and a duplicate is worse than a late post.

Who it is for: anyone scheduling posts to a Facebook Page or an Instagram account who wants a checkable routine instead of guessing whether a post went out.

## Prerequisites

- A Facebook Page (not just a personal profile) with a role that includes creating content — admin or editor-level access. Native scheduling is a Page feature.
- An Instagram professional account (creator or business) if you schedule Instagram posts. Personal accounts have limited or no scheduling.
- The caption file for the slot (see "Caption file format" below). The file is the single source of truth; fix copy there, never by editing live text after scheduling.
- The image or video file, final and checked, before you open the composer.

## When to use

- Scheduling any Facebook Page post or Instagram post.
- Verifying a slot you scheduled earlier.
- Deciding what to do after a publish or schedule reports an error, times out, or stalls.
- Choosing between the native routes when one of them fails for you.

## The routes, in order

### Route 1 — Meta Business Suite (primary, desktop)

This is Meta's own free scheduling tool and the primary route. Steps verified against Meta's Help Center as read 28 October 2026; re-check the help page if the interface has changed.

1. Go to business.facebook.com and sign in, or open your Page and click **Meta Business Suite** in the left menu.
2. Confirm the correct Page is selected (top left). Do not switch accounts to check — confirm from the details already shown on screen.
3. Click **Create post**. Choose where to post: your Facebook Page, and optionally your connected Instagram account.
4. Add your text, photo, video, or link. Check the preview.
5. Turn on **Scheduling options** (in some layouts: click the arrow beside **Publish** and select **Schedule**). Pick a date and time.
6. Click **Schedule**.
7. Verify the slot: open **Planner** (or **Content → Scheduled**) and confirm the post is listed with the right scheduled time, public visibility, attached image, and verbatim caption.

**Limits (Meta's own help page, as read 28 October 2026):** you can schedule a Page post between **20 minutes and 29 days** ahead. All scheduling times use your current time zone, not the Page's audience time zone. If you need content queued further out, native scheduling cannot do it — use a third-party scheduler of your choice, or schedule in batches inside the window.

### Route 2 — The in-app composer (when Suite fails for you)

If Business Suite fails in your environment — a button that does nothing, a picker that never opens, a session that drops — stop retrying it and use the composer in the Facebook or Instagram app instead. This is a fallback for a failing route, not a second copy of the same post.

**Facebook app:** open your Page, tap **What's on your mind?**, create the post, tap **Next** to open Post settings, choose **Schedule for later**, pick the date and time. Scheduled posts sit under **Manage Posts** on your Page. Note: to change a scheduled post after saving it, Meta's help page says you delete it and recreate it — so check the caption and time before saving.

**Instagram app (professional account):** create the post, reel, or carousel as usual; on the final share screen, choose the scheduling option and pick a date and time. Meta documents in-app Instagram scheduling up to 75 days ahead; confirm the current limit in the app, because it changes. Verify the slot in the app's scheduled-content view before you consider it done.

**Business Suite app (mobile):** tap **Content**, choose **Posts**, **Reels**, or **Stories**, tap **Create**, add text and media, tap **Next**, then **Schedule for later** and pick the date and time.

### Route 3 — Post from the account owner's device or app

When the account owner is available, they can publish or schedule directly from their own phone — the Instagram or Facebook app, signed in as the account. This is the most reliable route for anything the desktop tools mishandle (carousels, music, stories). Keep the caption file as the source of truth: the owner copies the approved text verbatim from the file. If the owner is not available, fall back to Route 1 or 2 — never to an unapproved workaround.

### What this skill does NOT prescribe

There is no standard command-line tool for publishing to Facebook or Instagram, and this skill does not invent one. If you use a third-party scheduler or an automation tool, that tool's own documentation governs its commands, flags, and duplicate guards — verify the slot in Meta's own scheduled-posts view afterwards, whichever tool you used. Any guide that names a specific CLI, command, or flag for this job without a source is making it up.

## Pre-schedule account check

Run this before scheduling anything. A failed check stops the schedule, not the day.

1. **Right account:** the composer shows the correct Page or Instagram account. Confirm from details already on screen.
2. **Right role:** the account has a role that includes creating content.
3. **Caption verbatim:** the composer text matches the caption file word for word, including hashtags and the link line, if any.
4. **Media attached and visible:** the image or video appears in the composer preview. If it does not, do not schedule — fix the attachment first.
5. **Time correct:** the scheduled time is in your time zone, at least 20 minutes out, and inside the 29-day window (Route 1).
6. **Visibility:** Public (or the intended audience) is selected.

## Verify before you retry or report

- **Re-read the live or scheduled surface before any retry.** A failed or stuck write can still execute minutes later. Check the scheduled-posts view (for a schedule) or the profile posts list (for a publish) before you touch anything again.
- **An error result does not prove the publish failed.** Check the profile posts list after any error result. If the post is there, it went out — record the link and move on.
- **Never retry a publish before checking the live surface.** If the slot is already scheduled or already live, the retry is skipped, not run.
- **Report a scheduled time or a live link only after you verified it** in the scheduled list or on the live surface.
- **Leave a slot unscheduled and report the blocker plainly** when every route in this skill has failed, instead of returning to a route that already failed for you.

## Caption file format

One file per slot, named `slot-YYYY-MM-DD-HHMM-<platform>.md`. Example:

```markdown
# Slot — 2027-06-15 19:00 — Facebook (EXAMPLE)

> Example caption file. Replace every bracketed line with your own
> post's copy before use.

## Caption (verbatim)
[Your hook — one line about your topic.]
[One useful point your reader can use today.]
[Your call to action — one action only.]

## Media
- hero.png (1200x675)

## Link (first comment, not in the caption body)
https://example.com/[your-page]

## Schedule
- Platform: Facebook Page
- Time: 2027-06-15 19:00 (your local time zone)
- Visibility: Public
- Route used: Business Suite
- Verified: [ ] in Planner — time, visibility, image, caption
```

## Example scheduled slot

| Field | Value |
|---|---|
| Slot | 2027-06-15 19:00, your local time zone (EXAMPLE) |
| Platform | Facebook Page |
| Caption file | `slot-2027-06-15-1900-facebook.md` |
| Media | `hero.png` (1200×675) |
| Route | Meta Business Suite |
| Verification | Listed in Planner → Scheduled, with correct time, Public visibility, image attached, caption verbatim |

## Troubleshooting

- **The file picker does not open when you click "Add photo/video".** First try a fresh browser session and a fresh sign-in. If the picker still does not open, try dragging the file into the composer drop zone instead — this worked in some environments and is worth one attempt, but it is a workaround, not a guaranteed fix, and it was last observed working in one environment in November 2026. If neither works, switch to Route 2 (in-app composer) or Route 3 (owner's device). Do not keep retrying the same dead button.
- **A scheduled post is missing from Planner.** Check the Content → Scheduled filter, and check whether you are looking at the right Page. If it is genuinely absent, treat the schedule as failed and re-schedule from the caption file — after checking the live Page, in case it published immediately instead.
- **A post published twice.** Do not delete either copy on your own if someone else owns the account — report both links and ask which to keep. Then verify the deletion live.
- **Suite worked yesterday and fails today.** Meta changes the interface and the limits. Re-read the current help page before assuming your environment is at fault.

## Failure modes

- **Retrying a failed publish blind.** Mitigate: the verify-before-retry rule above, every time, no exceptions.
- **Editing copy live after scheduling.** Mitigate: the caption file is the single source of truth; fix copy there, then re-schedule.
- **Scheduling outside the window.** Mitigate: the pre-schedule check catches times under 20 minutes or over 29 days (Route 1).
- **Wrong account.** Mitigate: confirm the account from on-screen details before composing, never by switching accounts mid-session.

## Known limits

- Native scheduling is a Page feature. Personal profiles do not get the same built-in scheduler, and no third-party tool can publish to a personal profile — Meta's API does not permit it.
- The 20-minute-to-29-day window and the in-app steps above reflect Meta's help pages as read 28 October 2026 and this skill's verification date of 16 November 2026. Meta changes these; re-check the help page when a step stops matching the screen.
- Instagram scheduling details (limits, which formats can be scheduled) vary by account type and app version. Confirm in the app for your account.
- This skill covers scheduling and verification. It does not cover writing captions, designing images, or comment management.
