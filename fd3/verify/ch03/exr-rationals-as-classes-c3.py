"""exr-rationals-as-classes-c3 (Section 3.1; formerly exm-fractions-nonzero-denominators):
transitivity of cross-multiplication on Z x (Z minus {0}) and (p, q) ~ (-p, -q). The values
3.(-8) = -24 and (0, 1), (1, 1), (-1, -1) are kept from the old example (the last now in
Section 3.2's non-example)."""
from itertools import product
rel = lambda x, y: x[0] * y[1] == y[0] * x[1]
W = [(a, b) for a in range(-4, 5) for b in range(-4, 5) if b != 0]
for x, y, z in product(W, repeat=3):          # transitivity on Z x (Z minus {0}), a window
    if rel(x, y) and rel(y, z):
        assert rel(x, z)
assert all(rel((a, b), (-a, -b)) for a, b in W)
QUOTED = {"warning": ((0, 1), (1, 1), (-1, -1))}
assert 3 * (-8) == -24 == (-6) * 4
x, y, y2 = QUOTED["warning"]
assert rel(y, y2)
assert (x[0] * y[1] < y[0] * x[1]) is True       # 0 < 1
assert (x[0] * y2[1] < y2[0] * x[1]) is False    # 0 < -1 is false
print("exr-rationals-as-classes-c3: all quoted values check")
