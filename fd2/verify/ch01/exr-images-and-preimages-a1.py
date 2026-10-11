"""exr-images-and-preimages-a1 (b) (Ch 6, Section 6.6): squaring, B1 = [0,4], B2 = [1,9]."""
from fractions import Fraction as F
QUOTED = {"B1": [0, 4], "B2": [1, 9], "f^{-1}(B2) endpoints": [-3, -1, 1, 3]}
xs = [F(k, 100) for k in range(-500, 501)]
sq = lambda x: x * x
lhs = {x for x in xs if 1 <= sq(x) <= 4}
assert lhs == {x for x in xs if -2 <= x <= -1 or 1 <= x <= 2}
p1 = {x for x in xs if 0 <= sq(x) <= 4}
p2 = {x for x in xs if 1 <= sq(x) <= 9}
assert p1 == {x for x in xs if -2 <= x <= 2}
assert p2 == {x for x in xs if -3 <= x <= -1 or 1 <= x <= 3}
assert p1 & p2 == lhs
print("exr-images-and-preimages-a1: all quoted values check")
