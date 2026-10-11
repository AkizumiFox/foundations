"""exr-limit-laws-a1 (e): a_n = 1 + 1/(n+1), b_n = 2, eps = 1/10: M = 2, tolerances 1/40 and 1/60,
least N1 = 0, least N2 = 60, N = 60; at n = 60 the product error is 2/61 < 1/10."""
from fractions import Fraction as Q

QUOTED = {"M": 2, "tol1": Q(1, 40), "tol2": Q(1, 60), "N1": 0, "N2": 60, "N": 60, "err60": Q(2, 61)}
eps = Q(1, 10); a, b = 1, 2
an = lambda k: 1 + Q(1, k + 1)
assert all(abs(an(k)) <= QUOTED["M"] for k in range(1000))
assert eps / (2 * QUOTED["M"]) == QUOTED["tol1"]
assert eps / (2 * (abs(b) + 1)) == QUOTED["tol2"]
works2 = lambda N: all(abs(an(m) - a) < QUOTED["tol2"] for m in range(N, 3000))
assert works2(60) and not works2(59)
assert all(abs(2 - b) < QUOTED["tol1"] for _ in range(1))   # N1 = 0
assert max(QUOTED["N1"], QUOTED["N2"]) == QUOTED["N"]
assert an(60) * 2 - a * b == QUOTED["err60"] < eps
assert all(abs(an(m) * 2 - a * b) < eps for m in range(60, 3000))
print("ok")
