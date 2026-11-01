"""cor-binomial-real: (a) row sums 2^n and alternating sums 0 (n >= 1) for n < 40; (b), (c) on a grid
of rationals x >= 0; Quick check: C(5,k) 2^k = 1, 10, 40, 80, 80, 32 and 3^5 = 243."""
from fractions import Fraction as Fr
from math import comb
QUOTED = {"terms": [1, 10, 40, 80, 80, 32], "best": (3, 4), "pow": 243}
for n in range(40):
    assert sum(comb(n, k) for k in range(n + 1)) == 2 ** n
    if n >= 1:
        assert sum((-1) ** k * comb(n, k) for k in range(n + 1)) == 0
assert sum((-1) ** k * comb(0, k) for k in range(1)) == 1  # why n >= 1 is needed
xs = [Fr(i, 7) for i in range(0, 50)]
for n in range(0, 25):
    for x in xs:
        for k in range(n + 1):
            assert (1 + x) ** n >= comb(n, k) * x ** k
        if n >= 2:
            assert (1 + x) ** n >= 1 + n * x + Fr(n * (n - 1), 2) * x ** 2
            assert comb(n, 2) == n * (n - 1) // 2
t = [comb(5, k) * 2 ** k for k in range(6)]
assert t == QUOTED["terms"]
assert max(t) == 80 and [k for k in range(6) if t[k] == 80] == list(QUOTED["best"])
assert 3 ** 5 == QUOTED["pow"] >= 80
print("ok")
