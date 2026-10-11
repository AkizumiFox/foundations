"""thm-prime-factor (Ch 7, 02): every n >= 2 has a prime factor; 91 = 7 * 13."""
def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, p))
assert 91 == 7 * 13 and is_prime(7) and is_prime(13) and not is_prime(91)
for n in range(2, 2000):
    assert any(n % p == 0 and is_prime(p) for p in range(2, n + 1))
print("thm-prime-factor: all quoted values check")
