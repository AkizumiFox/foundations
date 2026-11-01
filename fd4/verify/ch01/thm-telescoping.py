"""thm-telescoping (a), (b) on random data; the telescoping-products paragraph: prod_{k=1}^{n}(k+1)/k = n+1, prod_{k=2}^{n}(1 - 1/k^2) = prod (k-1)/k * prod (k+1)/k = (1/n)((n+1)/2) = (n+1)/(2n), check n = 3: 3/4 * 8/9 = 2/3 = 4/6."""
import random
from fractions import Fraction as Fr
from math import prod

QUOTED = {"n3_factors": (Fr(3, 4), Fr(8, 9)), "n3_value": Fr(2, 3)}
random.seed(5)
for _ in range(500):
    n = random.randint(0, 8)
    b = [Fr(random.choice([i for i in range(-9, 10) if i]), random.randint(1, 5)) for _ in range(n + 2)]
    assert sum(b[k + 1] - b[k] for k in range(n + 1)) == b[n + 1] - b[0]
    assert prod(b[k + 1] / b[k] for k in range(n + 1)) == b[n + 1] / b[0]
for n in range(1, 40):
    assert prod(Fr(k + 1, k) for k in range(1, n + 1)) == n + 1
    assert prod(Fr(k + 2, k + 1) for k in range(0, n)) == Fr(n + 1, 1)   # b_k = k + 1, k = 0..n-1
for n in range(2, 40):
    p = prod(1 - Fr(1, k * k) for k in range(2, n + 1))
    p1 = prod(Fr(k - 1, k) for k in range(2, n + 1))
    p2 = prod(Fr(k + 1, k) for k in range(2, n + 1))
    assert all(1 - Fr(1, k * k) == Fr(k - 1, k) * Fr(k + 1, k) for k in range(2, n + 1))
    assert p1 == Fr(1, n) and p2 == Fr(n + 1, 2) and p == p1 * p2 == Fr(n + 1, 2 * n)
assert tuple(1 - Fr(1, k * k) for k in (2, 3)) == QUOTED["n3_factors"]
assert QUOTED["n3_factors"][0] * QUOTED["n3_factors"][1] == QUOTED["n3_value"] == Fr(4, 6) == Fr(3 + 1, 2 * 3)
print("ok")
