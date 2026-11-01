"""exr-units-and-crt-r1: for composite n = r s with 2 <= r < n, 2^r - 1 divides 2^n - 1
and 3 <= 2^r - 1 < 2^n - 1; 2^n - 1 = (2^r - 1) * sum 2^{rk}; 11 is prime; 2047 = 23 * 89."""
def is_prime(m):
    return m >= 2 and all(m % d for d in range(2, int(m**0.5) + 1))
for n in range(2, 60):
    if not is_prime(n):
        for r in range(2, n):
            if n % r == 0:
                s = n // r
                d = 2**r - 1
                assert 2**n - 1 == d * sum(2**(r*k) for k in range(s))
                assert 3 <= d < 2**n - 1 and (2**n - 1) % d == 0
        assert not is_prime(2**n - 1)
assert is_prime(11) and 11 % 2 == 1 and 11 % 3 == 2
assert 2**11 - 1 == 2047 == 23 * 89 and not is_prime(2047)
print("ok")
