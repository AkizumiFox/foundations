"""lem-bernoulli-strict (03-inequalities-for-sums-and-products): strict Bernoulli for x >= -1, x != 0, n >= 2;
the endpoint x = -1 reads 0 > 1 - n; the Quick check: equality at x = 0 and at n = 1 (and n = 0)."""
from fractions import Fraction as Fr
QUOTED = {"endpoint": (Fr(-1), "0 > 1 - n")}
xs = [Fr(-1), Fr(-9, 10), Fr(-1, 2), Fr(-1, 100), Fr(1, 100), Fr(1, 3), Fr(1), Fr(5)]
for x in xs:
    for n in range(2, 30):
        assert (1 + x) ** n > 1 + n * x, (x, n)
    assert (1 + x) ** 1 == 1 + 1 * x and (1 + x) ** 0 == 1 + 0 * x
for n in range(0, 30):
    assert (1 + Fr(0)) ** n == 1 + n * 0
for n in range(2, 30):
    assert 0 ** n == 0 and 0 > 1 - n
# induction step identity (1 + nx)(1 + x) = 1 + (n+1)x + nx^2
for x in xs:
    for n in range(0, 10):
        assert (1 + n * x) * (1 + x) == 1 + (n + 1) * x + n * x * x
print("ok")
