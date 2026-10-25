"""exr-definability-and-isomorphism-c2 (Section 7.5): x -> 2x and x -> x + q preserve < on
sample rationals and are inverted by x/2 and x - q; 2x fixes 0."""
from fractions import Fraction as F

S = [F(n, d) for n in range(-6, 7) for d in (1, 2, 3, 5)]
for q in (F(-3, 4), F(0), F(5, 2)):
    assert all((x < y) == (x + q < y + q) and (x + q) - q == x for x in S for y in S)
assert all((x < y) == (2 * x < 2 * y) and (2 * x) / 2 == x for x in S for y in S)
assert 2 * F(0) == 0
print("exr-definability-and-isomorphism-c2: all quoted values check")
