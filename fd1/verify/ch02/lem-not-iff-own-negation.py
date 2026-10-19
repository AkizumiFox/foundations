"""lem-not-iff-own-negation (Ch 2, Section 2.4): the instance "x > 0 iff x <= 0" is false for every
real x (checked on a grid of rationals), and P <-> not P is false at both truth values of P."""
from fractions import Fraction as F

QUOTED = {"instance": "x > 0 iff x <= 0"}

for k in range(-400, 401):
    x = F(k, 16)
    assert ((x > 0) == (x <= 0)) is False
    assert (x <= 0) == (not (x > 0))   # the order convention of Section 2.1
for P in (True, False):
    assert (P == (not P)) is False
print("lem-not-iff-own-negation: all quoted values check")
