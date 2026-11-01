"""def-segment-rn: instance before the definition, p = (0,0), q = (2,4); t = 0, 1/2, 1 give (0,0), (1,2), (2,4)."""
from fractions import Fraction as Fr

QUOTED = {0: (0, 0), Fr(1, 2): (1, 2), 1: (2, 4)}
p, q = (0, 0), (2, 4)
for t, pt in QUOTED.items():
    t = Fr(t)
    assert tuple((1 - t) * a + t * b for a, b in zip(p, q)) == pt == (2 * t, 4 * t)
print("ok")
