"""exr-units-and-crt-b1: for primes p < 200, a^2 = 1 mod p only for a = +-1; in Z/8Z
[3]^2 = [9] = [1], 3 != 1, 3 != -1 (mod 8; 4 not divisible by 8); all four units square to 1."""
def isprime(k):
    return k >= 2 and all(k % d for d in range(2, int(k ** 0.5) + 1))
def primerange(lo, hi):
    return [k for k in range(lo, hi) if isprime(k)]
for p in primerange(2, 200):
    assert {a for a in range(p) if a * a % p == 1} == {1 % p, (-1) % p}
assert 9 % 8 == 1 and (3 - 1) % 8 != 0 and (3 + 1) % 8 != 0
assert all(a * a % 8 == 1 for a in (1, 3, 5, 7))
print("ok")
