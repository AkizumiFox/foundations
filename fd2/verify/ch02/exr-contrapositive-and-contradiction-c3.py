"""exr-contrapositive-and-contradiction-c3 (F2.2 §04): for 1 <= n <= 8, N = 3 n! - 1 has a prime factor p > n with p % 3 == 2;
every prime factor of N exceeds n and is not 3; (3a+1)(3b+1) = 3(3ab+a+b) + 1."""
from math import factorial
def prime_factors(m):
    out, d = [], 2
    while d * d <= m:
        while m % d == 0:
            out.append(d); m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out
for n in range(1, 9):
    N = 3 * factorial(n) - 1
    assert N >= 2 and N % 3 == 2 and N == 3 * (factorial(n) - 1) + 2
    fs = prime_factors(N)
    assert all(p > n and p != 3 for p in fs)
    assert any(p % 3 == 2 for p in fs)
for a in range(-30, 30):
    for b in range(-30, 30):
        assert (3 * a + 1) * (3 * b + 1) == 3 * (3 * a * b + a + b) + 1
print("exr-contrapositive-and-contradiction-c3: all quoted values check")
