"""exr-projection-and-angle-r4: ||x - w||^2 = ||x||^2 - 2<x,w> + ||w||^2 on random data, and n - 2n + n = 0 for the constrained x."""
from fractions import Fraction as Fr
import random
QUOTED = {"solution": "(1, ..., 1)"}
random.seed(8)
for _ in range(1000):
    n = random.randint(1, 6)
    x = [Fr(random.randint(-9, 9), random.randint(1, 3)) for _ in range(n)]
    lhs = sum((a - 1) ** 2 for a in x)
    assert lhs == sum(a * a for a in x) - 2 * sum(x) + n
for n in range(1, 8):
    assert n - 2 * n + n == 0
    w = [1] * n; assert sum(w) == n and sum(a * a for a in w) == n
print("ok")
