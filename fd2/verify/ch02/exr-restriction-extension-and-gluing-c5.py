"""exr-restriction-extension-and-gluing-c5: pieces [n, n+1) cover R and are disjoint; f(x) = x - n;
range [0, 1); f(x + 1) = f(x); f(0) = 0 = f(1); closed pieces disagree at 1 (values 1 and 0)."""
from fractions import Fraction as F
import math

QUOTED = {"f0": 0, "f1": 0, "closed_at_1": (1, 0)}
grid = [F(k, 12) for k in range(-120, 121)]
for x in grid:
    ns = [n for n in range(-12, 13) if n <= x < n + 1]
    assert ns == [math.floor(x)]  # exactly one piece
f = lambda x: x - math.floor(x)
assert all(0 <= f(x) < 1 for x in grid)
assert all(f(t) == t for t in grid if 0 <= t < 1)
assert all(f(x + 1) == f(x) for x in grid)
assert f(F(0)) == QUOTED["f0"] and f(F(1)) == QUOTED["f1"]
assert (1 - 0, 1 - 1) == QUOTED["closed_at_1"]
assert all(n + 1 <= m for n in range(-10, 10) for m in range(-10, 10) if n < m)
print("exr-restriction-extension-and-gluing-c5: all quoted values check")
