"""def-divides (Ch 7, 02): 3 | 12 (k = 4), -3 | 12 (k = -4), 3 does not divide 14 (4 < 14/3 < 5);
3 | 4^n - 1 with 4^(n+1) - 1 = 4(4^n - 1) + 3 = 3(4k + 1)."""
from fractions import Fraction as F
QUOTED = {"k12": 4, "k12neg": -4}
assert QUOTED["k12"] * 3 == 12 and QUOTED["k12neg"] * (-3) == 12
assert 4 < F(14, 3) < 5 and 14 % 3 != 0
for n in range(0, 60):
    assert (4 ** n - 1) % 3 == 0
    k = (4 ** n - 1) // 3
    assert 4 ** (n + 1) - 1 == 4 * (4 ** n - 1) + 3 == 3 * (4 * k + 1)
print("def-divides: all quoted values check")
