"""exm-polynomial-remainders-without-dividing and the Quick check after it."""
from _s0102_poly import P, divmod_, ev, mul, sub

QUOTED = {"f(2)": 19, "terms of f(2)": (32, 24, 4, 7)}
f = P(1, 0, -3, 0, 2, 7)
assert ev(f, 2) == QUOTED["f(2)"] == 32 - 24 + 4 + 7
assert divmod_(f, P(1, -2))[1] == P(19)
assert divmod_(P(1, 0, 0, 0, 0, 0), P(1, -1, 0))[1] == P(1, 0)
assert sub(P(1, 0, 0, 0, 0, 0), P(1, 0)) == mul(P(1, -1, 0), P(1, 1, 1, 1))
# check: x^7 + 1 at -1 and 1
assert ev(P(1, 0, 0, 0, 0, 0, 0, 1), -1) == 0 and ev(P(1, 0, 0, 0, 0, 0, 0, 1), 1) == 2
assert divmod_(P(1, 0, 0, 0, 0, 0, 0, 1, p=2), P(1, 1, p=2), p=2)[1] == ()
print("ok")
