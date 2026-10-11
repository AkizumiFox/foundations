"""prp-limit-preserves-order-ordered-field (a): with eps = (a - b)/2,
a - eps = (a + b)/2 = b + eps; and eps > 0 when b < a."""
from fractions import Fraction as Q

QUOTED = {}
for A in [Q(p, 3) for p in range(-12, 13)]:
    for B in [Q(p, 4) for p in range(-12, 13)]:
        e = (A - B) / 2
        assert A - e == (2 * A - A + B) / 2 == (A + B) / 2 == B + e
        if B < A:
            assert e > 0
print("ok")
