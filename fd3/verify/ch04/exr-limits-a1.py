"""exr-limits-a1 (c): (2n+1)/(n+1) - 2 = -1/(n+1); for eps = 1/50 the least N is 50."""
from fractions import Fraction as Q

QUOTED = {"least_N": 50, "at_49": Q(1, 50)}
eps = Q(1, 50)
a = lambda k: Q(2 * k + 1, k + 1)
for k in range(3000):
    assert a(k) - 2 == -Q(1, k + 1)
works = lambda N: all(abs(a(m) - 2) < eps for m in range(N, 3000))
assert works(QUOTED["least_N"]) and not works(QUOTED["least_N"] - 1)
assert abs(a(49) - 2) == QUOTED["at_49"]
print("ok")
