"""exm-value-down-the-tree and the Quick check after it (Section 3.3); the warning's row
(not(p and q) vs not p and not q at p = T, q = F); the coincidence Quick check."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"example value": True, "quick check value": False}
v = {"p": False, "q": True, "r": False}
assert L.val(L.parse(r"p \vee \neg q"), v) is False
assert L.val(L.parse(r"q \wedge r"), v) is False
assert L.val(L.parse(r"(p \vee \neg q) \to (q \wedge r)"), v) is QUOTED["example value"]
w = {"p": False, "q": True, "r": True}
assert L.val(L.parse(r"(p \vee q) \to \neg r"), w) is QUOTED["quick check value"]
x = {"p": True, "q": False}
assert L.val(L.parse(r"\neg(p \wedge q)"), x) and not L.val(L.parse(r"\neg p \wedge \neg q"), x)
# coincidence quick check: p -> (q or p) is a tautology
assert not L.false_rows(r"p \to (q \vee p)")
print("exm-value-down-the-tree: all quoted values check")
