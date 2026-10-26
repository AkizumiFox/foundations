"""exr-polynomial-division-b3: remainder of x^100 by x^2 - 1 over several fields."""
from _s0102_poly import P, divmod_, xpow, mul, add, norm

QUOTED = {"exponent": 100, "upper index": 49}
for p in (None, 2, 3, 5, 7):
    assert divmod_(xpow(100, p), P(1, 0, -1, p=p), p)[1] == P(1, p=p)
    s = norm([1 if (k % 2 == 0) else 0 for k in range(2 * QUOTED["upper index"] + 1)], p)
    assert add(mul(P(1, 0, -1, p=p), s, p), P(1, p=p), p) == xpow(QUOTED["exponent"], p)
# over F_2 the evaluation equations collapse: 1 = a + b has two solutions
assert [(a, b) for a in (0, 1) for b in (0, 1) if (a + b) % 2 == 1] == [(0, 1), (1, 0)]
print("ok")
