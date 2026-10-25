"""exm-list-two-element-subsets: c(S) = 2^min S * 3^max S is injective on the two-element subsets of {0..40};
n -> {0, n + 1} is injective into P_2; Quick check (3.1): n^2 + 3n values in N."""
from itertools import combinations
M = 41
codes = {}
for s, t in combinations(range(M), 2):
    c = 2 ** min(s, t) * 3 ** max(s, t)
    assert c not in codes, (s, t, codes.get(c))
    codes[c] = frozenset((s, t))
assert len(codes) == M * (M - 1) // 2
imgs = [frozenset((0, n + 1)) for n in range(500)]
assert all(len(S) == 2 for S in imgs) and len(set(imgs)) == len(imgs)
assert all(n * n + 3 * n >= 0 for n in range(1000))
print("ok")
