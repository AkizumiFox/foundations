"""exm-suffices-column (Section 8.3): (a) x^2 - 6x + 10 = (x - 3)^2 + 1 >= 1 > 0;
(b) a_n = (2n + 1)/(n + 1), a_n - 2 = -1/(n + 1), |a_n - 2| = 1/(n + 1), and N > 1/eps,
n >= N give |a_n - 2| < eps. Also the easy expansion of "Expand to check": for
A = {-1, 1}, "some element of A is positive" is true and "every element of A is positive"
false."""
from fractions import Fraction as Fr
import math

QUOTED = {"A": [-1, 1]}
for x in [Fr(a, 7) for a in range(-300, 301)]:
    assert x * x - 6 * x + 10 == (x - 3) ** 2 + 1
    assert (x - 3) ** 2 + 1 >= 1 > 0
for n in range(0, 2000):
    a = Fr(2 * n + 1, n + 1)
    assert a - 2 == Fr(-1, n + 1) and abs(a - 2) == Fr(1, n + 1)
for eps in [Fr(1), Fr(1, 2), Fr(1, 3), Fr(3, 10), Fr(1, 100), Fr(7, 1000), Fr(1, 999)]:
    N = math.floor(1 / eps) + 1          # an N in N with N > 1/eps
    assert N > 1 / eps
    for n in range(N, N + 500):
        a = Fr(2 * n + 1, n + 1)
        assert abs(a - 2) == Fr(1, n + 1) < Fr(1, N) < eps
A = QUOTED["A"]
assert any(x > 0 for x in A) and not all(x > 0 for x in A)
print("exm-suffices-column: all quoted values check")
