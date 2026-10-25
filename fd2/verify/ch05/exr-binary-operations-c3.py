"""exr-binary-operations-c3: phi(x) = 1 - x is its own inverse; transported product
x * x' = 1 - (1 - x)(1 - x') = x + x' - x x'; identity 0 = phi(1); non-invertible 1 = phi(0)."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"identity": 0, "non_invertible": 1}


phi = lambda x: 1 - x
star = lambda x, y: phi(phi(x) * phi(y))
pts = [F(k, 4) for k in range(-5, 6)]
for x in pts:
    assert phi(phi(x)) == x
for x, y in product(pts, repeat=2):
    assert star(x, y) == x + y - x * y
assert phi(1) == 0 and phi(0) == 1
assert all(star(QUOTED["identity"], x) == x for x in pts)
assert all(star(QUOTED["non_invertible"], x) == 1 for x in pts)
print("exr-binary-operations-c3: all quoted values check")
