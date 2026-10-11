"""exr-valuations-and-truth-tables-a1 (Section 3.3)."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"rows for p, q, r, s": 16}
# (a) not(p and not q) has the column of p -> q
assert L.equivalent(r"\neg(p \wedge \neg q)", r"p \to q")
assert [L.tv(r, "p", "q") for r in L.false_rows(r"(p \vee q) \to p")] == [(False, True)]
# (b) p <-> not p is false in both rows
assert len(L.false_rows(r"p \leftrightarrow \neg p")) == 2
# (c) true under every valuation
assert not L.false_rows(r"(p \to \bot) \vee (\bot \to p)")
# (d)
assert 2 ** 4 == QUOTED["rows for p, q, r, s"]
# (e) p -> (q -> p) is a tautology
assert not L.false_rows(r"p \to (q \to p)")
print("exr-valuations-and-truth-tables-a1: all quoted values check")
