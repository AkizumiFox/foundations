"""exm-parse-trees and its surroundings (Ch 3, Section 3.1): the three trees, the subformula
count of (c), the Quick check on ((not p or q) iff not(r and p)), and the height warning."""
from _s0102_formulas import tok, is_formula, height, nodes, subformulas

QUOTED = {
    "height of (b) and (c)": 4,
    "subformulas of (c)": "nine in all",
    "nodes of (c)": "The tree has ten nodes",
    "quick check subformulas": "**eight**",
    "quick check height": "The height is \\( 4 \\)",
    "warning: symbols of not(p and not q)": "has seven symbols",
    "warning: symbols of ((p and q) and (r and p))": "has thirteen symbols and height only \\( 3 \\)",
}

a = tok("p")
b = tok(r"\neg(p \wedge \neg q)")
c = tok(r"((p \leftrightarrow \neg q) \vee (r \wedge (\bot \to p)))")
for f in (a, b, c):
    assert is_formula(f)
assert height(a) == 1 and height(b) == 4 and height(c) == 4
assert nodes(c) == 10 and len(subformulas(c)) == 9
assert {"p", "q", "r", "bot"} <= {t for t in c}
qc = tok(r"((\neg p \vee q) \leftrightarrow \neg(r \wedge p))")
assert is_formula(qc) and height(qc) == 4 and len(subformulas(qc)) == 8
assert len(b) == 7 and height(b) == 4
w = tok(r"((p \wedge q) \wedge (r \wedge p))")
assert len(w) == 13 and height(w) == 3
# the "wide but shallow" formula of B3's equality case has 7 nodes
assert nodes(w) == 7
print("exm-parse-trees: all quoted values check")
