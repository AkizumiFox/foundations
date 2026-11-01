"""thm-projection-closest-point: (a), (b), (c) and the defect identity of the Alternatively paragraph, on random rational data."""
from fractions import Fraction as Fr
import random

QUOTED = {"b": True, "defect": True}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
random.seed(1)
for _ in range(2000):
    n = random.randint(1, 5)
    x = [Fr(random.randint(-9, 9), random.randint(1, 4)) for _ in range(n)]
    y = [Fr(random.randint(-9, 9), random.randint(1, 4)) for _ in range(n)]
    if dot(y, y) == 0:
        continue
    t0 = dot(x, y) / dot(y, y); p = [t0 * b for b in y]; e = [a - q for a, q in zip(x, p)]
    assert dot(e, y) == 0
    t = Fr(random.randint(-20, 20), random.randint(1, 5))
    v = [a - t * b for a, b in zip(x, y)]
    assert dot(v, v) == dot(e, e) + (t - t0) ** 2 * dot(y, y)
    if t != t0:
        assert dot(v, v) > dot(e, e)
    assert dot(x, x) == dot(p, p) + dot(e, e)
    assert dot(p, p) == dot(x, y) ** 2 / dot(y, y)
    assert dot(x, x) * dot(y, y) - dot(x, y) ** 2 == dot(y, y) * dot(e, e)
print("ok")
