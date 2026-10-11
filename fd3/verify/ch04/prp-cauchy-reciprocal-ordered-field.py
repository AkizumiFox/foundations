"""prp-cauchy-reciprocal-ordered-field: 1/a_n - 1/a_m = (a_m - a_n)/(a_n a_m), the bound
|b_n - b_m| <= |a_m - a_n|/c^2 when |a_n|, |a_m| >= c, and c^2 eps / c^2 = eps; the witness
a_n = 1/(n+1), 1/a_n = n + 1 unbounded."""
from fractions import Fraction as F
import random
QUOTED = {"witness": "n + 1"}
random.seed(1)
r = lambda: F(random.randint(1, 100), random.randint(1, 30))
for _ in range(5000):
    c = r()
    an = (c + r() - F(1, 31)) * random.choice([1, -1])
    am = (c + r() - F(1, 31)) * random.choice([1, -1])
    if abs(an) < c or abs(am) < c:
        continue
    assert 1/an - 1/am == (am - an) / (an*am)
    assert abs(1/an - 1/am) <= abs(am - an) / c**2
    eps = r()
    assert (c**2 * eps) / c**2 == eps
assert all(1 / F(1, n + 1) == n + 1 for n in range(100))
print("ok")
