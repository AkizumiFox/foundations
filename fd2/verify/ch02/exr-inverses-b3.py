"""exr-inverses-b3 (Ch 6, Section 6.5): h(x) = x/(1-|x|) on (-1,1) and k(y) = y/(1+|y|)."""
from fractions import Fraction as F
QUOTED = {"h": "x/(1 - \\abs{x})", "k": "y/(1 + \\abs{y})"}
h = lambda x: x / (1 - abs(x))
k = lambda y: y / (1 + abs(y))
xs = [F(j, 101) for j in range(-100, 101)]
ys = [F(j, 13) for j in range(-400, 401)]
assert all(k(h(x)) == x for x in xs)
assert all(-1 < k(y) < 1 and h(k(y)) == y for y in ys)
print("exr-inverses-b3: all quoted values check")
