"""exr-characteristic-and-prime-subfield-b2: x^2 + x + 1 = 0 in F7: D = -3 = 4 = 2^2, 2^{-1} = 4,
roots 4 and 2 (4^2 + 4 + 1 = 21, 2^2 + 2 + 1 = 7); in F2 no root though D = 1 is a square.
Also checks the completing-the-square criterion in F_p, p odd prime < 30, for all b, c."""
QUOTED = {"D": 4, "s": 2, "inv2": 4, "roots": {2, 4}, "vals": (21, 7)}
p = 7
assert (1 - 4) % p == QUOTED["D"] == (QUOTED["s"] ** 2) % p
assert (2 * QUOTED["inv2"]) % p == 1
roots = {x for x in range(p) if (x * x + x + 1) % p == 0}
assert roots == QUOTED["roots"]
assert {(QUOTED["inv2"] * (-1 + 2)) % p, (QUOTED["inv2"] * (-1 - 2)) % p} == roots
assert (4 * 4 + 4 + 1, 2 * 2 + 2 + 1) == QUOTED["vals"]
assert (4 * (-1 - 2)) == -12 and -12 % 7 == 2
# F2: no root, D = 1 square
assert all((x * x + x + 1) % 2 for x in range(2)) and (1 - 0) % 2 == 1
for q in (3, 5, 7, 11, 13, 17, 19, 23, 29):
    squares = {(s * s) % q: s for s in range(q)}
    inv2 = pow(2, -1, q)
    for b in range(q):
        for c in range(q):
            sol = {x for x in range(q) if (x * x + b * x + c) % q == 0}
            D = (b * b - 4 * c) % q
            if D in squares:
                s = squares[D]
                assert sol == {((-b + s) * inv2) % q, ((-b - s) * inv2) % q}
            else:
                assert sol == set()
print("ok")
