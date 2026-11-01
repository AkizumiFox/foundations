"""exr-units-and-crt-c2: in Z/6Z, [2][1] = [2] = [8] = [2][4] with [1] != [4]; for primes p,
a != 0 mod p, x -> ax is injective (cancellation) on Z/pZ."""
def isprime(k):
    return k >= 2 and all(k % d for d in range(2, int(k ** 0.5) + 1))
def primerange(lo, hi):
    return [k for k in range(lo, hi) if isprime(k)]
assert 2 * 1 % 6 == 2 * 4 % 6 == 2 and 8 % 6 == 2 and 1 % 6 != 4 % 6
for p in primerange(2, 100):
    for a in range(1, p):
        assert len({a * x % p for x in range(p)}) == p
print("ok")
