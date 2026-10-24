"""def-definite-description (Section 5.8): (0, 1) has no maximum, since (m + 1)/2 lies in (m, 1)
for every m in (0, 1) (checked on a grid); the two readings of 'the maximum of A is not 1'
(inside false, outside true) on a finite stand-in where Max(A, m) is empty; the Quick check:
0 <= u < v gives u*u < v*v (grid), and sqrt 2, -sqrt 2 both square to 2 (no rational square
root; the school fact is not rechecked)."""
from fractions import Fraction as Fr

QUOTED = {"bound": 1}

grid = [Fr(p, q) for q in range(2, 40) for p in range(1, q)]           # points of (0, 1)
for m in grid:
    w = (m + 1) / 2
    assert m < w < 1 and 0 < w                                          # w in A and w > m
# no element of the grid is a maximum of the grid's (0, 1)
assert not any(all(a <= m for a in grid + [(m + 1) / 2]) for m in grid)

# the two readings when nothing is a maximum: Max is empty
Max = set()
inside = any(m in Max and all(y == m for y in Max) and m != 1 for m in grid)
outside = not any(m in Max and all(y == m for y in Max) and m == 1 for m in grid)
assert inside is False and outside is True

# Quick check: non-negative numbers with the same square are equal
nn = [Fr(p, q) for p in range(0, 40) for q in range(1, 8)]
assert all(u * u < v * v for u in nn for v in nn if u < v)
print("def-definite-description: all quoted values check")
