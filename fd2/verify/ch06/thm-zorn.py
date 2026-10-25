"""Section 6.1, Quick check after thm-zorn: P = {{1}, {2}, {1, 3}} under inclusion. The only chain
with at least two elements is {{1}, {1, 3}}; every non-empty chain has an upper bound in P; the
maximal elements are {2} and {1, 3}; no greatest element. Also B4 (a): the
chains of {{1}, {2}} are bounded and there is no greatest element."""
from itertools import combinations

P = [frozenset({1}), frozenset({2}), frozenset({1, 3})]
QUOTED = {"long_chains": [{frozenset({1}), frozenset({1, 3})}],
          "maximal": {frozenset({2}), frozenset({1, 3})}}


def chains(P):
    out = []
    for r in range(1, len(P) + 1):
        for c in combinations(P, r):
            if all(a <= b or b <= a for a, b in combinations(c, 2)):
                out.append(set(c))
    return out


cs = chains(P)
assert [c for c in cs if len(c) >= 2] == QUOTED["long_chains"]
assert all(any(all(x <= u for x in c) for u in P) for c in cs)
maximal = {m for m in P if not any(m < a for a in P)}
assert maximal == QUOTED["maximal"]
assert not any(all(a <= g for a in P) for g in P)
# B4 (a): {{1}, {2}}: every chain bounded, no greatest
Q = [frozenset({1}), frozenset({2})]
assert all(any(all(x <= u for x in c) for u in Q) for c in chains(Q))
assert not any(all(a <= g for a in Q) for g in Q)
print("thm-zorn: all quoted values check")
