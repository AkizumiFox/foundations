"""exr-levels-of-abbreviation-b3 (Section 8.3): |x - 1| + |x + 1| >= 2 for every real x
(on a grid, and by the three-case route); |x - 1| = |1 - x|, (1 - x) + (x + 1) = 2; the
student's row "|x - 1| >= 1 and |x + 1| >= 1" fails exactly when 0 < |x| < 2, e.g. at
x = 1/2, where the goal holds (1/2 + 3/2 = 2)."""
from fractions import Fraction as Fr

QUOTED = {"x": Fr(1, 2), "values": (Fr(1, 2), Fr(3, 2))}
for x in [Fr(a, 40) for a in range(-400, 401)]:
    assert abs(x - 1) + abs(x + 1) >= 2
    assert abs(x - 1) == abs(1 - x) and (1 - x) + (x + 1) == 2
    assert abs(1 - x) + abs(x + 1) >= abs((1 - x) + (x + 1))
    # three cases
    if x <= -1:
        assert abs(x - 1) + abs(x + 1) == -2 * x >= 2
    elif x < 1:
        assert abs(x - 1) + abs(x + 1) == 2
    else:
        assert abs(x - 1) + abs(x + 1) == 2 * x >= 2
    row = abs(x - 1) >= 1 and abs(x + 1) >= 1
    assert row == (not (0 < abs(x) < 2)), x
x = QUOTED["x"]
assert (abs(x - 1), abs(x + 1)) == QUOTED["values"] and sum(QUOTED["values"]) == 2
assert not (abs(x - 1) >= 1)
print("exr-levels-of-abbreviation-b3: all quoted values check")
