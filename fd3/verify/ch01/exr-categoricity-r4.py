"""exr-categoricity-r4: union S(n) = n and union S(k) = k on numerals; x = {1} gives
union S(x) = {0, 1} = 2 != x; union S(x) = x iff x transitive, on a small universe of
hereditarily finite sets."""
from itertools import combinations
E0 = frozenset()
def S(x): return x | frozenset([x])
def U(x): return frozenset().union(*x) if x else E0
def num(k):
    x = E0
    for _ in range(k): x = S(x)
    return x
QUOTED = {"union_S_x": 2}
for n in range(9):
    assert U(S(num(n))) == num(n)
    assert U(num(n)) == (E0 if n == 0 else num(n - 1))
x = frozenset([num(1)])
assert U(x) == num(1)
assert U(S(x)) == num(QUOTED["union_S_x"]) and U(S(x)) != x
assert E0 in num(2) and E0 not in x
# universe: all subsets of {0, 1, 2, {1}}
base = [num(0), num(1), num(2), x]
universe = [frozenset(c) for r in range(len(base) + 1) for c in combinations(base, r)]
for y in universe:
    transitive = all(z <= y for z in y)
    assert (U(S(y)) == y) == transitive
    assert U(S(y)) == U(y) | y
print("ok")
