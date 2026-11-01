"""exm-binomial-absorbed-sum: sum_{k=1}^{4} k C(4,k) = 4 + 12 + 12 + 4 = 32;
k C(4,k) = 4 C(3,k-1) for 1 <= k <= 4; 4 * sum C(3,j) = 4 * 2^3 = 32."""
from math import comb
QUOTED = {"terms": (4, 12, 12, 4), "total": 32}
assert tuple(k * comb(4, k) for k in range(1, 5)) == QUOTED["terms"]
assert sum(QUOTED["terms"]) == QUOTED["total"]
for k in range(1, 5):
    assert k * comb(4, k) == 4 * comb(3, k - 1)
assert 4 * sum(comb(3, j) for j in range(4)) == 4 * 2 ** 3 == QUOTED["total"]
print("ok")
