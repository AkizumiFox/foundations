"""exr-exponential-and-logarithm-b1: n = 6 gives 117649/46656 > 5/2 and 46656/15625 < 3;
the upper bounds at n = 2, 3, 4, 5 are 4, 27/8, 256/81, 3125/1024, all above 3."""
from fractions import Fraction as Fr
QUOTED = {"lo": Fr(117649, 46656), "hi": Fr(46656, 15625), "hi5": Fr(3125, 1024)}
assert (Fr(7, 6)) ** 6 == QUOTED["lo"] and (1 - Fr(1, 6)) ** -6 == QUOTED["hi"]
assert 2 * 117649 == 235298 and 5 * 46656 == 233280 and QUOTED["lo"] > Fr(5, 2)
assert 3 * 15625 == 46875 and QUOTED["hi"] < 3
assert (1 - Fr(1, 5)) ** -5 == QUOTED["hi5"] > 3
UPPER = {2: Fr(4), 3: Fr(27, 8), 4: Fr(256, 81), 5: Fr(3125, 1024)}
for n in range(2, 6):
    assert (1 - Fr(1, n)) ** -n == UPPER[n] > 3
print("ok")
