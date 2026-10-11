"""thm-omega-arithmetic-laws: every clause (a)-(g), on numerals 0..6, with + and *
computed from the recursive equations only (a numeric spot check of the proved laws).

Sets are frozensets; numerals are von Neumann numerals."""
from functools import lru_cache

E = frozenset()
_NUM = [E]                 # canonical (interned) numerals, so comparisons stay cheap
_IDX = {id(E): 0}


def _raw_S(x):
    return x | frozenset([x])


def num(n):
    while len(_NUM) <= n:
        y = _raw_S(_NUM[-1])
        _IDX[id(y)] = len(_NUM)
        _NUM.append(y)
    return _NUM[n]


def S(x):
    """Successor x u {x}; returns the interned numeral when x is one."""
    if id(x) in _IDX:
        return num(_IDX[id(x)] + 1)
    return _raw_S(x)


def val(x):
    """The integer named by a numeral."""
    n = _IDX.get(id(x))
    assert n is not None and x is num(n), "not an interned numeral"
    return n


def pred(x):
    """The k with S(k) = x, for a numeral x != 0."""
    n = val(x)
    assert n > 0
    return num(n - 1)


@lru_cache(maxsize=None)
def add(m, n):
    # m + 0 = m; m + S(k) = S(m + k)
    if n == E:
        return m
    return S(add(m, pred(n)))


@lru_cache(maxsize=None)
def mul(m, n):
    # m * 0 = 0; m * S(k) = m * k + m
    if n == E:
        return E
    return add(mul(m, pred(n)), m)


def pair(a, b):
    return frozenset([frozenset([a]), frozenset([a, b])])

QUOTED = {}
R = [num(i) for i in range(7)]
one = num(1)
for k in R:
    for m in R:
        for n in R:
            assert add(add(k, m), n) == add(k, add(m, n))                  # (c)
            assert mul(m, add(n, k)) == add(mul(m, n), mul(m, k))          # (d)
            assert mul(add(n, k), m) == add(mul(n, m), mul(k, m))          # (d)
            assert mul(mul(k, m), n) == mul(k, mul(m, n))                  # (g)
for m in R:
    for n in R:
        assert add(E, n) == n and add(S(m), n) == S(add(m, n))            # (a)
        assert add(m, n) == add(n, m)                                      # (b)
        assert mul(E, n) == E and mul(S(m), n) == add(mul(m, n), n)       # (e)
        assert mul(n, one) == n == mul(one, n)                             # (e)
        assert mul(m, n) == mul(n, m)                                      # (f)
print("ok")
