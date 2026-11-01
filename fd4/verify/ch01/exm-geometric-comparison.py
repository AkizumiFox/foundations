"""exm-geometric-comparison: 1/n! <= 1/2^(n-1) < 2/n for n >= 1; h = 1 for r = 1/2; 1/2^(n-1) = 2 (1/2)^n."""
from fractions import Fraction as F
import math

QUOTED = {"h": 1, "C": 2}
assert 1 / F(1, 2) - 1 == QUOTED["h"]
for n in range(1, 400):
    assert math.factorial(n) >= 2 ** (n - 1)
    assert F(1, 2 ** (n - 1)) == 2 * F(1, 2) ** n
    assert F(1, 2) ** n < F(1, n)
    assert F(1, math.factorial(n)) <= F(1, 2 ** (n - 1)) < F(QUOTED["C"], n)
assert math.factorial(1) == 2 ** 0
for eps in [F(1), F(1, 3), F(1, 1000)]:
    N = math.floor(QUOTED["C"] / eps) + 1
    assert N >= 1 and all(F(1, math.factorial(n)) < eps for n in range(N, N + 100))
print("ok")
