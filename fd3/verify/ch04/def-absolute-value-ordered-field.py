"""def-absolute-value-ordered-field: the examples, the non-example (fold), the worked example after the proposition, and the second Quick check."""
from fractions import Fraction as F

QUOTED = {
    "abs_three_quarters": F(3, 4),
    "distance_third_half": F(1, 6),
    "interval": (F(1, 4), F(3, 4)),
    "two_thirds_lower_test": (3, 8),
    "two_thirds_test": (8, 9),
    "endpoint_distance": F(1, 4),
    "square_nonexample": (4, 2),
}
assert abs(F(3, 4)) == abs(F(-3, 4)) == QUOTED["abs_three_quarters"]
# -3/4 < 0 by the comparison formula: (-3)*1 < 0*4
assert (-3) * 1 < 0 * 4 and F(-3, 4) < 0
assert F(1, 3) - F(1, 2) == F(-1, 6) and abs(F(-1, 6)) == QUOTED["distance_third_half"]
assert (F(1, 2) - F(1, 4), F(1, 2) + F(1, 4)) == QUOTED["interval"]
# 1/4 < 2/3 by the comparison formula: 1*3 < 2*4
assert (1 * 3, 2 * 4) == QUOTED["two_thirds_lower_test"] and 3 < 8
# 2/3 < 3/4 by the comparison formula: 2*4 < 3*3
assert (2 * 4, 3 * 3) == QUOTED["two_thirds_test"] and 8 < 9
assert abs(F(2, 3) - F(1, 2)) < F(1, 4)
assert abs(F(3, 4) - F(1, 2)) == QUOTED["endpoint_distance"]
# the set {x : |x - 1/2| < 1/4} agrees with 1/4 < x < 3/4 on a grid
for k in range(-200, 201):
    x = F(k, 160)
    assert (abs(x - F(1, 2)) < F(1, 4)) == (F(1, 4) < x < F(3, 4))
sq = lambda x: x * x
assert (sq(1 + 1), sq(1) + sq(1)) == QUOTED["square_nonexample"]
# second Quick check: |x - 1| < 2 and |x + 1| < 2 iff -1 < x < 1
QUOTED["qc_single"] = ((F(-1), F(3)), (F(-3), F(1)))
QUOTED["qc_both"] = (F(-1), F(1))
assert (1 - 2, 1 + 2) == QUOTED["qc_single"][0]
assert (-1 - 2, -1 + 2) == QUOTED["qc_single"][1]
lo = max(QUOTED["qc_single"][0][0], QUOTED["qc_single"][1][0])
hi = min(QUOTED["qc_single"][0][1], QUOTED["qc_single"][1][1])
assert (lo, hi) == QUOTED["qc_both"]
for k in range(-800, 801):
    x = F(k, 200)
    assert ((abs(x - 1) < 2) and (abs(x + 1) < 2)) == (F(-1) < x < F(1))
print("ok")
