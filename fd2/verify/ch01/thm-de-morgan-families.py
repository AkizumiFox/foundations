"""thm-de-morgan-families (Section 6.2): both laws for all families (with repetition) of subsets
of a 3-element X indexed by sets of size 0..3; the swapped-law warning."""
from itertools import combinations, product
QUOTED = {}
X = frozenset({1, 2, 3})
subs = [frozenset(c) for k in range(4) for c in combinations(sorted(X), k)]
def big_union(fam):
    out = frozenset()
    for S in fam:
        out |= S
    return out
def big_inter(fam):  # inside X
    out = X
    for S in fam:
        out &= S
    return out
for n in range(4):
    for fam in product(subs, repeat=n):
        comp = [X - S for S in fam]
        assert X - big_union(fam) == big_inter(comp)
        assert X - big_inter(fam) == big_union(comp)
# empty family
assert big_union(()) == frozenset() and big_inter(()) == X
# warning
X2, A1, A2 = {1, 2}, {1}, {2}
assert X2 - (A1 | A2) == set() and (X2 - A1) | (X2 - A2) == {1, 2}
print("thm-de-morgan-families: all quoted values check")
