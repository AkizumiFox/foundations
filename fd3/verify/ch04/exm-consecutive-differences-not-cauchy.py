"""exm-consecutive-differences-not-cauchy: H_0 = 0, H_{n+1} = H_n + 1/(n+1); first terms
0, 1, 3/2, 11/6, 25/12; H_{n+k} - H_n >= k/(n+k) for n >= 1; H_{2n} - H_n >= 1/2;
with n = N + 1, m = 2n: |H_m - H_n| >= 1/2; the n steps from n to 2n are each below 1/n."""
from fractions import Fraction as F
QUOTED = {"first": [F(0), F(1), F(3, 2), F(11, 6), F(25, 12)], "half": F(1, 2)}
H = [F(0)]
for n in range(400):
    H.append(H[-1] + F(1, n + 1))
assert H[:5] == QUOTED["first"]
for n in range(1, 120):
    for k in range(0, 120):
        assert H[n + k] - H[n] >= F(k, n + k)
    assert H[2 * n] - H[n] >= QUOTED["half"]
    assert all(F(1, j + 1) < F(1, n) for j in range(n, 2 * n))
for N in range(150):
    n = N + 1; m = 2 * n
    assert m >= N and n >= N and abs(H[m] - H[n]) >= F(1, 2)
for n in range(1, 300):
    assert H[n + 1] - H[n] == F(1, n + 1)
print("ok")
