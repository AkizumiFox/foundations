"""exr-lines-and-segments-a1: direction (2,1,-2); (5,1,-2) at t = 2; midpoint (2,-1/2,1)."""
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

QUOTED = {"dir": (2, 1, -2), "t": 2, "point": (5, 1, -2), "mid": (2, Fr(-1, 2), 1)}
P, Q = v(1, -1, 2), v(3, 0, 0)
assert sub(Q, P) == QUOTED["dir"]
assert add(P, smul(QUOTED["t"], sub(Q, P))) == QUOTED["point"]
assert smul(Fr(1, 2), add(P, Q)) == QUOTED["mid"]
print("ok")
