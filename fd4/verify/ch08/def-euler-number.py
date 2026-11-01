"""def-euler-number and exr-exponential-and-logarithm-a1 (c): at n = 2 the bounds are 9/4 and 4;
for n >= 2 the bounds (1 + 1/n)^n <= e <= (1 - 1/n)^(-n) hold; e > 2; 1/e < 1/2 (the exp(2x) remark)."""
from fractions import Fraction as Fr
import math
QUOTED = {"lo2": Fr(9, 4), "hi2": Fr(4)}
assert (1 + Fr(1, 2)) ** 2 == QUOTED["lo2"]
assert (1 - Fr(1, 2)) ** -2 == QUOTED["hi2"]
for n in range(2, 300):
    assert float((1 + Fr(1, n)) ** n) <= math.e <= float((1 - Fr(1, n)) ** -n)
assert QUOTED["lo2"] > 2 and 1 / QUOTED["lo2"] < Fr(1, 2)
print("ok")
