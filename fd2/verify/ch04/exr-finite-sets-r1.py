"""exr-finite-sets-r1 (F2.2 §05): g(a, b) = 4a + 6b is even-valued (so 1 is missed) and has
g(3, -2) = g(0, 0) = 0; k(n) = 3n + 1 is injective and never 0 (checked for |n| <= 1000)."""
QUOTED = {"collision": (3, -2), "missed_value_g": 1, "missed_value_k": 0, "modulus": 3}
g = lambda a, b: 4 * a + 6 * b
k = lambda n: 3 * n + 1
R = range(-200, 201)
assert all(g(a, b) == 2 * (2 * a + 3 * b) and g(a, b) % 2 == 0 for a in R for b in R)
assert all(g(a, b) != 1 for a in R for b in R)
assert g(3, -2) == 0 == g(0, 0) and 1 == 2 * 0 + 1
R = range(-1000, 1001)
assert len({k(n) for n in R}) == len(R) and all(k(n) != 0 for n in R)
assert all(k(n) % 3 == 1 for n in R)
print("exr-finite-sets-r1: all quoted values check")
