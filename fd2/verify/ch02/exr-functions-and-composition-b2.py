"""exr-functions-and-composition-b2 (Section 2.1): s o s = doubling; t o s = s o t = id."""
from fractions import Fraction as F

QUOTED = {"t": ("u + v", "u - v")}

s = lambda p: (p[0] + p[1], p[0] - p[1])
t = lambda p: ((p[0] + p[1]) / F(2), (p[0] - p[1]) / F(2))
pts = [(F(i, 3), F(j, 4)) for i in range(-15, 16) for j in range(-15, 16)]
assert all(s(s(p)) == (2 * p[0], 2 * p[1]) for p in pts)
assert all(t(s(p)) == p and s(t(p)) == p for p in pts)
print("exr-functions-and-composition-b2: ok")
