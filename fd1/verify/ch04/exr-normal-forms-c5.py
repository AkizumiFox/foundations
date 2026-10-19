"""exr-normal-forms-c5 (Section 4.9, displayed C4): the three formulas, and the set facts on
random collections inside U = {0..11}."""
import random
from _logic import equivalent, false_rows
assert equivalent("\\neg(a \\wedge b)", "\\neg a \\vee \\neg b")
assert equivalent("a \\wedge (b \\vee c)", "(a \\wedge b) \\vee (a \\wedge c)")
assert false_rows("(a \\to b) \\to ((a \\wedge c) \\to (b \\wedge c))") == []
random.seed(5)
U = set(range(12))
for _ in range(500):
    A, B, C = ({x for x in U if random.random() < 0.5} for _ in range(3))
    assert U - (A & B) == (U - A) | (U - B)
    assert A & (B | C) == (A & B) | (A & C)
    if A <= B:
        assert A & C <= B & C
print("exr-normal-forms-c5: all quoted values check")
