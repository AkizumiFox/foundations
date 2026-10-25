"""exr-characteristic-and-prime-subfield-c3: the four-element field {a + b alpha : a, b in F2}
with (a + b al)(c + d al) = (ac + bd) + (ad + bc + bd) al. Checks the field axioms by exhaustion,
char 2, alpha^2 = beta, alpha*beta = 1, beta^2 = alpha, and that x -> x^2 is a bijective
homomorphism exchanging alpha and beta."""
from itertools import product
E = list(product(range(2), repeat=2))  # (a, b) = a + b alpha
ZERO, ONE, AL, BE = (0, 0), (1, 0), (0, 1), (1, 1)
QUOTED = {"char": 2, "squares": {(0, 0): (0, 0), (1, 0): (1, 0), (0, 1): (1, 1), (1, 1): (0, 1)}}


def add(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)


def mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + b * d) % 2, (a * d + b * c + b * d) % 2)


for x, y, z in product(E, repeat=3):
    assert add(x, y) == add(y, x) and mul(x, y) == mul(y, x)
    assert add(add(x, y), z) == add(x, add(y, z))
    assert mul(mul(x, y), z) == mul(x, mul(y, z))
    assert mul(x, add(y, z)) == add(mul(x, y), mul(x, z))
for x in E:
    assert add(x, ZERO) == x and mul(x, ONE) == x
    assert any(add(x, y) == ZERO for y in E)
    if x != ZERO:
        assert any(mul(x, y) == ONE for y in E)
assert add(ONE, ONE) == ZERO and ONE != ZERO
assert mul(AL, AL) == BE and mul(AL, BE) == ONE and mul(BE, BE) == AL
assert add(ONE, BE) == AL
sq = {x: mul(x, x) for x in E}
assert sq == QUOTED["squares"]
for x, y in product(E, repeat=2):
    assert sq[add(x, y)] == add(sq[x], sq[y]) and sq[mul(x, y)] == mul(sq[x], sq[y])
assert len(set(sq.values())) == 4
print("ok")
