"""exr-groups-a1: (b) a * b = a + b + 1 on Z is a group (identity -1, inverse -a - 2,
abelian, associative); (c) the two bijections of {1, 2, 3}; (d) 3.[5] = [1] and
(-2).[5] = [4] in Z/7Z."""
QUOTED = {"identity": -1, "inv_offset": -2, "fg": {1: 2, 2: 3, 3: 1},
          "fg_inv_1": 3, "three_5": 1, "minus_two_5": 4}
op = lambda a, b: a + b + 1
R = range(-12, 13)
for a in R:
    assert op(a, QUOTED["identity"]) == a == op(QUOTED["identity"], a)
    assert op(a, -a + QUOTED["inv_offset"]) == -1 == op(-a + QUOTED["inv_offset"], a)
    for b in R:
        assert op(a, b) == op(b, a)
        for c in R:
            assert op(op(a, b), c) == op(a, op(b, c)) == a + b + c + 2
f = {1: 2, 2: 1, 3: 3}
g = {1: 1, 2: 3, 3: 2}
fg = {x: f[g[x]] for x in (1, 2, 3)}
assert fg == QUOTED["fg"]
fg_inv = {v: k for k, v in fg.items()}
assert fg_inv[1] == QUOTED["fg_inv_1"]
assert fg[1] == 2  # f^{-1} o g^{-1} = f o g
assert {x: g[f[x]] for x in (1, 2, 3)}[1] == 3
assert (5 + 5 + 5) % 7 == QUOTED["three_5"] and 15 == 2 * 7 + 1
neg5 = (-5) % 7
assert neg5 == 2 and (neg5 + neg5) % 7 == QUOTED["minus_two_5"]
assert (QUOTED["minus_two_5"] + 10) % 7 == 0
print("exr-groups-a1: ok")
