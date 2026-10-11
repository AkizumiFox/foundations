"""exm-modus-tollens-instance (Ch 2, Section 2.3): x > 2 gives x^2 = x*x > 2x > 4;
x^2 <= 4 forces x <= 2."""
from fractions import Fraction as F

QUOTED = {"threshold": 2, "square threshold": 4}

pts = [F(k, 16) for k in range(-160, 161)] + [F(2) + F(1, 10**6), F(2) - F(1, 10**6)]
for x in pts:
    if x > 2:
        assert x * x > 2 * x > 4
    if x * x <= QUOTED["square threshold"]:
        assert x <= QUOTED["threshold"]
print("exm-modus-tollens-instance: all quoted values check")
