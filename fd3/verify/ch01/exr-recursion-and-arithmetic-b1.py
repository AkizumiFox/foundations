"""exr-recursion-and-arithmetic-b1: 3 * 2 = 6 and 2 * 3 = 6 from the equations, with the
intermediate values 0 + 3 = 3, 3 + 3 = 6, 4 + 2 = 6, 3 * 1 = 3, 2 * 2 = 4."""
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


QUOTED = {"3*2": 6, "2*3": 6, "0+3": 3, "3+3": 6, "4+2": 6, "3*1": 3, "2*2": 4}
for key, v in QUOTED.items():
    a, op, b = key[0], key[1], key[2]
    f = add if op == "+" else mul
    assert f(int(a), int(b)) == v, key
assert 5 == S(4) and 6 == S(5)
print("ok")
