"""exr-translation-b4 (Section 6.1): (f)'s sets separate A u B <= C from (e)."""

QUOTED = {"A": {1}, "B": {2}, "C": set()}
A, B, C = QUOTED["A"], QUOTED["B"], QUOTED["C"]
U = A | B | C | {0, 3}
union_sub = all(x in C for x in U if x in A or x in B)
e_formula = all(x in C for x in U if x in A and x in B)
assert union_sub is False and e_formula is True
assert not (A & B)
print("exr-translation-b4: all quoted values check")
