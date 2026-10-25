"""exm-checking-a-relation: x R y iff 7 | 3x + 4y on Z is reflexive, symmetric, transitive,
not antisymmetric (witness 0, 7); identities of the scratch work; the Quick check 7 | 3x + 5y."""
QUOTED = {}
W = range(-30, 31)
R = lambda x, y: (3 * x + 4 * y) % 7 == 0
assert all(R(x, x) for x in W)
assert all(R(y, x) for x in W for y in W if R(x, y))
assert all(R(x, z) for x in W for y in W for z in W if R(x, y) and R(y, z))
assert R(0, 7) and R(7, 0) and 3 * 0 + 4 * 7 == 28 == 7 * 4 and 3 * 7 + 4 * 0 == 21 == 7 * 3
assert R(1, 1) and 3 + 4 == 7
for x in W:
    for y in W:
        assert (3 * y + 4 * x) + (3 * x + 4 * y) == 7 * x + 7 * y
        if R(x, y):
            k = (3 * x + 4 * y) // 7
            assert 3 * y + 4 * x == 7 * (x + y - k)
            for z in W:
                if R(y, z):
                    l = (3 * y + 4 * z) // 7
                    assert 3 * x + 4 * z == 7 * (k + l - y)
S = lambda x, y: (3 * x + 5 * y) % 7 == 0
assert not S(1, 1) and 3 + 5 == 8 and 8 % 7 != 0
assert S(1, 5) and 3 + 25 == 28 and not S(5, 1) and 15 + 5 == 20 and 14 < 20 < 21
print("ok")
