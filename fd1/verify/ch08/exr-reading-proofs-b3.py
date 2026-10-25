"""exr-reading-proofs-b3 (Section 8.4): x^3 - 3x + 2 = (x - 1)^2 (x + 2) (exact, at 1201 rational points: both sides are cubics); the claim
x^3 + 2 >= 3x on a grid of [-2, 10]; c = -2 is least: the claim fails at x = -3
(-25 < -9) and at every sampled x in (-10, -2)."""
from fractions import Fraction as Fr

QUOTED = {"c": -2, "x": -3, "lhs": -25, "rhs": -9}
for a in range(-600, 601):
    t = Fr(a, 37)
    assert (t - 1) ** 2 * (t + 2) == (t * t - 2 * t + 1) * (t + 2) == t ** 3 - 3 * t + 2
for a in range(-200, 1001):
    x = Fr(a, 100)
    if x >= QUOTED["c"]:
        assert x ** 3 + 2 >= 3 * x
        assert (x - 1) ** 2 >= 0 and x + 2 >= 0
x = QUOTED["x"]
assert x ** 3 + 2 == QUOTED["lhs"] and 3 * x == QUOTED["rhs"] and not (QUOTED["lhs"] >= QUOTED["rhs"])
for a in range(-999, -200):
    x = Fr(a, 100)                       # x in (-10, -2)
    assert (x - 1) ** 2 > 0 and x + 2 < 0
    assert x ** 3 + 2 < 3 * x
print("exr-reading-proofs-b3: all quoted values check")
