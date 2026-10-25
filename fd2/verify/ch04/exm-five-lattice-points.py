"""exm-five-lattice-points: among any 5 different lattice points two have a lattice midpoint;
checked on all 5-subsets of a 4 x 4 grid (with negative coordinates). B = {0,1}^2 has 4 elements;
the remainder map lands in B; the four corners of a unit square show 5 cannot be lowered."""
from itertools import combinations, product
grid = list(product(range(-2, 2), repeat=2))
def mid_ok(p, q):
    return (p[0] + q[0]) % 2 == 0 and (p[1] + q[1]) % 2 == 0
B = set(product((0, 1), repeat=2))
assert len(B) == 4
for p in grid:
    assert (p[0] % 2, p[1] % 2) in B
for s in combinations(grid, 5):
    assert any(mid_ok(p, q) for p, q in combinations(s, 2))
corners = [(0, 0), (0, 1), (1, 0), (1, 1)]
assert not any(mid_ok(p, q) for p, q in combinations(corners, 2))
assert all(mid_ok(p, p) for p in grid)  # a point and itself: midpoint is the point
print("ok")
