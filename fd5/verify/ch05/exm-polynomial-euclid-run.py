"""exm-polynomial-euclid-run, the warning after it, and the Quick check after the warning."""
from _s0102_poly import P, mul, add, sub, gcd_run, neg

QUOTED = {"K": 3, "warning degrees": (3, 4)}
f, g = P(1, -1, -3, 1, 2), P(1, 0, -2, -1)
rows, d = gcd_run(f, g)
assert [(r[1], r[3]) for r in rows] == [(P(1, -1), P(-1, 0, 1)), (P(-1, 0), P(-1, -1)), (P(1, -1), ())]
assert len(rows) == QUOTED["K"] and d == P(1, 1)
# back-substitution
assert add(g, mul(P(1, 0), P(-1, 0, 1))) == P(-1, -1)
assert add(mul(P(1, 0), f), mul(P(-1, 1, 1), g)) == P(-1, -1)
a, b = P(-1, 0), P(1, -1, -1)
assert mul(a, f) == P(-1, 1, 3, -1, -2, 0) and mul(b, g) == P(1, -1, -3, 1, 3, 1)
assert add(mul(a, f), mul(b, g)) == P(1, 1)
# warning
a2, b2 = add(a, g), sub(b, f)
assert add(mul(a2, f), mul(b2, g)) == P(1, 1)
assert (len(a2) - 1, len(b2) - 1) == QUOTED["warning degrees"]
# quick check: x^3 and x^2 + 1
rows, d = gcd_run(P(1, 0, 0, 0), P(1, 0, 1))
assert [(r[1], r[3]) for r in rows] == [(P(1, 0), P(-1, 0)), (P(-1, 0), P(1)), (P(-1, 0), ())]
assert d == P(1)
assert add(mul(P(1, 0), P(1, 0, 0, 0)), mul(P(-1, 0, 1), P(1, 0, 1))) == P(1)
print("ok")
