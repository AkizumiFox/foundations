"""exm-verify-scope (Proof D, Ch 5, Section 5.6): x = 1/2 has x^2 = 1/4 < 1/2 = x;
x^2 - x + 1 = (x - 1/2)^2 + 3/4 > 0; x > 1 gives x^2 > x."""
from fractions import Fraction as F
QUOTED = {"x": F(1, 2), "x_squared": F(1, 4)}
x = QUOTED["x"]
assert x * x == QUOTED["x_squared"] < x
for k in range(-800, 801):
    x = F(k, 53)
    assert x * x - x + 1 == (x - F(1, 2)) ** 2 + F(3, 4) > 0
    assert x * x + 1 > x
    if x > 1:
        assert x * x > x
print("exm-verify-scope: all quoted values check")
