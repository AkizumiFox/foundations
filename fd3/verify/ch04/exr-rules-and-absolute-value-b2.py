"""exr-rules-and-absolute-value-b2: |2x - 3| < 5 iff -1 < x < 4; the numerals used."""
from fractions import Fraction as Fr

QUOTED = {"interval": (-1, 4), "shifted": (-2, 8), "numerals": {"5+3": 8, "2+3": 5, "4+4": 8}}
assert 5 + 3 == QUOTED["numerals"]["5+3"] and 2 + 3 == QUOTED["numerals"]["2+3"] and 4 + 4 == QUOTED["numerals"]["4+4"]
assert (-5 + 3, 5 + 3) == QUOTED["shifted"]
assert (Fr(-2, 2), Fr(8, 2)) == QUOTED["interval"]
for k in range(-400, 401):
    x = Fr(k, 40)
    assert (abs(2 * x - 3) < 5) == (-1 < x < 4)
assert abs(2 * 4 - 3) == 5
print("ok")
