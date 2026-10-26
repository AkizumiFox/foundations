"""exm-peano-axioms-independent: which of (P3), (P4), (P5) hold (F3.1 s01).

(i), (ii) are finite and checked exhaustively; (iii), two copies of N, is checked
on a truncation, natural numbers modelled by ints with S(n) = n + 1.
"""
from itertools import combinations

QUOTED = {"fails": {"i": "P3", "ii": "P4", "iii": "P5"},
          "iii_missed": (0, "b")}

def subsets(M):
    M = list(M)
    for r in range(len(M) + 1):
        for c in combinations(M, r):
            yield set(c)

def check_finite(M, e, s):
    p3 = all(s[x] != e for x in M)
    p4 = len({s[x] for x in M}) == len(M)
    p5 = all(A == set(M) for A in subsets(M) if e in A and all(s[x] in A for x in A))
    return {"P3": p3, "P4": p4, "P5": p5}

for key, (M, e, s) in {"i": ({0}, 0, {0: 0}), "ii": ({0, 1}, 0, {0: 1, 1: 1})}.items():
    r = check_finite(M, e, s)
    assert [k for k, v in r.items() if not v] == [QUOTED["fails"][key]], (key, r)

# (iii) two copies of N, truncated to first coordinates < N
N = 30
M = [(n, t) for n in range(N) for t in "ab"]
s = lambda x: (x[0] + 1, x[1])
e = (0, "a")
vals = [s(x) for x in M]
assert all(v != e for v in vals)                 # (P3)
assert len(set(vals)) == len(vals)               # (P4)
A = {(n, "a") for n in range(N + 1)}             # N x {a}
assert e in A and all(s(x) in A for x in A if x[0] < N)
assert QUOTED["iii_missed"] not in A and QUOTED["iii_missed"] in M   # (P5) fails
# the only elements with no arrow in are e and (0, b)
targets = set(vals)
assert [x for x in M if x not in targets] == [e, (0, "b")]
print("ok")
