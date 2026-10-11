"""def-integer-order (Section 10.3): the examples after the definition and the Quick check.
Integers are pairs (a, b) of naturals; [(a, b)] is positive iff b < a."""
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (x[1], x[0])


def pos(x):
    return x[1] < x[0]


def value(x):            # the school integer a - b, for orientation only
    return x[0] - x[1]


QUOTED = {
    "pos_5_2": True, "pos_2_5": False, "pos_4_4": False, "value_5_2": 3,
    "y_minus_x": (9, 4), "check_diff": (12, 11),
}
assert pos((5, 2)) == QUOTED["pos_5_2"] and value((5, 2)) == QUOTED["value_5_2"]
assert pos((2, 5)) == QUOTED["pos_2_5"] and pos((4, 4)) == QUOTED["pos_4_4"]
d = add((4, 1), neg((3, 5)))
assert d == QUOTED["y_minus_x"] and pos(d)
assert value((3, 5)) == -2 and value((4, 1)) == 3
c = add((2, 4), neg((7, 10)))
assert c == QUOTED["check_diff"] and pos(c)
assert value((7, 10)) == -3 and value((2, 4)) == -2
assert not pos((0, 0))
# closure of S under ~ on a grid: (a, b) ~ (a2, b2) and b < a imply b2 < a2
G = range(0, 9)
for a in G:
    for b in G:
        for a2 in G:
            for b2 in G:
                if a + b2 == b + a2 and b < a:
                    assert b2 < a2
print("def-integer-order: all quoted values check")
