"""exr-strange-functions-a2: 1/2 < sqrt(2)/2 < 3/4 via squares, and the values of x D(x)."""
from fractions import Fraction as Fr
import math

QUOTED = {"squares": (Fr(1, 4), Fr(1, 2), Fr(9, 16)), "values": (Fr(1, 2), 0, Fr(3, 4))}
a, m, b = QUOTED["squares"]
assert Fr(1, 2) ** 2 == a and Fr(3, 4) ** 2 == b and m == Fr(2, 4)
assert a < m < b
assert 0.5 < math.sqrt(2) / 2 < 0.75
assert QUOTED["values"] == (Fr(1, 2) * 1, 0, Fr(3, 4) * 1)
print("exr-strange-functions-a2: all checks passed")
