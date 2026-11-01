"""thm-conjugate-properties (a)-(e) on random Gaussian rationals (moduli compared through squares),
and the second route for (d): (ac - bd)^2 + (ad + bc)^2 = (a^2 + b^2)(c^2 + d^2).
Also -conj: z -> -conj(z) sends 1 to -1 and does not respect products."""

from fractions import Fraction as Fr

QUOTED = {"second_route": "(ac - bd)^2 + (ad + bc)^2 = (a^2 + b^2)(c^2 + d^2)"}

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


random.seed(10)
for _ in range(3000):
    z, w = rc(), rc()
    assert (z + w).conj() == z.conj() + w.conj() and z.conj().conj() == z
    assert (z * w).conj() == z.conj() * w.conj()
    assert z * z.conj() == C(z.norm2()) and z + z.conj() == C(2 * z.a)
    assert (z * w).norm2() == z.norm2() * w.norm2() and z.conj().norm2() == z.norm2()
    assert (z.norm2() == 0) == (z == C(0))
    a, b, c, d = z.a, z.b, w.a, w.b
    assert (a * c - b * d) ** 2 + (a * d + b * c) ** 2 == (a * a + b * b) * (c * c + d * d)
r = lambda t: -t.conj()
assert r(C(1)) == C(-1) and r(C(1) * C(1)) == C(-1) and r(C(1)) * r(C(1)) == C(1)
print("thm-conjugate-properties: ok")
