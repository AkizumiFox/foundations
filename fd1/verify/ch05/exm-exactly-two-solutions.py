"""exm-exactly-two-solutions (Section 5.8): y*y = 1 iff y in {1, -1} (on a rational grid, and
by the factorization (y - 1)(y + 1) = y*y - 1); the pigeonhole step: every triple from
{1, -1} satisfies u = v or u = w or v = w; and 1 != -1 are two witnesses."""
from fractions import Fraction as Fr
import itertools

QUOTED = {"roots": {1, -1}}

grid = {Fr(p, q) for p in range(-60, 61) for q in range(1, 13)}
assert {y for y in grid if y * y == 1} == QUOTED["roots"]
assert all((y - 1) * (y + 1) == y * y - 1 for y in grid)
assert 1 != -1 and 1 * 1 == 1 and (-1) * (-1) == 1
for u, v, w in itertools.product(sorted(QUOTED["roots"]), repeat=3):
    assert u == v or u == w or v == w
# the warning: exists x exists y (x*x = 1 and y*y = 1) holds with x = y = 1
assert any(x * x == 1 and y * y == 1 and x == y for x in grid for y in grid)
print("exm-exactly-two-solutions: all quoted values check")
