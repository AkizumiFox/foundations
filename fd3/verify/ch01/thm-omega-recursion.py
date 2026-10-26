"""thm-omega-recursion: the smallest closed set R of pairs, generated from (0, a) by the step
(n, x) -> (S(n), g(n, x)), is a graph; Quick check: for X = N, a = 0, g(n, x) = S(S(x)), the
pairs of R with first coordinate 0, 1, 2 are (0, 0), (1, 2), (2, 4). Warning: X = {0}, g = S(0)
leaves X. Also several finite X, where the closure is computed exactly."""
# The Peano system (N, 0, S) of ax-natural-numbers is modelled by Python ints with S(n) = n + 1;
# + and * are computed from their recursive equations only (def-omega-arithmetic).
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)


def S(n):
    return n + 1


def pred(n):
    """The k with S(k) = n, for n != 0 (prp-peano-predecessor (a))."""
    assert n != 0
    return n - 1


@lru_cache(maxsize=None)
def add(m, n):
    # m + 0 = m; m + S(k) = S(m + k)
    return m if n == 0 else S(add(m, pred(n)))


@lru_cache(maxsize=None)
def mul(m, n):
    # m * 0 = 0; m * S(k) = m * k + m
    return 0 if n == 0 else add(mul(m, pred(n)), m)


QUOTED = {0: {(0, 0)}, 1: {(1, 2)}, 2: {(2, 4)}}


def R_upto(a, g, N):
    """Elements of the smallest closed set with first coordinate <= N.  An element of R is
    reached from (0, a) by finitely many steps, and each step raises the first coordinate by
    one, so the pairs with first coordinate <= N are those reached in <= N steps."""
    level = {(0, a)}
    out = set(level)
    for _ in range(N):
        level = {(S(n), g(n, x)) for (n, x) in level}
        out |= level
    return out


R = R_upto(0, lambda n, x: S(S(x)), 10)
for k, v in QUOTED.items():
    assert {p for p in R if p[0] == k} == v
for n in range(11):
    assert len({x for (k, x) in R if k == n}) == 1       # the claim of Step 3

# finite X: brute-force the smallest closed subset of {0..N} x X (truncated at N) by
# intersecting all closed subsets is too large, so check minimality: removing any pair breaks closure
for Xs, g in [((0, 1, 2), lambda n, x: (x + n) % 3), ((0, 1), lambda n, x: 1 - x)]:
    Rg = R_upto(0, g, 8)
    for n in range(9):
        assert len({x for (k, x) in Rg if k == n}) == 1
    for p in Rg:
        Rp = Rg - {p}
        closed = (0, 0) in Rp and all((S(n), g(n, x)) in Rp for (n, x) in Rp if n < 8)
        assert not closed

# warning: X = {0}, g(n, x) = S(0) = 1 is not in X
X = {0}
assert S(0) not in X and S(0) != 0
print("ok")
