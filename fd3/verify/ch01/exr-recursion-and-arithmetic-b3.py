"""exr-recursion-and-arithmetic-b3: verdicts T, F, F, T, F and the counterexamples
(b) m = n = 0; (c) m = 0, n = 1 (0 * 2 = 0, 0 * 1 + 1 = 1); (e) n = 1."""
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


QUOTED = {"verdicts": ("True", "False", "False", "True", "False"), "c lhs": 0, "c rhs": 1}
B = range(25)
a = all(not (add(m, n) == 0) or (m == 0 and n == 0) for m in B for n in B)
b = all(not (mul(m, n) == m) or n == 1 for m in B for n in B)
c = all(mul(m, S(n)) == add(mul(m, n), n) for m in B for n in B)
d = all(not (add(m, n) == m) or n == 0 for m in B for n in B)
e = all(not (mul(n, n) == n) or n == 0 for n in B)
got = "".join("T" if v else "F" for v in (a, b, c, d, e))
assert tuple({"T": "True", "F": "False"}[c] for c in got) == QUOTED["verdicts"], got
assert mul(0, 0) == 0 and 0 != 1                                   # (b)
assert mul(0, 2) == QUOTED["c lhs"] and add(mul(0, 1), 1) == QUOTED["c rhs"]   # (c)
assert mul(1, 1) == 1 and 1 != 0                                   # (e)
print("ok")
