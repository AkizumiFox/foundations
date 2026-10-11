"""exm-backwards-from-f (Section 3.3): the only row making (p -> q) -> (p -> (q and r))
false is p = T, q = T, r = F, out of 8 rows."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"rows": 8, "false rows": 1}
fr = L.false_rows(r"(p \to q) \to (p \to (q \wedge r))")
assert [L.tv(r, "p", "q", "r") for r in fr] == [(True, True, False)]
assert len(fr) == QUOTED["false rows"] and len(list(L.rows("pqr"))) == QUOTED["rows"]
print("exm-backwards-from-f: all quoted values check")
