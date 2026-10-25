"""6.3, the well-ordering theorem and its Quick checks.

- Quick check 1: m <=_Z n iff |m| < |n|, or |m| = |n| and m <= n, is a total
  order on a window of Z, and the least element of a non-empty S is -k if
  -k in S, else k, where k = min |s|. Its mirror image (k before -k) too.
- The warning: A_n = {-n, ..., 0} with <= is a well-order; the A_n form a
  chain under (E1); (E2) fails for m < n at b = -n (Quick check 2).
- Quick check 3: c picks -4 from {n : n^2 > 10} and 11 from {n : n > 10}.
- The order (E1)-(E2) is a partial order on the partial objects of a small X,
  and for X = {1, 2} there are five partial objects, two maximal (A1 (e)).
"""
from itertools import combinations, permutations
import random

QUOTED = {
    "qc3_square": -4,
    "qc3_gt10": 11,
    "a1e_count": 5,
    "a1e_maximal": 2,
}


def zle(m, n):
    return abs(m) < abs(n) or (abs(m) == abs(n) and m <= n)


def zle_mirror(m, n):
    return abs(m) < abs(n) or (abs(m) == abs(n) and m >= n)


W = range(-12, 13)


def is_total_order(le, xs):
    for a in xs:
        assert le(a, a)
        for b in xs:
            assert le(a, b) or le(b, a)
            if le(a, b) and le(b, a):
                assert a == b
            for c in xs:
                if le(a, b) and le(b, c):
                    assert le(a, c)
    return True


def least(le, S):
    ms = [m for m in S if all(le(m, s) for s in S)]
    assert len(ms) == 1
    return ms[0]


assert is_total_order(zle, W)
assert is_total_order(zle_mirror, W)
random.seed(1)
for _ in range(3000):
    S = set(random.sample(list(W), random.randint(1, 8)))
    k = min(abs(s) for s in S)
    assert least(zle, S) == (-k if -k in S else k)
    assert least(zle_mirror, S) == (k if k in S else -k)

# Quick check 3 on a window large enough that the least elements lie inside it
big = range(-60, 61)
S1 = [n for n in big if n * n > 10]
S2 = [n for n in big if n > 10]
assert least(zle, S1) == QUOTED["qc3_square"]
assert least(zle, S2) == QUOTED["qc3_gt10"]
assert set(S1) == {n for n in big if abs(n) >= 4}

# The warning's chain
def A(n):
    return list(range(-n, 1))


def R(n):
    return {(a, b) for a in A(n) for b in A(n) if a <= b}


for n in range(0, 7):
    le = lambda a, b, n=n: (a, b) in R(n)
    assert is_total_order(le, A(n))
    for r in range(1, len(A(n)) + 1):
        for S in combinations(A(n), r):
            least(le, S)


def E1(Ar, Bs):
    (Aset, Rr), (Bset, Ss) = Ar, Bs
    return set(Aset) <= set(Bset) and Rr <= Ss


def E2(Ar, Bs):
    (Aset, Rr), (Bset, Ss) = Ar, Bs
    return all((a, b) in Ss for a in Aset for b in set(Bset) - set(Aset))


def tri(Ar, Bs):
    return E1(Ar, Bs) and E2(Ar, Bs)


for m in range(0, 7):
    for n in range(m, 7):
        assert E1((A(m), R(m)), (A(n), R(n)))
        assert tri((A(m), R(m)), (A(n), R(n))) == (m == n)
        if m < n:
            assert (0, -n) not in R(n)

# Partial objects of a small X: (A, R), R a well-order (= total order, A finite)
def partial_objects(X):
    out = []
    for r in range(len(X) + 1):
        for Aset in combinations(X, r):
            for perm in permutations(Aset):
                pos = {x: i for i, x in enumerate(perm)}
                Rr = frozenset((a, b) for a in Aset for b in Aset if pos[a] <= pos[b])
                out.append((frozenset(Aset), Rr))
    return out


P2 = partial_objects([1, 2])
assert len(P2) == QUOTED["a1e_count"]
maxs = [p for p in P2 if not any(tri(p, q) and p != q for q in P2)]
assert len(maxs) == QUOTED["a1e_maximal"]
assert all(p[0] == frozenset({1, 2}) for p in maxs)

for X in ([1, 2], [1, 2, 3]):
    P = partial_objects(X)
    for p in P:
        assert tri(p, p)
        for q in P:
            if tri(p, q) and tri(q, p):
                assert p == q
            for s in P:
                if tri(p, q) and tri(q, s):
                    assert tri(p, s)
    # the top extension of a non-maximal element is strictly larger
    for (M, RM) in P:
        for x in set(X) - set(M):
            M2 = M | {x}
            R2 = RM | {(a, x) for a in M2}
            assert (frozenset(M2), frozenset(R2)) in P
            assert tri((M, RM), (M2, R2))

print("ok")
