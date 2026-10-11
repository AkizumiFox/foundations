"""prp-power-laws: the laws on exact rationals, (e), and the (-1)^n remark."""
from fractions import Fraction as Fr
import random


def pw(u, n):  # def-power, by the recursion
    r = Fr(1)
    for _ in range(n):
        r = r * u
    return r


random.seed(2)
for _ in range(400):
    u = Fr(random.randint(-7, 7), random.randint(1, 4))
    v = Fr(random.randint(-7, 7), random.randint(1, 4))
    m, n = random.randint(0, 8), random.randint(0, 8)
    assert pw(u, m + n) == pw(u, m) * pw(u, n)
    assert pw(pw(u, m), n) == pw(u, m * n)
    assert pw(u * v, n) == pw(u, n) * pw(v, n)
    if u > 0:
        assert pw(u, n) > 0
    if u > 1 and m < n:
        assert pw(u, m) < pw(u, n)
assert pw(Fr(0), 0) == 1
for k in range(30):
    assert pw(Fr(-1), 2 * k) == 1 and pw(Fr(-1), 2 * k + 1) == -1 and pw(Fr(1), k) == 1
t = Fr(3, 7)
assert pw(pw(t, 2), 2) == pw(t, 4)
print("ok")
