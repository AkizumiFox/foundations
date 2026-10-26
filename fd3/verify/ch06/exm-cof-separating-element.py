"""exm-cof-separating-element: on finite rational samples A, B with a <= b for all a in A, b in B,
(a) c = max A (the supremum of a finite set) satisfies a <= c <= b;
(b) any c' with the same property satisfies |c - c'| <= b - a for every a in A, b in B.
Also the Quick check: every a in {p^2 < 2} is below every b in {p > 0, p^2 > 2}, and no sampled rational
upper bound u of A has u^2 < 2 or u^2 = 2 (so u lies in B)."""
from fractions import Fraction as Fr
import random

QUOTED = {"one_in_A": 1}
random.seed(61)
for _ in range(3000):
    cut = Fr(random.randint(-500, 500), random.randint(1, 50))
    A = [cut - Fr(random.randint(0, 500), random.randint(1, 50)) for _ in range(random.randint(1, 8))]
    B = [cut + Fr(random.randint(0, 500), random.randint(1, 50)) for _ in range(random.randint(1, 8))]
    assert all(a <= b for a in A for b in B)
    c = max(A)
    assert all(a <= c for a in A) and all(c <= b for b in B)
    lo, hi = max(A), min(B)
    for _ in range(5):
        cp = lo + (hi - lo) * Fr(random.randint(0, 100), 100)
        assert all(a <= cp <= b for a in A for b in B)
        for a in A:
            for b in B:
                assert abs(c - cp) <= b - a

# Quick check in Q
assert Fr(QUOTED["one_in_A"]) ** 2 < 2
for _ in range(20000):
    p = Fr(random.randint(-3000, 3000), random.randint(1, 1000))
    q = Fr(random.randint(1, 3000), random.randint(1, 1000))
    if p * p < 2 and q * q > 2:
        assert p < q
    # a rational with u >= 1 and u^2 != 2: if u^2 < 2 it is in A, and A has elements above it
    if q >= 1 and q * q < 2:
        # some element of A lies above q (A has no largest element)
        h = min(Fr(1, 2), (2 - q * q) / (2 * (2 * q + 1)))
        assert (q + h) ** 2 < 2 and q + h > q
    assert q * q != 2
print("exm-cof-separating-element: OK")
