"""exr-disjunction-and-cases-c1 (Ch 1, Section 1.7): ||x|-|y|| <= |x-y| via the two cases
|x| >= |y|, |x| < |y|; the triangle-inequality steps; |-a| = |a|."""
from fractions import Fraction as F

QUOTED = {"number of sign cases": 4, "number of cases used": 2}

pts = [F(k, 4) for k in range(-40, 41)]
for a in pts:
    assert abs(-a) == abs(a)
for x in pts:
    for y in pts:
        lhs = abs(abs(x) - abs(y))
        if abs(x) >= abs(y):
            assert lhs == abs(x) - abs(y)
            assert abs(x) == abs((x - y) + y) <= abs(x - y) + abs(y)
        else:
            assert lhs == abs(y) - abs(x)
            assert abs(y) == abs((y - x) + x) <= abs(y - x) + abs(x)
        assert lhs <= abs(x - y)
assert 2 * 2 == QUOTED["number of sign cases"]
print("exr-disjunction-and-cases-c1: all quoted values check")
