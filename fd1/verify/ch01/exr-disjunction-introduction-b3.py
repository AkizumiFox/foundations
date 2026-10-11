"""exr-disjunction-introduction-b3 (Ch 1, Section 1.6): the school fact x >= 1 -> x^2 >= x,
the derived x > 1 -> x^2 >= x, x >= 1 written as (x > 1) or (x = 1); at x = 3, 9 >= 3."""
from _grid import grid

QUOTED = {"x": 3, "x^2": 9}

for x in grid():
    assert (x >= 1) == (x > 1 or x == 1)
    if x >= 1:
        assert x * x >= x
    if x > 1:
        assert x * x >= x
x = QUOTED["x"]
assert x * x == QUOTED["x^2"] and x * x >= x
print("exr-disjunction-introduction-b3: all quoted values check")
