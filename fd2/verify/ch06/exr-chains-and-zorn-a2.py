"""Section 6.2, A1 (b): X = {1, 2, 3} with a single class. P (subsets meeting the class at most
once) is {{}, {1}, {2}, {3}}; the maximal elements are the three singletons; no greatest element.
A1 (d): on a finite window {0, ..., N-1} u {a, b} of the order, (PO1)-(PO3) hold, every non-empty
chain has an upper bound, and the maximal elements of the full order are a and b (checked on the
window for a, b; no n is maximal since n < n + 1)."""
from itertools import combinations

X = [1, 2, 3]
QUOTED = {
    "P": {frozenset(), frozenset({1}), frozenset({2}), frozenset({3})},
    "maximal": {frozenset({1}), frozenset({2}), frozenset({3})},
}
rel = lambda s, t: True  # a single class: any two elements are related
subsets = [frozenset(c) for r in range(len(X) + 1) for c in combinations(X, r)]
P = {S for S in subsets if all(s == t for s in S for t in S if rel(s, t))}
assert P == QUOTED["P"]
maximal = {M for M in P if not any(M < G for G in P)}
assert maximal == QUOTED["maximal"]
assert not any(all(G <= g for G in P) for g in P)

# (d) on a window
N = 6
E = list(range(N)) + ["a", "b"]
def le(x, y):
    if x == y:
        return True
    if isinstance(x, int) and isinstance(y, int):
        return x <= y
    return isinstance(x, int) and y in ("a", "b")
assert all(le(x, x) for x in E)
assert all(not (le(x, y) and le(y, x)) or x == y for x in E for y in E)
assert all(not (le(x, y) and le(y, z)) or le(x, z) for x in E for y in E for z in E)
chains = [C for r in range(1, len(E) + 1) for C in combinations(E, r)
          if all(le(x, y) or le(y, x) for x in C for y in C)]
assert all(any(all(le(c, u) for c in C) for u in E) for C in chains)
assert not any(set(C) >= {"a", "b"} for C in chains)
assert {m for m in E if not any(le(m, y) and m != y for y in E)} == {"a", "b"}
print("exr-chains-and-zorn-a2: all quoted values check")
