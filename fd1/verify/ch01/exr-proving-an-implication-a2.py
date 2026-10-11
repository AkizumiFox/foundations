"""exr-proving-an-implication-a2 (Section 1.4) and the scope figure of "Which lines a line
may cite" that its parts (a)-(c) use: every arrow and bracket of the figure, the Quick check
after it, and drill parts (a)-(c), (h), (j), decided by def-derivation's scope rule."""

# The figure: lines 1..11; box A = 2-4, box B = 6-10, box C = 7-8 (inside B).
BOXES = {"A": (2, 4), "B": (6, 10), "C": (7, 8)}


def boxes_containing_line(k):
    return {name for name, (a, b) in BOXES.items() if a <= k <= b}


def boxes_containing_box(name):
    a, b = BOXES[name]
    return {other for other, (c, d) in BOXES.items() if other != name and c <= a and b <= d}


def line_available(i, k):
    """def-derivation: i < k and every box containing line i also contains line k."""
    return i < k and boxes_containing_line(i) <= boxes_containing_line(k)


def box_available(name, k):
    """def-derivation: the box ends before k, and the boxes other than itself containing it
    are exactly the boxes containing line k."""
    return BOXES[name][1] < k and boxes_containing_box(name) == boxes_containing_line(k)


QUOTED = {
    "legal arrows": {(4, 2), (8, 6), (8, 1), (11, 5)},
    "illegal arrows": {(6, 3), (9, 7), (11, 9)},
    "whole boxes cited": {(5, "A"), (11, "B")},
    "line 10 may cite": {1, 5, 6, 9},
    "line 10 may cite box": {"C"},
    "caption checks": {(8, 1), (10, 5), (10, 6), (11, 5)},
}
for k, i in QUOTED["legal arrows"] | QUOTED["caption checks"]:
    assert line_available(i, k), (k, i)
for k, i in QUOTED["illegal arrows"]:
    assert not line_available(i, k), (k, i)
for k, name in QUOTED["whole boxes cited"]:
    assert box_available(name, k), (k, name)
assert {i for i in range(1, 10) if line_available(i, 10)} == QUOTED["line 10 may cite"]
assert {n for n in BOXES if box_available(n, 10)} == QUOTED["line 10 may cite box"]

# The picture rule (no path wording) agrees with the scope rule on every pair of the figure:
# "a line inside a box may be cited only from inside that box".
for k in range(1, 12):
    for i in range(1, k):
        picture = all(BOXES[n][0] <= k <= BOXES[n][1] for n in boxes_containing_line(i))
        assert picture == line_available(i, k)

# Drill (a) 8 may cite 5; (b) 9 may not cite the box 2-4; (c) 11 may not cite 6.
assert line_available(5, 8)
assert not box_available("A", 9)
assert not line_available(6, 11)

# Drill (h): boxes {2-3}; line 5 cites line 2 (illegal) and line 4 (legal).
BOXES = {"D": (2, 3)}
assert not line_available(2, 5) and line_available(4, 5)

# Drill (j): x^2 > 9 is false at x = 0.
assert not 0**2 > 9
print("exr-proving-an-implication-a2: checks")
