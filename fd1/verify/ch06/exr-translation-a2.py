"""exr-translation-a2 (Section 6.1): (h) on {-1, 1}; (i)'s hypothesis is false."""
from fractions import Fraction as F

QUOTED = {"(h) A": {-1, 1}, "(h) not every positive": True, "(h) no positive": False, "(i) value": True}

A = QUOTED["(h) A"]
assert (not all(x > 0 for x in A)) == QUOTED["(h) not every positive"]
assert (not any(x > 0 for x in A)) == QUOTED["(h) no positive"]
assert all(not (x > 0) for x in A) == QUOTED["(h) no positive"]
# (i): no real square is negative, so the hypothesis is false and the implication true
grid = [F(k, 7) for k in range(-300, 301)]
hyp = any(x * x < 0 for x in grid)
assert hyp is False and ((not hyp) or (0 == 1)) == QUOTED["(i) value"]
print("exr-translation-a2: all quoted values check")
