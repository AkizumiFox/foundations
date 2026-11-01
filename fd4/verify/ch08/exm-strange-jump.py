"""exm-strange-jump: H(x) = x (x < 0), x + 1 (x >= 0); strictly increasing; 1/2 not a value;
H(-1) = -1, H(0) = 1; H^{-1}(v) = v (v < 0), v - 1 (v >= 1)."""
from fractions import Fraction as F
import random

H = lambda x: x if x < 0 else x + 1
Hinv = lambda v: v if v < 0 else v - 1
QUOTED = {"H(-1)": -1, "H(0)": 1}
assert H(-1) == QUOTED["H(-1)"] and H(0) == QUOTED["H(0)"]
random.seed(4)
pts = sorted({F(random.randint(-400, 400), random.randint(1, 40)) for _ in range(2000)})
for a, b in zip(pts, pts[1:]):
    assert H(a) < H(b)
for x in pts:
    v = H(x)
    assert v < 0 or v >= 1
    assert v != F(1, 2)
    assert Hinv(v) == x
print("ok")
