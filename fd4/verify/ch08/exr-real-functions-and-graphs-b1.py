"""exr-real-functions-and-graphs-b1: max(a, b) = (a + b + |a - b|)/2 and min(a, b) = (a + b - |a - b|)/2."""
from fractions import Fraction as Fr

QUOTED = {}
vals = [Fr(k, 3) for k in range(-12, 13)]
for a in vals:
    for b in vals:
        assert max(a, b) == (a + b + abs(a - b)) / 2
        assert min(a, b) == (a + b - abs(a - b)) / 2
print("exr-real-functions-and-graphs-b1: ok")
