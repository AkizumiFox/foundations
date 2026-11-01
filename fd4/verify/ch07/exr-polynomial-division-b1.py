"""exr-polynomial-division-b1: the division over Q and over F_5."""
from fractions import Fraction
from _s0102_poly import P, divmod_, mul, sub

QUOTED = {"(a) quotient coefficients": (Fraction(1, 3), Fraction(1, 9)), "(a) remainder constant": Fraction(44, 9),
          "(a) check constant": Fraction(1, 9), "(b) remainder": 2, "(b) inverse of 2": 3}
f, g = P(1, -3, 0, 2, -5), P(3, 0, -1)
q, r = divmod_(f, g)
assert q == P(Fraction(1, 3), -1, Fraction(1, 9)) and r == P(1, -QUOTED["(a) remainder constant"])
assert mul(g, q) == P(1, -3, 0, 1, -QUOTED["(a) check constant"])
r1 = sub(f, mul(P(Fraction(1, 3), 0, 0), g)); assert r1 == P(-3, Fraction(1, 3), 2, -5)
r2 = sub(r1, mul(P(-1, 0), g)); assert r2 == P(Fraction(1, 3), 1, -5)
assert sub(r2, mul(P(Fraction(1, 9)), g)) == r
p = 5
assert 2 * QUOTED["(b) inverse of 2"] % p == 1
f, g = P(1, 2, 0, 3, 1, p=p), P(2, 0, 3, p=p)
q, r = divmod_(f, g, p)
assert q == P(3, 1, 3, p=p) and r == P(QUOTED["(b) remainder"], p=p)
assert mul(P(3, 0, 0, p=p), g, p) == P(1, 0, 4, 0, 0, p=p)
assert mul(P(1, 0, p=p), g, p) == P(2, 0, 3, 0, p=p)
assert mul(P(3, p=p), g, p) == P(1, 0, 4, p=p)
r1 = sub(f, mul(P(3, 0, 0, p=p), g, p), p); assert r1 == P(2, 1, 3, 1, p=p)
r2 = sub(r1, mul(P(1, 0, p=p), g, p), p); assert r2 == P(1, 0, 1, p=p)
print("ok")
