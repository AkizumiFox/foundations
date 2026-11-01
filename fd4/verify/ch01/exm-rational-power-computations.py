"""exm-rational-power-computations (05): 27^(2/3) * 9^(-1/2) = 3; (16/81)^(-3/4) = 27/8; 2^(1/2) < 3^(1/3) via 8 < 9."""
from fractions import Fraction as F

QUOTED = {"first": F(3), "second": F(27, 8), "sixth": (8, 9)}
assert 3 ** 3 == 27 and 3 ** 2 == 9
assert F(3) ** 2 * F(3) ** -1 == QUOTED["first"]
assert F(2, 3) ** 4 == F(16, 81) and 2 ** 4 == 16 and 3 ** 4 == 81
assert F(2, 3) ** -3 == QUOTED["second"]
assert (2 ** 3, 3 ** 2) == QUOTED["sixth"] and 8 < 9
print("ok")
