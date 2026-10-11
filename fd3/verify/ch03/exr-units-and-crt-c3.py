"""exr-units-and-crt-c3: 1 = 2*3 - 1*5, x1 = 1*5*(-1) + 2*3*2 = 7; 1 = 1*15 - 2*7,
x2 = 7*7*(-2) + 3*15*1 = -53; -53 + 105 = 52; 52 = 17*3 + 1 = 10*5 + 2 = 7*7 + 3."""
QUOTED = {"x1": 7, "x2": -53, "rep": 52}
assert 2 * 3 - 1 * 5 == 1 and 1 * 15 - 2 * 7 == 1
assert 1 * 5 * (-1) + 2 * 3 * 2 == QUOTED["x1"]
assert 7 * 7 * (-2) + 3 * 15 * 1 == QUOTED["x2"] and QUOTED["x2"] + 105 == QUOTED["rep"]
assert 52 == 17 * 3 + 1 == 10 * 5 + 2 == 7 * 7 + 3
assert [y for y in range(105) if y % 3 == 1 and y % 5 == 2 and y % 7 == 3] == [52]
assert [y for y in range(15) if y % 3 == 1 and y % 5 == 2] == [7]
print("ok")
