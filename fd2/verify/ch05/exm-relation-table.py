"""exm-relation-table: witnesses and sample checks; and the Quick check on common prime factors."""
from fractions import Fraction as Fr
from itertools import product, combinations

QUOTED = {}


def props(X, rel):
    X = list(X)
    R = all(rel(x, x) for x in X)
    S = all(rel(y, x) for x, y in product(X, X) if rel(x, y))
    A = all(x == y for x, y in product(X, X) if rel(x, y) and rel(y, x))
    T = all(rel(x, z) for x, y, z in product(X, X, X) if rel(x, y) and rel(y, z))
    return (R, S, A, T)


reals = [Fr(n, 2) for n in range(-6, 7)]
divides = lambda a, b: (b == 0) if a == 0 else (b % a == 0)
assert props(reals, lambda x, y: x == y) == (True, True, True, True)
assert props(reals, lambda x, y: x <= y) == (True, False, True, True)
assert props(reals, lambda x, y: x < y) == (False, False, True, True)
X = [1, 2]
subsets = [frozenset(c) for r in range(3) for c in combinations(X, r)]
assert props(subsets, lambda a, b: a <= b) == (True, False, True, True)
assert props(range(0, 25), divides) == (True, False, True, True)
assert props(range(-12, 13), divides) == (True, False, False, True)
assert props(reals, lambda x, y: (x - y).denominator == 1) == (True, True, False, True)
assert props([1, 2, 3], lambda x, y: False) == (False, True, True, True)
# witnesses quoted
assert 0 <= 1 and not 1 <= 0 and not 0 < 0
assert divides(1, 2) and not divides(2, 1) and divides(2, -2) and divides(-2, 2)
# degenerate: full relation antisymmetric iff |X| <= 1; subset order on P(empty) symmetric
for n in range(4):
    assert props(range(n), lambda x, y: True)[2] == (n <= 1)
assert props([frozenset()], lambda a, b: a <= b) == (True, True, True, True)


def common_prime(x, y):
    return any(x % p == 0 and y % p == 0 for p in range(2, min(x, y) + 1)
               if all(p % d for d in range(2, p)))


assert props(range(2, 40), common_prime) == (True, True, False, False)
assert common_prime(2, 6) and common_prime(6, 3) and not common_prime(2, 3)
assert common_prime(2, 4) and common_prime(4, 2)
print("ok")
