"""thm-pigeonhole: no injection {1..m} -> {1..n} for m > n (small cases, brute force),
and the Case 2 construction g = f o sigma lands injectively in {1..n}."""
from itertools import product

QUOTED = {"max_n_checked": 4}

def injective(f):
    return len(set(f.values())) == len(f)

for n in range(QUOTED["max_n_checked"] + 1):
    for m in range(n + 1, n + 3):
        dom = range(1, m + 1)
        for vals in product(range(1, n + 1), repeat=m):
            assert not injective(dict(zip(dom, vals)))

# Case 2 construction, tested on every injective f: {1..m} -> {1..n+1} hitting n+1
for n in range(0, 4):
    for m in range(1, n + 2):
        for vals in product(range(1, n + 2), repeat=m):
            f = dict(zip(range(1, m + 1), vals))
            if not injective(f) or (n + 1) not in vals:
                continue
            j = [i for i in f if f[i] == n + 1][0]
            sigma = {i: (m if i == j else i) for i in range(1, m)}
            assert len(set(sigma.values())) == len(sigma)
            assert all(sigma[i] != j for i in sigma)
            g = {i: f[sigma[i]] for i in sigma}
            assert all(1 <= v <= n for v in g.values())
            assert injective(g)
print("ok")
