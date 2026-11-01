"""exr-bounds-and-suprema-a1: x^2 on [-1, 2)."""
from fractions import Fraction as Fr

QUOTED = {"sup": 4, "inf": 0, "spread": 4}
pts = [Fr(k, 100) for k in range(-100, 200)]   # [-1, 2) sampled
vals = [x * x for x in pts]
assert min(vals) == QUOTED["inf"] and max(vals) < QUOTED["sup"]
assert max(vals) > QUOTED["sup"] - Fr(1, 20)
assert QUOTED["sup"] - QUOTED["inf"] == QUOTED["spread"]
assert max(abs(a - b) for a in vals for b in vals[::7]) < QUOTED["spread"]
assert 2 not in pts and -2 not in pts
print("ok")
