"""exr-quotient-rings-a1 (b), (c)."""
from fractions import Fraction as F
QUOTED = {"a": 2, "ap": 8, "b": 5, "diff": -6, "ab": 10, "apb": 40, "res": -30, "k": -5}
a, ap, b = QUOTED["a"], QUOTED["ap"], QUOTED["b"]
assert a - ap == QUOTED["diff"] and QUOTED["diff"] % 6 == 0
assert a * b == QUOTED["ab"] and ap * b == QUOTED["apb"]
assert a * b - ap * b == QUOTED["res"] == (a - ap) * b == QUOTED["k"] * 6
assert (F(3, 2) - F(1, 2)) * F(1, 2) == F(1, 2)
print("exr-quotient-rings-a1: ok")
