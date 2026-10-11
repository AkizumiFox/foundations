"""exr-disjunction-introduction-a1 (Ch 1, Section 1.6): the facts behind the sentences of (b):
x < 3 gives x <= 3 = (x < 3 or x = 3); |x - 2| < 1 implies 1 < x < 3; 0 < x < 1 gives x < 1."""
from _grid import grid

QUOTED = {"(b) fourth sentence": r"\abs{x - 2} < 1 \) implies \( 1 < x < 3"}

for x in grid():
    assert (x <= 3) == (x < 3 or x == 3)
    if abs(x - 2) < 1:
        assert 1 < x < 3
    if 0 < x < 1:
        assert x < 1
print("exr-disjunction-introduction-a1: all quoted values check")
