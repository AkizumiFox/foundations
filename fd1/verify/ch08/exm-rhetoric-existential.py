"""exm-rhetoric-existential (Ch 8, Section 8.2): 1/n -> 0; N an integer > 1/eps is positive,
1/N < eps, and n >= N gives 0 < 1/n <= 1/N; for eps = 0.03, 1/eps = 33.3..., N = 34 works."""
from fractions import Fraction as Fr
import math

QUOTED = {"eps": Fr(3, 100), "one_over_eps (33.3...)": 33.3, "N": 34}

e = QUOTED["eps"]
assert math.floor(1 / e) == 33 and abs(float(1 / e) - QUOTED["one_over_eps (33.3...)"]) < 0.04 and 1 / e != 33
N = QUOTED["N"]
assert N > 1 / e and Fr(1, N) < e
assert Fr(1, 33) > e      # 33 is too small: N must exceed 1/eps
for eps in [Fr(1), Fr(1, 2), Fr(3, 100), Fr(1, 997), Fr(5), Fr(7, 3)]:
    Nv = math.floor(1 / eps) + 1   # one integer beyond 1/eps
    assert Nv > 1 / eps > 0 and Nv >= 1 and Fr(1, Nv) < eps
    for n in range(Nv, Nv + 300):
        assert 0 < Fr(1, n) <= Fr(1, Nv) < eps

# The dependency numbers of "The dependency parenthesis" (ledgered under this block):
# for f(x) = x^2, eps = 1, a >= 0, the largest delta is sqrt(a^2 + 1) - a.
DEP = {"a=1": 0.41, "a=100": 0.005, "a=2": 0.236, "a=10": 0.0499, "x": Fr(1006, 100), "x2-100": Fr(12036, 10000)}


def largest_delta(a):
    return math.sqrt(a * a + 1) - a


def works(a, d, samples=4000):
    """No x with |x - a| < d has |x^2 - a^2| >= 1 (sampled, endpoints approached)."""
    for i in range(1, samples):
        t = d * i / samples
        for x in (a + t, a - t):
            if abs(x * x - a * a) >= 1:
                return False
    return True


for a in [0, 0.5, 1, 2, 10, 100]:
    d = largest_delta(a)
    assert works(a, d)
    assert abs((a + d) ** 2 - a * a - 1) < 1e-9          # at the edge |x^2 - a^2| reaches 1
    assert (a + d + 1e-6) ** 2 - a * a >= 1                 # a slightly larger delta fails
assert abs(largest_delta(1) - DEP["a=1"]) < 0.005
assert abs(largest_delta(100) - DEP["a=100"]) < 0.0001
assert abs(largest_delta(2) - DEP["a=2"]) < 0.0005
assert abs(largest_delta(10) - DEP["a=10"]) < 0.0001
# the Quick check: delta = 0.1 works at a = 2, fails at a = 10 with x = 10.06
assert 0.1 < largest_delta(2) and works(2, 0.1)
x = DEP["x"]
assert abs(x - 10) < Fr(1, 10) and x * x - 100 == DEP["x2-100"] >= 1
# f(x) = 3x + 1: |f(x) - f(a)| = 3|x - a| < eps when |x - a| < eps/3
for a in [Fr(-7), Fr(0), Fr(5, 2)]:
    for eps in [Fr(1), Fr(1, 100)]:
        for x in [a + eps / 3 * Fr(k, 10) for k in range(-9, 10)]:
            assert abs((3 * x + 1) - (3 * a + 1)) == 3 * abs(x - a) < eps
print("exm-rhetoric-existential: all quoted values check")
