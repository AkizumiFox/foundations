"""exr-limits-b4: verdicts T, F, T, T, F, T.
(b) (-1)^(2n) = 1, (-1)^(2n+1) = -1; (-1)^n has both values beyond every N (diverges).
(e) a_n = (1 + (-1)^n)/2, b_n = (1 - (-1)^n)/2: values 1,0,1,... and 0,1,0,...; a_n b_n = 0;
    for eps = 1, every N has an n in {N, N+1} with |a_n| = 1 and one with |b_n| = 1.
(a), (c), (d), (f): brute-force sanity on sample convergent sequences in Q."""
from fractions import Fraction as Q

QUOTED = {"verdicts": ("True", "False", "True", "True", "False", "True")}

# (b)
for n in range(0, 2000):
    assert (-1) ** (2 * n) == 1 and (-1) ** (2 * n + 1) == -1
    assert (-1) ** (n + 2) == (-1) ** n
# (-1)^n: for eps = 1 and each candidate a, consecutive terms are 2 apart, so not both within 1
for N in range(0, 200):
    assert abs((-1) ** (N + 1) - (-1) ** N) == 2

# (e)
for n in range(0, 2000):
    an = Q(1 + (-1) ** n, 2)
    bn = Q(1 - (-1) ** n, 2)
    assert an == (1 if n % 2 == 0 else 0) and bn == (0 if n % 2 == 0 else 1)
    assert an * bn == 0
for N in range(0, 500):
    pair = [N, N + 1]
    assert any(Q(1 + (-1) ** n, 2) == 1 for n in pair)
    assert any(Q(1 - (-1) ** n, 2) == 1 for n in pair)
    assert sorted(n % 2 for n in pair) == [0, 1]

# sanity for the true parts on sample sequences
samples = [
    (lambda n: Q(1, n + 1), Q(0)),
    (lambda n: Q(3 * n + 2, n + 4), Q(3)),
    (lambda n: Q(2 * n + (-1) ** n, n + 1), Q(2)),
]
for f, lim in samples:
    for eps in [Q(1, 3), Q(1, 20), Q(1, 200)]:
        # an N valid for f (checked on a long range), then (a) and (d)
        N = next(N for N in range(0, 5000) if all(abs(f(n) - lim) < eps for n in range(N, N + 3000)))
        assert all(abs(f(2 * n) - lim) < eps for n in range(N, N + 1500))  # (a)
        N2 = next(N for N in range(0, 5000) if all(abs(f(n) - lim) < eps / 2 for n in range(N, N + 3000)))
        assert all(abs(f(n + 1) - f(n)) < eps for n in range(N2, N2 + 1500))  # (d)
        # (c) with |b_n| <= |a_n|: b_n = a_n * (-1)^n / 2 for the null case
        if lim == 0:
            assert all(abs(f(n) * (-1) ** n / 2) < eps for n in range(N, N + 1500))

# (f): an integer-valued convergent sequence (eventually constant) in Q; the 1/2-threshold
# forces a_n = a_N, since an integer k with |k| < 1 is 0
for k in range(-3, 4):
    assert (abs(k) < 1) == (k == 0)
g = lambda n: 7 if n < 5 else 4
N = next(N for N in range(0, 100) if all(abs(g(n) - 4) < Q(1, 2) for n in range(N, N + 100)))
assert all(g(n) == g(N) for n in range(N, N + 100))
print("ok")
