"""exm-polynomial-long-division: the two divisions, their passes and checks."""
from fractions import Fraction
from _s0102_poly import P, mul, add, sub, divmod_

QUOTED = {"(i) remainder": (Fraction(11, 2), Fraction(7, 2)), "(i) quotient constant (negated)": Fraction(3, 2),
          "(i) check constant (negated)": Fraction(9, 2), "(ii) F_3 inverse of 2": 2}

f, g = P(2, -3, 1, 4, -1), P(2, -1, 3)
q, r = divmod_(f, g)
assert q == P(1, -1, -Fraction(3, 2)) and r == P(*QUOTED["(i) remainder"])
r1 = sub(f, mul(P(1, 0, 0), g)); assert r1 == P(-2, -2, 4, -1)
r2 = sub(r1, mul(P(-1, 0), g)); assert r2 == P(-3, 7, -1)
r3 = sub(r2, mul(P(-Fraction(3, 2)), g)); assert r3 == r
assert mul(q, g) == P(2, -3, 1, -Fraction(3, 2), -QUOTED["(i) check constant (negated)"])
# (ii) in F_3
p = 3
assert (2 * QUOTED["(ii) F_3 inverse of 2"]) % p == 1
f, g = P(1, 0, 0, 1, 2, p=p), P(2, 0, 1, p=p)
q, r = divmod_(f, g, p)
assert q == P(2, 0, 2, p=p) and r == P(1, 0, p=p)
assert mul(P(2, 0, 0, p=p), g, p) == P(1, 0, 2, 0, 0, p=p)
assert mul(P(2, p=p), g, p) == P(1, 0, 2, p=p)
r1 = sub(f, mul(P(2, 0, 0, p=p), g, p), p); assert r1 == P(1, 1, 2, p=p)
assert sub(r1, mul(P(2, p=p), g, p), p) == P(1, 0, p=p)
assert mul(q, g, p) == P(1, 0, 0, 0, 2, p=p)
# the hook of the section: x^4 + 2x^3 - x + 3 = (x^2 + x)(x^2 + x - 1) + 3
assert add(mul(P(1, 1, 0), P(1, 1, -1)), P(3)) == P(1, 2, 0, -1, 3)
print("ok")
