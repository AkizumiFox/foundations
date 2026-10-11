"""School facts quoted in Section 1.3 (04-using-an-implication) around
def-rule-implication-elimination: the 42 example (2 | 42, 3 | 42, 6 | 42 and the theorem
"divisible by 2 and by 3 implies divisible by 6"), the 72 Quick check, the n = 2 witness of
affirming the consequent, the x = -3 warning, the x > 2 chain, the whole-hypothesis warning
at x = 1, y = -1, and the f(x) = x on (0, 1) fold."""
import sys, pathlib
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {
    "42 = 2 *": 21, "42 = 3 *": 14, "42 = 6 *": 7,
    "72 = 4 *": 18, "72 = 9 *": 8, "72 = 36 *": 2,
    "warning x": -3, "n": 2, "whole-hypothesis x": 1, "whole-hypothesis y": -1,
}

def divides(d, n):
    return n % d == 0

# the 42 example
assert 2 * QUOTED["42 = 2 *"] == 42 and 3 * QUOTED["42 = 3 *"] == 42 and 6 * QUOTED["42 = 6 *"] == 42
# the theorem: divisible by 2 and by 3 implies divisible by 6 (checked on a range of integers)
assert all(divides(6, n) for n in range(-10000, 10001) if divides(2, n) and divides(3, n))
# the Quick check: 4 | n and 9 | n implies 36 | n; 72 = 4*18 = 9*8 = 36*2
assert 4 * QUOTED["72 = 4 *"] == 72 and 9 * QUOTED["72 = 9 *"] == 72 and 36 * QUOTED["72 = 36 *"] == 72
assert all(divides(36, n) for n in range(-10000, 10001) if divides(4, n) and divides(9, n))
# affirming the consequent: 4 | n -> n even holds; n = 2 even, not divisible by 4
n = QUOTED["n"]
assert all(m % 2 == 0 for m in range(-100, 101) if m % 4 == 0)
assert n % 2 == 0 and n % 4 != 0
# reals: x > 2 -> x^2 > 4 for every x, and at x = -3 the conclusion holds and the hypothesis fails
assert implies_on_grid(lambda x: x > 2, lambda x: x**2 > 4)
x0 = QUOTED["warning x"]
assert x0**2 == 9 and x0**2 > 4 and not x0 > 2
# the chain x > 2 -> x^2 > 4 -> x^2 + 1 > 5
assert implies_on_grid(lambda x: x**2 > 4, lambda x: x**2 + 1 > 5)
assert implies_on_grid(lambda x: x > 2, lambda x: x**2 > 2 * x and 2 * x > 4)
# whole-hypothesis warning: (x > 0 and y > 0) -> xy > 0 on a grid; at (1, -1) x > 0, xy > 0 fails
G = list(grid())
assert all(x * y > 0 for x in G[::7] for y in G[::7] if x > 0 and y > 0)
x, y = QUOTED["whole-hypothesis x"], QUOTED["whole-hypothesis y"]
assert x > 0 and not x * y > 0
# f(x) = x on (0, 1): (a + 1)/2 lies in (0, 1) and exceeds a
for k in range(1, 1000):
    a = Fraction(k, 1000)
    b = (a + 1) / 2
    assert 0 < b < 1 and b > a
print("def-rule-implication-elimination: checks")
