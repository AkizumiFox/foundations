"""exr-projection-and-angle-c2: (a) on random rational data for n = 1..5, (b) the n = 2 double sum, and the check x = (3,1), y = (1,1)."""
from fractions import Fraction as Fr
import random
QUOTED = {"check_sq": 2}   # distance sqrt 2: |3 - 1|^2 / ||y||^2 = 4/2
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
random.seed(3)
for _ in range(1500):
    n = random.randint(1, 5)
    x = [Fr(random.randint(-9, 9), random.randint(1, 3)) for _ in range(n)]
    y = [Fr(random.randint(-9, 9), random.randint(1, 3)) for _ in range(n)]
    if dot(y, y) == 0:
        continue
    t0 = dot(x, y) / dot(y, y); e = [a - t0 * b for a, b in zip(x, y)]
    rhs = Fr(1, 2) * sum((x[j] * y[k] - x[k] * y[j]) ** 2 for j in range(n) for k in range(n))
    assert dot(y, y) * dot(e, e) == rhs
    if n == 2:
        assert rhs == (x[0] * y[1] - x[1] * y[0]) ** 2
x, y = (3, 1), (1, 1)
assert Fr(x[0] * y[1] - x[1] * y[0]) ** 2 / dot(y, y) == QUOTED["check_sq"]
print("ok")
