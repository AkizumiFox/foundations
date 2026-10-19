"""exr-four-kinds-of-task-c1 (Ch 3 s02, exit check): Gamma |- P -> S is valid by truth table;
with R -> S replaced by R -> T the claim breaks at x = 1 with P: x > 0, Q: x > 5, R: x < 2,
S: x > 3, T: x < 10 (every member of the new counterexample set true)."""
from fractions import Fraction
from itertools import product


def imp(a, b):
    return (not a) or b


for P, Q, R, S in product([False, True], repeat=4):
    if imp(P, Q or R) and imp(Q, S) and imp(R, S):
        assert imp(P, S)
QUOTED = {"x": 1, "lines_bot": 13, "lines_direct": 11}
x = Fraction(QUOTED["x"])
P, Q, R, S, T = x > 0, x > 5, x < 2, x > 3, x < 10
cset = [imp(P, Q or R), imp(Q, S), imp(R, T), not imp(P, S)]
assert all(cset)
print("exr-four-kinds-of-task-c1: ok")
