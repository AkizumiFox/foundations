"""exm-subset-bounded-above (Ch 5, Section 5.5) and the warnings after it: the example has no
numbers; the warning "The search is not the proof" quotes x = -3: x < 2 and x^2 = 9 >= 4.
The warning on dependencies quotes delta = min(1, eps/(2|x| + 1)), which depends on x; for a
fixed eps the formula gives different deltas at different x.
The Quick check on scratch work (Section 8.5): |3x - 6| = 3|x - 2|, and delta = eps/3 > 0 gives
|3x - 6| < eps whenever |x - 2| < delta."""
from fractions import Fraction as F

QUOTED = {"x": -3, "x_squared": 9}
x = QUOTED["x"]
assert x < 2 and x * x == QUOTED["x_squared"] and not (x * x < 4)

eps = F(1, 10)
d = lambda x: min(F(1), eps / (2 * abs(x) + 1))
assert d(0) != d(100)          # the formula mentions x
for k in range(-400, 401):
    x = F(k, 17)
    assert abs(3 * x - 6) == 3 * abs(x - 2)
    for eps in [F(1), F(1, 10), F(3, 7)]:
        delta = eps / 3
        assert delta > 0
        if abs(x - 2) < delta:
            assert abs(3 * x - 6) < eps
print("exm-subset-bounded-above: all quoted values check")
