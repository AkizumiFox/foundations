"""Section 5.1, Quick check after exm-zorn-representatives: X = Z, m ~ n iff m - n even. The
two-element partial objects are exactly {e, o} (e even, o odd), and these are exactly the maximal
ones; {0, 1} and {4, -7} are examples. Checked on the window Z cap [-8, 8]."""
from itertools import combinations

W = list(range(-8, 9))
QUOTED = {"examples": [{0, 1}, {4, -7}]}
rel = lambda m, n: (m - n) % 2 == 0
partial = lambda S: all(not rel(s, t) for s, t in combinations(S, 2))
two = [set(c) for c in combinations(W, 2) if partial(c)]
assert all(sum(x % 2 == 0 for x in S) == 1 for S in two)
assert len(two) == 9 * 8  # 9 even, 8 odd in the window
# no partial object has three elements (pigeonhole on parity), so two-element ones are maximal
assert not any(partial(c) for c in combinations(W, 3))
# one-element sets are not maximal
assert all(any(partial({x, y}) for y in W if y != x) for x in W)
for S in QUOTED["examples"]:
    assert partial(S) and len(S) == 2
print("exm-zorn-representatives: all quoted values check")
