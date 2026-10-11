"""Witnesses and truth-table arguments in the solution of exr-statements-and-connectives-b4 (Section 1.1)."""
import sys, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import implies_on_grid

QUOTED = {"(a) x": -3, "(c) x": -1}
imp = lambda p, q: (not p) or q

# (a) P: x > 2, Q: x^2 > 4 at x = -3
assert implies_on_grid(lambda x: x > 2, lambda x: x**2 > 4)    # P -> Q for every x
x = QUOTED["(a) x"]
P, Q = x > 2, x**2 > 4
assert imp(P, Q) and (not P) and Q                              # premises true, not-Q false
# (c) P: x > 0, Q: x <= 0 at x = -1
x = QUOTED["(c) x"]
P, Q = x > 0, x <= 0
assert (P or Q) and not P
# (b), (d): no valuation makes every premise true and the conclusion false
for p, q, r in itertools.product([True, False], repeat=3):
    assert not (imp(p, q) and imp(q, r) and not imp(p, r))
    assert not ((p and q) and not (p or q))
# (a), (c) are bad as forms too (a valuation breaks them)
assert any(imp(p, q) and (not p) and q for p, q in itertools.product([True, False], repeat=2))
print("exr-statements-and-connectives-b4: checks")
