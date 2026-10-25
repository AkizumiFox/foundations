"""exm-root-and-square (Section 2.1): r o q = |.| != id_R, q o r = id_[0, inf), checked on exact rational squares and on floats."""
import math
from fractions import Fraction as F

QUOTED = {"(r o q)(-1)": 1, "id_R(-1)": -1}

# r o q at rationals whose square has an exact rational root: sqrt(x^2) = |x|
def exact_sqrt(t):
    """Nonnegative rational s with s*s == t, for t a square of a rational."""
    n, d = math.isqrt(t.numerator), math.isqrt(t.denominator)
    assert n * n == t.numerator and d * d == t.denominator
    return F(n, d)

xs = [F(k, 7) for k in range(-70, 71)]
assert all(exact_sqrt(x * x) == abs(x) for x in xs)
assert exact_sqrt(F(-1) ** 2) == QUOTED["(r o q)(-1)"] != QUOTED["id_R(-1)"]
# q o r: (sqrt t)^2 = t for t >= 0 (floats), and sqrt t >= 0, so values lie in [0, inf)
ts = [k / 13 for k in range(0, 400)]
assert all(abs(math.sqrt(t) ** 2 - t) < 1e-12 and math.sqrt(t) ** 2 >= 0 for t in ts)
# r o q differs from id at every negative x
assert all(abs(x) != x for x in xs if x < 0)
print("exm-root-and-square: ok")
