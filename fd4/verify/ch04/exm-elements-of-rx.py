"""exm-elements-of-rx (Section 4.1): coefficient sequences and the classes of 7."""
QUOTED = {
    "a": [2, -1, 3],        # 3x^2 - x + 2 over Q, constant term first
    "b": [0, 1, 1],         # x^2 + x over F_2
    "c": [4, 3],            # [3]x + [4] over Z/6Z
    "seven_mod_5": 2,
    "seven_minus_2": 5,
    "seven_mod_2": 1,
    "seven_minus_1": 6,
}
# 3x^2 - x + 2: coefficient of x^k in position k
poly_a = {2: 3, 1: -1, 0: 2}
assert [poly_a.get(k, 0) for k in range(3)] == QUOTED["a"]
poly_b = {2: 1, 1: 1}
assert [poly_b.get(k, 0) % 2 for k in range(3)] == QUOTED["b"] and any(QUOTED["b"])
poly_c = {1: 3, 0: 4}
assert [poly_c.get(k, 0) % 6 for k in range(2)] == QUOTED["c"]
assert 7 % 5 == QUOTED["seven_mod_5"] and 7 - 2 == QUOTED["seven_minus_2"] == 5
assert 7 % 2 == QUOTED["seven_mod_2"] and 7 - 1 == QUOTED["seven_minus_1"] == 3 * 2
print("exm-elements-of-rx: ok")
