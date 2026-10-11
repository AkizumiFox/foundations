"""thm-limit-laws-ordered-field: the product identity, the reciprocal identity and bound,
the tolerances; the Quick check (limit 3, values at n = 0); the warning quotient n + 1."""
from fractions import Fraction as Q
import itertools

vals = [Q(p, q) for p in range(-9, 10) for q in (1, 2, 3, 7)]
nz = [v for v in vals if v != 0]
for an, bn, a, b in itertools.product(vals[::3], vals[::4], vals[::5], vals[::6]):
    assert an * (bn - b) + b * (an - a) == an * bn - a * b
for bn, b in itertools.product(nz, nz):
    assert 1 / bn - 1 / b == (b - bn) / (bn * b)
    assert 1 / (b * b / 2) == 2 / (b * b)
    if abs(bn) > abs(b) / 2:
        assert abs(1 / bn - 1 / b) <= 2 * abs(bn - b) / (b * b)
for eps, M, b in itertools.product([Q(1, 10), Q(3, 7), Q(5)], [Q(1, 2), Q(2), Q(9)], vals[::4]):
    assert M * (eps / (2 * M)) + (abs(b) + 1) * (eps / (2 * (abs(b) + 1))) == eps
    if b != 0:
        assert (2 / (b * b)) * (eps * b * b / 2) == eps
# Quick check: for n >= 1, (3 - 1/n)/(1 + 5/n^2) = (3n^2 - n)/(n^2 + 5); limit 3
QUOTED = {"limit": 3, "c0": 3, "a0": 0}
for k in range(1, 3000):
    u = Q(1, k)
    c = (3 - u) / (1 + 5 * u * u)
    assert c == Q(3 * k * k - k, k * k + 5)
    assert abs(c - 3) <= Q(16, k)              # distance shrinks: tends to 3
assert (3 - Q(0)) / (1 + 5 * Q(0)) == QUOTED["c0"] and Q(0, 5) == QUOTED["a0"]
# warning: (1/(n+1)) / (1/(n+1)^2) = n + 1
for k in range(200):
    assert Q(1, k + 1) / Q(1, (k + 1) ** 2) == k + 1
print("ok")
