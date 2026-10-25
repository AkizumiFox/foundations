"""lem-one-step-order-extension: for every partial order on a 4-element set and every
incomparable pair (a, b), R = order u {(x, y): x <= a, b <= y} is a partial order
containing the order and (a, b). Also the Quick check on P({1, 2}) and C1 on all
partial orders of a 4-element set (order = intersection of its total extensions)."""
from itertools import product

X = range(4)
allpairs = [(x, y) for x in X for y in X if x != y]


def is_po(R):
    return (all((x, x) in R for x in X)
            and all(not ((x, y) in R and (y, x) in R) for x, y in allpairs)
            and all((x, z) in R for (x, y) in R for (w, z) in R if y == w))


diag = {(x, x) for x in X}
orders = []
for bits in product([0, 1], repeat=len(allpairs)):
    R = diag | {p for p, b in zip(allpairs, bits) if b}
    if is_po(R):
        orders.append(frozenset(R))
assert len(orders) == 219, len(orders)
totals = [T for T in orders if all((x, y) in T or (y, x) in T for x, y in allpairs)]
assert len(totals) == 24
count = 0
for O in orders:
    for a, b in allpairs:
        if (a, b) in O or (b, a) in O:
            continue
        R = set(O) | {(x, y) for x in X for y in X if (x, a) in O and (b, y) in O}
        assert is_po(R) and O <= R and (a, b) in R and (a, b) not in O
        count += 1
    ext = [T for T in totals if O <= T]
    assert ext and frozenset.intersection(*ext) == O  # C1
# Quick check on P({1,2}), coded 0 = {}, 1 = {1}, 2 = {2}, 3 = {1,2}
sets = [frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})]
S = {(i, j) for i in range(4) for j in range(4) if sets[i] <= sets[j]}
new = {(x, y) for x in range(4) for y in range(4) if (x, 1) in S and (2, y) in S}
assert new - S == {(1, 2)}
R = S | new
assert all((x, y) in R for x in range(4) for y in range(4) if x <= y)  # order 0,1,2,3
print("lem-one-step-order-extension: ok,", len(orders), "orders,", count, "incomparable cases")
