"""exm-verify-cases (Proof A, Ch 5, Section 5.6): (x-1)(x-2) = x^2 - 3x + 2; a negative product
has factors of opposite signs; the second case x < 1 and x > 2 is impossible; the claim."""
from fractions import Fraction as F
QUOTED = {}
for k in range(-600, 601):
    x = F(k, 101)
    assert (x - 1) * (x - 2) == x * x - 3 * x + 2
    if x * x - 3 * x + 2 < 0:
        assert (x - 1 > 0 and x - 2 < 0) or (x - 1 < 0 and x - 2 > 0)
        assert not (x - 1 < 0 and x - 2 > 0)
        assert 1 < x < 2
# the second case: x > 2 and x < 1 would give 2 < 1, against not(2 < 1)
assert not (2 < 1)
print("exm-verify-cases: all quoted values check")
