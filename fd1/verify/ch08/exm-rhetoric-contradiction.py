"""exm-rhetoric-contradiction (Ch 5, Section 5.1): a <= b + eps for all eps > 0 gives a <= b;
eps = (a - b)/2 > 0 when a > b, and a <= b + (a - b)/2 iff a <= b."""
from fractions import Fraction as Fr

QUOTED = {"eps": "(a-b)/2"}

# a <= b + (a - b)/2  <=>  2a <= a + b  <=>  a <= b: the linear identity 2((b + eps) - a) = b - a
grid = [Fr(k, 3) for k in range(-9, 10)]
for av in grid:
    for bv in grid:
        e = (av - bv) / 2
        assert 2 * ((bv + e) - av) == bv - av
        assert (av <= bv + e) == (av <= bv)
for av in [Fr(3), Fr(1, 2), Fr(-2)]:
    for bv in [Fr(1), Fr(0), Fr(-5)]:
        if av > bv:
            e = (av - bv) / 2
            assert e > 0
            assert not (av <= bv + e)  # the instance is violated, so the hypothesis fails: a > b impossible
print("exm-rhetoric-contradiction: all quoted values check")
