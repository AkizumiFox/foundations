"""exr-conjugate-and-modulus-b2: Re z = (z + conj z)/2, Im z = (z - conj z)/(2i);
conj z = z iff Im z = 0; conj z = -z iff Re z = 0."""

from fractions import Fraction as Fr

QUOTED = {"Re z = (z + conj z)/2 and Im z = (z - conj z)/(2i); conj z = z iff Im z = 0; conj z = -z iff Re z = 0": True}

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


random.seed(11)
for _ in range(1000):
    z = rc()
    if random.random() < 0.2:
        z = C(z.a, 0)
    if random.random() < 0.2:
        z = C(0, z.b)
    assert (z + z.conj()) / C(2) == C(z.a)
    assert (z - z.conj()) / C(0, 2) == C(z.b)
    assert (z.conj() == z) == (z.b == 0)
    assert (z.conj() == -z) == (z.a == 0)
print("exr-conjugate-and-modulus-b2: ok")
