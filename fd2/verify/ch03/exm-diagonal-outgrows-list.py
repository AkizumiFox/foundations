"""exm-diagonal-outgrows-list: g(n) = max{f_0(n), ..., f_n(n)} + 1 satisfies g(n) > f_k(n)
for all n >= k, on random lists of functions on {0, ..., 30}."""
import random

random.seed(2)
N = 31
for _ in range(500):
    f = [[random.randrange(0, 1000) for _ in range(N)] for _ in range(N)]
    g = [max(f[k][n] for k in range(n + 1)) + 1 for n in range(N)]
    for k in range(N):
        for n in range(k, N):
            assert g[n] > f[k][n]
print("exm-diagonal-outgrows-list: all quoted values check")
