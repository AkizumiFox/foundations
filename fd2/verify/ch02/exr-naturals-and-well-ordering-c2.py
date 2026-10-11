"""exr-naturals-and-well-ordering-c2 (Ch 7, 01): the candidate c (a, b + 1/2, or the smaller of them)
is the least element of every non-empty finite T in N u (N + 1/2) (random tests)."""
from fractions import Fraction as F
import random

H = F(1, 2)
random.seed(3)
pool = [F(n) for n in range(30)] + [n + H for n in range(30)]
for _ in range(3000):
    T = set(random.sample(pool, random.randint(1, 8)))
    A = {t for t in T if t.denominator == 1}
    B = {t - H for t in T if t.denominator != 1}
    assert all(b.denominator == 1 and b >= 0 for b in B)
    if not B:
        c = min(A)
    elif not A:
        c = min(B) + H
    else:
        c = min(min(A), min(B) + H)
    assert c in T and c == min(T)
print("exr-naturals-and-well-ordering-c2: all quoted values check")
