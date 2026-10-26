"""thm-omega-order (a)-(e) on 0..14, the zero-sum fact, the totality step, and the Quick check (no k with 4 < k < 5; {0..3} = {0,1,2,3})."""
from functools import lru_cache

# A model of the Peano system (N, 0, S): Python ints with S(n) = n + 1 used ONLY
# as the successor; + and * are defined by the recursion equations of
# def-omega-arithmetic, and <= by def-omega-order (n = m + j for some j).


def S(n):
    return n + 1


def pred(n):
    assert n > 0
    return n - 1


@lru_cache(maxsize=None)
def add(m, n):
    # m + 0 = m; m + S(k) = S(m + k)
    return m if n == 0 else S(add(m, pred(n)))


@lru_cache(maxsize=None)
def mul(m, n):
    # m * 0 = 0; m * S(k) = m * k + m
    return 0 if n == 0 else add(mul(m, pred(n)), m)


def pw(b, n):
    # b^0 = 1; b^(n+1) = b^n * b
    return 1 if n == 0 else mul(pw(b, pred(n)), b)


def witnesses(m, n):
    """All j with n = m + j (def-omega-order); the search runs over j <= n + 1,
    which covers every candidate since m + j is reached from j by m steps."""
    return [j for j in range(n + 2) if add(m, j) == n]


def le(m, n):
    return len(witnesses(m, n)) > 0


def lt(m, n):
    return le(m, n) and m != n


def upto(n, lo=0, bound=60):
    """{k : lo <= k <= n}, computed from le."""
    return frozenset(k for k in range(bound) if le(lo, k) and le(k, n))

QUOTED = {"upto3": {0, 1, 2, 3}}
R = range(15)
for j in R:
    for i in R:
        if add(j, i) == 0:
            assert i == 0 and j == 0                               # zero sums
for n in R:
    assert not lt(n, n)                                            # irreflexive
    assert le(n, n)                                                # (PO1)
    for m in R:
        assert le(m, n) or le(n, m)                                # totality
        assert sum([lt(m, n), m == n, lt(n, m)]) == 1              # trichotomy
        if le(m, n) and le(n, m):
            assert m == n                                          # (PO2)
        assert lt(m, S(n)) == le(m, n)                             # (b)
        for k in R:
            if lt(k, m) and lt(m, n):
                assert lt(k, n)                                    # transitive
            if le(k, m) and le(m, n):
                assert le(k, n)                                    # (PO3)
    assert not any(lt(n, k) and lt(k, S(n)) for k in range(30))    # (b), nothing between
    assert upto(0) == {0}
    assert upto(S(n)) == upto(n) | {S(n)} and S(n) not in upto(n)  # (c)
    assert le(0, n) and (n == 0 or le(1, n))                       # (d)
    assert upto(0, lo=1) == frozenset()
    assert upto(S(n), lo=1) == upto(n, lo=1) | {S(n)}              # (e)
assert lt(0, 1)
assert not any(lt(4, k) and lt(k, 5) for k in range(30))
assert upto(3) == QUOTED["upto3"]
print("ok")
