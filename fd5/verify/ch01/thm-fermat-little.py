"""thm-fermat-little: a^p = a in F_p, a^(p-1) = 1 for a != 0, a^(p-2) = a^{-1}, p | a^p - a for
a in [-60, 60], primes p < 60. Check: 2^6 = 64 = 9*7 + 1; 3^5 = 243 = 22*11 + 1, 3^10 = 1 in F11.
After the proof: 2^4 - 2 = 14 and 2^3 - 1 = 7 not multiples of 4, 4 does not divide 2;
for a != 0, a^(q(p-1)+r) = a^r."""
QUOTED = {"64": (9, 1), "243": (22, 1)}
for p in range(2, 60):
    if all(p % d for d in range(2, p)):
        for a in range(p):
            assert pow(a, p, p) == a
            if a:
                assert pow(a, p - 1, p) == 1 and (a * pow(a, p - 2, p)) % p == 1
        for a in range(-60, 61):
            assert (a ** p - a) % p == 0
            if a % p:
                assert (a ** (p - 1) - 1) % p == 0
q, r = QUOTED["64"]
assert 2 ** 6 == 64 == q * 7 + r
q, r = QUOTED["243"]
assert 3 ** 5 == 243 == q * 11 + r and pow(3, 10, 11) == 1
assert 2 ** 4 - 2 == 14 and 14 % 4 and 2 ** 3 - 1 == 7 and 7 % 4 and 2 % 4
assert pow(2, 4, 4) == 0 != 2
for p in (2, 3, 5, 7, 11, 13):
    for a in range(1, p):
        for q in range(4):
            for r in range(p - 1):
                assert pow(a, q * (p - 1) + r, p) == pow(a, r, p)
print("ok")
