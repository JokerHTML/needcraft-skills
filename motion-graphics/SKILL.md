---
name: motion-graphics
description: >-
  Animate text and graphics in short-form vertical video so every movement
  explains, emphasizes, or guides attention: five locked easing tokens, a
  five-phase build system, stagger and reveal rules, a six-transition grammar,
  camera-move language, and per-scene timing budgets. Use when animating a
  reel, a Short, or any kinetic-typography scene and you need motion that
  serves the story instead of decorating it.
license: MIT
metadata:
  version: 1.0.0
  date: 2026-11-16
  author: Muhammad Saad Ranjha / NeedCraft
---

# Motion Graphics

## What this skill is

A closed motion system for short-form vertical video (1080x1920, 30 fps).
It covers only **how elements move**: easing curves, build phases, layer
discipline, stagger, reveals, transitions, camera language, and timing
budgets. It does not cover scripting, voiceover, colour, or publishing —
bring those from your own pipeline.

Who it is for: an editor or agent animating text and graphics in reels,
Shorts, or kinetic-typography scenes who wants motion that is repeatable
and checkable instead of improvised per scene.

## Prerequisites

- A locked storyboard or beat map: one idea per beat, with a beat grid
  (music beats or a voiceover cue sheet) already measured.
- A voiceover cue sheet for any scene with spoken words:
  `(start_frame, end_frame, text, emphasis)`. Text timing comes from the
  cue sheet, never hardcoded inside draw code.
- A frame-based renderer (this skill was built around PIL frame rendering
  at 30 fps, but the tokens, phases, and budgets are renderer-independent).
- Locked copy: exact words, exact order, before animation starts.

All numbers are 30 fps; 1 frame = 33.3 ms. Durations below are in frames
(`f`).

## House rules (the author's tested practice)

These are house rules from the author's own builds, stated as practice,
not as researched fact. Where a number is a judgment call, it is labelled
as one.

1. **Motion serves the story or it is removed.** If a movement does not
   explain, emphasize, or guide attention, cut it.
2. **Taste as numbers, not adjectives.** Every brief states damping,
   settle time, and stagger in milliseconds or frames — never "smooth" or
   "snappy".
3. **Music first.** The beat grid comes before the storyboard. Something
   lands on every beat for the first 8 seconds; stillness is rationed
   (no hold longer than 1 second; at most one earned ~400 ms absolute
   stillness per film). Moves start ~0.05 s before the beat so they land
   on it.
4. **One formal idea per film (and one per beat).** Three extraordinary
   visual moments beat ten mediocre animations. No effect exists simply
   because it looks cool.
5. **Restraint is the flex.** Banned by default: particle bursts, glows,
   bouncy easing, shockwave rings, RGB split, camera shake, lens flares,
   neon, grid floors, fake HUD numbers, corner labels, and
   brains/robots/neural-net clichés.
6. **Text discipline.** Locked copy before animation. A type system with
   roles (display / grotesque / mono), never one font for everything.
   Content enters after its container starts morphing and leaves before
   the next morph. Captions are designed for sound-off viewing, never
   defaulted.
7. **Series consistency.** Easing tokens stay locked across a series:
   the same token always means the same movement. Brand consistency is
   token consistency.

## The easing tokens (only these — never invent a curve per scene)

Precompute each as a 101-point lookup table at script start (see
`examples/easing_lookup.py`). Reuse across the whole series.

| Token | cubic-bezier | Use | Duration |
|---|---|---|---|
| `enter` | (0.16, 1, 0.3, 1) easeOutExpo | text/graphic entrances | 9–15f (300–500ms) |
| `hero_enter` | (0.05, 0.7, 0.1, 1) Material emphasized-decelerate | the one hero element per scene | 11–15f |
| `move` | (0.65, 0, 0.35, 1) | on-screen moves | 9–12f |
| `exit` | (0.7, 0, 0.84, 0) ease-in | exits — always 30–50% SHORTER than the entrance | 6–9f |
| `pop` | easeOutBack, s=1.70158 (~10% overshoot) | badges, keywords, numbers, prices ONLY | 9–14f |

- `ease_out_back(t, s)`: `u = t - 1; return 1 + (s+1)*u**3 + s*u**2`.
  Hero word only: s=2.2 (~15% overshoot). Clamp the final frame exactly
  to target (no 1 px jitter).
- NEVER overshoot a large panel/card — wobble on a big surface reads
  sloppy.
- NEVER animate scale from 0% — scale-land is 95%→100% + fade.
- Duration-based easing only. No per-frame physics integration (springs
  drift and break voiceover sync); bake any spring feel into the lookup
  table.

## The build system (every hero element, in order)

1. **Anticipation:** 2–4f counter-move, 5–8% in the opposite direction
   (dip 8–12 px or scale 0.95).
2. **Main action:** 8–12f on `enter` / `hero_enter`.
3. **Overshoot:** pass the rest point by 6–10 px (or scale 1.03–1.08),
   2–3f — via `pop` or the phase list.
4. **Settle:** 3–6f decaying to exact rest.
5. **Hold:** ≥12–18f still before the next idea. Total hero build
   ≈18–24f.

Implement as a phase list per element, sampled per global frame, e.g.
`[(3, 0, -10, enter), (10, -10, +8, enter), (5, +8, 0, enter)]`
— (frames, from_y, to_y, token). A single Back curve cannot
anticipate — use phases when anticipation matters.

## Layer discipline

- **Primary/Hero:** full amplitude, smoothest ease, lands first.
- **Secondary/Support:** 30–50% amplitude, lag **+2–3f** behind primary
  (follow-through), 60–70% of primary duration. Every layer has its OWN
  `delay_frames` + `duration_frames` — never one global `t`.
- **Ambient:** slow sine drift only (`offset = 3*sin(f*0.03 + phase)` px),
  <10% change, loops.
- **Simultaneity cap:** with 3+ elements, ≤⅓ in active motion on any
  frame; delay lowest-rank elements 2f to enforce.
- **Distance cap:** no element travels >⅓ of screen without an
  intermediate keyframe / scale / opacity change (long unbroken slides
  read as template motion).

## Stagger (lists, bullets, checklist builds)

- Offset **2f per item** (3f for slow/premium builds, 1f for dense
  grids).
- Per item: fade + translateY 12–20 px + `enter`. Line builds overlap:
  next line starts when the previous is ~70% done.
- **Whole-group reveal capped at 18–24f.** If count × stagger > cap,
  shrink the stagger — never extend the total.

## Reveals (prefer clipping over fading)

- **Baseline mask rise** (the premium editorial look): text rises from
  behind its line mask, 10–14f on `enter`, 0 rotation. In PIL, per-frame
  `crop()` IS the matte — `clip_h = int(line_h * ease(t))`, paste the
  slice into a fixed clip box.
- **Mask wipe L→R:** 12–18f ease-in-out, feather the matte edge 2–4 px
  (hard edge = cheap).
- **Squash & stretch:** landing squash scaleY 0.92–0.95 / scaleX
  1.05–1.08 (`sx*sy ≈ 1`), recover 4–6f on `pop`; fast travel stretches
  1.05–1.12 along motion direction at peak velocity; numbers squash ONCE
  on the final value landing.
- **Arcs:** add a perpendicular sine bulge of 5–10% of travel distance
  at the path midpoint (`y += amp*sin(pi*t)`). Straight-line organic
  motion reads mechanical.

## Transitions (grammar of six — hard cut is the default)

1. **Hard cut — 0f.** The default. Fast action, beat re-timing,
   viewpoint change.
2. **Cut on action:** cut at peak velocity; motion continues across the
   cut. Match motion DIRECTION across every cut so the eye never resets.
3. **Match cut:** hero shape at identical `(cx, cy, bbox_w)` on both
   sides; slow→fast→slow, cut at the fastest point. Just cut — no
   transition frames.
4. **Dissolve — 12–24f, RARE:** time passing / location change only.
5. **Infinite zoom:** scale 1.0→3.0+ over 20–30f through a sub-frame
   (window / screen / logo shape); never stop zooming between scenes.
   In PIL: shrink the centre crop box per frame, resize back to full
   canvas.
6. **Morph — 15–24f:** same-fill shapes only, logo/icon
   transformations; interpolate polygon vertices (same vertex count);
   text→shape ≈ 8f cross-dissolve while scaling.

Whip pan: 6–10f blur + horizontal stretch, direction matched both
sides, 3f either side of the cut.

**Cut test (mandatory):** if a transition cannot answer "what does this
shot give me the last one didn't?" — hard cut on the beat / motion peak
instead.

## Camera language

Every storyboard names ONE camera move per beat — never "zoom in a bit".
A move must earn its place via PURPOSE: EXPLAIN / EMPHASIZE / TRANSITION
/ RESET / EMOTE / PROVE / CLARIFY. One beat = one move = one idea; moves
land ON the beat, starting ~0.05 s early.

### The 24 essential moves for vertical educational reels

| Beat role | Move | Easing token | 2D implementation |
|---|---|---|---|
| HOOK (0–1 s) | `/impact zoom` or `/fast push` | `pop` | scale ramp |
| LOCK-IN | `/slow push` | `move` | scale 1.00→1.06 |
| New idea / transition | `/whip pan` (+ directional blur) | `exit`→`enter` | translate + blur |
| Vertical energy shift | `/whip tilt` | `exit`→`enter` | translate + blur |
| Reveal the payoff | `/dolly out` / `/cinematic pullback` | `move` | scale 1.06→1.00 |
| Emphasize a word/stat | `/dolly in` / `/push in` | `hero_enter` | scale + hold |
| Shift between 2 ideas | `/rack focus` (blur ramp A→B) | `move` | blur ramp layers |
| Depth / premium feel | `/parallax move` (2–3 layers, different speeds) | `move` | multi-layer |
| Scene drift / life | `/micro shake` (seeded, deterministic) | — | ±2 px noise |
| Lateral comparison | `/truck left` / `/truck right` | `move` | translate |
| Before → after | `/pan left` / `/pan right` | `move` | translate |
| Vertical list scroll | `/pedestal up` / `/pedestal down` | `move` | vertical translate |
| Grand reveal | `/crane reveal` (simulate: scale + rise) | `hero_enter` | scale + translate |
| CTA resolve | `/pull back` → settle | `exit` | scale down, hold |
| Speed contrast | `/speed ramp` (slow→fast on the beat) | — | frame remap |
| Settle / breathe | `/smooth glide` or `/floating camera` | `move` | slow drift |
| Stylized beat | `/dutch angle` (≤8°, brief) | `pop` | rotate |
| Loop energy | `/accelerate` into loop point | `enter` | ease ramp |

BANNED as decoration (still banned): `/camera shake`, `/dramatic
shake`, `/360 spin` as filler, `/epic shot` without a payoff, any orbit
needing true 3D in a 2D pipeline. True-3D moves (`/orbit 360`,
`/drone fly`, crane arcs) are reserved for AI-video-generated segments —
never faked badly in 2D.

Camera gotchas:

- Whip moves NEED motion blur or they read as glitches — directional
  blur along the travel axis.
- Never two moves in one beat. One beat = one move = one idea.
- The camera serves the voiceover/text — moves land ON the beat/phrase,
  starting ~0.05 s early.
- Rack-focus blur ramps must be symmetric in duration (out = in) or the
  cut feels cheap.

## Timing budgets (per scene, non-negotiable)

- Scene frame budget = `build (12–18f) + HOLD (≥ word_count × 15f) +
  exit (6–9f)`. Frames running short? Steal from build/exit — **NEVER
  from hold**.
- Reading floor: an information-bearing word gets ≥9f on screen.
  On-screen informational text runs at roughly **60–90 wpm** (author's
  tested practice) even when the voiceover runs ~150 wpm — show phrases,
  not every spoken word.
- The reel's final phrase holds a full beat longer than any other hold.

## Quality rules

- One focal element animates first; entrance order = reading order.
- Animate hook + emphasis words only. If every word does a backflip,
  nothing stands out.
- Exits leave in the direction motion was heading; never reversed; never
  the entrance ease played backwards.
- Text timing comes from the VO cue sheet — never hardcoded inside draw
  code.
- Motion that draws attention to itself instead of the idea = defect.
  REJECT → simplify → re-render.

## Worked example — hook scene (90 frames, 30 fps)

**Brief.** A 3-second hook for a vertical reel. Locked copy: hero line
"STOP GUESSING." (2 words), support line "Test one idea a week."
(5 words), one stat badge "3 tests". Beat grid: 120 BPM, beat every
15f. Camera: `/impact zoom` on the hero, then `/slow push` lock-in.

**Phase lists.**

- Hero "STOP GUESSING." (primary, `hero_enter`, starts f0):
  `[(3, 0, -10, enter), (11, -10, +6, hero_enter), (4, +6, 0, enter)]`
  — anticipate 3f, main action 11f, settle 4f. Rest at f18.
- Support line (secondary, `enter`, delay +3f, 60% duration):
  `[(3, 0, -8, enter), (8, -8, +4, enter), (4, +4, 0, enter)]`
  — starts f3, rest at f18.
- Stat badge "3 tests" (badge, `pop`, delay +6f):
  `[(9, scale 0.95→1.03, pop), (4, scale 1.03→1.00, enter)]`
  — starts f6, rest at f19. Overshoot is on the badge only, never on
  the hero line or any large panel.

**Timing budget.** Build 18f + hold: hero 2 words × 15f = 30f (support
line 5 words × 15f = 75f governs — the scene holds until the longest
line has had its floor) + exit 6f on `exit` = 18 + 75 + 6 = 99f.
The 90f slot is 9f short: steal 6f from build (tighter anticipate) and
3f from exit — never from hold. Final: build 12f, hold 75f, exit 3f…
no — exit floor is 6f, so the honest fix is to extend the scene to 99f
or cut the support line to 4 words (60f hold → 18 + 60 + 6 = 84f, fits
in 90f with 6f slack). Cut the word; do not steal from hold.

**Verification.** Spot-check frames: f3 (anticipation dip −10 px on
hero), f14 (peak overshoot +6 px), f18 (settle = exact rest), f10
(mid-stagger: support line mid-rise). Count moving elements on 5 random
frames: ≤⅓ of elements in motion. Hold check from the cue sheet:
support line visible ≥75f.

## Failure modes

- Everything stopping on the same frame → add follow-through lags
  (+2–3f per layer).
- Group reveal overrunning → shrink stagger, cap 24f.
- Wobble on panels → `pop` was applied to a large surface; switch to
  `enter` at 95%→100%.
- Motion feels "template" → check distance cap, simultaneity cap, and
  whether easing tokens were replaced with ad-hoc curves.

## Verification

- Spot-check rendered frames at: anticipation frame, peak-overshoot
  frame, settle frame, mid-stagger frame — values must match the phase
  list exactly.
- Count simultaneously-moving elements on 5 random frames: ≤⅓.
- Every scene's hold ≥ word_count × 15f — verify from the cue sheet,
  not by eye.

## Stop conditions

- Stop if a scene needs a 7th transition type or a new easing curve to
  work — the scene concept is wrong, not the toolbox. Rebuild the
  scene.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Motion drifts out of sync with voiceover | Per-frame physics or a global `t` | Duration-based easing from the cue sheet; per-layer delay/duration |
| 1 px jitter on rest frames | Final frame not clamped | Clamp the last lookup-table entry exactly to target |
| Wobble on a card/panel | `pop` on a large surface | `enter` at 95%→100% instead |
| Scene feels rushed | Hold stolen to fit the budget | Steal from build/exit only; or cut words |
| Two moves fighting in one beat | Beat has two camera moves | One beat = one move; pick the one that serves the idea |

## Known limits

- 30 fps only. At 24 or 60 fps, convert frame counts by duration in
  milliseconds (1f = 33.3 ms at 30 fps), not by copying frame numbers.
- The wpm and token-percentage figures are the author's tested practice
  on their own builds, not measured research — treat them as starting
  points and adjust to your own footage.
- This skill assumes a deterministic frame renderer. In a real-time
  engine (CSS/JS animation), implement the same tokens as cubic-bezier
  curves and the same phase lists as keyframe sequences.
