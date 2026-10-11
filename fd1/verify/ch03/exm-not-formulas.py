"""exm-not-formulas, exm-formation-sequences and the Quick check after them (Ch 3, Section 3.1):
which strings are formulas."""
from _s0102_formulas import tok, is_formula

QUOTED = {"length of p and -> q": "it has length \\( 4 \\)", "non-formulas": True}

for s in [r"p \wedge \to q", r"(p \wedge q", r"(\neg p)", r"p \wedge q", r"(p \to \neg)", r"\bot\bot"]:
    assert not is_formula(tok(s)), s
for s in ["p", r"\bot", r"\neg\neg q", r"((p \wedge \neg q) \to p)", r"\neg(p \to \bot)", r"(p \wedge q)"]:
    assert is_formula(tok(s)), s
assert len(tok(r"p \wedge \to q")) == 4
# the formation sequences quoted in exm-formation-sequences: every entry built from earlier ones
seq = [tok(x) for x in ["p", "q", r"\neg q", r"(p \wedge \neg q)", r"((p \wedge \neg q) \to p)"]]
assert all(is_formula(x) for x in seq)
print("exm-not-formulas: all quoted values check")
