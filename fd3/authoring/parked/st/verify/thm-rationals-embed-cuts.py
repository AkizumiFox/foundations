"""thm-rationals-embed-cuts (Section 7.5): the splits in the proof of (b) and (d), and the sample
computations after the theorem: D_{1/2} + D_{1/3} = D_{5/6}, D_{-2} D_3 = D_{-6}, D_2^{-1} = D_{1/2}.
Rational cuts are modelled by their rational q (D_q = {r : r < q})."""
from fractions import Fraction as F
import random

QUOTED = {"sum": F(5, 6), "product": -6, "inverse": F(1, 2)}
assert F(1, 2) + F(1, 3) == QUOTED["sum"]
assert -2 * 3 == QUOTED["product"]
assert 2 * QUOTED["inverse"] == 1

# (b): x = (p - delta) + (q - delta) with delta = (p + q - x)/2; (d): r s = x with r = lambda p,
# s = x/(lambda p); both are checked exactly, on random rationals, in the loop below.

random.seed(7)
for _ in range(5000):
    p_ = F(random.randint(-300, 300), random.randint(1, 40))
    q_ = F(random.randint(-300, 300), random.randint(1, 40))
    x_ = p_ + q_ - F(random.randint(1, 500), random.randint(1, 40))   # x < p + q
    d = (p_ + q_ - x_) / 2
    assert d > 0 and p_ - d < p_ and q_ - d < q_ and (p_ - d) + (q_ - d) == x_
    pp = F(random.randint(1, 300), random.randint(1, 40))
    qq = F(random.randint(1, 300), random.randint(1, 40))
    xx = pp * qq * F(random.randint(1, 999), 1000)                   # 0 < x < pq
    l = (1 + xx / (pp * qq)) / 2
    r, s = l * pp, xx / (l * pp)
    assert xx / (pp * qq) < l < 1 and 0 < r < pp and 0 < s < qq and r * s == xx
    # x <= 0 case: r = p/2, s = q/2 positive with rs > 0
    assert pp / 2 < pp and qq / 2 < qq and (pp / 2) * (qq / 2) > 0
print("ok")
