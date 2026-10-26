"""exr-two-non-examples-c2: S_k(s) = sum_{n<=k} 2 s_n / 3^{n+1}; tail bound
0 <= S_m - S_k <= 1/3^{k+1} - 1/3^{m+1}; S_k <= 1; for s != s' first differing at j with s_j = 1:
sup S(s) >= c + 2/3^{j+1} and S_k(s') <= c + 1/3^{j+1} for every k, so the gap is >= 1/3^{j+1}.
Checked exactly for all s, s' in {0,1}^8."""
from fractions import Fraction as F
from itertools import product
QUOTED = {"terms": r"\frac{2 s_n}{3^{n+1}}", "tail": r"\frac{1}{3^{k+1}}"}
L = 8
def S(s):
    out, acc = [], F(0)
    for i, b in enumerate(s):
        acc += F(2 * b, 3 ** (i + 1)); out.append(acc)
    return out
seqs = list(product((0, 1), repeat=L)); sums = {s: S(s) for s in seqs}
assert F(-1, 3) + F(2, 9) == F(-1, 9)
for s in seqs:
    for k in range(L):
        assert sums[s][k] <= 1
        for m in range(k, L):
            assert 0 <= sums[s][m] - sums[s][k] <= F(1, 3 ** (k + 1)) - F(1, 3 ** (m + 1))
for s in seqs:
    for t in seqs:
        if s == t: continue
        j = min(i for i in range(L) if s[i] != t[i])
        if s[j] == 0: continue
        c = sums[s][j - 1] if j else F(0)
        assert c == (sums[t][j - 1] if j else F(0))
        assert sums[s][j] == c + F(2, 3 ** (j + 1))
        assert all(x <= c + F(1, 3 ** (j + 1)) for x in sums[t])
print("ok")
