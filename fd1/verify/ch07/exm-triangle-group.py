"""exm-triangle-group (Section 7.4): the table computed from the six rearrangements of the
corners (x.y = first x, then y); all 216 triples associative; identity; inverses;
a.r = c, r.a = b; every two-element group is commutative (enumeration)."""
import itertools

PERM = {  # where each corner 1, 2, 3 goes
    "e": {1: 1, 2: 2, 3: 3},
    "r": {1: 2, 2: 3, 3: 1},
    "q": {1: 3, 2: 1, 3: 2},
    "a": {1: 1, 2: 3, 3: 2},
    "b": {1: 3, 2: 2, 3: 1},
    "c": {1: 2, 2: 1, 3: 3},
}
QUOTED = {  # rows as printed: row x, column y, entry x.y, columns e r q a b c
    "e": "e&e&r&q&a&b&c", "r": "r&r&q&e&b&c&a", "q": "q&q&e&r&c&a&b",
    "a": "a&a&c&b&e&q&r", "b": "b&b&a&c&r&e&q", "c": "c&c&b&a&q&r&e",
}
NAMES = "erqabc"
inv = {tuple(sorted(p.items())): n for n, p in PERM.items()}


def mul(x, y):  # first x, then y
    return inv[tuple(sorted({i: PERM[y][PERM[x][i]] for i in (1, 2, 3)}.items()))]


# the flips fix the stated corner and swap the other two
assert PERM["a"][1] == 1 and PERM["b"][2] == 2 and PERM["c"][3] == 3
for x in NAMES:
    assert "&".join([x] + [mul(x, y) for y in NAMES]) == QUOTED[x], x
for x, y, z in itertools.product(NAMES, repeat=3):
    assert mul(mul(x, y), z) == mul(x, mul(y, z))
assert len(list(itertools.product(NAMES, repeat=3))) == 216
for x in NAMES:
    assert mul(x, "e") == x and mul("e", x) == x
    assert any(mul(x, y) == "e" and mul(y, x) == "e" for y in NAMES)
assert mul("a", "r") == "c" and mul("r", "a") == "b"
assert mul("r", "q") == "e" == mul("q", "r")
assert all(mul(f, f) == "e" for f in "abc")
assert mul("a", "a") == "e" and mul(mul("r", "r"), "r") == "e" == mul("r", mul("r", "r"))
assert mul("q", "a") == "c" and mul("a", "q") == "b"   # A2 (c)
# every group on {e, g} with identity e is commutative
D = ["e", "g"]
for gg in D:
    t = {("e", "e"): "e", ("e", "g"): "g", ("g", "e"): "g", ("g", "g"): gg}
    assert all(t[(x, y)] == t[(y, x)] for x in D for y in D)
print("exm-triangle-group: all quoted values check")
