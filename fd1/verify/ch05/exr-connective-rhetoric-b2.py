"""exr-connective-rhetoric-b2 (Ch 5, Section 5.1): y = x/2 is non-zero for x != 0; |x/2| = |x|/2;
|x| <= |x|/2 forces |x| <= 0, against |x| > 0."""
from fractions import Fraction as Fr

QUOTED = {"y": "x/2"}
for k in range(-30, 31):
    x = Fr(k, 7)
    if x != 0:
        y = x / 2
        assert y != 0 and abs(y) == abs(x) / 2 and abs(x) > 0
        assert not (abs(x) <= abs(y))          # the instance fails, so x != 0 is impossible
    # |x| <= |x|/2 iff |x| <= 0
    assert (abs(x) <= abs(x) / 2) == (abs(x) <= 0)
print("exr-connective-rhetoric-b2: all quoted values check")
