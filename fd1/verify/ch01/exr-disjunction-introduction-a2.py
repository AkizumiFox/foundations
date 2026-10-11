"""exr-disjunction-introduction-a2 (Section 1.5 drill): (a) from x = 5 the lines (i), (ii) and
x >= 5 written out are true; (e) premise x < -1 gives x < 0, and x = -2 breaks x < -5;
(f) 4 = 2 * 2."""
from _grid import grid
from fractions import Fraction as F

QUOTED = {"(e) witness": -2, "(f) n": 4}
x = F(5)
assert (x == 5 or x == 6) and (x > 4 or x == 5) and (x > 5 or x == 5)
assert all((t >= 5) == (t > 5 or t == 5) for t in grid())
assert all((not t < -1) or t < 0 for t in grid())
x = QUOTED["(e) witness"]
assert x < -1 and not x < -5
n = QUOTED["(f) n"]
assert n == 2 * 2 and n % 2 == 0
print("exr-disjunction-introduction-a2: checks")
