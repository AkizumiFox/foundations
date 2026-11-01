"""exr-vector-operations-b2 (a): (1,t,2) || (2,6,4) iff t = 3, with factor s = 2."""
from fractions import Fraction as Fr
# --- exact vector helpers (tuples of Fractions) ---
from fractions import Fraction as Fr


def v(*xs):
    return tuple(Fr(x) for x in xs)


def add(x, y):
    assert len(x) == len(y)
    return tuple(a + b for a, b in zip(x, y))


def smul(c, x):
    return tuple(Fr(c) * a for a in x)


def sub(x, y):
    return add(x, smul(-1, y))


def e(k, n):
    return tuple(Fr(1) if j == k else Fr(0) for j in range(1, n + 1))


def parallel(x, y):
    """Parallel per def-parallel-rn: y = cx or x = cy for some real c (tested exactly)."""
    def multiple(a, b):  # is b = c a for some c?
        if all(t == 0 for t in a):
            return all(t == 0 for t in b)
        k = next(i for i, t in enumerate(a) if t != 0)
        c = b[k] / a[k]
        return smul(c, a) == b
    return multiple(x, y) or multiple(y, x)
# ---
QUOTED = {"s": 2, "t": 3}
# (2,6,4) = s(1,t,2): first coordinate gives s, third is a check, second gives t
s = Fr(2, 1)
assert 4 == s * 2
t = Fr(6) / s
assert (s, t) == (QUOTED["s"], QUOTED["t"])
assert smul(QUOTED["s"], v(1, QUOTED["t"], 2)) == v(2, 6, 4)
for tt in [Fr(k, 2) for k in range(-10, 11)]:
    assert parallel(v(1, tt, 2), v(2, 6, 4)) == (tt == 3)
print("ok")
