"""exm-peano-axioms-independent: which of (P3), (P4), (P5) hold (ch09 s04)."""
from itertools import combinations

QUOTED = {"fails": {"i": "P3", "ii": "P4", "iii": "P5"}}

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

r1 = check_finite({0}, 0, {0: 0})
r2 = check_finite({0, 1}, 0, {0: 1, 1: 1})
for r, key in ((r1, "i"), (r2, "ii")):
    failing = [k for k, v in r.items() if not v]
    assert failing == [QUOTED["fails"][key]], (key, r)

# (iii) on omega x 3 truncated to first coordinates < N (natural numbers as ints here;
# the structure's definition only uses S, its injectivity and 0 != S(k))
N = 6
M = [(n, i) for n in range(N) for i in range(3)]
def s(x):
    n, i = x
    if i == 0: return (n + 1, 0)
    if i == 1: return (n + 1, 1)
    return (0, 1) if n == 0 else (n - 1, 2)
e = (0, 0)
vals = [s(x) for x in M]
assert all(v != e for v in vals)                      # (P3)
assert len(set(vals)) == len(vals)                     # (P4) on the truncation
A = {(n, 0) for n in range(N + 1)}
assert e in A and all(s(x) in A for x in A if x[0] < N)  # closed (within truncation)
assert (0, 1) not in A                                 # (P5) fails
# every element has at most one arrow in; only e (in the top row) has none, inside the truncation
ins = {}
for x in M:
    ins.setdefault(s(x), []).append(x)
assert all(len(v) == 1 for v in ins.values())
no_in = [x for x in M if x not in ins]
assert no_in == [e, (N - 1, 2)]   # (N-1, 2) has no predecessor only because of the truncation

# tagged numbers omega x {0}: injective, never e, on a truncation
T = [(n, 0) for n in range(N)]
assert all((n + 1, 0) != (0, 0) for n, _ in T)

# C2 (b), (c) on the truncation: R_m, L_k good (closed within range); L_k forced
def good(A):
    return e in A and all(s(x) in A for x in A if x[0] < N - 1)
G0 = {(n, 0) for n in range(N)}
for m in range(N):
    R = G0 | {(n, 1) for n in range(N) if m <= n}
    assert good(R)
for k in range(N - 1):
    L = G0 | {(n, 1) for n in range(N)} | {(j, 2) for j in range(k + 1)}
    assert good(L)
    # closure of {e, (k,2)} under s, within the truncation, is L_k
    C, todo = set(), [e, (k, 2)]
    while todo:
        x = todo.pop()
        if x in C or x[0] >= N: continue
        C.add(x); todo.append(s(x))
    assert C == L, k
print("ok")
