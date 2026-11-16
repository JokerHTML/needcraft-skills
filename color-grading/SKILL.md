---
name: color-grading
description: >-
  Grade short-form vertical video with ffmpeg only: one locked chain (deband, grain, S-curve
  with a 0.94 highlight shoulder, saturation), frozen into a versioned Hald LUT, with a numeric
  QC gate (ffprobe plus signalstats) and a face-cam exception. Use at the final encode of a
  video, after the edit is assembled losslessly and before delivery.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Color Grading (ffmpeg-only)

## What this skill is

A repeatable way to grade short-form video identically every time, using only ffmpeg: one
locked filter chain, applied once at the final encode, frozen into a versioned Hald LUT, and
verified numerically — so the look survives platform re-encoding instead of washing out.

Who it is for: an editor or agent doing the final encode of a video built from rendered
graphics or screen content. It assumes a lossless assembled intermediate exists. It does
not colour-correct raw camera footage and it does not replace a colourist's judgement on
photographic material.

## Prerequisites

- **ffmpeg 8.1.2 or later** (with ffprobe). The worked example in this skill was run on
  ffmpeg 8.1.2 on Linux. Older versions may behave differently — in particular, see the
  note in "Delivery target" about colour tags not sticking with output-level flags.
- **A lossless assembled intermediate** meeting the input spec below.
- A palette chart or test frame (a still image of your palette's flat fills) for the first
  LUT validation.
- Enough disk for one lossless intermediate plus the graded delivery file.

## Input spec (what the assembled file must be)

The chain grades a finished edit, not raw clips. Before you grade, the assembled file
must be:

- **Resolution:** your delivery resolution (this skill's examples use 1080x1920 vertical).
- **Frame rate:** your delivery frame rate (examples use 30 fps). Match the source rate;
  never conform the frame rate at the grade step.
- **Codec:** lossless — `libx264 -crf 0` or ffv1. Never grade a lossy intermediate; a
  grade baked onto compression artefacts cannot be undone.
- **Colour:** palette-exact frames, ungraded. Grain goes ONLY into background layers at
  render time; text layers stay clean.
- **Range:** full-range RGB source material converted to limited-range YUV at assembly,
  or a render that already carries correct limited-range tags. If you are unsure, check
  with ffprobe before grading — a range mismatch at this stage is a re-render, not a
  grade fix.

## The architecture (never deviate)

1. **Render clean** — palette-exact frames, ungraded.
2. **Assemble losslessly** — `libx264 -crf 0` (or ffv1 for archive). Never grade a lossy
   intermediate.
3. **Grade ONCE, at final encode**, with the master chain below — one transform, identical
   on every frame.
4. **Verify numerically** (QC gate below) and file the probe output next to the encode
   command.

Photographic inserts that need correction are pre-graded **on the asset alone** before
assembly — never by unlocking the master chain. A look change = a new LUT version (see
"The LUT") from the next video, never retro-applied mid-series.

## Worked example palette

The examples in this skill use one dark editorial palette as the worked example. Substitute
your own colours; the chain logic is the same.

- Dark ground `#0A0A0C` (luma about 10 full-range / about 25 limited-range)
- Soft white `#F5F2EA` (luma about 243 / about 225)
- Yellow `#FFC933` (red channel at the 255 ceiling; luma about 202 / about 189)

The numbers above are the palette's own RGB-to-luma conversions, not measurements of a
graded file. Your graded file's measured values will differ — see the QC worked example.

## The master chain

```bash
ffmpeg -i assembled_lossless.mp4 \
 -vf "deband=1thr=0.02:2thr=0.02:3thr=0.02:4thr=0.02:range=16:blur=1,noise=alls=5:allf=t+u,curves=master='0/0 0.25/0.21 0.5/0.50 0.75/0.79 0.9/0.87 1/0.94':interp=pchip,eq=saturation=1.00,setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709,format=yuv420p" \
 -c:v libx264 -profile:v high -crf 16 -preset slow \
 -movflags +faststart out_1080x1920.mp4
```

Why each stage exists (the author's working rationale for the design — see "Known limits"
for what is and is not established fact):

- **deband** (low thresholds only — high values eat thin text strokes): replaces banded
  pixels before the encoder sees them.
- **noise alls=5, allf=t+u:** a small amount of grain, there for the encoder, not the
  viewer — it must be invisible at phone size. The working rationale is that grain gives
  the encoder texture to spend bits on in near-black areas instead of collapsing them
  into flat blocks. Never use `gradfun` before lossy compression: it is documented as
  playback-only, and compression removes its dither, so the bands return.
- **curves (master, pchip):** the S-curve — midtone contrast from the middle slope;
  `interp=pchip` because the default spline can overshoot and clip. The **0.9/0.87 to
  1/0.94 shoulder** caps whites at about 94% so soft white never hard-clips or merges
  into a flat block after re-encode. Master curve only — per-channel S-curves shift hue
  in saturated areas.
- **eq saturation=1.00:** the palette is already final; saturation is a correction here,
  not a look (working band 0.92–1.05, default 1.00). Saturation always sits BEFORE the
  final shoulder logic — the shoulder is the last thing touching channel ceilings.
- **setparams (in the filter chain):** sets the colour tags on the frames themselves.
  This matters: on ffmpeg 8.1.2, output-level flags (`-color_trc bt709` etc.) did NOT
  stick — a test encode showed `color_space=bt709` but `color_transfer=unknown` and
  `color_primaries=unknown`. Adding `setparams` inside the filter chain produced all
  four tags correctly (verified 2026-11-16, see the QC worked example). Always verify
  with ffprobe on your own build; do not trust the command line alone.

## Hard rules

- **Blacks stay anchored for graphics.** `0/0` — never lift the dark ground globally
  (a lifted variant such as `0/0.05 …` is for photographic looks only). Washed-out
  blacks are fixed by grain and correct range tags, never by lifting.
- **Range integrity:** limited/tv in the tag AND in reality. A full-range file tagged tv
  (crushed blacks) or limited content tagged pc (washed out) = fail, re-encode.
- **The yellow is never boosted.** In the example palette, `#FFC933` has red at 255: any
  saturation increase clips red while green/blue move, so the hue slides and flat fills
  posterize. If yellow still clips after the chain, the approved fallback is the
  per-channel endpoint pull — `curves=r='0/0 1/0.97':g='0/0 1/0.95':b='0/0 1/1'` —
  which REDEFINES the delivered yellow and needs one-time human approval before
  becoming the standard.
- **Vibrance discipline:** pure-graphic videos keep `vibrance` at 0 (nothing muted to
  rescue, everything to clip). Mixed/photo videos may use
  `vibrance=intensity=0.10–0.30`. Before relying on vibrance, run the palette-strip test:
  crop a saturated swatch and a muted swatch, compare `signalstats` before and after —
  the saturated swatch's SATAVG must move LESS than the muted swatch's; equal movement
  means vibrance buys nothing, so use saturation only. Never `alternate=1` (it changes
  hues).
- **Text edges are built in luma, not hue (a render rule the grade cannot fix):**
  delivery is 4:2:0 — chroma is quarter-resolution, so colour-only edges smear and no
  bitrate fixes it. Light text on a dark ground (large brightness difference) is safe.
  **Yellow on soft white is forbidden for small text** in the example palette — the
  brightness difference is too small; re-render, never re-grade. Accent-coloured text
  strokes should be at least 3–4 px at 1080 wide. Luma-only sharpening
  (`unsharp=5:5:0.3:5:5:0.0`) is the only sanctioned encode-side mitigation; skip it
  if it halos.

## The LUT (series lock)

Once the master chain is approved on a test video, freeze it into a Hald CLUT and grade
future videos with that single file:

```bash
# Build once:
ffmpeg -f lavfi -i haldclutsrc=8 -vf "curves=master='0/0 0.25/0.21 0.5/0.50 0.75/0.79 1/0.94',eq=saturation=1.00" -frames:v 1 grade_hald_v1.png
# Apply (lossless intermediates only):
ffmpeg -i in.mp4 -i grade_hald_v1.png -filter_complex "[0][1]haldclut=interp=tetrahedral" -c:v libx264 out.mp4
```

- Name and date every LUT version; never edit one in place. A look change is a new file
  (`grade_hald_v2.png`, …), never an overwrite.
- LUTs are dumb maps (no scene adaptation) that bake in any clipping — that is why the
  chain is approved BEFORE freezing.
- Validate each new LUT on a palette chart: graded swatches must match the direct chain
  within ±1 code value, else regenerate at a larger Hald level.
- No LUT intensity slider exists in lut3d/haldclut — fading a LUT means blending
  graded/ungraded streams deliberately; do not improvise it per video.

## Delivery target

Rec.709, 8-bit SDR, H.264, yuv420p, **color_range tv**, all four colour tags present
(space, transfer, primaries, range). Every platform re-encodes, so the same file defends
all of them.

YouTube's published reference (checked 2026-11-16): "YouTube recommended upload encoding
settings", https://support.google.com/youtube/answer/1722171 — MP4 container, H.264 High
Profile, 4:2:0 chroma, BT.709 for SDR, and recommended video bitrates of 8 Mbps for 1080p
at 24–30 fps and 12 Mbps at 48–60 fps. Those are recommendations for the file you upload,
not a guarantee about what viewers see — YouTube re-encodes every upload. An oversize
upload master is a signal-quality tactic, not a promise; verify per platform.

## Face exception (face-cam inserts only — skip entirely for graphics videos)

Graphics videos have no skin: add NO skin step, and never dull the accent colour to solve
a problem the video does not have. For face inserts, ffmpeg has no skin qualifier and no
hue-selective tool, so the only defence is order plus restraint: white-balance FIRST with
small `colorbalance` moves (±0.05), saturation LAST and at most 1.05, prefer vibrance
over saturation.

### Worked example — face insert (illustrative procedure)

Suppose a face-cam insert reads too cool (blue) after assembly. The correction, applied
to the insert asset alone BEFORE assembly, is:

```bash
ffmpeg -i face_insert_raw.mp4 \
 -vf "colorbalance=rs=0.03:gs=0.01:bs=-0.03,vibrance=intensity=0.15,eq=saturation=1.02" \
 -c:v libx264 -crf 0 -pix_fmt yuv420p face_insert_balanced.mp4
```

- Each `colorbalance` move stays within ±0.05. Larger moves shift the whole image, not
  just skin.
- Saturation is last and stays at or below 1.05.
- QC: `histogram=mode=color2` — the skin cluster's angle must not move between the
  balanced and final frames; only its distance from centre may change. If the angle
  moves, a stage is shifting hue: reduce the saturation stage first.
- The graded master chain then runs on the assembled video exactly as usual. The face
  exception never changes the master chain.

## Numeric QC gate (delivery file, every video)

```bash
ffprobe -show_streams out.mp4   # must show bt709 / bt709 / bt709 / color_range=tv — any "unknown" = FAIL
ffprobe -f lavfi "movie=out.mp4,signalstats" -show_entries frame_tags=lavfi.signalstats.YMIN,lavfi.signalstats.YMAX,lavfi.signalstats.YAVG,lavfi.signalstats.SATAVG,lavfi.signalstats.SATMAX -of compact
ffmpeg -i out.mp4 -vf "signalstats=out=brng:color=red" -f null -   # out-of-range overlay population must be zero/unexplained-free
```

Pass criteria (the reference row is set once from YOUR first approved video, then held):

- `YMIN` stable across the series (a limited-range encode; the exact value depends on
  your darkest content and the grain stage — see the worked example).
- `YMAX` below the hard 255 plateau — the shoulder cap; a hard 255 plateau from the
  white = clipped = FAIL.
- `YHIGH` measurably below `YMAX` (a gap means the shoulder exists; equal means a
  clipped plateau = FAIL).
- `SATMAX` stable video-to-video within a small tolerance; a jump = a saturation/LUT
  fault.
- A flat-fill crop of your accent colour = a single tight signalstats cluster (two
  populations = posterization = FAIL).
- Determinism: the same test video through the chain on two builds gives bit-identical
  `YAVG` / `SATAVG` / `YMIN` / `YMAX`.

### Worked example — real probe output (synthetic palette chart)

This is a real run, not a target. On 2026-11-16 a synthetic 2-second 1080x1920 test
chart was built with ffmpeg (dark `#0A0A0C` ground, cream `#F5F2EA` block, yellow
`#FFC933` block), encoded losslessly, graded with the master chain above (ffmpeg 8.1.2),
and probed. The full procedure and commands are in
`examples/qc-worked-example.md`. Results for frame 30:

Ungraded input:

```
frame|tag:lavfi.signalstats.YMIN=25|tag:lavfi.signalstats.YAVG=105.312|tag:lavfi.signalstats.YMAX=224|tag:lavfi.signalstats.SATAVG=16.75|tag:lavfi.signalstats.SATMAX=81
```

Graded output (master chain with `setparams` in the filter chain):

```
frame|tag:lavfi.signalstats.YMIN=17|tag:lavfi.signalstats.YMAX=217|tag:lavfi.signalstats.YAVG=100.433|tag:lavfi.signalstats.SATAVG=15.9741|tag:lavfi.signalstats.SATMAX=82
```

Yellow-block crop of the graded output (540x960 region over the yellow fill):

```
frame|tag:lavfi.signalstats.YMIN=181|tag:lavfi.signalstats.YAVG=191.927|tag:lavfi.signalstats.YMAX=217|tag:lavfi.signalstats.SATAVG=61.9843|tag:lavfi.signalstats.SATMAX=85
```

Colour tags on the graded file (ffprobe `-show_entries stream=...`):

```
pix_fmt=yuv420p
color_range=tv
color_space=bt709
color_transfer=bt709
color_primaries=bt709
```

What this example shows — and what it does not:

- The shoulder works: `YMAX` fell from 224 to 217, below any 255 plateau.
- `YMIN` fell from 25 to 17 after grading. That is the grain stage (noise adds a few
  code values of spread) plus the curve darkening the low end — it is NOT a failure of
  the "blacks anchored" rule, and it is why the pass criterion says "stable across the
  series", not a fixed number. Do NOT copy 17 or 25 as your target: set your reference
  row from your own first approved video, on your own content.
- The yellow crop is a single tight cluster (YAVG 191.9, YMIN 181, YMAX 217) — no
  second population, so no posterization on this chart.
- The same run WITHOUT `setparams` left `color_transfer=unknown` and
  `color_primaries=unknown` on ffmpeg 8.1.2 even though output-level `-color_trc` /
  `-color_primaries` flags were passed. That is why the chain puts `setparams` in the
  filter chain.
- A synthetic flat chart is the easiest possible input. Real footage will measure
  differently; the procedure is the transferable part, not these numbers.

## Failure modes

- Washed-out blacks after upload → check range tags first (tagging, not grading), then
  grain presence.
- Banding in gradients → deband thresholds or noise too low; verify on the ENCODED file
  on a non-OLED screen, never the master.
- Yellow gone green/pale → a saturation stage ran after (or inside) the chain; remove
  it — the accent colour is never boosted.
- Haloed text → remove the unsharp stage.

## Stop conditions

- Stop and re-render if the QC gate fails twice on the same file — the input render is
  wrong (clipped at render cannot be recovered by any grade). Re-render, do not re-grade.
- Stop if any colour tag reads "unknown" after the `setparams` fix — the file is not
  deliverable until all four tags read correctly.

## Known limits

- The grain and shoulder mechanisms in "Why each stage exists" are the author's working
  rationale for the chain design, based on the behaviour observed while building it.
  They are not cited findings from a published study. What is established is the
  procedure and the measurements it produces on your own files.
- The chain is tuned for graphics-led short-form video with a dark palette. Photographic
  or log footage needs its own correction before assembly; this chain will not fix it.
- ffmpeg behaviour varies by version. The `setparams` finding and the probe values above
  were measured on ffmpeg 8.1.2 (2026-11-16). Re-verify the tag behaviour on your own
  build before trusting it.
- CRF 16 at 1080x1920 is the chain's default. If your platform's recommended upload
  bitrate (see "Delivery target") implies a different operating point, adjust the CRF
  and re-run the QC gate — do not assume the numbers transfer.
