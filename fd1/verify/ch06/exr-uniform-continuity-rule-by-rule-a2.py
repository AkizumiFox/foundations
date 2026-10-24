"""exr-uniform-continuity-rule-by-rule-a2 (Section 6.4): (g) delta = eps/5 for 5x;
(h) min(1, 1/7) = 1/7; (i) sqrt(17) - 4 = 0.1231 (about 0.123)."""
import math
from fractions import Fraction as F
for eps in [F(1), F(1, 10), F(7, 3)]:
    d = eps / 5
    for k in range(-50, 51):
        x, y = F(k, 3), F(k, 3) + d * F(49, 50)
        assert abs(x - y) < d and abs(5 * x - 5 * y) < eps
assert min(F(1), F(1) / (2 * 3 + 1)) == F(1, 7)
v = math.sqrt(17) - 4
assert round(v, 4) == 0.1231 and round(v, 3) == 0.123
# it works at x = 4 with eps = 1 and nothing larger does
assert abs((4 + v) ** 2 - 16) <= 1 + 1e-9 and (4 + v * 1.001) ** 2 - 16 > 1
print("exr-uniform-continuity-rule-by-rule-a2: all quoted values check")
