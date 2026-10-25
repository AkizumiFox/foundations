"""exr-finite-fields-from-modular-arithmetic-c3: x^2 + x + 1 = 0: F_2 values 1, 1 (none);
F_3 values 1, 0, 1 (x = 1); F_7 raw values 1, 3, 7, 13, 21, 31, 43, remainders 1, 3, 0, 6, 0, 3, 1
(x = 2, 4)."""
QUOTED = {2: [1, 1], 3: [1, 0, 1], 7: [1, 3, 0, 6, 0, 3, 1]}
raw = [x * x + x + 1 for x in range(7)]
assert raw == [1, 3, 7, 13, 21, 31, 43]
assert 3 % 2 == 1 and 7 % 3 == 1
for p, vals in QUOTED.items():
    assert [(x * x + x + 1) % p for x in range(p)] == vals
assert [x for x in range(2) if (x*x + x + 1) % 2 == 0] == []
assert [x for x in range(3) if (x*x + x + 1) % 3 == 0] == [1]
assert [x for x in range(7) if (x*x + x + 1) % 7 == 0] == [2, 4] and 7 == 1 * 7 and 21 == 3 * 7
print("ok")
