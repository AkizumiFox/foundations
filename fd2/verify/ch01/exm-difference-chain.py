"""exm-difference-chain: (A - B) - C = A - (B u C) on all small sets; the Quick check witness."""
import os, sys
from itertools import product
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sets import subsets

QUOTED = {"A": {1, 2}, "B": {1}, "C": {2}, "left": set(), "right": {1, 2}}
S = subsets([1, 2, 3])
assert all((A - B) - C == A - (B | C) for A, B, C in product(S, repeat=3))
A, B, C = QUOTED["A"], QUOTED["B"], QUOTED["C"]
assert (A - B) - C == QUOTED["left"] and A - (B & C) == QUOTED["right"]
print("exm-difference-chain: all quoted values check")
