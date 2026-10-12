"""exm-chains-about-numbers (Section 1.3): the premises of (a) are true for every integer,
the premises of (b) for all real x, y (premise 6 included), and the derivations' last lines
follow; the read-back of (a): 6 | n implies 36 | n^2."""
import sys, pathlib, itertools
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid

QUOTED = {"(b) bound in premise 5": 2, "(b) bound in premise 6": 2}
RANGE = (-60, 60)     # integers checked for (a); not quoted in the text


def d(a, b):
    return b % a == 0


lo, hi = RANGE
for n in range(lo, hi + 1):
    assert (not d(6, n)) or (d(2, n) and d(3, n))           # premise 2
    assert (not d(2, n)) or d(4, n * n)                      # premise 3
    assert (not d(3, n)) or d(9, n * n)                      # premise 4
    assert (not d(6, n)) or d(36, n * n)                     # read-back
for m in range(-5000, 5001):
    assert (not (d(4, m) and d(9, m))) or d(36, m)           # premise 5 (for m = n^2 and more)
# witnesses for the divisions quoted: 6k = 2(3k) = 3(2k); (2k)^2 = 4k^2; (3k)^2 = 9k^2
for k in range(-30, 31):
    assert 6 * k == 2 * (3 * k) == 3 * (2 * k) and (2 * k) ** 2 == 4 * k * k and (3 * k) ** 2 == 9 * k * k

# (b), on a rational grid in x and y (pairs from a coarser grid)
pts = [p for p in grid(-6, 6, 4)]
b5, b6 = QUOTED["(b) bound in premise 5"], QUOTED["(b) bound in premise 6"]
for x in grid():
    assert (not x > 1) or x * x > 1                          # premises 3, 4
for x, y in itertools.product(pts, pts):
    assert (not (x * x > 1 and y * y > 1)) or x * x + y * y > b5     # premise 5
    assert (not x > 2) or x * x + y * y > b6                          # premise 6
    assert y * y >= 0
print("exm-chains-about-numbers: checks")
