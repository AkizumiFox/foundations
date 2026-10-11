"""exm-recursive-definitions (Ch 3, Section 3.2): height, atoms, connectives, subformulas and
length of (not(p and q) -> (q or bot)); recursive height = tree height; length clauses."""
from _s0102_formulas import tok, height, atoms, connectives, subformulas, all_formulas, parse

QUOTED = {"height": "= 1 + \\max\\{3, 2\\} = 4", "length": 14, "connectives": "four in all",
          "length pieces": "\\( 6 + 5 + 3 = 14 \\)"}

chi = tok(r"(\neg(p \wedge q) \to (q \vee \bot))")
assert height(chi) == 4 and atoms(chi) == {"p", "q"} and connectives(chi) == 4
assert len(chi) == 14 and len(tok(r"\neg(p \wedge q)")) == 6 and len(tok(r"(q \vee \bot)")) == 5
assert len(subformulas(chi)) == 7


def rec_len(s):
    sp = parse(s)
    if sp[0] == "base":
        return 1
    if sp[0] == "neg":
        return rec_len(sp[1]) + 1
    return rec_len(sp[1]) + rec_len(sp[2]) + 3


def tree_height(s):
    """longest root-to-leaf path in the tree built from the unique decomposition"""
    sp = parse(s)
    kids = sp[1:]
    return 1 + (max(tree_height(k) for k in kids) if kids else 0)


for f in all_formulas(10):
    assert rec_len(f) == len(f) and tree_height(f) == height(f)
print("exm-recursive-definitions: all quoted values check")
