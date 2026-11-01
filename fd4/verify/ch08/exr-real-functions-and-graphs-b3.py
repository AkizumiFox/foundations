"""exr-real-functions-and-graphs-b3: even and odd parts of 1/(1 - x) on R minus {-1, 1}."""
from fractions import Fraction as Fr

QUOTED = {"even": lambda x: 1 / (1 - x * x), "odd": lambda x: x / (1 - x * x)}
f = lambda x: 1 / (1 - x)
for k in range(-50, 51):
    x = Fr(k, 9)
    if x in (1, -1):
        continue
    e = (f(x) + f(-x)) / 2
    o = (f(x) - f(-x)) / 2
    assert f(x) + f(-x) == 2 / (1 - x * x) and f(x) - f(-x) == 2 * x / (1 - x * x)
    assert e == QUOTED["even"](x) and o == QUOTED["odd"](x)
print("exr-real-functions-and-graphs-b3: ok")
