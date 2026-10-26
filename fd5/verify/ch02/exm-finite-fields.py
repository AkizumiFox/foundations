"""exm-finite-fields: tables of Z/2Z; [1] + [1] = [2] = [0]; [1] != [0] iff n >= 2;
Z/nZ has n elements (remainders)."""
QUOTED = {"add": [[0, 1], [1, 0]], "mul": [[0, 0], [0, 1]]}
assert [[(a + b) % 2 for b in range(2)] for a in range(2)] == QUOTED["add"]
assert [[(a * b) % 2 for b in range(2)] for a in range(2)] == QUOTED["mul"]
assert (1 + 1) % 2 == 0 and (-1) % 2 == 1
for n in range(1, 30):
    assert ((1 - 0) % n != 0) == (n >= 2)
    assert len({a % n for a in range(-3 * n, 3 * n)}) == n
print("ok")
