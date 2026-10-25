"""exr-comparing-cardinalities-b4 (d): S -> p(S), p(m, n) = 2^m 3^n, is injective
on the subsets of {0, 1, 2}^2; also the 3.4 Quick check map on sample points."""
from fractions import Fraction as F
from itertools import product

grid = list(product(range(3), repeat=2))
p = lambda mn: 2 ** mn[0] * 3 ** mn[1]
assert len({p(x) for x in grid}) == len(grid)  # p injective on the grid
images = set()
for mask in range(1 << len(grid)):
    S = [grid[i] for i in range(len(grid)) if mask >> i & 1]
    images.add(frozenset(p(x) for x in S))
assert len(images) == 1 << len(grid)  # 512 distinct images

# Quick check: x -> x/2 on [0, 1], 5 -> 1; injective on samples, values in [0, 1]
pts = [F(k, 40) for k in range(41)]
vals = [x / 2 for x in pts] + [F(1)]
assert len(set(vals)) == len(vals) and all(0 <= v <= 1 for v in vals)
assert max(x / 2 for x in pts) == F(1, 2) < 1
print("ok")
