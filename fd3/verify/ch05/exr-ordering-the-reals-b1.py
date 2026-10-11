"""exr-ordering-the-reals-b1: (7/5)^2 = 49/25 < 2, so x_n - 1 > 2/5 for the Newton sequence;
margins: a: 1/2 (N = 1), b: 2/5 (N = 0); sum 9/10, product 1/5, threshold 1."""
from fractions import Fraction as F
QUOTED = {"sq": F(49, 25), "db": F(2, 5), "da": F(1, 2), "sum": F(9, 10), "prod": F(1, 5), "N": 1}
assert F(7, 5) ** 2 == QUOTED["sq"] < 2
x = [F(2)]
for _ in range(6):
    x.append(x[-1] / 2 + 1 / x[-1])
assert all(t - 1 > QUOTED["db"] for t in x)
assert QUOTED["da"] + QUOTED["db"] == QUOTED["sum"] and QUOTED["da"] * QUOTED["db"] == QUOTED["prod"]
assert max(1, 0) == QUOTED["N"]
a = lambda n: 1 - F(1, n + 1)
for n in range(1, 7):
    assert a(n) + (x[n] - 1) >= QUOTED["sum"] and a(n) * (x[n] - 1) >= QUOTED["prod"]
print("ok")
