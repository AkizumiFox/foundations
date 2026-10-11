"""exr-derivations-c1 (Section 1.2): Flip passes the checker and leads from true to false."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import is_derivation

QUOTED = {"accepted by the checker": True, "premise 0 < 1 true": True, "1 < 0 true": False}
d = [("0 < 1", None, ()), ("1 < 0", "Flip", (1,))]
assert is_derivation(d, ("Tr", "Sh", "Flip")) == QUOTED["accepted by the checker"]
assert (0 < 1) == QUOTED["premise 0 < 1 true"] and (1 < 0) == QUOTED["1 < 0 true"]
print("exr-derivations-c1: all checks pass")
