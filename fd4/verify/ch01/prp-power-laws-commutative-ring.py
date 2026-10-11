"""prp-power-laws-commutative-ring (a)-(d) on random Gaussian rationals, small exponents;
and iota(a^n) = iota(a)^n for real a."""

from fractions import Fraction as Fr

QUOTED = {"(a)-(d) and iota(a^n) = iota(a)^n, checked on random Gaussian rationals": True}

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


random.seed(4)
for _ in range(300):
    z, w = rc(), rc()
    m, n = random.randint(0, 6), random.randint(0, 6)
    assert z ** (m + n) == z ** m * z ** n
    assert (z ** m) ** n == z ** (m * n)
    assert (z * w) ** n == z ** n * w ** n
    if not z == C(0):
        assert not z ** n == C(0)
    a = rq()
    assert C(a) ** n == C(a ** n)
print("prp-power-laws-commutative-ring: ok")
