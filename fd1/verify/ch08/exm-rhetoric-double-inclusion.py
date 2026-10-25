"""exm-rhetoric-double-inclusion (Ch 8, Section 8.2): x^2 <= 2x iff 0 <= x <= 2, exactly on
rationals with denominators up to 50 and on a grid; the sign facts used in the solution."""
from fractions import Fraction as Fr

QUOTED = {"A": "x^2 <= 2x", "B": "0 <= x <= 2"}

pts = {Fr(p, q) for q in range(1, 51) for p in range(-6 * q, 6 * q + 1)}
pts |= {Fr(k, 1000) for k in range(-5000, 5001)}
for x in pts:
    inA = x * x <= 2 * x
    inB = 0 <= x <= 2
    assert inA == inB
    assert (x * x <= 2 * x) == (x * (x - 2) <= 0)
    if x < 0:
        assert x - 2 < 0 and x * (x - 2) > 0
    if x > 2:
        assert x > 0 and x - 2 > 0 and x * (x - 2) > 0
    if 0 <= x <= 2:
        assert x * (x - 2) <= 0
print("exm-rhetoric-double-inclusion: all quoted values check")
