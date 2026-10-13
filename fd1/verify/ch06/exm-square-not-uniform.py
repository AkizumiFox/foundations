"""exm-square-not-uniform (Section 4.10): f(x) = x^2 on R.
C: delta = min(1, eps/(2|x| + 1)) works (sampled x, eps, y); it depends on x.
not UC: eps = 1, x = 1/delta, y = 1/delta + delta/2 give |x - y| = delta/2 < delta and
|y^2 - x^2| = 1 + delta^2/4 >= 1 (exact arithmetic at many rational delta; both sides are
rational functions of delta of low degree, so agreement at these points is an identity)."""
from fractions import Fraction as F

QUOTED = {"eps for not UC": 1}
xs = [F(0), F(1), F(-3), F(7, 2), F(100), F(-1000, 3)]
epss = [F(1), F(1, 10), F(5), F(1, 1000)]
for x in xs:
    for eps in epss:
        delta = min(F(1), eps / (2 * abs(x) + 1))
        assert delta > 0
        for k in range(-20, 21):
            y = x + delta * F(k, 21)          # |x - y| < delta
            assert abs(x - y) < delta
            assert abs(y) < abs(x) + 1 and abs(x + y) < 2 * abs(x) + 1
            assert abs(x * x - y * y) < eps
# delta depends on x: for eps = 1 it differs at x = 0 and x = 100
assert min(F(1), F(1) / 1) != min(F(1), F(1) / 201)
for d in [F(k, 7) for k in range(1, 60)] + [F(1, 10**6), F(10**3)]:
    x, y = 1 / d, 1 / d + d / 2
    assert y - x == d / 2 < d
    assert y * y - x * x == 1 + d * d / 4 == (d / 2) * (2 / d + d / 2)
    assert y * y - x * x >= 1
assert QUOTED["eps for not UC"] == 1
print("exm-square-not-uniform: all quoted values check")
