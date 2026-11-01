"""exr-real-functions-and-graphs-a2: g(f(2)) = 1 and f(g(2)) = -1/2 for f(x) = x - 1, g(y) = 1/y."""
from fractions import Fraction as Fr

QUOTED = {"gf2": Fr(1), "fg2": Fr(-1, 2)}
f = lambda x: x - 1
g = lambda y: 1 / Fr(y)
assert g(f(2)) == QUOTED["gf2"]
assert f(g(2)) == QUOTED["fg2"]
# domain of g o f excludes exactly x = 1 (where f(x) = 0) among sample points
assert [x for x in range(-5, 6) if f(x) == 0] == [1]
print("exr-real-functions-and-graphs-a2: ok")
