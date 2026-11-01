"""exr-vector-operations-a1 (a): 2(1,0,-1) - 3(0,1,1) + (1,1,1) = (3,-2,-4) = 3e1 - 2e2 - 4e3."""
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
QUOTED = {"2a": (2, 0, -2), "3b": (0, 3, 3), "result": (3, -2, -4), "coeffs": (3, -2, -4)}
assert smul(2, v(1, 0, -1)) == v(*QUOTED["2a"]) and smul(3, v(0, 1, 1)) == v(*QUOTED["3b"])
r = add(add(smul(2, v(1, 0, -1)), smul(-3, v(0, 1, 1))), v(1, 1, 1))
assert r == v(*QUOTED["result"])
s = v(0, 0, 0)
for k, c in enumerate(QUOTED["coeffs"], start=1):
    s = add(s, smul(c, e(k, 3)))
assert s == r
print("ok")
