"""exm-fractions-nonzero-denominators (Section 10.4): (p, q) ~ (-p, -q); the Quick check
3.(-8) = -24 = (-6).4; the warning: (0, 1) vs (1, 1) gives 0 < 1, vs (-1, -1) gives 0 < -1."""
from itertools import product
rel = lambda x, y: x[0] * y[1] == y[0] * x[1]
W = [(a, b) for a in range(-4, 5) for b in range(-4, 5) if b != 0]
for x, y, z in product(W, repeat=3):          # transitivity on Z x (Z \ {0}), a window
    if rel(x, y) and rel(y, z):
        assert rel(x, z)
assert all(rel((a, b), (-a, -b)) for a, b in W)
QUOTED = {"check": -24, "warning": ((0, 1), (1, 1), (-1, -1))}
assert 3 * (-8) == QUOTED["check"] == (-6) * 4
x, y, y2 = QUOTED["warning"]
assert rel(y, y2)
assert (x[0] * y[1] < y[0] * x[1]) is True       # 0 < 1
assert (x[0] * y2[1] < y2[0] * x[1]) is False    # 0 < -1 is false
print("exm-fractions-nonzero-denominators: all quoted values check")
