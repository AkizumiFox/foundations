"""Fold "When the cancellation skips" and the third Quick check of 1.1.
Skip: sum_{k=0}^{n}(b_{k+2} - b_k) = (b_{n+2} - b_1) + (b_{n+1} - b_0); b_k = 1/(k+1), n = 1: (1/3 - 1) + (1/4 - 1/2) = -11/12 = b_3 + b_2 - b_1 - b_0, while b_3 - b_0 = -3/4.
Quick check: 1/((2k-1)(2k+1)) = (1/2)(1/(2k-1) - 1/(2k+1)) = b_{k+1} - b_k with b_k = -1/(2(2k-1)).
Verification form of the box: F(0) = a_0 and F(k) - F(k-1) = a_k give sum = F(n)."""
import random
from fractions import Fraction as Fr
QUOTED = {"skip_value": Fr(-11, 12), "one_end": Fr(-3, 4)}
random.seed(7)
for _ in range(300):
    n = random.randint(0, 8)
    b = [Fr(random.randint(-20, 20), random.randint(1, 4)) for _ in range(n + 3)]
    assert sum(b[k + 2] - b[k] for k in range(n + 1)) == (b[n + 2] - b[1]) + (b[n + 1] - b[0])
b = lambda k: Fr(1, k + 1)
v = (b(2) - b(0)) + (b(3) - b(1))
assert v == (Fr(1, 3) - 1) + (Fr(1, 4) - Fr(1, 2)) == QUOTED["skip_value"] == b(3) + b(2) - b(1) - b(0)
assert b(3) - b(0) == QUOTED["one_end"] != v
c = lambda k: -Fr(1, 2 * (2 * k - 1))
for k in range(1, 200):
    a = Fr(1, (2 * k - 1) * (2 * k + 1))
    assert a == Fr(1, 2) * (Fr(1, 2 * k - 1) - Fr(1, 2 * k + 1)) == c(k + 1) - c(k)
    assert Fr(1, 2 * k - 1) - Fr(1, 2 * k + 1) == Fr(2, (2 * k - 1) * (2 * k + 1))
# verification form on random polynomial-like data
for _ in range(100):
    F = [Fr(random.randint(-9, 9)) for _ in range(10)]
    a = [F[0]] + [F[k] - F[k - 1] for k in range(1, 10)]
    for n in range(10):
        assert sum(a[: n + 1]) == a[0] + F[n] - F[0] == F[n]
print("ok")
