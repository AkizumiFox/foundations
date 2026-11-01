"""lem-ring-finite-sums and the first Quick check of 1.1: sum_{k=0}^{3}(2k-1) = 8, the empty sum sum_{k=4}^{3} k^2 = 0, the empty product prod_{k=1}^{0} 7 = 1; parts (a)-(f) on random integer lists, and (c) for natural m."""
import random
from math import prod

QUOTED = {"qc_sum": 8, "qc_terms": [-1, 1, 3, 5], "qc_empty_sum": 0, "qc_empty_product": 1}


def S(a, lo, hi):
    """sum_{k=lo}^{hi} a(k); empty when hi < lo."""
    return sum(a(k) for k in range(lo, hi + 1))


assert [2 * k - 1 for k in range(4)] == QUOTED["qc_terms"]
assert S(lambda k: 2 * k - 1, 0, 3) == QUOTED["qc_sum"]
assert S(lambda k: k * k, 4, 3) == QUOTED["qc_empty_sum"]
assert prod(7 for _ in range(1, 1)) == QUOTED["qc_empty_product"]

random.seed(1)
for _ in range(500):
    n = random.randint(0, 8)
    a = [random.randint(-9, 9) for _ in range(n + 2)]
    b = [random.randint(-9, 9) for _ in range(n + 2)]
    c, m = random.randint(-9, 9), random.randint(0, 9)
    A = lambda k: a[k]
    assert S(lambda k: a[k] + b[k], 0, n) == S(A, 0, n) + S(lambda k: b[k], 0, n)   # (a)
    assert c * S(A, 0, n) == S(lambda k: c * a[k], 0, n)                             # (b)
    assert S(lambda k: m * a[k], 0, n) == m * S(A, 0, n)                             # (c)
    j = random.randint(0, n + 3)
    e = lambda k: a[k % len(a)] if k == j else 0
    assert S(e, 0, n) == (e(j) if j <= n else 0)                                     # (d)
    assert -S(A, 0, n) == S(lambda k: -a[k], 0, n)                                   # (e)
    assert S(A, 0, n + 1) == a[0] + S(lambda k: a[k + 1], 0, n)                      # (f)
print("ok")
