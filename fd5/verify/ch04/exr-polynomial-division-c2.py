"""exr-polynomial-division-c2: remainder modulo (x - a)(x - b), and x^100 mod x^2 - 3x + 2."""
from fractions import Fraction
from _s0102_poly import P, divmod_, xpow, mul, ev, add

QUOTED = {"exponent": 100}
r = divmod_(xpow(100), P(1, -3, 2))[1]
assert r == P(2 ** 100 - 1, 2 - 2 ** 100)
assert mul(P(1, -1), P(1, -2)) == P(1, -3, 2)
# the general formula on random-ish data, a != b, and the double-root formula
f = P(3, -1, 0, 5, 2, -7)
for a, b in ((Fraction(1), Fraction(-2)), (Fraction(3, 2), Fraction(5))):
    rr = divmod_(f, mul(P(1, -a), P(1, -b)))[1]
    s = add(mul(P(ev(f, a) / (a - b)), P(1, -b)), mul(P(ev(f, b) / (b - a)), P(1, -a)))
    assert rr == s
a = Fraction(2)
h, fa = divmod_(f, P(1, -a))
assert fa == P(ev(f, a))
rr = divmod_(f, mul(P(1, -a), P(1, -a)))[1]
assert rr == add(mul(P(ev(h, a)), P(1, -a)), P(ev(f, a)))
print("ok")
