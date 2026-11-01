"""prp-even-odd-decomposition: the example (x + 1)^2 has even part x^2 + 1 and odd part 2x."""
from fractions import Fraction as Fr

QUOTED = {"even": lambda x: x * x + 1, "odd": lambda x: 2 * x}
f = lambda x: (x + 1) ** 2
for k in range(-30, 31):
    x = Fr(k, 7)
    e = (f(x) + f(-x)) / 2
    o = (f(x) - f(-x)) / 2
    assert e == QUOTED["even"](x) and o == QUOTED["odd"](x)
    assert e + o == f(x) == x * x + 2 * x + 1
print("prp-even-odd-decomposition: ok")
