"""exr-finite-fields-from-modular-arithmetic-b1: (a) 3x + 5 = 2 in F_7: 3x = -3 = 4, 3^{-1} = 5,
x = 20 = 6, check 23 = 3*7 + 2. (b) x + 2y = 3, 3x + y = 1: ad - bc = -5 = 2, 2^{-1} = 4,
x = (3 - 2)*4 = 4, y = (1 - 9)*4 = -32 = 3; checks 10 = 3, 15 = 1."""
QUOTED = {"(a) 3x = 2 - 5 = -3 =": (-3, 4), "3^{-1}": 5, "x": 6, "check 3*6 + 5": 23,
          "(b) ad - bc = -5 =": (-5, 2), "2^{-1}": 4, "y before reduction": -32,
          "(x, y)": (4, 3), "checks x + 2y, 3x + y": (10, 15)}
p = 7
assert (2 - 5) % p == 4 and 3 * 5 % p == 1 and 5 * 4 == 20 and 20 % p == 6
assert 3 * 6 + 5 == 23 == 3 * 7 + 2
assert [x for x in range(p) if (3 * x + 5 - 2) % p == 0] == [6]
a, b, c, d, e, f = 1, 2, 3, 1, 3, 1
D = a * d - b * c
assert D == -5 and D % p == 2 and 2 * 4 % p == 1
x = (e * d - b * f) * 4
y = (a * f - c * e) * 4
assert x == 4 and y == -32 and -32 == -5 * 7 + 3
x, y = x % p, y % p
assert (x, y) == (4, 3)
assert (x + 2 * y, 3 * x + y) == (10, 15) and 10 % p == 3 and 15 % p == 1
sols = [(u, v) for u in range(p) for v in range(p)
        if (u + 2 * v - 3) % p == 0 and (3 * u + v - 1) % p == 0]
assert sols == [(4, 3)]
# QUOTED, from the computation above
assert (2 - 5, (2 - 5) % p) == QUOTED["(a) 3x = 2 - 5 = -3 ="]
assert next(i for i in range(p) if 3 * i % p == 1) == QUOTED["3^{-1}"]
assert [v for v in range(p) if (3 * v + 5 - 2) % p == 0] == [QUOTED["x"]]
assert 3 * QUOTED["x"] + 5 == QUOTED["check 3*6 + 5"]
assert (D, D % p) == QUOTED["(b) ad - bc = -5 ="]
assert next(i for i in range(p) if D * i % p == 1) == QUOTED["2^{-1}"]
assert (a * f - c * e) * 4 == QUOTED["y before reduction"]
assert sols == [QUOTED["(x, y)"]] and (x + 2 * y, 3 * x + y) == QUOTED["checks x + 2y, 3x + y"]
print("ok")
