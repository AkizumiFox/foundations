"""def-omega-arithmetic (Section 9.5): numerals; n + 1 = S(n); 1 + 1 = 2; k + 2 = (k + 1) + 1;
and the Quick check after cor-omega-successor-cancellation: 2 + 2 = 4, 2 * 2 = 4, 0 + 2 = 2.

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

QUOTED = {"1+1": 2, "2+2": 4, "2*2": 4, "0+2": 2, "2*1": 2, "0+1": 1}

one, two = num(1), num(2)
assert one == S(E) and two == S(one)
assert val(add(one, one)) == QUOTED["1+1"]
assert val(add(two, two)) == QUOTED["2+2"]
assert val(mul(two, two)) == QUOTED["2*2"]
assert val(add(E, two)) == QUOTED["0+2"]
assert val(add(E, one)) == QUOTED["0+1"]
assert val(mul(two, one)) == QUOTED["2*1"]
for k in range(12):
    n = num(k)
    assert add(n, one) == S(n)                      # n + 1 = S(n)
    assert add(n, two) == add(add(n, one), one)     # k + 2 = (k + 1) + 1
    for m in range(8):
        assert val(add(num(m), n)) == m + k and val(mul(num(m), n)) == m * k
print("ok")
