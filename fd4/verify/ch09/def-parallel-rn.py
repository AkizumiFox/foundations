"""def-parallel-rn: quick check values; e_1 and 0 are parallel only via the second clause."""
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
QUOTED = {"factor": -2, "t_from": (2, Fr(3, 2)), "s_from": (Fr(1, 2), Fr(2, 3))}
assert smul(QUOTED["factor"], v(-1, -2, 3)) == v(2, 4, -6)
assert smul(-3, v(-1, 2)) == v(3, -6)  # hook of the subsection
x, y = v(1, 2), v(2, 3)
assert (y[0] / x[0], y[1] / x[1]) == QUOTED["t_from"]
assert (x[0] / y[0], x[1] / y[1]) == QUOTED["s_from"]
assert not parallel(x, y)
z = v(0, 0)
assert parallel(z, e(1, 2)) and smul(0, e(1, 2)) == z
assert all(smul(c, z) != e(1, 2) for c in range(-5, 6))
# (3,-2) = 3e1 - 2e2 and (0,5,0) = 5 e2 (text after prp-standard-basis-expansion)
assert tuple(a + b for a, b in zip(smul(3, e(1, 2)), smul(-2, e(2, 2)))) == v(3, -2)
assert smul(5, e(2, 3)) == v(0, 5, 0)
print("ok")
