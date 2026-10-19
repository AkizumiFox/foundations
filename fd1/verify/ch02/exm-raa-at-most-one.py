"""exm-raa-at-most-one (Ch 2 s05): x^2 <= x implies x <= 1 (exactly on [0, 1]); x > 1 gives
x > 0 and x^2 > x; and the x^3 comparison of "Not-I or RAA?": x >= 0 implies x^3 >= 0, so
x^3 < 0 implies x < 0."""
import sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

QUOTED = {"bound": 1}
grid = [Fraction(k, 64) for k in range(-640, 641)]
for x in grid:
    if x * x <= x:
        assert x <= QUOTED["bound"]
        assert 0 <= x <= 1                      # x^2 <= x holds exactly on [0, 1]
    if 0 <= x <= 1:
        assert x * x <= x
    if x > 1:
        assert x > 0 and x * x > x and x * x - x == x * (x - 1)
    if x >= 0:
        assert x ** 3 >= 0
    if x ** 3 < 0:
        assert x < 0
print("exm-raa-at-most-one: ok")
