"""exr-disjunction-and-cases-c2 (Ch 1, Section 1.7): the flawed Case 2b; witness x = -3, y = -1;
the repaired Case 2b; the four printed cases (1a, 1b, 2a) are correct."""
from fractions import Fraction as F

QUOTED = {"x": -3, "y": -1, "x - y": -2, "|x - y|": 2, "|x| + |y|": 4}

x, y = QUOTED["x"], QUOTED["y"]
assert x < 0 and y < 0                      # this is Case 2b
assert x - y == QUOTED["x - y"] and not (x - y > 0)
assert abs(x - y) == QUOTED["|x - y|"] != x - y
assert abs(x) + abs(y) == QUOTED["|x| + |y|"] and abs(x - y) <= abs(x) + abs(y)
pts = [F(k, 4) for k in range(-40, 41)]
for a in pts:
    for b in pts:
        assert abs(a - b) <= abs(a) + abs(b)        # the statement is true
        if a >= 0 and b >= 0:                        # Case 1a
            assert a - b <= a <= a + b and b - a <= b <= a + b
        if a >= 0 and b < 0:                         # Case 1b
            assert a - b > 0 and abs(a - b) == a - b == abs(a) + abs(b)
        if a < 0 and b >= 0:                         # Case 2a
            assert a - b < 0 and abs(a - b) == b - a == abs(b) + abs(a)
        if a < 0 and b < 0:                          # repaired Case 2b
            assert a - b < -b == abs(b) and b - a < -a == abs(a)
print("exr-disjunction-and-cases-c2: all quoted values check")
