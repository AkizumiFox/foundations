"""def-vector-operations-rn: the two worked sums x + y and 2x - y for x = (1,0,-1), y = (2,5,3)."""
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
QUOTED = {"x+y": (3, 5, 2), "2x": (2, 0, -2), "-y": (-2, -5, -3), "2x-y": (0, -5, -5)}
x, y = v(1, 0, -1), v(2, 5, 3)
assert add(x, y) == v(*QUOTED["x+y"])
assert smul(2, x) == v(*QUOTED["2x"])
assert smul(-1, y) == v(*QUOTED["-y"])
assert sub(smul(2, x), y) == v(*QUOTED["2x-y"])
# opening motivation: (1,4) moved by (3,-1) once and twice
assert add(v(1, 4), v(3, -1)) == v(4, 3) and add(v(1, 4), smul(2, v(3, -1))) == v(7, 2)
# instance before prp-vector-space-laws-rn: c = 2, x = (1,-3), y = (4,5)
assert add(v(1, -3), v(4, 5)) == v(5, 2)
assert smul(2, add(v(1, -3), v(4, 5))) == v(10, 4) == add(smul(2, v(1, -3)), smul(2, v(4, 5)))
assert smul(2, v(1, -3)) == v(2, -6) and smul(2, v(4, 5)) == v(8, 10)
# instance before lem-vector-sums-coordinatewise: (1,2) + (0,3) + (4,-1) = (5,4)
assert add(add(v(1, 2), v(0, 3)), v(4, -1)) == v(5, 4)
print("ok")
