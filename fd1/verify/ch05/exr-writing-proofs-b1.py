"""exr-writing-proofs-b1 (Ch 5, Section 5.5): (a) n = 2k+1 gives 3n + 5 = 6k + 3 + 5 = 2(3k + 4);
(b) x^2 + 1 = 2x - 1 iff (x - 1)^2 + 1 = 0, which has no real solution;
(c) x^3 - x = (x + 1) x (x - 1), roots -1, 0, 1, and (-1)^3 = -1, 0^3 = 0, 1^3 = 1."""
from fractions import Fraction as F
QUOTED = {"a_witness": "3k+4", "c_roots": (-1, 0, 1)}
for k in range(-1000, 1001):
    n = 2 * k + 1
    assert 3 * n + 5 == 6 * k + 3 + 5 == 2 * (3 * k + 4)
pts = [F(k, 31) for k in range(-400, 401)]
for x in pts:
    lhs = (x * x + 1) - (2 * x - 1)
    assert lhs == x * x - 2 * x + 2 == (x - 1) ** 2 + 1
    assert lhs > 0                       # no solution
    assert x ** 3 - x == (x + 1) * (x * (x - 1))
    assert (x ** 3 == x) == (x in (-1, 0, 1))
for r in QUOTED["c_roots"]:
    assert r ** 3 == r
print("exr-writing-proofs-b1: all quoted values check")
