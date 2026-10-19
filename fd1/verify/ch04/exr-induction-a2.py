"""exr-induction-a2 (Ch 4, Section 4.2): the drill's numbers and identities."""
from math import factorial

QUOTED = {"(e)": (24, 16), "(g) n": 41, "(h)": "even"}


def is_prime(m):
    return m >= 2 and all(m % d for d in range(2, int(m ** 0.5) + 1))


for n in range(0, 300):
    assert (n + 1) ** 2 + (n + 1) == (n * n + n) + 2 * (n + 1)                       # (b)
    assert (n + 1) ** 3 + 2 * (n + 1) == (n ** 3 + 2 * n) + 3 * (n * n + n + 1)       # (k)
    assert (n ** 3 + 2 * n) % 3 == 0
for n in range(1, 100):
    assert sum(range(1, 2 * n, 2)) == n * n and sum(range(1, 2 * n + 2, 2)) == (n + 1) ** 2  # (d)
assert factorial(4) == 24 >= 16 == 2 ** 4                                             # (e)
assert all(factorial(n) >= 2 ** n for n in range(4, 60)) and factorial(3) < 2 ** 3
assert all(is_prime(n * n - n + 41) for n in range(0, 41))                            # (g)
assert 41 * 41 - 41 + 41 == 41 ** 2 and not is_prime(41 ** 2)
print("exr-induction-a2: all quoted values check")
