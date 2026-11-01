"""prp-polynomial-gcd-field-extension: the example and the Quick check after it."""
from _s0102_poly import P, divmod_, gcd_run, mul

QUOTED = {"remainder of x^2 + 1 by x - 1": 2}
q, r = divmod_(P(1, 0, 1), P(1, -1))
assert q == P(1, 1) and r == P(QUOTED["remainder of x^2 + 1 by x - 1"])
assert gcd_run(P(1, 0, 1), P(1, -1))[1] == P(1)
# (x - i)(x + i) = x^2 + 1 with Gaussian integers as pairs (a, b) = a + bi
def cm(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])
# coefficients: x^2 + (i - i) x + (-i)(i)
assert (0 + 0, 1 - 1) == (0, 0) and cm((0, -1), (0, 1)) == (1, 0)
# check: gcd(x^2 - 2, x^3 - 2x) over Q
rows, d = gcd_run(P(1, 0, -2), P(1, 0, -2, 0))
assert d == P(1, 0, -2)
assert divmod_(P(1, 0, -2, 0), P(1, 0, -2)) == (P(1, 0), ())
print("ok")
