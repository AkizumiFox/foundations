"""exm-three-premise-entailment (Section 3.4): p or q, p -> r, q -> s |= r or s, over the
16 rows of four atoms."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"rows": 16}
assert not L.entails([r"p \vee q", r"p \to r", r"q \to s"], r"r \vee s")
assert len(list(L.rows("pqrs"))) == QUOTED["rows"]
print("exm-three-premise-entailment: all quoted values check")
