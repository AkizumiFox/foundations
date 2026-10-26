"""exr-ordered-field-of-rationals-b4 (printed B3): the quotient q of a = qn + r, 0 <= r < n, is floor(a/n)."""
from fractions import Fraction as F
import math
QUOTED = {}
for a in range(-60, 61):
    for n in range(1, 13):
        q, r = divmod(a, n)  # Python: 0 <= r < n for n > 0
        assert a == q * n + r and 0 <= r < n
        # q <= a/n < q + 1 in Q, and uniqueness of the integer part
        assert F(q) <= F(a, n) < F(q + 1)
        assert q == math.floor(F(a, n))
        assert r == a - n * math.floor(F(a, n))
        assert F(q * n) * F(1, n) == q and F(q * n + n) * F(1, n) == q + 1
print("ok")
