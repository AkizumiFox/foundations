"""prp-rational-integer-part and the Quick check after it: floor(-7/3) = -3 with its two
comparisons; the least n with 1/n < 3/1000 is 334."""
from fractions import Fraction as F
import math

QUOTED = {"floor_m7_3": -3, "least_n": 334, "products": (-9, -6, 999, 1002)}
x = F(-7, 3)
m = QUOTED["floor_m7_3"]
assert m <= x < m + 1 and math.floor(x) == m
assert (-3) * 3 == QUOTED["products"][0] and -9 <= -7
assert (-2) * 3 == QUOTED["products"][1] and -7 < -6
n = next(k for k in range(1, 10**4) if F(1, k) < F(3, 1000))
assert n == QUOTED["least_n"]
assert 3 * 333 == QUOTED["products"][2] and 3 * 334 == QUOTED["products"][3]
# uniqueness and existence on a grid
for p in range(-50, 51):
    for q in range(1, 13):
        y = F(p, q)
        cands = [k for k in range(-60, 61) if k <= y < k + 1]
        assert cands == [math.floor(y)]
print("ok")
