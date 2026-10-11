"""exr-writing-proofs-a1 (Ch 5, Section 5.5): x + y > 2 implies x > 1 or y > 1; the
contrapositive x <= 1 and y <= 1 gives x + y <= 2; not(a > 1) iff a <= 1;
a <= 2 implies not(a > 2)."""
from fractions import Fraction as F
QUOTED = {}
pts = [F(k, 13) for k in range(-60, 61)]
for x in pts:
    assert (not (x > 1)) == (x <= 1)
    if x <= 2:
        assert not (x > 2)
    for y in pts:
        if x + y > 2:
            assert x > 1 or y > 1
        if x <= 1 and y <= 1:
            assert x + y <= 2
print("exr-writing-proofs-a1: all quoted values check")
