"""exr-the-uniqueness-theorem-c2: counterexample to line (2): x = 0, y = 2, q = 1 has
q < x + y but not q/2 < x. Also checks the repair split of lem-cof-below-sum exists
(r = -1/2: r < x and q - r = 3/2 < y)."""
from fractions import Fraction as F
QUOTED = {"x": F(0), "y": F(2), "q": F(1)}
x, y, q = QUOTED["x"], QUOTED["y"], QUOTED["q"]
assert q < x + y
assert not (q / 2 < x)
r = F(-1, 2)
assert r < x and q - r < y and r + (q - r) == q
print("ok")
