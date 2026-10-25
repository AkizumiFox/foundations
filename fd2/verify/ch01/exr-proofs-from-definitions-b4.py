"""exr-proofs-from-definitions-b4 (F2.1 §01): verdicts and witnesses for (a)-(f), plus the C3 counts."""
QUOTED = {"b": (2, 1, 1), "e": 6, "f": (2, 1), "j": "2k^2 + 2k"}
from itertools import product, combinations

def div(a, b):
    return b == 0 if a == 0 else b % a == 0

R = range(-12, 13)
# (a) true
assert all(div(a, c) for a, b, c in product(R, R, R) if div(a, b + c) and div(a, b))
# (b) false at a = 2, b = c = 1
assert div(2, 2) and not div(2, 1)
# (c) true; the odd-case algebra
# polynomial identities of degree <= 4 in k (and l), checked at 41 points (41^2 for two variables)
K = range(-20, 21)
for k in K:
    n = 2 * k
    assert n**4 + n**2 + 1 == 2 * (8 * k**4 + 2 * k**2) + 1
    n = 2 * k + 1; j = 2 * k**2 + 2 * k
    assert n**2 == 2 * j + 1 and n**4 + n**2 == n**2 * (n**2 + 1) == (2 * j + 1) * (2 * j + 2) == 2 * (2 * j + 1) * (j + 1)
    assert (2 * k + 1)**2 - 1 == 4 * (k**2 + k)
    for l in K:
        assert (2 * k)**2 + (2 * l + 1)**2 == 4 * k**2 + 4 * l**2 + 4 * l + 1 == 2 * (2 * k**2 + 2 * l**2 + 2 * l) + 1
assert all((m**4 + m**2 + 1) % 2 == 1 for m in range(-60, 61))
# (d) false: 1 + 1 + 1 = 3 odd
assert (1 + 1 + 1) % 2 == 1
# (e) true at n = 6; it is the only n > 5
assert [n for n in range(6, 500) if div(n, n + 6)] == [6]
# (f) false at m = 2, n = 1
assert (2 * 1) % 2 == 0 and 1 % 2 == 1
# B2, B3 algebra
# C3: eight 0/1 points, no lattice midpoint; 2^3 patterns
cube = list(product((0, 1), repeat=3))
assert len(cube) == 8 == 2**3
assert all(any((p[i] + q[i]) % 2 for i in range(3)) for p, q in combinations(cube, 2))
print("exr-proofs-from-definitions-b4: all quoted values check")
