"""exm-groups and the hook before def-group: the units of Z/12Z are [1], [5], [7], [11],
each its own inverse; the quarter turn of a square; bijections of a three-element set
do not commute; bijections of a two-element set do."""
from itertools import permutations
from math import gcd

QUOTED = {
    "units12": {1, 5, 7, 11},
    "squares12": {5: (25, 2), 7: (49, 4), 11: (121, 10)},  # a*a = q*12 + 1
    "quarter_turn": {1: 2, 2: 3, 3: 4, 4: 1},
}
units = {a for a in range(12) if any(a * b % 12 == 1 for b in range(12))}
assert units == QUOTED["units12"] == {a for a in range(12) if gcd(a, 12) == 1}
for a in units:
    assert a * a % 12 == 1
for a, (sq, q) in QUOTED["squares12"].items():
    assert a * a == sq == q * 12 + 1
qt = QUOTED["quarter_turn"]
assert sorted(qt.values()) == [1, 2, 3, 4]
assert all(qt[i] == i + 1 for i in (1, 2, 3)) and qt[4] == 1

def comp(f, g):  # f o g
    return {x: f[g[x]] for x in g}
# x, y, z = 1, 2, 3: f swaps x, y; g swaps y, z
f = {1: 2, 2: 1, 3: 3}
g = {1: 1, 2: 3, 3: 2}
assert comp(f, f) == {1: 1, 2: 2, 3: 3}
assert comp(f, g)[1] == 2 and comp(g, f)[1] == 3
# a two-element set: the group of bijections is abelian
bij2 = [dict(zip((1, 2), p)) for p in permutations((1, 2))]
assert all(comp(a, b) == comp(b, a) for a in bij2 for b in bij2)
print("exm-groups: ok")
