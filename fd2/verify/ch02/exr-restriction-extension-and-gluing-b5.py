"""exr-restriction-extension-and-gluing-b5: x on (-inf, 0] glued with x^2 on [0, inf):
agreement 0 at 0; injective (across: a < 0 < b^2); surjective (y < 0 -> y, y >= 0 -> sqrt y)."""
from fractions import Fraction as F
import math

QUOTED = {"overlap_value": 0}
g1 = lambda x: x; g2 = lambda x: x * x
assert g1(0) == g2(0) == QUOTED["overlap_value"]
f = lambda x: g1(x) if x <= 0 else g2(x)
grid = [F(k, 20) for k in range(-200, 201)]
vals = [f(x) for x in grid]
assert len(set(vals)) == len(vals)  # injective on the grid
assert all(f(a) < 0 < f(b) for a in grid if a < 0 for b in grid if b > 0)
for k in range(-100, 101):
    y = k / 7
    x = y if y < 0 else math.sqrt(y)
    assert abs((x if x <= 0 else x * x) - y) < 1e-12
print("exr-restriction-extension-and-gluing-b5: all quoted values check")
