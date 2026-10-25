"""thm-primes-infinite (F2.2 §04): for n <= 12 every prime factor of n! + 1 exceeds n;
k | n! for 1 <= k <= n; 4! + 1 = 25 = 5 * 5; 5! + 1 = 121 = 11 * 11; 6! + 1 = 721 = 7 * 103 (A1 (c))."""
from math import factorial
def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))
def prime_factors(m):
    out, d = [], 2
    while d * d <= m:
        while m % d == 0:
            out.append(d); m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out
for n in range(0, 13):
    f = factorial(n)
    assert f >= 1 and all(f % k == 0 for k in range(1, n + 1))
    N = f + 1
    assert N >= 2
    assert all(is_prime(p) and p > n for p in prime_factors(N)), n
assert 25 == 5 * 5 and factorial(4) + 1 == 25
assert factorial(5) + 1 == 121 == 11 * 11 and is_prime(11)
assert factorial(6) + 1 == 721 == 7 * 103 and is_prime(103) and min(prime_factors(721)) == 7
assert 721 == 2 * 360 + 1 == 3 * 240 + 1 == 5 * 144 + 1
print("thm-primes-infinite: all quoted values check")
