"""exm-grouping-of-implications (Section 3.4): (p -> q) -> r |= p -> (q -> r), and the
converse fails exactly in the rows p = r = F (q either value)."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"refuting rows": 2}
assert not L.entails([r"(p \to q) \to r"], r"p \to (q \to r)")
ref = L.entails([r"p \to (q \to r)"], r"(p \to q) \to r")
assert sorted(L.tv(r, "p", "q", "r") for r in ref) == [(False, False, False), (False, True, False)]
assert len(ref) == QUOTED["refuting rows"]
print("exm-grouping-of-implications: all quoted values check")
