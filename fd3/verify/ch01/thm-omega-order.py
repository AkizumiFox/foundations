"""thm-omega-order and the warning after it: < is membership on numerals 0..9;
n = {m : m < n}; {0..n} = S(n); {1..n} = S(n) minus {0}; the warning's sets.

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

QUOTED = {}  # no numeric values quoted; the assertions check the claims
N = [num(i) for i in range(10)]
for i, m in enumerate(N):
    for j, n in enumerate(N):
        assert (m in n) == (i < j)
        assert sum([m in n, m == n, n in m]) == 1                  # trichotomy
        if m in n:
            assert S(m) in S(n)                                    # the claim
    assert m == frozenset(k for k in N if k in m)                  # (c)
    assert S(m) == frozenset(k for k in N if k in m or k == m)     # {0..n}
    assert S(m) - {E} == frozenset(k for k in N if (num(1) in k or num(1) == k) and (k in m or k == m))  # (e)
a = E; b = frozenset([E]); c = frozenset([b])
assert a in b and b in c and a not in c
print("ok")
