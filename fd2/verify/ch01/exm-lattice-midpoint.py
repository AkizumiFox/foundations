"""exm-lattice-midpoint and "Back to the lattice points" (F2.1 §01): the hook's two midpoints,
the six midpoints of the unit square (none a lattice point), the Quick check (-3, 8), (1, 0) -> (-1, 4),
same pattern => lattice midpoint, and five points always contain a pair with a lattice midpoint (small grid)."""
from fractions import Fraction as F
from itertools import combinations

QUOTED = {"hook": {((0, 0), (2, 4)): (1, 2), ((0, 0), (1, 4)): (F(1, 2), 2)},
          "square": [(0, 0), (0, 1), (1, 0), (1, 1)],
          "six": [(0, F(1, 2)), (F(1, 2), 0), (F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)), (F(1, 2), 1), (1, F(1, 2))],
          "check": ((-3, 8), (1, 0), (-1, 4))}

mid = lambda p, q: (F(p[0] + q[0], 2), F(p[1] + q[1], 2))
lattice = lambda m: all(x.denominator == 1 for x in m)
pattern = lambda p: (p[0] % 2, p[1] % 2)

for (p, q), m in QUOTED["hook"].items():
    assert mid(p, q) == m
assert lattice(mid((0, 0), (2, 4))) and not lattice(mid((0, 0), (1, 4)))
mids = [mid(p, q) for p, q in combinations(QUOTED["square"], 2)]
assert mids == QUOTED["six"] and not any(lattice(m) for m in mids)
p, q, m = QUOTED["check"]
assert pattern(p) == pattern(q) == (1, 0) and mid(p, q) == m and lattice(m)
pts = [(a, b) for a in range(-3, 4) for b in range(-3, 4)]
for p, q in combinations(pts, 2):
    assert (pattern(p) == pattern(q)) == lattice(mid(p, q))
small = [(a, b) for a in range(3) for b in range(3)]
assert all(any(lattice(mid(p, q)) for p, q in combinations(S, 2)) for S in combinations(small, 5))
print("exm-lattice-midpoint: all quoted values check")
