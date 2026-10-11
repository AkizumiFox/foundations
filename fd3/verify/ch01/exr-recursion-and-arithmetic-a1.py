"""exr-recursion-and-arithmetic-a1 (b): partial solutions of thm-omega-recursion
for X = omega, a = 0, g(n, x) = S(S(x)), built on frozensets exactly as in Step 3.

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

QUOTED = {0: {(0, 0)}, 1: {(0, 0), (1, 2)}, 2: {(0, 0), (1, 2), (2, 4)}}

def partial(n):
    """Graph of the partial solution up to n, as a dict input -> value (sets)."""
    G = {E: E}                                  # up to 0: {(0, a)}
    for k in range(n):                          # add the pair at S(k)
        kk = num(k)
        assert S(kk) not in S(kk)               # the new input is new
        G[S(kk)] = S(S(G[kk]))
    assert set(G) == set(S(num(n)))             # domain is S(n)
    return G

for n in range(3):
    G = partial(n)
    assert {(val(k), val(v)) for k, v in G.items()} == QUOTED[n], n
for n in range(10):
    small, big = partial(n), partial(n + 1)
    assert all(big[k] == v for k, v in small.items())   # restriction agrees
print("ok")
