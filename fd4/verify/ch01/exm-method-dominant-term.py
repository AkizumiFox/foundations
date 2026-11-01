"""exm-method-dominant-term: 5 <= n^2/2 once n >= 4, so n^2 - 5 >= n^2/2; false for n <= 3."""
from fractions import Fraction as F

QUOTED = {"n0": 4}
for n in range(0, 2000):
    ok = (n * n - 5 >= F(n * n, 2))
    assert ok == (n >= QUOTED["n0"]), n
print("ok")
