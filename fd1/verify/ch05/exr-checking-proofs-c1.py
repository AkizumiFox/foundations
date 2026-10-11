"""exr-checking-proofs-c1 (Ch 5, Section 5.6): |u| < r gives u > -r; from |f(x) - f(a)| < f(a)/2
and f(a) > 0, f(x) > f(a)/2 > 0; -|u| <= u; the second route
f(x) <= 0 gives |f(x) - f(a)| >= f(a) - f(x) >= f(a) > f(a)/2. Run with sample continuous f and a delta for eps = f(a)/2."""
from fractions import Fraction as F
QUOTED = {"eps": "f(a)/2"}
for u in [F(k, 9) for k in range(-50, 51)]:
    for r in [F(1, 3), F(2), F(5, 2)]:
        assert -abs(u) <= u
        if abs(u) < r:
            assert u > -r
# f(x) = x^2 + x at a = 1 (f(a) = 2), eps = 1; |f(x) - f(1)| = |x - 1||x + 2| <= 4|x - 1| for |x - 1| < 1
f = lambda x: x * x + x
a = F(1)
fa = f(a)
assert fa > 0
eps = fa / 2
delta = min(F(1), eps / 4)
for t in range(-999, 1000):
    x = a + delta * F(t, 1000)
    assert abs(f(x) - fa) < eps
    assert f(x) - fa > -eps and f(x) > fa / 2 > 0
# second route: f(x) <= 0 and f(a) > 0 give |f(x) - f(a)| >= f(a) - f(x) >= f(a) > f(a)/2
for fa2 in [F(1, 3), F(2), F(7, 2)]:
    for fx in [F(k, 7) for k in range(-40, 1)]:
        assert abs(fx - fa2) >= fa2 - fx >= fa2 > fa2 / 2
print("exr-checking-proofs-c1: all quoted values check")
