"""prp-power-set-count: a set with n elements has 2^n subsets; P(A) splits into subsets without/with a."""
from itertools import combinations
QUOTED = {"P_empty": 1}
def subsets(s):
    s = list(s)
    return [frozenset(c) for r in range(len(s) + 1) for c in combinations(s, r)]
assert len(subsets([])) == QUOTED["P_empty"] == 2**0
for n in range(0, 10):
    A = set(range(n + 1)); a = n; X = A - {a}
    PX = subsets(X); T = {S | {a} for S in PX}
    assert len(T) == len(PX) == 2**n
    assert set(PX).isdisjoint(T)
    assert set(PX) | T == set(subsets(A))
    assert len(subsets(A)) == 2**(n + 1)
print("ok")
