"""exr-completeness-a1 (d): for the constant sequence x_k = r (r^2 = 2, r > 0) the approximants are
q_0 = 1, q_1 = 1, q_2 = 4/3, from 1 <= r < 2, 2 <= 2r < 3, 4 <= 3r < 5 (r in [7/5, 3/2))."""
from fractions import Fraction as F
from math import isqrt
QUOTED = {"q": [F(1), F(1), F(4, 3)], "m": [1, 2, 4]}
for k in range(3):
    m = isqrt(2 * (k + 1) ** 2)          # integer part of (k+1) sqrt 2
    assert m == QUOTED["m"][k] and F(m, k + 1) == QUOTED["q"][k]
    # also forced by 7/5 <= r < 3/2
    assert m <= (k + 1) * F(7, 5) and (k + 1) * F(3, 2) <= m + 1
# the approximants are within 1/(k+1) below r, checked by squares: q^2 <= 2 < (q + 1/(k+1))^2
for k in range(200):
    m = isqrt(2 * (k + 1) ** 2)
    q = F(m, k + 1)
    assert q * q <= 2 < (q + F(1, k + 1)) ** 2
print("ok")
