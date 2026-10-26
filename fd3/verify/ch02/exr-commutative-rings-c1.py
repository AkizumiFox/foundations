"""exr-commutative-rings-c1: on Z, x (+) y = x + y - 1, x (.) y = x + y - xy.
(a) zero 1, one 0, negative 2 - x. (b) (F9) for (+), (.): both sides equal 2x + y + z - 1 - xy - xz.
(c) phi(x) = 1 - x: phi(x (+) y) = phi(x) + phi(y), phi(x (.) y) = phi(x) phi(y), phi(phi(x)) = x.
Also every ring law (F1)-(F7), (F9) for (+), (.) on a box of integers."""
import itertools
oplus = lambda x, y: x + y - 1
odot = lambda x, y: x + y - x * y
phi = lambda x: 1 - x
QUOTED = {"zero": 1, "one": 0, "neg": lambda x: 2 - x}
B = range(-6, 7)
for x in B:
    assert oplus(x, QUOTED["zero"]) == x
    assert odot(x, QUOTED["one"]) == x
    assert oplus(x, QUOTED["neg"](x)) == QUOTED["zero"]
    assert phi(phi(x)) == x
for x, y in itertools.product(B, repeat=2):
    assert phi(oplus(x, y)) == phi(x) + phi(y)
    assert phi(odot(x, y)) == phi(x) * phi(y)
    assert oplus(x, y) == oplus(y, x) and odot(x, y) == odot(y, x)
for x, y, z in itertools.product(B, repeat=3):
    lhs = odot(x, oplus(y, z))
    assert lhs == x + (y + z - 1) - x * (y + z - 1) == 2 * x + y + z - 1 - x * y - x * z
    assert oplus(odot(x, y), odot(x, z)) == (x + y - x * y) + (x + z - x * z) - 1 == lhs
    assert oplus(oplus(x, y), z) == oplus(x, oplus(y, z))
    assert odot(odot(x, y), z) == odot(x, odot(y, z))
print("exr-commutative-rings-c1: OK")
