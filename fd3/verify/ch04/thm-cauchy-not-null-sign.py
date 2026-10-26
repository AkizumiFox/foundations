"""thm-cauchy-not-null-sign, Quick check: a_n = (n - 3)/(n + 1) = 1 - 4/(n + 1) in Q;
c = 1/2 with N = 7 (least for this c, since a_6 = 3/7 < 1/2); c = 1/5 with N = 4 (a_4 = 1/5)."""
from fractions import Fraction as F

QUOTED = {"c": F(1, 2), "N": 7, "a6": F(3, 7), "c_alt": F(1, 5), "N_alt": 4, "a4": F(1, 5)}

# (n - 3)/(n + 1) = 1 - 4/(n + 1): (n + 1) - 4 = n - 3, checked exactly on many n
assert all(F(k - 3, k + 1) == 1 - F(4, k + 1) for k in range(0, 5000))

a = lambda k: F(k - 3, k + 1)
# a_n is increasing, so a_n >= a_N for n >= N; check a long stretch too
assert all(a(k + 1) > a(k) for k in range(0, 5000))
for c, N in [(QUOTED["c"], QUOTED["N"]), (QUOTED["c_alt"], QUOTED["N_alt"])]:
    assert all(a(k) >= c for k in range(N, 5000))
    assert a(N - 1) < c  # N is least for this c
assert a(6) == QUOTED["a6"] and a(6) < QUOTED["c"]
assert a(4) == QUOTED["a4"]
# n + 1 >= 8 gives 4/(n + 1) <= 1/2
assert all(F(4, k + 1) <= F(1, 2) for k in range(7, 2000))
print("ok")
