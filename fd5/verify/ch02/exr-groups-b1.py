"""exr-groups-b1: {1,3,5,7} in Z/8Z is closed under multiplication with every element its
own inverse; Z/6Z minus [0] is not closed; 1 + 1 = 2 is even; positives: closure and
reciprocals on sample rationals."""
from fractions import Fraction
QUOTED = {"units8": {1, 3, 5, 7}, "z6": (2, 3, 0), "odd_sum": 2}
S = QUOTED["units8"]
assert all(a * b % 8 in S for a in S for b in S)
assert all(a * a % 8 == 1 for a in S)
a, b, c = QUOTED["z6"]
assert a * b % 6 == c
assert 1 + 1 == QUOTED["odd_sum"] and QUOTED["odd_sum"] % 2 == 0
xs = [Fraction(p, q) for p in range(1, 9) for q in range(1, 9)]
assert all(x * y > 0 and 1 / x > 0 for x in xs for y in xs)
print("exr-groups-b1: ok")
