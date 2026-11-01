"""exr-roots-and-rational-powers-r2 (05): sum binom(n,k)(-2)^k = (-1)^n."""
from math import comb

QUOTED = {}
for n in range(0, 60):
    assert sum(comb(n, k) * (-2) ** k for k in range(n + 1)) == (-1) ** n
print("ok")
