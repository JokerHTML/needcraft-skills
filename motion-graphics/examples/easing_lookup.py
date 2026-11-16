"""Precompute the five motion-graphics easing tokens as 101-point lookup
tables, then sample them per frame. Pure standard library; run with
`python3 easing_lookup.py`.

Cubic-bezier tokens are sampled by solving the bezier x(t) for the given
progress and returning y. For the `pop` token the easeOutBack formula is
used directly.
"""

# (x1, y1, x2, y2) control points for the cubic-bezier tokens.
TOKENS = {
    "enter": (0.16, 1.0, 0.30, 1.0),
    "hero_enter": (0.05, 0.7, 0.10, 1.0),
    "move": (0.65, 0.0, 0.35, 1.0),
    "exit": (0.70, 0.0, 0.84, 0.0),
}

N = 101  # lookup points: index 0..100 maps to progress 0.0..1.0


def _bezier_component(t, p1, p2):
    """One component of a cubic bezier with endpoints 0 and 1."""
    return 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3


def _sample_bezier(x1, y1, x2, y2, progress):
    """Return eased value for linear `progress` in [0, 1]."""
    lo, hi = 0.0, 1.0
    for _ in range(24):  # bisection on x(t) == progress
        mid = (lo + hi) / 2
        if _bezier_component(mid, x1, x2) < progress:
            lo = mid
        else:
            hi = mid
    return _bezier_component((lo + hi) / 2, y1, y2)


def ease_out_back(t, s=1.70158):
    """Back easing: overshoots, then settles. t in [0, 1]."""
    u = t - 1
    return 1 + (s + 1) * u ** 3 + s * u ** 2


def build_tables():
    """Return {token: [101 floats]} with the last entry clamped to 1.0."""
    tables = {}
    for name, (x1, y1, x2, y2) in TOKENS.items():
        table = [_sample_bezier(x1, y1, x2, y2, i / (N - 1))
                 for i in range(N)]
        table[-1] = 1.0  # clamp: no 1px jitter on the rest frame
        tables[name] = table
    pop = [ease_out_back(i / (N - 1)) for i in range(N)]
    pop[-1] = 1.0
    tables["pop"] = pop
    return tables


def sample(table, progress):
    """Sample a lookup table at linear progress in [0, 1]."""
    progress = min(max(progress, 0.0), 1.0)
    pos = progress * (N - 1)
    i = int(pos)
    if i >= N - 1:
        return table[-1]
    frac = pos - i
    return table[i] * (1 - frac) + table[i + 1] * frac


if __name__ == "__main__":
    tables = build_tables()
    for name, table in tables.items():
        print(f"{name:11} t=0.00 -> {table[0]:.3f}  "
              f"t=0.50 -> {table[50]:.3f}  t=1.00 -> {table[-1]:.3f}")
    # Example: hero element rising 10px over 11 frames on hero_enter.
    hero = tables["hero_enter"]
    print("hero_enter y-offsets, 11 frames, 0 -> -10px:")
    print([round(-10 * sample(hero, f / 10), 1) for f in range(11)])
