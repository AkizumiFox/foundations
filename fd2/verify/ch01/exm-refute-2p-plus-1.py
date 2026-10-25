"""exm-refute-2p-plus-1 (F2.1 §01) and the Quick check after exm-method-counterexample:
2p + 1 for p = 2, 3, 5 is 5, 7, 11 (prime); p = 7 gives 15 = 3*5; p = 4 gives 9 (warning);
p = 2 and p = 11 give 5 and 23 (prime). Also the prime examples after def-prime and n = 3 | 2^3 + 1."""
QUOTED = {"first": {2: 5, 3: 7, 5: 11}, "break": (7, 15, 3, 5), "warn": (4, 9),
          "check": {2: 5, 11: 23}, "primes": (2, 3, 5, 7), "nonprimes": (9, 15, 1), "exist": (3, 9)}

def is_prime(p):
    return p >= 2 and [d for d in range(1, p + 1) if p % d == 0] == [1, p]

for p, v in QUOTED["first"].items():
    assert is_prime(p) and 2 * p + 1 == v and is_prime(v)
p, v, d1, d2 = QUOTED["break"]
assert is_prime(p) and 2 * p + 1 == v == d1 * d2 and not is_prime(v) and v % d1 == 0
assert min(q for q in range(2, 100) if is_prime(q) and not is_prime(2 * q + 1)) == 7
p, v = QUOTED["warn"]
assert not is_prime(p) and 2 * p + 1 == v and not is_prime(v)
for p, v in QUOTED["check"].items():
    assert is_prime(p) and 2 * p + 1 == v and is_prime(v)
assert all(is_prime(q) for q in QUOTED["primes"]) and not any(is_prime(q) for q in QUOTED["nonprimes"])
assert all(7 % d != 0 for d in range(2, 7))
n, v = QUOTED["exist"]
assert n > 1 and 2 ** n + 1 == v and v % n == 0
print("exm-refute-2p-plus-1: all quoted values check")
