"""exr-frobenius-and-fermat-c2: induction (r.1)^p = r.1 in F_p for r < 3p; [a]^n = [a^n] and
[a]^p = [a] (so p | a^p - a) for every integer a, negative ones included."""
QUOTED = {"primes": (2, 3, 5, 7, 11, 13)}
for p in QUOTED["primes"]:
    for r in range(3 * p):
        assert pow(r % p, p, p) == r % p
    for a in range(-40, 41):
        for n in range(6):
            assert pow(a % p, n, p) == (a ** n) % p
        assert pow(a % p, p, p) == a % p and (a ** p - a) % p == 0
print("ok")
