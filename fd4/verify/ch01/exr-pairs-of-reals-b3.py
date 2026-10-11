"""exr-pairs-of-reals-b3: (a,b)*(ta,-tb) = (t(a^2 - b^2), 0); (a,a)*(1,-1) = (0,0), (a,-a)*(1,1) = (0,0);
the eliminations a(ac+bd) - b(ad+bc) = (a^2-b^2)c and b(ac+bd) - a(ad+bc) = (b^2-a^2)d;
(2,1)*(2/3,-1/3) = (1,0);
(a,a)*(c,d) = (a(c+d), a(c+d)) and (a,-a)*(c,d) = (a(c-d), -a(c-d)), never (1,0)."""

from fractions import Fraction as Fr

QUOTED = {"(2,1)*(2/3,-1/3)": (1, 0)}

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


random.seed(8)
for _ in range(2000):
    a, b, c, d, t = (rq() for _ in range(5))
    assert star((a, b), (t * a, -t * b)) == (t * (a * a - b * b), 0)
    assert star((a, a), (1, -1)) == (0, 0) and star((a, -a), (1, 1)) == (0, 0)
    e1, e2 = star((a, b), (c, d))
    assert a * e1 - b * e2 == (a * a - b * b) * c
    assert b * e1 - a * e2 == (b * b - a * a) * d
    if a * a != b * b:
        t = 1 / (a * a - b * b)
        assert star((a, b), (t * a, -t * b)) == (1, 0)
    # (a, +-a) has no inverse: (a,a)*(c,d) = (a(c+d), a(c+d)), (a,-a)*(c,d) = (a(c-d), -a(c-d))
    assert star((a, a), (c, d)) == (a * (c + d), a * (c + d))
    assert star((a, -a), (c, d)) == (a * (c - d), -a * (c - d))
    assert star((a, a), (c, d)) != (1, 0) and star((a, -a), (c, d)) != (1, 0)
assert star((2, 1), (Fr(2, 3), Fr(-1, 3))) == QUOTED["(2,1)*(2/3,-1/3)"]
print("exr-pairs-of-reals-b3: ok")
