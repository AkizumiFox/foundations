"""exr-well-defined-operations-a1 (b): the run of the key proof with
(a, b) = (1, 3), (a', b') = (4, 6), (c, d) = (2, 0)."""
QUOTED = {"out1": (2, 6), "out2": (8, 12), "cross": 14, "inter1": (2 + 12, 8 + 6), "inter2": (0, 0)}
a, b, a1, b1, c, d = 1, 3, 4, 6, 2, 0
assert a + b1 == 7 == b + a1
out1 = (a * c + b * d, a * d + b * c)
out2 = (a1 * c + b1 * d, a1 * d + b1 * c)
assert out1 == QUOTED["out1"] and out2 == QUOTED["out2"]
assert out1[0] + out2[1] == QUOTED["cross"] == out1[1] + out2[0]
assert (a * c + b1 * c, a1 * c + b * c) == QUOTED["inter1"] and a * c + b1 * c == a1 * c + b * c
assert (a1 * d + b * d, a * d + b1 * d) == QUOTED["inter2"]
# both outputs represent -4 = (-2) * 2
assert out1[0] - out1[1] == -4 == out2[0] - out2[1] == (a - b) * (c - d)
print("exr-well-defined-operations-a1: OK")
