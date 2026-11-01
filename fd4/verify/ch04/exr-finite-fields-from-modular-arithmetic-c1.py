"""exr-finite-fields-from-modular-arithmetic-c1: the four-element field a + b*alpha over F_2.
Tables (beta = 1 + alpha; alpha^2 = beta, alpha*beta = 1, beta^2 = alpha); all field axioms by
exhaustion; the coefficient identities for (F5); no bijection to Z/4Z preserving + and *."""
QUOTED = {"addition table": [["0", "1", "alpha", "beta"], ["1", "0", "beta", "alpha"],
                             ["alpha", "beta", "0", "1"], ["beta", "alpha", "1", "0"]],
          "multiplication table": [["0", "0", "0", "0"], ["0", "1", "alpha", "beta"],
                                   ["0", "alpha", "beta", "1"], ["0", "beta", "1", "alpha"]],
          "triples to list for (F5) and (F9)": 64}
from itertools import product, permutations
E = [(0, 0), (1, 0), (0, 1), (1, 1)]  # 0, 1, alpha, beta
name = {(0, 0): "0", (1, 0): "1", (0, 1): "alpha", (1, 1): "beta"}
add = lambda x, y: ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)
mul = lambda x, y: ((x[0] * y[0] + x[1] * y[1]) % 2,
                    (x[0] * y[1] + x[1] * y[0] + x[1] * y[1]) % 2)
QUOTED_ADD = QUOTED["addition table"]
QUOTED_MUL = QUOTED["multiplication table"]
assert [[name[add(x, y)] for y in E] for x in E] == QUOTED_ADD
assert [[name[mul(x, y)] for y in E] for x in E] == QUOTED_MUL
Z, O = (0, 0), (1, 0)
assert len(list(product(E, repeat=3))) == QUOTED["triples to list for (F5) and (F9)"]
for x, y, z in product(E, repeat=3):
    assert add(x, y) == add(y, x) and add(add(x, y), z) == add(x, add(y, z))
    assert mul(x, y) == mul(y, x) and mul(mul(x, y), z) == mul(x, mul(y, z))
    assert mul(x, add(y, z)) == add(mul(x, y), mul(x, z))
for x in E:
    assert add(x, Z) == x and add(x, x) == Z and mul(x, O) == x
    if x != Z:
        assert any(mul(x, y) == O for y in E)
assert O != Z
# (F5) coefficient identities, mod 2
for a, b, c, d, e, g in product(range(2), repeat=6):
    h, k = a * c + b * d, a * d + b * c + b * d
    l, m = c * e + d * g, c * g + d * e + d * g
    assert (h * e + k * g) % 2 == (a*c*e + a*d*g + b*c*g + b*d*e + b*d*g) % 2
    assert (h * g + k * e + k * g) % 2 == (a*c*g + a*d*e + a*d*g + b*c*e + b*c*g + b*d*e) % 2
    assert (a * l + b * m) % 2 == (a*c*e + a*d*g + b*c*g + b*d*e + b*d*g) % 2
    assert (a * m + b * l + b * m) % 2 == (a*c*g + a*d*e + a*d*g + b*c*e + b*c*g + b*d*e) % 2
# no structure-preserving bijection to Z/4Z
good = 0
for perm in permutations(range(4)):
    phi = dict(zip(E, perm))
    if all(phi[add(x, y)] == (phi[x] + phi[y]) % 4 and phi[mul(x, y)] == phi[x] * phi[y] % 4
           for x in E for y in E):
        good += 1
assert good == 0 and 2 * 2 % 4 == 0
print("ok")
