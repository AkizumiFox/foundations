"""exr-dot-product-b3: x = (r/<a,a>)a solves <a,x> = r; v = a_k e_j - a_j e_k is orthogonal to a; example a = (1,1), r = 2."""
from fractions import Fraction as Fr
import random


def dot(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


QUOTED = {"x": (1, 1), "other": (2, 0)}
a, r = (1, 1), 2
x = tuple(Fr(r, dot(a, a)) * c for c in a)
assert x == QUOTED["x"] and dot(a, x) == r
o = QUOTED["other"]
assert dot(a, o) == r and o[0] * a[1] != o[1] * a[0]  # not parallel
random.seed(1)
for _ in range(300):
    n = random.randint(2, 5)
    a = tuple(random.randint(-5, 5) for _ in range(n))
    if all(c == 0 for c in a):
        continue
    r = Fr(random.randint(-9, 9))
    x = tuple(r / dot(a, a) * c for c in a)
    assert dot(a, x) == r
    k = next(i for i in range(n) if a[i] != 0)
    j = 0 if k != 0 else 1
    v = [0] * n
    v[j] += a[k]
    v[k] -= a[j]
    assert dot(a, v) == 0 and v[j] == a[k] != 0
print("ok")
