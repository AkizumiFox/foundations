"""exm-costume-direct (Ch 5, Section 5.1): (x - 3)(x + 1) = x^2 - 2x - 3, and x^2 - 2x > 3 for x > 3."""
from fractions import Fraction as Fr

QUOTED = {"factorization (x-3)(x+1) checked below": True}

for k in range(-20, 21):          # degree-2 identity, checked at 41 points
    xv = Fr(k, 3)
    assert (xv - 3) * (xv + 1) == xv**2 - 2 * xv - 3
for k in range(1, 200):
    xv = 3 + Fr(k, 17)
    assert xv - 3 > 0 and xv + 1 > 0 and xv**2 - 2 * xv > 3
assert 3**2 - 2 * 3 == 3  # boundary: strictness needs x > 3
print("exm-costume-direct: all quoted values check")
