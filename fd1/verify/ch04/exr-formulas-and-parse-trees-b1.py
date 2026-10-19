"""exr-formulas-and-parse-trees-b1 (Ch 4, Section 4.1): three trees from Chapter 1."""
from _s0102_formulas import tok, subformulas

QUOTED = {"(c) subformulas": "six, with \\( p \\) listed once"}

for s, n in [(r"((p \wedge q) \to r)", 5), (r"(p \to (q \to r))", 5), (r"((p \wedge q) \vee (p \wedge r))", 6)]:
    assert len(subformulas(tok(s))) == n, s
print("exr-formulas-and-parse-trees-b1: all quoted values check")
