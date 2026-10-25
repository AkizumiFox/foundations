"""exm-field-negated-product: (Q, +, a o b = -(ab)) satisfies (F5), (F6), (F9);
its one is -1, and the inverse of a != 0 is the usual a^{-1}."""
from fractions import Fraction
from itertools import product
QUOTED = {"one": Fraction(-1)}
op = lambda a, b: -(a * b)
vals = [Fraction(v) for v in (-3, -1, 0, 1, 2)] + [Fraction(1, 2), Fraction(-5, 7)]
for a, b, c in product(vals, repeat=3):
    assert op(op(a, b), c) == op(a, op(b, c)) == a * b * c
    assert op(a, b) == op(b, a)
    assert op(a, b + c) == op(a, b) + op(a, c)
for a in vals:
    assert op(a, QUOTED["one"]) == a
    if a != 0:
        assert op(a, 1 / a) == QUOTED["one"]
assert QUOTED["one"] != 0
print("ok")
