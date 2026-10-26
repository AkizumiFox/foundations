"""prp-pair-not-natural and its warning: (0, 1) = {1, 2}; Wiener's pair (ch09 s04)."""
from itertools import product
F = frozenset
E = F()
def S(x): return F(x | {x})
def kpair(a, b): return F([F([a]), F([a, b])])
def wpair(a, b): return F([F([F([a]), E]), F([F([b])])])
num = [E]
for _ in range(9):
    num.append(S(num[-1]))

QUOTED = {"pair_0_1": [1, 2], "wiener_0_1": "{2, {{1}}}"}

p = kpair(num[0], num[1])
assert p == F(num[k] for k in QUOTED["pair_0_1"])
assert num[1] in p and num[0] not in p
w = wpair(num[0], num[1])
assert w == F([num[2], F([F([num[1]])])])
assert num[1] not in w

# no Kuratowski pair over a small universe is one of the numerals, and none contains emptyset
U = list(num[:5]) + [F([num[1]]), F([num[2]]), kpair(num[0], num[0])]
for a, b in product(U, repeat=2):
    q = kpair(a, b)
    assert q != E and E not in q and q not in num
print("ok")
