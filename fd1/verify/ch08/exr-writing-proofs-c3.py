"""exr-writing-proofs-c3 (Section 8.5): squares mod 3 are 0 or 1; (3k + 1)^2 = 3(3k^2 + 2k) + 1,
(3k + 2)^2 = 3(3k^2 + 4k + 1) + 1; 3 | n^2 implies 3 | n; 3j + 1 = 3t has no integer solution;
p^2 = 3q^2 has no solution with p, q not both multiples of 3 (small search);
the failure for 4: 4 | 2^2 but not 4 | 2; 4 = (2/1)^2 with p = 2, q = 1 not both multiples of 4."""
from fractions import Fraction as F
QUOTED = {"n_fail": 2, "p": 2, "q": 1}
for k in range(-300, 301):
    assert (3 * k + 1) ** 2 == 3 * (3 * k * k + 2 * k) + 1
    assert (3 * k + 2) ** 2 == 3 * (3 * k * k + 4 * k + 1) + 1
for n in range(-500, 501):
    assert (n * n) % 3 in (0, 1)
    if (n * n) % 3 == 0:
        assert n % 3 == 0
for j in range(-50, 51):
    for t in range(-50, 51):
        assert 3 * j + 1 != 3 * t
for p in range(-60, 61):
    for q in range(1, 61):
        assert p * p != 3 * q * q
n = QUOTED["n_fail"]
assert (n * n) % 4 == 0 and n % 4 != 0
p, q = QUOTED["p"], QUOTED["q"]
assert F(p, q) ** 2 == 4 and not (p % 4 == 0 and q % 4 == 0)
print("exr-writing-proofs-c3: all quoted values check")
