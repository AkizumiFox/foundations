"""exr-set-operations-b2: witnesses for the three families indexed by t > 0."""
from fractions import Fraction as F
QUOTED = {}
pts = [F(n, 13) for n in range(-100, 101)]
for x in pts:
    # (a) union (0, inf): t = x; intersection empty: t = |x| + 1 excludes x
    if x > 0:
        assert x <= x <= 1 + x
    t = abs(x) + 1
    assert not (t <= x <= 1 + t)
    # (b) union R: t = 1 - x (x <= 0), t = 1/(2x) (x > 0)
    if x <= 0:
        t = 1 - x
        assert t > 0 and -t < x < 1 / t
    else:
        t = 1 / (2 * x)
        assert t > 0 and -t < x < 1 / t
    # (b) intersection {0}
    if x < 0:
        t = -x
        assert not (-t < x < 1 / t)
    if x > 0:
        t = 1 / x
        assert not (-t < x < 1 / t)
    # (c) union (0, inf): t = 2x/3
    if x > 0:
        t = 2 * x / 3
        assert t < x < 2 * t
    # (c) C_1 and C_2 disjoint
    assert not (1 < x < 2 and 2 < x < 4)
assert all(-t < 0 < 1 / t for t in [F(k, 7) for k in range(1, 60)])
print("exr-set-operations-b2: all quoted values check")
