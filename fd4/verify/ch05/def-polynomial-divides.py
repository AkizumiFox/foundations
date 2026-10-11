"""def-polynomial-divides: the four instances, the F_3 Quick check, and the associates check."""
from fractions import Fraction
from _s0102_poly import P, mul, divmod_, ev, monic

QUOTED = {"value of x^2 + 1 at -1 over Q": 2, "F_3 check: 2^2 + 1": 5,
          "3x + 6 monic associate": (1, 2), "scale": Fraction(1, 3)}

assert mul(P(1, -1), P(1, 1)) == P(1, 0, -1)
assert mul(P(2, -2), P(Fraction(1, 2), Fraction(1, 2))) == P(1, 0, -1)
assert mul(P(1, 1, p=2), P(1, 1, p=2), p=2) == P(1, 0, 1, p=2)
# over Q, x + 1 does not divide x^2 + 1: remainder is the value at -1
assert divmod_(P(1, 0, 1), P(1, 1))[1] == P(2) and ev(P(1, 0, 1), -1) == QUOTED["value of x^2 + 1 at -1 over Q"]
# over F_3: value at 2 is 5 = 2 != 0, so no division
assert 2 ** 2 + 1 == QUOTED["F_3 check: 2^2 + 1"] and 5 % 3 == 2
assert divmod_(P(1, 0, 1, p=3), P(1, 1, p=3), p=3)[1] == P(2, p=3)
# associates of 3x + 6
assert monic(P(3, 6)) == P(*QUOTED["3x + 6 monic associate"]) == mul(P(QUOTED["scale"]), P(3, 6))
print("ok")
