"""exr-limits-b1 (rewritten): (a) (3n+2)/(n+4) - 3 = -10/(n+4), and 10/(n+4) < 10/(n+1);
(b) distance (n+5)/(n^2+1); for n >= 1: n + 5 <= 6n, 1/(n^2+1) < 1/n^2, 6/n <= 12/(n+1) (n + 1 <= 2n),
so (n+5)/(n^2+1) < 12/(n+1); the term at n = 0 is 5. Forward proofs checked on sample eps."""
from fractions import Fraction as Q

QUOTED = {"a_num": -10, "C_a": 10, "C_b": 12, "term_0": 5}
assert Q(0 + 5, 0 + 1) == QUOTED["term_0"]
for n in range(0, 5000):
    assert Q(3 * n + 2, n + 4) - 3 == Q(QUOTED["a_num"], n + 4)
    assert Q(10, n + 4) < Q(QUOTED["C_a"], n + 1)
    if n >= 1:
        assert n + 5 <= 6 * n
        assert Q(1, n * n + 1) < Q(1, n * n)
        assert Q(6, n) <= Q(12, n + 1)
        assert n + 1 <= 2 * n
        assert Q(n + 5, n * n + 1) < Q(6 * n, n * n) == Q(6, n)
        assert Q(n + 5, n * n + 1) < Q(QUOTED["C_b"], n + 1)

for eps in [Q(1, 2), Q(1, 10), Q(3, 7), Q(1, 500)]:
    for C, f, n0 in [(10, lambda n: abs(Q(3 * n + 2, n + 4) - 3), 0), (12, lambda n: Q(n + 5, n * n + 1), 1)]:
        N = 1
        while not Q(1, N) < eps / C:
            N += 1
        assert N >= n0
        assert all(f(n) < Q(C, n + 1) < eps for n in range(N, N + 1000))
print("ok")
