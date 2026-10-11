"""exr-derived-rules-b1 (Ch 2, Section 2.3): x^2 = 1 and x > 0 give x = 1; -1 < 0."""
from fractions import Fraction as F

QUOTED = {"root": 1, "other root": -1}

assert QUOTED["other root"] < 0
pts = [F(k, 64) for k in range(-256, 257)]
for x in pts:
    if x * x == 1:
        assert x in (QUOTED["root"], QUOTED["other root"])
        if x > 0:
            assert x == QUOTED["root"]
print("exr-derived-rules-b1: all quoted values check")
