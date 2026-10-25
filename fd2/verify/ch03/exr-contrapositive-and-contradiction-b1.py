"""exr-contrapositive-and-contradiction-b1 (F2.2 §04): (a) 3 not | a + b => 3 not | a or 3 not | b;
(b) x^2 > 2x + 8 => x > 4 or x < -2; x^2 - 2x - 8 = (x - 4)(x + 2)."""
from fractions import Fraction as Fr
for a in range(-60, 60):
    for b in range(-60, 60):
        if (a + b) % 3:
            assert a % 3 or b % 3
for i in range(-4000, 4000):
    x = Fr(i, 100)
    assert x * x - 2 * x - 8 == (x - 4) * (x + 2)
    if x * x > 2 * x + 8:
        assert x > 4 or x < -2
    if -2 <= x <= 4:
        assert x * x <= 2 * x + 8
print("exr-contrapositive-and-contradiction-b1: all quoted values check")
