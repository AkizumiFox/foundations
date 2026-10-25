"""exr-inverses-c2 (Ch 6, Section 6.5): uniqueness of left inverses; left inverses of f(k) = 2k, {1,2} -> {1,2,3,4}."""
from itertools import product
QUOTED = {"count": 4, "2^2": 4,
          "list": [(1, 1, 1, 2), (1, 1, 2, 2), (2, 1, 1, 2), (2, 1, 2, 2)]}
f = {1: 2, 2: 4}
lefts = sorted(v for v in product([1, 2], repeat=4) if all(v[f[x] - 1] == x for x in f))
assert lefts == QUOTED["list"] and len(lefts) == QUOTED["count"] == 2 ** 2

# (a), (b): for every injective f: X -> Y with 1 <= |X| <= |Y| <= 4, the number of
# left inverses is 1 if f is surjective or |X| = 1, and at least 2 otherwise.
for nx in range(1, 5):
    for ny in range(nx, 5):
        X, Y = range(nx), range(ny)
        for vals in product(Y, repeat=nx):
            if len(set(vals)) < nx:
                continue
            n = sum(1 for g in product(X, repeat=ny) if all(g[vals[x]] == x for x in X))
            if len(set(vals)) == ny or nx == 1:
                assert n == 1, (nx, ny, vals, n)
            else:
                assert n >= 2, (nx, ny, vals, n)
print("exr-inverses-c2: all quoted values check")
