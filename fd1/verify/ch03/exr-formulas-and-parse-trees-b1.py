"""exr-formulas-and-parse-trees-b1 (Ch 3, Section 3.1): three trees from Chapter 1."""
from _s0102_formulas import tok, height, subformulas

QUOTED = {"(c) subformulas": "six, with \\( p \\) listed once", "heights": "Height \\( 3 \\)"}

for s, n in [(r"((p \wedge q) \to r)", 5), (r"(p \to (q \to r))", 5), (r"((p \wedge q) \vee (p \wedge r))", 6)]:
    f = tok(s)
    assert height(f) == 3 and len(subformulas(f)) == n, s
print("exr-formulas-and-parse-trees-b1: all quoted values check")
