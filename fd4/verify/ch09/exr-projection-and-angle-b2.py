"""exr-projection-and-angle-b2: (e) counterexample; (a)-(d), (f) on random data."""
from fractions import Fraction as Fr
import random
QUOTED = {"e": ((Fr(1, 2), Fr(1, 2)), (1, 0))}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
proj = lambda x, y: tuple(dot(x, y) / dot(y, y) * b for b in y)
assert (proj((1, 0), (1, 1)), proj((1, 1), (1, 0))) == QUOTED["e"]
random.seed(2)
for _ in range(300):
    x, y, z = (tuple(random.randint(-6, 6) for _ in range(3)) for _ in range(3))
    if dot(y, y) == 0:
        continue
    assert proj(proj(x, y), y) == proj(x, y)
    assert proj(tuple(a + b for a, b in zip(x, z)), y) == tuple(a + b for a, b in zip(proj(x, y), proj(z, y)))
    c = random.choice([-2, 3, Fr(1, 2)])
    assert proj(x, tuple(c * b for b in y)) == proj(x, y)
    pp = proj(x, y); assert dot(pp, pp) <= dot(x, x)
    if dot(x, y) == 0:
        assert proj(x, y) == (0, 0, 0)
print("ok")
