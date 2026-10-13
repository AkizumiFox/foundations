"""exr-uniform-continuity-rule-by-rule-c2: (a) f = 0 on x < 1, 1 on x >= 1; eps = 1;
eta = min(delta/4, 1/2), x = 1 - eta in (0, 1), y = 1 + eta in (1, 2), |x - y| = 2 eta <= delta/2
< delta, |f(x) - f(y)| = 1. (b) the mixed case: x <= b <= y gives |x - b|, |b - y| <= |x - y|;
checked on [0, 1], [1, 2] with f(x) = x^2 (uniformly continuous on each piece) for sample eps."""
from fractions import Fraction as F

QUOTED = {"eps in (a)": 1, "cap on eta": F(1, 2)}
f = lambda t: 0 if t < 1 else 1
for delta in [F(3), F(1), F(1, 2), F(1, 9), F(1, 10**5)]:
    eta = min(delta / 4, QUOTED["cap on eta"])
    x, y = 1 - eta, 1 + eta
    assert F(1, 2) <= x < 1 and 0 < x and 1 < y <= F(3, 2) < 2
    assert abs(x - y) == 2 * eta <= delta / 2 < delta
    assert abs(f(x) - f(y)) == 1 >= QUOTED["eps in (a)"]
# (b): A = [0, 1], B = [1, 2], g(x) = x^2; on each piece |g(x) - g(y)| <= 4|x - y|, so
# delta_i = eps/8 serves eps/2; delta = min = eps/8 serves eps on [0, 2]
g = lambda t: t * t
for eps in [F(1), F(1, 3), F(1, 50)]:
    d1 = d2 = eps / 8
    delta = min(d1, d2)
    pts = [F(k, 40) for k in range(0, 81)]
    for xx in pts:
        for yy in pts:
            if abs(xx - yy) < delta:
                assert abs(g(xx) - g(yy)) < eps
                if xx <= 1 <= yy:
                    assert abs(xx - 1) <= abs(xx - yy) and abs(1 - yy) <= abs(xx - yy)
print("exr-uniform-continuity-rule-by-rule-c2: all quoted values check")
