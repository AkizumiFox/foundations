"""exr-conjugate-and-modulus-c2: the inverse of a + bi (a, b rational, not both 0) is
a/(a^2 + b^2) + (-b/(a^2 + b^2)) i, with rational parts; (1 + 2i)^(-1) = 1/5 - (2/5) i."""

from fractions import Fraction
from fractions import Fraction as Fr

QUOTED = {"(1+2i)^-1": (Fraction(1, 5), Fraction(-2, 5))}

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


random.seed(12)
for _ in range(1000):
    z = rc()
    if z == C(0):
        continue
    n = z.a ** 2 + z.b ** 2
    inv = C(z.a / n, -z.b / n)
    assert z * inv == C(1) and isinstance(inv.a, Fr) and isinstance(inv.b, Fr)
assert C(1, 2).inv() == C(*QUOTED["(1+2i)^-1"])
print("exr-conjugate-and-modulus-c2: ok")
