"""exr-checking-proofs-b3 (Section 8.6): (i) odd times odd is odd, (2k+1)(2l+1) = 2(2kl+k+l)+1;
(ii) a^2 = b^2 implies a = b or a = -b; (iii) m = n = 0 gives m^2 + n^2 = 0; (iv) every n in
[2, 500] is a product of primes; (v) 1 + 1 + 1 = 3 != 0 and x^2 + x + 1 = (x + 1/2)^2 + 3/4 > 0."""
from fractions import Fraction as F
QUOTED = {"iii": (0, 0), "v": 3}
for k in range(-60, 61):
    for l in range(-60, 61):
        assert (2 * k + 1) * (2 * l + 1) == 2 * (2 * k * l + k + l) + 1
for i in range(-40, 41):
    for j in range(-40, 41):
        a, b = F(i, 3), F(j, 3)
        if a * a == b * b:
            assert a == b or a == -b
        assert (a - b) * (a + b) == a * a - b * b
m, n = QUOTED["iii"]
assert m * m + n * n == 0 < 1
def is_prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))
def factor(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0:
            out.append(d); n //= d
        d += 1
    return out
for n in range(2, 501):
    fs = factor(n)
    assert all(is_prime(p) for p in fs)
    prod = 1
    for p in fs:
        prod *= p
    assert prod == n
assert 1 + 1 + 1 == QUOTED["v"] != 0
for k in range(-500, 501):
    x = F(k, 37)
    assert x * x + x + 1 == (x + F(1, 2)) ** 2 + F(3, 4) > 0
    assert x ** 3 - 1 == (x - 1) * (x * x + x + 1)
print("exr-checking-proofs-b3: all quoted values check")
