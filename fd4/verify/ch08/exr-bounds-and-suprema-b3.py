"""exr-bounds-and-suprema-b3: x/(x^2 + 1) on R."""
from fractions import Fraction as Fr

QUOTED = {"sup": Fr(1, 2), "argsup": 1, "inf": Fr(-1, 2), "arginf": -1}
h = lambda x: Fr(x) / (Fr(x)**2 + 1)
for k in range(-500, 501):
    x = Fr(k, 37)
    assert Fr(1, 2) - h(x) == (x - 1)**2 / (2 * (x**2 + 1))
    assert h(x) + Fr(1, 2) == (x + 1)**2 / (2 * (x**2 + 1))
    assert QUOTED["inf"] <= h(x) <= QUOTED["sup"]
assert h(QUOTED["argsup"]) == QUOTED["sup"] and h(QUOTED["arginf"]) == QUOTED["inf"]
print("ok")
