# Motion Graphics

Animate text and graphics in short-form vertical video so every movement
explains, emphasizes, or guides attention.

## What it is

A closed motion system for 1080x1920, 30 fps reels and Shorts: five locked
easing tokens, a five-phase build system (anticipate → act → overshoot →
settle → hold), layer discipline, stagger rules, clip-based reveals, a
six-transition grammar, a 24-move camera language, and per-scene timing
budgets. The playbook principles and camera moves are inlined — there are
no external files to fetch.

## Who it is for

Editors and agents animating text and graphics in short-form video who want
motion that is repeatable and checkable instead of improvised per scene.

## Install

Copy this folder into your skills directory (for example, your
Claude Code skills folder) as `motion-graphics/`. No dependencies beyond
Python 3 (standard library only) for the lookup-table example.

## How to use

1. Lock the copy and the beat grid first (music beats or a voiceover cue
   sheet). Motion is built on top of those, never before them.
2. Pick one easing token per element from the table in `SKILL.md` — never
   invent a curve per scene.
3. Write a phase list per hero element (anticipation, main action,
   overshoot, settle, hold).
4. Name one camera move per beat from the 24-move table.
5. Check the timing budget: build + hold (≥ words × 15 frames) + exit.
   Steal from build/exit when short — never from hold.
6. Verify: spot-check the anticipation, overshoot, settle, and mid-stagger
   frames against the phase list.

## Example

`SKILL.md` contains a complete worked example: a 90-frame hook scene
("STOP GUESSING.") with phase lists, a timing budget, and the verification
steps. `examples/easing_lookup.py` precomputes the five tokens as
101-point lookup tables — run it with `python3 easing_lookup.py`.

## License

MIT. See `SKILL.md` frontmatter.

## Disclaimer

The timing figures (words-per-minute, token percentages, frame counts) are
the author's tested practice on their own builds, not measured research.
Treat them as starting points and adjust to your own footage.
