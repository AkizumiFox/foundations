"""exr-ordered-rings-b3 (Section 2.4, [B2: Prove or disprove]): verdicts F, T, T, T, F,
with the counterexamples quoted in the solution."""
import itertools

QUOTED = {
    "a": {"a": -3, "b": 1, "a2": 9, "b2": 1},
    "e": {"x": 0, "y": 1},
}

G = range(-8, 9)
# (a) false: -3 < 1 but (-3)^2 = 9 > 1 = 1^2; true when a >= 0
q = QUOTED["a"]
assert q["a"] < q["b"] and q["a"] ** 2 == q["a2"] and q["b"] ** 2 == q["b2"] and q["a2"] > q["b2"]
assert all(a * a < b * b for a in range(0, 9) for b in range(0, 9) if a < b)
# (b) true: a^2 + 1 > 0
assert all(a * a + 1 > 0 for a in G)
# (c) true in Z: x > 0 and xy = x imply y = 1
for x, y in itertools.product(G, repeat=2):
    if x > 0 and x * y == x:
        assert y == 1
    assert x * (y - 1) == x * y - x
# (d) true: a < b, c < d imply a - d < b - c
for a, b, c, d in itertools.product(range(-4, 5), repeat=4):
    if a < b and c < d:
        assert a - d < b - c
# (e) false: x = 0, y = 1; but x < y gives x + 1 <= y in Z
x, y = QUOTED["e"]["x"], QUOTED["e"]["y"]
assert x < y and not (x + 1 < y)
assert all(x + 1 <= y for x in G for y in G if x < y)
# A1 (d): a < b, c <= 0 give ac >= bc, and ac - bc = (b - a)(-c)
for a, b, c in itertools.product(G, repeat=3):
    assert a * c - b * c == (b - a) * (-c)
    if a < b and c <= 0:
        assert a * c >= b * c
print("exr-ordered-rings-b3: all quoted values check")
