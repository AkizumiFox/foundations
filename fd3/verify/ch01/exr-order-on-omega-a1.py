"""exr-order-on-omega-a1: (a) m < n implies m + 1 <= n; (b) 5 <= 2 fails; (c) {0..2} = {0,1,2}, {1..2} = {1,2}; (d) 5 - 2 = 3."""
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

QUOTED = {"upto2": {0, 1, 2}, "oneto2": {1, 2}, "5-2": 3}
for m in range(15):
    for n in range(15):
        if lt(m, n):
            assert le(S(m), n)
assert lt(2, 5) and not le(5, 2)
assert upto(2) == QUOTED["upto2"] and upto(2, lo=1) == QUOTED["oneto2"]
assert witnesses(2, 5) == [QUOTED["5-2"]]
print("ok")
