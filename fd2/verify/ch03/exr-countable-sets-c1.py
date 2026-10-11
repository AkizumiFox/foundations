"""exr-countable-sets-c1: S_N(F) = sum_{k<=N} 1_F(k) 2^k is injective on subsets of {0..N},
bounded by 2^(N+1) - 1, independent of N; sigma(empty) = 0, sigma({0,2}) = 5, sigma({1,3}) = 10."""
from itertools import combinations
QUOTED = {"empty": 0, "{0,2}": 5, "{1,3}": 10}
def S(N, F):
    return sum(2**k for k in range(N + 1) if k in F)
assert S(0, set()) == QUOTED["empty"]
assert S(3, {0, 2}) == QUOTED["{0,2}"] and S(7, {0, 2}) == 5
assert S(3, {1, 3}) == QUOTED["{1,3}"]
for N in range(0, 12):
    subs = [set(c) for r in range(N + 2) for c in combinations(range(N + 1), r)]
    vals = [S(N, F) for F in subs]
    assert len(set(vals)) == len(vals) == 2**(N + 1)
    assert max(vals) == 2**(N + 1) - 1 == sum(2**k for k in range(N + 1))
    assert all(S(N + 3, F) == S(N, F) for F in subs)
print("ok")
