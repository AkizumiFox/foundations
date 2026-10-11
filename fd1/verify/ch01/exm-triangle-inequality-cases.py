"""exm-triangle-inequality-cases (Ch 1, Section 1.7): a <= |a|, -a <= |a|; the two cases on the
sign of x + y; the warning's witness x = 1, y = -1 (0 <= 2, strict)."""
from fractions import Fraction as F

QUOTED = {"witness x": 1, "witness y": -1, "|x+y| at witness": 0, "|x|+|y| at witness": 2}

pts = sorted({F(k, 4) for k in range(-40, 41)})
for a in pts:
    assert a <= abs(a) and -a <= abs(a)
for x in pts:
    for y in pts:
        s = x + y
        if s >= 0:
            assert abs(s) == s <= abs(x) + abs(y)
        else:
            assert abs(s) == -x - y <= abs(x) + abs(y)
x, y = QUOTED["witness x"], QUOTED["witness y"]
# the witness satisfies neither "both >= 0" nor "both < 0"
assert not (x >= 0 and y >= 0) and not (x < 0 and y < 0)
assert abs(x + y) == QUOTED["|x+y| at witness"] and abs(x) + abs(y) == QUOTED["|x|+|y| at witness"]
assert abs(x + y) < abs(x) + abs(y)
print("exm-triangle-inequality-cases: all quoted values check")
