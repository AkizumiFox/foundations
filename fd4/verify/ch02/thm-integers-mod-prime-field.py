"""thm-integers-mod-prime-field: for 2 <= n <= 200, every non-zero class of Z/nZ is a unit
iff n is prime; for composite n the factorization n = rs has 1 < r, s < n and [r][s] = [0].
Remark: 5*[1] = [0] in Z/5Z."""
def isprime(k):
    return k >= 2 and all(k % d for d in range(2, int(k ** 0.5) + 1))
for n in range(2, 201):
    field = all(any(a * x % n == 1 for x in range(n)) for a in range(1, n))
    assert field == isprime(n), n
    if not isprime(n):
        r = next(d for d in range(2, n) if n % d == 0)
        s = n // r
        assert 1 < r < n and 1 < s < n and r * s % n == 0
assert 5 * 1 % 5 == 0
print("ok")
