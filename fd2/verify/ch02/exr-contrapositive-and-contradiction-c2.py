"""exr-contrapositive-and-contradiction-c2 (F2.2 §04): 3*5 + 1 = 16 = 2^4; 2*7 + 1 = 15 = 3*5;
for lists of primes, p1...pk + 1 has a prime factor off the list (all lists of distinct primes < 30, length <= 3)."""
from itertools import combinations
from math import prod
def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))
assert 3 * 5 + 1 == 16 == 2 ** 4 and 2 * 7 + 1 == 15 == 3 * 5
ps = [p for p in range(2, 30) if is_prime(p)]
for k in (1, 2, 3):
    for L in combinations(ps, k):
        P = prod(L) + 1
        fs = [d for d in range(2, P + 1) if P % d == 0 and is_prime(d)]
        assert fs and all(d not in L for d in fs)
print("exr-contrapositive-and-contradiction-c2: all quoted values check")
