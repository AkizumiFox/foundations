"""exr-checking-proofs-b1 (Ch 5, Section 5.6): (i) (2k+1) + (2l+1) = 2(k + l + 1);
(ii) x > 1 gives x^2 > x > 1, hence not(x^2 < 1); x = 1 has not(x > 1) and not(x < 1); x >= 1 gives x^2 >= x >= 1;
the claim x^2 < 1 => x < 1 is true."""
from fractions import Fraction as F
QUOTED = {"x": 1}
for k in range(-100, 101):
    for l in range(-100, 101):
        assert (2 * k + 1) + (2 * l + 1) == 2 * (k + l + 1)
x = QUOTED["x"]
assert not x > 1 and not x < 1
for t in range(-500, 501):
    x = F(t, 61)
    if x > 1:
        assert x * x > x > 1
        assert not x * x < 1
    if x >= 1:
        assert x * x >= x >= 1
    if x * x < 1:
        assert x < 1
print("exr-checking-proofs-b1: all quoted values check")
