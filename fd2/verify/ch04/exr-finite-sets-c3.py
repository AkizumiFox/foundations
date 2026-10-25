"""exr-finite-sets-c3: |I(k, n)| = n!/(n-k)! for k <= n <= 6 and 0 for k > n;
s_v, t_v range and round trips; Phi a bijection I(k+1, n) -> {1..n} x I(k, n-1); I(2, 3) listed."""
from itertools import permutations, product
from math import factorial

def I(k, n):
    # an injection {1..k} -> {1..n} is its tuple of values (phi(1), ..., phi(k))
    return set(permutations(range(1, n + 1), k))

def brute_I(k, n):
    return {t for t in product(range(1, n + 1), repeat=k) if len(set(t)) == k}

def s(v, x): return x if x < v else x + 1
def t(v, y): return y if y < v else y - 1   # only used for y != v

for n in range(0, 7):
    for k in range(0, 8):
        assert I(k, n) == brute_I(k, n)
        if k > n:
            assert len(I(k, n)) == 0
        else:
            assert len(I(k, n)) == factorial(n) // factorial(n - k)

for n in range(1, 7):
    for v in range(1, n + 1):
        dom = list(range(1, n))
        cod = [y for y in range(1, n + 1) if y != v]
        assert sorted(s(v, x) for x in dom) == cod          # s_v lands in and covers {1..n}\{v}
        assert all(t(v, s(v, x)) == x for x in dom)          # t_v o s_v = id
        assert all(s(v, t(v, y)) == y for y in cod)          # s_v o t_v = id
        assert all(1 <= t(v, y) <= n - 1 for y in cod)       # t_v lands in {1..n-1}

for n in range(1, 7):
    for k in range(0, n):
        src = I(k + 1, n)
        Phi = {phi: (phi[k], tuple(t(phi[k], phi[i]) for i in range(k))) for phi in src}
        target = {(v, psi) for v in range(1, n + 1) for psi in I(k, n - 1)}
        assert set(Phi.values()) == target and len(set(Phi.values())) == len(src)
        Psi = {(v, psi): tuple(s(v, x) for x in psi) + (v,) for (v, psi) in target}
        assert all(Psi[Phi[phi]] == phi for phi in src)
        assert all(n * factorial(n - 1) // factorial(n - 1 - k) == factorial(n) // factorial(n - k - 1) for _ in [0])

assert sorted(I(2, 3)) == [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("ok")
