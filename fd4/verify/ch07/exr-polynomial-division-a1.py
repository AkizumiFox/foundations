"""exr-polynomial-division-a1: (c) division by a constant; (d) x and 2x divide each other in Q[x]."""
from fractions import Fraction
from _s0102_poly import P, divmod_, mul

QUOTED = {"(d) scale": Fraction(1, 2)}
f = P(3, -1, 0, 2)
for c in (2, Fraction(-5, 3)):
    q, r = divmod_(f, P(c))
    assert q == mul(P(1 / Fraction(c)), f) and r == ()
assert mul(P(QUOTED["(d) scale"]), P(2, 0)) == P(1, 0) and mul(P(2), P(1, 0)) == P(2, 0)
# in F_2 the only non-zero constant is 1
assert [c for c in range(2) if c % 2 != 0] == [1]
print("ok")
