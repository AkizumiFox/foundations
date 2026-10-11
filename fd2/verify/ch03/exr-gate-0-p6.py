"""Gate 0, P6: the shifted diagonal stays in S and misses the list; |E_N| = (N+1)!."""
import random
from math import factorial, prod
from itertools import product

QUOTED = {"EN_sizes": [1, 2, 6, 24, 120], "points": [1, 2, 2, 1, 2, 2]}
assert sum(QUOTED["points"]) == 10

L = 40  # check sequences on places 0..L-1


def diag(fs):
    g = [0]
    for n in range(L - 1):
        g.append(0 if fs[n][n + 1] != 0 else 1)
    return g


random.seed(1)
for trial in range(300):
    fs = [[random.randint(0, k) for k in range(L)] for _ in range(L)]
    if trial % 3 == 0:
        for f in fs:
            for k in range(L):
                f[k] = 0 if random.random() < 0.5 else f[k]
    g = diag(fs)
    assert all(g[k] <= k for k in range(L))            # g in S
    assert all(g[n + 1] != fs[n][n + 1] for n in range(L - 1))  # differs at n + 1
# the naive diagonal g(n) = f_n(n) + 1 leaves S at place 0
assert all(f[0] == 0 for f in fs) and fs[0][0] + 1 > 0

# |E_N|: sequences determined by (a_0..a_N), a_k <= k
for N, size in enumerate(QUOTED["EN_sizes"]):
    count = sum(1 for _ in product(*[range(k + 1) for k in range(N + 1)]))
    assert count == size == factorial(N + 1) == prod(range(1, N + 2))
# E_0 is only the zero sequence
assert sum(1 for _ in product(range(1))) == 1
print("ok")
