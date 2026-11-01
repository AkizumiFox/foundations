"""exr-vector-operations-b1: counterexamples for (b) and (d); (d) true in R^1 and for non-zero middle vector."""
import random, itertools
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
# (b): c = 0, x = e1, y = e2
assert smul(0, e(1, 2)) == smul(0, e(2, 2)) and e(1, 2) != e(2, 2)
# (d): e1 || 0, 0 || e2, e1 not || e2
z = v(0, 0)
assert parallel(e(1, 2), z) and parallel(z, e(2, 2)) and not parallel(e(1, 2), e(2, 2))
# (d) in R^1: any two reals are parallel
for a, b in itertools.product(range(-3, 4), repeat=2):
    assert parallel(v(a), v(b))
# (d) with y != 0: transitive (random small vectors in R^2 built as multiples)
random.seed(3)
for _ in range(500):
    y = v(random.randint(-4, 4), random.randint(-4, 4))
    if y == z:
        continue
    s, t = Fr(random.randint(-3, 3)), Fr(random.randint(-3, 3))
    x, w = smul(s, y), smul(t, y)
    assert parallel(x, y) and parallel(y, w) and parallel(x, w)
# (c) and (e) sanity: (c - d)x = 0 with x != 0 forces c = d
x = v(0, 2)
for c, d in itertools.product(range(-2, 3), repeat=2):
    assert (smul(c, x) == smul(d, x)) == (c == d)
print("ok")
