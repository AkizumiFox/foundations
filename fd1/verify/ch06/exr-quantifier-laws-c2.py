"""exr-quantifier-laws-c2 (Section 4.9, exit check (b)): f(x) = 1/x on (0, 1), eps = 1; for each
delta, t = min(delta, 1/2), x = t, y = t/2: x, y in (0, 1), |x - y| = t/2 < delta and
|1/x - 1/y| = 1/t >= 2 >= 1."""
from fractions import Fraction as F

QUOTED = {"eps": 1, "cap on t": F(1, 2), "lower bound of |1/x - 1/y|": 2}
for delta in [F(5), F(1), F(1, 2), F(1, 3), F(1, 100), F(7, 10**6)]:
    t = min(delta, QUOTED["cap on t"])
    x, y = t, t / 2
    assert 0 < y < x < 1
    assert abs(x - y) == t / 2 < delta
    assert abs(1 / x - 1 / y) == 1 / t >= QUOTED["lower bound of |1/x - 1/y|"] >= QUOTED["eps"]
print("exr-quantifier-laws-c2: all quoted values check")
