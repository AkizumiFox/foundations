"""exr-roots-and-rational-powers-b3 (05): sqrt(2/(n-1)) < 0.1 iff 2/(n-1) < 0.01 iff n - 1 > 200; N = 202."""
from fractions import Fraction as F

QUOTED = {"N": 202}
assert all((F(2, n - 1) < F(1, 100)) == (n - 1 > 200) for n in range(2, 3000))
assert min(n for n in range(2, 3000) if F(2, n - 1) < F(1, 100)) == QUOTED["N"]
# n^(1/n) < 1.1 for n >= 202, i.e. 1.1^n > n
assert all(F(11, 10) ** n > n for n in range(QUOTED["N"], 1500))
print("ok")
