"""exr-frobenius-and-fermat-r1: z^2 = -3 + 4i; r = 5, (r + a)/2 = 1, (r - a)/2 = 4, w = 1 + 2i,
(1 + 2i)^2 = -3 + 4i; exactly two roots +-w (checked over Gaussian integers in a box)."""
QUOTED = {"r": 5, "x2": 1, "y2": 4, "w": (1, 2)}
a, b = -3, 4
assert a * a + b * b == 25 == QUOTED["r"] ** 2
assert (QUOTED["r"] + a) / 2 == QUOTED["x2"] and (QUOTED["r"] - a) / 2 == QUOTED["y2"]
w = complex(*QUOTED["w"])
assert w * w == complex(-3, 4)
sols = {(x, y) for x in range(-10, 11) for y in range(-10, 11) if complex(x, y) ** 2 == complex(-3, 4)}
assert sols == {(1, 2), (-1, -2)}
print("ok")
