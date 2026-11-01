"""exm-binomial-bound: 2^n >= n(n-1)/2 and n/2^n <= 2/(n-1) for 2 <= n < 300; n(n-1) >= 2;
instance n = 5: 5/32 <= 2/4."""
from fractions import Fraction as Fr
QUOTED = {"inst": (Fr(5, 32), Fr(2, 4))}
for n in range(2, 300):
    assert n * (n - 1) >= 2
    assert 2 ** n >= Fr(n * (n - 1), 2)
    assert Fr(n, 2 ** n) <= Fr(2, n - 1)
a, b = QUOTED["inst"]
assert a == Fr(5, 2 ** 5) and b == Fr(2, 5 - 1) and a <= b
print("ok")
