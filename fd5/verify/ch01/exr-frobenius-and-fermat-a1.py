"""exr-frobenius-and-fermat-a1: rows 5 and 6; divisibility by 5 and by 6."""
from math import comb
QUOTED = {"row5": [1, 5, 10, 10, 5, 1], "row6": [1, 6, 15, 20, 15, 6, 1]}
assert [comb(5, k) for k in range(6)] == QUOTED["row5"]
assert [comb(6, k) for k in range(7)] == QUOTED["row6"]
assert [k for k in range(6) if comb(5, k) % 5 == 0] == [1, 2, 3, 4]
assert [k for k in range(7) if comb(6, k) % 6 == 0] == [1, 5]
print("ok")
