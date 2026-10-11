"""lem-cof-below-sum: Quick check in Section 6.2 with a = 3/4, b = 1/2, q = 1:
r works iff 1/2 < r < 3/4; r = 2/3 gives q - r = 1/3 < 1/2. Plus random checks of both lemmas in Q
(sum: q < a + b iff some rational r has r < a and q - r < b; product for a, b, q > 0)."""
from fractions import Fraction as F
import random

QUOTED = {"a": F(3, 4), "b": F(1, 2), "q": 1, "r": F(2, 3), "q_minus_r": F(1, 3),
          "low": F(1, 2), "high": F(3, 4)}
a, b, q, r = QUOTED["a"], QUOTED["b"], QUOTED["q"], QUOTED["r"]
assert q - r == QUOTED["q_minus_r"] and r < a and q - r < b
assert q - b == QUOTED["low"] and a == QUOTED["high"]
# r works iff low < r < high, sampled
for num in range(-200, 200):
    rr = F(num, 100)
    assert (rr < a and q - rr < b) == (QUOTED["low"] < rr < QUOTED["high"])

random.seed(3)
for _ in range(3000):
    a = F(random.randint(-500, 500), random.randint(1, 50))
    b = F(random.randint(-500, 500), random.randint(1, 50))
    q = F(random.randint(-1000, 1000), random.randint(1, 50))
    if q < a + b:
        r = ((q - b) + a) / 2   # the midpoint lies in the gap (q - b, a)
        assert r < a and q - r < b
    else:
        # no r: r < a and q - r < b would give q < a + b
        pass
    if a > 0 and b > 0 and q > 0 and q < a * b:
        r = (q / b + a) / 2
        assert r > 0 and r < a and q / r < b
print("ok")
