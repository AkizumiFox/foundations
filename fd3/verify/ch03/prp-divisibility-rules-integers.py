"""prp-divisibility-rules-integers and the instances before it (01-division-with-remainder):
3 | -12 (k = -4), -4 | 0, 0 | 0, 5 does not divide 12; 2 | -2 | 2 and 3 | -3 (the paragraph after)."""
QUOTED = {"3|-12": -4, "-4|0": 0, "0|0": 1}
assert QUOTED["3|-12"] * 3 == -12
assert QUOTED["-4|0"] * (-4) == 0
assert QUOTED["0|0"] * 0 == 0
assert all(5 * k != 12 for k in range(-100, 101))
assert (-1) * 2 == -2 and (-1) * (-2) == 2 and (-1) * 3 == -3 and 3 > -3
# (e) and (g) on a range
for a in range(1, 40):
    for b in range(1, 40):
        if b % a == 0:
            assert a <= b
assert [a for a in range(-10, 11) if a != 0 and 1 % a == 0] == [-1, 1]
print("ok")
