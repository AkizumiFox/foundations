"""exr-finite-sets-r1 (F2.2 §05): g(a, b) = 2a + 3b has g(-n, n) = n and g(0, 0) = g(3, -2) = 0;
k(n) = 3n + 1 is injective and never 0 (checked for |n| <= 1000)."""
QUOTED = {"collision": (3, -2), "missed_value": 0, "modulus": 3}
g = lambda a, b: 2 * a + 3 * b
k = lambda n: 3 * n + 1
R = range(-1000, 1001)
assert all(g(-n, n) == n for n in R)
assert g(0, 0) == 0 == g(3, -2)
assert len({k(n) for n in R}) == len(R) and all(k(n) != 0 for n in R)
assert all(k(n) % 3 == 1 for n in R)
print("exr-finite-sets-r1: all quoted values check")
