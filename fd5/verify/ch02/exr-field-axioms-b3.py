"""exr-field-axioms-b3: (a) (Q, +, a o b = 2ab) is a field with one 1/2 and inverse 1/(4a);
(b) a o b = ab + 1 breaks (F9): ab + ac + 1 vs ab + ac + 2; (c) 1 + 1 = 2 not in {0, 1}."""
from fractions import Fraction
from itertools import product
QUOTED = {"one": Fraction(1, 2)}
op = lambda a, b: 2 * a * b
vals = [Fraction(v) for v in (-3, -1, 0, 1, 2)] + [Fraction(1, 2), Fraction(-5, 7)]
for a, b, c in product(vals, repeat=3):
    assert op(op(a, b), c) == op(a, op(b, c)) == 4 * a * b * c
    assert op(a, b) == op(b, a)
    assert op(a, b + c) == op(a, b) + op(a, c)
for a in vals:
    assert op(a, QUOTED["one"]) == a
    if a != 0:
        assert op(a, 1 / (4 * a)) == QUOTED["one"]
assert QUOTED["one"] != 0
op2 = lambda a, b: a * b + 1
for a, b, c in product(vals, repeat=3):
    assert op2(a, b + c) == a * b + a * c + 1
    assert op2(a, b) + op2(a, c) == a * b + a * c + 2
assert op2(0, 0 + 0) == 1 and op2(0, 0) + op2(0, 0) == 2
assert 1 + 1 == 2 and 2 not in (0, 1)
print("ok")
