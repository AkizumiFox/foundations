"""exr-comparing-cardinalities-c2: u(x) = x/2 + 1/4 misses 9/10; 2n misses 1."""
from fractions import Fraction as F

QUOTED = {"missed": F(9, 10), "range": (F(1, 4), F(3, 4))}

lo, hi = QUOTED["range"]
assert not (lo <= QUOTED["missed"] <= hi)
# solving u(x) = 9/10 gives x = 13/10, outside [0, 1]
assert (QUOTED["missed"] - F(1, 4)) * 2 == F(13, 10) > 1
assert 1 not in {2 * n for n in range(1000)}
print("ok")
