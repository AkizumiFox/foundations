"""Values quoted in Section 1.1 around def-counterexample-set: the phrase book, its Quick check,
the "Not:" catalogue, the everyday readings, "Where to look first" and its Quick check, fold F1.1-c."""
import sys, pathlib
from fractions import Fraction as Fr
from math import gcd, isqrt
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {
    "minimal pair n": 3, "exactly one x true": 2, "exactly one x false": Fr(1, 2),
    "at least two all three": 6, "at least two only one": -3,
    "qc n": (2, 9, 7), "1.414^2": Fr("1.999396"),
    "x^2 = x solutions": {0, 1}, "stock breaker x": Fr(1, 2), "qc2 x": -1,
}
imp = lambda p, q: (not p) or q
prime = lambda n: n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))
even = lambda n: n % 2 == 0
m3 = lambda n: n % 3 == 0

# phrase-book examples
assert implies_on_grid(lambda x: x > 2, lambda x: x**2 > 4)         # x^2 > 4 provided x > 2
assert all(imp(even(n), even(n * n)) for n in range(-200, 201))    # n^2 even whenever n even
assert prime(2) and even(2)                                         # 2 prime but even
assert not even(9) and not prime(9)                                 # 9 neither even nor prime
assert not (not even(9) and prime(9))                               # 9 not both odd and prime
n = QUOTED["minimal pair n"]
assert not (not even(n) and not prime(n)) and not (even(n) and prime(n))
one = lambda p, q: (p or q) and not (p and q)
x = QUOTED["exactly one x true"];  assert one(x > 0, x < 1) and x > 0 and not x < 1
x = QUOTED["exactly one x false"]; assert x > 0 and x < 1 and not one(x > 0, x < 1)
two = lambda p, q, r: (p and q) or (p and r) or (q and r)
n = QUOTED["at least two all three"];  assert even(n) and n > 0 and m3(n)
n = QUOTED["at least two only one"];   assert (even(n), n > 0, m3(n)) == (False, False, True) and not two(even(n), n > 0, m3(n))
# the at-least-two formula matches "at least two of three" on every valuation
import itertools
for p, q, r in itertools.product([True, False], repeat=3):
    assert two(p, q, r) == (sum((p, q, r)) >= 2)
    assert one(p, q) == (p != q)
# Quick check: exactly one of even, prime at 2, 9, 7
a, b, c = QUOTED["qc n"]
assert [one(even(k), prime(k)) for k in (a, b, c)] == [False, False, True]

# "Not:" catalogue
assert gcd(4, 9) == 1 and isqrt(4)**2 == 4 and isqrt(9)**2 == 9
assert Fr("1.414")**2 == QUOTED["1.414^2"] != 2
assert 12 > 0 and even(12)

# everyday readings: solutions of x^2 = x
sols = {x for x in range(-1000, 1001) if x * x == x}
assert sols == QUOTED["x^2 = x solutions"] and all(s >= 0 for s in sols)
# x^2 - x = x(x - 1): a product is zero only when a factor is, so no other real solution
assert all((x * x == x) == (x == 0 or x == 1) for x in grid())

# "Where to look first": P: x > 2, Q: x > 1, R: x > 0
P, Q, R = (lambda x: x > 2), (lambda x: x > 1), (lambda x: x > 0)
assert implies_on_grid(P, Q) and implies_on_grid(Q, R)
x = QUOTED["stock breaker x"]
assert imp(P(x), Q(x)) and imp(Q(x), R(x)) and not imp(R(x), P(x))
# the conclusion R -> P is false only with R true and P false
assert [(r, p) for r, p in itertools.product([True, False], repeat=2) if not imp(r, p)] == [(True, False)]
# its Quick check: P: x > 1, Q: x > 0 at x = -1
assert implies_on_grid(lambda x: x > 1, lambda x: x > 0)
x = QUOTED["qc2 x"]; assert imp(x > 1, x > 0) and not (x > 0)

# fold F1.1-c: "x > 2; so x > 1" has no numerical counterexample
assert implies_on_grid(lambda x: x > 2, lambda x: x > 1)
print("def-counterexample-set: checks")
