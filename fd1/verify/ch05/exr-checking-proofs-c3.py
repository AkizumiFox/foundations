"""exr-checking-proofs-c3 (Ch 5, Section 5.6): (1) 4k = 2(2k), 6k = 2(3k); (2) m = 2, n = 4 have
no common k; mn = 4kl; (3) x = 1/2 is in neither case; for 0 < x < 1, |x - 1| = 1 - x < 1 < |x| + 1;
the claim |x - 1| <= |x| + 1; (4) a = 1, b = 2, x = 0 refutes cancellation; x = 0 refutes the
claim; x^2 = 2x iff x(x - 2) = 0 iff x in {0, 2}."""
from fractions import Fraction as F
QUOTED = {}
for k in range(-300, 301):
    assert 4 * k == 2 * (2 * k) and 6 * k == 2 * (3 * k)
assert not any(2 == 2 * k and 4 == 2 * k for k in range(-10, 11))
for k in range(-50, 51):
    for l in range(-50, 51):
        assert (2 * k) * (2 * l) == 4 * (k * l)
x = F(1, 2)
assert not (x >= 1 or x <= 0)
for t in range(-300, 301):
    x = F(t, 37)
    assert abs(x - 1) <= abs(x) + 1
    if 0 < x < 1:
        assert abs(x - 1) == 1 - x < 1 < abs(x) + 1
    assert (x * x == 2 * x) == (x * (x - 2) == 0) == (x in (0, 2))
a, b, x = 1, 2, 0
assert a * x == b * x and a != b
assert 0 ** 2 == 2 * 0 and 0 != 2
print("exr-checking-proofs-c3: all quoted values check")
