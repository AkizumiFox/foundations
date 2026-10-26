"""def-omega-arithmetic (F3.1 §02): numerals 1 = S(0), 2 = S(1), ...; n + 1 = S(n); 1 + 1 = 2;
k + 2 = (k + 1) + 1; the non-example g(n, x) = S(n) gives 2 + 1 = 1; the Quick check after
cor-omega-successor-cancellation: 2 + 2 = 4, 2 * 2 = 4, 0 + 2 = 2."""
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


QUOTED = {"1+1": 2, "2+2": 4, "2*2": 4, "0+2": 2, "2*1": 2, "0+1": 1, "fake 2+1": 1, "S(f(0))": 3}

one, two = S(0), S(S(0))
assert add(one, one) == QUOTED["1+1"] == S(one)
assert add(two, two) == QUOTED["2+2"]
assert mul(two, two) == QUOTED["2*2"]
assert add(0, two) == QUOTED["0+2"]
assert add(0, one) == QUOTED["0+1"]
assert mul(two, one) == QUOTED["2*1"]
# non-example: f(0) = m, f(S(n)) = S(n); with m = 2, f(1) = 1, S(f(0)) = 3
m = 2
f = lambda n: m if n == 0 else S(pred(n))
assert f(1) == QUOTED["fake 2+1"] and S(f(0)) == QUOTED["S(f(0))"]
for k in range(30):
    assert add(k, one) == S(k)                      # n + 1 = S(n)
    assert add(k, two) == add(add(k, one), one)     # k + 2 = (k + 1) + 1
    for j in range(20):
        assert add(j, k) == j + k and mul(j, k) == j * k
print("ok")
