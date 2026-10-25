"""Section 7.5, after def-congruence: 14 = 2 + 1*12, -10 = 2 + (-1)*12, 7 is not congruent to 2
mod 12; clock: [9] + [5] = [14] = [2] and [21] + [-7] = [14] in Z/12 (prp-congruence-arithmetic
aftermath); [2]_12 contains -22, -10, 2, 14, 26."""

QUOTED = {"k14": 1, "k_minus10": -1, "clock": 2, "class2": [-22, -10, 2, 14, 26]}

n = 12
assert 14 - 2 == QUOTED["k14"] * n
assert -10 - 2 == QUOTED["k_minus10"] * n
assert (7 - 2) % n != 0
assert (9 + 5) % n == QUOTED["clock"] and 14 % n == 2
assert (21 + (-7)) == 14 and 21 % n == 9 and (-7) % n == 5
assert all((x - 2) % n == 0 for x in QUOTED["class2"])
# congruence mod n is an equivalence relation and respects + and * (sampled)
R = range(-40, 41)
for m in range(1, 9):
    for a in range(-15, 16):
        for b in range(-15, 16):
            if (a - b) % m == 0:
                for c in range(-10, 11, 3):
                    for d in range(-10, 11, 3):
                        if (c - d) % m == 0:
                            assert (a + c - b - d) % m == 0 and (a * c - b * d) % m == 0
print("def-congruence: all quoted values check")
