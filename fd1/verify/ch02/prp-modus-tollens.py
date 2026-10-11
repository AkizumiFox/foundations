"""prp-modus-tollens (Ch 2, Section 2.3), the two motivating arguments before it:
n even gives n^2 even; x >= 1 gives x^2 >= x >= 1, so x^2 < 1 forces x < 1."""
from fractions import Fraction as F

QUOTED = {"threshold": 1}

for n in range(-500, 501):
    if n % 2 == 0:
        assert (n * n) % 2 == 0
    if (n * n) % 2 != 0:
        assert n % 2 != 0
pts = [F(k, 64) for k in range(-256, 257)] + [F(1) - F(1, 10**6), F(1) + F(1, 10**6)]
t = QUOTED["threshold"]
for x in pts:
    if x >= t:
        assert x * x >= x >= t
    if x * x < t:
        assert x < t
print("prp-modus-tollens: all quoted values check")
