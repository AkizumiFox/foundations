"""thm-exp-unique: for n > |x|, (1 + x/n)^n <= exp x <= (1 - x/n)^(-n) and
(1 + x/n)^n >= exp x - (x^2 + 1) exp x / n, checked numerically on a grid; also the
Bernoulli step (1 - x^2/n^2)^n >= 1 - x^2/n and the algebraic identity
(1 + x/n)^n = (1 - x^2/n^2)^n (1 - x/n)^(-n) exactly (fractions)."""
from fractions import Fraction as Fr
import math

QUOTED = {"C": True}  # the text writes (x^2 + 1) exp x
xs = [Fr(k, 4) for k in range(-40, 41)]
for x in xs:
    for n in range(1, 120):
        if n <= abs(x):
            continue
        lo = (1 + x / n) ** n
        hi = (1 - x / n) ** (-n)
        assert lo == (1 - x * x / (n * n)) ** n * hi            # identity, exact
        assert (1 - x * x / (n * n)) ** n >= 1 - x * x / n      # Bernoulli, exact
        assert 1 - x * x / n >= 1 - (x * x + 1) / n
        E = math.exp(float(x))
        assert float(lo) <= E * (1 + 1e-12)
        assert E <= float(hi) * (1 + 1e-12)
        assert float(lo) >= E - float(x * x + 1) * E / n - 1e-9 * E
# failing case of A1 (d): x = -3, n = 2
assert (1 + Fr(-3, 2)) ** 2 == Fr(1, 4) and math.exp(-3) < 0.25
# instance before the theorem: x = 1, n = 2, 3, 4
assert [(1 + Fr(1, n)) ** n for n in (2, 3, 4)] == [Fr(9, 4), Fr(64, 27), Fr(625, 256)]
assert round(64 / 27, 3) == 2.370 and round(625 / 256, 3) == 2.441 and 9 / 4 == 2.25
print("ok")
