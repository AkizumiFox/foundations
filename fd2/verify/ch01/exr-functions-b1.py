"""exr-functions-b1 (Ch 6 Section 6.4)."""
from fractions import Fraction as F

QUOTED = {"(1,2) and (2,1) go to": 3, "not hit": 1, "value at n = 1 in (e)": 0,
          "x = 1 goes to": F(1, 2)}

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
# (d) x / (1 + |x|) and y / (1 - |y|) are mutually inverse
phi = lambda x: x / (1 + abs(x))
psi = lambda y: y / (1 - abs(y))
xs = [F(k, 3) for k in range(-60, 61)]
assert all(abs(phi(x)) < 1 and psi(phi(x)) == x for x in xs)
ys = [F(k, 50) for k in range(-49, 50)]
assert all(phi(psi(y)) == y for y in ys)
assert phi(1) == QUOTED["x = 1 goes to"] and psi(F(1, 2)) == 1
# (e) n + (-1)^n at n = 1 is 0, not in Z_{>0}; on N = {0, 1, ...} it swaps 2k and 2k + 1
assert 1 + (-1) ** 1 == QUOTED["value at n = 1 in (e)"]
e = {n: n + (-1) ** n for n in range(0, 40)}
assert all(e[e[n]] == n for n in range(0, 39))
print("exr-functions-b1: all quoted values check")
