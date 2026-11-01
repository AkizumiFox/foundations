"""exr-binomial-theorem-b2: sum_{k=1}^n k C(n,k) = n 2^(n-1) for 1 <= n < 60; check n = 3: 12."""
from math import comb
QUOTED = {"n3": 12}
for n in range(1, 60):
    assert sum(k * comb(n, k) for k in range(1, n + 1)) == n * 2 ** (n - 1)
    for j in range(n):
        assert (j + 1) * comb(n, j + 1) == n * comb(n - 1, j)
assert 1 * 3 + 2 * 3 + 3 * 1 == QUOTED["n3"] == 3 * 2 ** 2
print("ok")
