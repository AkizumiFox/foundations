"""exr-recursion-and-arithmetic-c3: D(0) = 0, D(n + 1) = (D(n) + 1) + 1 gives D(n) = n + n = 2n;
D(1) = 2, D(2) = 4."""
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


QUOTED = {"D1": 2, "D2": 4}
D = [0]
for n in range(40):
    D.append(S(S(D[-1])))
assert D[1] == QUOTED["D1"] and D[2] == QUOTED["D2"]
for n in range(41):
    assert D[n] == add(n, n) == mul(2, n) == mul(n, 2)
print("ok")
