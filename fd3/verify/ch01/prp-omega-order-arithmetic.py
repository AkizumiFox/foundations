"""prp-omega-order-arithmetic and the Quick check before it: 3 < 5, 5 = {0,1,2,3,4},
5 - 2 = 3 (unique j); clauses (a)-(f) on numerals 0..7.

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

QUOTED = {"5-2": 3}
assert num(3) in num(5) and num(5) == frozenset(num(i) for i in range(5))
js = [j for j in range(8) if add(num(2), num(j)) == num(5)]
assert js == [QUOTED["5-2"]]
R = [num(i) for i in range(8)]
lt = lambda x, y: x in y
for m in R:
    for n in R:
        js = [j for j in R if add(m, j) == n]
        assert (len(js) == 1) == (lt(m, n) or m == n) and len(js) <= 1     # (a)
        if lt(m, n):
            assert js[0] != E
        for k in R:
            if add(m, k) == add(n, k):
                assert m == n                                              # (b)
            if lt(m, n):
                assert lt(add(m, k), add(n, k))                            # (c)
                if k != E:
                    assert lt(mul(m, k), mul(n, k))                        # (e)
            if k != E and mul(m, k) == mul(n, k):
                assert m == n                                              # (f)
        if mul(m, n) == E:
            assert m == E or n == E                                        # (d)
print("ok")
