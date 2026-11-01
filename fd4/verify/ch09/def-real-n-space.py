"""def-real-n-space quick check: {0,1}^3 has 2*2*2 = 8 points, listed in lexicographic order."""

from itertools import product

QUOTED = {
    "count": 8,
    "list": [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)],
}

pts = list(product([0, 1], repeat=3))
assert len(pts) == QUOTED["count"] == 2 * 2 * 2
assert pts == QUOTED["list"]
assert len(set(pts)) == 8
print("def-real-n-space: OK")
