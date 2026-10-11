"""exr-writing-proofs-c2 (Ch 5, Section 5.5): with N from eps = 1 and
M = max(|a_0|, ..., |a_{N-1}|, |L| + 1), |a_n| <= M for every n; run on sample sequences."""
from fractions import Fraction as F
QUOTED = {"eps": 1}
samples = [
    (lambda n: F((-1) ** n * 5, n + 1) + 3, 3),
    (lambda n: F(10 ** 3, (n + 1) ** 2) - 2, -2),
    (lambda n: F(n, n + 1), 1),
]
for a, L in samples:
    N = 0
    while not all(abs(a(n) - L) < 1 for n in range(N, N + 3000)):
        N += 1
    M = max([abs(a(n)) for n in range(N)] + [abs(L) + 1])
    for n in range(0, N + 3000):
        if n >= N:
            assert abs(a(n)) <= abs(a(n) - L) + abs(L) < 1 + abs(L) <= M
        assert abs(a(n)) <= M
print("exr-writing-proofs-c2: all quoted values check")
