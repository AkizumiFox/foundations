"""exr-order-on-omega-a1: {k <= 3} = 4; least n with n * n > 10 is 4; squares 0, 1, 4, 9, 16.

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

QUOTED = {"le3": 4, "least": 4, "squares": [0, 1, 4, 9, 16]}
assert frozenset(k for k in (num(i) for i in range(10)) if k in num(3) or k == num(3)) == num(QUOTED["le3"])
sq = [val(mul(num(i), num(i))) for i in range(5)]
assert sq == QUOTED["squares"]
ten = num(10)
least = next(i for i in range(20) if ten in mul(num(i), num(i)))
assert least == QUOTED["least"]
assert all(mul(num(i), num(i)) in ten for i in range(4))
print("ok")
