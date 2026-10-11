"""exm-closed-open-interval: u(x) = x/2 + 1/4 and the hotel bijection phi on [0, 1]."""
from fractions import Fraction as F

QUOTED = {
    "u_range": (F(1, 4), F(3, 4)),
    "phi_examples": {F(0): F(1, 2), F(1): F(1, 3), F(1, 2): F(1, 4), F(3, 4): F(3, 4)},
    "max_shifted": F(1, 3),
    "u_misses": F(9, 10),
}


def u(x):
    return x / 2 + F(1, 4)


def phi(x):
    if x == 0:
        return F(1, 2)
    if x > 0 and (1 / x).denominator == 1:
        n = int(1 / x)
        return F(1, n + 2)
    return x


lo, hi = QUOTED["u_range"]
assert u(F(0)) == lo and u(F(1)) == hi
# u maps a grid of [0, 1] into (0, 1), injectively
grid = [F(k, 997) for k in range(998)]
vals = [u(x) for x in grid]
assert all(lo <= v <= hi and 0 < v < 1 for v in vals) and len(set(vals)) == len(vals)
assert not (lo <= QUOTED["u_misses"] <= hi)
for x, y in QUOTED["phi_examples"].items():
    assert phi(x) == y, (x, phi(x), y)
# on H = {0} u {1/n}: injective onto {1/m : m >= 2} (checked on n <= 500)
N = 500
H = [F(0)] + [F(1, n) for n in range(1, N + 1)]
img = [phi(h) for h in H]
assert len(set(img)) == len(img)
assert set(img) == {F(1, m) for m in range(2, N + 3)}
assert all(F(1, n + 2) <= QUOTED["max_shifted"] for n in range(1, N + 1))
# a sample of points of [0, 1] off H is fixed, and phi maps the whole sample into (0, 1) injectively
sample = H + [F(k, 1009) for k in range(1, 1009)]
sample = list(dict.fromkeys(sample))
pv = [phi(x) for x in sample]
assert all(0 < v < 1 for v in pv) and len(set(pv)) == len(pv)
print("ok")
