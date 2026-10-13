"""exr-uniform-continuity-rule-by-rule-a1 (d): f(x) = 3x + 1, delta = eps/3 works at every x0,
since |f(x0) - f(y)| = 3|x0 - y| < eps."""
from fractions import Fraction as F

QUOTED = {"delta = eps / k, k": 3}
f = lambda t: 3 * t + 1
for eps in [F(1), F(1, 7), F(9)]:
    delta = eps / QUOTED["delta = eps / k, k"]
    for x0 in [F(0), F(-5), F(22, 7)]:
        for k in range(-30, 31):
            y = x0 + delta * F(k, 31)
            assert abs(f(x0) - f(y)) == 3 * abs(x0 - y) < eps
print("exr-uniform-continuity-rule-by-rule-a1: all quoted values check")
