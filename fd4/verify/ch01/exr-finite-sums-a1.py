"""exr-finite-sums-a1: (a) sum_{k=5}^{4} k = 0, prod_{k=1}^{3}(k+1) = 24; (b) n = 1, all ones: 2 vs 4; (c) sum_{k=2}^{6} k^2 = sum_{j=0}^{4} (j+2)^2; (d) (k+1)^2 - k^2 = 2k+1."""
from math import prod
QUOTED = {"a_sum": 0, "a_prod": 24, "b": (2, 4)}
assert sum(range(5, 5)) == QUOTED["a_sum"]
assert prod(k + 1 for k in range(1, 4)) == QUOTED["a_prod"] == 2 * 3 * 4
assert (sum(1 * 1 for _ in range(2)), sum([1, 1]) * sum([1, 1])) == QUOTED["b"]
assert sum(k * k for k in range(2, 7)) == sum((j + 2) ** 2 for j in range(0, 5))
assert all((k + 1) ** 2 - k ** 2 == 2 * k + 1 for k in range(-50, 50))
print("ok")
