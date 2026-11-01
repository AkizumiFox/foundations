"""prp-complex-arithmetic-laws (b): both real parts of (zw)u and z(wu) equal ace - adf - bcf - bde,
both imaginary parts equal acf + ade + bce - bdf; (c) the displayed expansion of z(w + u).
Checked as polynomial identities at many random rational points (degree 3 in six variables)."""

from fractions import Fraction as Fr

QUOTED = {"real": "ace - adf - bcf - bde", "imag": "acf + ade + bce - bdf"}

import random


class C:
    """Exact complex numbers a + bi with rational parts (pairs, as in def-complex-numbers)."""

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, C) else C(o)
        return C(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.a, -self.b)

    def __sub__(self, o):
        o = o if isinstance(o, C) else C(o)
        return self + (-o)

    def __rsub__(self, o):
        return C(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, C) else C(o)
        return C(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __pow__(self, n):
        r = C(1)
        for _ in range(n):
            r = r * self
        return r

    def conj(self):
        return C(self.a, -self.b)

    def norm2(self):
        return self.a * self.a + self.b * self.b

    def inv(self):
        n = self.norm2()
        assert n != 0
        return C(self.a / n, -self.b / n)

    def __truediv__(self, o):
        o = o if isinstance(o, C) else C(o)
        return self * o.inv()

    def __eq__(self, o):
        o = o if isinstance(o, C) else C(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"({self.a}) + ({self.b})i"


I = C(0, 1)


def rq():
    return Fr(random.randint(-60, 60), random.randint(1, 12))


def rc():
    return C(rq(), rq())


random.seed(3)
for _ in range(3000):
    a, b, c, d, e, f = (rq() for _ in range(6))
    re = a * c * e - a * d * f - b * c * f - b * d * e
    im = a * c * f + a * d * e + b * c * e - b * d * f
    # the two expansions written in the proof
    lhs_re = (a * c - b * d) * e - (a * d + b * c) * f
    lhs_im = (a * c - b * d) * f + (a * d + b * c) * e
    rhs_re = a * (c * e - d * f) - b * (c * f + d * e)
    rhs_im = a * (c * f + d * e) + b * (c * e - d * f)
    assert lhs_re == rhs_re == re and lhs_im == rhs_im == im
    z, w, u = C(a, b), C(c, d), C(e, f)
    assert (z * w) * u == z * (w * u) == C(re, im)
    # (c)
    zwu = z * (w + u)
    assert zwu == C((a * c - b * d) + (a * e - b * f), (a * d + b * c) + (a * f + b * e)) == z * w + z * u
    # (a), (d)
    assert z * w == w * z and z + w == w + z and z * C(1) == z and z + (-z) == C(0)
print("prp-complex-arithmetic-laws: ok")
