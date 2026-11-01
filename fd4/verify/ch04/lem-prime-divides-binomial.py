"""lem-prime-divides-binomial: p | C(p, k) for 0 < k < p, primes p < 50; C(4, 2) = 6, 4 does not
divide 6, gcd(4, 2) = 2; check: 3 C(7, 3) = 7 C(6, 2) = 105, C(7, 3) = 35 = 5 * 7 = 15 + 20."""
from math import comb, gcd
QUOTED = {"c42": 6, "c62": 15, "c73": 35, "c63": 20, "prod": 105}
for p in range(2, 50):
    if all(p % d for d in range(2, p)):
        assert all(comb(p, k) % p == 0 for k in range(1, p))
assert comb(4, 2) == QUOTED["c42"] and QUOTED["c42"] % 4 != 0 and gcd(4, 2) == 2
assert comb(6, 2) == QUOTED["c62"] and comb(6, 3) == QUOTED["c63"]
assert 3 * comb(7, 3) == 7 * QUOTED["c62"] == QUOTED["prod"]
assert comb(7, 3) == QUOTED["c73"] == 5 * 7 == QUOTED["c62"] + QUOTED["c63"]
print("ok")
