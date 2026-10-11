"""thm-rationals-dense-ordered-field: the construction of the proof, run in F = Q on sample pairs x < y."""
from fractions import Fraction as Fr
import math, itertools

QUOTED = {}
vals = [Fr(-7, 3), Fr(-1, 5), Fr(0), Fr(1, 3), Fr(1, 2), Fr(100, 301), Fr(101, 301), Fr(4)]
for x, y in itertools.product(vals, repeat=2):
    if x < y:
        n = min(n for n in range(1, 10 ** 6) if Fr(1, n) < y - x)
        m = math.floor(n * x)
        q = Fr(m + 1, n)
        assert x < q < y
print("ok")
