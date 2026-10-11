"""exr-the-least-upper-bound-property-r3: S_k(s) = sum_{i<=k} 2 s_i / 3^{i+1};
tail bound 0 <= S_m - S_k <= 1/3^{k+1} - 1/3^{m+1} (m >= k); 1/3^{k+1} < 1/(k+1) via 3^{k+1} >= 2^{k+1} >= k + 2;
for s != t first differing at j with s_j = 1, t_j = 0: S_k(s) - S_k(t) >= 1/3^{j+1} for all k >= j.
Checked for all s, t in {0,1}^8."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"gap": r"\delta \coloneqq 1/3^{j+1}"}
gap = lambda j: F(1, 3 ** (j + 1))
L = 8
def S(s):
    out, acc = [], F(0)
    for i, b in enumerate(s):
        acc += F(2 * b, 3 ** (i + 1))
        out.append(acc)
    return out
seqs = list(product((0, 1), repeat=L))
sums = {s: S(s) for s in seqs}
for s in seqs:
    Ss = sums[s]
    for k in range(L):
        for m in range(k, L):
            assert 0 <= Ss[m] - Ss[k] <= F(1, 3 ** (k + 1)) - F(1, 3 ** (m + 1))
for k in range(100):
    assert 3 ** (k + 1) >= 2 ** (k + 1) >= k + 2 and F(1, 3 ** (k + 1)) < F(1, k + 1)
for s in seqs:
    for t in seqs:
        if s == t:
            continue
        j = min(i for i in range(L) if s[i] != t[i])
        if s[j] == 0:
            continue
        assert sums[s][j] - sums[t][j] == F(2, 3 ** (j + 1))
        for k in range(j, L):
            assert sums[s][k] - sums[t][k] >= gap(j)
print("ok")
