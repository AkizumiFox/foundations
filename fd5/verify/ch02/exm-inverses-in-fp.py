"""exm-inverses-in-fp: inverses in F_7 (1*1, 2*4 = 8, 3*5 = 15, 6*6 = 36); 101 prime with
remainders 1, 2, 1, 1, 5, 3, 5, 2, 1 on division by 2..10, 11*11 = 121; Euclid on (101, 17):
101 = 5*17 + 16, 17 = 1*16 + 1, 1 = 6*17 - 101; 17^{-1} = 6, 17*6 = 102."""
QUOTED = {"f7": {1: 1, 2: 4, 3: 5, 4: 2, 5: 3, 6: 6}, "products": (8, 15, 36),
          "rem101": [1, 2, 1, 1, 5, 3, 5, 2, 1], "steps": [(101, 5, 17, 16), (17, 1, 16, 1)],
          "bez": (6, -1), "inv": 6, "check": 102}
for a, b in QUOTED["f7"].items():
    assert a * b % 7 == 1
assert sorted(QUOTED["f7"].values()) == list(range(1, 7))
assert (2 * 4, 3 * 5, 6 * 6) == QUOTED["products"]
assert [x for x in range(1, 7) if x * x % 7 == 1] == [1, 6]
assert [101 % d for d in range(2, 11)] == QUOTED["rem101"]
assert 10 * 10 <= 101 < 11 * 11 == 121
assert all(101 % d for d in range(2, 101))
for a, q, b, r in QUOTED["steps"]:
    assert a == q * b + r and 0 <= r < b
assert 17 - 16 == 1 and 17 - (101 - 5 * 17) == 6 * 17 - 101 == 1
u, v = QUOTED["bez"]
assert 17 * u + 101 * v == 1
assert QUOTED["inv"] == u % 101 and 17 * 6 == QUOTED["check"] == 101 + 1
print("ok")
