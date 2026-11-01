"""exm-telescoping-squares: (k+1)^3 - k^3 = 3k^2 + 3k + 1; (n+1)^3 - 1 = 3 sum k^2 + 3n(n+1)/2 + n; 3 sum k^2 = (n+1)(n^2 + 2n - 3n/2) = n(n+1)(2n+1)/2; sum k^2 = n(n+1)(2n+1)/6; check n = 3: 14."""
from fractions import Fraction as Fr
QUOTED = {"check_n": 3, "check_value": 14}
# polynomial identities of degree <= 3, checked at 50 points (more than the degree), so exact
for x in map(Fr, range(-25, 25)):
    assert (x + 1) ** 3 - x ** 3 == 3 * x ** 2 + 3 * x + 1
    lhs = (x + 1) ** 3 - (x + 1) - Fr(3, 2) * x * (x + 1)
    mid = (x + 1) * (x ** 2 + 2 * x - Fr(3, 2) * x)
    assert lhs == mid == x * (x + 1) * (2 * x + 1) / 2
for N in range(0, 100):
    s2 = sum(j * j for j in range(1, N + 1))
    assert (N + 1) ** 3 - 1 == 3 * s2 + Fr(3 * N * (N + 1), 2) + N
    assert s2 == Fr(N * (N + 1) * (2 * N + 1), 6)
N = QUOTED["check_n"]
assert sum(j * j for j in range(1, N + 1)) == QUOTED["check_value"] == Fr(3 * 4 * 7, 6)
print("ok")
