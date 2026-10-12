"""Section 1.3, "Common errors": the whole-line warning (P: x > 2, Q: x > 4, R: x <= 4).
The line (P -> Q) or R holds for every real x; at x = 3, P is true and Q false.  Also: the
step from P and (Q -> R) and Q to R never leads from truth to falsehood (all 8 valuations),
and the gallery rows of exm-using-an-implication-instances quote no values."""
import sys, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid

QUOTED = {"x": 3}
imp = lambda a, b: (not a) or b
for x in grid():
    assert imp(x > 2, x > 4) or x <= 4
x = QUOTED["x"]
assert x > 2 and not x > 4
assert imp(x > 2, x > 4) or x <= 4      # the first line is true at x = 3 too
for P, Q, R in itertools.product((False, True), repeat=3):
    if P and imp(Q, R) and Q:
        assert R
print("exm-using-an-implication-instances: checks")
