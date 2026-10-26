"""exr-recursion-and-arithmetic-a1 (c): 0 * n = 0 by induction on n; spot check from the equations."""
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


QUOTED = {"0*0": 0}
assert mul(0, 0) == QUOTED["0*0"]
for n in range(50):
    assert mul(0, S(n)) == add(mul(0, n), 0) == 0
print("ok")
