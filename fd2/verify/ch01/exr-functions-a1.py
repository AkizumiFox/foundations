"""exr-functions-a1 (Ch 6 Section 6.4): R1-R3; 9 functions {1,2} -> {a,b,c}, 6 injective."""
import sys
sys.path.insert(0, "verify/ch06")
from _sets import functions, injective, is_function

QUOTED = {"functions": 9, "injective": 6, "equal-entry pairs": 3}

X = {1, 2, 3}
assert is_function({(1, 2), (2, 2), (3, 1)}, X, X)
assert not is_function({(1, 1), (2, 3)}, X, X)
assert not is_function({(1, 1), (1, 2), (2, 2), (3, 3)}, X, X)
fs = functions({1, 2}, {"a", "b", "c"})
assert len(fs) == QUOTED["functions"]
assert sum(injective(f) for f in fs) == QUOTED["injective"] == QUOTED["functions"] - QUOTED["equal-entry pairs"]
print("exr-functions-a1: all quoted values check")
