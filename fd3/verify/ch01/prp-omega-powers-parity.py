"""prp-omega-powers-parity (a)-(d) for small values, and the Quick check 2^3 = 8 (2^1 = 2, 2^2 = 4)."""
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)

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

QUOTED = {"2^1": 2, "2^2": 4, "2^3": 8}
assert pw(2, 1) == QUOTED["2^1"] and pw(2, 2) == QUOTED["2^2"] and pw(2, 3) == QUOTED["2^3"]
assert mul(1, 2) == 2 and mul(2, 2) == 4 and mul(4, 2) == 8
for b in range(4):
    assert pw(b, 1) == b
    for m in range(3):
        for n in range(3):
            assert pw(b, add(m, n)) == mul(pw(b, m), pw(b, n))     # (a)
            assert pw(b, n) == b ** n
            if b != 0:
                assert pw(b, n) != 0                               # (b)
            if lt(1, b) and lt(m, n):
                assert lt(pw(b, m), pw(b, n))                      # (c)
for n in range(30):
    reps = [(q, r) for q in range(30) for r in (0, 1) if add(mul(2, q), r) == n]
    assert len(reps) == 1                                          # (d)
print("ok")
