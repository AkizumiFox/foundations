"""Quick check before thm-constructed-reals-cauchy-complete (Section 5.5):
x_k = r + 1/(k+1) with r^2 = 2, r > 0; 7/5 <= r < 3/2 from (7/5)^2 = 49/25 < 2 < 9/4 = (3/2)^2;
(k+1) x_k = (k+1) r + 1 has integer parts 2, 3, 5 for k = 0, 1, 2, so q_0, q_1, q_2 = 2, 3/2, 5/3;
the interval bounds 12/5 <= r+1 < 5/2, 19/5 <= 2r+1 < 4, 26/5 <= 3r+1 < 11/2;
x_2 in [26/15, 11/6) and q_2 = 25/15, x_2 - q_2 < 1/3."""
from fractions import Fraction as F
from math import isqrt
QUOTED = {"m": [2, 3, 5], "q": [F(2), F(3, 2), F(5, 3)],
          "r_lo": F(7, 5), "r_hi": F(3, 2),
          "intervals": [(F(12, 5), F(5, 2)), (F(19, 5), F(4)), (F(26, 5), F(11, 2))],
          "x2": (F(26, 15), F(11, 6))}
lo, hi = QUOTED["r_lo"], QUOTED["r_hi"]
assert lo * lo == F(49, 25) < 2 < F(9, 4) == hi * hi
for k in range(3):
    # exact integer part of (k+1)*sqrt(2) + 1, computed by integer square roots
    m = isqrt(2 * (k + 1) ** 2) + 1
    assert m == QUOTED["m"][k]
    assert F(m, k + 1) == QUOTED["q"][k]
    a, b = QUOTED["intervals"][k]
    assert a == (k + 1) * lo + 1 and b == (k + 1) * hi + 1
    # the bounds alone force the integer part
    assert m <= a and b <= m + 1
assert QUOTED["x2"] == (lo + F(1, 3), hi + F(1, 3))
assert QUOTED["q"][2] == F(25, 15) <= QUOTED["x2"][0]
assert QUOTED["x2"][1] - QUOTED["q"][2] <= F(1, 3)
print("ok")
