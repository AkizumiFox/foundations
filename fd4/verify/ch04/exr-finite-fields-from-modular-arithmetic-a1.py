"""exr-finite-fields-from-modular-arithmetic-a1: [2][4] = [8] = [0] in Z/8Z; inverses in F_5;
4*4 + 3 = 19 = 3*5 + 4; x^2 = x on F_2; 13 prime (2, 3 do not divide, 16 > 13), 13 = 0 in F_13."""
QUOTED = {"inv5": {1: 1, 2: 3, 3: 2, 4: 4}, "c": 4, "nineteen": 19}
assert 2 * 4 % 8 == 0 and 2 % 8 and 4 % 8
for a, b in QUOTED["inv5"].items():
    assert a * b % 5 == 1
assert 4 * 4 + 3 == QUOTED["nineteen"] == 3 * 5 + 4 and QUOTED["nineteen"] % 5 == QUOTED["c"]
assert all(x * x % 2 == x for x in range(2))
assert 13 % 2 and 13 % 3 and 4 * 4 > 13 and all(13 % d for d in range(2, 13))
assert 13 % 13 == 0
print("ok")
