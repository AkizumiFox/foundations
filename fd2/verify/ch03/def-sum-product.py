"""def-sum-product: empty sum/product, factorials, finite lists, index shift, splitting;
and the Quick check product prod_{k=1}^4 (1 + 1/k) = 5 (telescoping)."""
from fractions import Fraction as Fr
import random

QUOTED = {"factorials": {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}, "check_product": 5}


def S(a, n):  # sum_{k=1}^n a(k), by the recursion
    s = 0
    for k in range(n):
        s = s + a(k + 1)
    return s


def P(a, n):
    p = 1
    for k in range(n):
        p = p * a(k + 1)
    return p


def Sgen(a, m, n):  # sum_{k=m}^n a(k) := sum_{i=1}^{n-m+1} a(m-1+i)
    assert m <= n + 1
    return S(lambda i: a(m - 1 + i), n - m + 1)


for n, v in QUOTED["factorials"].items():
    assert P(lambda k: k, n) == v
assert S(lambda k: 7, 0) == 0 and P(lambda k: 7, 0) == 1
random.seed(1)
for _ in range(300):
    vals = {k: Fr(random.randint(-9, 9), random.randint(1, 5)) for k in range(-40, 80)}
    a = lambda k: vals[k]
    m = random.randint(-10, 10)
    n = random.randint(m - 1, 20)
    p = random.randint(-15, 15)
    # index shift
    assert Sgen(a, m, n) == Sgen(lambda k: a(k - p), m + p, n + p)
    # splitting off the last term
    assert Sgen(a, m, n + 1) == Sgen(a, m, n) + a(n + 1)
    # empty sum
    assert Sgen(a, m, m - 1) == 0
    # finite lists: changing terms beyond N does not change sums up to N
    N = random.randint(0, 15)
    b = lambda k: a(k) if k <= N else Fr(123)
    assert all(S(a, j) == S(b, j) for j in range(N + 1))
# Quick check
q = P(lambda k: 1 + Fr(1, k), 4)
assert q == QUOTED["check_product"]
assert all(P(lambda k: Fr(k + 1, k), n) == n + 1 for n in range(40))
print("ok")
