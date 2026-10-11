"""exm-completing-square-f3: in F3, 2*2 = 4 = 1 (so 2^{-1} = 2), 4 = 1 != 0, 3 = 0,
4(x^2 + x + 1) = (2x + 1)^2 for all x, the only root is x = 2^{-1}(-1) = 2*2 = 1, and the
values at 0, 1, 2 are 1, 3, 7 (= 1, 0, 1). In F2, 2 = 4 = 0."""
QUOTED = {"inv2": 2, "minus1": 2, "root": 1, "vals": (1, 3, 7)}
p = 3
assert (2 * QUOTED["inv2"]) % p == 1 and 4 % p == 1 and 3 % p == 0
assert (-1) % p == QUOTED["minus1"]
for x in range(p):
    assert (4 * (x * x + x + 1)) % p == ((2 * x + 1) ** 2) % p
assert (QUOTED["inv2"] * QUOTED["minus1"]) % p == QUOTED["root"]
assert tuple(x * x + x + 1 for x in range(p)) == QUOTED["vals"]
assert {x for x in range(p) if (x * x + x + 1) % p == 0} == {QUOTED["root"]}
assert 2 % 2 == 0 and 4 % 2 == 0
print("ok")
