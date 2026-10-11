"""School-algebra facts quoted in Section 1.4 (04-using-an-implication) around
def-rule-implication-elimination: the sqrt(2) < 1.5 < 2 instance, the affirming-the-consequent
witnesses, the x > 2 chain, and the f(x) = x on (0, 1) warning."""
import sys, pathlib
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {"1.5": Fraction(3, 2), "1.5^2": Fraction(9, 4), "warning x": -3, "n": 2}
h = QUOTED["1.5"]
assert h * h == QUOTED["1.5^2"] and h * h > 2 and h < 2   # sqrt 2 < 1.5 < 2
# affirming the consequent, integers: 4 | n -> n even holds; n = 2 even, not divisible by 4
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
# f(x) = x on (0, 1): (a + 1)/2 lies in (0, 1) and exceeds a
for k in range(1, 1000):
    a = Fraction(k, 1000)
    b = (a + 1) / 2
    assert 0 < b < 1 and b > a
print("def-rule-implication-elimination: checks")
