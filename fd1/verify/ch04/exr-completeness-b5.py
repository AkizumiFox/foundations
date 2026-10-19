"""exr-completeness-b5 (Section 4.8, Consistent or not): (a), (b) unsatisfiable, (c) made
true by the all-F row; (a)'s derivation by tools/check_fitch.py on a capital-letter copy;
(b)'s search: under (p, q) and under (not p, not q) the remaining disjunction closes."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L
import _s0708_lib as H

lists = [[r"p \to q", r"q \to r", "p", r"\neg r"],
         [r"p \vee q", r"\neg p \vee \neg q", r"p \leftrightarrow q"],
         [r"p \to \neg q", r"q \to \neg r", r"r \to \neg p"]]
sat = [not not [r for r in L.rows(["p", "q", "r"]) if all(L.val(L.parse(f), r) for f in g)] for g in lists]
assert sat == [False, False, True]
allf = {"p": False, "q": False, "r": False}
assert all(L.val(L.parse(f), allf) for f in lists[2])
for row in ({"p": True, "q": True}, {"p": False, "q": False}):
    assert not (L.val(L.parse(r"\neg p \vee \neg q"), row) and L.val(L.parse(r"p \vee q"), row))
H.check(H.block(H.S08, "exr-completeness-b5"), derivations=1)
print("exr-completeness-b5: all quoted values check")
