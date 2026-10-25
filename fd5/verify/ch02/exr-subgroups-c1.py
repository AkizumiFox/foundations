"""exr-subgroups-c1: every non-empty subset of S_3 closed under products is a subgroup
(brute force over all 63 non-empty subsets)."""
from itertools import permutations, combinations
def mul(s, t):
    return tuple(s[t[i]] for i in range(3))
def inv(s):
    r = [0] * 3
    for i, j in enumerate(s):
        r[j] = i
    return tuple(r)
QUOTED = {}  # no numeric value is quoted in the text; structural brute-force check only
G = list(permutations(range(3)))
e = (0, 1, 2)
count = 0
for r in range(1, 7):
    for H in combinations(G, r):
        H = set(H)
        if all(mul(a, b) in H for a in H for b in H):
            count += 1
            assert e in H and all(inv(a) in H for a in H)
assert count == 6  # {e}, three of order 2, A_3, S_3
print("exr-subgroups-c1: ok")
