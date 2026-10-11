from fractions import Fraction as Fr
QUOTED = {}
for r in [Fr(-3), Fr(-1), Fr(0), Fr(1, 2), Fr(2), Fr(7, 3)]:
    for n in range(40):
        assert sum(r ** (k - 1) for k in range(1, n + 1)) == (1 - r ** n) / (1 - r)
assert all(sum(Fr(1) ** (k - 1) for k in range(1, n + 1)) == n for n in range(20))
print("ok")
