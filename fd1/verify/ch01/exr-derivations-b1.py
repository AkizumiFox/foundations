"""exr-derivations-b1 (Section 1.2): the four-line derivation with Sh (c = 1) and Tr."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import is_derivation

QUOTED = {"derivation is correct": True, "shift by": 1}
d = [("x < y", None, ()), ("y + 1 < z", None, ()), ("x + 1 < y + 1", "Sh", (1,)),
     ("x + 1 < z", "Tr", (3, 2))]
assert is_derivation(d) == QUOTED["derivation is correct"]
print("exr-derivations-b1: all checks pass")
