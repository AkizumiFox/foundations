"""exr-quotient-rings-b1: tables of Z/4Z, zero divisors, classes with a partner of product [1]."""
QUOTED = {
    "add": [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]],
    "mul": [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 0, 2], [0, 3, 2, 1]],
    "ex": {(3, 3, "+"): (6, 1, 2), (3, 3, "*"): (9, 2, 1)},
    "zero_div": {2}, "inv": {1, 3},
}
for a in range(4):
    for b in range(4):
        assert QUOTED["add"][a][b] == (a + b) % 4 and QUOTED["mul"][a][b] == (a * b) % 4
for (a, b, op), (v, q, r) in QUOTED["ex"].items():
    assert (a + b if op == "+" else a * b) == v == q * 4 + r
M = QUOTED["mul"]
assert {a for a in range(1, 4) if any(M[a][b] == 0 for b in range(1, 4))} == QUOTED["zero_div"]
assert {a for a in range(4) if 1 in M[a]} == QUOTED["inv"]
print("exr-quotient-rings-b1: ok")
