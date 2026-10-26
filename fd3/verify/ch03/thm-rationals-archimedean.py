"""thm-rationals-archimedean and cor-rationals-archimedean-epsilon: the n of the proof
(1 if p <= 0, p + 1 if p > 0) beats x = p/q; the least n with 1/n < eps; the C3
counterexample -3/2 > -3."""
from fractions import Fraction as F

QUOTED = {"c3_x": F(-3, 2), "c3_p": -3}
for p in range(-30, 31):
    for q in range(1, 15):
        x = F(p, q)
        n = 1 if p <= 0 else p + 1
        assert n >= 0 and x < n
        if p > 0:
            assert x <= p
for eps in [F(a, b) for a in range(1, 12) for b in range(1, 40)]:
    n = int(1 / eps) + 1           # some natural number above 1/eps
    assert n >= 1 and F(1, n) < eps
    for m in range(n, n + 20):
        assert F(1, m) < eps
# C3 / exit-check fatal error: p/q <= p fails for negative p
assert QUOTED["c3_x"] > QUOTED["c3_p"] and (-3) * 2 < (-3) * 1
print("ok")
