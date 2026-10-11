"""exr-disjunction-introduction-c1 (Ch 1, Section 1.6): (a) the premise "x >= 0 or x < 0" is
true at x = -1 and the line x >= 0 is false; (c) phi: x = -1 true, phi and psi (psi: x >= 0)
false at x = -1."""
from _grid import grid

QUOTED = {"x": -1}

assert all(x >= 0 or x < 0 for x in grid())
x = QUOTED["x"]
assert (x >= 0 or x < 0) and not (x >= 0)
phi, psi = (x == -1), (x >= 0)
assert phi and not (phi and psi)
# (b): a true side makes the disjunction true whatever the other side is
for p in (True,):
    for q in (True, False):
        assert (p or q) and (q or p)
print("exr-disjunction-introduction-c1: all quoted values check")
