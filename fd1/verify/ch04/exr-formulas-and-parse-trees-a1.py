"""exr-formulas-and-parse-trees-a1 (Ch 3, Section 3.1): formula or not; subformulas and height."""
from _s0102_formulas import tok, is_formula, height, subformulas

QUOTED = {"(b) subformulas": "five, with \\( q \\) listed once", "(b) height": "so the height is \\( 4 \\)"}

verdict = {
    r"(p \vee \bot)": True, r"\neg\neg p": True, r"(p \neg q)": False,
    r"((p \to q))": False, r"(p \wedge q \wedge r)": False, r"\to p": False,
}
for s, v in verdict.items():
    assert is_formula(tok(s)) == v, s
f = tok(r"(\neg(p \to q) \vee q)")
assert len(subformulas(f)) == 5 and height(f) == 4
# (c): every proper subformula has smaller height, on all formulas up to length 11
from _s0102_formulas import all_formulas
for g in all_formulas(11):
    assert all(height(h) < height(g) for h in subformulas(g) if h != g)
print("exr-formulas-and-parse-trees-a1: all quoted values check")
