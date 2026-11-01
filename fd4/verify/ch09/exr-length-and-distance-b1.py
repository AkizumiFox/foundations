"""exr-length-and-distance-b1: (a) e1, e2 equal norms, e1 != +-e2; (b)-(d) true identities on random vectors; (e) e1 ⊥ e2,
d(e1,0) + d(0,e2) = 2 but d(e1,e2) = sqrt 2."""
QUOTED = {"e_counter": "e_1", "d": "\\sqrt 2"}
from fractions import Fraction as Fr
import random

def dot(x, y): return sum(a * b for a, b in zip(x, y))
def add(x, y, s=1): return [a + s * b for a, b in zip(x, y)]
e1, e2 = [1, 0], [0, 1]
assert dot(e1, e1) == dot(e2, e2) == 1 and e1 != e2 and e1 != [0, -1]
assert dot(e1, e2) == 0 and dot(add(e1, e2, -1), add(e1, e2, -1)) == 2 != 2 * 2  # d(e1,e2)^2 = 2, while (1 + 1)^2 = 4
random.seed(3)
for _ in range(2000):
    n = random.randint(2, 5)
    x = [Fr(random.randint(-9, 9)) for _ in range(n)]; y = [Fr(random.randint(-9, 9)) for _ in range(n)]
    p, m = add(x, y), add(x, y, -1)
    assert dot(p, m) == dot(x, x) - dot(y, y)
    if dot(x, y) == 0: assert dot(p, p) == dot(m, m)
    assert dot(p, p) <= 2 * dot(x, x) + 2 * dot(y, y)
print("ok")
