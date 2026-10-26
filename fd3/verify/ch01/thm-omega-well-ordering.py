"""thm-omega-well-ordering, the Quick check: least n with n*n > 10 is 4; squares 0, 1, 4, 9, 16; 10 = 9 + 1, 16 = 10 + 6; and least elements of random subsets of 0..19."""
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

import random
QUOTED = {"least": 4, "squares": [0, 1, 4, 9, 16], "10-9": 1, "16-10": 6}
assert [mul(i, i) for i in range(5)] == QUOTED["squares"]
assert witnesses(9, 10) == [QUOTED["10-9"]] and witnesses(10, 16) == [QUOTED["16-10"]]
A = [n for n in range(30) if lt(10, mul(n, n))]
least = [a for a in A if all(le(a, x) for x in A)]
assert least == [QUOTED["least"]]
assert all(le(mul(x, x), 9) for x in range(4))
random.seed(1)
for _ in range(200):
    B = {x for x in range(20) if random.random() < 0.3}
    if B:
        L = [a for a in B if all(le(a, x) for x in B)]
        assert len(L) == 1 and L[0] == min(B)
print("ok")
