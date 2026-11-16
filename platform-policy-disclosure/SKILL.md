---
name: platform-policy-disclosure
description: >-
  Keep social posts inside current platform policy: AI-disclosure rules per
  platform, monetisation eligibility checks, affiliate and sponsor disclosure
  wording, and originality rules for Facebook and YouTube. Use before
  publishing any post that uses realistic AI content, mentions income or
  monetisation, or carries an affiliate or sponsored link — and re-check the
  official pages before every publishing cycle, because policies change.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Platform Policy, Monetisation & Disclosure

## What this skill is

A pre-publish policy check for creators posting to YouTube, Instagram,
Facebook, Threads, TikTok, X, Pinterest, and LinkedIn. It covers four
things: (1) when each platform requires an AI-content label and how to
turn it on; (2) whether a channel or account can earn money at all;
(3) how to disclose affiliate and sponsored relationships; and (4) what
counts as original content under Meta's and YouTube's rules.

Who it is for: a creator or agent publishing social content who wants a
repeatable check instead of guessing at policy — especially when a post
uses AI-generated media, mentions money, or links to a product.

## How to use it

1. Before a publishing cycle, re-check the official pages in
   [Official references](#official-references). Policies change; this
   skill's dates show when each claim was last verified.
2. Run the post through the [Disclosure checklist](#disclosure-checklist-per-post).
3. If the post mentions income or monetisation, run the
   [Monetisation eligibility decision tree](#monetisation-eligibility-decision-tree).
4. If the post carries an affiliate or sponsored link, add disclosure
   wording from the [templates](#affiliatesponsor-disclosure-wording-templates).
5. If a policy claim is uncertain, label it, investigate more, or do not
   publish. Never state a policy claim without a re-check.

This skill is guidance, not legal advice. For paid campaigns or
regulated claims, check with a qualified adviser.

## The realism test (the rule behind every platform's AI label)

Every major platform applies the same underlying test, in different
words: **if AI created or meaningfully changed something a viewer could
mistake for real — a real person, a real place, a real event, a realistic
voice — disclose it.** Clearly unrealistic, animated, or cartoon content
does not need a label. Minor edits (colour, cropping, captions, filters,
upscaling) do not need one either. Production help — AI-written scripts,
outlines, titles, or thumbnails — does not trigger disclosure on its own.

## Per-platform AI-disclosure matrix

Last verified: 16 November 2026 (via each platform's help pages and
secondary reporting of them). Menu wording changes often — if a toggle
has moved, follow the platform's current help page, not this table.

| Platform | Label name | When it is required | Where to enable it | Auto-applied? |
|---|---|---|---|---|
| YouTube | "Altered or synthetic content" / "AI generated or altered" | Realistic GenAI content: a real person shown saying/doing something they did not; footage of a real event or place altered; a realistic scene that never occurred; AI music as the main focus of the video | YouTube Studio upload flow → Details → "AI use" (under Attributes): select Yes/No | Yes — YouTube may label automatically when its systems detect significant photorealistic AI use (since its May 2026 update), and permanently for content made with YouTube's own AI tools or carrying C2PA metadata |
| Instagram / Facebook | "AI info" | Photorealistic video or realistic-sounding audio digitally created or altered, including with AI. Meta's help pages say images are not mandatory to label, but Meta may label them automatically | Post/reel share screen → "Add AI label" toggle (in-app; wording varies by version) | Yes — from C2PA/IPTC provenance signals in the file. Fully AI-generated content gets a visible label; content only edited with AI shows it in the post's menu |
| Threads | "AI info" | Same Meta rule as Instagram/Facebook | Same "Add AI label" control where the app offers it | Yes — same Meta provenance detection |
| TikTok | "AI-generated" (creator label) / "AI-generated" (auto label) | AI-generated or significantly edited content showing realistic scenes or people: face swaps, fake speech, misleading additions/removals, an AI voice imitating a real person | Upload → Next → More options → "AI-generated content" toggle, before posting. A caption, sticker, or watermark also counts | Yes — TikTok's own AI effects, C2PA Content Credentials, and its detection systems; auto labels cannot be removed |
| X | No creator self-label documented (as of Oct–Nov 2026) | No published toggle found in X's help pages; X enforces its synthetic and manipulated media policy against deceptive media | Disclose in the post text itself (e.g. "Made with AI") and re-check X's policy page before posting | Not stated by X |
| Pinterest | "AI modified" | Applied by Pinterest (no creator toggle): shown at the bottom left of a Pin close-up when image metadata matches the IPTC standard, or Pinterest's classifiers flag it (introduced 30 April 2025) | No creator control — keep provenance metadata intact in your files; disclose in the Pin description if the image is AI-generated | Yes — metadata + classifiers |
| LinkedIn | Content Credentials "CR" icon | No creator mandate and no creator switch. LinkedIn reads C2PA Content Credentials in the file and shows an icon viewers can click to see whether AI generated or edited any part | No creator control — keep C2PA credentials embedded if your tool writes them | Yes, from C2PA metadata only; no credential, no icon |

Notes:

- **YouTube, May 2026 update (verified via search, 16 Nov 2026):** YouTube
  changed where the label appears — below the player and above the
  description for long-form video, and as an overlay on Shorts — and began
  applying labels automatically when its systems detect significant
  photorealistic AI use. Re-check the YouTube Help page before relying on
  the placement detail.
- **Disclosing alone does not hurt a video.** YouTube's Help page states
  that disclosing AI content will not limit a video's audience or affect
  its eligibility to earn money. Failing to disclose can: YouTube may
  apply a label itself or penalise the channel, up to removal or suspension
  from the YouTube Partner Program for repeated non-disclosure.
- **Keep provenance metadata.** C2PA Content Credentials embedded by your
  generation tool are read by YouTube, TikTok, Meta, LinkedIn, and
  Pinterest. Stripping them does not remove the obligation to disclose.

## Monetisation eligibility decision tree

Work top to bottom. A "no" at any step means: do not claim the content
can earn money, and do not publish an income claim about it.

1. **Is the platform's payout programme open to you?**
   - YouTube: the YouTube Partner Program (YPP) is the route to ad
     revenue. Thresholds (YouTube Help, verified 16 Nov 2026): 1,000
     subscribers AND either 4,000 valid public watch hours in the last
     12 months OR 10 million valid public Shorts views in the last
     90 days. Shorts-feed watch time does not count toward the 4,000
     hours. A lower tier (500 subscribers) unlocks fan funding and
     Shopping only — not ad revenue. You also need an AdSense account,
     no active Community Guidelines strikes, and to live in a country
     where YPP is available.
   - Facebook: Content Monetization is invite-only (Meta's own pages,
     verified Nov 2026). There is no published follower-count or
     watch-time threshold to apply against, and open enrolment has been
     announced as "coming soon" with no date. Do not promise anyone a
     route in.
   - TikTok, Instagram, X, Pinterest, LinkedIn: each runs its own
     creator payout or bonus programmes with their own eligibility
     pages. Check the programme's official page for your country before
     claiming eligibility.
   - If you cannot confirm the programme is open to you: STOP. Say
     "eligibility not confirmed", never "you can monetise this".
2. **Is the content original?** See
   [Originality rules](#originality-rules-meta-and-youtube) below. Reused
   or repetitious content fails monetisation review on YouTube and loses
   monetisation on Facebook even inside the programme.
3. **Is the AI disclosure done?** Realistic AI content without the
   required label risks removal and YPP suspension. Disclosure itself
   does not block monetisation (YouTube Help).
4. **Are the income claims honest?** Never say AI videos automatically
   qualify for monetisation, and never guarantee income, views, or
   virality. State realistic costs (tools, time) alongside any earnings
   claim, and label any earnings figure as your own measured result with
   its date — or do not use it.

## Affiliate/sponsor disclosure wording templates

The rule, from the US Federal Trade Commission's Endorsement Guides
(16 CFR Part 255, updated June 2023): any **material connection** — a
payment, a free product, or a commission on sales — must be disclosed
**clearly and conspicuously**, in plain language, **before** the audience
engages with the recommendation or clicks the link. A platform's native
"Paid partnership" toggle helps but is not enough on its own. A
disclosure buried at the end, behind a "see more" cutoff, or only on an
About page does not satisfy the rule. Ambiguous tags such as `#sp`,
`#collab`, `#thanks`, or `#ambassador` alone are not accepted by the FTC;
`#ad` and `#sponsored` are.

### Caption templates (put the disclosure first, before any link)

- Affiliate link, short post:
  `#ad — This post contains affiliate links. If you buy through them,
  I may earn a small commission at no extra cost to you.`
- Affiliate link, longer post:
  `Disclosure: This post contains affiliate links. I may earn a
  commission if you buy through them, at no extra cost to you. My
  ranking is independent — no sponsor decides the order.`
- Paid sponsorship:
  `#ad — Paid partnership with [Brand]. They sponsored this post; the
  opinions are my own.`
- Gifted product (no payment, free product only):
  `#gifted — [Brand] sent me this product for free. No payment, and
  they did not approve what I say about it.`
- Amazon Associates (their programme requires its own sentence):
  `As an Amazon Associate I earn from qualifying purchases.`

### On-screen / spoken templates (video — same-medium rule)

If the endorsement is spoken, disclose it spoken. If it is on screen,
disclose it on screen. For video, do both:

- Spoken, in the first 30 seconds: `"This video is sponsored by
  [Brand]."` or `"The links below are affiliate links — I earn a
  commission if you buy through them."`
- On-screen text, first few seconds, readable size, high contrast:
  `Paid partnership with [Brand]` or `Affiliate links — I earn a
  commission`.
- YouTube: also tick the "includes paid promotion" box in Studio — it
  supplements the spoken/on-screen disclosure, it does not replace it.
- Stories / multi-slide posts: disclose on every frame, or at minimum
  every three to four slides, because viewers join mid-sequence.

### Ranking-independence line (use on every ranked post with a link)

`No sponsor or affiliate relationship affects this ranking. [Brand] did
not pay for placement. If a link earns me a commission, it is disclosed
next to the link.`

## Originality rules (Meta and YouTube)

### Meta — "Rewarding Original Creators" (announced 13 March 2026; verified 16 Nov 2026)

Meta's position: original content is content **filmed or produced
directly by the creator or owner of the Profile or Page**. Content that
incorporates third-party material still counts as original when the
creator's own on-screen presence is the focus and they add genuinely new
information, analysis, or a substantially improved storyline.

What Meta calls **unoriginal** (and deprioritises, demonetises, or makes
non-recommendable after repeated posting):

| Unoriginal (do not do) | Why it fails | Original version of the same idea |
|---|---|---|
| Re-uploading someone else's video with only minor edits | No new contribution | Film your own take, with your own footage and analysis |
| Reaction content that is only facial expressions or narration of what is on screen | Nothing meaningful added | Add fresh information, a test, or a counter-argument |
| Compilations of third-party clips without meaningful commentary | Assembly is not authorship | Curate with a thesis: why these clips, what the pattern is |
| Content carrying a visible TikTok/YouTube watermark | Signals a re-upload | Post your own export, watermark-free |
| Cosmetic edits only: borders, captions, speed changes | No real transformation | Re-edit with new structure, new narration, new conclusion |
| Watching along / narrating what is already visible | The viewer learns nothing new | Explain what the clip does not show |

Enforcement is graduated: reduced distribution across **all** posts on
the account (not just the offending one), then loss of access to Meta's
Content Monetization Program, then the account becomes
non-recommendable. The July 2025 crackdown on the same behaviour
preceded the March 2026 definition. This applies to Profiles and
Business Pages alike.

### YouTube — reused and repetitious content

YouTube's channel monetisation policies exclude **reused content**
(someone else's content re-uploaded without adding significant original
commentary or educational value) and **repetitious content** (videos
that are largely the same, mass-produced, or templated with minimal
differences). A channel applying for YPP is reviewed as a whole, and
reviewers keep checking after acceptance. Practical test before
uploading: could a viewer get the same video from the original source?
If yes, add commentary, a test, or an edit that changes what the viewer
learns — or do not upload it.

## Disclosure checklist (per post)

- [ ] AI-generated/altered realistic content identified → required label
      enabled (see matrix above)?
- [ ] Monetisation/income claim present? → official policy re-checked
      + no guarantee language + realistic costs stated?
- [ ] Affiliate/sponsor link present? → disclosure written at the top,
      before the link + ranking independence stated?
- [ ] Originality: meaningful original contribution (not a re-upload or
      light edit of someone else's work)?
- [ ] Platform-specific disclosure rules verified for each platform the
      post ships to (matrix re-check date noted)?
- [ ] Provenance metadata (C2PA) left intact in media files?

## Worked example — one post run through the checklist

**Post:** a 40-second vertical video, "I tested 3 free AI image tools
so you don't have to". The video shows the presenter's face on camera,
screen recordings of the three tools, and an AI-generated thumbnail
image of a robot holding a paintbrush (clearly cartoon-style). Caption
links to the three tools; one link is an affiliate link. The post ships
to Instagram, TikTok, and YouTube Shorts.

| Check | Result |
|---|---|
| AI label — video | The presenter is real, the screen recordings are real. No realistic synthetic person, place, or event. **No label required** on any platform. |
| AI label — thumbnail | Cartoon robot, clearly not real. **No label required** on YouTube (thumbnails are production help anyway). Meta may auto-label it "AI info" from metadata — that is fine, do not strip the metadata. |
| Monetisation | No income claim in the post. No YPP check needed for this post. |
| Affiliate disclosure | Caption opens with: `#ad — This post contains affiliate links. If you buy through them, I may earn a small commission at no extra cost to you.` The affiliate link is labelled next to it. Spoken line in the first 10 seconds: "One of the links below is an affiliate link." |
| Originality | Presenter on camera + own tests + own verdicts = original under Meta's rule and YouTube's reused-content rule. |
| Platform check | Instagram: no "Add AI label" needed (nothing realistic). TikTok: no "AI-generated content" toggle needed. YouTube Studio: "AI use" = No (nothing realistic). Re-check dates noted: 16 Nov 2026. |

**Verdict: publish.** If the thumbnail had instead been a photorealistic
image of a real person, the answer would change: YouTube "AI use" = Yes,
Instagram "Add AI label" on, TikTok toggle on.

## Official references (re-check before applying — policies change)

- YouTube Help — channel monetization policies:
  https://support.google.com/youtube/answer/1311392
- YouTube Help — disclosing use of GenAI content:
  https://support.google.com/youtube/answer/14328491
- YouTube Help — YouTube Partner Program overview & eligibility:
  https://support.google.com/youtube/answer/72851
- Meta — approach to labeling AI-generated and manipulated media (2024):
  https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
- Meta — Rewarding Original Creators on Facebook (13 March 2026):
  https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/
- Instagram Creators best-practices hub:
  https://about.fb.com/news/2024/10/best-practices-education-hub-creators-instagram/
- FTC — Endorsement Guides, 16 CFR Part 255 (updated June 2023).
  Search ftc.gov for "Endorsement Guides" for the current text.
- TikTok — Community Guidelines, AI-generated content section:
  https://www.tiktok.com/community-guidelines/en/

## Troubleshooting

| Problem | What to do |
|---|---|
| The label toggle moved or is missing | Menu wording changes by app version. Search the platform's help centre for the current path; do not guess. If no toggle exists for that platform, disclose in the caption/text. |
| A platform auto-labelled your post "AI info" / "AI modified" | Do not strip metadata to remove it. If the label is wrong, use the platform's appeal/correction flow; otherwise leave it. |
| You cannot confirm monetisation eligibility | Say "eligibility not confirmed" and publish without any income claim. Never fill the gap with a guess. |
| A sponsor wants the disclosure removed or hidden | Refuse. Disclosure is a legal and platform requirement, not a style choice. |
| Unsure whether content is "realistic" enough to label | Label it. Over-disclosure costs nothing (YouTube: disclosure does not limit reach or monetisation); under-disclosure risks removal. |

## Known limits

- Policy claims in this skill were last verified 16 November 2026.
  Platforms change rules without notice — the official references above
  are the source of truth, not this skill.
- This skill is general guidance, not legal advice, and it does not
  cover jurisdiction-specific rules outside the FTC framework (for
  example, EU AI Act transparency duties, which apply from August 2026
  to deepfakes and certain AI-generated public-interest text). If your
  audience is in the EU, check the EU AI Act Article 50 duties
  separately.
- Monetisation figures (thresholds, programme names) are platform-set
  and change. Never quote them from memory in a post — re-check the
  official page on the day you publish.
