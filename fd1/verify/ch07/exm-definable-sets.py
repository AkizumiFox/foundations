"""exm-definable-sets (Section 7.5): the sets defined in (a)-(d), checked on windows of N
(with witnesses searched in the window), primes against a sieve; the Quick check on Z and Q;
and the minimal change (dropping not-U(x) adds exactly 1)."""
from fractions import Fraction as F

QUOTED = {"window": 200}
W = range(0, QUOTED["window"] + 1)
# (a) squares of reals: every square is >= 0, every x >= 0 is (sqrt x)^2
import math
assert all(y * y >= 0 for y in [k / 7 for k in range(-70, 71)])
assert all(abs(math.sqrt(x) ** 2 - x) < 1e-9 for x in [0, 0.25, 2, 9, 1e4])
# (b) x + x = x defines {0}; exists z (z+z != z and x + z = y) defines x < y
assert [d for d in W if d + d == d] == [0]
for x in range(0, 60):
    for y in range(0, 60):
        assert any(z + z != z and x + z == y for z in range(0, 120)) == (x < y)
# (c) U(x): forall y (x*y = y) defines {1}
U = lambda x: all(x * y == y for y in W)
assert [d for d in W if U(d)] == [1]
# (d) primes
sieve = [True] * (len(W)); sieve[0] = sieve[1] = False
for i in range(2, len(W)):
    if sieve[i]:
        for j in range(2 * i, len(W), i):
            sieve[j] = False
primes = {d for d in W if sieve[d]}
def prime_formula(x, with_notU=True):
    body = all(not (y * z == x) or U(y) or U(z) for y in W for z in W)
    return (not U(x) if with_notU else True) and body
small = range(0, 80)
assert {d for d in small if prime_formula(d)} == {d for d in small if d in primes}
assert {d for d in small if prime_formula(d, False)} == {d for d in small if d in primes} | {1}
# Quick check: exists y (x = y + y) in Z: evens; in Q: everything (y = x/2)
assert [x for x in range(-20, 21) if any(x == y + y for y in range(-20, 21))] == list(range(-20, 21, 2))
for x in [F(1), F(-3, 7), F(5, 2)]:
    assert x / 2 + x / 2 == x
print("exm-definable-sets: all quoted values check")
