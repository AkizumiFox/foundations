"""exr-writing-proofs-a2 (Section 8.5), part (i): for 1 < x < 3, x - 1 > 0 and x - 3 < 0, so
x^2 - 4x + 3 = (x - 1)(x - 3) < 0."""
from fractions import Fraction as F
QUOTED = {"interval": (1, 3)}
a, b = QUOTED["interval"]
for k in range(1, 400):
    x = a + F(k, 400) * (b - a)
    assert x - 1 > 0 and x - 3 < 0
    assert x * x - 4 * x + 3 == (x - 1) * (x - 3) < 0
print("exr-writing-proofs-a2: all quoted values check")
