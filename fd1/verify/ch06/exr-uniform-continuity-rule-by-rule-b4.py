"""exr-uniform-continuity-rule-by-rule-b4 (Section 6.4): (a) ||x| - |y|| <= |x - y| on a grid;
(b) |x^2 - y^2| <= 6|x - y| on [0, 3]^2 (grid, exact)."""
from fractions import Fraction as F
G = [F(k, 4) for k in range(-40, 41)]
assert all(abs(abs(x) - abs(y)) <= abs(x - y) for x in G for y in G)
H = [F(k, 20) for k in range(0, 61)]
assert all(abs(x * x - y * y) <= 6 * abs(x - y) for x in H for y in H)
assert max(x + y for x in H for y in H) == 6
print("exr-uniform-continuity-rule-by-rule-b4: all quoted values check")
