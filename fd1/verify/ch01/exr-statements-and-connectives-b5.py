"""Sixteen translations of exr-statements-and-connectives-b5 checked against their English, -30 <= n <= 30."""
from math import isqrt
QUOTED = {"16 false at": 3, "7 vs 6 at": 2}
imp = lambda p, q: (not p) or q
prime = lambda n: n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

for n in range(-30, 31):
    E, P, T, G = n % 2 == 0, prime(n), n % 3 == 0, n > 10
    odd = n % 2 != 0
    formulas = {
        1: E and G, 2: not E, 3: E and P, 4: imp(P and G, not E), 5: T and not P,
        6: (not E) and (not T), 7: not (E and T), 8: imp(P, (not E) or (not G)),
        9: imp(T and G, E), 10: imp(G, imp(E, not P)), 11: imp(E and T, G),
        12: (E or P) and not (E and P), 13: (E and P) or (E and T) or (P and T),
        14: (not E) and imp(G, not T), 15: imp(not G, E or T), 16: imp(P and not E, G),
    }
    english = {
        1: n % 2 == 0 and n > 10, 2: odd, 3: n % 2 == 0 and prime(n),
        4: (not (prime(n) and n > 10)) or odd, 5: n % 3 == 0 and not prime(n),
        6: not (n % 2 == 0) and not (n % 3 == 0), 7: not (n % 2 == 0 and n % 3 == 0),
        8: (not prime(n)) or odd or n <= 10, 9: (not (n % 3 == 0 and n > 10)) or n % 2 == 0,
        10: (not n > 10) or (not n % 2 == 0) or not prime(n), 11: (not (n % 2 == 0 and n % 3 == 0)) or n > 10,
        12: [n % 2 == 0, prime(n)].count(True) == 1,
        13: [n % 2 == 0, prime(n), n % 3 == 0].count(True) >= 2,
        14: odd and ((not n > 10) or n % 3 != 0), 15: n > 10 or n % 2 == 0 or n % 3 == 0,
        16: (not (prime(n) and odd)) or n > 10,
    }
    assert formulas == english, n
    assert formulas[10] == imp(G and E, not P)   # the equivalent form of 10

n = QUOTED["16 false at"]
assert n % 2 == 1 and prime(n) and not n > 10
n = QUOTED["7 vs 6 at"]
assert not ((n % 2 != 0) and (n % 3 != 0)) and not (n % 2 == 0 and n % 3 == 0)
print("exr-statements-and-connectives-b5: checks")
