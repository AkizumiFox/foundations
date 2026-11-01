"""prp-sum-order on random rational lists (a)-(e), and the Warning: n = 1, all terms 1: sum a_k b_k = 2, product of sums = 4; 1/1 + 1/1 = 2 != 1/2."""
import random
from fractions import Fraction as Fr

QUOTED = {"w_sum_prod": 2, "w_prod_sums": 4, "w_recip_sum": 2, "w_recip_of_sum": Fr(1, 2)}
a = b = [1, 1]
assert sum(x * y for x, y in zip(a, b)) == QUOTED["w_sum_prod"]
assert sum(a) * sum(b) == QUOTED["w_prod_sums"]
assert Fr(1, 1) + Fr(1, 1) == QUOTED["w_recip_sum"] and Fr(1, sum(a)) == QUOTED["w_recip_of_sum"]
random.seed(3)
for _ in range(2000):
    n = random.randint(0, 7)
    a = [Fr(random.randint(-30, 30), random.randint(1, 6)) for _ in range(n + 1)]
    d = [Fr(random.randint(0, 5), random.randint(1, 3)) for _ in range(n + 1)]
    b = [x + y for x, y in zip(a, d)]
    assert sum(a) <= sum(b)
    if any(y > 0 for y in d):
        assert sum(a) < sum(b)
    p = [abs(x) for x in a]
    for m in range(-1, n + 1):
        assert sum(p) >= sum(p[: m + 1])
    for j in range(n + 1):
        assert sum(p) >= p[j]
    M = max(a)
    assert sum(a) <= (n + 1) * M
    assert abs(sum(a)) <= sum(p)
    if sum(p) == 0:
        assert all(x == 0 for x in p)
print("ok")
