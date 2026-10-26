"""exr-ordered-field-of-rationals-b3: floors of 22/7, -22/7, 0, -1/100."""
from fractions import Fraction as F
import math
QUOTED = {F(22, 7): 3, F(-22, 7): -4, F(0): 0, F(-1, 100): -1}
for x, m in QUOTED.items():
    assert m <= x < m + 1 and math.floor(x) == m
assert 3 * 7 == 21 and 4 * 7 == 28 and -4 * 7 == -28 and -3 * 7 == -21
print("ok")
