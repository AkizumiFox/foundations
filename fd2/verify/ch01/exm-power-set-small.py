"""exm-power-set-small (Section 6.2): P(empty), P({empty}), P({1,2})."""
from itertools import combinations
QUOTED = {"sizes": (1, 2, 4)}
def P(s):
    s = list(s)
    return {frozenset(c) for k in range(len(s) + 1) for c in combinations(s, k)}
E = frozenset()
assert P(set()) == {E}
assert P({E}) == {E, frozenset({E})}
assert P({1, 2}) == {E, frozenset({1}), frozenset({2}), frozenset({1, 2})}
assert (len(P(set())), len(P({E})), len(P({1, 2}))) == QUOTED["sizes"]
print("exm-power-set-small: all quoted values check")
