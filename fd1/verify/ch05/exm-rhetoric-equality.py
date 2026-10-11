"""exm-rhetoric-equality (Ch 5, Section 5.2): the limit-uniqueness chain; the row's examples:
|x - 2| < 1 gives |x^2 - 4| <= 5|x - 2|; 2x + 3 = 7 has exactly one solution x = 2."""
from fractions import Fraction as Fr

QUOTED = {"bound_factor": 5, "solution": 2}

assert 2 * QUOTED["solution"] + 3 == 7
assert all((2 * Fr(k, 4) + 3 == 7) == (Fr(k, 4) == 2) for k in range(-40, 41))   # linear: one root
for k in range(-99, 100):
    xv = 2 + Fr(k, 100)          # |x - 2| < 1
    assert 1 < xv < 3 and 3 < xv + 2 < 5
    assert abs(xv**2 - 4) == abs(xv - 2) * abs(xv + 2) <= QUOTED["bound_factor"] * abs(xv - 2)
# the chain |L - M| <= |a_n - L| + |a_n - M| on sample values
for L, M, an in [(Fr(1), Fr(3), Fr(2)), (Fr(-1), Fr(1, 2), Fr(5)), (Fr(0), Fr(0), Fr(7))]:
    assert abs(L - M) == abs((L - an) + (an - M)) <= abs(an - L) + abs(an - M)
print("exm-rhetoric-equality: all quoted values check")
