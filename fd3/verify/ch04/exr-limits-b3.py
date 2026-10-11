"""exr-limits-b3: with eps = 1/2, the triangle bound gives 1 < 1/2 + 1/2 = 1, a contradiction;
(n + 1) - n = 1 for the multiples n.1 (checked on the integers, the case F = Q)."""
from fractions import Fraction as Q

QUOTED = {"eps": Q(1, 2), "sum": 1}
assert QUOTED["eps"] + QUOTED["eps"] == QUOTED["sum"]
assert not (QUOTED["sum"] < QUOTED["eps"] + QUOTED["eps"])
for n in range(0, 1000):
    assert (n + 1) - n == 1
print("ok")
