"""exr-a-cauchy-sequence-without-a-limit-a1 (d): x_2 - x_3 = 1/408 = (17*34 - 577)/408;
e_2/x_2 = 1/204; chain 1/408 <= 1/204 <= 1/144 <= 1/8."""
from fractions import Fraction as F
QUOTED = {"diff": F(1, 408), "ratio": F(1, 204)}
x2, x3 = F(17, 12), F(577, 408)
e2 = x2*x2 - 2
assert 408 == 12*34 and 17*34 - 577 == 1
assert x2 - x3 == QUOTED["diff"]
assert e2 / x2 == QUOTED["ratio"] == F(1, 144) * F(12, 17)
assert F(1, 408) <= F(1, 204) <= F(1, 144) <= F(1, 8)
print("ok")
