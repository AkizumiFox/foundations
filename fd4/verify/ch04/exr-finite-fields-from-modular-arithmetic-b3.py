"""exr-finite-fields-from-modular-arithmetic-b3: x^2 = 2 in F_7: x = 3, 4 (9 = 2, 16 = 2*7 + 2);
in F_5 the squares of 0..4 are 0, 1, 4, 4, 1: none."""
QUOTED = {"roots in F_7": (3, 4), "3^2 = 9": 9, "4^2 = 16 = 2*7 + 2": 16,
          "squares of 0..4 as integers": (0, 1, 4, 9, 16), "their classes in F_5": (0, 1, 4, 4, 1)}
assert [x for x in range(7) if x * x % 7 == 2] == [3, 4] and 16 == 2 * 7 + 2 and (-3) % 7 == 4
assert [x * x % 5 for x in range(5)] == [0, 1, 4, 4, 1]
assert [x for x in range(5) if x * x % 5 == 2] == []
assert tuple(x for x in range(7) if x * x % 7 == 2) == QUOTED["roots in F_7"]
assert 3 * 3 == QUOTED["3^2 = 9"] and 4 * 4 == QUOTED["4^2 = 16 = 2*7 + 2"]
assert tuple(x * x for x in range(5)) == QUOTED["squares of 0..4 as integers"]
assert tuple(x * x % 5 for x in range(5)) == QUOTED["their classes in F_5"]
assert 2 not in QUOTED["their classes in F_5"]
print("ok")
