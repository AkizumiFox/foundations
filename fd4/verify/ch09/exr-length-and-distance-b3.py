"""exr-length-and-distance-b3: ||x-a||^2 = ||x-b||^2 iff 2<x, b-a> = ||b||^2 - ||a||^2 (random exact check, both directions, with
points constructed on the set); the midpoint satisfies <(a+b)/2, b-a> = (||b||^2 - ||a||^2)/2."""
QUOTED = {"half": "\\tfrac12"}
from fractions import Fraction as Fr
import random
def dot(x, y): return sum(p * q for p, q in zip(x, y))
def sub(x, y): return [p - q for p, q in zip(x, y)]
random.seed(5)
for _ in range(3000):
    n = random.randint(1, 5)
    a = [Fr(random.randint(-6, 6)) for _ in range(n)]; b = [Fr(random.randint(-6, 6)) for _ in range(n)]
    x = [Fr(random.randint(-6, 6), random.randint(1, 3)) for _ in range(n)]
    lhs = dot(sub(x, a), sub(x, a)) == dot(sub(x, b), sub(x, b))
    rhs = dot(x, sub(b, a)) == Fr(1, 2) * (dot(b, b) - dot(a, a))
    assert lhs == rhs
    mid = [(p + q) / 2 for p, q in zip(a, b)]
    assert dot(mid, sub(b, a)) == Fr(1, 2) * (dot(b, b) - dot(a, a))
    assert dot(sub(mid, a), sub(mid, a)) == dot(sub(mid, b), sub(mid, b))
print("ok")
