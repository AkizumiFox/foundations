"""exm-group-nonexamples: (1 - 1) - 1 = -1 and 1 - (1 - 1) = 1; [2][3] = [0] in Z/6Z;
no integer b with 2b = 1; no natural b with 1 + b = 0 (checked on a range)."""
QUOTED = {"left": -1, "right": 1, "z6": (2, 3, 0)}
assert (1 - 1) - 1 == QUOTED["left"] and 1 - (1 - 1) == QUOTED["right"]
a, b, c = QUOTED["z6"]
assert a * b % 6 == c
assert all(2 * b != 1 for b in range(-100, 101))
assert all(1 + b != 0 for b in range(0, 101))
print("exm-group-nonexamples: ok")
