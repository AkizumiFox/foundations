"""exr-dot-product-b1: vectors orthogonal to (1,1,0) and (0,1,1) are exactly t(1,-1,1)."""
from fractions import Fraction as Fr
import itertools


def dot(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


QUOTED = {"direction": (1, -1, 1)}
d = QUOTED["direction"]
assert dot(d, (1, 1, 0)) == 0 and dot(d, (0, 1, 1)) == 0
grid = [Fr(p, q) for p in range(-4, 5) for q in (1, 2)]
for x in itertools.product(grid, repeat=3):
    both = dot(x, (1, 1, 0)) == 0 and dot(x, (0, 1, 1)) == 0
    t = x[0]
    assert both == (x == tuple(t * c for c in d))
print("ok")
