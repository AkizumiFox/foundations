"""Values quoted in exm-statements (Chapter 1, Section 1.1)."""
from fractions import Fraction

QUOTED = {
    "2^11 - 1": 2047,
    "factors of 2047": (23, 89),
    "7 is prime": True,
    "0.999 > 1": False,
    "3 > 2": True,
}


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


a, b = QUOTED["factors of 2047"]
assert 2**11 - 1 == QUOTED["2^11 - 1"]
assert a * b == 2047 and is_prime(a) and is_prime(b)
assert not is_prime(2047)
assert is_prime(7) == QUOTED["7 is prime"]
assert (Fraction(999, 1000) > 1) == QUOTED["0.999 > 1"]
assert (3 > 2) == QUOTED["3 > 2"]
print("exm-statements: all quoted values check")
