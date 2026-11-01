"""C2: Lagrange's identity AB - C^2 = 1/2 sum_j sum_k (x_j y_k - x_k y_j)^2 on random vectors; equality iff parallel; n = 2 form."""
import random, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
random.seed(8)
for _ in range(5000):
    n = random.randint(1, 5); x = rvec(n, -3, 3)
    y = rvec(n, -3, 3) if random.random() < .6 else sc(random.choice([-2, 0, 1, Fr(1, 2)]), x)
    A, B, C = n2(x), n2(y), dot(x, y)
    D = sum((x[j] * y[k] - x[k] * y[j]) ** 2 for j in range(n) for k in range(n))
    exp_ = sum(x[j]**2 * y[k]**2 - 2 * x[j] * y[j] * x[k] * y[k] + x[k]**2 * y[j]**2 for j in range(n) for k in range(n))
    assert D == exp_ == 2 * A * B - 2 * C * C
    assert A * B - C * C == Fr(D, 2)
    assert (D == 0) == parallel(x, y)
    if n == 2: assert A * B - C * C == (x[0] * y[1] - x[1] * y[0]) ** 2
print("ok")
