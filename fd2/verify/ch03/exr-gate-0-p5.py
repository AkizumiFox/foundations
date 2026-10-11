"""Gate 0, P5: brute-force check of (a) and of (b)'s equivalence on all functions between small sets."""
from itertools import product, chain, combinations

QUOTED = {"points": [4, 3, 3]}
assert sum(QUOTED["points"]) == 10


def subsets(s):
    s = list(s)
    return [frozenset(c) for c in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))]


for nx in range(0, 4):
    for ny in range(1, 4):
        X, Y = range(nx), range(ny)
        for vals in product(Y, repeat=nx):
            f = dict(zip(X, vals))
            pre = lambda B: frozenset(x for x in X if f[x] in B)
            img = lambda A: frozenset(f[a] for a in A)
            SY = subsets(Y)
            # (a) for families of size 0..2 (I = empty included)
            for k in range(0, 3):
                for fam in product(SY, repeat=k):
                    U = frozenset().union(*fam) if fam else frozenset()
                    lhs = pre(frozenset(Y) - U)
                    rhs = frozenset(X)
                    for B in fam:
                        rhs &= frozenset(X) - pre(B)
                    assert lhs == rhs
            # (b)
            inj = len(set(vals)) == nx
            cond = all(img(frozenset(X) - A) <= frozenset(Y) - img(A) for A in subsets(X))
            assert cond == inj
print("ok")
