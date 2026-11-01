"""exr-...-b3 (03): sum k/100 (k = 1..10) = 55/100, product >= 0.45."""
from fractions import Fraction as Fr
QUOTED = {"sum": Fr(55, 100), "bound": Fr(45, 100)}
a = [Fr(k, 100) for k in range(1, 11)]
assert sum(range(1, 11)) == 55 and sum(a) == QUOTED["sum"] and 1 - sum(a) == QUOTED["bound"]
p = Fr(1)
for x in a:
    p *= 1 - x
assert p >= QUOTED["bound"], float(p)
print("ok", float(p))
