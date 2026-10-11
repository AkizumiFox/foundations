"""exr-derivations-a1 (Section 1.2): (e) Tr leads from true lines to a true line (sampled on
exact rationals); (d) the justifications and (f) the sequent of the and-derivation."""
import itertools
from fractions import Fraction

QUOTED = {"(d) (iv)": "4, 2", "(e) true": True}

pts = [Fraction(n, 4) for n in range(-12, 13)]
for a, b, c in itertools.product(pts, repeat=3):
    if a < b and b < c:
        assert a < c

# (d): lines 1 P&(Q&R), 2 P (andE 1), 3 Q&R (andE 1), 4 R (andE 3), 5 R&P (andI 4, 2)
A = lambda l, r: ("and", l, r)
lines = {1: A("P", A("Q", "R")), 2: "P", 3: A("Q", "R"), 4: "R", 5: A("R", "P")}
andE = lambda i, k: lines[i][0] == "and" and lines[k] in lines[i][1:]
assert andE(1, 2) and andE(1, 3) and andE(3, 4) and not andE(1, 4)
assert lines[5] == A(lines[4], lines[2])          # "andI 4, 2"; "2, 4" equally (either order)
# (f): premise line 1, last line 5
assert (lines[1], lines[5]) == (A("P", A("Q", "R")), A("R", "P"))
print("exr-derivations-a1: all checks pass")
