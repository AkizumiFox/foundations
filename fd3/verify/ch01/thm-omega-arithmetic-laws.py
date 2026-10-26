"""thm-omega-arithmetic-laws: every clause (a)-(g) on 0..9, with + and * from the recursive
equations only (a numeric spot check of the proved laws); and the Quick check chain
(km)(n+1) = (km)n + km = k(mn) + km = k(mn + m) = k(m(n+1))."""
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


QUOTED = {}
R = range(10)
for k in R:
    for m in R:
        for n in R:
            assert add(add(k, m), n) == add(k, add(m, n))                  # (c)
            assert mul(m, add(n, k)) == add(mul(m, n), mul(m, k))          # (d)
            assert mul(add(n, k), m) == add(mul(n, m), mul(k, m))          # (d)
            assert mul(mul(k, m), n) == mul(k, mul(m, n))                  # (g)
            chain = [mul(mul(k, m), S(n)), add(mul(mul(k, m), n), mul(k, m)),
                     add(mul(k, mul(m, n)), mul(k, m)), mul(k, add(mul(m, n), m)),
                     mul(k, mul(m, S(n)))]
            assert len(set(chain)) == 1                                    # Quick check
for m in R:
    for n in R:
        assert add(0, n) == n and add(S(m), n) == S(add(m, n))            # (a)
        assert add(m, n) == add(n, m)                                      # (b)
        assert mul(0, n) == 0 and mul(S(m), n) == add(mul(m, n), n)       # (e)
        assert mul(n, 1) == n == mul(1, n)                                 # (e)
        assert mul(m, n) == mul(n, m)                                      # (f)
        # long step of (e), each intermediate term equal
        steps = [mul(S(m), S(n)), add(mul(S(m), n), S(m)), add(add(mul(m, n), n), S(m)),
                 add(mul(m, n), add(n, S(m))), add(mul(m, n), S(add(n, m))),
                 add(mul(m, n), S(add(m, n))), add(mul(m, n), add(m, S(n))),
                 add(add(mul(m, n), m), S(n)), add(mul(m, S(n)), S(n))]
        assert len(set(steps)) == 1
print("ok")
