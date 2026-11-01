"""prp-floor-rules (a)-(h) on many rationals; Quick check 2 (floor(floor(7.5)/2) = 3 = floor(3.75));
the stages example floor(floor(17/3)/2) = 2 = floor(17/6); the two-stage corollary."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, ceil, rationals
QUOTED = {"qc2": (3, 3), "stages": (2, 2)}
xs = rationals()
ys = rationals(seed=9)
for x, y in zip(xs, ys):
    m = floor(x)
    isint = x.denominator == 1
    assert x - 1 < m <= x and ((m == x) == isint)                       # (a)
    for n in (-5, -1, 0, 2, 7):
        assert floor(x + n) == m + n                                     # (b)
    assert (x <= y) <= (floor(x) <= floor(y))                            # (c)
    assert m + floor(y) <= floor(x + y) <= m + floor(y) + 1              # (d)
    assert floor(-x) == (-m if isint else -m - 1)                        # (e)
    c = ceil(x)
    assert c - 1 < x <= c and [k for k in range(c - 3, c + 4) if k - 1 < x <= k] == [c]  # (f)
    for j in range(m - 4, m + 5):
        assert (j <= x) == (j <= m)                                      # (g)
    for k in (1, 2, 3, 7, 10):
        assert floor(F(m, k)) == floor(x / k)                            # (h)
        for l in (1, 2, 5):
            assert floor(F(floor(x / k), l)) == floor(x / (k * l))
assert (floor(F(floor(F(15, 2)), 2)), floor(F(15, 4))) == QUOTED["qc2"]
assert (floor(F(floor(F(17, 3)), 2)), floor(F(17, 6))) == QUOTED["stages"]
print("prp-floor-rules: OK")
