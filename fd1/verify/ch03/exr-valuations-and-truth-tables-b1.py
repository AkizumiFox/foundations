"""exr-valuations-and-truth-tables-b1 (Section 3.3): the false rows of four formulas; and B3."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"(c) false rows": 2, "(d) false rows": 2}
assert not L.false_rows(r"((p \vee q) \wedge ((p \to r) \wedge (q \to r))) \to r")
assert not L.false_rows(r"(p \to (q \to r)) \to ((p \to q) \to (p \to r))")
c = [L.tv(r, "p", "q", "r") for r in L.false_rows(r"((p \to r) \vee (q \to r)) \to ((p \vee q) \to r)")]
assert c == [(True, False, False), (False, True, False)] and len(c) == QUOTED["(c) false rows"]
d = [L.tv(r, "p", "q", "r") for r in L.false_rows(r"((p \to q) \wedge (q \to r)) \to (r \to p)")]
assert d == [(False, True, True), (False, False, True)] and len(d) == QUOTED["(d) false rows"]
# B3: disjunctive syllogism as a tautology
assert not L.false_rows(r"((p \vee q) \wedge \neg p) \to q")
print("exr-valuations-and-truth-tables-b1: all quoted values check")
