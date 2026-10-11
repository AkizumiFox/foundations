"""Gate 0, P2: marking-scheme totals, and the Gate's pass line (42 of 60 = 70%)."""
from fractions import Fraction as Fr
QUOTED = {"points": [4, 2, 4], "total": 60, "pass": 42, "problems": 6, "minutes": 120}
assert sum(QUOTED["points"]) == 10
assert QUOTED["problems"] * 10 == QUOTED["total"]
assert Fr(QUOTED["pass"], QUOTED["total"]) == Fr(70, 100)
assert QUOTED["problems"] * 20 == QUOTED["minutes"]
print("ok")
