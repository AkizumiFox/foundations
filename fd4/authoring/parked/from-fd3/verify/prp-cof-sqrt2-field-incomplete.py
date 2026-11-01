"""prp-cof-sqrt2-field-incomplete (and exr-two-non-examples-b2): the descent identity
u'^2 - n v'^2 = (k^2 - n)(u^2 - n v^2) with u' = n v - k u, v' = u - k v, as a polynomial identity
(checked on a grid large enough to determine a polynomial of degree 2 in each of u, v, n, k);
k^2 < n < (k+1)^2 for (n, k) = (3, 1), (6, 2), (5, 2), (10, 3); a^2 + 2b^2 = 3 with 2ab = 0
reduces to a^2 = 3 or (2b)^2 = 6, and for 5 to a^2 = 5 or (2b)^2 = 10. Also: no rational square
equals 3, 6, 5, 10 among fractions with small denominators (sanity only)."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"pairs": [(3, 1), (6, 2), (5, 2), (10, 3)]}
for u, v, n, k in product(range(-3, 4), repeat=4):
    up, vp = n * v - k * u, u - k * v
    assert up ** 2 - n * vp ** 2 == (k * k - n) * (u * u - n * v * v)
for n, k in QUOTED["pairs"]:
    assert k * k < n < (k + 1) ** 2
for N in (3, 5):
    # b = 0: a^2 = N; a = 0: 2 b^2 = N <=> (2b)^2 = 2N
    for b in [F(p, q) for p in range(-30, 31) for q in range(1, 13)]:
        assert (2 * b * b == N) == ((2 * b) ** 2 == 2 * N)
for N in (3, 6, 5, 10):
    for p in range(0, 200):
        for q in range(1, 60):
            assert p * p != N * q * q
# the descent on concrete u, v with u^2 close to n v^2: inequalities kv < u < (k+1)v give 0 < v' < v, u' > 0
for n, k in QUOTED["pairs"]:
    for v in range(1, 40):
        for u in range(1, 200):
            if k * v < u < (k + 1) * v and k * u < n * v:
                assert 0 < u - k * v < v and n * v - k * u > 0
print("ok")
