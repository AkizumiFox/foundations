"""exm-reals-mod-integers: 1 < sqrt 2 < 2 (1 < 2 < 4); 1/2 < sqrt 2 < 3/2 (1/4 < 2 < 9/4);
so sqrt2 - 1 and sqrt2 - 1/2 lie strictly between 0 and 1; [sqrt 2] meets [0, 1) in sqrt 2 - 1."""
from fractions import Fraction as F
import math

QUOTED = {"lo1": 1, "hi1": 2, "lo2": F(1, 2), "hi2": F(3, 2)}

assert QUOTED["lo1"] ** 2 < 2 < QUOTED["hi1"] ** 2
assert QUOTED["lo2"] ** 2 == F(1, 4) and QUOTED["hi2"] ** 2 == F(9, 4)
assert QUOTED["lo2"] ** 2 < 2 < QUOTED["hi2"] ** 2
r = math.sqrt(2)
assert 0 < r - 1 < 1 and 0 < r - 0.5 < 1 and 0 < 0.5 < 1
print("exm-reals-mod-integers: all quoted values check")
