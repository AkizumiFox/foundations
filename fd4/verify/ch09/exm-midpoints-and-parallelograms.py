"""exm-midpoints-and-parallelograms: midpoint (3,1); m - a = (2,-3) = b - m; parallelogram data."""
import random
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
QUOTED = {"a+b": (6, 2), "m": (3, 1), "m-a": (2, -3), "b-a": (3, 1), "c-d": (3, 1),
          "a+c": (4, 3), "mid": (2, Fr(3, 2))}
a, b = v(1, 4), v(5, -2)
m = smul(Fr(1, 2), add(a, b))
assert add(a, b) == v(*QUOTED["a+b"]) and m == v(*QUOTED["m"])
assert sub(m, a) == v(*QUOTED["m-a"]) == sub(b, m)
a, b, c, d = v(0, 0), v(3, 1), v(4, 3), v(1, 2)
assert sub(b, a) == v(*QUOTED["b-a"]) and sub(c, d) == v(*QUOTED["c-d"])
assert add(a, c) == v(*QUOTED["a+c"]) == add(b, d)
assert smul(Fr(1, 2), add(a, c)) == v(*QUOTED["mid"]) == smul(Fr(1, 2), add(b, d))
# the general equivalence (B2 (b)) on random rational data, both ways
random.seed(1)
for _ in range(500):
    a, b, d = (v(*[random.randint(-6, 6) for _ in range(3)]) for _ in range(3))
    c = add(d, sub(b, a))  # forces b - a = c - d
    assert smul(Fr(1, 2), add(a, c)) == smul(Fr(1, 2), add(b, d))
    c2 = add(c, v(1, 0, 0))  # breaks it
    assert sub(b, a) != sub(c2, d) and smul(Fr(1, 2), add(a, c2)) != smul(Fr(1, 2), add(b, d))
print("ok")
