"""def-peano-system: the loop and the merge of F3.1 s01, and the first Quick check.
QUOTED: which of (P3), (P4), (P5) fail for each."""
from itertools import combinations

QUOTED = {"loop": ["P3"], "merge": ["P4"]}

def subsets(M):
    M = list(M)
    for r in range(len(M) + 1):
        for c in combinations(M, r):
            yield set(c)

def failing(M, e, s):
    p3 = all(s[x] != e for x in M)
    p4 = len({s[x] for x in M}) == len(M)
    p5 = all(A == set(M) for A in subsets(M) if e in A and all(s[x] in A for x in A))
    return [k for k, v in (("P3", p3), ("P4", p4), ("P5", p5)) if not v]

M = {"p", "q", "r"}
loop = {"p": "q", "q": "r", "r": "p"}
merge = {"p": "q", "q": "r", "r": "q"}
assert failing(M, "p", loop) == QUOTED["loop"]
assert failing(M, "p", merge) == QUOTED["merge"]
assert merge["p"] == merge["r"] == "q"
# second Quick check after prp-peano-predecessor: in the loop every element has exactly one predecessor
assert all(sum(1 for y in M if loop[y] == x) == 1 for x in M)
print("ok")
