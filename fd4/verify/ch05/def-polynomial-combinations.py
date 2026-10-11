"""def-polynomial-combinations: the opening question, the non-example, and the Quick check."""
from _s0102_poly import P, mul, sub, add, gcd_run, ev, deg

QUOTED = {"non-example degree": 1}
f, g = P(1, 0, -1), P(1, 1, -2)
assert f == mul(P(1, -1), P(1, 1)) and g == mul(P(1, -1), P(1, 2))
assert sub(g, f) == P(1, -1)
assert gcd_run(f, g)[1] == P(1, -1)
assert deg(add(P(1, 0, 0, 0), P(-1, 0, 1, 0))) == QUOTED["non-example degree"]
assert ev(P(1, 1), 0) == 1 and ev(P(2), 0) == 2  # (1 + 1)(0) = 2
print("ok")
