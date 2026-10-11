"""exr-polynomial-gcd-b1: gcd of x^3 + x^2 + x + 1 and x^3 + x + 2 over Q."""
from fractions import Fraction
from _s0102_poly import P, gcd_run, mul, add, ev

QUOTED = {"K": 3, "Bezout coefficient": Fraction(1, 2)}
f, g = P(1, 1, 1, 1), P(1, 0, 1, 2)
rows, d = gcd_run(f, g)
assert [(r[1], r[3]) for r in rows] == [(P(1), P(1, 0, -1)), (P(1, 0), P(2, 2)), (P(Fraction(1, 2), -Fraction(1, 2)), ())]
assert len(rows) == QUOTED["K"] and d == P(1, 1)
assert add(mul(P(-1, 0), f), mul(P(1, 1), g)) == P(2, 2)
h = QUOTED["Bezout coefficient"]
a, b = P(-h, 0), P(h, h)
assert mul(a, f) == P(-h, -h, -h, -h, 0)
assert mul(b, g) == P(h, h, h, 3 * h, 2 * h)
assert add(mul(a, f), mul(b, g)) == P(1, 1)
assert ev(f, -1) == 0 and ev(g, -1) == 0
# no other rational root: any common root is a root of x + 1
print("ok")
