"""exr-induction-c5 (Ch 4, Section 4.2): R_n = prod_{k=2}^n (1 - 1/k^2) = (n+1)/(2n) > 1/2."""
from fractions import Fraction as F

QUOTED = {"R_2": F(3, 4), "R_3": F(2, 3), "R_4": F(5, 8), "factor 3": F(8, 9), "factor 4": F(15, 16)}

R = F(1)
for n in range(2, 301):
    R *= 1 - F(1, n * n)
    assert R == F(n + 1, 2 * n) == F(1, 2) + F(1, 2 * n) and R > F(1, 2)
    assert (n + 1) ** 2 - 1 == n * (n + 2)
    assert F(n + 1, 2 * n) * F(n * (n + 2), (n + 1) ** 2) == F(n + 2, 2 * (n + 1))
assert 1 - F(1, 9) == F(8, 9) and 1 - F(1, 16) == F(15, 16)
assert F(3, 4) * F(8, 9) == F(2, 3) and F(2, 3) * F(15, 16) == F(5, 8)
print("exr-induction-c5: all quoted values check")
