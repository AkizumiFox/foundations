"""exr-functions-b1 (Ch 6 Section 6.4)."""
from fractions import Fraction as F

QUOTED = {"(1,2) and (2,1) go to": 3, "not hit": 1, "value at n = 1 in (e)": 0,
          "x = 3/4 goes to": F(3, 5)}

# (b)
assert 1 + 2 == 2 + 1 == QUOTED["(1,2) and (2,1) go to"]
assert all(0 + k == k for k in range(0, 200))  # (0, k) |-> k: surjective on N = {0, 1, ...}
# (a) 2n never 1
assert all(2 * n != QUOTED["not hit"] for n in range(-500, 501))
# (c) factorization and the positive factor
pts = [F(k, 4) for k in range(-20, 21)]
for a in pts:
    for b in pts:
        assert a ** 3 - b ** 3 == (a - b) * (a * a + a * b + b * b)
        assert a * a + a * b + b * b == (a + b / 2) ** 2 + F(3, 4) * b * b
        if a != b:
            assert a * a + a * b + b * b > 0
# (d) x / sqrt(1 + x^2) and y / sqrt(1 - y^2) are mutually inverse (floats, tolerance),
# and the quoted example 3/4 -> 3/5 -> 3/4 exactly (both radicands are rational squares)
import math
phi = lambda x: x / math.sqrt(1 + x * x)
psi = lambda y: y / math.sqrt(1 - y * y)
xs = [k / 3 for k in range(-60, 61)]
assert all(abs(phi(x)) < 1 and abs(psi(phi(x)) - x) < 1e-9 for x in xs)
ys = [k / 50 for k in range(-49, 50)]
assert all(abs(phi(psi(y)) - y) < 1e-12 for y in ys)
x0 = F(3, 4)
assert 1 + x0 * x0 == F(5, 4) ** 2 and x0 / F(5, 4) == QUOTED["x = 3/4 goes to"]
y0 = QUOTED["x = 3/4 goes to"]
assert 1 - y0 * y0 == F(4, 5) ** 2 and y0 / F(4, 5) == x0
# (e) n + (-1)^n at n = 1 is 0, not in Z_{>0}; on N = {0, 1, ...} it swaps 2k and 2k + 1
assert 1 + (-1) ** 1 == QUOTED["value at n = 1 in (e)"]
e = {n: n + (-1) ** n for n in range(0, 40)}
assert all(e[e[n]] == n for n in range(0, 39))
print("exr-functions-b1: all quoted values check")
