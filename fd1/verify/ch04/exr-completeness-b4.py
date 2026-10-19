"""exr-completeness-b4 (Section 4.8): the TAUT version and the primitive version of
p -> (q and r), not r |- not p, by tools/check_fitch.py on a capital-letter copy (the TAUT
line by its table); (c): not(p and not q) and p -> q are equivalent, false exactly at (T, F)."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L
import _s0708_lib as H

assert not L.entails([r"p \to (q \wedge r)", r"\neg r"], r"\neg p")
H.check(H.block(H.S08, "exr-completeness-b4"), derivations=2)
assert L.equivalent(r"\neg(p \wedge \neg q)", r"p \to q")
assert [L.tv(r, "p", "q") for r in L.false_rows(r"p \to q")] == [(True, False)]
assert [L.tv(r, "p", "q") for r in L.false_rows(r"\neg(p \wedge \neg q)")] == [(True, False)]
print("exr-completeness-b4: all quoted values check")
