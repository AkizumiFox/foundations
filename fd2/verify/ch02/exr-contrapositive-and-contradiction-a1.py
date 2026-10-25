"""exr-contrapositive-and-contradiction-a1 (F2.2 §04): (a) 9 = 3 * 3 odd, not prime; even n >= 3 not prime;
(b)(ii) a, b odd => a^2 + b^2 even; (c) 6! + 1 = 721 = 7 * 103, remainders 1 mod 2, 3, 5."""
from math import factorial
def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, p))
assert 9 % 2 == 1 and not is_prime(9)
assert all(not is_prime(n) for n in range(4, 2000, 2))
assert all(n % 2 == 1 for n in range(3, 2000) if is_prime(n))
for a in range(-41, 41, 2):
    for b in range(-41, 41, 2):
        assert (a * a + b * b) % 2 == 0
N = factorial(6) + 1
assert N == 721 and N % 2 == 1 and N % 3 == 1 and N % 5 == 1 and N == 7 * 103 and is_prime(103)
print("exr-contrapositive-and-contradiction-a1: all quoted values check")
