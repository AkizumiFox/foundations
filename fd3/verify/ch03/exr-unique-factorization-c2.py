"""exr-unique-factorization-c2: counterexamples to the step and to the claim without coprimality."""
QUOTED = {"x": 4, "c": 2, "no_gcd": (4, 6, 12)}
x, c = QUOTED["x"], QUOTED["c"]
assert (c * c) % x == 0 and c % x != 0 and 0 < c < x
m, n, cc = QUOTED["no_gcd"]
assert cc % m == 0 and cc % n == 0 and cc % (m * n) != 0
print("exr-unique-factorization-c2: ok")
