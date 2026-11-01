"""B3: phi(x) = floor(2x) - 2 floor(x) on [0, 2]: values 0, 1, 0, 1 on the open pieces of
0, 1/2, 1, 3/2, 2, and 0, 1, 0, 1, 0 at the cut points."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor
QUOTED = {"pieces": [0, 1, 0, 1], "points": [0, 1, 0, 1, 0]}
phi = lambda x: floor(2 * x) - 2 * floor(x)
cuts = [F(0), F(1, 2), F(1), F(3, 2), F(2)]
for (lo, hi), v in zip(zip(cuts, cuts[1:]), QUOTED["pieces"]):
    assert {phi(lo + (hi - lo) * F(i, 40)) for i in range(1, 40)} == {v}
assert [phi(c) for c in cuts] == QUOTED["points"]
print("exr-floor-and-step-functions-b3: OK")
