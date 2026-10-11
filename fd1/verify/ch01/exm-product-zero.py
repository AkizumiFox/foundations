"""exm-product-zero (Ch 1, Section 1.6): the school fact "a = 0 or b = 0 implies a*b = 0" and
the derived "a = 0 implies a*b = 0"; x > 0 gives (x > 0) or (x = 0), which is x >= 0."""
from _grid import grid

QUOTED = {"fact": r"if \( a = 0 \) or \( b = 0 \), then \( a \cdot b = 0 \)"}

pts = grid(-3, 3, 4)
for a in pts:
    for b in pts:
        if a == 0 or b == 0:
            assert a * b == 0
        if a == 0:
            assert a * b == 0
for x in grid():
    if x > 0:
        assert (x > 0 or x == 0) and x >= 0
print("exm-product-zero: all quoted values check")
