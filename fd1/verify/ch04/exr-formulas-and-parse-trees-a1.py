"""exr-formulas-and-parse-trees-a1 (Ch 4, Section 4.1): formula or not; subformulas;
a formation sequence listing (p or q) once."""
from _s0102_formulas import tok, is_formula, subformulas

QUOTED = {"(b) subformulas": "five, with \\( q \\) listed once"}

verdict = {
    r"(p \vee \bot)": True, r"\neg\neg p": True, r"(p \neg q)": False,
    r"((p \to q))": False, r"(p \wedge q \wedge r)": False, r"\to p": False,
}
for s, v in verdict.items():
    assert is_formula(tok(s)) == v, s
f = tok(r"(\neg(p \to q) \vee q)")
assert len(subformulas(f)) == 5
assert subformulas(f) == {tok(s) for s in [r"(\neg(p \to q) \vee q)", r"\neg(p \to q)", r"(p \to q)", "p", "q"]}
# (c): the sequence is checked entry by entry in exm-not-formulas.py; here: (p or q) occurs once in it
seq = [tok(s) for s in ["p", "q", r"(p \vee q)", r"\neg(p \vee q)", r"((p \vee q) \wedge \neg(p \vee q))"]]
assert seq.count(tok(r"(p \vee q)")) == 1 and all(is_formula(x) for x in seq)
print("exr-formulas-and-parse-trees-a1: all quoted values check")
