"""exr-writing-proofs-b2 (Ch 5, Section 5.5): eps/2 + eps/2 = eps; n >= max(N1, N2) gives n >= N1
and n >= N2; for a_n = 1/(n + 1), L = 0, no N1 serves eps = 1/(N1 + 2), since
a_{N1} = 1/(N1 + 1) >= 1/(N1 + 2); a numeric run of the sum-of-limits proof."""
from fractions import Fraction as F
QUOTED = {}
for N1 in range(0, 300):
    eps = F(1, N1 + 2)
    assert F(1, N1 + 1) >= eps
for e in [F(1), F(1, 3), F(1, 100)]:
    assert e / 2 + e / 2 == e
    # a_n = 1/(n+1) -> 0, b_n = 2 + 1/(n+1)^2 -> 2
    def N_for(seq, L, eps):
        N = 0
        while not all(abs(seq(n) - L) < eps for n in range(N, N + 2000)):
            N += 1
        return N
    a = lambda n: F(1, n + 1)
    b = lambda n: 2 + F(1, (n + 1) ** 2)
    N1, N2 = N_for(a, 0, e / 2), N_for(b, 2, e / 2)
    N = max(N1, N2)
    for n in range(N, N + 500):
        assert n >= N1 and n >= N2
        assert abs((a(n) + b(n)) - 2) <= abs(a(n)) + abs(b(n) - 2) < e
print("exr-writing-proofs-b2: all quoted values check")
