"""exr-the-uniqueness-theorem-r3 (c): for x < y, a rational q with x < q < y and N in Z_{>0}
with 1/N < (y - q)/sqrt2, the element z = q + sqrt2/N satisfies q < z < y. Checked with exact
rationals on samples (x, y rational), using rational bounds lo < sqrt2 < hi; N is chosen from
the lower bound lo, so 1/N < (y - q)/hi <= (y - q)/sqrt2 is certified, and z < q + hi/N <= y."""
from fractions import Fraction as F
import math

LO, HI = F(14142, 10000), F(14143, 10000)
assert LO * LO < 2 < HI * HI and LO > 0
QUOTED = {}

samples = [(F(0), F(1)), (F(-3, 7), F(-2, 5)), (F(1), F(1) + F(1, 10**6)), (F(5, 3), F(17, 10))]
for x, y in samples:
    q = (x + y) / 2                      # x < q < y
    assert x < q < y
    N = math.floor(HI / (y - q)) + 1     # 1/N < (y - q)/HI
    assert N >= 1 and F(1, N) < (y - q) / HI
    z_lo, z_hi = q + LO / N, q + HI / N  # z lies strictly between these bounds
    assert q < z_lo and z_hi < y
print("ok")
