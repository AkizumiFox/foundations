"""exr-disjunction-and-cases-b2 (Ch 1, Section 1.7): max(a, b) >= a, b, >= average; max(3, -5)."""
from fractions import Fraction as F

QUOTED = {"max(3,-5)": 3, "average of 3 and -5": -1}


def mx(a, b):
    return a if a >= b else b


pts = [F(k, 3) for k in range(-30, 31)]
for a in pts:
    for b in pts:
        m = mx(a, b)
        assert m >= a and m >= b and m >= (a + b) / 2
assert mx(3, -5) == QUOTED["max(3,-5)"]
assert F(3 + (-5), 2) == QUOTED["average of 3 and -5"]
print("exr-disjunction-and-cases-b2: all quoted values check")
