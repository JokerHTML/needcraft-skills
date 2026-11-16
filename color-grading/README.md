# Color Grading (ffmpeg-only)

Grade short-form vertical video with ffmpeg only: one locked chain, frozen into a
versioned Hald LUT, verified numerically.

## What it is

A repeatable final-encode method: render clean, assemble losslessly, grade once with a
locked filter chain (deband, grain, S-curve with a 0.94 highlight shoulder, saturation),
freeze the chain into a Hald LUT for future videos, and verify the delivery file with
ffprobe plus signalstats. It includes a face-cam exception and a worked QC example with
real probe output from a synthetic palette chart.

## Who it is for

An editor or agent doing the final encode of a video built from rendered graphics or
screen content, who wants the same look on every video and a numeric check instead of
eyeballing it.

## How to use

1. Read `SKILL.md` — prerequisites, input spec, master chain, LUT procedure, QC gate.
2. Assemble your edit losslessly (`libx264 -crf 0` or ffv1) at delivery resolution and
   frame rate.
3. Run the master chain at final encode (copy the command from `SKILL.md`; substitute
   your input/output filenames).
4. Run the QC gate commands on the delivery file. All four colour tags must read
   correctly and the signalstats numbers must match your reference row.
5. See `examples/qc-worked-example.md` for the full worked example — the exact commands
   used to build a synthetic test chart, the real probe output, and what each number
   means.

## Example

The QC worked example (`examples/qc-worked-example.md`) shows a real run on ffmpeg
8.1.2: ungraded input `YMIN=25, YMAX=224` → graded output `YMIN=17, YMAX=217`, all four
colour tags reading bt709/tv. Those numbers are an illustration of the procedure on a
synthetic chart, not targets to copy — your reference row comes from your own first
approved video.

## Install

Copy this folder into your skills directory and reference it by name at final encode.
Requires ffmpeg 8.1.2 or later (with ffprobe). No build step, no API key, no account.

## License

MIT — see the license in the skill frontmatter.

## Disclaimer

The chain is tuned for graphics-led short-form video with a dark palette. It does not
colour-correct raw or log camera footage, and the grain/shoulder rationale in the skill
is the author's working rationale, not a cited published finding. ffmpeg behaviour varies
by version — re-verify the colour-tag behaviour on your own build. YouTube bitrate
figures are cited from YouTube's published "recommended upload encoding settings" help
page (https://support.google.com/youtube/answer/1722171), checked 2026-11-16.
