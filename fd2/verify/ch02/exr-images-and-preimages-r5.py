"""exr-images-and-preimages-r5: f = x on (-inf, 0] glued with 3x on [0, inf);
inverse g = y on (-inf, 0] glued with y/3 on [0, inf); f^{-1}([-4, 9]) = [-4, 3]."""
from fractions import Fraction as F

QUOTED = {"preimage": (-4, 3), "g_at": {-4: -4, 9: 3}}


def f(x):
    return x if x <= 0 else 3 * x


def g(y):
    return y if y <= 0 else y / 3


# the pieces agree on the overlap {0}
assert 0 == 3 * 0 and F(0) == F(0) / 3
grid = [F(k, 7) for k in range(-200, 201)]
for t in grid:
    assert g(f(t)) == t and f(g(t)) == t          # two-sided inverse
    assert (f(t) <= 0) == (t <= 0) and (g(t) <= 0) == (t <= 0)  # sign kept
lo, hi = QUOTED["preimage"]
for x in grid:
    assert (-4 <= f(x) <= 9) == (lo <= x <= hi)
for y, v in QUOTED["g_at"].items():
    assert g(F(y)) == v
print("exr-images-and-preimages-r5: all quoted values check")
