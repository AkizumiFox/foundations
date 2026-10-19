"""exm-taut-step and the TAUT subsection (Section 4.8): the premise not(p -> q) is true only
at p = T, q = F, where p and not q is true; the TAUT derivation and the twelve-line
derivation of the fold, by tools/check_fitch.py on a capital-letter copy (the copy checks
the TAUT line by its table); the Quick check and the Not-allowed rows."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L
import _s0708_lib as H

QUOTED = {"lines written out": 12}
rows = [L.tv(r, "p", "q") for r in L.rows(["p", "q"]) if L.val(L.parse(r"\neg(p \to q)"), r)]
assert rows == [(True, False)]
assert not L.entails([r"\neg(p \to q)"], r"p \wedge \neg q")
ex = H.block(H.S08, "exm-taut-step")
fold = H.between(H.S08, 'title="The step written out"', "::: {.check}")
H.check(ex, derivations=2)
H.check(fold, derivations=1)
assert len(H.boxes(fold)) == 3 and "\\raa" in fold
import re
assert max(int(x) for x in re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", fold)) == QUOTED["lines written out"]
# Quick check: p or q, p -> r |= r or q
assert not L.entails([r"p \vee q", r"p \to r"], r"r \vee q")
# Not allowed (1): p -> q |/= q -> p at (F, T); (4) is legal: p -> q, not q |= not p
assert (False, True) in [L.tv(r, "p", "q") for r in L.entails([r"p \to q"], r"q \to p")]
assert not L.entails([r"p \to q", r"\neg q"], r"\neg p")
print("exm-taut-step: all quoted values check")
