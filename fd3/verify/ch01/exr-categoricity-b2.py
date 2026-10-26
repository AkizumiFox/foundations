"""exr-categoricity-b2: phi(3) = 3 in N_R; 2 * 3 = 6 in N from the recursive equations,
with the intermediate sums 0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6; phi(6) = 6."""
from fractions import Fraction
def S(n): return n + 1
def pred(n): return n - 1
def add(m, n): return m if n == 0 else S(add(m, pred(n)))
def mul(m, n): return 0 if n == 0 else add(mul(m, pred(n)), m)
QUOTED = {"phi3": 3, "prod": 6, "steps": [(0, 2, 2), (2, 2, 4), (4, 2, 6)], "phi6": 6}
def phi(n):      # phi(0) = 0, phi(S(n)) = phi(n) + 1 in N_R (real arithmetic)
    return Fraction(0) if n == 0 else phi(pred(n)) + 1
assert phi(3) == QUOTED["phi3"] == ((0 + 1) + 1) + 1
assert mul(2, 3) == QUOTED["prod"]
assert mul(2, 0) == 0
for a, b, c in QUOTED["steps"]:
    assert add(a, b) == c
assert phi(mul(2, 3)) == QUOTED["phi6"] == phi(2) * phi(3)
print("ok")
