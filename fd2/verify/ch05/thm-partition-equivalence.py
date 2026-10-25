"""thm-partition-equivalence, Quick check after the correspondence paragraph: among all 2^16
relations on {1, 2, 3, 4}, exactly 7 are equivalence relations with two classes, and there are
exactly 7 partitions of {1, 2, 3, 4} into two blocks (4 singleton-plus-triple, 3 pair-plus-pair).
Sanity check: 5 equivalence relations on {1, 2, 3}."""
from itertools import product

QUOTED = {"two_classes_on_4": 7, "singleton_split": 4, "pair_split": 3, "all_on_3": 5}

def equivalences(X):
    pairs = [(x, y) for x in X for y in X]
    out = []
    for bits in product((0, 1), repeat=len(pairs)):
        R = {p for p, b in zip(pairs, bits) if b}
        if all((x, x) in R for x in X) and all((y, x) in R for (x, y) in R) and \
           all((x, z) in R for (x, y) in R for (w, z) in R if y == w):
            out.append(R)
    return out

def classes(R, X):
    return {frozenset(y for y in X if (y, x) in R) for x in X}

X4 = (1, 2, 3, 4)
eq4 = equivalences(X4)
two = [R for R in eq4 if len(classes(R, X4)) == 2]
assert len(two) == QUOTED["two_classes_on_4"]
# two-block partitions by subsets
blocks = set()
for mask in range(1, 15):
    A = frozenset(x for i, x in enumerate(X4) if mask >> i & 1)
    blocks.add(frozenset({A, frozenset(X4) - A}))
assert len(blocks) == 7
assert sum(1 for P in blocks if min(len(B) for B in P) == 1) == QUOTED["singleton_split"]
assert sum(1 for P in blocks if min(len(B) for B in P) == 2) == QUOTED["pair_split"]
assert {frozenset(classes(R, X4)) for R in two} == blocks
assert len(equivalences((1, 2, 3))) == QUOTED["all_on_3"]
print("thm-partition-equivalence: all quoted values check")
