"""exr-connective-rhetoric-b4 (Ch 8, Section 8.1): a + b even, a - b even, same parity are
equivalent; the identities of the solution."""
from itertools import product


def identity(f, nvars):
    """A polynomial identity of low degree, checked on a grid of integer points."""
    return all(f(*v) == 0 for v in product(range(-7, 8), repeat=nvars))

RANGE = 60  # test range, not quoted in the text

# (i) => (ii): a + b = 2k gives a - b = 2(k - b)
assert identity(lambda k, b: (2 * k - b - b) - 2 * (k - b), 2)
# (ii) => (iii): a - b = 2j, b = 2m gives a = 2(j + m); b = 2m + 1 gives a = 2(j + m) + 1
assert identity(lambda j, m: (2 * j + 2 * m) - 2 * (j + m), 2)
assert identity(lambda j, m: (2 * j + 2 * m + 1) - (2 * (j + m) + 1), 2)
# (iii) => (i)
assert identity(lambda s, t: (2 * s + 2 * t) - 2 * (s + t), 2)
assert identity(lambda s, t: (2 * s + 1 + 2 * t + 1) - 2 * (s + t + 1), 2)
R = RANGE
for x in range(-R, R + 1):
    for y in range(-R, R + 1):
        c1 = (x + y) % 2 == 0
        c2 = (x - y) % 2 == 0
        c3 = (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1)
        assert c1 == c2 == c3
print("exr-connective-rhetoric-b4: all quoted values check")
