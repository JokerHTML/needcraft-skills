# Worked example: sample script record + SEO package

> Example file. The script record below is the worked 10-minute long-form script from the `video-script-retention` skill ("How to brew pour-over coffee at home"). The SEO package is written for it and scored against the rubric in `SKILL.md` Stage 5. Scores are a worked demonstration of the rubric, not measured performance. Replace the topic, title, and tags with your own — this file shows the shape, not content to copy.

## Script record

```json
{
  "title": "How to Brew Pour-Over Coffee at Home",
  "hook": "Your pour-over tastes bitter no matter which beans you buy — the problem is your grind, not the bag.",
  "sections": [
    "Why coffee tastes bitter",
    "Grind size",
    "Water temperature",
    "Pouring technique",
    "What not to do",
    "The honest limit"
  ],
  "cta": "The brew ratio card is in the description — copy it, and use it for your next morning cup.",
  "claims": [
    {
      "text": "Since 24 August 2026 YouTube counts a view from the first frame of playback.",
      "riskLevel": "standard",
      "sourceUrls": ["https://www.clyper.io/guides/youtube-shorts-algorithm"]
    }
  ]
}
```

Note: the claim above is illustrative of the `claims[]` shape. In a real script, claims cite sources from your own source catalog, and this claim would only appear if the video actually made it.

## SEO package

**Title (36 characters):** "How to Brew Pour-Over Coffee at Home"

**Description:**

> Bitter pour-over? It is not the beans. In ten minutes you will brew a cup that tastes sweet, using three numbers you already own.
>
> WHAT YOU'LL LEARN
> - Why coffee turns bitter (and why it rarely means bad beans)
> - Grind size, word for word
> - Water temperature: the one number that matters
> - The pouring technique that keeps the bed level
> - Three mistakes that ruin a cup — and what to do instead
> - The honest limit: when technique cannot help
>
> TIMESTAMPS
> 0:00 Hook — bitter coffee?
> 0:30 Why coffee tastes bitter
> 2:00 Grind size
> 4:30 Water temperature
> 6:30 Pouring technique
> 8:30 The honest limit
> 9:30 Recap and ratio card
>
> ABOUT
> A practical brewing guide for anyone making pour-over coffee at home.
>
> DISCLAIMER
> This video shares a brewing method. Results depend on your beans, your grinder, and your water.

**Tags (12, within the 500-character budget):** pour over coffee, how to brew pour over, coffee brewing guide, pour over tutorial, coffee grind size, water temperature coffee, home coffee brewing, beginner coffee, v60 pour over, coffee tips, brew better coffee, coffee at home

**Hashtags (3):** #Coffee #PourOver #HomeBrewing

**Category:** Education. **Language:** English. **Audience:** Not made for kids.

## SEO score (worked)

| Component | Max | Awarded | Reason |
|---|---|---|---|
| Title | 30 | 26 | Under 100 characters, keyword-first, clear promise; no year token, no power word beyond the promise |
| Description | 40 | 34 | Hook in the first 125 characters, WHAT YOU'LL LEARN, timestamps, about, disclaimer; links section empty (no links for this video) |
| Tags | 30 | 26 | 12 tags, exact keyword first, long-tail covered, all within the 500-character budget |
| **Total** | **100** | **86** | **Pass (≥50). Ship.** |

## Review attestations (example)

- `factChecked: true` — the one claim verified against its source.
- `rightsConfirmed: true` — voiceover only, no music, no third-party clips.
- Synthetic-media flag: NO — no realistic AI-generated or altered content in this video. (If the video had used realistic AI footage, the flag would be YES.)
