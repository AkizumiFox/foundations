"""exm-converse-proof-critique (Section 6.4): sqrt(x^2 + 1) - x = 1/(sqrt(x^2 + 1) + x) < 1/(2x)
for x in (0, 1000] on a grid; the minimum of finitely many positive values is positive."""
import math
import random
for i in range(1, 100001):
    x = i / 100
    s = math.sqrt(x * x + 1)
    assert abs((s - x) - 1 / (s + x)) < 1e-9
    assert 1 / (s + x) < 1 / (2 * x)
random.seed(64)
for _ in range(1000):
    vals = [random.uniform(1e-6, 5) for _ in range(random.randint(1, 20))]
    assert min(vals) > 0 and all(min(vals) <= v for v in vals)
print("exm-converse-proof-critique: all quoted values check")
