"""exm-parse-trees and its surroundings (Ch 4, Section 4.1): the three trees, the subformula
count of (c), and the Quick check on ((not p or q) iff not(r and p)).
(The heights and the height warning moved with def-height to Section 4.3.)"""
from _s0102_formulas import tok, is_formula, nodes, subformulas

QUOTED = {
    "subformulas of (c)": "nine in all",
    "nodes of (c)": "The tree has ten nodes",
    "quick check subformulas": "**eight**",
}

a = tok("p")
b = tok(r"\neg(p \wedge \neg q)")
c = tok(r"((p \leftrightarrow \neg q) \vee (r \wedge (\bot \to p)))")
for f in (a, b, c):
    assert is_formula(f)
assert nodes(a) == 1 and nodes(b) == 5
assert nodes(c) == 10 and len(subformulas(c)) == 9
assert {"p", "q", "r", "bot"} <= {t for t in c}
qc = tok(r"((\neg p \vee q) \leftrightarrow \neg(r \wedge p))")
assert is_formula(qc) and len(subformulas(qc)) == 8
s2 = tok(r"((p \wedge q) \vee r)")
assert len(subformulas(s2)) == 5
print("exm-parse-trees: all quoted values check")
