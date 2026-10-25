"""exr-polynomial-gcd-b2: gcd over F_2."""
from _s0102_poly import P, gcd_run, mul, add, sub

QUOTED = {"field size": 2}
p = QUOTED["field size"]
f, g = P(1, 1, 0, 1, 1, p=p), P(1, 1, 1, 1, p=p)
assert mul(P(1, 0, p=p), g, p) == P(1, 1, 1, 1, 0, p=p)
assert sub(f, mul(P(1, 0, p=p), g, p), p) == P(1, 0, 1, p=p)
assert mul(P(1, 1, p=p), P(1, 0, 1, p=p), p) == g
rows, d = gcd_run(f, g, p)
assert len(rows) == 2 and d == P(1, 0, 1, p=p)
assert add(f, mul(P(1, 0, p=p), g, p), p) == P(1, 0, 1, p=p)
print("ok")
