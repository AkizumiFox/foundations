"""prp-power-null: |r|^n < 1/(nh), h = 1/|r| - 1, for n >= 1; the Quick check r = 0.9: h = 1/9, bound 9/n,
N = 900, and the remark (0.9)^44 < 0.01."""
from fractions import Fraction as F

QUOTED = {"qc_h": F(1, 9), "qc_C": 9, "qc_N": 900, "qc_small": 44}
for r in [F(9, 10), F(-1, 2), F(1, 3), F(-99, 100), F(1, 1000), F(2, 3)]:
    h = 1 / abs(r) - 1
    assert h > 0 and abs(r) == 1 / (1 + h)
    for n in range(1, 400):
        assert (1 + h) ** n >= 1 + n * h > n * h          # Bernoulli and the strict step
        assert abs(r) ** n < 1 / (n * h)
        assert abs(r ** n) == abs(r) ** n
r = F(9, 10)
h = 1 / r - 1
assert h == QUOTED["qc_h"] and 1 / h == QUOTED["qc_C"]
# 9/n <= 1/100 exactly when n >= 900
for n in range(1, 5000):
    assert (F(QUOTED["qc_C"], n) <= F(1, 100)) == (n >= QUOTED["qc_N"])
for n in range(QUOTED["qc_N"], QUOTED["qc_N"] + 50):
    assert r ** n < F(QUOTED["qc_C"], n) <= F(1, 100)
assert r ** QUOTED["qc_small"] < F(1, 100)
assert r ** (QUOTED["qc_small"] - 1) >= F(1, 100)      # 44 is the least, for the record
print("ok")
