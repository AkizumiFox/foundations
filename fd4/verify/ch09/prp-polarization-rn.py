"""prp-polarization-rn (same checks as prp-parallelogram-law-rn, keyed to the polarization block): eq-expand-norm-squared, prp-pythagoras-rn, prp-parallelogram-law-rn, prp-polarization-rn: exact checks on random rational vectors
in R^n, n = 1..6, and Pythagoras' equivalence on orthogonal and non-orthogonal pairs."""
QUOTED = {"quarter": "\\frac14", "a": "4\\inner{x}{y}"}
from fractions import Fraction as Fr
import random

def dot(x, y): return sum(a * b for a, b in zip(x, y))
def add(x, y, s=1): return [a + s * b for a, b in zip(x, y)]
random.seed(7)
for _ in range(3000):
    n = random.randint(1, 6)
    x = [Fr(random.randint(-9, 9), random.randint(1, 5)) for _ in range(n)]
    y = [Fr(random.randint(-9, 9), random.randint(1, 5)) for _ in range(n)]
    p, m = add(x, y), add(x, y, -1)
    assert dot(p, p) == dot(x, x) + 2 * dot(x, y) + dot(y, y)
    assert dot(m, m) == dot(x, x) - 2 * dot(x, y) + dot(y, y)
    assert dot(p, p) + dot(m, m) == 2 * dot(x, x) + 2 * dot(y, y)
    assert dot(x, y) == Fr(1, 4) * (dot(p, p) - dot(m, m))
    assert 2 * dot(x, y) == dot(x, x) + dot(y, y) - dot(m, m)
    assert (dot(p, p) == dot(x, x) + dot(y, y)) == (dot(x, y) == 0) == (dot(m, m) == dot(x, x) + dot(y, y))
# an orthogonal pair, so the "iff" is tested on both sides
x, y = [1, 2, 0], [-2, 1, 5]; assert dot(x, y) == 0 and dot(add(x, y), add(x, y)) == dot(x, x) + dot(y, y)
print("ok")
