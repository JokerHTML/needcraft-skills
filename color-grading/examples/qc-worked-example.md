# QC worked example — real probe output (synthetic palette chart)

This is a real run on a synthetic test chart, performed 2026-11-16 on ffmpeg 8.1.2
(Linux). It demonstrates the QC procedure. The numbers are an illustration of the
procedure on this chart — do NOT copy them as your targets. Your reference row comes
from your own first approved video, on your own content.

## 1. Build the test chart (synthetic input)

A 2-second 1080x1920 chart: dark `#0A0A0C` ground, a cream `#F5F2EA` block, and a
yellow `#FFC933` block.

```bash
ffmpeg -y -v error -f lavfi -i "color=c=0x0A0A0C:s=1080x1920:d=2:r=30" \
 -f lavfi -i "color=c=0xF5F2EA:s=540x960:d=2:r=30" \
 -f lavfi -i "color=c=0xFFC933:s=540x960:d=2:r=30" \
 -filter_complex "[0][1]overlay=270:240[bg];[bg][2]overlay=270:1200[out]" \
 -map "[out]" -c:v libx264 -crf 0 -pix_fmt yuv420p -color_range tv test_input.mp4
```

## 2. Grade it with the master chain

```bash
ffmpeg -y -v error -i test_input.mp4 \
 -vf "deband=1thr=0.02:2thr=0.02:3thr=0.02:4thr=0.02:range=16:blur=1,noise=alls=5:allf=t+u,curves=master='0/0 0.25/0.21 0.5/0.50 0.75/0.79 0.9/0.87 1/0.94':interp=pchip,eq=saturation=1.00,setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709,format=yuv420p" \
 -c:v libx264 -profile:v high -crf 16 -preset slow -movflags +faststart test_graded.mp4
```

## 3. Probe the graded file — real output

Colour tags (ffprobe `-show_entries stream=pix_fmt,color_range,color_space,
color_transfer,color_primaries`):

```
pix_fmt=yuv420p
color_range=tv
color_space=bt709
color_transfer=bt709
color_primaries=bt709
```

Ungraded input, frame 30 (signalstats):

```
frame|tag:lavfi.signalstats.YMIN=25|tag:lavfi.signalstats.YAVG=105.312|tag:lavfi.signalstats.YMAX=224|tag:lavfi.signalstats.SATAVG=16.75|tag:lavfi.signalstats.SATMAX=81
```

Graded output, frame 30 (signalstats):

```
frame|tag:lavfi.signalstats.YMIN=17|tag:lavfi.signalstats.YMAX=217|tag:lavfi.signalstats.YAVG=100.433|tag:lavfi.signalstats.SATAVG=15.9741|tag:lavfi.signalstats.SATMAX=82
```

Yellow-block crop of the graded output (540x960 region over the yellow fill), frame 30:

```
frame|tag:lavfi.signalstats.YMIN=181|tag:lavfi.signalstats.YAVG=191.927|tag:lavfi.signalstats.YMAX=217|tag:lavfi.signalstats.SATAVG=61.9843|tag:lavfi.signalstats.SATMAX=85
```

## 4. What each number means

- **Shoulder works:** `YMAX` fell from 224 (input) to 217 (graded) — below any 255
  plateau. A hard 255 plateau would mean clipped whites.
- **YMIN moved 25 → 17.** The grain stage adds a few code values of spread and the
  curve darkens the low end. This is expected on this chart and is why the skill's pass
  criterion is "stable across the series", not a fixed number. Do not adopt 17 or 25
  as a target.
- **Yellow crop is one tight cluster:** YAVG 191.9 with YMIN 181 and YMAX 217 — a
  single population, so no posterization on this chart. Two separated populations would
  mean the flat fill split into bands.
- **Determinism check:** the ungraded input's frame-30 values were identical across
  repeated probe runs (YMIN=25, YAVG=105.312, SATMAX=81, repeated exactly), which is
  what a deterministic pipeline looks like. Run the same check on your own graded
  output across two builds.

## 5. The setparams finding (verified in this run)

The same grade run WITHOUT `setparams` in the filter chain — using only output-level
`-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv` flags —
produced:

```
color_range=tv
color_space=bt709
color_transfer=unknown
color_primaries=unknown
```

That is a QC-gate FAIL under this skill ("any 'unknown' = FAIL"). Adding `setparams`
inside the filter chain fixed all four tags. This was measured on ffmpeg 8.1.2;
re-verify on your own build, and always trust the ffprobe output, not the command line.
