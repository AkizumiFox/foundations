"""exm-or-hypothesis-split (Ch 1, Section 1.6): the reading "if x >= 0 then x^3 >= 0" splits
into "if x > 0 then x^3 >= 0" and "if x = 0 then x^3 >= 0"; x >= 0 is (x > 0) or (x = 0)."""
from _grid import grid

QUOTED = {"statement": r"if \( x \ge 0 \), then \( x^3 \ge 0 \)"}

for x in grid():
    assert (x >= 0) == (x > 0 or x == 0)
    if x >= 0:
        assert x ** 3 >= 0
    if x > 0:
        assert x ** 3 >= 0
    if x == 0:
        assert x ** 3 >= 0
print("exm-or-hypothesis-split: all quoted values check")
