"""prp-limit-preserves-order-ordered-field (a): with eps = (a - b)/2,
a - eps = (a + b)/2 = b + eps; and eps > 0 when b < a.
Quick check (4.4): |a_n| <= 3 for all n and a_n -> a give |a| <= 3; checked
through |x| <= 3 <=> -3 <= x <= 3 on a grid and on sample sequences in Q
whose limits are known (3 - 1/(n+1) -> 3, (-1)^n 3/(n+1) -> 0, -3 + 2/(n+2) -> -3)."""
from fractions import Fraction as Q

QUOTED = {}
for A in [Q(p, 3) for p in range(-12, 13)]:
    for B in [Q(p, 4) for p in range(-12, 13)]:
        e = (A - B) / 2
        assert A - e == (2 * A - A + B) / 2 == (A + B) / 2 == B + e
        if B < A:
            assert e > 0
for x in [Q(p, 7) for p in range(-40, 41)]:
    assert (abs(x) <= 3) == (-3 <= x <= 3)
samples = [
    (lambda n: 3 - Q(1, n + 1), Q(3)),
    (lambda n: (-1) ** n * Q(3, n + 1), Q(0)),
    (lambda n: -3 + Q(2, n + 2), Q(-3)),
]
for f, lim in samples:
    for n in range(2000):
        assert abs(f(n)) <= 3
    # the terms approach lim: distance below 1/100 from n = 400 on
    assert all(abs(f(n) - lim) < Q(1, 100) for n in range(400, 2000))
    assert abs(lim) <= 3
print("ok")
