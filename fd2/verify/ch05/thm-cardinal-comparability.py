"""5.2 Quick check after thm-cardinal-comparability: partial matchings between
A = {1, 2, 3} and B = {x, y}; maximal ones are the six two-pair matchings, none
pairs all of A, each pairs all of B. Also A1 (c): A = {} gives P = {{}}."""
from itertools import combinations


def matchings(A, B):
    pairs = [(a, b) for a in A for b in B]
    out = []
    for r in range(len(pairs) + 1):
        for G in combinations(pairs, r):
            G = frozenset(G)
            if len({a for a, _ in G}) == len(G) and len({b for _, b in G}) == len(G):
                out.append(G)
    return out


def maximal(P):
    return [M for M in P if not any(M < G for G in P)]


A, B = [1, 2, 3], ["x", "y"]
P = matchings(A, B)
Ms = maximal(P)
assert len(Ms) == 6
assert all(len(M) == 2 for M in Ms)
assert all({b for _, b in M} == set(B) for M in Ms)
assert not any({a for a, _ in M} == set(A) for M in Ms)
assert all(len(G) < 2 for G in P if G not in Ms)
assert matchings([], B) == [frozenset()]
print("thm-cardinal-comparability: ok,", len(P), "partial matchings, 6 maximal")
