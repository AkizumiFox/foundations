"""exr-naturals-and-well-ordering-b4 (Ch 2, 01): prove-or-disprove items; Quick check {n in Z : n^2 < 30}."""
from fractions import Fraction as Fr
import random, math
random.seed(2)
# (a) Z: n-1 < n, in Z.  (b) -1/(n+1) in set and > -1/n
for n in range(1, 2000):
    assert Fr(-1, n) < Fr(-1, n + 1) < 0
    # (e) 1/(n+1) in set and below 1/n
    assert Fr(1, n + 1) < Fr(1, n)
# (c) even naturals: min exists (trivially, finite samples)
# (d) greatest of T subset {1/n} is 1/min N
for _ in range(5000):
    N = random.sample(range(1, 200), random.randint(1, 10))
    T = [Fr(1, n) for n in N]
    assert max(T) == Fr(1, min(N))
# (f) -5 < -13/3, and -5 = floor(-13/3)
assert Fr(-5) < Fr(-13, 3) and math.floor(Fr(-13, 3)) == -5
# Quick check
QUOTED = {"least": -5, "bound": -6}
A = [n for n in range(-100, 101) if n * n < 30]
assert min(A) == QUOTED["least"] and 0 in A and (-5) ** 2 == 25 < 30
assert all(n * n >= 36 > 30 for n in range(-100, QUOTED["bound"] + 1))
assert all(n > QUOTED["bound"] for n in A)
print("exr-naturals-and-well-ordering-b4: all quoted values check")
