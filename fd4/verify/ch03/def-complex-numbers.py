"""def-complex-numbers: i*i = (-1, 0), and the non-example by minimal change
(a, b) * (c, d) = (ac + bd, ad + bc): commutative, unit (1, 0), (1,1)*(1,-1) = (0,0),
(1,1)*(c,d) = (c + d, d + c) never equals (1, 0)."""

from fractions import Fraction as Fr

QUOTED = {"i*i": (-1, 0), "(1,1)*(1,-1)": (0, 0)}

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


def star(p, q):
    (a, b), (c, d) = p, q
    return (a * c + b * d, a * d + b * c)


random.seed(2)
assert I * I == C(*QUOTED["i*i"])
assert star((1, 1), (1, -1)) == QUOTED["(1,1)*(1,-1)"]
for _ in range(500):
    p, q = (rq(), rq()), (rq(), rq())
    assert star(p, q) == star(q, p)
    assert star(p, (1, 0)) == p
    c, d = q
    s = star((1, 1), q)
    assert s == (c + d, d + c) and s != (1, 0)
print("def-complex-numbers: ok")
