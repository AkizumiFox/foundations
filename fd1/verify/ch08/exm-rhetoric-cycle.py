"""exm-rhetoric-cycle (Ch 8, Section 8.1): n odd, n^2 odd, n^2 + 2n odd are equivalent;
the identities n^2 = 2a + 1 => n^2 + 2n = 2(a + n) + 1 and (2k)^2 + 2(2k) = 2(2k^2 + 2k)."""
from itertools import product


def identity(f, nvars):
    """A polynomial identity of low degree, checked on a grid of integer points."""
    return all(f(*v) == 0 for v in product(range(-7, 8), repeat=nvars))

RANGE = 200  # test range, not quoted in the text

# (ii) => (iii): substitute n^2 = 2a + 1
assert identity(lambda a, n: (2 * a + 1 + 2 * n) - (2 * (a + n) + 1), 2)
# (iii) => (i), even case
assert identity(lambda k: (2 * k) ** 2 + 2 * (2 * k) - 2 * (2 * k ** 2 + 2 * k), 1)
# the three conditions agree on |n| <= 200
for m in range(-RANGE, RANGE + 1):
    c1 = m % 2 == 1
    c2 = (m * m) % 2 == 1
    c3 = (m * m + 2 * m) % 2 == 1
    assert c1 == c2 == c3
print("exm-rhetoric-cycle: all quoted values check")
