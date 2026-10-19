"""thm-structural-recursion (Ch 4, Section 4.3): the non-example after the fold. The positive integers
built from 1 by "add one" and "double": adding one alone reaches every one; clauses per building step
can clash (g(2) in {0, 1}; the Quick check's h(2) in {3, 2}; drill (k)'s g(4) in {4, 3}); A1 (e):
g(n) = n obeys g(1) = 1, g(n+1) = g(n) + 1, g(2n) = 2g(n)."""
QUOTED = {"g(2) values": (1, 0), "h(2) values": (3, 2)}


def values_at(n, one, add, dbl, limit=64):
    """All values the clauses can assign at n, following every way n is built (memoized)."""
    memo = {1: {one}}
    for k in range(2, limit + 1):
        vals = set()
        for v in memo[k - 1]:
            vals.add(add(v))
        if k % 2 == 0:
            for v in memo[k // 2]:
                vals.add(dbl(v))
        memo[k] = vals
    return memo[n]


# adding one alone reaches every positive integer: 1, 2, 3, ... (trivially, k = 1 + (k - 1) ones)
assert values_at(2, 0, lambda v: v + 1, lambda v: v) == {1, 0}           # the g of the text
assert values_at(2, 1, lambda v: v + 2, lambda v: 2 * v) == {3, 2}       # the h of the Quick check
assert values_at(4, 1, lambda v: v + 1, lambda v: v + 1) >= {4, 3}       # drill (k): g(4)
assert values_at(2, 1, lambda v: v + 1, lambda v: v + 1) == {2}
assert values_at(3, 1, lambda v: v + 1, lambda v: v + 1) == {3}
# A1 (e): clauses that happen to agree: every way of building n gives n
for n in range(1, 65):
    assert values_at(n, 1, lambda v: v + 1, lambda v: 2 * v) == {n}
print("thm-structural-recursion: all quoted values check")
