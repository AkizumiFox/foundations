"""exr-binomial-theorem-c1: sum k(k-1) C(n,k) = n(n-1) 2^(n-2) for 2 <= n < 60; the termwise identity
k(k-1) C(n,k) = n(n-1) C(n-2,k-2) for 2 <= k <= n; check n = 3: 2*3 + 6*1 = 12 = 6*2."""
from math import comb
QUOTED = {"n3": (6, 6, 12)}
for n in range(2, 60):
    assert sum(k * (k - 1) * comb(n, k) for k in range(n + 1)) == n * (n - 1) * 2 ** (n - 2)
    for k in range(2, n + 1):
        assert k * comb(n, k) == n * comb(n - 1, k - 1)
        assert (k - 1) * comb(n - 1, k - 1) == (n - 1) * comb(n - 2, k - 2)
        assert k * (k - 1) * comb(n, k) == n * (n - 1) * comb(n - 2, k - 2)
a, b, c = QUOTED["n3"]
assert (a, b) == (2 * 1 * comb(3, 2), 3 * 2 * comb(3, 3)) and a + b == c == 3 * 2 * 2
print("ok")
