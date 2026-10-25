"""thm-frobenius-homomorphism: opening (1 + 2)^5 = 243 = 48*5 + 3 and 1 + 32 = 33 = 6*5 + 3 in F5;
try-it-first rows 5, 6 reduced mod 5; (x+y)^6 = x^6 + x^5 y + x y^5 + y^6 in F5 (all pairs);
warning: (1+1)^2 = 1 vs 2 in F3, (1+1)^4 = 0 vs 2 in Z/4Z, 2^n != 2 for n >= 2.
Also Fr additive and multiplicative on F_p for p < 40 and bijective."""
from math import comb
QUOTED = {"243": (48, 3), "33": (6, 3), "row5": [1, 0, 0, 0, 0, 1], "row6": [1, 1, 0, 0, 0, 1, 1],
          "F3": (1, 2), "Z4": (0, 2)}
q, r = QUOTED["243"]
assert 3 ** 5 == 243 == q * 5 + r and r == 3
q, r = QUOTED["33"]
assert 1 + 2 ** 5 == 33 == q * 5 + r and r == 3
assert [comb(5, k) % 5 for k in range(6)] == QUOTED["row5"]
assert [comb(6, k) % 5 for k in range(7)] == QUOTED["row6"]
for x in range(5):
    for y in range(5):
        assert pow(x + y, 6, 5) == (x**6 + x**5 * y + x * y**5 + y**6) % 5
assert ((1 + 1) ** 2 % 3, (1 + 1) % 3) == QUOTED["F3"]
assert ((1 + 1) ** 4 % 4, (1 + 1) % 4) == QUOTED["Z4"]
assert comb(4, 2) % 4 != 0
assert all(2 ** n != 2 for n in range(2, 40))
for p in range(2, 40):
    if all(p % d for d in range(2, p)):
        for x in range(p):
            for y in range(p):
                assert pow(x + y, p, p) == (pow(x, p, p) + pow(y, p, p)) % p
                assert pow(x * y, p, p) == (pow(x, p, p) * pow(y, p, p)) % p
        assert len({pow(x, p, p) for x in range(p)}) == p
print("ok")
