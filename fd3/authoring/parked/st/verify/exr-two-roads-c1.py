"""exr-two-roads-c1 (Section 7.6): the threshold (N eps > 1 and 2^n >= n + 1 give 2^{-n} < eps), and the
rule a_n = a + (k_n - 1) 2^{-n} run on alpha = sigma from a = 1: a_n in alpha, a_n + 2^{-n} not in alpha,
a_n < a_m + 2^{-m}, so -2^{-m} < a_m - a_n < 2^{-n} and |a_m - a_n| < 2^{-min(m, n)}. Also run on
alpha = {q < 1} from a = 0 (a_n = 1 - 2^{-n}), where the chain with m and n swapped fails."""
from fractions import Fraction as F
import math

QUOTED = {"threshold": True}

def in_sigma(p):
    return p <= 0 or p * p < 2

for eps in [F(1), F(1, 2), F(1, 3), F(3, 100), F(1, 1000), F(7, 1000003)]:
    N = math.floor(1 / eps) + 1          # N eps > 1
    assert N * eps > 1
    for n in range(N, N + 40):
        assert 2 ** n >= n + 1 and F(1, 2 ** n) < eps

a = F(1)
seq = []
for n in range(0, 16):
    e = F(1, 2 ** n)
    k = 0
    while in_sigma(a + k * e):
        k += 1
    assert k >= 1
    an = a + (k - 1) * e
    assert in_sigma(an) and not in_sigma(an + e)
    seq.append(an)
for m in range(16):
    for n in range(16):
        assert seq[n] < seq[m] + F(1, 2 ** m)
        assert -F(1, 2 ** m) < seq[m] - seq[n] < F(1, 2 ** n)
        assert abs(seq[m] - seq[n]) < F(1, 2 ** min(m, n))

def run(member, a, count=16):
    out = []
    for n in range(count):
        e = F(1, 2 ** n)
        k = 0
        while member(a + k * e):
            k += 1
        assert k >= 1
        out.append(a + (k - 1) * e)
    return out

seq1 = run(lambda p: p < 1, F(0))
assert all(seq1[n] == 1 - F(1, 2 ** n) for n in range(16))
for m in range(16):
    for n in range(16):
        assert -F(1, 2 ** m) < seq1[m] - seq1[n] < F(1, 2 ** n)
# the swapped chain -2^{-n} < a_m - a_n < 2^{-m} fails, e.g. at m = 5, n = 1
assert not (seq1[5] - seq1[1] < F(1, 2 ** 5))
print("ok")
