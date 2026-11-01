"""exr-roots-and-rational-powers-a1 (05): (c) m = 1, M = 8, s = 2 for n = 3, a = 8; (d) 8^(-2/3) = 1/4."""
from fractions import Fraction as F

QUOTED = {"m": 1, "M": 8, "s": 2, "d": F(1, 4)}
assert min(1, 8) == QUOTED["m"] and max(1, 8) == QUOTED["M"] and QUOTED["s"] ** 3 == 8
assert F(2) ** -2 == QUOTED["d"]
print("ok")
