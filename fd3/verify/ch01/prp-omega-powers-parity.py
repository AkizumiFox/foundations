"""prp-omega-powers-parity: b^n by b^0 = 1, b^(n+1) = b^n * b on numerals; (a)-(d)
for small values.

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
def pw(b, n):
    x = num(1)
    for _ in range(n):
        x = mul(x, b)
    return x
for bi in range(4):
    b = num(bi)
    for m in range(4):
        for n in range(4):
            assert pw(b, m + n) == mul(pw(b, m), pw(b, n))                 # (a)
            assert val(pw(b, n)) == bi ** n
            if bi != 0:
                assert pw(b, n) != E                                       # (b)
            if bi > 1 and m < n:
                assert pw(b, m) in pw(b, n)                                # (c)
two = num(2)
for n in range(20):
    reps = [(q, r) for q in range(20) for r in (0, 1) if add(mul(two, num(q)), num(r)) == num(n)]
    assert len(reps) == 1                                                  # (d)
print("ok")
