"""exr-ordering-the-reals-a1: (a) 1 - 1/(n+1) >= 1/2 for n >= 1, a_0 = 0;
(c) d_0 = 1, d_1 = 7/5 (14^2 = 196 <= 200 < 225), d_k - 1 >= 2/5 for k >= 1; (e) margin 1."""
from fractions import Fraction as F
from math import isqrt
QUOTED = {"a_delta": F(1, 2), "a_N": 1, "d0": F(1), "d1": F(7, 5), "c_delta": F(2, 5), "c_N": 1}
a = lambda n: 1 - F(1, n + 1)
assert a(0) == 0 and all(a(n) >= QUOTED["a_delta"] for n in range(QUOTED["a_N"], 2000))
def d(k):
    m = isqrt(2 * 10 ** (2 * k))          # largest m with m^2 <= 2 * (10^k)^2
    assert m * m <= 2 * 10 ** (2 * k) < (m + 1) ** 2
    return F(m, 10 ** k)
assert d(0) == QUOTED["d0"] and d(1) == QUOTED["d1"]
assert 14 ** 2 == 196 <= 200 < 225 == 15 ** 2
ds = [d(k) for k in range(12)]
assert all(ds[i] <= ds[i + 1] for i in range(11))           # non-decreasing
assert all(x - 1 >= QUOTED["c_delta"] for x in ds[QUOTED["c_N"]:])
assert ds[0] - 1 == 0
print("ok")
