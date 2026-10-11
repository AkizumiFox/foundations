"""exm-abs-at-least-x (Ch 1, Section 1.7): |x| >= x by cases on x >= 0 or x < 0; the premises
x >= 0 -> |x| = x and x < 0 -> |x| > x; |x| >= x is (|x| > x) or (|x| = x); neither side holds
for every x (|x| > x fails at 1, |x| = x fails at -1); the instances x = 3 and x = -2."""
from _grid import grid

QUOTED = {"first side fails at": 1, "second side fails at": -1, "case 1 instance": 3,
          "case 2 instance": -2, "case 2 |x|": 2}

for x in grid():
    assert x >= 0 or x < 0
    if x >= 0:
        assert abs(x) == x
    if x < 0:
        assert abs(x) == -x and -x > 0 > x and abs(x) > x
    assert (abs(x) >= x) == (abs(x) > x or abs(x) == x) and abs(x) >= x
x = QUOTED["first side fails at"]
assert not abs(x) > x
x = QUOTED["second side fails at"]
assert not abs(x) == x
x = QUOTED["case 1 instance"]
assert x >= 0 and not abs(x) > x and abs(x) == x
x = QUOTED["case 2 instance"]
assert x < 0 and abs(x) == QUOTED["case 2 |x|"] and abs(x) > x
print("exm-abs-at-least-x: all quoted values check")
