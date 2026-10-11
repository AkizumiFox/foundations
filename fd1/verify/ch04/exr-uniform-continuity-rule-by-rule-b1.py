"""exr-uniform-continuity-rule-by-rule-b1: for L >= 0 and eps > 0, delta = eps/(L + 1) > 0 and
L * delta < eps (so |f(x) - f(y)| <= L|x - y| <= L delta < eps); L = 0 makes eps/L undefined;
on a one-point set the matrix holds for L = -1."""
from fractions import Fraction as F

QUOTED = {"L in the remark": -1}
for L in [F(0), F(1, 2), F(1), F(37, 3)]:
    for eps in [F(1), F(1, 100), F(4)]:
        delta = eps / (L + 1)
        assert delta > 0 and L * delta < eps
        for k in range(0, 50):
            dist = delta * F(k, 50)                 # |x - y| < delta
            assert L * dist <= L * delta < eps
# one-point set: x = y, |f(x) - f(y)| = 0 <= L * 0 for L = -1
L = QUOTED["L in the remark"]
assert 0 <= L * 0
print("exr-uniform-continuity-rule-by-rule-b1: all quoted values check")
