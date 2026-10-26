"""prp-peano-predecessor: (a), (b) on a truncation of N, and the Quick check on structure (ii)
of exm-peano-axioms-independent (the element 1 has two predecessors; (a) and (b) fail there)."""
QUOTED = {"ii_two_predecessors": 1, "ii_predecessors": {0, 1}}

N = 200
S = lambda n: n + 1
for x in range(1, N):
    assert sum(1 for y in range(N) if S(y) == x) == 1      # (a)
assert all(S(x) != x for x in range(N))                     # (b)
# the set A of the proof: e together with the values of S, on the truncation, is everything
A = {0} | {S(y) for y in range(N - 1)}
assert A == set(range(N))

# structure (ii): M = {0, 1}, e = 0, s(0) = s(1) = 1
s = {0: 1, 1: 1}
preds = {x for x in s if s[x] == QUOTED["ii_two_predecessors"]}
assert preds == QUOTED["ii_predecessors"]
assert s[1] == 1          # (b) fails at 1
print("ok")
