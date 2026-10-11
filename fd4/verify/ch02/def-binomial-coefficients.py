"""def-binomial-coefficients: Pascal recursion; rows n = 0..6 of the table; facts
C(n, k) = 0 for k > n, C(n, n) = 1, C(n, 1) = n (checked for n < 40)."""
QUOTED = {
    0: [1, 0, 0, 0, 0, 0, 0],
    1: [1, 1, 0, 0, 0, 0, 0],
    2: [1, 2, 1, 0, 0, 0, 0],
    3: [1, 3, 3, 1, 0, 0, 0],
    4: [1, 4, 6, 4, 1, 0, 0],
    5: [1, 5, 10, 10, 5, 1, 0],
    6: [1, 6, 15, 20, 15, 6, 1],
}
from math import comb
N = 40
C = [[1 if k == 0 else 0 for k in range(N + 2)]]
for n in range(N):
    prev = C[-1]
    C.append([1] + [prev[k] + prev[k + 1] for k in range(N + 1)])
for n, row in QUOTED.items():
    assert C[n][:7] == row
for n in range(N):
    for k in range(N + 1):
        assert C[n][k] == (comb(n, k) if k <= n else 0)
    assert C[n][n] == 1 and C[n][1] == n
print("ok")
