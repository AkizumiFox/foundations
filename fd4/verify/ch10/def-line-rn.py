"""def-line-rn and def-collinear: (1,0,0)+t(-1,1,0) = (1-t,t,0); Quick check (c) t = 2; opening plane points."""
from fractions import Fraction as Fr
# --- exact vector helpers (tuples of Fractions) ---


def v(*xs):
    return tuple(Fr(x) for x in xs)


def add(x, y):
    assert len(x) == len(y)
    return tuple(a + b for a, b in zip(x, y))


def smul(c, x):
    return tuple(Fr(c) * a for a in x)


def sub(x, y):
    return add(x, smul(-1, y))


def dot(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


def multiple_of(b, a):
    """Is b = c a for some real c? (a != 0)"""
    k = next(i for i, t in enumerate(a) if t != 0)
    c = b[k] / a[k]
    return smul(c, a) == b# ---

QUOTED = {"qc_c_t": 2, "qc_c_point": (3, 5, 7)}
for t in [Fr(-3), Fr(0), Fr(1), Fr(5, 7)]:
    assert add(v(1, 0, 0), smul(t, v(-1, 1, 0))) == v(1 - t, t, 0)
assert add(v(1, 1, 1), smul(QUOTED["qc_c_t"], v(1, 2, 3))) == v(*QUOTED["qc_c_point"])
# opening: the three points satisfy x1 + x2 + x3 = 1
for p in [v(1, 0, 0), v(0, 1, 0), v(0, 0, 1)]:
    assert sum(p) == 1
# (0,0,1) not on (1,0,0) + R(-1,1,0): would need (0,0,1)-(1,0,0) multiple of (-1,1,0)
assert not multiple_of(sub(v(0, 0, 1), v(1, 0, 0)), v(-1, 1, 0))
# second name of the same line: (0,1,0) + R(2,-2,0)
assert multiple_of(sub(v(0, 1, 0), v(1, 0, 0)), v(-1, 1, 0)) and smul(-2, v(-1, 1, 0)) == v(2, -2, 0)
print("ok")
