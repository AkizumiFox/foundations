"""exm-sum-consecutive-products (Ch 3, Section 3.2): 1*2 + ... + n(n+1) = n(n+1)(n+2)/3."""
from fractions import Fraction as F

QUOTED = {"n=1": 2, "n=2": 8, "n=3": 20}

total = 0
for n in range(1, 500):
    total += n * (n + 1)
    assert total == F(n * (n + 1) * (n + 2), 3)
    # the inductive step's algebra: n(n+1)(n+2)/3 + (n+1)(n+2) = (n+1)(n+2)(n+3)/3
    assert F(n * (n + 1) * (n + 2), 3) + (n + 1) * (n + 2) == F((n + 1) * (n + 2) * (n + 3), 3)
assert [sum(k * (k + 1) for k in range(1, n + 1)) for n in (1, 2, 3)] == [2, 8, 20]
print("exm-sum-consecutive-products: all quoted values check")
