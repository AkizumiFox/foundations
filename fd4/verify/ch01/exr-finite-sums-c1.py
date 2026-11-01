"""exr-finite-sums-c1: F(k) = k^2(k+1)^2/4, F(0) = 0, F(k) - F(k-1) = (k^2/4)((k+1)^2 - (k-1)^2) = k^3; sum of cubes = (n(n+1)/2)^2; check n = 3: 36 = 6^2; marking scheme points sum to 10."""
from fractions import Fraction as Fr
QUOTED = {"check": (1, 8, 27, 36, 6), "points": (4, 3, 3)}
F = lambda x: Fr(x) ** 2 * (Fr(x) + 1) ** 2 / 4
# degree-4 identities checked at 50 points, so exact
for x in map(Fr, range(-25, 25)):
    assert F(x) - F(x - 1) == x ** 3 == x ** 2 / 4 * ((x + 1) ** 2 - (x - 1) ** 2)
assert F(0) == 0
for n in range(0, 150):
    assert sum(j ** 3 for j in range(0, n + 1)) == Fr(n * (n + 1), 2) ** 2 == Fr(F(n))
c = QUOTED["check"]
assert (1, 8, 27) == c[:3] and sum(c[:3]) == c[3] == c[4] ** 2 == (3 * 4 // 2) ** 2
assert sum(QUOTED["points"]) == 10
print("ok")
