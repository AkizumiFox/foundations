"""exm-rhetoric-cases (Ch 5, Section 5.1): |x| + x >= 0; x^2 = x and x != 0 give x = 1;
the warning: max{a, b} >= (a + b)/2."""
from fractions import Fraction as Fr

QUOTED = {"b_solution": 1, "case_neg_value": 0}

xs = [Fr(k, 5) for k in range(-50, 51)]
for x in xs:
    assert abs(x) + x >= 0
    if x < 0:
        assert abs(x) + x == QUOTED["case_neg_value"]
    else:
        assert abs(x) + x == 2 * x
# x^2 = x iff x(x - 1) = 0 iff x in {0, 1}: a degree-2 identity checked at many points
for x in xs:
    assert x * (x - 1) == x**2 - x
    assert (x**2 == x) == (x in (0, 1))
assert [v for v in (0, 1) if v != 0] == [QUOTED["b_solution"]]
for a in xs[::3]:
    for b in xs[::4]:
        assert max(a, b) >= (a + b) / 2
        if a <= b:
            assert max(a, b) == b == (b + b) / 2
print("exm-rhetoric-cases: all quoted values check")
