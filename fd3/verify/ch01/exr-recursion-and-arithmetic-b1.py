"""exr-recursion-and-arithmetic-b1: 3 * 2 = 6 and 2 * 3 = 6 from the equations, with the
intermediate values 0 + 3 = 3, 3 + 3 = 6, 4 + 2 = 6.

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

QUOTED = {"3*2": 6, "2*3": 6, "0+3": 3, "3+3": 6, "4+2": 6, "3*1": 3, "2*2": 4}
for key, v in QUOTED.items():
    a, op, b = key[0], key[1], key[2]
    f = add if op == "+" else mul
    assert val(f(num(int(a)), num(int(b)))) == v, key
assert num(5) == S(num(4)) and num(6) == S(num(5))
print("ok")
