"""exr-the-uniqueness-theorem-r2: brute-force well-definedness on pairs (p, q) with |p| <= 12,
1 <= q <= 12. (p, q) ~ (r, s) iff p s = r q. Rules (a) (p^2, q^2) and (b) (p + q, q) respect ~;
rule (c) (p + 1, q) does not, with the quoted witness (1, 2) ~ (2, 4) but (2, 2) !~ (3, 4)."""
from fractions import Fraction as F
from itertools import product

QUOTED = {"witness": ((1, 2), (2, 4)), "images": ((2, 2), (3, 4)), "cross": (8, 6)}

def eq(x, y):
    return x[0] * y[1] == y[0] * x[1]

pairs = [(p, q) for p in range(-12, 13) for q in range(1, 13)]
rules = {
    "a": lambda p, q: (p * p, q * q),
    "b": lambda p, q: (p + q, q),
    "c": lambda p, q: (p + 1, q),
}
bad = {k: 0 for k in rules}
for x, y in product(pairs, pairs):
    if eq(x, y):
        for k, f in rules.items():
            fx, fy = f(*x), f(*y)
            assert fx[1] > 0
            if not eq(fx, fy):
                bad[k] += 1
assert bad["a"] == 0 and bad["b"] == 0 and bad["c"] > 0
# (a) is x -> x^2, (b) is x -> x + 1
for p, q in pairs:
    assert F(*rules["a"](p, q)) == F(p, q) ** 2
    assert F(*rules["b"](p, q)) == F(p, q) + 1
(w1, w2), (i1, i2) = QUOTED["witness"], QUOTED["images"]
assert eq(w1, w2) and rules["c"](*w1) == i1 and rules["c"](*w2) == i2
assert i1[0] * i2[1] == QUOTED["cross"][0] and i1[1] * i2[0] == QUOTED["cross"][1]
assert not eq(i1, i2)
print("ok")
