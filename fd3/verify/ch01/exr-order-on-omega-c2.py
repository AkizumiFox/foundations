"""exr-order-on-omega-c2: line (5) fails at m = n = 0 (n <= m holds, n + 1 <= m fails); the repaired step holds on 0..14."""
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

QUOTED = {"m": 0, "n": 0}
m, n = QUOTED["m"], QUOTED["n"]
assert le(m, n) or le(n, m)            # hypothesis of line (3)
assert le(n, m) and not le(S(n), m)    # line (5) fails
assert le(m, S(n))                     # line (6) is still true here
for m in range(15):
    for n in range(15):
        if lt(n, m):
            j = witnesses(n, m)[0]
            assert j != 0 and add(S(n), pred(j)) == m   # repair: m = (n + 1) + j'
        if n == m:
            assert le(m, S(n))
print("ok")
