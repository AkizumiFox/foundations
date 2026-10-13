"""prp-arbitrarily-close-equal (Section 4.9): the remark's values a = 0, b = 1/2, eps = 1 show
that "for some eps > 0" is not enough; and the proof's choice eps = |a - b| makes the
hypothesis fail for a != b (checked on samples)."""
from fractions import Fraction as F

QUOTED = {"a": F(0), "b": F(1, 2), "eps": F(1)}
a, b, eps = QUOTED["a"], QUOTED["b"], QUOTED["eps"]
assert eps > 0 and abs(a - b) < eps and a != b
for a, b in [(F(1), F(3)), (F(-2, 3), F(5, 7)), (F(10), F(-1))]:
    e = abs(a - b)
    assert e > 0 and not (abs(a - b) < e)
print("prp-arbitrarily-close-equal: all quoted values check")
